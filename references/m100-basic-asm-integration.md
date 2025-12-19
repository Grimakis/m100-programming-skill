# Model 100 BASIC + ASM Integration (CALL ABI)

Primary integration mechanism: `CALL address, expr1, expr2`

## Calling convention (entry registers)
- On entry to the machine-language routine:
  - `A` contains the value of `expr1`
  - `HL` contains the value of `expr2`

## Design guidance
- Treat `A` as an 8-bit scalar input (0-255) unless you intentionally mask/extend.
- Treat `HL` as a 16-bit scalar (often used for addresses/pointers or 16-bit values).
- If you need a pointer to a BASIC variable/array/string, pass it via `HL` using `VARPTR(...)` from BASIC when appropriate.
- Keep the routine tight: no unnecessary register saving, but preserve what BASIC needs (be conservative until confirmed).
- Document each routine as a micro-API:
  - Inputs (A, HL meaning)
  - Outputs (what changes, what registers/memory are returned/modified)
  - Clobbers (registers touched)
  - Preconditions (range/format assumptions)

## Workflow for optimization
1. Identify the BASIC hot path (inner loop / repeated string scan / heavy math).
2. Define a minimal CALL interface (A + HL only; pack more data in memory if needed).
3. Implement ASM routine.
4. Add a BASIC wrapper subroutine:
   - Validates ranges
   - Prepares pointer/value inputs
   - Calls ASM
   - Converts/uses outputs safely
5. Add a quick BASIC test harness to verify correctness before performance tuning.
