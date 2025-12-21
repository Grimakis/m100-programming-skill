# Model 100 BASIC Variable and Memory Layout (RRW)

This is a reformatted reference for how BASIC variables, arrays, and RAM areas are laid out in memory on the Model 100.

## Scalar Variable Format

When BASIC encounters a variable name, it searches the variable table for the name and type:
double-precision, single-precision, integer, or string. If not found, BASIC appends a new
entry to the table. Each entry has a 3-byte header plus 2 to 8 bytes of content, depending
on type. The Type byte also serves as a skip-count to the next header.

### Header (all types)

| Byte | Meaning |
| --- | --- |
| 0 | Type / skip-count: 8 = double, 4 = single, 2 = integer, 3 = string |
| 1 | Name, 1st character |
| 2 | Name, 2nd character (NUL for 1-char names) |

### Content layout by type

| Byte | Double-precision | Single-precision | Integer | String |
| --- | --- | --- | --- | --- |
| 3 | S & E | S & E | LSB | Len |
| 4 | BCD M | BCD M | MSB | Addr Low |
| 5 | BCD # | BCD # | - | Addr High |
| 6 | BCD # | BCD L | - | - |
| 7 | BCD # | - | - | - |
| 8 | BCD # | - | - | - |
| 9 | BCD # | - | - | - |
| 10 | BCD L | - | - | - |

Notes:
- LSB = least significant byte of integer.
- MSB = most significant byte of integer. Bit 7 contains the sign.
- BCD L / BCD M / BCD # = BCD-encoded digits (nibbles).
- S & E = sign and exponent. Bit 7 is sign. Bits 0-5 determine decimal point placement.
- Addr = address of string content (string constant or in string area).
- Len = length of string (matches LEN(var$)).

## Array Format

Example: `SV$(1,2,3)` is a 3-D string array. When BASIC encounters a subscripted variable,
it searches the array table for name+type. If not found, BASIC validates that all indices
are < 11, then expands the array table and creates a default 10-max array per dimension.

If found, BASIC checks each index against its maximum and throws BS if any index exceeds.

### Array header layout

| Byte | Meaning |
| --- | --- |
| 0 | Type: 8=double, 4=single, 2=integer, 3=string |
| 1 | Name, 1st character |
| 2 | Name, 2nd character (NUL for 1-char names) |
| 3 | Length LSB of array (relative to Byte 5) |
| 4 | Length MSB of array (relative to Byte 5) |
| 5 | Number of dimensions |
| 6 | Max index LSB for last dimension |
| 7 | Max index MSB for last dimension |
| ... | Next dimension (LSB/MSB), descending to first dimension |

The list of elements follows the header. Each element uses the same per-type format as
scalar variables (numeric content or string descriptor).

### Element order (ascending indices)

```
Byte00 SV$(0,0,0)  Byte18 SV$(0,0,1)  Byte36 SV$(0,0,2)  Byte54 SV$(0,0,3)
Byte03 SV$(1,0,0)  Byte21 SV$(1,0,1)  Byte39 SV$(1,0,2)  Byte57 SV$(1,0,3)
Byte06 SV$(0,1,0)  Byte24 SV$(0,1,1)  Byte42 SV$(0,1,2)  Byte60 SV$(0,1,3)
Byte09 SV$(1,1,0)  Byte27 SV$(1,1,1)  Byte45 SV$(1,1,2)  Byte63 SV$(1,1,3)
Byte12 SV$(0,2,0)  Byte30 SV$(0,2,1)  Byte48 SV$(0,2,2)  Byte66 SV$(0,2,3)
Byte15 SV$(1,2,0)  Byte33 SV$(1,2,1)  Byte51 SV$(1,2,2)  Byte69 SV$(1,2,3)
```

## RAM Dynamic Areas & Related Pointers

RAM is partitioned into three regions: upward growth, unused, and downward growth. Pointers
in the MAXRAM protected area track boundaries. Notation:

- `[    ]` means 16-bit word content at that address.
- `(    )` means 8-bit byte content at that address.
- `H` suffix means hex.

Reference diagram (verbatim formatting preserved):

```
         __________
[FAC0H]-> Start of .BA area. Also is lowest equipped RAM address.
         --  --  --
[F99AH]-> Noname.BA (unsaved BASIC program). Minimum size 2 bytes.
         __________
[FBAEH]-> Start of .DO area which follows the end of Noname.BA.
         --  --  --
[F9A5H]-> Noname.DO (paste buffer). Minimum size 1 byte.
         __________
[FBB0H]-> Start of .CO area.
         __________
[FBB2H]-> Variable Table.
         __________
[FBB4H]-> Array Table.
         __________
[FBB6H]-> Start of system unused RAM.
[F678H]-> End of system unused RAM.
  +1     __________
  = ----> Start of BASIC string area. Size set by CLEAR.
         __________
[FC83H]-> File Buffer descriptor pointer list (MAXFILES).
  +       addr of fbn = [FC83H] + 2*(FC82H) + 265*fbn
(FC82H)  __________
  = ----> File Buffer #0 (265 bytes).
         --  --  --
  +265 -> File Buffer #1 (if assigned) ... up to #15.
         __________
[F5F4H]-> HIMEM protected area. Size set by CLEAR.
         __________
 Note 1  MAXRAM protected area. End = FFFFH.
end=FFFFH__________
```

Additional reference:
http://www.club100.org/library/doc/ramabout.html

## File Descriptor Block (VARPTR(#file))

```
Byte 0   File status (0=not open, 1=input, 2=output/append)
Byte 2-3 Address of file directory entry +1
Byte 4   File device (248=RAM, 249=MODEM, 250=LP, 251=WAND, 252=COM,
                      253=CAS, 254=CRT, 255=LCD)
Byte 6   Offset from buffer start for next record
Byte 7-8 Relative position of next 256-byte block from file start
Byte 9-264 256-byte buffer
```
