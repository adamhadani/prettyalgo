#!/usr/bin/env python
"""
Example of using the library with a duplicate finding algorithm
"""

import sys

from prettyalgo.pprint import PrettyListPrinter


def main():
    # some common print parameters we can tweak
    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]

    with PrettyListPrinter(padding=4, v_padding=1) as pprint:
        i, j = 1, 1
        count = 1
        while i < len(nums):
            pprint.pp(nums, ptrs=dict(i=i, j=j))
            if nums[i] == nums[i - 1]:
                count += 1
                if count > 2:
                    i += 1
                    continue
            else:
                count = 1

            nums[j] = nums[i]
            j += 1
            i += 1

        pprint.pp(nums, ptrs=dict(i=i, j=j))


if __name__ == "__main__":
    sys.exit(main())
