#!/usr/bin/env python3
"""
build_project.py — Generate Quartus .qpf and .qsf project files.

Usage:
    python build_project.py \
        --name my_project \
        --family "Cyclone IV E" \
        --device EP4CE22F17C6 \
        --top top_module \
        --src src/top.v src/sub.v \
        --sdc constraints/timing.sdc \
        --pins "clk:PIN_R8,rst_n:PIN_J15,led[0]:PIN_A15"
"""

import argparse
import sys
from pathlib import Path


def generate_qpf(project_name: str) -> str:
    """Generate a minimal .qpf file."""
    return (
        f'QUARTUS_VERSION = "21.1"\n'
        f'DATE = "auto"\n'
        f'PROJECT_REVISION = "{project_name}"\n'
    )


def parse_pin_string(pin_str: str) -> list[tuple[str, str]]:
    """Parse 'port:PIN_XX,port2:PIN_YY' into [(port, pin), ...]."""
    pins = []
    if not pin_str:
        return pins
    for pair in pin_str.split(","):
        pair = pair.strip()
        if ":" not in pair:
            print(f"WARNING: Skipping invalid pin spec '{pair}' (expected port:PIN_XX)")
            continue
        port, pin = pair.split(":", 1)
        pins.append((port.strip(), pin.strip()))
    return pins


def generate_qsf(
    project_name: str,
    family: str,
    device: str,
    top_entity: str,
    source_files: list[str],
    sdc_file: str | None = None,
    pins: list[tuple[str, str]] | None = None,
    io_standard: str = "3.3-V LVTTL",
) -> str:
    """Generate a .qsf settings file."""
    lines = [
        f'set_global_assignment -name FAMILY "{family}"',
        f"set_global_assignment -name DEVICE {device}",
        f"set_global_assignment -name TOP_LEVEL_ENTITY {top_entity}",
        f'set_global_assignment -name PROJECT_OUTPUT_DIRECTORY output_files',
        "",
        "# Source files",
    ]

    for src in source_files:
        lines.append(f"set_global_assignment -name VERILOG_FILE {src}")

    if sdc_file:
        lines.append("")
        lines.append("# Timing constraints")
        lines.append(f"set_global_assignment -name SDC_FILE {sdc_file}")

    if pins:
        lines.append("")
        lines.append("# Pin assignments")
        for port, pin in pins:
            lines.append(f"set_location_assignment {pin} -to {port}")
            lines.append(
                f'set_instance_assignment -name IO_STANDARD "{io_standard}" -to {port}'
            )

    lines.append("")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate Quartus .qpf and .qsf project files."
    )
    parser.add_argument("--name", required=True, help="Project name.")
    parser.add_argument(
        "--family", required=True, help='FPGA family (e.g., "Cyclone IV E").'
    )
    parser.add_argument(
        "--device", required=True, help="Device part number (e.g., EP4CE22F17C6)."
    )
    parser.add_argument("--top", required=True, help="Top-level entity name.")
    parser.add_argument(
        "--src", nargs="+", required=True, help="Verilog source files."
    )
    parser.add_argument("--sdc", default=None, help="SDC timing constraints file.")
    parser.add_argument(
        "--pins",
        default="",
        help='Pin assignments as "port:PIN_XX,port2:PIN_YY".',
    )
    parser.add_argument(
        "--io-standard",
        default="3.3-V LVTTL",
        help='I/O standard (default: "3.3-V LVTTL").',
    )
    parser.add_argument(
        "--output-dir",
        default=".",
        help="Directory to write project files (default: current dir).",
    )

    args = parser.parse_args()

    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    pin_list = parse_pin_string(args.pins)

    # Write .qpf
    qpf_path = out_dir / f"{args.name}.qpf"
    qpf_content = generate_qpf(args.name)
    qpf_path.write_text(qpf_content, encoding="utf-8")
    print(f"[build_project] Created {qpf_path}")

    # Write .qsf
    qsf_path = out_dir / f"{args.name}.qsf"
    qsf_content = generate_qsf(
        project_name=args.name,
        family=args.family,
        device=args.device,
        top_entity=args.top,
        source_files=args.src,
        sdc_file=args.sdc,
        pins=pin_list,
        io_standard=args.io_standard,
    )
    qsf_path.write_text(qsf_content, encoding="utf-8")
    print(f"[build_project] Created {qsf_path}")


if __name__ == "__main__":
    main()
