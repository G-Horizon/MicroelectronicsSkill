# FPGA Agent Skills Development Guide

This guide outlines the architecture and implementation details for creating two AI agent skills for FPGA development: `modelsim-agent` and `quartus-agent`.

## 1. modelsim-agent (Logic Simulation & Verification)

**Purpose:** Writing Verilog code, generating testbenches, and running simulations.

### Directory Structure:
```
skills/modelsim-agent/
├── SKILL.md                 # Main instructions and prompt constraints
├── scripts/
│   ├── run_sim.py          # Wrapper for 'vsim' CLI
│   └── parse_sim_log.py    # Log parser to extract errors/assertions
└── templates/              # Optional testbench templates
```

### Core Components:

#### SKILL.md Constraints:
*   **Trigger:** Activate when asked to "write Verilog", "simulate", "create testbench", "verify logic".
*   **Coding Standards:**
    *   Use non-blocking assignments (`<=`) for sequential logic.
    *   Use blocking assignments (`=`) for combinational logic.
*   **Testbench Requirements:**
    *   **CRITICAL:** Every testbench *must* contain a `$finish;` or `$stop;` statement to prevent infinite simulation loops.
    *   Use `$display`, `$monitor`, or `$error` to print explicit success/failure messages rather than relying on waveform (GUI) inspection.

#### Scripts Implementation:
*   **`run_sim.py`**:
    *   Must execute ModelSim in CLI mode (headless): `vsim -c -do "run -all; quit" work.tb_module`
    *   Handle compilation (`vlog`) before simulation.
*   **`parse_sim_log.py`**:
    *   The LLM cannot read `.wlf` files or 10,000-line logs.
    *   This script must parse the simulation output and extract *only*: Syntax errors, `$display` outputs, assertion failures.

---

## 2. quartus-agent (Synthesis, Place & Route, Implementation)

**Purpose:** Project management, pin assignments, timing constraints, and synthesis/compilation.

### Directory Structure:
```
skills/quartus-agent/
├── SKILL.md                 # Main instructions and workflow
├── scripts/
│   ├── build_project.py    # Generates .qpf and .qsf files
│   ├── run_compile.py      # Wrapper for 'quartus_sh'
│   └── extract_rpt.py      # Parses complex compilation reports
└── constraints/            # Scripts to handle .sdc generation
```

### Core Components:

#### SKILL.md Constraints:
*   **Trigger:** Activate for "synthesis", "pin assignment", "timing closure", "compile to bitstream", "generate .sof".
*   **Workflow:**
    1.  Create/Update Project files (`.qpf`, `.qsf`).
    2.  Assign Pins (via `.qsf` commands).
    3.  Create Timing Constraints (`.sdc`).
    4.  Run Compilation.
*   **Error Handling:**
    *   If the synthesis report shows `inferred latch`, treat it as a coding bug and return to RTL editing.
    *   Watch out for "Multiple Driver" errors.

#### Scripts Implementation:
*   **`run_compile.py`**:
    *   Execute full flow via CLI: `quartus_sh --flow compile <project_name>`
    *   Do *not* attempt to open the Quartus GUI.
*   **`extract_rpt.py` (CRITICAL)**:
    *   Quartus generates massive report files (`.rpt`).
    *   This script *must* filter the reports using regex/parsing out only:
        *   Resource Usage (ALMs, Registers, Block RAM).
        *   Errors and Critical Warnings.
        *   Timing Summary (Fmax, Setup/Hold violations).
    *   Sending unfiltered `.rpt` files directly to the LLM will exhaust context limits.

---

## Architecture Synergy

*   **Shared Workspace:** Both skills should operate on the same local directory structure (e.g., `src/` for RTL, `sim/` for testbenches, `syn/` for Quartus project).
*   **Clear Boundaries:** The `modelsim-agent` writes and tests the RTL. Only when simulation passes should the `quartus-agent` take over for physical implementation.
