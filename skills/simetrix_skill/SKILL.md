---
name: SIMetrix Script Command Finder
description: Guides the AI on how to find and look up SIMetrix automation commands and functions from the manual directory.
---

# SIMetrix Automation Skill

This skill provides instructions on how to discover, look up, and use SIMetrix script commands and functions for automating the SIMetrix/SIMPLIS software.

## 📂 Documentation Location
All relevant SIMetrix script documentation is located here:
**`./SIMetrix_document/SIMetrix Script Manual`**

This directory is your single source of truth for the SIMetrix script language.

## 🔍 How to Find the Right Instruction

**Quick lookup**: For a fast reference of common component symbols (device letters) and their associated commands, see the [📜 Common Component Symbol Mapping](#-common-component-symbol-mapping) section below.

Whenever you need to automate a specific operation in SIMetrix (e.g., opening a schematic, probing a node, extracting simulation data), follow this workflow:

### Step 1: Browse the Summaries
Before guessing commands, consult the summary files to find the correct command or function for the job:

- **Commands** (for performing actions, such as `Run`, `OpenSchem`, `Close`):
  Read `./SIMetrix_document/SIMetrix Script Manual/Command Summary.md`
  
- **Functions** (for processing data, retrieving statuses, evaluating logic):
  Read `./SIMetrix_document/SIMetrix Script Manual/Function Summary.md`

### Step 2: Read the Detailed Manual
Once you have found a potential command or function in the summary table, you MUST check its exact syntax, arguments, and return types before using it.

- For **Commands**, look in the `Command Summary` folder.
  *Example: If you want to use the `Abort` command, read:*
  `./SIMetrix_document/SIMetrix Script Manual/Command Summary/Abort Command.md`

- For **Functions**, look in the `Function Summary` folder.
  *Example: If you need to use the `Abs` function, read:*
  `./SIMetrix_document/SIMetrix Script Manual/Function Summary/Abs Function.md`

*Note: Use the `view_file` tool to read these files and understand their arguments (often formatted with specific switches like `/switch`).*

## 📜 Common Component Symbol Mapping

When working with schematic components in SIMetrix/SIMPLIS scripts, each device type is identified by a single-letter **device letter** (used in netlists and model properties). The following table provides a quick reference for the most common component symbols, their corresponding device letters, and typical script commands/functions for manipulating them.

| Device Letter | Component Type | Description | Common Script Commands / Functions | Notes |
|---------------|----------------|-------------|-----------------------------------|-------|
| R | Resistor | Fixed or variable resistor | `Inst` (place), `SetComponentValue`, `Prop` | Value in ohms |
| C | Capacitor | Fixed or variable capacitor | `Inst` (place), `SetComponentValue`, `Prop` | Value in farads |
| L | Inductor | Fixed or variable inductor | `Inst` (place), `SetComponentValue`, `Prop` | Value in henries |
| D | Diode | Semiconductor diode | `Inst` (place), `CreateDiodeDialog`, `Prop` | Model name required |
| Q | Bipolar Junction Transistor (BJT) | NPN/PNP transistor | `Inst` (place), `Prop` | Model property "Q" |
| M | MOSFET | Metal‑oxide‑semiconductor FET | `Inst` (place), `Prop` | LEVEL parameter specifies model |
| J | JFET | Junction field‑effect transistor | `Inst` (place), `Prop` | |
| V | Independent Voltage Source | DC, AC, pulse, etc. | `Inst` (place), `Prop` | Value/type defined by properties |
| I | Independent Current Source | DC, AC, pulse, etc. | `Inst` (place), `Prop` | Value/type defined by properties |
| E | Voltage‑Controlled Voltage Source (VCVS) | Linear voltage‑controlled source | `Inst` (place), `Prop` | Gain defined by value |
| F | Current‑Controlled Current Source (CCCS) | Linear current‑controlled source | `Inst` (place), `Prop` | Gain defined by value |
| G | Voltage‑Controlled Current Source (VCCS) | Linear voltage‑controlled source | `Inst` (place), `Prop` | Transconductance defined by value |
| H | Current‑Controlled Voltage Source (CCVS) | Linear current‑controlled source | `Inst` (place), `Prop` | Transresistance defined by value |
| S | Voltage‑Controlled Switch | Ideal switch (SPICE S‑device) | `Inst` (place), `Prop` | Model required |
| W | Current‑Controlled Switch | Ideal switch (SPICE W‑device) | `Inst` (place), `Prop` | Model required |
| K | Mutual Inductance (Transformer) | Coupled inductors | `Inst` (place), `Prop` | Value = coupling coefficient |
| X | Subcircuit | User‑defined subcircuit block | `Inst` (place), `Prop` | Model property "X" |
| T | Transmission Line | Lossless/lossy transmission line | `Inst` (place), `Prop` | |
| O | Lossy Transmission Line | Lossy line (SIMetrix‑specific) | `Inst` (place), `Prop` | |
| B | Behavioral Source | Arbitrary behavioral source | `Inst` (place), `Prop` | Expression‑based |

**Notes:**
- The **model property** of a symbol must be set to the device letter (e.g., `AddProp model Q` for a BJT). This single‑letter code tells the simulator which device type to use.
- To place a component, use the `Inst` command (interactive unless `/loc` switch is given).
- To modify a component’s value or model, use the `Prop` command or the `SetComponentValue` function.
- For a complete, authoritative list of device letters and their corresponding simulator devices, consult the **Simulator Reference Manual** (mentioned in the “Summary of Simulator Devices” section of the User’s Manual). The `GetAllSimulatorDevices` function can also be called to retrieve the current device list programmatically.
- **Symbol names** (used with the `Inst` command) may differ from device letters. For example, a resistor symbol might be named `res`, `res_dig`, or `resistor`. Use the `GetSymbols()` function to list all installed symbols and their internal names. Common symbol names include `res` (resistor), `vsrc` or `avsrc` (voltage source), `gnd` (ground), `cap` (capacitor), `ind` (inductor).

## 💡 AI Implementation Guidelines

1. **Be Precise**: SIMetrix commands often require exact syntax, specific argument order, and slash-based switches. Do not guess the syntax; ALWAYS read the detailed markdown file for the command.
2. **Use Search**: If the summary files are long, use `grep_search` to look for keywords (e.g., "export", "netlist", "zoom") within the `./SIMetrix_document/SIMetrix Script Manual` directory.
3. **Execution**: To execute these commands and communicate with SIMetrix from Python, you MUST use the `simetrix_automation.py` program located in the same directory (`./simetrix_automation.py`). This script is the designated communication interface between Python and SIMetrix.
