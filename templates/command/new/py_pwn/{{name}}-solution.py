#!/usr/bin/env python3

from ptpython.repl import embed
from pwn import *


elf = context.binary = ELF("{{name}}")
libc = ELF(elf.runpath + b"/libc.so.6")  # elf.libc broke again

gs = """
continue
"""


def start():
{% if host is defined and port is defined -%}
    if args.REMOTE:
        return remote("{{host}}", {{port}})
    elif args.GDB:
{%- else %}
    if args.GDB:
{%- endif %}
        return gdb.debug(
            elf.path,
            gdb_args=["-ix", "~/gdbinit/pwndbg.gdbinit"],
            gdbscript=gs,
            env={"LD_LIBRARY_PATH": "./"},
        )
    else:
        return process(
            elf.path,
            env={"LD_LIBRARY_PATH": "./"},
        )


def delta(x, y):
    return (0xFFFFFFFFFFFFFFFF - x) + y


def main():
    io = start()

    # =============================================================================
    embed(globals(), locals(), vi_mode=False)

    # TO-DO: Solution here

    # =============================================================================

    io.interactive()


if __name__ == "__main__":
    main()
