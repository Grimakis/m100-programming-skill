#!/usr/bin/env python
from __future__ import annotations

import argparse
import json
import pathlib
from typing import Any

from emu_runner import (
    assemble_source,
    load_program,
    read_u16,
    run_until_ret,
    write_u16,
)


def _parse_range(val: Any) -> list[int]:
    if isinstance(val, int):
        return [val]
    if isinstance(val, list):
        return [int(v) for v in val]
    if isinstance(val, str) and ".." in val:
        start_s, end_s = val.split("..", 1)
        start = int(start_s)
        end = int(end_s)
        return list(range(start, end + 1))
    raise SystemExit(f"Invalid range value: {val}")


def _layout_cell_addr(layout: dict[str, Any], row: int, col: int) -> int:
    base = int(layout["base"])
    cols = int(layout["cols"])
    cell_bytes = int(layout.get("cell_bytes", 2))
    return base + ((row * cols) + col) * cell_bytes


def _apply_writes(cpu, layouts: dict[str, Any], writes: list[dict[str, Any]]) -> None:
    for w in writes:
        if "layout" in w:
            layout = layouts[w["layout"]]
            addr = _layout_cell_addr(layout, int(w["row"]), int(w["col"]))
            write_u16(cpu, addr, int(w["u16"]))
        else:
            write_u16(cpu, int(w["addr"]), int(w["u16"]))


def _apply_fills(cpu, layouts: dict[str, Any], fills: list[dict[str, Any]]) -> None:
    for f in fills:
        layout = layouts[f["layout"]]
        rows = _parse_range(f["rows"])
        cols = _parse_range(f["cols"])
        val = int(f["u16"])
        for r in rows:
            for c in cols:
                addr = _layout_cell_addr(layout, r, c)
                write_u16(cpu, addr, val)


def _expect_cells(cpu, layouts: dict[str, Any], cells: list[dict[str, Any]]) -> None:
    for c in cells:
        layout = layouts[c["layout"]]
        addr = _layout_cell_addr(layout, int(c["row"]), int(c["col"]))
        got = read_u16(cpu, addr)
        want = int(c["u16"])
        if got != want:
            raise SystemExit(f"expect cell {c['layout']} r{c['row']} c{c['col']}: {got} != {want}")


def _expect_grid(cpu, layouts: dict[str, Any], grids: list[dict[str, Any]]) -> None:
    for g in grids:
        layout = layouts[g["layout"]]
        rows = _parse_range(g["rows"])
        cols = _parse_range(g["cols"])
        want = int(g["u16"])
        skip = {(int(s["row"]), int(s["col"])) for s in g.get("except_cells", [])}
        for r in rows:
            for c in cols:
                if (r, c) in skip:
                    continue
                addr = _layout_cell_addr(layout, r, c)
                got = read_u16(cpu, addr)
                if got != want:
                    raise SystemExit(
                        f"expect grid {g['layout']} r{r} c{c}: {got} != {want}"
                    )


def _apply_registers(cpu, regs: dict[str, Any]) -> None:
    for name, val in regs.items():
        reg = getattr(cpu, name, None)
        if reg is not None and hasattr(reg, "value"):
            reg.value = int(val)
        else:
            setattr(cpu, name, int(val))


def _run_case(case: dict[str, Any], asm, cpu_cls, layouts: dict[str, Any]) -> None:
    cpu = load_program(asm, cpu_cls)
    if "registers" in case:
        _apply_registers(cpu, case["registers"])
    if "fills" in case:
        _apply_fills(cpu, layouts, case["fills"])
    if "writes" in case:
        _apply_writes(cpu, layouts, case["writes"])

    run_until_ret(cpu, int(case.get("max_steps", 50000)))

    if "expect_grid" in case:
        _expect_grid(cpu, layouts, case["expect_grid"])
    if "expect_cells" in case:
        _expect_cells(cpu, layouts, case["expect_cells"])


def main() -> None:
    root = pathlib.Path(__file__).resolve().parents[2]
    default_spec = root / "tools" / "8085_harness" / "specs" / "snowed_in_init.json"
    default_sim = pathlib.Path(__file__).resolve().parent / "Sim8085"

    parser = argparse.ArgumentParser(description="Generic 8085 spec runner.")
    parser.add_argument("--spec", type=pathlib.Path, default=default_spec, help="Path to JSON spec")
    args = parser.parse_args()

    spec_path = args.spec.resolve()
    spec = json.loads(spec_path.read_text())

    asm_path = (spec_path.parent / spec["asm"]).resolve()
    sim_path = (spec_path.parent / spec.get("sim8085_path", default_sim)).resolve()

    asm, cpu_cls = assemble_source(asm_path, sim_path)
    layouts = spec.get("layouts", {})

    for case in spec.get("cases", []):
        _run_case(case, asm, cpu_cls, layouts)

    print("OK")


if __name__ == "__main__":
    main()
