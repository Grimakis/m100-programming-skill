# TRS-80 Model 100 ROM Functions (700–2245)

Source: rom_funcs-600.pdf

> **Convention:** “Entry conditions” are register inputs before `CALL`ing the routine. “Exit conditions” are outputs/flags after return. All addresses below are **hex**.

---

## LCD functions

| Function | Entry Addr | Purpose | Entry conditions | Exit conditions |
|---|---:|---|---|---|
| `LCD` | `4B44` | Display a character at the **current cursor** position (also `RST 4`) | `A = character to display` | none |
| `SETCUR` | `7440` | Move cursor to specified location | `D = column (1–40)`, `E = row (1–8)` | none |
| `PLOT` | `744C` | Turn **on** pixel at location | `D = x (0–239)`, `E = y (0–63)` | none |
| `UNPLOT` | `744D` | Turn **off** pixel at location | `D = x (0–239)`, `E = y (0–63)` | none |
| `POSIT` | `427C` | Set cursor position | `H = column (1–40)`, `L = row (1–8)` | none |
| `ESCA` | `4270` | Send specified escape-code sequence | `A = escape code` | none |

---

## Common LCD routines + equivalent escape codes

| Function | Entry Addr | Equivalent `ESC` code | Description |
|---|---:|:---:|---|
| `CRLF` | `4222` | — | Carriage return + line feed |
| `HOME` | `422D` | — | Cursor to home position `(1,1)` |
| `CLS` | `4231` | — | Clear display |
| `SETSYS` | `4235` | `T` | Set system line (lock line 8, `LABEL`) |
| `RSTSYS` | `423A` | `U` | Reset system line (unlock line 8, `LABEL`) |
| `LOCK` | `423F` | `Y` | Lock display (no scrolling) |
| `UNLOCK` | `4244` | `W` | Unlock display (scrolling) |
| `CURSON` | `4249` | `P` | Turn on cursor |
| `CUROFF` | `424E` | `Q` | Turn off cursor |
| `DELLIN` | `4253` | `M` | Delete line at current cursor position |
| `INSLIN` | `4258` | `L` | Insert blank line at cursor position |
| `ERAEOL` | `425D` | `K` | Erase from cursor to end of line |
| `ENTREV` | `4269` | `p` | Set reverse character mode |
| `EXTREV` | `426E` | `q` | Turn off reverse character mode |

### Variable / status locations

| Name | Meaning | Address |
|---|---|---:|
| `CSRY` | Cursor position (row) | `F639` |
| `CSRX` | Cursor position (column) | `F63A` |
| `BEGLCD` | Start of LCD memory | `FE00` |
| `ENDLCD` | End of LCD memory | `FF40` |

---

## Keyboard functions

### `KYREAD` — scan keyboard
- **Entry address:** `7242`
- **Entry conditions:** none  
- **Exit conditions:**
  - `A = character` (if any)
  - `Z flag` set if **no key found**, reset if key found
  - `Carry` set if **special key** (see table), reset for normal character set code

When **Carry is set**, `A` contains:

| `A` | Key |
|---:|---|
| `00` | `F1` |
| `01` | `F2` |
| `02` | `F3` |
| `03` | `F4` |
| `04` | `F5` |
| `05` | `F6` |
| `06` | `F7` |
| `07` | `F8` |
| `08` | `LABEL` |
| `09` | `PRINT` |
| `0A` | `SHIFT-PRINT` |
| `0B` | `PASTE` |

### `CHGET` — wait/get a character
- **Entry address:** `12CB`
- **Entry conditions:** none  
- **Exit conditions:** `A = character code`
  - `Carry` set if special character, reset if normal
  - `(F1)–(F8)` return preprogrammed strings

### `CHSNS` — check keyboard queue
- **Entry address:** `13DB`
- **Entry conditions:** none  
- **Exit conditions:** `Z flag` set if queue empty, reset if keys pending

### `KEYX` — check keyboard queue for chars or BREAK
- **Entry address:** `7270`
- **Entry conditions:** none  
- **Exit conditions:**
  - `Z flag` set if queue empty, reset if keys pending
  - `Carry` set when `BREAK` entered; reset with any other key

### `BRKCHK` — check BREAK chars only (`CTRL-C` or `CTRL-S`)
- **Entry address:** `7283`
- **Entry conditions:** none  
- **Exit conditions:** `Carry` set if `BREAK` or `PAUSE` entered; reset if no break characters

### `INLIN` — get a line (terminated by `<ENTER>`)
- **Entry address:** `4644`
- **Entry conditions:** none  
- **Exit conditions:** data stored at `F685`

---

## Function key routines (`F1`–`F8` tables)

### Function table format (how the keyboard driver consumes it)
- Table consists of **strings** used when processing `(F1)`–`(F8)`.
- Each string has **max 16 characters** and is terminated by byte `80h`.
- If the **last character** is OR’ed with `80h`, that character also acts as the terminator.
- Entire string is placed in the keyboard buffer when its function key is pressed.
- You must define strings for **all 8** function keys (use the terminator byte for any you want to ignore).

### Example function table (as shown)
```asm
FCTAB   DEFM 'Files'   ; F1
        DEFW 0D80
        DEFM 'Load'    ; F2
        DEFB 80
        DEFM 'Save'    ; F3
        DEFB 80
        DEFM 'Run'     ; F4
        DEFW 0D80
        DEFM 'List'    ; F5
        DEFW 0D80
        DEFB 80        ; Ignore F6
        DEFB 80        ; Ignore F7
        DEFM 'Menu'    ; F8
        DEFW 0D80
```

### Routines

| Function | Entry Addr | Purpose | Entry conditions | Exit conditions |
|---|---:|---|---|---|
| `STFNK` | `5A7C` | Set function key definitions | `HL = address of function table` | none |
| `CLRFLK` | `5A79` | Clear function-key definition table (fills with `80h`) | none | none |
| `DSPNFK` | `42A8` | Display function keys | none | none |
| `STDSPF` | `42A5` | Set and display function keys | `HL = start address of function table` | none |
| `ERAFNK` | `428A` | Erase function key display | none | none |
| `FNKSB` | `5A9E` | Display function table (if enabled) | none | none |

---

## Printing routines

| Function | Entry Addr | Purpose | Entry conditions | Exit conditions |
|---|---:|---|---|---|
| `PRINTR` | `6D3F` | Send a character to the line printer | `A = character` | `Carry` set if cancelled by `BREAK`, reset if normal return |
| `PNOTAB` | `1470` | Print char **without expanding** tab characters | `A = character` | — |
| `PRTTAB` | `4B55` | Print char **expanding tabs** to spaces | `A = character` | — |
| `PRTLCD` | `1E5E` | Print contents of LCD | none | none |

---

## RS232-C and modem routines

### Phone/modem control

| Function | Entry Addr | Purpose | Entry conditions | Exit conditions |
|---|---:|---|---|---|
| `DISC` | `52DD` | Disconnect phone line | none | none |
| `CONN` | `52D0` | Connect phone line | none | none |
| `DIAL` | `532D` | Dial phone number | `HL = phone number address` | none |

### Serial I/O + flow control

| Function | Entry Addr | Purpose | Entry conditions | Exit conditions |
|---|---:|---|---|---|
| `RCVX` | `6D6D` | Check RS232 receive queue | none | `A = # chars in queue`, `Z` set if no data, reset if chars pending |
| `RV232C` | `6D7E` | Get a character from RS232 receive queue | none | `A = char`, `Z` set if OK / reset if error (`PE`, `FF`, or `OF`), `Carry` set if `BREAK` pressed |
| `SENSCQ` | `6E0B` | Send XON resume (`CTRL-Q`) | none | none |
| `SENDCS` | `6E1E` | Send XOFF pause (`CTRL-S`) | none | none |
| `SD232C` | `6E32` | Send character to RS-232/modem **with** XON/XOFF | `A = char` | — |
| `SNDCOM` | `6E3A` | Send character to RS-232/modem **without** XON/XOFF | `C = char` | — |
| `CARDET` | `6EFF` | Detect carrier | none | `A = 0 if carrier`, `Z` set if carrier else reset |
| `BAUDST` | `6E75` | Set baud rate for RS232-C | `H = baud rate (1–9,M)` | none |

### Init/config

#### `INZCOM` — initialize RS232-C and modem
- **Entry address:** `6EA6`
- **Entry conditions:**  
  - `H = baud rate (1–9,M)`  
  - `L = UART configuration code` (see below)
- **Exit conditions:** none  
  - `Carry` set if RS232-C, reset if modem

UART config bits in `L`:
- Bit `0`: stop bits (`0=1`, `1=2`)
- Bits `1–2`: parity (`00=None`, `01=Even`, `10=Odd`)
- Bits `3–4`: word length (`00=6`, `01=7`, `10=8`)
- Byte is ANDed with `1Fh` to ignore bits `5–7`.
- Current STAT setting string is located at `F65B` (5 bytes): **Baud, Length, Parity, Stop Bits, XON/XOFF switch**

#### `SETSER` — set serial interface parameters + activate RS232/modem
- **Entry address:** `17E6`
- **Entry conditions:** `HL = start address of ASCII parameter string`, terminated by binary zero (`'78E1E', 0`), syntax same as Telcom’s `STAT`  
- **Exit conditions:** none  
  - `Carry` set for RS232-C, reset for modem

#### `CLSCOM` — deactivate RS232-C / modem
- **Entry address:** `6ECB`
- **Entry conditions:** none
- **Exit conditions:** none

---

## Cassette recorder routines

| Function | Entry Addr | Purpose | Entry conditions | Exit conditions |
|---|---:|---|---|---|
| `DATAR` | `702A` | Read char from cassette (no checksum) | none | `D = character` |
| `CTON` | `14A8` | Turn motor on | none | none |
| `CTOFF` | `14AA` | Turn motor off | none | none |
| `CASIN` | `14B0` | Read char + update checksum | `C = current checksum` | `A = character`, `C = updated checksum` |
| `CSOUT` | `14C1` | Send char + update checksum | `A = character`, `C = current checksum` | `C = updated checksum` |
| `SYNCW` | `6F46` | Write cassette header + sync byte only | none | none |
| `SYNCR` | `6F85` | Read cassette header + sync byte only | none | none |
| `DATAW` | `6F5B` | Write char to cassette (no checksum) | `A = character` | none |

---

## RAM file routines

### Directory table + directory entry format
- Directory table is located at `F962` and contains file location/type/status.
- Each file has an **11-byte** directory entry:
  - Byte `1`: directory flag (file type + status)
  - Bytes `2–3`: address of file
  - Bytes `4–11`: 8-byte filename

Directory flag bits:
- Bit `7` (MSB): `1` if valid entry  
- Bit `6`: `1` for ASCII text file (`DO`)  
- Bit `5`: `1` for machine language file (`CO`)  
- Bit `4`: `1` for ROM file  
- Bit `3`: `1` for invisible file  
- Bit `2`: reserved  
- Bit `1`: reserved  
- Bit `0`: internal use only  

### File routines

| Function | Entry Addr | Purpose | Entry conditions | Exit conditions |
|---|---:|---|---|---|
| `MAKTXT` | `220F` | Create a text file | filename (max 8 bytes) must be stored in `FILNAM (0FC93)`; `.DO` extension not required | `HL = TOP address of new file`, `DE = directory entry address (flag)`, `Carry` set if file exists / reset if new |
| `CHKDC` | `5AA9` | Search for file in directory | `DE = addr of filename to find` (ASCII filename + `00` terminator) | `HL = start addr (TOP) of file`; `Z=0` found, `Z=1` not found |
| `GTXTTB` | `5AE3` | Get TOP start address of file | `HL = addr of directory entry for file` | `HL = TOP start addr of file` |
| `KILASC` | `1FBE` | Kill a text (`DO`) file | `DE = file TOP start addr`, `HL = addr of directory entry (flag)` | none |
| `INSCHR` | `6B61` | Insert a character in a file | `A = char`, `HL = addr to insert at` | `HL = HL+1`; `Carry` set if out of memory |
| `MAKHOL` | `6B6D` | Insert N spaces in a file | `BC = # spaces`, `HL = addr to insert at` | `HL & BC preserved`; `Carry` set if out of memory |
| `MASDEL` | `6B9F` | Delete N characters | `BC = # chars`, `HL = addr of deletion` | `HL & BC preserved` |

---

## Other routines

| Function | Entry Addr | Purpose | Entry conditions | Exit conditions |
|---|---:|---|---|---|
| `INITIO` | `6CD6` | Cold start reset | none | none |
| `IOINIT` | `6CE0` | Warm start reset | none | none |
| `MENU` | `5797` | Go to main menu | none | none |
| `MUSIC` | `72C5` | Make tone | `DE = frequency`, `B = duration` | none |
| `TIME` | `190F` | Read system time | `HL = address of 8-byte area` | buffer => `TIME (hh:mm:ss)` |
| `DATE` | `192F` | Read system date | `HL = address of 8-byte area` | buffer => `DATE (mm/dd/yy)` |
| `DAY` | `1962` | Read system day of week | `HL = address of 3-byte area` | buffer => `DAY (ddd)` |
