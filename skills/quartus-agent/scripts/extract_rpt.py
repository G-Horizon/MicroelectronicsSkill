#!/usr/bin/env python3
"""
extract_rpt.py — Parse Quartus compilation report files (.rpt) and extract key metrics.

Extracts:
  - Resource usage (ALMs, Registers, Block RAM, DSP)
  - Errors and critical warnings
  - Timing summary (Fmax, Setup/Hold slack)

Usage:
    python extract_rpt.py --project my_project
    python extract_rpt.py --project my_project --cwd syn/ --json
    python extract_rpt.py --project my_project --cwd syn/ --output syn/reports/compile_result.json
"""

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path


@dataclass
class CompileReport:
    """Structured extraction of Quartus compilation results."""
    resource_usage: dict[str, str] = field(default_factory=dict)
    fmax: list[str] = field(default_factory=list)
    timing_violations: list[str] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)
    critical_warnings: list[str] = field(default_factory=list)
    warnings_count: int = 0
    success: bool = False

    def has_failures(self) -> bool:
        return bool(self.errors or self.timing_violations)


                                   
RESOURCE_PATTERNS = {
    "Total logic elements": re.compile(
        r"Total logic elements\s*[;:]\s*(.+?)(?:\s*$)", re.IGNORECASE
    ),
    "Total registers": re.compile(
        r"Total registers\s*[;:]\s*(.+?)(?:\s*$)", re.IGNORECASE
    ),
    "Total memory bits": re.compile(
        r"Total memory bits\s*[;:]\s*(.+?)(?:\s*$)", re.IGNORECASE
    ),
    "Embedded Multiplier": re.compile(
        r"Embedded Multiplier.*?[;:]\s*(.+?)(?:\s*$)", re.IGNORECASE
    ),
    "Total ALMs": re.compile(
        r"(?:Estimate of )?Logic utilization.*ALMs.*?[;:]\s*(.+?)(?:\s*$)", re.IGNORECASE
    ),
    "Total block memory bits": re.compile(
        r"Total block memory bits\s*[;:]\s*(.+?)(?:\s*$)", re.IGNORECASE
    ),
    "Total DSP Blocks": re.compile(
        r"Total DSP Blocks\s*[;:]\s*(.+?)(?:\s*$)", re.IGNORECASE
    ),
    "Total pins": re.compile(
        r"Total pins\s*[;:]\s*(.+?)(?:\s*$)", re.IGNORECASE
    ),
}

FMAX_PATTERN = re.compile(
    r";\s*Fmax\s*;\s*([\d.]+\s*MHz)", re.IGNORECASE
)

SLACK_PATTERN = re.compile(
    r";\s*(Setup|Hold)\s*;\s*.*?;\s*(-?[\d.]+)", re.IGNORECASE
)

ERROR_PATTERN = re.compile(r"^Error\s*\(.*?\)\s*:", re.IGNORECASE)
CRITICAL_WARNING_PATTERN = re.compile(r"^Critical Warning\s*\(.*?\)\s*:", re.IGNORECASE)
WARNING_PATTERN = re.compile(r"^Warning\s*\(.*?\)\s*:", re.IGNORECASE)
LATCH_PATTERN = re.compile(r"inferred latch", re.IGNORECASE)


def parse_rpt_file(filepath: Path) -> tuple[list[str], list[str], dict[str, str], list[str], list[str]]:
    """Parse a single .rpt file and return categorized findings."""
    errors = []
    critical_warnings = []
    resources = {}
    fmax_results = []
    timing_violations = []

    try:
        text = filepath.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return errors, critical_warnings, resources, fmax_results, timing_violations

    for line in text.splitlines():
        stripped = line.strip()

                
        if ERROR_PATTERN.match(stripped):
            errors.append(stripped)
            continue

        if LATCH_PATTERN.search(stripped) and "warning" in stripped.lower():
            critical_warnings.append(f"[LATCH WARNING] {stripped}")
            continue

                           
        if CRITICAL_WARNING_PATTERN.match(stripped):
            critical_warnings.append(stripped)
            continue

                        
        for name, pattern in RESOURCE_PATTERNS.items():
            m = pattern.search(stripped)
            if m:
                resources[name] = m.group(1).strip().rstrip(";").strip()
                break

              
        m = FMAX_PATTERN.search(stripped)
        if m:
            fmax_results.append(m.group(1).strip())

                            
        m = SLACK_PATTERN.search(stripped)
        if m:
            slack_type = m.group(1)
            slack_val = float(m.group(2))
            if slack_val < 0:
                timing_violations.append(f"{slack_type} violation: {slack_val} ns")

    return errors, critical_warnings, resources, fmax_results, timing_violations


def extract_reports(project_name: str, project_dir: Path) -> CompileReport:
    """Parse all .rpt files in the project directory."""
    report = CompileReport()

                                                                     
    rpt_dirs = [project_dir, project_dir / "output_files"]
    rpt_files = []
    for d in rpt_dirs:
        if d.exists():
            rpt_files.extend(d.glob("*.rpt"))

    if not rpt_files:
        report.errors.append(f"No .rpt files found in {project_dir}")
        return report

    for rpt_file in rpt_files:
        errors, crit_warns, resources, fmax, violations = parse_rpt_file(rpt_file)
        report.errors.extend(errors)
        report.critical_warnings.extend(crit_warns)
        report.resource_usage.update(resources)
        report.fmax.extend(fmax)
        report.timing_violations.extend(violations)

    report.success = not report.has_failures()
    return report


def format_text(report: CompileReport) -> str:
    """Format the report as human-readable text."""
    status = "SUCCESS" if report.success else "FAILED"
    sections = [f"=== Quartus Compilation: {status} ===\n"]

    if report.errors:
        sections.append("--- ERRORS ---")
        for e in report.errors:
            sections.append(f"  {e}")
        sections.append("")

    if report.critical_warnings:
        sections.append("--- CRITICAL WARNINGS ---")
        for cw in report.critical_warnings:
            sections.append(f"  {cw}")
        sections.append("")

    if report.resource_usage:
        sections.append("--- RESOURCE USAGE ---")
        for name, val in report.resource_usage.items():
            sections.append(f"  {name}: {val}")
        sections.append("")

    if report.fmax:
        sections.append("--- TIMING (Fmax) ---")
        for f in report.fmax:
            sections.append(f"  {f}")
        sections.append("")

    if report.timing_violations:
        sections.append("--- TIMING VIOLATIONS ---")
        for v in report.timing_violations:
            sections.append(f"  {v}")
        sections.append("")

    return "\n".join(sections)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Parse Quartus .rpt files and extract key metrics."
    )
    parser.add_argument(
        "--project",
        required=True,
        help="Quartus project name.",
    )
    parser.add_argument(
        "--cwd",
        default=".",
        help="Directory containing the Quartus project.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output in JSON format.",
    )
    parser.add_argument(
        "--output",
        default=None,
        help="Write JSON report to this file path (e.g., syn/reports/compile_result.json).",
    )

    args = parser.parse_args()
    project_dir = Path(args.cwd)

    report = extract_reports(args.project, project_dir)

                               
    json_output = {
        "status": "SUCCESS" if report.success else "FAILED",
        "timestamp": datetime.now().isoformat(),
        "resource_usage": report.resource_usage,
        "fmax": report.fmax,
        "timing_violations": report.timing_violations,
        "errors": report.errors,
        "critical_warnings": report.critical_warnings,
    }

                                         
    if args.output:
        out_path = Path(args.output)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(
            json.dumps(json_output, indent=2, ensure_ascii=False), encoding="utf-8"
        )
        print(f"[extract_rpt] Report saved to {out_path}")

                      
    if args.json or args.output:
        print(json.dumps(json_output, indent=2))
    else:
        print(format_text(report))

    sys.exit(0 if report.success else 1)


if __name__ == "__main__":
    main()
