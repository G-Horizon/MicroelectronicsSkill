#!/usr/bin/env python3
"""
plot_waveform.py — Parse VCD files and render digital waveform diagrams.

Features:
  - Pure-Python VCD parser (no third-party VCD library needed)
  - Renders digital signals (1-bit) as step waveforms
  - Renders multi-bit buses as hex-annotated bands
  - Supports signal selection and time range filtering
  - Outputs PNG or SVG to sim/waveforms/

Usage:
    python plot_waveform.py --vcd sim/tb_module.vcd
    python plot_waveform.py --vcd sim/tb_module.vcd --signals clk rst_n counter --start 0 --end 500
    python plot_waveform.py --vcd sim/tb_module.vcd --output sim/waveforms/result.svg
    python plot_waveform.py --demo
"""

import argparse
import os
import re
import sys
from collections import OrderedDict
from dataclasses import dataclass, field
from pathlib import Path

try:
    import matplotlib
    matplotlib.use("Agg")                           
    import matplotlib.pyplot as plt
    import matplotlib.patches as mpatches
    from matplotlib.collections import PatchCollection
except ImportError:
    print(
        "ERROR: matplotlib is required. Install with: pip install matplotlib",
        file=sys.stderr,
    )
    sys.exit(1)


                                                                             
            
                                                                             

@dataclass
class VCDSignal:
    """Metadata for a signal in the VCD file."""
    id_code: str
    name: str
    width: int
    scope: str
    full_name: str              


@dataclass
class VCDData:
    """Parsed VCD contents."""
    signals: dict[str, VCDSignal] = field(default_factory=dict)                     
    timescale: str = "1ns"
    changes: list[tuple[int, str, str]] = field(default_factory=list)                          


def parse_vcd(filepath: Path) -> VCDData:
    """Parse a VCD file and return structured data."""
    data = VCDData()
    current_scope = []
    current_time = 0

    text = filepath.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()

    i = 0
    while i < len(lines):
        line = lines[i].strip()

                   
        if line.startswith("$timescale"):
            ts_parts = []
            while "$end" not in line:
                ts_parts.append(line)
                i += 1
                line = lines[i].strip()
            ts_text = " ".join(ts_parts).replace("$timescale", "").strip()
            data.timescale = ts_text
            i += 1
            continue

               
        if line.startswith("$scope"):
            parts = line.split()
            if len(parts) >= 3:
                current_scope.append(parts[2])
            i += 1
            continue

        if line.startswith("$upscope"):
            if current_scope:
                current_scope.pop()
            i += 1
            continue

                             
        if line.startswith("$var"):
            parts = line.split()
                                    
            if len(parts) >= 5:
                var_type = parts[1]
                width = int(parts[2])
                id_code = parts[3]
                name = parts[4]
                scope_str = ".".join(current_scope)
                full_name = f"{scope_str}.{name}" if scope_str else name
                data.signals[id_code] = VCDSignal(
                    id_code=id_code,
                    name=name,
                    width=width,
                    scope=scope_str,
                    full_name=full_name,
                )
            i += 1
            continue

                   
        if line.startswith("#"):
            try:
                current_time = int(line[1:])
            except ValueError:
                pass
            i += 1
            continue

                                                             
        m = re.match(r"^([01xXzZ])(.+)$", line)
        if m:
            value = m.group(1)
            id_code = m.group(2)
            data.changes.append((current_time, id_code, value))
            i += 1
            continue

                                                     
        m = re.match(r"^[bB]([01xXzZ]+)\s+(.+)$", line)
        if m:
            value = m.group(1)
            id_code = m.group(2)
            data.changes.append((current_time, id_code, value))
            i += 1
            continue

        i += 1

    return data


                                                                             
                    
                                                                             

              
COLORS = {
    "background":    "#1e1e2e",
    "grid":          "#313244",
    "text":          "#cdd6f4",
    "label":         "#89b4fa",
    "signal_high":   "#a6e3a1",
    "signal_low":    "#a6e3a1",
    "signal_bus":    "#89b4fa",
    "bus_fill":      "#89b4fa22",
    "bus_text":      "#cdd6f4",
    "time_marker":   "#f38ba8",
    "title":         "#cba6f7",
}


def build_waveform_data(
    vcd: VCDData,
    signal_names: list[str] | None = None,
    t_start: int | None = None,
    t_end: int | None = None,
) -> dict[str, list[tuple[int, str]]]:
    """
    Build per-signal time-value lists from VCD changes.
    Returns {full_name: [(time, value), ...]}.
    """
                                        
    id_to_name = {s.id_code: s.full_name for s in vcd.signals.values()}
    name_to_id = {s.full_name: s.id_code for s in vcd.signals.values()}
                                       
    short_to_id = {s.name: s.id_code for s in vcd.signals.values()}

                                        
    if signal_names:
        selected_ids = set()
        for sn in signal_names:
            if sn in name_to_id:
                selected_ids.add(name_to_id[sn])
            elif sn in short_to_id:
                selected_ids.add(short_to_id[sn])
            else:
                                                                       
                for sig in vcd.signals.values():
                    if sn.lower() in sig.full_name.lower() or sn.lower() in sig.name.lower():
                        selected_ids.add(sig.id_code)
    else:
        selected_ids = set(vcd.signals.keys())

                                
    waves: dict[str, list[tuple[int, str]]] = OrderedDict()
    for id_code in selected_ids:
        if id_code in id_to_name:
            waves[id_to_name[id_code]] = []

    for time, id_code, value in vcd.changes:
        if id_code not in selected_ids:
            continue
        if t_start is not None and time < t_start:
            continue
        if t_end is not None and time > t_end:
            continue
        name = id_to_name.get(id_code)
        if name and name in waves:
            waves[name].append((time, value))

    return waves


def render_waveform(
    waves: dict[str, list[tuple[int, str]]],
    vcd: VCDData,
    output_path: Path,
    title: str = "Simulation Waveform",
    t_start: int | None = None,
    t_end: int | None = None,
) -> None:
    """Render waveforms to an image file using matplotlib."""
    if not waves:
        print("[plot_waveform] WARNING: No signals to render.", file=sys.stderr)
        return

                          
    all_times = set()
    for changes in waves.values():
        for t, _ in changes:
            all_times.add(t)
    if not all_times:
        print("[plot_waveform] WARNING: No signal transitions found.", file=sys.stderr)
        return

    if t_start is None:
        t_start = min(all_times)
    if t_end is None:
        t_end = max(all_times)

                                   
    t_margin = max(1, (t_end - t_start) * 0.05)
    t_plot_end = t_end + t_margin

    n_signals = len(waves)
    row_height = 1.0
    fig_height = max(3, n_signals * row_height + 1.5)
    fig_width = max(10, min(20, (t_end - t_start) / 50 + 6))

    fig, axes = plt.subplots(
        n_signals, 1,
        figsize=(fig_width, fig_height),
        sharex=True,
        squeeze=False,
    )
    fig.patch.set_facecolor(COLORS["background"])
    fig.suptitle(title, color=COLORS["title"], fontsize=14, fontweight="bold", y=0.98)

    signal_names = list(waves.keys())

    for idx, (sig_name, changes) in enumerate(waves.items()):
        ax = axes[idx, 0]
        ax.set_facecolor(COLORS["background"])
        sig = None
                              
        for s in vcd.signals.values():
            if s.full_name == sig_name:
                sig = s
                break

        is_bus = sig is not None and sig.width > 1

        if is_bus:
            _draw_bus_waveform(ax, changes, t_start, t_plot_end, sig.width)
        else:
            _draw_digital_waveform(ax, changes, t_start, t_plot_end)

               
        display_name = sig.name if sig else sig_name.split(".")[-1]
        ax.set_ylabel(
            display_name,
            color=COLORS["label"],
            fontsize=10,
            fontweight="bold",
            rotation=0,
            labelpad=60,
            ha="right",
            va="center",
        )

                 
        ax.set_xlim(t_start, t_plot_end)
        ax.tick_params(axis="x", colors=COLORS["text"], labelsize=8)
        ax.tick_params(axis="y", left=False, labelleft=False)
        for spine in ax.spines.values():
            spine.set_visible(False)

              
        ax.grid(True, axis="x", color=COLORS["grid"], linewidth=0.5, alpha=0.5)

                                
    axes[-1, 0].set_xlabel(
        f"Time ({vcd.timescale})",
        color=COLORS["text"],
        fontsize=10,
    )

    plt.tight_layout(rect=[0.08, 0.02, 0.98, 0.95])

          
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(str(output_path), dpi=150, facecolor=fig.get_facecolor(), edgecolor="none")
    plt.close(fig)
    print(f"[plot_waveform] Waveform saved to {output_path}")


def _draw_digital_waveform(ax, changes, t_start, t_end):
    """Draw a 1-bit digital signal as a step waveform."""
    if not changes:
        ax.set_ylim(-0.2, 1.4)
        return

    times = []
    values = []
    for t, v in sorted(changes):
        if v in ("1",):
            val = 1
        elif v in ("0",):
            val = 0
        else:
            val = 0.5          
        times.append(t)
        values.append(val)

                               
    plot_times = [t_start] + times + [t_end]
    plot_values = [values[0]] + values + [values[-1]]

    ax.step(
        plot_times, plot_values,
        where="post",
        color=COLORS["signal_high"],
        linewidth=1.5,
    )
    ax.fill_between(
        plot_times, plot_values,
        step="post",
        alpha=0.1,
        color=COLORS["signal_high"],
    )
    ax.set_ylim(-0.2, 1.4)


def _draw_bus_waveform(ax, changes, t_start, t_end, width):
    """Draw a multi-bit bus as a hex-annotated band."""
    if not changes:
        ax.set_ylim(-0.2, 1.4)
        return

    sorted_changes = sorted(changes)
    patches = []
    texts = []

    for i, (t, v) in enumerate(sorted_changes):
                               
        if i + 1 < len(sorted_changes):
            t_next = sorted_changes[i + 1][0]
        else:
            t_next = t_end

                                                                                       
        seg_width = t_next - t
        if seg_width <= 0:
            continue

                           
        rect = mpatches.FancyBboxPatch(
            (t, 0.1), seg_width, 0.8,
            boxstyle="round,pad=0.02",
            facecolor=COLORS["bus_fill"],
            edgecolor=COLORS["signal_bus"],
            linewidth=1.2,
        )
        ax.add_patch(rect)

                                 
        try:
            int_val = int(v, 2)
            hex_str = f"0x{int_val:0{(width + 3) // 4}X}"
        except ValueError:
            hex_str = v              

        mid_t = t + seg_width / 2
        if seg_width > (t_end - t_start) * 0.03:                                        
            ax.text(
                mid_t, 0.5, hex_str,
                ha="center", va="center",
                color=COLORS["bus_text"],
                fontsize=7,
                fontfamily="monospace",
            )

    ax.set_ylim(-0.2, 1.4)


                                                                             
           
                                                                             

DEMO_VCD = """\
$timescale 1ns $end
$scope module tb_demo $end
$var wire 1 ! clk $end
$var wire 1 " rst_n $end
$var wire 4 # counter[3:0] $end
$upscope $end
$enddefinitions $end
$dumpvars
0!
0"
b0000 #
$end
#0
0!
0"
b0000 #
#5
1!
#10
0!
#15
1!
#20
0!
1"
#25
1!
b0001 #
#30
0!
#35
1!
b0010 #
#40
0!
#45
1!
b0011 #
#50
0!
#55
1!
b0100 #
#60
0!
#65
1!
b0101 #
#70
0!
#75
1!
b0110 #
#80
0!
#85
1!
b0111 #
#90
0!
#95
1!
b1000 #
#100
0!
#105
1!
b1001 #
#110
0!
#115
1!
b1010 #
#120
0!
"""


def run_demo(output_dir: Path) -> None:
    """Generate a demo waveform from built-in VCD data."""
    demo_vcd_path = output_dir / "demo.vcd"
    demo_vcd_path.parent.mkdir(parents=True, exist_ok=True)
    demo_vcd_path.write_text(DEMO_VCD, encoding="utf-8")

    vcd = parse_vcd(demo_vcd_path)
    waves = build_waveform_data(vcd)
    output_path = output_dir / "demo_waveform.png"
    render_waveform(waves, vcd, output_path, title="Demo: 4-bit Counter Waveform")

                       
    demo_vcd_path.unlink(missing_ok=True)
    print(f"[plot_waveform] Demo waveform generated at {output_path}")


                                                                             
      
                                                                             

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Parse VCD files and render waveform diagrams."
    )
    parser.add_argument(
        "--vcd",
        help="Path to the VCD file.",
    )
    parser.add_argument(
        "--signals",
        nargs="*",
        default=None,
        help="Signal names to display (default: all). Supports short names and fuzzy match.",
    )
    parser.add_argument(
        "--start",
        type=int,
        default=None,
        help="Start time for the waveform display.",
    )
    parser.add_argument(
        "--end",
        type=int,
        default=None,
        help="End time for the waveform display.",
    )
    parser.add_argument(
        "--output",
        default=None,
        help="Output image path (default: sim/waveforms/<vcd_basename>.png).",
    )
    parser.add_argument(
        "--title",
        default=None,
        help="Waveform diagram title.",
    )
    parser.add_argument(
        "--demo",
        action="store_true",
        help="Generate a demo waveform from built-in data.",
    )

    args = parser.parse_args()

    if args.demo:
        run_demo(Path("sim/waveforms"))
        return

    if not args.vcd:
        parser.error("--vcd is required (or use --demo for a demo).")

    vcd_path = Path(args.vcd)
    if not vcd_path.exists():
        print(f"ERROR: VCD file not found: {args.vcd}", file=sys.stderr)
        sys.exit(1)

           
    vcd = parse_vcd(vcd_path)
    print(f"[plot_waveform] Parsed {len(vcd.signals)} signals, {len(vcd.changes)} transitions.")

                         
    waves = build_waveform_data(vcd, signal_names=args.signals, t_start=args.start, t_end=args.end)
    print(f"[plot_waveform] Rendering {len(waves)} signal(s)...")

                           
    if args.output:
        output_path = Path(args.output)
    else:
        output_path = Path("sim/waveforms") / f"{vcd_path.stem}.png"

    title = args.title or f"Waveform: {vcd_path.stem}"

    render_waveform(waves, vcd, output_path, title=title, t_start=args.start, t_end=args.end)


if __name__ == "__main__":
    main()
