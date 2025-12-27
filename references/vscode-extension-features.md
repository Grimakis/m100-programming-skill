# VSCode Extension Features

This document describes the "TRS-80 Model 100/200 BASIC" VSCode extension which provides tooling specifically designed for M100 BASIC development.

## Diagnostics (Automatic Warnings/Errors)

The extension automatically flags issues in your code:

**Errors:**
- `E_LINE_RANGE` - Line number out of range (1-65529)
- `E_DUP_LINE` - Duplicate line numbers
- `E_MISSING_TARGET` - GOTO/GOSUB target doesn't exist
- `E_ASSIGN_TO_FUNCTION` - Cannot assign to BASIC functions (e.g., `CHR$="foo"`)
- `E_VAR_INVALID_START` - Variable must start with a letter

**Warnings:**
- `W_VAR_NAME_TOO_LONG` - Variable name >2 chars (only first 2 + type suffix are significant)
- `W_VAR_NAME_COLLISION` - Variables share same first 2 chars + type (e.g., `PIECE` and `PILOT` both → `PI`)
- `W_LINE_ORDER` - Lines out of numerical order
- `W_LINE_LEN` - Line exceeds recommended length
- `W_ASSIGN_TYPE` - Type mismatch in assignment
- `W_ARG_MIN` / `W_ARG_MAX` - Wrong number of arguments
- `W_ARG_TYPE` - Argument type mismatch
- `W_NO_TOKENS` - Line has no executable tokens
- `W_COMMENT_TARGET` - Comment on a GOTO target line
- `W_UNREACHABLE` - Unreachable code detected

## Quick Fixes (Available on Diagnostics)

When you see a diagnostic, click the lightbulb 💡 or press `Cmd+.` (Mac) / `Ctrl+.` (Windows) to see available fixes:

**Variable Issues:**
- **Truncate to 2 characters** - Automatically shortens variable names (preserves type suffix)
  - Example: `PLAYER$` → `PL$`
  - Marked as "preferred" - LLMs should suggest this first

- **Rename variable to avoid collision** - Interactive rename with validation
  - Prompts for new name
  - Validates no new collisions
  - Must preserve type suffix
  - Finds and replaces all occurrences (skips strings/comments)

**Line Number Issues:**
- **Renumber this line** - Renumbers single line and updates all references
- **Renumber entire program** - Renumbers all lines sequentially

## Refactoring Actions (Right-Click Menu)

Right-click anywhere in a BASIC file → **"Refactor..."** to access:

1. **Pack Program (merge statements)**
   - Merges multiple lines onto fewer lines using `:` separators
   - Respects GOTO targets (won't merge target lines)
   - Prompts for max line length
   - Use when: Optimizing for memory/storage

2. **Remove All Comments**
   - Strips all REM statements and `'` comments
   - Preserves GOTO target lines
   - Shows confirmation dialog
   - Use when: Preparing for upload to hardware (save bytes)

3. **Squash Program (remove whitespace)**
   - Removes unnecessary spaces outside strings
   - Collapses PRINT semicolons
   - Removes trailing colons
   - Use when: Final optimization before tokenization

4. **Tokenize to .BA format**
   - Converts ASCII BASIC to binary tokenized format
   - Prompts for output file location
   - Prompts for base memory address:
     - Model 100/102: `8001` (default)
     - Tandy 200: `A001`
   - Creates .BA file ready for hardware/emulator
   - Use when: Preparing to load on actual M100/200

5. **Renumber Program**
   - Renumbers all lines sequentially
   - Updates all GOTO/GOSUB/RESTORE references
   - Prompts for start line and increment
   - Use when: Lines out of order or need to insert lines

## CodeLens (Top of File Links)

Clickable links appear at the top of every .DO file:

- **Renumber Program…** - Quick access to renumbering
- **Tokenize to .BA…** - Quick access to tokenization
- **Pack Program** - Quick access to packing
- **Squash Program** - Quick access to squashing
- **Remove Comments** - Quick access to comment removal

## Command Palette Commands

Press `Cmd+Shift+P` (Mac) / `Ctrl+Shift+P` (Windows) and type:

- `M100 BASIC: Renumber Program`
- `M100 BASIC: Renumber Current Line`
- `M100 BASIC: Renumber From Current Line`
- `M100 BASIC: Pack Program Lines`
- `M100 BASIC: Remove Comments`
- `M100 BASIC: Squash BASIC Lines`
- `M100 BASIC: Tokenize Program to .BA`
- `M100 BASIC: Open Tokenized .BA (detokenized, read-only)`
- `M100 BASIC: View DATA as 8085 Disassembly`

## When to Recommend Extension Features

**During coding:**
- See variable collision warning → Suggest "Rename variable" quick fix
- See variable too long warning → Suggest "Truncate to 2 chars" quick fix
- Lines out of order → Suggest "Renumber Program"
- Need to add lines between existing → Suggest renumber to create gaps

**Before upload to hardware:**
1. Run "Remove Comments" to save memory
2. Run "Squash Program" to remove whitespace
3. Run "Pack Program" if need more space (careful with line length)
4. Run "Tokenize to .BA" to create binary file

**During debugging:**
- Use "Renumber Program" to organize line numbers
- Use quick fixes to resolve all diagnostics before testing

## File Types

- `.DO` - ASCII BASIC source (editable)
- `.BA` - Tokenized binary BASIC (read-only in VSCode, use "Open Tokenized .BA" command to view)

## LLM Best Practices

When helping with M100 BASIC code:
1. **Check diagnostics first** - Address warnings/errors before suggesting new features
2. **Recommend quick fixes proactively** - Don't wait for user to ask
3. **Explain the "why"** - Variable truncation and collisions are confusing, explain them
4. **Suggest optimization workflow** - Comments → Squash → Pack → Tokenize
5. **Use extension features instead of manual edits** - Safer and handles references automatically

## CALL Statement for ASM

The `CALL` statement invokes machine language subroutines. Use when BASIC is too slow:
- `CALL address` - Execute ML at decimal address
- `CALL address, arg1, arg2, ...` - Pass arguments
- Common addresses on Model 100:
  - `16959` (`0x423F`) - CHGET (wait for keypress)
  - `16964` (`0x4244`) - Clear keyboard buffer

When implementing hot paths in ASM, use the extension's features to optimize the BASIC wrapper code.
