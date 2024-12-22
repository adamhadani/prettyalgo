"""Pretty printing module."""

import os
import re
import sys
from time import sleep
from typing import List

NEW_LINE = "\n"
V_SEP = "|"


def build_vpad(s):
    """Helper method to build the vertical padding for a list,
    given the primary string representation already constructed.

    """
    return re.sub(r"[^\s|]", " ", s)


class PrettyListPrinter:
    def __init__(self, padding=1, v_padding=0, animate=True, animate_fps=1):
        """A pretty printer for list objects useful in particular for visualizing algorithms involving
        iteration over lists with one or more pointers.

        Implements an interface similar to the native Python pprint module.

        """
        self.padding = padding
        self.v_padding = v_padding
        self.animate = animate
        self.animate_fps = animate_fps

        # used to track state as a context manager
        self.using_context = False

    def __enter__(self):
        self.using_context = True
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.using_context = False
        return

    def pformat(self, lst: List, ptrs=None, context=None):
        if not lst:
            return "<Empty List>"

        pad = " " * self.padding
        ham = (
            f"{V_SEP}{pad}" + f"{pad}|{pad}".join(str(x) for x in lst) + f"{pad}{V_SEP}"
        )
        bun = "-" * len(ham)

        if self.v_padding > 0:
            vpad = NEW_LINE.join((build_vpad(ham) for i in range(self.v_padding)))
            ham = NEW_LINE.join((vpad, ham, vpad))

        sando = NEW_LINE + NEW_LINE.join((bun, ham, bun)) + NEW_LINE

        fries = []
        if ptrs:
            # given some pointers to list to display
            cell_border_pos = [pos for pos, char in enumerate(ham) if char == V_SEP]

            for name, value in ptrs.items():
                if value < 0 or value > len(lst) - 1:
                    # Out of bounds
                    fries.append(
                        f"{name} = {value} is out of bounds! (0 <= N <= {len(lst)=})"
                    )
                else:
                    display_pos = (
                        cell_border_pos[value] + cell_border_pos[value + 1]
                    ) // 2
                    fries.append(" " * display_pos + f"^ {name}={value}")
        fries = NEW_LINE.join(fries) + NEW_LINE

        soda = []
        if context:
            for name, value in context.items():
                soda.append(f"{name} = {value}")
        soda = NEW_LINE.join(soda) + NEW_LINE

        return sando + fries + soda

    def pprint(self, lst: List, fp=None, *args, **kwargs):
        fp = fp if fp else sys.stdout
        if self.using_context:
            if self.animate:
                sleep(1 / self.animate_fps)
                os.system("clear")
        fp.write(self.pformat(lst, *args, **kwargs))

    # alias for pprint
    pp = pprint


class PrettyList(list):
    def __str__(self):
        return PrettyListPrinter(padding=1).pprint(self)
