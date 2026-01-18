#!/usr/bin/env python3
"""
Test runner script for Ocularis Mose testing system.
This script provides an easy way to run tests with various options.
"""
import sys
import subprocess


def run_tests(args=None):
    """Run the test suite with pytest"""
    cmd = ["python", "-m", "pytest"]
    
    if args:
        cmd.extend(args)
    else:
        # Default: run all tests with coverage
        cmd.extend([
            "tests/",
            "--cov=main",
            "--cov-report=term-missing",
            "--cov-report=html"
        ])
    
    print(f"Running: {' '.join(cmd)}")
    print("-" * 60)
    
    result = subprocess.run(cmd)
    return result.returncode


if __name__ == "__main__":
    # Pass any command-line arguments to pytest
    exit_code = run_tests(sys.argv[1:] if len(sys.argv) > 1 else None)
    sys.exit(exit_code)
