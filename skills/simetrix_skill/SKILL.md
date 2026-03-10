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

## 💡 AI Implementation Guidelines

1. **Be Precise**: SIMetrix commands often require exact syntax, specific argument order, and slash-based switches. Do not guess the syntax; ALWAYS read the detailed markdown file for the command.
2. **Use Search**: If the summary files are long, use `grep_search` to look for keywords (e.g., "export", "netlist", "zoom") within the `./SIMetrix_document/SIMetrix Script Manual` directory.
3. **Execution**: To execute these commands and communicate with SIMetrix from Python, you MUST use the `simetrix_automation.py` program located in the same directory (`./simetrix_automation.py`). This script is the designated communication interface between Python and SIMetrix.
