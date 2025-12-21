8085 Harness (Sim8085 core)

Purpose
- Headless test runner for 8085 routines used in SNOW.
- Designed to be portable into a Skill repo without GUI dependencies.

Requirements
- Python 3.10+
- Sim8085 submodule at scripts/Sim8085 (or pass --sim8085-path)

Usage (project-specific)
- python tools/8085_harness/run_8085_harness.py
- python tools/8085_harness/run_8085_spec.py --spec tools/8085_harness/specs/snowed_in_init.json

Generic core
- scripts/emu_runner.py is reusable and project-agnostic.
- scripts/run_8085_spec.py runs a JSON spec (project-agnostic).

Options
--asm <path>            Path to .8085 source (default: assembly/17000_init_board.8085)
--sim8085-path <path>   Path to Sim8085 repo (default: tools/8085_harness/Sim8085)
--mode fill|clear|both  Which tests to run (default: both)

Notes
- The harness loads the assembled bytes into memory and executes until RET.
- It emulates the Model 100 CALL ABI by setting A (mode) and HL (MP% pointer).
- The memory layout matches BASIC integer arrays: 42 columns, 2 bytes per cell.
- Sim8085 has a DAD implementation bug (H<<4 instead of H<<8); the harness
  patches DAD execution when using the Sim8085 core.
