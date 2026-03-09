---
name: quartus-agent
description: Manage Intel Quartus FPGA projects — synthesis, pin assignment, timing constraints, and compilation to bitstream. Use this skill when the user asks to "synthesize", "assign pins", "compile to bitstream", "generate .sof", "timing closure", or perform any FPGA physical implementation task.
---

# Quartus Agent — Synthesis, Place & Route, Implementation

This skill handles Intel Quartus Prime project management, pin assignments, timing constraints (SDC), and full compilation flows. All operations run via Quartus CLI tools; never launch the Quartus GUI.

> [!NOTE]
> This skill follows the unified workspace convention defined in [`SHARED_WORKSPACE.md`](file:///c:/skills-main/skills-main/skills/SHARED_WORKSPACE.md). Read it for directory ownership, file formats, and handoff protocols.

## Workflow

Follow this order for every implementation cycle:

0. **Check Simulation Status** — Read `sim/sim_result.json` and verify `status` is `"PASS"` before proceeding. If missing or `"FAIL"`, refuse and instruct the user to fix simulation first.
1. **Create / Update Project** — Generate or modify `.qpf` and `.qsf` files.
2. **Assign Pins** — Add pin location assignments to the `.qsf`.
3. **Create Timing Constraints** — Write an `.sdc` file for clock definitions and timing requirements.
4. **Run Compilation** — Execute the full flow (Analysis & Synthesis → Fitter → Assembler → Timing Analyzer).
5. **Analyze Reports** — Use `extract_rpt.py` to parse compilation results.
6. **Write Handoff** — Save filtered report to `syn/reports/compile_result.json`.

## Project Setup

### `.qpf` (Quartus Project File)
Minimal project file:
```tcl
QUARTUS_VERSION = "21.1"
PROJECT_REVISION = "top"
```

### `.qsf` (Quartus Settings File)
Key settings to always include:
```tcl
set_global_assignment -name FAMILY "<device_family>"
set_global_assignment -name DEVICE <device_part_number>
set_global_assignment -name TOP_LEVEL_ENTITY <top_module>
set_global_assignment -name VERILOG_FILE src/<file>.v

# Pin assignments
set_location_assignment PIN_xx -to <port_name>
set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to <port_name>
```

## Pin Assignment Rules

- Always specify `IO_STANDARD` alongside `set_location_assignment`.
- Use the device's pin-out documentation to verify valid pin numbers.
- Group related pins (clock, reset, data bus) for clarity.

## Timing Constraints (SDC)

Every project **must** have an SDC file. Minimum contents:

```tcl
# Primary clock definition
create_clock -name clk -period <period_ns> [get_ports {clk}]

# Input/output delay constraints
set_input_delay -clock clk -max <ns> [get_ports {data_in[*]}]
set_output_delay -clock clk -max <ns> [get_ports {data_out[*]}]
```

Register the SDC file in the `.qsf`:
```tcl
set_global_assignment -name SDC_FILE constraints/timing.sdc
```

## Error Handling

> [!CAUTION]
> If the synthesis report shows an **inferred latch**, treat it as an RTL bug. Return to the `modelsim-agent` to fix the Verilog source — do NOT attempt to constrain around it.

> [!WARNING]
> **Multiple Driver** errors indicate conflicting assignments to the same signal. These must be resolved at the RTL level.

Common issues to watch for:
- **Inferred latches** → incomplete `if`/`case` in combinational blocks.
- **Multiple drivers** → signal driven from more than one `always` block.
- **Unconstrained clocks** → missing SDC `create_clock`.
- **Hold time violations** → may need clock domain crossing treatment.

## Using the Helper Scripts

### Build Project (`scripts/build_project.py`)

Generate project files from a specification:

```bash
python scripts/build_project.py \
    --name my_project \
    --family "Cyclone IV E" \
    --device EP4CE22F17C6 \
    --top top_module \
    --src src/top.v src/sub.v \
    --sdc constraints/timing.sdc \
    --pins "clk:PIN_R8,rst_n:PIN_J15,led[0]:PIN_A15"
```

### Run Compilation (`scripts/run_compile.py`)

Execute the full Quartus compilation flow:

```bash
python scripts/run_compile.py --project my_project --cwd syn/
```

This calls `quartus_sh --flow compile <project_name>`. Do **not** open the GUI.

### Extract Reports (`scripts/extract_rpt.py`)

Parse Quartus report files and extract key metrics:

```bash
# Print to console
python scripts/extract_rpt.py --project my_project --cwd syn/

# Save filtered report as JSON for handoff
python scripts/extract_rpt.py --project my_project --cwd syn/ --output syn/reports/compile_result.json
```

Extracts:
- **Resource usage** — ALMs, Registers, Block RAM bits, DSP blocks
- **Errors and critical warnings**
- **Timing summary** — Fmax, setup/hold slack, violations

> [!IMPORTANT]
> Never send raw `.rpt` files to the LLM. They can be hundreds of thousands of lines. Always use `extract_rpt.py` to filter first.

## Shared Workspace & Handoff

See [`SHARED_WORKSPACE.md`](file:///c:/skills-main/skills-main/skills/SHARED_WORKSPACE.md) for the complete specification.

Key points for this skill:
- **Before compilation**: Read `sim/sim_result.json` — only proceed if `status` is `"PASS"`.
- Write Quartus project files to `syn/`, SDC files to `constraints/`.
- After compilation, save filtered report to `syn/reports/compile_result.json` using `extract_rpt.py --output`.
- Do NOT modify `src/` (RTL source) or `sim/` (simulation workspace) — those are owned by `modelsim-agent`.
- If synthesis reveals RTL bugs (inferred latches, multiple drivers), hand back to `modelsim-agent`.
