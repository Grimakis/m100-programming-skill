# Intel 8080/8085 Instruction Set (Opcode Reference)

Extracted from the *8080/8085 Assembly Language Programming Manual* (May 1981), Chapter 3.

- Each section is one instruction mnemonic (what you’d usually call an “opcode” in assembly).
- “Forms” shows the legal operand patterns, plus cycles/states/addressing mode/flags (when present).
- Examples are reproduced as shown in the manual (sometimes including bit patterns).

> Note: `RIM` and `SIM` are 8085-only.


## Table of contents
- [`ACI`](#aci) — Add Immediate With Carry
- [`ADC`](#adc) — Add With Carry
- [`ADD`](#add) — Add
- [`ADI`](#adi) — Add Immediate
- [`ANA`](#ana) — Logical And With Accumulator
- [`ANI`](#ani) — And Immediate With Accumulator
- [`CALL`](#call) — Call
- [`CC`](#cc) — Call If Carry
- [`CM`](#cm) — Call If Minus
- [`CMA`](#cma) — Complement Accumulator
- [`CMC`](#cmc) — Complement Carry
- [`CMP`](#cmp) — Compare
- [`CNC`](#cnc) — Call If No Carry
- [`CNZ`](#cnz) — Call If Not Zero
- [`CP`](#cp) — Call If Positive
- [`CPE`](#cpe) — Call If Parity Even
- [`CPO`](#cpo) — Call If Parity Odd
- [`CZ`](#cz) — Call If Zero
- [`DAA`](#daa) — Decimal Adj Ust Accumulator
- [`DAD`](#dad) — Double Register Add
- [`DCR`](#dcr) — Decrement Register or Memory
- [`DCX`](#dcx) — Decrement Register Pair
- [`DI`](#di) — Disable Interrupts
- [`EI`](#ei) — Enable Interrupts
- [`HLT`](#hlt) — Halt
- [`IN`](#in) — Input From Port
- [`INR`](#inr) — Increment Register or Memory
- [`INX`](#inx) — Increment Register Pair
- [`JC`](#jc) — Jump If Carry
- [`JM`](#jm) — Jump If Minus
- [`JMP`](#jmp) — Jump If Carry
- [`JNC`](#jnc) — Jump If No Carry
- [`JNZ`](#jnz) — Jump If Not Zero
- [`JP`](#jp) — Jump If Positive
- [`JPE`](#jpe) — Jump If Parity Even
- [`JPO`](#jpo) — Jump If Parity Odd
- [`JZ`](#jz) — Jump If Zero
- [`LDA`](#lda) — Load Accumulator Direct
- [`LDAX`](#ldax) — Load Accumulator  Indirect
- [`LHLD`](#lhld) — Load HL Direct
- [`LXI`](#lxi) — Load Register Pair Immediate
- [`MOV`](#mov) — A,M     ;Load Strng Into Accumulator
- [`MVI`](#mvi) — Move  Immediate
- [`NOP`](#nop) — No Operation
- [`ORA`](#ora) — Inclusive Or With Accumulator
- [`ORI`](#ori) — Inclusive Or Immediate
- [`OUT`](#out) — Output To Port
- [`PCHL`](#pchl) — Move H&L To Program Counter
- [`POP`](#pop) — Pop Register Pair
- [`PUSH`](#push) — Push Register Pair
- [`RAL`](#ral) — Rotate Left Through Carry
- [`RAR`](#rar) — Rotate Right Through Carry
- [`RC`](#rc) — Return If Carry
- [`RET`](#ret) — Return From -Subroutine
- [`RIM`](#rim) — Read Interrupt Mask / Serial Input (8085 only)
- [`RLC`](#rlc) — Rotate Accumulator Left
- [`RM`](#rm) — Return If Minus
- [`RNC`](#rnc) — Return If No Carry
- [`RNZ`](#rnz) — Return If Not Zero
- [`RP`](#rp) — Return If Positive
- [`RPE`](#rpe) — Return If Parity Even
- [`RPO`](#rpo) — Return If Parity Odd
- [`RRC`](#rrc) — Rotate Accumulator Right
- [`RST`](#rst) — Program
- [`RZ`](#rz) — Return If Zero
- [`SBB`](#sbb) — Subtract With Borrow
- [`SBI`](#sbi) — Subtract Immediate With Borrow
- [`SHLD`](#shld) — Store HL Direct
- [`SIM`](#sim) — Sim
- [`SPHL`](#sphl) — Move H& L To Sp
- [`STA`](#sta) — Store Accumulator Direct
- [`STAX`](#stax) — Store Accumulator Indirect
- [`STC`](#stc) — Set Carry
- [`SUB`](#sub) — Subtract
- [`SUI`](#sui) — Subtract Immediate
- [`XCHG`](#xchg) — Exchange HL With D And E
- [`XRA`](#xra) — Exclusive Or With Accumulator
- [`XRI`](#xri) — Exclusive Or Immediate With Accumulator
- [`XTHL`](#xthl) — Exchange H&L With Top Of Stack

---

<a id="aci"></a>

## `ACI` — Add Immediate With Carry

ACI adds the contents of the second instruction byte and the carry bit to the contents of the accumulator and stores the result in the accumulator.

### Forms

```asm
ACI         data
```

- Cycles: 2 | States: 7 | Addressing: immediate | Flags: Z,S,P,CY,AC

The operand specifies the actual data to be added to the accumulator except, of course, for the carry bit. Data may be in the form of a number, an ASCII constant, the label of a previously defined value, or an expression. The data may not exceed one byte. The assembler's relocation feature treats all external and relocatable symbols as 16-bit addresses. When one of these symbols appears in the operand expression of an immediate instruction, it must be preceded by either the > HIGH or LOW operator to specify which byte of the address is to be used in the evaluation of the expression. When neither operator is present, the assembler assumes the LOW operator and issues an error message. o  0         o data

### Examples

```text
Assume that the accumulator contains the value 14H and that the carry bit is set to one. The instruction ACI 66
has the following effect:
Accumulator = 14H 0001 0100
Immediate data = 42H 01000010
Carry     1
01010111 57H
```

---

<a id="adc"></a>

## `ADC` — Add With Carry

The ADC instruction adds one byte of data plus the setting of the carry flag to the contents of the accumulator. The result is stored in the accumulator. ADC then updates the setting of the carry flag to indicate the outcome of the operation. The ADC instruction's use of the carry bit enables the program to add multi-byte numeric strings. Add Register to Accumulator with Carry

### Forms

```asm
ADC         reg
```

- Cycles: 1 | States: 4 | Addressing: register | Flags: Z,S,P,CY,AC

The operand must specify one of the registers A through E, H or L. This instruction adds the contents of the specified register and the carry bit to the accumulator and stores the result in the accumulator. Add Memory to Accumulator with Carry

```asm
ADC        M
```

- Cycles: 2 | States: 7 | Addressing: register indirect | Flags: Z,S,P,CY,AC

This instruction adds the contents of the memory location addressed by the HL register pair and the carry bit to the accumulator and stores the result in the accumulator. M is a symbolic reference to the HL register pair.

### Examples

```text
Assume that register C contains 3DH, the accumulator contains 42H, and the carry bit is set to zero. The
instruction ADC C performs the addition as follows:
3DH  001111 01
42H  01000010
o
CARRY
01111111 = 7FH
The condition flags are set as follows:
Carry     0
Sign      0
Zero      0
Parity    0
Aux. Carry 0
If the carry bit is set to one, the instruction has the following results:
3DH 00111101
42H 01000010
CARRY        1
10000000 80H
Carry      0
Sign
Zero       0
Parity     0
Aux. Carry
```

---

<a id="add"></a>

## `ADD` — Add

The ADD instruction adds one byte of data to the contents of the accumulator. The result is stored in the accumulator. Notice that the ADD instruction excludes the carry flag from the addition but sets the flag to indicate the outcome of the operation.

### Forms

```asm
ADD        reg
```

- Cycles: 1 | States: 4 | Addressing: register | Flags: Z,S,P,CY,AC

The operand must specify one of the registers A through E, H or L. The instruction adds the contents of the specified register to the contents of the accumulator and stores the result in the accumulator. Is 11  0 0  0 0     S SI Add From Memory

```asm
ADD        M
```

- Cycles: 2 | States: 7 | Addressing: register indirect | Flags: Z,S,P,CY,AC

This instruction adds the contents of the memory location addressed by the HL register pair to the contents of the accumulator and stores the result in the accumulator. M is a symbolic reference to the HL register pair. 11 0 0  0 0 34 Examples: Assume that the accumulator contains 6CH and register D contains 2EH. The instruction ADD D performs the addition as follows: 2 E H 001 0111 0 6CH  01101100 9 A H 10 01 "1 01 0 The accumulator contains the value 9AH following execution of the ADD D instruction. The contents of the D register remain unchanged. The condition flags are set as follows: Carry     = 0 Sign        1 Zero        0 Parity Aux. Carry The following instruction doubles the contents of the accumulator: ADD A

---

<a id="adi"></a>

## `ADI` — Add Immediate

ADI adds the contents of the second instruction byte of the contents of the accumulator and stores the result in the accumulator.

### Forms

```asm
ADI        data
```

- Cycles: 2 | States: 7 | Addressing: immediate | Flags: Z,S,P,CY,AC

The operand specifies the actual data to be added to the accumulator. This data may be in the form of a number, an ASCII constant, the label of a previously defined value, or an expression. The data may not exceed one byte. The assembler's relocation feature treats all external and relocatable symbols as 16-bit addresses. When one of these symbols appears in the operand expression of an immediate instruction, it must be preceded by either the HIGH or LOW operator to specify which byte of the address is to be used in the evaluation of the expression. When neither operator is present, the assembler assumes the LOW operator and issues an error message. 000 data

### Examples

```text
Assume that the accumulator contains the value 14H. The illstruction ADI 66 has the following effect:
Accumulator 14H 00010100
Immediate data 42H 01000010
01010110 = 56H
Notice that the assembler converts the decimal value 66 into the hexadecimal value 42.
```

---

<a id="ana"></a>

## `ANA` — Logical And With Accumulator

ANA                                       LOGICAL AND WITH ACCUMULATOR ANA performs a logical AND operation using the contents of the specified byte and the accumulator. The result is placed in the accumulator. Summary of Logical Operations AND produces a one bit in the result only when the corresponding bits in the test data and the mask data are ones. OR produces a one bit in the result when the corresponding bits in either the test data or the mask data are ones. Exclusive OR produces a one bit only when the corresponding bits in the test data and the mask data are different; i.e., a one bit in either the test data or the mask data - but not both - produces a one bit in the result. AND         OR      EXCLUSIVE OR 1010 1010  1010 1010   1010 1010 0000 1111  0000 1111   0000 1111 0000 1010  10101111    1010 0101 AND Register with Accumulator

### Forms

```asm
ANA        reg
```

- States: 4 | Addressing: register | Flags: Z,S,P,CY,AC

The operand must specify one of the registers A through E, H or L. This instruction ANDs the contents of the specified register with the accumulator and stores the result in the accumulator. The carry flag is reset to zero. I     sl 0    0  0 S  S 11 AND Memory with Accumulator

```asm
ANA         M
```

- Cycles: 2 | States: 7 | Addressing: register indirect | Flags: Z,S,P,CY,AC

This instruction ANDs the contents of the specified memory location with the accumulator and stores the result in the accumulator. The carry flag is reset to zero. ~_O                O~I ____O_ _O_ _____

### Examples

```text
Since any bit ANDed with a zero produces a zero and any bit ANDed with a one remains unchanged, AND is
frequently used to zero particular groups of bits. The following example ensures that the high-order four bits of
the accumulator are zero, and the low-order four bits ar~ unchanged. Assume that the C register contains OFH:
o
Accumulator 1 1 1 1    0  OFCH
C Register o 000       1  OFH
000  0     o 0  OCH
```

---

<a id="ani"></a>

## `ANI` — And Immediate With Accumulator

ANI                                      AND IMMEDIATE WITH ACCUMULATOR AN I performs a logical AND operation using the contents of the second byte of the instruction and the accumu lator. The result is placed in the accumulator. ANI also resets the carry flag to zero. Op co de    Operand ANI         data The operand must specify the data to be used in the AND operation. This data may be in the form of a number, an ASCII constant, the label of some previously defined value, or an expression. The data may not exceed one byte. The assembler's relocation feature treats all external and relocatable symbols as 16-bit addresses. When one of these symbols appears in the operand expression of an immediate instruction, it must be preceded by either the HIGH or LOW operator to specify which byte of the address is to be used in the evaluation of the expression. When neither operator is present, the assembler assumes the LOW operator and issues an error message. o  0 data Cycles:     2 States:     7 Addressing: immediate Flags:      Z,S,P,CY,AC Summary of Logical Operations AND produces a one bit in the result only when the corresponding bits in the test data and the mask data are ones. OR produces a one bit in the result when the corresponding bits in either the test data or the mask data are ones. Exclusive OR produces a one bit only when the corresponding bits in the test data and the mask data are different; i.e., a one bit in either the test data or the mask data - but not both - produces a one bit in the result. AND         OR      EXCLUSIVE OR 1010 1010  1010 1010   1010 1010 0000 1111  0000 1111   0000 1111 0000 '1010 10101111    10100101 Example: The following instruction is used to reset OFF bit six of the byte in the accumulator: ANI       101111118 Since any bit ANDed with a one remains unchanged and a bit ANDed with a zero is rest to zero, the ANI instruction shown above sets bit six OFF and leaves the others unchanged. This technique is useful when a program uses individual bits as status flags.

---

<a id="call"></a>

## `CALL` — Call

The CALL instruction combines functions of the PUSH and J MP instructions. CALL pushes the contents of the program counter (the address of the next sequential instruction) onto the stack and then jumps to the address specified in the CALL instruction. Each CALL instruction or one of its variants implies the use of a subsequent RET (return) instruction. When a call has no corresponding return, excess addresses are built up in the stack. Op co de    Operand The address may be specified as a number, a label, or an expression. (The label is most common.) The assembler inverts the high and low address bytes when it assembles the instruction.

---

<a id="cc"></a>

## `CC` — Call If Carry

The CC instruction combines functions of the JC and PUSH instructions. CC tests the setting of the carry flag. If the flag is set to one, CC pushes the contents of the program counter onto the stack and then jumps to the address specified in bytes two and three of the CC instruction. If the flag is reset to zero, program execution continues with the next sequential instruction.

### Forms

```asm
CC         address
```

- Cycles: 3 or 5 (2 or 5 on 8085) | States: 11 or 17 (9 or 18 on 8085) | Addressing: immediate/register indirect | Flags: none

### Examples

```text
For the sake of brevity, an example is given for the CALL instruction but not for each of its closely related
variants.
```

---

<a id="cm"></a>

## `CM` — Call If Minus

The CM instruction combines functions of the J M and PUSH instructions. CM tests the setting of the sign flag. If the flag is set to one (indicating that the contents of the accumulator are minus), CM pushes the contents of the program counter onto the stack and then jumps to the address specified by the CM instruction. If the flag is set to zero, program execution simply continues with the next sequential instruction.

### Forms

```asm
CM          address
```

- Cycles: 3 or 5 (2 or 5 on 8085) | States: 11 or 17 (9 or 18 on 8085) | Addressing: immediate/register indirect | Flags: none

### Examples

```text
For the sake of brevity, an example is given for the CALL instruction but not for each of its closely related
variants.
```

---

<a id="cma"></a>

## `CMA` — Complement Accumulator

CMA complements each bit of the accumulator to produce the one's complement. All condition flags remain unchanged.

### Forms

```asm
CMA
```

- States: 4 | Flags: none

To produce the two's complement, add one to the contents of the accumulator after the CMA instructions has been executed.

### Examples

```text
Assume that the accumulator contains the value 51 H; when complemented by CMA, it becomes OAEH:
51H     01 01 0001
OAEH    10101110
```

---

<a id="cmc"></a>

## `CMC` — Complement Carry

If the carry flag equals zero, CMC sets it to one. If the carry flag is one, CMC resets it to zero. All other flags remain unchanged.

### Forms

```asm
CMC
```

- States: 4 | Flags: CYonly

### Examples

```text
Assume that a program uses bit 7 of a byte to control whether a subroutine is called. To test the bit, the pro
gram loads the byte into the accumulator, rotates bit 7 into the carry flag, and executes a CC (Call if Carry)
instruction. Before returning to the calling program, the subroutine reinitializes the flag byte using the following
code:
CMC     ;SET BIT 7 OFF
RAR     ;ROTATE BIT 7 INTO ACCUMULATOR
RET     ;RETURN
CMP                                           COMPARE WITH ACCUMULATOR
```

---

<a id="cmp"></a>

## `CMP` — sl

CMP compares the specified byte with the contents of the accumulator and indicates the result by setting the carry and zero flags. The values being compared remain unchanged. The zero flag indicates equality. No carry indicates that the accumulator is greater than or equal to the specified byte; a carry indicates that the accumulator is less than the byte. However, the meaning of the carry flag is reversed when the values have different signs or one of the values is complemented. The program tests the condition flags using one of the conditional Jump, Call, or Return instructions. For example, J Z (J ump if Zero) tests for equality. Functional Description: Comparisons are performed by subtracting the specified byte from the contents of the accumulator, which is why the zero and carry flags indicate the result. This subtraction uses the processor's internal registers so that source data is preserved. Because subtraction uses two's complement addition, the CMP instruction recomplements the carry flag generated by the subtraction. Compare Register with Accumulator

### Forms

```asm
CMP         reg
```

- States: 4 | Addressing: register | Flags: Z,S,P,CY,AC

The operand must name one of the registers A through E, H or L. sl o          S S Compare Memory with Accumulator

```asm
CMP         M
```

- Cycles: 2 | States: 7 | Addressing: register indirect | Flags: Z,S,P,CY,AC

This instruction compares the contents of the memory location addressed by the HL register pair with the contents of the accumulator. M is a symbolic reference to the HL register pair. Example 1: Assume that the accumulator contains the value OAH and register E contains the value OSH. The instruction CMP E performs the following internal subtraction (remember that subtraction is actually two's complement addition) : Accumulator = 00001010 +( -E Register) 11111011 000001 01 + ( -carry) After the carry is complemented to account for the subtract operation, both the zero and carry bits are zero, thus indicating A greater than E. Example 2: Assume that the accumulator contains the value -1 BH and register E contains OSH: Accumulator 111 00101 +( -E Register) 11111011 11100000 +( -carry) 3·13 After the CMP instruction recomplements the carry flag, both the carry flag and zero flag are zero. Normally this indicates that the accumulator is greater than register E. However, the meaning of the carry flag is reversed since the values have different signs. The user program is responsible for proper interpretation of the carry flag.

---

<a id="cnc"></a>

## `CNC` — Call If No Carry

The CNC instruction combines functions of the J NC and PUSH instructions. CNC tests the setting of the carry flag. If the flag is set to zero, CNC pushes the contents of the program counter onto the stack and then jumps to the address specified by the CNC instruction. If the flag is set to one, program execution simply continues with the next sequential instruction.

### Forms

#### with the next sequential instruction.

```asm
CNC         address
```

- Cycles: 3 or 5 (2 or 5 on 8085) | States: 11 or "17 (9 or 18 on 8085) | Addressing: immediate/register indirect | Flags: none

### Examples

```text
For the sake of brevity, an example is given for the CALL instruction but not for each of its closely related
variants.
```

---

<a id="cnz"></a>

## `CNZ` — Call If Not Zero

The CNZ instruction combines functions of the J NZ and PUSH instructions. CNZ tests the setting of the zero flag. If the flag is off (indicating that the contents of the accumulator are other than zero), CNZ pushes the contents of the program counter onto the stack and then jumps to the address specified in the instruction's second and third bytes. If the flag is set to one, program execution simply continues with the next sequential instruction.

### Forms

```asm
CNZ         address
```

- Cycles: 3 or 5 (2 or 5 on 8085) | States: 1"1 or 17 (9 or 18 on 8085) | Addressing: immediate/register indirect | Flags: none

### Examples

```text
For the sake of brevity, an example is given for the CALL instruction but not for each of its closely related
variants.
```

---

<a id="cp"></a>

## `CP` — Call If Positive

The CP instruction combines features of the J P and PUSH instructions. CP tests the setting of the sign flag. If the flag is set to zero (indicating that the contents of the accumulator are positive), CP pushes the contents of the program counter onto the stack and then jumps to the address specified by the CP instruction. If the flag is set to one, program execution simply continues with the next sequential instruction.

### Forms

```asm
CP          address
```

- Cycles: 3 or 5 (2 or 5 on 8085) | States: 11 or 17 (9 or 18 on 8085) | Addressing: immediate/register indirect | Flags: none

### Examples

```text
For the sake of brevity, an example is given for the CALL instruction but not for each of its closely related
variants.
```

---

<a id="cpe"></a>

## `CPE` — Call If Parity Even

Parity is even if the byte in the accumulator has an even number of one bits. The parity flag is set to one to indicate this condition. The CPE and CPO instructions are useful for testing the parity of input data. However, the IN instruction does not set any of the condition flags. The flags can be set without altering the data by adding OOH to the contents of the accumulator. The CPE instruction combines functions of the J PE and PUSH instructions. CPE tests the setting of the parity flag. If the flag is set to one, CPE pushes the contents of the program counter onto the stack and then jumps to the address specified by the CPE instruction. If the flag is set to zero, program execution simply continues with the next sequential instruction.

### Forms

```asm
CPE        address
```

- Cycles: 3 or 5 (2 or 5 on 8085) | States: 11 or 17 (9 or 18 on 8085) | Addressing: immediate/register indirect | Flags: none

```asm
CPI        data
```

- Cycles: 2 | States: 7 | Addressing: register indirect | Flags: Z,S,P,CY,AC

The operand must specify the data to be compared. This data may be in the form of a number, an ASCII constant, the label of a previously defined value, or an expression. The data may not exceed one byte. The assembler's relocation feature treats all external and relocatable symbols as 16-bit addresses. When one of these symbols appears in the operand expression of an immediate instruction, it must be preceded by either the HIGH or LOW operator to specify which byte of the address is to be used in the evaluation of the expression. When neither operator is present, the assembler assumes the LOW operator and issues an error message. o data

### Examples

```text
For the sake of brevity, an example is given for the CALL instruction but not for each of its closely related
variants.
CPI                                                  COMPARE IMMEDIATE
CPI compares the contents of the second instruction byte with the contents of the accumulator and sets the zero
and carry flags to indicate the result. The values being compared remain unchanged.
The zero flag indicates equality. No carry indicates that the contents of the accumulator are greater than the
immediate data; a carry indicates that the accumulator is less than the immediate data. However, the meaning
of the carry flag is reversed when the values have different signs or one of the values is complemented.
```

```text
The instruction CPI IC' compares the contents of the accumulator to the letter C (43H).
```

---

<a id="cpo"></a>

## `CPO` — Call If Parity Odd

Parity is odd if the byte in the accumulator has an odd number of one bits. The parity flag is set to zero to indicate this condition. The CPO and ePE instructions are useful for testing the parity of input data. However, the I N instruction does not set any of the condition flags. The flags can be set without altering the data by adding OOH to the contents of the accumulator. The CPO instruction combines functions of the J PO and PUSH instructions. CPO tests the setting of the parity flag. If the flag is set to zero, CPO pushes the contents of the program counter onto the stack and then jumps to the address specified by the CPO instruction. If the flag is set to one, program execution simply continues with the next sequential instruction.

### Forms

```asm
CPO         address
```

- Cycles: 3 or 5 (2 or 5 on 8085) | States: 11 or 17 (9 or 18 on 8085) | Addressing: immediate/register indirect | Flags: none

### Examples

```text
For the sake of brevity, an example is given for the CALL instruction but not for each of its closely related
variants.
```

---

<a id="cz"></a>

## `CZ` — Call If Zero

The CZ instruction combines functions of the JZ and PUSH instructions. CZ tests the setting of the zero flag. If the flag is set to one (indicating that the contents of the accumulator are zero), CZ pushes the contents of the program counter onto the stack and then jumps to the address specified in the CZ instruction. If the flag is set to zero (indicating that the contents of the accumulator are other than zero), program execution simply continues with the next sequential instruction.

### Forms

```asm
CZ          address
```

- Cycles: 3 or 5 (2 or 5 on 8085) | States: 11 or "17 (9 or 18 on 8085) | Addressing: immediate/register indirect | Flags: none

### Examples

```text
For the sake of brevity, an example is given for the CALL instruction but not for each of its closely related
variants.
```

---

<a id="daa"></a>

## `DAA` — Decimal Adj Ust Accumulator

The DAA instruction adjusts the eight-bit value in the accumulator to form two four-bit binary coded decimal digits.

### Forms

```asm
DAA
DAA is used when adding decimal numbers. It is the only instruction whose function requires use of the auxiliary
DAA operates as follows:
```

- States: 4 | Addressing: register | Flags: Z,S,P,CY,AC

### Examples

```text
Assume that the accumulator contains the value 9BH as a result of adding 08 to 93:
CY   AC
a    a
1001 0011
0000 1000
1001 1011 = 9BH
Since OBH is greater than nine, the instruction adds six to contents of the accumulator:
CY   AC
a
1001 1011
0000 0110
1 01 a 000 1 = A1 H
Now that the most significant bits have a value greater than nine, the instruction adds six to them:
CY   AC
1
1010 0001
0110 0000
0000 0001
When the DAA has finished, the accumulator contains the value 01 in a BCD format; both the carry and auxiliary
carry flags are set ON. Since the actual result of this addition is 101, the carry flag is probably significant to the
program. The program is responsible for recovering and using this information. Notice that the carry flag setting is
, lost as soon as the program executes any subsequent instruction that alters the flag.
```

---

<a id="dad"></a>

## `DAD` — Double Register Add

DAD adds the 16-bit value in the specified register pair to the contents of the HL register pair. The result is stored in HL.

### Forms

```asm
DAD
DAD may add only the contents of the B&C, D&E, H&L, or the SP (Stack Pointer) register pairs to the contents
DAD sets the carry flag ON if there is a carry out of the HL registers. DAD affects none of the condition
```

- Cycles: 3 | States: 10 | Addressing: register | Flags: CY

Examples: The DAD instruction provides a means for saving the current contents of the stack pointer. LXI  H,OOH  ;CLEAR H& L TO ZEROS DAD  SP     ;GET SP INTO H&L SHLD SAVSP  ;STORE SP IN MEMORY The instruction DAD H doubles the number in the HL registers except when the operation causes a carry ou t of the H register. DCR                                                         DECREMENT

---

<a id="dcr"></a>

## `DCR` — o     o

DCR subtracts one from the contents of the specified byte. DCR affects all the condition flags except the carry flag. Because DCR preserves the carry flag, it can be used within multi-byte arithmetic routines for decrementing character counts and similar purposes. Decrement Register

### Forms

```asm
DCR         reg
```

- Cycles: 1 | States: 5 (4 on 8085) | Addressing: register | Flags: Z,S,P,AC

The operand must specify one of the registers A through E, H or L. Thp- instruction subtracts one from the contents of the specified register. EiIDDD           0 Decrement Memory

```asm
DCR        M
```

- Cycles: 3 | States: 10 | Addressing: register indirect | Flags: Z,S,P,AC

This instruction subtracts one from the contents of the memory location addressed by the HL register pair. M is a symbolic reference to the memory byte addressed by the HL register pair. o     o

### Examples

```text
The DCR instruction is frequently used to control multi-byte operations such as moving a number of characters
from one area of memory to another:
MVI  B,5H   ; set control counter
LXI  H,250H ; load H & L with source address
LXI  D,900H ; load D & E with destination address
LOOP: MOV A,M   ; load byte to be moved
STAX D      ; store byte
DCX  D      ; decrement destination address
DCX  H      ; decrement source address
DCR  B      ; decrement control counter
XRA  A      ; clear accumulator
CMP   B     ; compare control counter to zero
JNZ   LOOP  ; move another byte if counter not zero
```

---

<a id="dcx"></a>

## `DCX` — Decrement Register Pair

DCX decrements the contents of the specified register pair by one. DCX affects none of the condition flags. Because DCX preserves all the flags, it can be used for address modification in any instruction sequence that relies on the passing of the flags.

### Forms

#### relies on the passing of the flags.

```asm
DCX
DCX may decrement only the B&C, O&E, H&L, or the SP (Stack Pointer) register pairs. Notice that the letter
```

- States: 5 (6 on 8085) | Addressing: register | Flags: none

### Examples

```text
Assume that the HL registers contain the address 9800H when the instruction DCX H is executed. DCX
considers the contents of the two registers to be a single 16-bit value and therefore performs a borrow from the
H register to produce the value 97FFH.
```

---

<a id="di"></a>

## `DI` — Disable Interrupts

The interrupt system is disabled when the processor recognizes an interrupt or immediately following execution of a 01 instruction. In applications that use interrupts, the 01 instruction is commonly used only when a code sequence must not be interrupted. For example, time-dependent code sequences become inaccurate when interrupted. You can disable the interrupt system by including a 01 instruction at the beginning of the code sequence. Because you cannot predict the occurrence of an interrupt, include an EI instruction at the end of the time-dependent code sequence.

### Forms

- States: 4 | Flags: none

NOTE The 8085 TRAP interrupt cannot be disabled. This special interrupt is intended for serious problems that must be serviced regardless of the interrupt flag such as power failure or bus error. However, no interrupt including TRAP can interrupt the execution of the 01 or EI instruction.

---

<a id="ei"></a>

## `EI` — Enable Interrupts

The EI instruction enables the interrupt system following execution of the next program instruction. Enabling the interrupt system is delayed one instruction to allow interrupt subroutines to return to the main program before;! subsequent interrupt is acknowledged. In applications that use interrupts, the interrupt system is usually disabled only when the processor accepts an interrupt or when a code sequence must not be interrupted. You can disable the interrupt system by including a 01 instruction at the beginning of the code sequence. Because you cannot predict the occurrence of an interrupt, incl ude an E I instruction at the end of the code sequence.

### Forms

```asm
EI
```

- Cycles: 1 | States: 4 | Flags: none

NOTE The 8085 TRAP interrupt cannot be disabled. This special interrupt is _ intended for serious problems that must be serviced regardless of the interrupt flag such as power failure or bus failure. However, no interrupt including TRAP can interrupt the execution of the 01 or EI instruction.

### Examples

```text
The EI instruction is frequently used as part of a start-up sequence. When power is first applied, the processor
begins operating at some indeterminate address. Application of a RESET signal forces the program counter to
3·23
zero. A common instruction sequence at this point is EI, HLT. These instructions enable the interrupt system
(RESET also disables the interrupt system) and halt the processor. A subsequent manual or automatic interrupt
then determ ines the effective start-up address.
```

---

<a id="hlt"></a>

## `HLT` — Halt

The HLT instruction halts the processor. The program counter contains the address of the next sequential instruction. Otherwise, the flags and registers remain unchanged. 0 01 0 1 Cycles:     1 States:     7 (5 on 8085) Flags:     none Once in the halt state, the processor can be restarted only by an external event, typically an interrupt. Therefore, you should be certain that interrupts are enabled before the HLT instruction is executed. See the description of the EI (Enable Interrupt) instruction. If an 8080 HLT instruction is executed while interrupts are disabled, the only way to restart the processor is by application of a RESET signal. This forces the program counter to zero. The same is true of the 8085, except for the TRAP interrupt, which is recognized even when the interrupt system is disabled. The processor can temporarily leave the halt state to service a direct memory access request. However, the pro cessor reenters the halt state once the request has been serviced. A basic purpose for the HLT instruction is to allow the processor to pause while waiting for an interrupt from a peripheral device. However, a halt wastes processor resources and should be used only when there is no useful processing task available.

---

<a id="in"></a>

## `IN` — Input From Port

The IN instruction reads eight bits of data from the specified port and loads it into the accumulator. NOTE This description is restricted to the exact function of the IN instruction. Input/output structures are described in the 8080 or 8085 Microcomputer Systems User's Manual.

### Forms

```asm
IN          exp
```

- Cycles: 3 | States: 10 | Addressing: direct | Flags: none

The operand expression may be a number or any expression that yields a value in the range OOH through OFFH. o       o exp INR                                                          INCREMENT

---

<a id="inr"></a>

## `INR` — Eo

INR adds one to the contents of the specified byte. INR affects all of the condition flags except the carry flag. Because INR preserves the carry flag, it can be used within multi-byte arithmetic routines for incrementing character counts and similar purposes. Increment Register

### Forms

```asm
INR         reg
```

- States: 5 (4 on 8085) | Addressing: register | Flags: Z,S,P,AC

The operand must specify one of the registers A through E, H or L. The instruction adds one to the contents of the specified register. Eo I            o   I D D  D       0 Increment Memory

```asm
INR         M
```

- Cycles: 3 | States: 10 | Addressing: register indirect | Flags: Z,S,P,AC

This instruction increments by one the contents of the memory location addressed by the HL register pair. M is a symbolic reference to the HL register pair. ~_0                 0~1 _____0_ _ ___0_ _

### Examples

```text
If register C contains 99H, the instruction I NR C increments the contents of the register to 9AH.
```

---

<a id="inx"></a>

## `INX` — Increment Register Pair

INX adds one to the contents of the specified register pair. INX affects none of the condition flags. Because INX preserves all the condition flags, it can be used for address modification within multi-byte arithmetic routines.

### Forms

```asm
INX
INX may increment only the B&C, D&E, H& L, or the SP (Stack Pointer) register pairs. Notice that the letter H
PO
```

- Cycles: 1 | States: 5 (6 on 8085) | Addressing: register | Flags: none

### Examples

```text
Assume that the D and E registers contain the value 01 F FH. The instruction INX D increments the value to
0200H. By contrast, the INR E instruction ignores the carry out of the low-order byte and produces a result of
01 OOH. (This condition can be detected by testing the Zero condition flag.)
If the stack pointer register contains the value OFFFFH, the instruction INX SP increments the contents of SP
to OOOOH. The INX instruction sets no flags to indicate this condition.
```

---

<a id="jc"></a>

## `JC` — Jump If Carry

The JC instruction tests the setting of the carry flag. If the flag is set to one, program execution resumes at the address specified in the JC instruction. If the flag is reset to zero, execution continues with the next sequential instruction.

### Forms

```asm
JC          address
```

- Cycles: 3 (2 or 3 on 8085) | States: 10 (7 or lOon 8085) | Addressing: immediate | Flags: none

The address may be specified as a number, a label, or an expression. The assembler inverts the high and low address bytes when it assembles the instruction.

### Examples

```text
Examples of the variations of the jump instruction appear in the description of the J PO instruction.
```

---

<a id="jm"></a>

## `JM` — Jump If Minus

The J M instruction tests the setting of the sign flag. If the contents of the accumulator are negative (sign flag = 1), program execution resumes at the address specified in the J M instruction. If the contents of the accumulator are positive (sign flag = 0), execution continues with the next sequential instruction.

### Forms

```asm
JM          address
```

- Cycles: 3 (2 or 3 on 8085) | States: 10 (7 or lOon 8085) | Addressing: immediate | Flags: none

The address may be specified as a number, a label, or an expression. The assembler inverts the high and low address bytes when it assembles the instructions. lowaddr highaddr

### Examples

```text
Examples of the variations of the jump instruction appear in the description of the J PO instruction.
jMP                                                               JUMP
The J MP instruction alters the execution sequence by loading the address in its second and third bytes into the
program counter.
```

---

<a id="jmp"></a>

## `JMP` — Jump If Carry

JMP address The address may be specified as a number, a label, or an expression. The assembler inverts the high and low address bytes when it assembles the address. 1 . lowaddr highaddr Cycles: 3 States: 10 Addressing: immediate Flags: none Example: Examples of the variations of the jump instruction appear in the description of the JPO instruction. jNC JUMP IF NO CARRY

---

<a id="jnc"></a>

## `JNC` — Jump If No Carry

The JNC instruction tests the setting of the carry flag. If there is no carry (carry flag = 0), program execution resumes at the address specified in the J NC instruction. If there is a carry (carry flag =1), execution continues with the next sequential instruction.

### Forms

```asm
JNC         address
```

- Cycles: 3 (2 or 3 on 8085) | States: 10 (7 or 10 on 8085) | Addressing: immediate | Flags: none

The address may be specified as a number, a label, or an expression. The assembler inverts the high and low address bytes when it assembles the instruction.

### Examples

```text
Examples of the variations of the jump instruction appear in the description of the J PO instruction.
```

---

<a id="jnz"></a>

## `JNZ` — Jump If Not Zero

The J NZ instruction tests the setting of the zero flag. If the contents of the accumulator are not zero (zero flag = 0), program execution resumes at the address specified in the JN Z instruction. If the contents of the accumulator are zero (zero flag = 1), execution continues with the next sequential instruction.

### Forms

```asm
JNZ         address
```

- Cycles: 3 (2 or 3 on 8085) | States: 10 (7 or 10 on 8085) | Addressing: immediate | Flags: none

The address may be specified as a number, a label, or an expression. The assembler inverts the high and low address bytes when it assembles the instruction.

### Examples

```text
Examples of the variations of the jump instruction appear in the description of the J PO instruction.
```

---

<a id="jp"></a>

## `JP` — Jump If Positive

The J P instruction tests the setting of the sign flag. If the contents of the accumulator are positive (sign flag = 0), program execution resumes at the address specified in the J P instruction. If the contents of the accumulator are minus (sign flag = 1), execution continues with the next sequential instruction.

### Forms

```asm
JP         address
```

- Cycles: 3 (2 or 3 on 8085) | States: 10 (7 or 10 on 8085) | Addressing: immediate | Flags: none

The address may be specified as a nu'mber, a label, or an expression. The assembler inverts the high and low order address bytes when it assembles the instruction.

### Examples

```text
Examples of the variations of the jump instruction appear in the description of the J PO instruction.
```

---

<a id="jpe"></a>

## `JPE` — Jump If Parity Even

Parity is even if the byte in the accumulator has an even number of one bits. The parity flag is set to one to indicate this condition. The J PE instruction tests the setting of the parity flag. If the parity flag is set to one, program execution resumes at the address specified in the J PE instruction. If the flag is reset to zero, execution continues with the next sequential instruction.

### Forms

```asm
JPE        address
```

- Cycles: 3 (2 or 3 on 8085) | States: 10 (7 or lOon 8085) | Addressing: immediate | Flags: none

The address may be specified as a number, a label, or an expression. The assembler inverts the high and low address bytes when it assembles the instruction.

### Examples

```text
Examples of the variations of the jump instruction appear in the description of the J PO instruction.
```

---

<a id="jpo"></a>

## `JPO` — Jump If Parity Odd

Parity is odd if the byte in the accumulator has an odd number of one bits. The parity flag is set to zero to indicate this condition. The J PO instruction tests the setting of the parity flag. If the parity flag is reset to zero, program execution resumes at the address specified in the J PO instruction. If the flag is set to one, execution continues with the next sequential instruction.

### Forms

```asm
JPO        address
```

- Cycles: 3 (2 or 3 on 8085) | States: 10 (7 or 10 on 8085) | Addressing: immediate | Flags: none

The address may be specified as a number, a label, or an expression. The assembler inverts the high and low address bytes when it assembles the instruction.

### Examples

```text
This example shows three different but equivalent methods for jumping to one of two points in a program hased
upon whether or not the Sign bit of a number is set. Assume that the byte to be tested is the C register.
Label   Code   Operand
ONE:    MOV    A,C
ANI    80H
jZ     PLUS
jNZ    MINUS
TWO:    MOV    A,C
RLC
jNC    PLUS
JMP    MINUS
THREE:  MOV    A,C
ADI    0
JM     MINUS
PLUS:          ;SIGN BIT RESET
MINUS:         ;SIGN BIT SET
The ANO immediate instruction in block ONE zeroes all bits of the data byte except the Sign bit; which re
mains unchanged. If the Sign bit was zero, the Zero condition bit will be set, and the JZ instruction will cause
program control .to be transferred to the instruction at PLUS. Otherwise, the J Z instruction will merely update
the program counter by three, and the JNZ instruction will be executed, causing control to be transferred to
the instruction at MINUS. (The Zero bit is unaffected by all jump instructions.)
The RLC instruction in block TWO causes the Carry bit to be set equal to the Sign bit of the data byte. If the
Sign bit was reset, the J NC instruction causes a jump to PLUS. Otherwise the J MP instruction is executed,
unconditionally transferring control to MINUS. (Note that, in this instance, a JC instruction could be sub
stituted for the unconditional jump with identical results.)
The add immediate instruction in block THREE causes the condition bits to be set. If the sign bit was set, the
J M instruction causes program control to be transferred to MINUS. Otherwise, program control flows auto
matically into the PLUS routine.
```

---

<a id="jz"></a>

## `JZ` — Jump If Zero

The J Z instruction tests the setting of the zero flag. If the flag is set to one, program execution resumes at the address specified in the J Z instruction. If the flag is reset to zero, execution continues with the next sequential instruction.

### Forms

```asm
JZ          address
```

- Cycles: 3 (2 or 3 on 8085) | States: 10 (7 orl 0 on 8085) | Addressing: immediate | Flags: none

The address may be specified as a number, a label, or an expression. The assembler inverts the high and low address bytes when it assembles the instruction.

### Examples

```text
Examples of the variations of the jump instruction appear in the description of the J PO instruction.
```

---

<a id="lda"></a>

## `LDA` — Load Accumulator Direct

LDA loads the accumulator with a copy of the byte at the location specified in bytes two and three of the LDA instruction.

### Forms

```asm
LDA        address
```

- Cycles: 4 | States: 13 | Addressing: direct | Flags: none

The address may be stated as a number, a previously defined label, or an expression. The assembler inverts the high and low address bytes when it builds the instruction.

---

<a id="ldax"></a>

## `LDAX` — Load Accumulator  Indirect

L OAX loads the accumulator with a copy of the byte stored at the memory location addressed by register pair B or register pair O. Op co de   Operand LDA X The operand B specifies the Band C register pair; 0 specifies the 0 and E register pair. This instruction may specify only the B or 0 register pair. I            I ~O       rio 0            0 ~L  _fo = register pair B ~ = register pair 0 Cycles:     2 States:     7 Addressing: register indirect Flags:      none Example: Assume that register D contains 93H and register E contains BBH. The following instruction loads the accumulator with the contents of memory location 93BBH: LDAX D L.HLD                                               LOAD HAND  L DIRECT

---

<a id="lhld"></a>

## `LHLD` — Load HL Direct

LHLD loads the L register with a copy of the byte stored at the memory location specified in bytes two and three of the LHLD instruction. LHLD then loads the H register with a copy of the byte stored at the next higher memory location.

### Forms

```asm
LHLD        address
```

- Cycles: 5 | States: 16 | Addressing: direct | Flags: none

The address may be stated as a number, a label, or an expression. Certain instructions use the symbolic reference M to access the memory location currently specified by the HL registers. LHLD is one of the instructions provided for loading new addresses into the HL registers. The user may also load the current top of the stack into the HL registers (POP instruction). Both LH LD and POP replace the contents of the HL registers. You can also exchange the contents of HL with the D and E registers (XCHG instruction) or the top of the stack (XTHL instruction) if you need to save the current HL registers for subsequent use. SHLD stores HL in memory. lowaddr highaddr

### Examples

```text
Assume that locations 3000 and 3001 H contain the address 064EH stored in the format 4E06. In the following
sequence, the MOV instruction moves a copy of the byte stored at address 064E into the accumulator:
LHLD   3000H  ;SET UP ADDRESS
MOV    A,M    ;LOAD ACCUM FROM ADDRESS
3·34
```

---

<a id="lxi"></a>

## `LXI` — Load Register Pair Immediate

LXI is a three-byte instruction; its second and third bytes contain the source data to be loaded into a register pair. LXI loads a register pair by copying its second and third bytes into the specified destination register pair.

### Forms

```asm
LXI
```

- Cycles: 3 | States: -10 | Addressing: immediate | Flags: none

The first operand must specify the register pair to be loaded. LXI can load the Band C register pair, the D and E register pair, the HL register pair, or the Stack Pointer. The second operand specifies the two bytes of data to be loaded~ This data may be coded in the form of a num ber, an ASCII constant, the label of some previously defined value, or an expression. The data must not exceed two bytes. LXI is the only immediate instruction that accepts a 16-bit value. All other immediate instructions require 8-bit values. Notice that the assembler inverts the two bytes of data to create the format of an address stored in memory. LXI loads its third byte into the first register of the pair and its second byte into the second register of the pair. This has the effect of reinverting the data into the format required for an address stored in registers. Thus, the instruction LXI B,'AZ' loads A into register Band Z into register C. pE 0  0 IR       0 0  1 low-order data high-order data Examples: A common use for LXI is to establish a memory address for use in subsequent instructions. In the following

---

<a id="mov"></a>

## `MOV` — Move

sequence, the LXI instruction loads the address of STRNG into the HL registers. The MOV instruction then loads the data stored at that address into the accumulator. LXI  H,STRNG ;SET ADDRESS The following LXI instruction is used to initialize the stack pointer in a relocatable module. The LOCATE pro gram provides an address for the special reserved label STACK. LX I SP ,ST ACK MOV                                                              MOVE The MOV instruction moves one byte of data by copying the source field into the destination field. Source data remains unchanged. The instruction's operands specify whether the move is from register to register, from a register to memory, or from memory to a register. Move Register to Register

### Forms

```asm
MOV         regl,reg2
```

- Cycles: 1 | States: 5 (4 on 8085) | Addressing: register | Flags: none

The instruction copies the contents of reg2 into regl. Each operand must specify one of the registers A, B, C, D, E, H, or L. When the same register is specified for both operands (as in MOV A,A), the MOV functions as a NOP (no opera tion) since it has no other noticeable effect. This form of MOV requires one more machine state than NOP, and therefore has a slightly longer execution time than NOP. MOV M,M is not permitted. 0  1 I D D DI S  S 51 1 Move to Memory

```asm
MOV         M,r
```

- Cycles: 2 | States: 7 | Addressing: register indirect | Flags: none

This instruction copies the contents of the specified register into the memory location addressed by the HL register pair. M refers to the byte addressed by the HL register pair. The second operand must address one of the registers. MOV M,M is not permitted. I 5 5  51 o Move from Memory

```asm
MOV         r,M
```

- Cycles: 2 | States: 7 | Addressing: register indirect | Flags: none

This instruction copies the contents of the memory location addressed by the HL register pair into the specified "register. The first operand must name the destination register. The second operand must be M. M is a symbolic reference to the HL register pair. I D  D  D Examples:

```asm
LDACC:  MOV     A,M       ;LOAD ACCUM FROM MEMORY
MOV     E,A       ;COPY ACCUM INTO E REG
NULOP:  MOV     C,C       ;NULL OPERATION
```

---

<a id="mvi"></a>

## `MVI` — Move  Immediate

MVI is a two-byte instruction; its second byte contains the source data to be moved. MVI moves one byte of data by copying its second byte into the destination field. The instruction's operands specify whether the move is to a register or to memory. Move Immediate to Register

### Forms

```asm
MVI         reg,data
```

- Cycles: 2 | States: 7 | Addressing: immediate | Flags: none

The first operand must name one of the registers A through E, H or L as a destination for the move. The second operand specifies the actual data to be moved. This data may be in the form of a number, an ASCII constant, the label of some previously defined value, or an expression. The data must not exceed one byte. The assembler's relocation feature treats all external and relocatable symbols as 16-bit addresses. When one of these symbols appears in the operand expression of an immediate instruction, it must be preceded by either the HIGH or LOW operator to specify which byte of the address is to be used in the evaluation of the expression. When neither operator is present, the assembler assumes the LOW operator and issues an error message. 0  D  D  D 1°       data       °1 Chapter 3. Instructhm Set MOlle Immediate to Memory

```asm
MVI         M,data
```

- Cycles: 3 | States: 10 | Addressing: immediate/register indirect | Flags: none

This instruction copies the data stored in its second byte into the memory location addressed by HL. M is a symbolic reference to the HL register pair. o  0       o      o data Examples: The following examples show a number of methods for defining immediate data in the MVI instruction. All of the examples generate the bit pattern for the ASCII character A. MVI      M,Ol 000001 B MVI      M,IA' MVI      M,41 H MVI      M,101Q MVI      M,65 MVI      M,5+30*2

---

<a id="nop"></a>

## `NOP` — No Operation

NOP performs no operation and affects none of the condition flags. NOP is useful as filler in a timing loop.

### Forms

```asm
NOP
```

---

<a id="ora"></a>

## `ORA` — Inclusive Or With Accumulator

ORA                                       INCLUSIVE OR WITH ACCUMULATOR ORA performs an inclusive OR logical operation using the contents of the specified byte and the accumulator. The result is placed in the accumulator. Summary of Logical Operations AND produces a one bit in the result only when the corresponding bits in the test data and the mask data are one. OR produces a one bit in the result when the corresponding bits in either the test data or the mask data are ones. Exclusive OR produces a one bit only when the corresponding bits in the test data and the mask data are different; i.e., a one bit in either the test data or the mask data - but not both - produces a one bit in the result. AND       OR        EXCLUSIVE OR 1010 1010 1010 1010     1010 1010 0000 1111 0000 1111     0000 1111 0000 1010 1010 1111     1.010 0101 OR Register with Accumulator

### Forms

```asm
ORA         reg
```

- Cycles: 1 | States: 4 | Addressing: register | Flags: Z,S,P,CY,AC

The operand must specify one of the registers A through E, H or L. This instruction ORs the contents of the specified register and the accumulator and stores the result in the accumulator. The carry and auxiliary carry flags are reset to zero. I o       o  s s  s OR Memory with Accumulator

```asm
ORA         M
```

- Cycles: 2 | States: 7 | Addressing: register indirect | Flags: Z,S,P,CY,AC

The contents of the memory location specified by the HL registers are inciusive-ORed with the contents of the accumulator. The result is stored in the accumulator. The carry and auxiliary carry flags are reset to zero. o       o 3·39

### Examples

```text
Since any bit inclusive-ORed with a one produces a one and any bit ORed with a zero remains unchanged, ORA
is frequently used to set ON particular bits or groups of bits. The following example ensures that bit 3 of the
accumulator is set ON, but the remaining bits are not disturbed. This is frequently done when individual bits
are used as status flags in a program. Assume that register D contains the value 08H:
o
Accumulator 1 0 0 0 0 1
o
Register D  0 0 0 000
o  o 0  o
```

---

<a id="ori"></a>

## `ORI` — Inclusive Or Immediate

ORI                                               INCLUSIVE OR IMMEDIATE ORI performs an inclusive OR logical operation using the contents of the second byte of the instruction and the contents of the accumulator. The result is placed in the accumulator. ORI also resets the carry and auxiliary carry flags to zero.

### Forms

```asm
ORI         data
```

- Cycles: 2 | States: 7 | Flags: Z,S,P,SY,AC

The operand must specify the data to be used in the inclusive OR operation. This data may be in the form of a number, an ASCII constant, the label of some previously defined value, or an expression. The data may not exceed one byte. The assembler's relocation feature treats all external and relocatable symbols as 16-bit addresses. When one of these symbols appears in the operand expression of an immediate instruction, it must be preceded by either the HIGH or LOW operator to specify which byte of the address is to be used in the evaluation of the expression. When neither operator is present, the assembler assume the LOW operator and issues an error message. o       o data Ad dressi ng: immediate Summary of Logical Operations AND produces a one bit in the result only when the corresponding bits in both the test data and the mask data are ones. OR produces a one bit in the result when the corresponding bits in either the test data or the mask data are ones. Exclusive OR produces a one bit only when the corresponding bits in the test data and the mask data are different; i.e., a one bit in either the test data or the mask data - but not both - produces a one bit in the result. AND         OR        EXCLUSIVE OR 1010 1010  1010 1010     1010 1010 0000 1111  0000 1111     0000 1111 0000 1010  1010 1111     1010 0101

### Examples

```text
See the description of the ORA instruction for an example of the use of the inclusive OR. The following
examples show a number of methods for defining immediate data in the ORI instruction. All of the examples
generate the bit pattern for the ASCII character A.
ORI     01000001 B
ORI     'A'
ORI     41H
ORI     101Q
ORI     65
ORI     5+30*2
```

---

<a id="out"></a>

## `OUT` — Output To Port

The OUT instruction places the contents of the accumulator on the eight-bit data bus and the number of the selected port on the sixteen-bit address bus. Since the number of ports ranges from 0 through 255, the port number is duplicated on the address bus. It is the responsibility of external logic to decode the port number and to accept the output data. NOTE Because a discussion of input/output structures is beyond the scope of this manual, th is description is restricted to the exact function of the OUT instruction. Input/output structures are described in the 8080 or 8085 Microcomputer Systems User's Manual. '

### Forms

```asm
OUT         exp
```

- Cycles: 3 | States: 10 | Addressing: direct | Flags: none

The operand must specify the number of the desired output port. This may be in the form of a number or an expression in the range OOH through OFFH. g o    0 exp

---

<a id="pchl"></a>

## `PCHL` — Move H&L To Program Counter

PCHL loads the contents of the HL registers into the program counter register. Because the processor fetches the next instruction from the updated program counter address, PCHL has the effect of a jump instruc tion.

### Forms

```asm
PCHL
PCHL moves the contents of the H register to the high-order eight bits of the program counter and the contents
```

- Cycles: 1 | States: 5 (6 on 8085) | Addressing: register | Flags: none

The user program must ensure that the HL registers contain the address of an executable instruction when the PCHL instruction is executed. o    o  0

### Examples

```text
One technique for passing data to a subroutine is to place the data immediately after the subroutine call. The
return address pushed onto the stack by the CALL instruction actually addresses the data rather than the next
instruction after the CALL. For this example, assume that two bytes of data follow the subroutine call. The
following coding sequence performs a return to the next instruction after the call:
GOBACK: POP  H   ;GET DATA ADDRESS
INR  L   ;ADD 2 TO FORM
INR  L   ;RETURN ADDRESS
PCHL     ;RETURN
POP                                                                POP
```

---

<a id="pop"></a>

## `POP` — E

The POP instruction removes two bytes of data from the stack and copies them to a register pair or copies the Program Status Word into the accumulator and the condition flags. POP Register Pair POP copies the contents of the memory location addressed by the stack pointer into the low-order register of the register pair. POP then increments the stack pointer by one and copies the contents of the resulting address into the high-order register of the pair. POP then increments the stack pointer again so that it addresses the next older item on the stack.

### Forms

```asm
POP
```

- Cycles: 3 | States: 10 | Addressing: register indirect | Flags: Z,S,P,CY,AC

The operand may specify the B&C, D&E, or the H&L register pairs. POP PSW is explained separately. E I E1   I R P    0  0 1 POP PSW POP PSW uses the contents of the memory location specified by the stack pointer to restore the condition flags. POP PSW increments the stack pointer by one and restores the contents of that address to the accumulator. POP then increments the stack pointer again so that it addresses the next older item on the stack. 000

### Examples

```text
Assume that a subroutine is called because of an external interrupt. In general, such subroutines should save and
restore any registers it uses so that main program can continue normally when it regains control. The following
sequence of PUSH and POP instructions save and restore the Program Status Word and all the registers:
343
PUSH    PSW
PUSH    B
PUSH    D
PUSH    H
subroutine coding
POP     H
POP     D
POP     B
POP     PSW
RET
Notice that the sequence of the POP instructions is the opposite of the PUSH instruction sequence.
PUSH                                                              PUSH
```

---

<a id="push"></a>

## `PUSH` — o

The PUSH instruction copies two bytes of data to the stack. This data may be the contents of a register pair or the Program Status Word, as explained below: PUSH Register Pair PUSH decrements the stack pointer register by one and copies the contents of the high-order register of the register pair to the resulting address. PUSH then decrements the pointer again and copies the low-order register to the resulting address. The source registers remain unchanged.

### Forms

```asm
PUSH
```

- Cycles: 3 | States: 11 (130n8085) | Addressing: register indirect | Flags: none

The operand may specify the B&C, D& E, or H& L register pairs. PUSH PSW is explained separately. I           o 1 R  P  0

### Examples

```text
Assume that register B contains 2AH, the C register contains 4CH, and the stack pointer is set at 9AAF. The
instruction PUSH B stores the B register at memory address 9AAEH and the C register at 9AADH. The stack
pointer is set to 9AADH:
344
Stack               Stack
Before PUSH Address After PUSH
..
SP before      xx        9AAF      xx
xx        9AAE      2A
...
xx        9AAD      4C           SP after
xx        9AAC      xx
PUSH PSW
PUSH PSW copies the Program Status Word onto the stack. The Program Status Word comprises the contents
of the accumulator and the current settings of the condition flags. Because there are only five condition flags,
PUSH PSW formats the flags into an eight-bit byte as follows:
o
7  6   5  4  3   2
z  o     o        Icy I
S         AC     P
On the 8080, bits 3 and 5 are always zero; bit one is always set to one. These filler bits are undefined on the
8085.
PUSH PSW decrements the stack pointer by one and copies the contents of the accumulator to the resulting
address. PUSH PSW again decrements the pointer and copies the formatted condition flag byte to the resulting
address. The contents of the accumulator and the condition flags remain unchanged.
o    o
Cycles:     3
States:     11 (12 on 8085)
Addressing: register indirect
Flags:      none
Example:
When a program calls subroutines, it is frequently necessary to preserve the current program status so the calling
program can continue normally when it regains control. Typically, the subroutine performs a PUSH PSW prior to
execution of any instruction that might alter the contents of the accumulator or the condition flag settings.
The subroutine then restores the pre-call system status by executing a POP PSW instruction just before returning
control to the calling program.
```

---

<a id="ral"></a>

## `RAL` — Rotate Left Through Carry

RAL rotates the contents of the accumulator and the carry flag one bit position to the left. The carry flag, which is treated as though it were part of the accumulator, transfers to the low-order bit of the accumulator. The high order bit of the accumulator transfers into the carry flag.

### Forms

```asm
RAL
```

- States: 4 | Flags: CYonly

### Examples

```text
Assume that the accumulator contains the value OAAH and the carry flag is zero. The following diagrams illus
trate the effect of the RAL instruction:
Before:                 Carry
o
~--------------~
Accumulator
o     o    o    o
After:                     Carry
CD
Accumulator
0    0    0    0  01
1
```

---

<a id="rar"></a>

## `RAR` — Rotate Right Through Carry

RAR rotates the contents of the accumulator and the carry flag one bit position to the right. The carry flag, which is treated as though it were part of the accumulator, transfers to the high-order Qjt of the accumulator. The low-order bit of the accumulator transfers into the carry flag.

### Forms

```asm
RAR
```

- States: 4 | Flags: CYonly

### Examples

```text
Assume that the accumulator contains the value OAAH and the carry flag is zero. The following diagrams illus
trate the effect of the RAR instruction:
Before:                  Carry
o
Accumulator
o    o    o     o
After:                     Carry
Accumulator
o     o    o
[ 0
```

---

<a id="rc"></a>

## `RC` — Return If Carry

The RC instruction tests the carry flag. If the flag is set to one to indicate a carry, the instruction pops two bytes off the stack and places them in the program counter. Program execution resumes at the new address in the program counter. If the flag is zero, program execution simply continues with the next sequential instruction.

### Forms

```asm
RC
```

- Cycles: 1 or 3 | States: 5 or 11 (6 or 12 on 8085) | Addressing: register indirect | Flags: none

### Examples

```text
For the sake of brevity, an example is given for the RET instruction but not for each of its closely related
variants.
347
```

---

<a id="ret"></a>

## `RET` — Return From -Subroutine

The RET instruction pops two bytes of data off the stack and places them in the program counter register. Program execution resumes at the new address in the program counter. Typically, RET instructions are used in conjunction with CALL instructions. (The same is true of the variants of these instructions.) In this case, it is assumed that the data the RET instruction pops off the stack is a return address placed there by a previous CALL. This has the effect of returning control to the next instruction after the CALL. The user must be certain that the RET instruction finds the address of executable code on the stack. If the instruction finds the address of data, the processor attempts to execute the data as though it were code.

### Forms

```asm
RET
```

- Cycles: 3 | States: 10 | Addressing: register indirect | Flags: none

### Examples

```text
As mentioned previously, subroutines can be nested. That is, a subroutine can call a subroutine that calls
another subroutine. The only practical limit on the number of nested calls is the amount of memory available
for stacking return addresses. A nested subroutine can even call the subroutine that called it, as shown in the
following example. (Notice that the program must contain logic that eventually returns control to the main
program. Otherwise, the two subroutines will call each other indefinitely.)
1                      1·' --               1
MAIN PROGRAM
SUBA:               SUBB:
~                     ~----CALLSUBA
T
~ ~  ~ ~ ~
CALL SUBA              CNZTSUBB             -
T                           ~ ~
RET
.",.
RET .....
```

---

<a id="rim"></a>

## `RIM` — Read Interrupt Mask / Serial Input (8085 only)

The RIM instruction loads eight bits of data into the accumulator. The resulting bit pattern indicates the current setting of the interrupt mask, the setting of the interrupt flag, pending interrupts, and one bit of serial input data, if any. 348

### Forms

```asm
RIM
```

- States: 4 | Flags: none

The RIM instruction loads the accumulator with the following information: 7  6  5   4  3  2   1  0 SID 17 16 15  ILE 7.5 6.5 5.5 "-V~v~ L Interrupt Masks: 1 = masked Interrupt Enable Flag: = enabled I.....---Pending Interrupts: = pending '-----Serial Input Data Bit, if any The mask and pending flags refer only to the RST5.5, RST6.5, and RST7.5 hdrdware interrupts. The IE flag refers to the entire interrupt system. Thus, the IE flag is identical in function and level to the INTE pin on the 8080. A 1 bit in this flag indicates that the entire interrupt system is enabled. E 0    0  0  0 0 01

---

<a id="rlc"></a>

## `RLC` — Rotate Accumulator Left

RLC sets the carry flag equal to the high-order bit of the accumulator, thus overwriting its previous setting. RLC then rotates the contents of the accumulator one bit position to the left with the high-order bit transferring to the low-order position of the accumulator.

### Forms

#### the low-order position of the accumulator.

```asm
RLC
```

- States: 4 | Flags: CYonly

349

### Examples

```text
Assume that the accumulator contains the value OAAH and the carry flag is zero. The following diagrams illus
trate the effect of the RLC instruction.
Before:                  Carry
GJ
Accumulator
0    0    0     0
After:                     Carry
Accumulator
o    o
```

---

<a id="rm"></a>

## `RM` — Return If Minus

The RM instruction tests the sign flag. If the flag is set to one to indicate negative data in the accumulator, the instruction pops two bytes off the stack and places them in the program counter. Program execution resumes at the new address in the program counter. If the flag is set to zero, program execution simply continues with the next sequential instruction.

### Forms

```asm
RM
```

- Cycles: or 3 | States: 5 or 11 (6 or 12 on 8085) | Addressing: register indirect | Flags: none

### Examples

```text
For the sake of brevity, an example is given for the RET instruction but not for each of its closely related
variants.
```

---

<a id="rnc"></a>

## `RNC` — Return If No Carry

The RNC instruction tests the carry flag. If the flag is set to zero to indicate that there has been no carry, the instruction pops two bytes off the ~tack and places them in the program counter. Program execution resumes at the new address in the program counter. If the flag is one, program execution simply continues with the next sequential instruction.

### Forms

```asm
RNC
```

- Cycles: or 3 | States: 5 or 11 (6 or 12 on 8085) | Addressing: register indirect | Flags: none

### Examples

```text
For the sake of brevity, an example is given for the RET instruction but not for each of its closely related
variants.
```

---

<a id="rnz"></a>

## `RNZ` — Return If Not Zero

The RNZ instruction tests the zero flag. If the flag is set to zero to indicate that the contents of the accumulator are other than zero, the instruction pops two bytes off the stack and places them in the program counter. Pro gram execution resumes at the new address in the program counter. If the flag is set to one, program execution simply continues with the next sequential instruction.

### Forms

```asm
RNZ
```

- Cycles: or 3 | States: 5 or 11 (6 or 12 on 8085) | Addressing: register indirect | Flags: none

### Examples

```text
For the sake of brevity, an example is given for the RET instruction but not for each of its closely related
variants.
```

---

<a id="rp"></a>

## `RP` — Return If Positive

The RP instruction tests the sign flag. If the flag is reset to zero to indicate positive data in the accumulator, the instruction pops two bytes off the stack and places them in the program counter. Program execution resumes at the new address in the program counter. If the flag is set to one, program execution simply continues with the next sequential instruction. Op co de   Operand RP Operands are not permitted with the RP instruction. 0  0  0 11                 01 Cycles:      or 3 States:     5 or 11 (6 or 12 on 8085) Addressing: register indirect Flags:      none Example: For the sake of brevity, an example is given for the RET instruction but not for each of its closely related variants.

---

<a id="rpe"></a>

## `RPE` — Return If Parity Even

Parity is even if the byte in the accumulator has an even number of one bits. The parity flag is set to one to indicate this condition. The RPE and RPO instructions are useful for testing the parity of input data. However, the I N instruction does not set any of the condition flags. The flags can be set without altering the data by adding OOH to the contents of the accumulator. The RPE instruction tests the parity flag. If the flag is set to one to indicate even parity, the instruction pops two bytes off the stack and places them in the program counter. Program execution resumes at the new address in the program counter. If the flag is zero, program execution simply continues with the next sequential instruc tion.

### Forms

```asm
RPE
```

- Cycles: or 3 | States: 5 or 11 (6 or 12 on 8085) | Addressing: register indirect | Flags: none

### Examples

```text
For the sake of brevity, an example is given for the RET instruction but not for each of its closely related
variants.
```

---

<a id="rpo"></a>

## `RPO` — Return If Parity Odd

Parity is odd if the byte in the accumulator has an odd number of one bits. The parity flag is reset to zero to indicate this condition. The RPO and RPE instructions are useful for testing the parity of input data. However, the IN instruction does not set any of the condition flags. The flags can be set without altering the data by adding OOH to the contents of the accumulator. The RPO instruction tests the parity flag. If the flag is reset to zero to indicate odd parity, the instruction pops two bytes off the stack and places them in the program counter. Program execution resumes at the new address in the program counter. If the flag is set to one, program execution simply continues with the next sequential instruction. Opeode      Operand RPO Operands are not permitted with the RPO instruction. 11       0 0  0  0 01 Cycles:      or 3 States:     5 or 11 (6 or 12 on 8085) Addressing: register indirect Flags:      none Example: For the sake of brevity, an example is given for the RET instruction but not for each of its closely related variants.

---

<a id="rrc"></a>

## `RRC` — Rotate Accumulator Right

RRC sets the carry flag equal to the low-order bit of the accumulator, thus overwriting its previous setting. RRC then rotates the contents of the accumulator one bit position to the right with the low-order bit transferring to the high order position of the accumulator. Ope ode     Operand RRC Operands are not permitted with the RRC instruction. 10 0  0  0 Cycles: States:     4 Flags:     CYonly Example: Assume that the accumulator contains the value OAAH and the carry flag is zero. The following diagrams illus trate the effect of the RRC instruction: Before:                  Carry G Accumulator 0    0    0 After:                     Carry Accumulator o     o RST                                                            RESTART

---

<a id="rst"></a>

## `RST` — Program

RST is a special purpose CALL instruction designed primarily for use with interrupts. RST pushes the contents of the program counter onto the stack to provide a return address and then jumps to one of eight predetermined addresses. A three-bit code carried in the opcode of the RST instruction specifies the jump address. The restart instruction is unique because it seldom appears as source code in an applications program: More often, the peripheral devices seeking interrupt service pass this one-byte instruction to the processor. When a device requests interrupt service and interrupts are enabled, the processor acknowledges the request and prepares its data lines to accept anyone-byte instruction from the device. RST is generally the instruction of choice because its special purpose CALL establishes a return to the main program. The processor moves the three-bit address code from the RST instruction into bits 3, 4, and 5 of the program counter. In effect, this multiplies the code by eight. Program execution resumes at the new address where eight bytes are available for code to service the interrupt. If eight bytes are too few, the program can either jump to or call a subroutine. 8085 NOTE The 8085 processor includes four hardware inputs that generate internal RST instructions. Rather than send a RST instruction, the interrupting device need only apply a signal to the RST5.5, RST6.5, RST7.5, or TRAP input pin. The processor then generates an internal RST instruction. The execution depends on the input: INPUT           RESTART NAME             ADDRESS TRAP             24H RST5.5           2CH RST6.5           34H RST7.5           3CH Notice that these addresses are within the same portion of memory used by the RST instruction, and therefore allow only four bytes - enough for a call or jump and a return - for the interrupt service routine. If included in the program code, the RST instruction has the following format:

### Forms

```asm
RST         code
```

- Cycles: 3 | States: 11 (12 on 8085) | Addressing: register indirect | Flags: none

The address code must be a number or expression within the range OOOB through 111 B. I I 11 C C C 1 11 '---y--- - -----/- Program ~ Counter 15 14 13 12 11 10 9 8 7 6 5 4 3 2 0 After RST 10 C C C 0 0 01

---

<a id="rz"></a>

## `RZ` — Return If Zero

The RZ instruction tests the zero flag. If the flag is set to one to indicate that the contents of the accumulator are zero, the instruction pops two bytes of data off the stack and places them in the program counter. Program execution resumes at the new address in the program counter. If the flag is zero, program execution simply continues with the next sequential instruction.

### Forms

```asm
RZ
```

- Cycles: or 3 | States: 5 or 11 (6 or 12 on 8085) | Addressing: register indirect | Flags: none

### Examples

```text
For the sake of brevity, an example is given for the RET instruction but oot for each of its closely related
variants.
```

---

<a id="sbb"></a>

## `SBB` — Subtract With Borrow

SBB                                               SUBTRACT WITH BORROW SBB subtracts one byte of data and the setting of the carry flag from the contents of the accumulator. The result is stored in the accumulator. SBB then updates the setting of the carry flag to indicate the outcome of the operation. SBB's use of the carry flag enables the program to subtract rrulti-byte strings. SBB incorporates the carry flag by adding it to the byte to be subtracted from the accumulator. It then subtracts the result "from the accumulator by using two's complement addition. These preliminary operations occur in the processor's internal work registel so that the source data remains unchanged. Subtract Register from Accumulator with Borrow

### Forms

```asm
SBB         reg
```

- Cycles: 1 | States: 4 | Addressing: register | Flags: Z,S,P ,CY ,AC

The operand must specify one of the registers A through E, H or L. This instruction subtracts the contents of the specified register and the carry flag from the accumulator and stores the result in the accumulator. sl S S Subtract Memory from Accumulator with Borrow

```asm
SBB         M
```

- Cycles: 2 | States: 7 | Addressing: register indirect | Flags: Z,S,P,CY,AC

This instruction subtracts the carry flag and the contents of the memory location addressed by the HL register pair from the accumulator and stores the result in the accumulator. [0    0

### Examples

```text
Assume that register B contains 2, the accumulator contains 4, and the carry flag is set to 1. The instruction
SBB B operates as follows:
2H + carry = 3H
2's complement of 3H = 11111101
Accumulator = 00000100
11111101
00000001 = 1 H
Notice that this two's complement addition produces a carry. When SBB complements the carry bit generated
by the addition, the carry flag is reset OFF. The flag settings resulting from the SBB B instruction are as
follows:
Carry        0
Sign         0
Zero         0
Parity       0
Aux. Carry
```

---

<a id="sbi"></a>

## `SBI` — Subtract Immediate With Borrow

SBI                                       SUBTRACT IMMEDIATE WITH BORROW SBI subtracts the contents of the second instruction byte and the setting of the carry flag from the contents of the accumulator. The result is stored in the accumulator. SBI's use of the carry flag enables the program to subtract multi-byte strings. SBI incorporates the carry flag by adding it to the byte to be subtracted from the accumulator. It then subtracts the result from the accumulator by using two's complement addition. These preliminary operations occur in the processor's internal work registers so that the immediate source data remains unchanged. The assembler's relocation feature treats all external and relocatable symbols as 16-bit addresses. When one of these symbols appears in the operand expression of an immediate instruction, it must be preceded by either the HIGH or LOW operator to specify which byte of the address is to be used in the evaluation of the expression. When neither operator is present, the assembler assumes the LOW operator and issues an error message.

### Forms

```asm
SBI         data
```

- Cycles: 2 | States: 7 | Addressing: immediate | Flags: Z,S,P,CY,AC

The operand must specify the data to be subtracted. This data may be in the form of a number, an ASCII constant, the label of some perviously defined value, or an expression. The data may not exceed one byte. o

### Examples

```text
This sequence of instructions replaces a 20·byte array at symbolic location AXLOTL with a logical array consisting
of zeros and ones, as follows:
•  If an element ofAXLOTL is 5 or greater in absolute value, it is replaced with 1.
•  If an element ofAXLOTL is less than 5 in absolute value, it is replaced with O.
Note that the program flow is governed by how the carry flag is set.
MVI B,20    ; initialize counter
XRA A       ; clear accumulator and carry
LXI H,AXLOTL ; (H,L) point to array AXLOTL
LOAD: MOV A,M     ; load acc. with byte pointed to by (H,L)
SBI 5       ; subtract 5, set carry if acc. less than 5
JC SMALL    ; jump to SMALL if acc. was less than 5
MVI M,l     ; store 1 where array element was
JMP TEST    ; jump down to test count
SMALL: MVI M,O     ; store 0 where array element was
TEST:  XRA A       ; clear accumulator and carry
OCR B       ; decrement count
CMP B       ; compare B to 0
JZ  DONE    ; if accum. is zero, all done
INX H       ; bump (H,L) to point to next array element
JMP LOAD    ; go back and get another array element
DONE:             ; remainder of program
SHLD                                                STORE HAND L DIRECT
SHLD stores a copy of the L register in the memory location specified in bytes two and three of the SHLD
instruction. SHLD then stores a copy of the H register in the next higher memory location.
```

---

<a id="shld"></a>

## `SHLD` — Store HL Direct

SHLD is one of the instructions provided for saving the contents of the HL registers. Alternately, the H and L data can be placed in the D and E registers (XCHG instruction) or placed on the stack (PUSH and XTHL instructions). 0 0  1  0 0  0  1 0 low addr high addr Cycles:     5 States:     16 Addressing: direct Flags:      none Example: Assume that the HL registers contain OAEH and 29H, respectively. The following is an illustration of the effect of the SH LD 10AH instruction: MEMORY ADDRESS 109  lOA  lOB  10C Memory Before SHLD     00   00   00   00

---

<a id="sim"></a>

## `SIM` — Set Interrupt Mask / Serial Output (8085 only)

SIM is a mUlti-purpose instruction that uses the current contents of the accumulator to perform the following functions: Set the interrupt mask for the 8085's RST5.5, RST6.5, and RST7.5 hardware interrupts; reset RST7.5's edge sensitive input; and output bit 7 of the accumulator to the Serial Output Data latch.

### Forms

```asm
SIM
RESET RST7.S: If 1, RST7.S flip flop is reset OFF
SOD output where it can be accessed by a peripheral device. If bit 6 is reset to 0, bit 7 is ignored.
```

- Cycles: 1 | States: 4 | Flags: none

The RST7.S flip flop remains set \Jntil reset by 1) issuing a RESET to the 808S, 2) recognizing the interrupt, or 3) setting accumulator bit 4 and executing a SIM instruction. The Reset RST7.S feature of the SIM instruction allows the program to override the interrupt. The RST7.S input flip flop is not affected by the setting of the interrupt mask or the 01 instruction and there fore can be set at any time. However, the interrupt cannot be serviced when RST7.S is masked or a DI instruction is in effect. 0 0  0       0  0    01 1 Example 1: Assume that the accumulator contains the bit pattern 00011100. The SIM instruction resets the RST7.S flip flop and sets the RST7.S interrupt mask. If an RST7.S interrupt is pending when this SI M instruction is executed, it is overridden without being serviced. Also, any subsequent RST7.S interrupt is masked and cannot be serviced until the interrupt mask is reset. Example 2: Assume that the accumulator contains the bit pattern 11001111. The SI M instruction masks out the RST5.5, RST6.5, and RST7.5 level interrupts and latches a 1 bit into the SOD input. By contrast, the bit pattern 10000111 has no effect since the enable bits 3 and 6 are not set to ones.

---

<a id="sphl"></a>

## `SPHL` — Move H& L To Sp

SPH L loads the contents of the HL registers into the SP (Stack Pointer) register.

### Forms

```asm
SPHL
SP is a special purpose 16-bit register used to address the stack; the stack must be in random access memory
```

- Cycles: 1 | States: 5 (6 on 8085) | Addressing: register | Flags: none

The hardware decrements the stack pointer as items are added to the stack and increments the pointer as items are removed. The stack pointer must be initialized before any instruction attempts to access the stack. Typically, stack initialization occurs very early in the program. Once established, the stack pointer should be altered with caution. Arbitrary use of SPHL can cause the loss of stack data. ~1                 ~11 __________0_ _0_ _

### Examples

```text
Assume that the HL registers contain 50H and OFFH, respectively. SPHL loads the stack pointer with the
value 50FFH.
```

---

<a id="sta"></a>

## `STA` — Store Accumulator Direct

ST A stores a copy of the current accumulator contents into the memory location specified in bytes two and three of the ST A instruction.

### Forms

```asm
STA        address
```

- Cycles: 4 | States: 13 | Addressing: direct | Flags: none

The address may be stated as a number, a previously defined label, or an expression. The assembler inverts the high and low address bytes when it builds the instruction.

### Examples

```text
The following instruction stores a copy of the contents of the accumulator at memory location 5B3H:
STA    5B3H
When assembled, the previous instruction has the hexadecimal value 32 B3 05. Notice that the assembler inverts
the high and low order address bytes for proper storage in memory.
```

---

<a id="stax"></a>

## `STAX` — Store Accumulator Indirect

The STAX instruction stores a copy of the contents of the accumulator into the memory location addressed by register pair B or register pair D.

### Forms

```asm
STAX
```

- Cycles: 2 | States: 7 | Addressing: register indirect | Flags: none

The operand B specifies the Band C register pair; D specifies the D and E register pair. This instruction may specify only the B or D register pair. 10001100           01 '-v-/ l{o = register pair B 1 = register pair D

### Examples

```text
If register B contains 3FH and register C contains 16H, the following instruction stores a copy of the contents
of the accumulator at memory location 3F16H:
STAX B
3·62
```

---

<a id="stc"></a>

## `STC` — Set Carry

STC                                                          SET CARRY STC sets the carry flag to one. No other flags are affected.

### Forms

```asm
STC
```

- States: 4 | Flags: CY

When used in combination with the rotate accumulator through the carry flag instructions, STC allows the pro gram to modify individual bits.

---

<a id="sub"></a>

## `SUB` — Subtract

SUB                                                           SUBTRACT The SUB instruction subtracts one byte of data from the contents of the accumulator. The result is stored in the accumulator. SUB uses two's complement representation of data as explained in Chapter 2. Notice that the SUB instruction excludes the carry flag (actually a 'borrow' flag for the purposes of subtraction) but sets the flag to indicate the outcome of the operation. Subtract Register from Accumulator Op co de    Operand SUB         reg The operands must specify one of the registers A through E, H or L. The instruction subtracts the contents of the specified register from the contents of the accumulator using two's complement data representation. The result is stored in the accumulator. o S S  S\ Cycles: States:     4 Addressing: register Flags:     Z,S,P,CY,AC Subtract Memory from Accumulator

### Forms

```asm
SUB         M
```

- Cycles: 2 | States: 7 | Addressing: register indirect | Flags: Z,S,P,CY,AC

This instruction subtracts the contents of the memory location addressed by the HL register pair from the contents of the accumulator and stores the result in the accumulator. M is a symbolic reference to the HL register pair. o      o 0

### Examples

```text
Assume that the accumulator contains 3EH. The instruction SUB A subtracts the contents of the accumulator
from the accumulator and produces a result of zero as follows:
3EH  001111"10
+(-3EH) 11000001 one's complement
1  add one to produce two's complement
carry out = 1 00000000 result = 0
The condition flags are set as follows:
Carry       o
Sign        o
Zero
Parity
Aux. Carry
Notice that the SUB instruction complements the carry generated by the two's complement addition to form a
'borrow' flag. The auxiliary carry flag is set because the particular value used in this example causes a carry out
of bit 3.
```

---

<a id="sui"></a>

## `SUI` — Subtract Immediate

SUI                                                 SUBTRACT IMMEDIATE SU I subtracts the contents of the second instruction byte from the contents of the accumulator and stores the result in the accumulator. Notice that the SUI instruction disregards the carry ('borrow') flag during the sub traction but sets the flag to indicate the outcome of the operation.

### Forms

```asm
SUI        data
```

- Cycles: 2 | States: '] | Addressing: immediate | Flags: Z,S,P,CY,AC

The operand must specify the data to be subtracted. This data may be in the form of a number, an ASCII constant, the label of some previously defined value, or an expression. The data must not exceed one byte. The assembler's relocation feature treats all external and relocatable symbols as 16-bit addresses. When one of these symbols appears in the operand expression of an immediate instruction, it must be preceded by either the HIGH or LOW operator to specify which byte of the address is to be used in the evaluation of the expression. When neither operator is present, the assembler assumes the LOW operator and issues an error message. cc=_1_ _0_ _ ___0_ _ ______0 ~

### Examples

```text
Assume that the accumulator contains the value 9 when the instruction SUI 1 is executed:
Accumulator       00001001 = 9H
Immediate data (2's comp) 11111111 = -1 H
00001000 = 8H
Notice that this two's complement addition results in a carry. The SUI instruction complements the carry
generated by the addition to form a 'borrow' flag. The flag settings resulting from this operation are as follows:
Carry        a
Sign         a
Zero         a
Parity       a
Aux. Carry
```

---

<a id="xchg"></a>

## `XCHG` — Exchange HL With D And E

XCHG                                       EXCHANGE HAND L WITH D AND E XCHG exchanges the contents of the HL registers with the contents of the 0 and E registers.

### Forms

```asm
XCHG
XCHG both saves the current HL and loads a new address into the HL registers. Since XCHG is a
```

- Cycles: 1 | States: 4 | Addressing: register | Flags: none

### Examples

```text
Assume that the HL registers contain 1234H, and the D and E registers contain OABCDH. Following
execution of the XCHG instruction, HL contain OABCDH, and D and E contain 1234H.
```

---

<a id="xra"></a>

## `XRA` — Exclusive Or With Accumulator

XRA                                       EXCLUSIVE OR WITH ACCUMULATOR XRA performs an excl usive OR logical operation using the contents of the specified byte and the accumulator. The result is placed in the accumulator. Summary of Logical Operations AND produces a one bit in the result only when the corresponding bits in the test data and the mask data are ones. OR produces a one bit in the result when the corresponding bits in either the test data or the mask data are ones. Exclusive OR produces a one bit only when the corresponding bits in the test data and the mask data are different; i.e., a one bit in either the test data or the mask data - but not both - produces a one bit in the result. AND       OR        EXCLUSIVE OR 10101010  1010 1010     1010 1010 n 0000 1111 0000 11       0000 1111 0000 1010 10101111      10100101 XRA Register with Accumulator

### Forms

```asm
XRA         reg
```

- States: 4 | Addressing: register | Flags: Z,S,P,CY,AC

The operand must specify one of the registers A through E, H or L. This instruction performs an exclusive OR using the contents of the specified register and the accumulator and stores the result in the accumulator. The carry and auxil iary carry flags are reset to zero. o    o    S  S  S X RA Memory with Accumulator

```asm
XRA         M
```

- Cycles: 2 | States: "1 | Addressing: register indirect | Flags: Z ,S ,P ,CY ,AC

The contents of the memory location specified by the HL registers is exclusive-ORed with the contents of the accumulator. The result is stored in the accumulator. The carry and auxiliary carry flags are reset to zero. ~_O                o __O   _ Examples: Since any bit exclusive-ORed with itself produces zero, XRA is frequently used to zero the accumulator. The following instructions zero the accumulator and the Band C registers. XRA   A MOV   B,A MOV   C,A Any bit exclusive-ORed with a one bit is complemented. Thus, if the accumulator contains all ones (OFFH), the instruction XRA B produces the one's complement of the B register in the accumulator.

---

<a id="xri"></a>

## `XRI` — Exclusive Or Immediate With Accumulator

XRI                              EXCLUSIVE OR IMMEDIATE WITH ACCUMULATOR XRI performs an exclusive OR operation using the contents of the second instruction byte and the contents of the accumulator. The result is placed in the accumulator. XRI also resets the carry and auxiliary carry flags to zero.

### Forms

```asm
XRI         data
```

- Cycles: 2 | States: 7 | Addressing: immediate | Flags: Z,S,P,CY,AC

The operand must specify the data to be used in the OR operation. This data may be in the form of a number, an ASCII constant, the label of some previously defined value, or an expression. The data may not exceed one byte. The assembler's relocation feature treats all external and relocatable symbols as 16-bit addresses. When one of these symbols appears in the operand expression of an immediate instruction, it must be preceded by either the HIGH or LOW operator to specify which byte of the address is to be used in the evaluation of the expression. When neither operator is present, the assembler assumes the LOW operator and issues an error message. o          o data Summary of Logical Operations AND produces a one bit in the result only when the corresponding bits in the test data and the mask data are ones. OR produces a one bit in the result when the corresponding bits in either the test data or the mask data are ones. Exclusive OR produces a one bit only when the corresponding bits in the test data and the mask data are different; i.e., a one bit in either the test data or the mask data - but not both - produces a one bit in the resul t. AND         OR        EXCLUSIVE OR 1010 1010  1010 1010     1010 1010 0000 1111  0000 1111     0000 11 n 0000 1010  10101111      10100101

### Examples

```text
Assume that a program uses bits 7 and 6 of a byte as flags that control the calling of two subroutines. The
program tests the bits by rotating the contents of the accumulator until the desired bit is in the carry flag; a
CC instruction (Call if Carry) tests the flag and calls the subroutine if required.
Assume that the control flag byte is positioned normally in the accumulator, and the program must set OFF bit
6 and set bit 7 ON. The remaining bits, which are status flags used for other purposes, must not be altered.
Since any bit exclusive-ORed with a one is complemented, and any bit exclusive-ORed with a zero remains
unchanged, the following instruction is used:
XRI       110000008
The instruction has the following results:
Accumulator    01 001100
Immediate data 11000000
10001100
```

---

<a id="xthl"></a>

## `XTHL` — Exchange H&L With Top Of Stack

XTHL exchanges two bytes from the top of the stack with the two bytes stored in the HL registers. Thus, XTHL both saves the current contents of the HL registers and loads new values into HL.

### Forms

```asm
XTHL
XTHL exchanges the contents of the L register with the contents of the memory location specified by the SP
```

- Cycles: 5 | States: 18 (16on8085) | Addressing: register indirect | Flags: none

### Examples

```text
Assume that the stack pointer register contains 1 OADH; register H contai ns OBH and L contains 3CH; and
memory locations 10ADH and 10AEH contain FOH and ODH, respectively. The following is an illustration of
the effect of the XTHL instruction:
MEMORY ADDRESS           H    L
10AC  lOAD   10AE   lOAF
Before XTHL    FF     FO    OD     FF     OB   3C
After XTHL     FF     3C     OB    FF      OD  FO
The stack pointer register remains unchanged following execution of the XTH L instruction.
4. ASSEMBLER  DIRECTIVES
This chapter describes the assembler directives used to control the 8080/85 assembler in its generation of object
code. This chapter excludes the macro directives, which are discussed as a separate topic in Chapter 5.
Generally, directives have the same format as instructions and can be interspersed throughout your program.
Assembler directives discussed in this chapter are grouped as follows:
GENERAL DI RECTIVES:
•  Symbol Definition
EQU
SET
•  Data Definition
DB
DW
•  Memory Reservation
DS
•  Conditional Assembly
IF
ELSE
ENDIF
•  Assembler Termination
END
LOCATION COUNTER CONTROL AND RELOCATION:
•  Location Counter Control
ASEG
DSEG
CSEG
ORG
•  Program Linkage
PUBLIC
EXTRN
NAME
STKLN
4-1
```
