---
name: modelsim-agent
description: Write Verilog/SystemVerilog code, generate testbenches, and run ModelSim simulations. Use this skill when the user asks to "write Verilog", "simulate", "create testbench", "verify logic", or perform any RTL-level logic verification task.
---

# ModelSim Agent — Logic Simulation & Verification

This skill handles Verilog/SystemVerilog RTL coding, testbench generation, and ModelSim CLI-based simulation. All simulations run in headless (CLI) mode; never launch the ModelSim GUI.

> [!NOTE]
> This skill follows the unified workspace convention defined in [`SHARED_WORKSPACE.md`](file:///c:/skills-main/skills-main/skills/SHARED_WORKSPACE.md). Read it for directory ownership, file formats, and handoff protocols.

## Workflow

1. **Write RTL** — Create or modify Verilog source files under `src/`.
2. **Generate Testbench** — Create a testbench under `sim/` that exercises the design.
3. **Compile & Simulate** — Use `scripts/run_sim.py` to compile and run.
4. **Analyze Results** — Use `scripts/parse_sim_log.py` to extract errors/pass-fail.
5. **Visualize Waveform** *(optional)* — Hand off VCD file to the `waveform-viewer` skill for rendering.
6. **Write Handoff** — On success, `run_sim.py` generates `sim/sim_result.json` for `quartus-agent`.

## Coding Standards

Follow these rules strictly when writing Verilog/SystemVerilog:

- Use **non-blocking assignments** (`<=`) inside `always @(posedge clk)` blocks (sequential logic).
- Use **blocking assignments** (`=`) inside `always @(*)` blocks (combinational logic).
- Always provide a complete sensitivity list or use `always @(*)` / `always_comb`.
- Avoid inferred latches — every `if` must have a matching `else`, every `case` must have a `default`.

## Testbench Requirements

> [!CAUTION]
> Every testbench **MUST** contain a `$finish;` or `$stop;` statement. Omitting this will cause an infinite simulation loop that hangs the CLI.

> [!IMPORTANT]
> Every testbench **MUST** include `$dumpfile` and `$dumpvars` to generate a VCD file for waveform visualization.

- Use `$display`, `$monitor`, or `$error` to print **explicit pass/fail messages** in the transcript.
- Do **not** rely on waveform (GUI) inspection for verification — but DO generate VCD for post-simulation waveform review.
- Include a clock generator and a reset sequence in every testbench.
- Add meaningful test scenarios with expected-vs-actual value checks.

Example skeleton:

```verilog
module tb_example;
    reg clk, rst_n;
    // ... DUT instantiation ...

    // --- VCD Dump (REQUIRED) ---
    initial begin
        $dumpfile("sim/tb_example.vcd");
        $dumpvars(0, tb_example);
    end

    // --- Clock Generator ---
    initial begin
        clk = 0;
        forever #5 clk = ~clk;
    end

    // --- Test Sequence ---
    initial begin
        rst_n = 0;
        #20 rst_n = 1;

        // --- Test cases ---
        // ...

        $display("=== ALL TESTS PASSED ===");
        $finish;
    end
endmodule
```

## Using the Helper Scripts

### Compile & Simulate (`scripts/run_sim.py`)

Run a simulation end-to-end:

```bash
python scripts/run_sim.py --src src/my_module.v --tb sim/tb_my_module.v --top tb_my_module
```

The script will:
1. Call `vlog` to compile all source and testbench files.
2. Call `vsim -c -do "run -all; quit" work.<top_module>` to simulate in CLI mode.
3. Capture the full transcript for parsing.
4. Generate `sim/sim_result.json` with status, log path, and VCD path.

### Parse Log (`scripts/parse_sim_log.py`)

Extract only actionable information from a simulation transcript:

```bash
python scripts/parse_sim_log.py --log sim_output.log
```

The parser extracts:
- **Syntax / compilation errors**
- **`$display` / `$monitor` output lines**
- **Assertion failures** (`$error`, `$fatal`, `assert`)

> [!IMPORTANT]
> Never send raw simulation logs directly to the LLM. Always use `parse_sim_log.py` first to stay within context limits.

### Visualize Waveform

Waveform rendering is handled by the separate **`waveform-viewer`** skill. After simulation completes, pass the generated VCD file (e.g., `sim/tb_example.vcd`) to that skill for visualization.

> [!TIP]
> The `$dumpfile` / `$dumpvars` statements in the testbench template ensure VCD files are always generated. The `waveform-viewer` skill reads these files and outputs images to `sim/waveforms/`.

## Shared Workspace & Handoff

See [`SHARED_WORKSPACE.md`](file:///c:/skills-main/skills-main/skills/SHARED_WORKSPACE.md) for the complete specification.

Key points for this skill:
- Write RTL to `src/`, testbenches to `sim/`.
- VCD files go to `sim/` (consumed by `waveform-viewer`).
- After simulation passes, `sim/sim_result.json` is the **handoff artifact** to `quartus-agent`.
- Do NOT modify `syn/` or `constraints/` — those belong to `quartus-agent`.
- Only hand off to `quartus-agent` for synthesis **after** all simulations pass.
