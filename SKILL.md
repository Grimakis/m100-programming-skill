---
name: tandy-m100-basic-asm
description: TRS-80 Model 100 BASIC constraints + workflow for offloading hot paths to ASM via CALL.
---

# Tandy Model 100 BASIC + ASM Skill

## When to use this skill
Use this skill whenever:
- Editing or generating Model 100 BASIC code.
- Optimizing slow BASIC routines by rewriting hot loops in assembly.
- Designing/adjusting the BASIC+ASM interface.

## Non-negotiable constraints (BASIC)
- **Line numbering:** default increment = **20**.
- **Section spacing:** leave **~1000 line-number gaps** between major program sections (INIT / INPUT / GAMELOOP / RENDER / UTIL, etc.).
- **Max BASIC line length:** **255 characters**.
- **Variable names:** **2 characters max**, plus type sigil.
- **Prefer explicit typing** so linting can detect mistakes.
  - `%` integer
  - `!` single precision float
  - `#` double precision float
  - `$` string

## Expression/operator rules
- Follow Model 100 operator hierarchy and left-to-right evaluation on same precedence level.
- Strings max length 255.
- Keep integer ranges and numeric precision limits in mind for any optimized math.

(Full operator + keyword reference lives in: `references/m100-basic-keywords.md`)

## Error Handling
- If you are shown an error code you can find the lookup table at: `references/m100-basic-errors.md`

## BASIC + ASM integration (CALL ABI)
- See `references/m100-basic-asm-integration.md` for the calling convention, design guidance, and workflow.

## Output format rules (when generating BASIC)
- Maintain your line-number spacing rules.
- Keep each BASIC line under 255 chars.
- Use 2-char vars with explicit type sigils.
- Avoid clever implicit typing; prefer DEFxxx only if you already do so consistently.

## What to do when uncertain
- If ABI details are ambiguous for a routine, generate a tiny BASIC harness + assembly stub to empirically test behavior.
- Prefer correctness + stable calling pattern over micro-optimizations.
