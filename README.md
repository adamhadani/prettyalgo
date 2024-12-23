# :sparkles: prettyalgo

Pretty print for programming puzzles.

Highlights:

* Pretty print data structures and algorithms, especially list-oriented ones
  involving arrays and iterations, in the vein of leetcode and similar
programming puzzles.

## Getting Started

To install from PyPI, use pip:

    pip install prettyalgo


See the [examples](./examples) sub-directory for examples showing the usage of the library.

Typical output when using on the terminal in interactive mode would like:

```
Remove Duplicates From Sorted Array 2
-------------------------------------
len(lst):          9
i                  6
j                  4
count              4

+-----------------------------------------------------------------------------------------+
|         |         |         |         |         |         |         |         |         |
|    0    |    0    |    1    |    1    |    1    |    1    |    2    |    3    |    3    |
|         |         |         |         |         |         |         |         |         |
+-----------------------------------------------------------------------------------------+
                                                                 ^ i=6
                                             ^ j=4

Press Enter to continue...
```
