# Model 100 / PC-8201 / T200 System Map

Converted from `system_map.txt` for quick reference in skills.

Columns:
- M100 HEX / DEC
- PC-8201 HEX / DEC
- T200 HEX / DEC
- Name1 / Name2
- Description

| M100 HEX | M100 DEC | PC-8201 HEX | PC-8201 DEC | T200 HEX | T200 DEC | Name1 | Name2 | Description |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 62960 |  |  | EEB0 | 61104 |  | MAXRAM |  |  |
| F5F4 | 62964 | F384 | 62340 | 0000 |  | HIMEM |  | Highest memory available to BASIC (clear value) |
| F5F9 | 62969 | F389 | 62345 | 0000 |  | INTRPT |  | Rst 5.5 hook normally barcode reader |
| F5FC | 62972 | F38C | 62348 | 0000 |  | R65HOK |  | Rst 6.5 hook normally UART (COM) |
| F5FF | 62975 | F38F | 62351 | EEC2 | 61122 | R75HOK | RS75HK | Rst 7.5 hook normally from timer |
| F624 | 63012 | F3B9 | 62393 | 0000 |  | BRUN |  | This executes second ROM |
| F625 | 63013 | F3BA | 62394 | 0000 |  | BRUN2 |  | This executes second ROM |
| F62A | 63018 | F3BF | 62399 | 0000 |  | ROMFLG |  | Option ROM flag |
| F62B | 63019 |  |  | EEF4 | 61172 |  | CALPPS |  |
|  | 63020 |  |  |  | 61177 |  | FNKMAC |  |
| F639 | 63033 | F3E5 | 62437 | EF06 | 61190 | CSRY |  | Current cursor Y position |
| F63A | 63034 | F3E6 | 62438 | EF07 | 61191 | CSRX |  | Current cursor X positon |
| F63B | 63035 | F3E7 | 62439 | 0000 |  | LINCNT |  | Console height |
| F63C | 63036 | F3E8 | 62440 | 0000 |  | LINWDT |  | Console width |
|  | 63037 |  |  |  | 61194 |  |  |  |
| F63E | 63038 | F3EA | 62442 | EF0B | 61195 | LOKFLG | SCLFLG | Flag 00 = screen scrolls |
| F640 | 63040 | F3EC | 62444 | 0000 |  | LCDCSY |  | Cursor row (1-8) |
| F641 | 63041 | F3ED | 62445 | 0000 |  | LCDCSX |  | Cursor column (1-40) |
| F646 | 63046 | F3F2 | 62450 | 0000 |  | ESCCNT |  | ESC mode flag (0 normal/ non-zero escape sequence) |
| F648 | 63048 | F3F4 | 62452 | 0000 |  | REVFLG |  | Reverse video flag (FF=reverse/ 00=normal) |
| F64E | 63054 | F3FA | 62458 | 0000 |  | PRVCOO |  | X coordinate of last graphic point plotted |
| F64F | 63055 | F3FB | 62459 | 0000 |  | PRVCO2 |  | Y coordinate of last graphic point plotted * |
| F650 | 63056 | F3FC | 62460 | EF32 | 61234 | FNKMOD |  | Function key mode/ BIT 7=in TEXT; BIT 6=in TELCOM |
|  | 63058 |  |  |  | 61236 |  | ERRTRP |  |
|  | 63062 |  |  |  | 61239 |  |  |  |
| F658 | 63064 | F403 | 62467 | EF39 | 61241 | FULDUP | DUPFLG | Full/half duplex switch (FF=full duplex/ 00=half duplex) |
| F65A | 63066 | F405 | 62469 | EF3B | 61243 | LFFLG |  | Auto linefeed on RS232 output switch (non zero send line feeds with each carriage return) |
| F65B | 63067 | F406 | 62470 | EF3C | 61244 | SERMOD |  | Serial initialization string |
| F660 | 63072 | F40C | 62476 | 0000 |  | TMPHOK |  | Temporary hook |
| F661 | 63073 | F40D | 62477 | 0000 |  | TMPAD1 |  | Temporary hook address |
| F663 | 63075 | F40F | 62479 | 0000 |  | TMPAD2 |  | Temporary hook address 2 |
| F665 | 63077 | F411 | 62481 | 0000 |  | TMPAD3 |  | Temporary hook address 3 |
| F672 | 63090 | F453 | 62547 | 0000 |  | ERRFLG |  | Error code of last error |
| F674 | 63092 | F455 | 62549 | 0000 |  | LPTPOS |  | Line printer head position (based from zero) |
| F675 | 63093 | F456 | 62550 | 0000 |  | PRTFLG |  | Flag FF=send output to lpt |
| F67A | 63098 | F45B | 62555 | EF65 | 61285 | CURLIN |  | Current Basic executing line number |
|  | 63099 |  |  |  | 61286 |  |  |  |
| F67C | 63100 | F45D | 62557 | EF67 | 61287 | TXTTAB | CURBAS | Pointer to start of Basic programs |
|  | 63105 |  |  |  | 61292 |  | INPBFR |  |
| F685 | 63109 | F462 | 62562 | EF70 | 61296 | KBUF | INPBUF | Start of keyboard crunch buffer for line input routine |
| F788 | 63368 | F6A4 | 63140 | 0000 |  | TTYPOS |  | Current TTY (horizontal cursor) position (0-39) |
| F789 | 63369 | F6A5 | 63141 | F074 | 61556 | FNKSTR | KEYDSP | Function key definition area |
|  | 63449 |  |  |  | 61636 |  |  |  |
| F80A | 63498 | F7E6 | 63462 | 0000 |  | BASFNK |  | BASIC's function keys |
| F923 | 63779 | F832 | 63538 | 0000 |  | TIMSC1 |  | TIMBUF: Seconds (ones) |
| F924 | 63780 | F833 | 63539 | 0000 |  | TIMSC2 |  | TIMBUF+1: Seconds (tens) |
| F925 | 63781 | F834 | 63540 | 0000 |  | TIMMN1 |  | TIMBUF+2: Minutes (ones) |
| F926 | 63782 | F835 | 63541 | 0000 |  | TIMMN2 |  | TIMBUF+3: Minutes (tens) |
| F927 | 63783 | F836 | 63542 | 0000 |  | TIMHR1 |  | TIMBUF+4: Hours (ones) |
| F928 | 63784 | F837 | 63543 | 0000 |  | TIMHR2 |  | TIMBUF+5: Hours (tens) |
| F929 | 63785 | F838 | 63544 | 0000 |  | TIMDT1 |  | TIMBUF+6: Day (ones) |
| F92A | 63786 | F839 | 63545 | 0000 |  | TIMDT2 |  | TIMBUF+7: Day (tens) |
| F92B | 63787 | F83A | 63546 | 0000 |  | TIMDAY |  | TIMBUF+8: Day of week code (0=Sun / 1=Mon / etc..) **Not implemented?** |
| F92C | 63788 | F83B | 63547 | 0000 |  | TIMMON |  | TIMBUF+9: Current month |
| F92D | 63789 | F83C | 63548 | 0000 |  | TIMYR1 |  | TIMBUF+10: Year (ones) |
| F92E | 63790 | F83D | 63549 | 0000 |  | TIMYR2 |  | TIMBUF+11: Year (tens) |
| F92F | 63791 | F83E | 63550 | F21F | 61983 | TIMCNT | CSRITP | Counter (M200: 150 to 1 M100: 125 to 1) |
| F930 | 63792 | F83F | 63551 | 0000 |  | TIMCN2 |  | Counter (12 to 1) |
| F931 | 63793 | F840 | 63552 | 0000 |  | TIMINT |  | Power |
|  | 63794 |  |  |  | 61986 |  |  |  |
| F99A | 63898 | F870 | 63600 | F295 | 62101 | NULDIR |  | Address of non |
| F9A5 | 63909 | F87B | 63611 | 0000 |  | SCRDIR |  | Start of paste buffer |
|  | 63919 |  |  |  | 62122 |  |  |  |
|  | 64173 |  |  |  | 61194 |  |  |  |
| FABA | 64186 | F9AC | 63916 | 0000 |  | LSTLIN |  | Address of last BASIC line listed (decrunched) |
| FABE | 64190 | F9AE | 63918 | 0000 |  | STAKSV |  | Save area for stack pointer during power off state |
| FAC0 | 64192 | F9B0 | 63920 | F4EE | 62702 | BOTTOM | LOMEM | Lowest RAM address in system (8000H for 32K system) |
|  | 64194 |  |  |  | 62704 |  | CAPTUR |  |
|  | 64195 |  |  |  | 62705 |  |  |  |
|  | 64198 |  |  |  | 62708 |  |  |  |
| FAC9 | 64201 | F9BC | 63932 | 0000 |  | OFSSAV |  | Offset save for hook dispatch |
|  | 64206 |  |  |  | 62715 |  | TOP |  |
| FAD0 | 64208 | F9C2 | 63938 | F4FD | 62717 | BINLEN | LEN | Length of last program loaded or saved on tape |
|  | 64210 |  |  |  | 62719 |  | EXE |  |
|  | 64216 |  |  |  | 62725 |  |  |  |
| FADA | 64218 | F9CC | 63948 | F507 | 62727 | H.CLEAR |  | CLEAR hook (retadr) |
| FADC | 64220 | F9CE | 63950 | F509 | 62729 | H.MAXRAM |  | MAXRAM hook (retadr) |
| FADE | 64222 | F9D0 | 63952 | 0000 |  | H.CHGET1 |  | CHGET hook (retadr) |
| FAE0 | 64224 | F9D2 | 63954 | 0000 |  | H.CHSNS |  | CHSNS hook (retadr) |
| FAE2 | 64226 | F9D4 | 63956 | 0000 |  | H.CHPUT |  | LCD hook (retadr) |
| FAF0 | 64240 | F9E4 | 63972 | F51F | 62751 | H.SAVE |  | SAVE hook (retadr) |
| FAF4 | 64244 | F9E8 | 63976 | F523 | 62755 | H.MERGE |  | LOAD/MERGE hook (retadr) |
| FAF6 | 64246 | F9EA | 63978 | 0000 |  | H.NULOPN |  | OPEN hook (retadr) |
| FAFC | 64252 | F9F0 | 63984 | 0000 |  | H.BINSAV |  | SAVE(NM ERROR) hook (retadr) |
| FAFE | 64254 | F9F2 | 63986 | 0000 |  | H.BINLOD |  | LOAD(NM ERROR) hook (retadr) |
| FB00 | 64256 | F9F4 | 63988 | F52F | 62767 | H.EOF |  | EOF hook (retadr) |
|  | 64264 |  |  |  | 62775 |  |  |  |
|  | 64266 |  |  |  | 62777 |  |  |  |
| FB10 | 64272 | FA26 | 64038 | 0000 |  | H.UPLD |  | TELCOM(TERM |
| FB12 | 64274 | FA28 | 64040 | 0000 |  | H.TEXT |  | TEXT hook (retadr) |
| FB14 | 64276 | FA2A | 64042 | 0000 |  | H.WIDTHS |  | WIDTH hook (fcerr) |
| FB18 | 64280 | FA2C | 64044 | 0000 |  | H.SCREEN |  | SCREEN hook (fcerr) |
| FB1A | 64282 | FA2E | 64046 | 0000 |  | H.TVOPN |  | CRT open hook |
| FB1E | 64286 | FA32 | 64050 | 0000 |  | H.TVOUT |  | CRT put hook (fcerr) |
| FB20 | 64288 | FA38 | 64056 | 0000 |  | H.WAOPN |  | WAND open hook (fcerr) |
| FB22 | 64290 | FA3A | 64058 | 0000 |  | H.WACLS |  | WAND close hook (fcerr) |
| FB24 | 64292 | FA3C | 64060 | 0000 |  | H.WAINP |  | WAND get hook |
| FB26 | 64294 | FA3E | 64062 | 0000 |  | H.WABCK |  | WAND other hook (fcerr) |
| FB28 | 64296 | FA40 | 64064 | 0000 |  | H.LOF |  | LOF hook (fcerr) |
| FB2A | 64298 | FA42 | 64066 | 0000 |  | H.LOC |  | LOC hook (fcerr) |
| FB2C | 64300 | FA44 | 64068 | F55D | 62813 | H.LFILES |  | LFILES hook (fcerr) |
| FB2E | 64302 | FA46 | 64070 | 0000 |  | H.DSKI$ |  | DSKI$ hook (fcerr) |
| FB30 | 64304 | FA48 | 64072 | 0000 |  | H.DSKO$ |  | DSK0$ hook (fcerr) |
| FB32 | 64306 | FA4A | 64074 | F563 | 62819 | H.KILL |  | KILL hook (fcerr) |
| FB34 | 64308 | FA4C | 64076 | F565 | 62821 | H.NAME |  | NAME hook (fcerr) |
| FB36 | 64310 | FA4E | 64078 | F567 | 62823 | H.MSAVE |  | SAVEM hook (fcerr) |
| FB38 | 64312 | FA50 | 64080 | F569 | 62825 | H.MLOAD |  | LOADM/RUNM hook (fcerr) |
| FB62 | 64354 | FA88 | 64136 | 0000 |  | TXTEND |  | Pointer to end of .DO storage |
| FB65 | 64357 | FA8B | 64139 | 0000 |  | VALTYP |  | Type of last variable used |
| FB66 | 64358 | FA8C | 64140 | 0000 |  | DORES |  | Flag to tokenize reserved words in strings |
| FB69 | 64361 | FABF | 64191 | 0000 |  | FRETOP |  | Pointer to next free location in string buffer |
| FB8E | 64398 | FAC1 | 64193 | 0000 |  | TEMP3 |  | Multipurpose string register |
| FB94 | 64404 | FAC7 | 64199 | 0000 |  | DATLIN |  | Line number of active DATA statement |
| FB9B | 64411 | FACE | 64206 | 0000 |  | SAVTXT |  | Save for TXTPNT (current basic line/ used by RESUME) |
| FB9D | 64413 | FAD0 | 64208 | F650 | 63056 | SAVSTK | STKVAL | Save for stack pointer (used by RESUME) |
| FB9F | 64415 | FAD2 | 64210 | 0000 |  | ERRLIN |  | Line number of last Basic error |
| FBA1 | 64417 | FAD4 | 64212 | 0000 |  | DOT |  | Most recent entered/ listed/ or edited line |
| FBA3 | 64419 | FAD6 | 64214 | 0000 |  | ERRTXT |  | Points to line where error occurred |
| FBA5 | 64421 | FAD8 | 64216 | 0000 |  | ONELIN |  | Address of "ON ERROR GOTO" line |
| FBA7 | 64423 | FADA | 64218 | 0000 |  | ONEFLG |  | Error status flag (0=no error/ nz=in error routine) |
| FBA8 | 64424 | FADB | 64219 | 0000 |  | TEMP2 |  | Formula evaluator temporary storage |
| FBAA | 64426 | FADD | 64221 | 0000 |  | OLDLIN |  | Line number where Break occurred |
| FBAC | 64428 | FADF | 64223 | 0000 |  | OLDTXT |  | Next line to execute |
| FBAE | 64430 | FAE1 | 64225 | F661 | 63073 | ASCTAB | DOAREA | Pointer to start of ASCII files |
| FBB0 | 64432 | FAE3 | 64227 | F663 | 63075 | BINTAB |  | Pointer to start of binary files |
| FBB2 | 64434 | FAE5 | 64229 | F665 | 63077 | VARTAB | VARSPC | Pointer to start of simple variable space |
| FBB4 | 64436 | FAE7 | 64231 | F667 | 63079 | ARYTAB | VAREND | Pointer to start of array table |
| FBB6 | 64438 | FAE9 | 64233 | F669 | 63081 | STREND | FRESPC | End of storage/ first free byte |
| FBB8 | 64440 | FAEB | 64235 | 0000 |  | DATPTR |  | Pointer to current data item (message line) |
| FBBA | 64442 | FAED | 64237 | 0000 |  | DEFTBL |  | Variable type table |
| FBE8 | 64488 |  |  | F69B | 63131 |  |  | :number string stored here when 18187 is called |
| FC18 | 64536 | FB24 | 64292 | 0000 |  | DFACLO |  | Floating Point Accumulator (FAC1) |
| FC69 | 64617 | FB2E | 64302 | 0000 |  | ARGLO |  | Second FAC (FAC2) |
| FC7A | 64634 |  |  | F72D | 63277 |  | SEEDRD |  |
| FC82 | 64642 | FB62 | 64354 | 0000 |  | MAXFIL |  | Current maximum file number (read only) |
| FC83 | 64643 | FB63 | 64355 | 0000 |  | FILTAB |  | Pointer to basic file table |
| FC8C | 64652 |  |  | F73F | 63295 |  | DEVOUT |  |
| FC92 | 64658 |  |  | F745 | 63301 |  |  |  |
| FC93 | 64659 | FB78 | 64376 | F746 | 63302 | FILNAM | FLNM | 9 byte area for setting file names for search or open |
| FC99 | 64665 |  |  | F74C | 63308 |  |  |  |
| FC9C | 64668 | FB81 | 64385 | F74F | 63311 | FILNM2 |  | Second file name/ same format as above. Used by NAMEB |
| FCA7 | 64679 |  |  | F75A | 63322 |  |  |  |
| FCC0 | 64704 | FBC0 | 64448 | F7B0 | 63408 | LINE0 | ALTLCD | Screen buffer 0 (Previous page for Telcom) |
| FDA1 | 64929 |  |  |  | 63433 |  |  |  |
| FDD5 | 64981 |  |  |  | 63701 |  |  |  |
| FDD7 | 64983 |  |  |  | 63537 |  |  |  |
| FDEE | 65006 |  |  |  | 63560 | MENCNT |  |  |
| FDEF | 65007 |  |  |  | 63561 | FA2F |  |  |
| FDFF | 65023 | FCFF | 64767 | FA2F | 64047 | LINE0E | end ALTLCD | End of Screen buffer 0 |
| FE00 | 65024 | FD00 | 64768 | FA30 | 64048 | LINE1 | LCD | Screen buffer 1 (LCD memory) |
| FF3F | 65343 | FE3F | 65087 | FCAF | 64687 | LINE1E | end LCD | End of Screen Buffer 1 |
| FF40 | 65344 | FE40 | 65088 | FCF2 | 64754 | XONOFF |  | Flag (00) means XOF has not been received |
| FF41 | 65345 | FE41 | 65089 | 0000 |  | INHDSP |  | Flag (FF) XOF received |
| FF42 | 65346 | FE42 | 65090 | 0000 |  | INHBIT |  | Flag (0) XON/XOF disabled |
| FF46 | 65350 | FEC4 | 65220 | 0000 |  | COMBUF |  | Data buffer for COM: |
| FF86 | 65414 | FE45 | 65093 | 0000 |  | CMPNT |  | Number of bytes waiting in serial buffer |
| FF87 | 65415 | FE46 | 65094 | 0000 |  | RDADDR |  | Read pointer for COMBUF |
| FF88 | 65416 | FE47 | 65095 | 0000 |  | WTADDR |  | Write pointer for COMBUF |
| FF89 | 65417 | FE48 | 65096 | 0000 |  | CMERR |  | Number of characters in COMBUF when there was an error |
| FF8A | 65418 | FE49 | 65097 | 0000 |  | CMFLG |  | Flag (0)=XOF has been sent |
| FF8B | 65419 | FE4A | 65098 | 0000 |  | BAUDRT |  | Baud rate table entry address |
| FF8F | 65423 | FE4D | 65101 | FD03 | 64771 | KYSCNX | KBSITP | Flag to determine if key scan should be done |
| FF91 | 65425 | FE4F | 65103 | 0000 |  | KYDATA |  | Keyboard matrix read |
| FF99 | 65433 | FE60 | 65120 | FD0D | 64781 | KYMODE | PKGFF | Keyboard mode storage (brk//caps/num/cod/gph/ctl/sft) |
| FFA3 | 65443 | FE61 | 65121 | 0000 |  | KYHOW |  | Mode storage of last keypress for repeat |
| FFA2 | 65442 |  |  | FD16 | 64790 | KEYGPC |  |  |
| FFA4 | 65444 | FE62 | 65122 | FD18 | 64792 | KYREPT |  | Wait count for repeat |
| FFA5 | 65445 |  |  | FD19 | 64793 |  |  |  |
| FFA7 | 65447 |  |  | FD1B | 64795 |  |  |  |
| FFA8 | 65448 |  |  | FD1C | 64796 |  |  |  |
| FFAA | 65450 | FE68 | 65128 | FD1E | 64798 | KYBCNT |  | Number of characters in keyboard queue (KYRDBF) |
| FFAB | 65451 | FE69 | 65129 | FD1F | 64799 | KYRDBF |  | Keyboard buffer |
| FFEB | 65515 | FEA9 | 65193 | 0000 |  | BRKCHR |  | 0 until break is pressed. 03=Break |
| FFEC | 65516 | FEB1 | 65201 | 0000 |  | WORK1 |  | 6 byte buffer holding pattern under the cursor |
| FFF3 | 65523 | FEB8 | 65208 | FEA1 | 65185 | CSRCNT |  | Time until next cursor blink |
| FFF4 | 65524 | FEB9 | 65209 | 0000 |  | LCTEY |  | LCD row 1 |
| FFF5 | 65525 | FEBA | 65210 | 0000 |  | LCTEX |  | LCD column 1 |
