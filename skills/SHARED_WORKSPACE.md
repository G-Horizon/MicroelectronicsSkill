# FPGA Skills — Shared Workspace Convention

This document defines the unified workspace structure and data exchange contracts used by all FPGA skills (`modelsim-agent`, `quartus-agent`, `waveform-viewer`).

**All skills MUST follow these conventions.** When referencing workspace layout in your own `SKILL.md`, point here instead of duplicating.

## Directory Structure

```
<project_root>/
├── src/                    # RTL source files (.v, .sv)
│   └── *.v / *.sv
├── sim/                    # Simulation workspace (owned by modelsim-agent)
│   ├── *.v                 # Testbench files
│   ├── *.vcd               # Value Change Dump (waveform data)
│   ├── *.log               # Raw simulation transcripts
│   ├── sim_result.json     # Simulation outcome handoff file
│   └── waveforms/          # Generated waveform images (owned by waveform-viewer)
│       └── *.png / *.svg
├── syn/                    # Synthesis workspace (owned by quartus-agent)
│   ├── *.qpf / *.qsf      # Quartus project files
│   ├── output_files/       # Quartus build outputs (.sof, .pof, .rpt)
│   └── reports/            # Filtered reports
│       └── compile_result.json
└── constraints/            # Timing constraint files (.sdc)
    └── *.sdc
```

## Ownership Rules

| Directory | Owner | Other skills |
|---|---|---|
| `src/` | **Shared** — `modelsim-agent` writes & tests, `quartus-agent` reads | All may read |
| `sim/` | `modelsim-agent` | `quartus-agent` reads `sim_result.json`; `waveform-viewer` reads `.vcd` |
| `sim/waveforms/` | `waveform-viewer` | All may read |
| `syn/` | `quartus-agent` | `modelsim-agent` should NOT modify |
| `constraints/` | `quartus-agent` | — |

## Handoff Protocol

### Simulation → Synthesis

After all simulations pass, `modelsim-agent` writes **`sim/sim_result.json`**:

```json
{
  "status": "PASS",
  "timestamp": "2026-02-24T01:00:00",
  "log_file": "sim/sim_output.log",
  "vcd_file": "sim/tb_module.vcd",
  "waveform_image": "sim/waveforms/tb_module.png",
  "summary": "All 5 test cases passed. No errors or warnings."
}
```

If simulation fails, `status` should be `"FAIL"` with error details in `summary`.

**`quartus-agent` MUST check `sim/sim_result.json`** before starting compilation:
- If `status` is `"PASS"` — proceed.
- If `status` is `"FAIL"` or the file is missing — refuse and instruct the user to fix simulation first.

### Synthesis → User

After compilation, `quartus-agent` writes **`syn/reports/compile_result.json`**:

```json
{
  "status": "SUCCESS",
  "timestamp": "2026-02-24T01:10:00",
  "resource_usage": {
    "Total logic elements": "150 / 22,320 (< 1%)",
    "Total registers": "48",
    "Total memory bits": "0"
  },
  "fmax": ["120.5 MHz"],
  "timing_violations": [],
  "errors": [],
  "critical_warnings": []
}
```

## Standard File Formats

| Format | Purpose | Producer | Consumer |
|---|---|---|---|
| `.vcd` | Waveform data (Value Change Dump) | Testbench via `$dumpfile` | `waveform-viewer` |
| `.log` | Raw simulation transcript | `run_sim.py` | `parse_sim_log.py` |
| `sim_result.json` | Simulation outcome | `modelsim-agent` | `quartus-agent` |
| `.rpt` | Raw Quartus reports | `quartus_sh` | `extract_rpt.py` |
| `compile_result.json` | Filtered compilation result | `extract_rpt.py` | User / other tools |
| `.png` / `.svg` | Waveform images | `waveform-viewer` | User |
