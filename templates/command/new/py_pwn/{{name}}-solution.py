#!/usr/bin/env python3

from pwn import *


elf = context.binary = ELF("{{name}}")
libc = ELF(elf.runpath + b"/libc.so.6")  # elf.libc broke again

gs = """
continue
"""


def start():
    if args.GDB:
        return gdb.debug(
            elf.path, gdb_args=["-ix", "~/gdbinit/pwndbg.gdbinit"], gdbscript=gs
        )
    else:
        return process(elf.path)


def delta(x, y):
    return (0xFFFFFFFFFFFFFFFF - x) + y


def main():
    io = start()

    # =============================================================================

    # TO-DO: Solution here

    # =============================================================================

    io.interactive()


if __name__ == "__main__":
    main()
