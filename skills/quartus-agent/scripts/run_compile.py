#!/usr/bin/env python3
"""
run_compile.py — Run the full Quartus compilation flow via CLI.

Usage:
    python run_compile.py --project my_project
    python run_compile.py --project my_project --cwd syn/
"""

import argparse
import subprocess
import sys


def run_cmd(cmd: list[str], cwd: str | None = None) -> subprocess.CompletedProcess:
    """Run a command, print it, and return the result."""
    print(f"[run_compile] > {' '.join(cmd)}")
    result = subprocess.run(
        cmd,
        cwd=cwd,
        capture_output=True,
        text=True,
        timeout=1800,  # 30-minute timeout for large designs
    )
    return result


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run the full Quartus compilation flow."
    )
    parser.add_argument(
        "--project",
        required=True,
        help="Quartus project name (without extension).",
    )
    parser.add_argument(
        "--cwd",
        default=None,
        help="Working directory containing the project files.",
    )
    parser.add_argument(
        "--flow",
        default="compile",
        choices=["compile", "analysis_and_synthesis", "fitter", "assembler", "timing"],
        help="Compilation flow to run (default: compile = full flow).",
    )

    args = parser.parse_args()

    # Map flow names to quartus_sh arguments
    flow_map = {
        "compile": "compile",
        "analysis_and_synthesis": "analysis_and_synthesis",
        "fitter": "fitter",
        "assembler": "assembler",
        "timing": "sta",
    }

    flow_arg = flow_map[args.flow]

    cmd = [
        "quartus_sh",
        "--flow",
        flow_arg,
        args.project,
    ]

    result = run_cmd(cmd, cwd=args.cwd)

    # Print output
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr, file=sys.stderr)

    if result.returncode != 0:
        print(
            f"\n[run_compile] FAILED with return code {result.returncode}.",
            file=sys.stderr,
        )
        sys.exit(result.returncode)
    else:
        print(f"\n[run_compile] Compilation flow '{args.flow}' completed successfully.")


if __name__ == "__main__":
    main()
