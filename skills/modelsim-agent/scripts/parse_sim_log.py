#!/usr/bin/env python3
"""
parse_sim_log.py — Parse ModelSim simulation logs and extract actionable info.

Extracts:
  - Syntax / compilation errors
  - $display / $monitor output lines
  - Assertion failures ($error, $fatal, assert)

Usage:
    python parse_sim_log.py --log sim_output.log
    python parse_sim_log.py --log sim_output.log --json
"""

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class ParsedLog:
    """Structured result of parsing a simulation log."""
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    display_output: list[str] = field(default_factory=list)
    assertions: list[str] = field(default_factory=list)
    summary: str = ""

    def has_failures(self) -> bool:
        return bool(self.errors or self.assertions)


                                                 
PATTERNS = {
    "error": re.compile(
        r"(?i)"
        r"(\*\*\s*Error.*|"                                           
        r"Error\s*\(.*\).*|"                           
        r".*Syntax error.*|"                   
        r".*Fatal:.*|"                        
        r"\*\*\s*Fatal.*)"                     
    ),
    "warning": re.compile(
        r"(?i)"
        r"(\*\*\s*Warning.*|"                    
        r"Warning\s*\(.*\).*)"                           
    ),
    "display": re.compile(
        r"^#\s+(.*)$"                                                        
    ),
    "assertion": re.compile(
        r"(?i)"
        r"(.*\$error.*|"                            
        r".*\$fatal.*|"                             
        r".*Assertion.*fail.*|"                         
        r".*FAIL.*|"                                 
        r".*ASSERTION.*)"                                 
    ),
}

                                      
SKIP_PATTERNS = re.compile(
    r"(?i)"
    r"(^#\s*$|"                                       
    r"^#\s*Loading.*|"                             
    r"^#\s*Compiling.*|"                               
    r"^Reading\s+.*|"                              
    r"^vsim\s+.*|"                                     
    r"^Start time:.*|"                       
    r"^End time:.*|"
    r"^Errors:\s*0,\s*Warnings:\s*0$)"                 
)


def parse_log(log_text: str) -> ParsedLog:
    """Parse a ModelSim simulation log and extract key information."""
    result = ParsedLog()

    for line in log_text.splitlines():
        stripped = line.strip()
        if not stripped or SKIP_PATTERNS.match(stripped):
            continue

                          
        if PATTERNS["error"].match(stripped):
            result.errors.append(stripped)
            continue

                                                                                       
        if PATTERNS["assertion"].match(stripped):
                                                              
            if stripped not in result.errors:
                result.assertions.append(stripped)
            continue

                            
        if PATTERNS["warning"].match(stripped):
            result.warnings.append(stripped)
            continue

                                              
        m = PATTERNS["display"].match(stripped)
        if m:
            content = m.group(1).strip()
            if content:                            
                result.display_output.append(content)

                   
    parts = []
    if result.errors:
        parts.append(f"{len(result.errors)} error(s)")
    if result.warnings:
        parts.append(f"{len(result.warnings)} warning(s)")
    if result.assertions:
        parts.append(f"{len(result.assertions)} assertion failure(s)")
    if result.display_output:
        parts.append(f"{len(result.display_output)} display line(s)")

    if result.has_failures():
        result.summary = "FAIL — " + ", ".join(parts)
    elif parts:
        result.summary = "PASS — " + ", ".join(parts)
    else:
        result.summary = "PASS — No output captured (check testbench $display statements)"

    return result


def format_text(parsed: ParsedLog) -> str:
    """Format parsed log as human-readable text."""
    sections = [f"=== Simulation Result: {parsed.summary} ===\n"]

    if parsed.errors:
        sections.append("--- ERRORS ---")
        sections.extend(f"  {e}" for e in parsed.errors)
        sections.append("")

    if parsed.assertions:
        sections.append("--- ASSERTION FAILURES ---")
        sections.extend(f"  {a}" for a in parsed.assertions)
        sections.append("")

    if parsed.warnings:
        sections.append("--- WARNINGS ---")
        sections.extend(f"  {w}" for w in parsed.warnings)
        sections.append("")

    if parsed.display_output:
        sections.append("--- DISPLAY OUTPUT ---")
        sections.extend(f"  {d}" for d in parsed.display_output)
        sections.append("")

    return "\n".join(sections)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Parse ModelSim simulation logs and extract actionable info."
    )
    parser.add_argument(
        "--log",
        required=True,
        help="Path to the simulation log file.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output in JSON format.",
    )

    args = parser.parse_args()

    log_path = Path(args.log)
    if not log_path.exists():
        print(f"ERROR: Log file not found: {args.log}", file=sys.stderr)
        sys.exit(1)

    log_text = log_path.read_text(encoding="utf-8", errors="replace")
    parsed = parse_log(log_text)

    if args.json:
        output = {
            "summary": parsed.summary,
            "has_failures": parsed.has_failures(),
            "errors": parsed.errors,
            "warnings": parsed.warnings,
            "assertions": parsed.assertions,
            "display_output": parsed.display_output,
        }
        print(json.dumps(output, indent=2))
    else:
        print(format_text(parsed))

    sys.exit(1 if parsed.has_failures() else 0)


if __name__ == "__main__":
    main()
