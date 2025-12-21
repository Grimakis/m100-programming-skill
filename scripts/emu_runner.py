from __future__ import annotations

import pathlib
import sys


def add_sim8085_path(sim8085_path: pathlib.Path) -> None:
    if not sim8085_path.exists():
        raise SystemExit(f"Sim8085 path not found: {sim8085_path}")
    sys.path.insert(0, str(sim8085_path))


def assemble_source(asm_path: pathlib.Path, sim8085_path: pathlib.Path):
    add_sim8085_path(sim8085_path)
    from emu import assembler, emu8085  # type: ignore

    lines = asm_path.read_text().splitlines()
    asm = assembler()
    ok, msg = asm.assemble(lines)
    if not ok:
        raise SystemExit(f"ASM assemble failed: {msg}")
    return asm, emu8085


def load_program(asm, cpu_cls):
    cpu = cpu_cls()
    cpu.reset()
    for addr, written in enumerate(asm.writtenaddresses):
        if written != 0:
            cpu.memory[addr].value = asm.pmemory[addr]
    cpu.PC.value = asm.ploadoff
    return cpu


def step_cpu(cpu) -> int:
    op = cpu.memory[cpu.PC.value].value
    if cpu.__class__.__module__ == "emu" and op in (0x09, 0x19, 0x29, 0x39):
        hl = (cpu.H.value << 8) | cpu.L.value
        if op == 0x09:
            rp = (cpu.B.value << 8) | cpu.C.value
        elif op == 0x19:
            rp = (cpu.D.value << 8) | cpu.E.value
        elif op == 0x29:
            rp = hl
        else:
            rp = cpu.SP.value
        total = (hl + rp) & 0xFFFF
        cpu.H.value = (total >> 8) & 0xFF
        cpu.L.value = total & 0xFF
        cpu.PC.value = (cpu.PC.value + 1) & 0xFFFF
        return op

    cpu.runcrntins()
    return op


def run_until_ret(cpu, max_steps: int = 50000) -> None:
    for _ in range(max_steps):
        op = step_cpu(cpu)
        if op == 0xC9:
            return
    raise SystemExit("Execution did not return within step limit")


def write_u16(cpu, addr: int, val: int) -> None:
    cpu.memory[addr].value = val & 0xFF
    cpu.memory[addr + 1].value = (val >> 8) & 0xFF


def read_u16(cpu, addr: int) -> int:
    lo = cpu.memory[addr].value
    hi = cpu.memory[addr + 1].value
    return lo | (hi << 8)


def write_u8(cpu, addr: int, val: int) -> None:
    cpu.memory[addr].value = val & 0xFF


def read_u8(cpu, addr: int) -> int:
    return cpu.memory[addr].value
