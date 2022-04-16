#!/usr/bin/env python3

""" 
        Bold    Underline
 Italic  / Blinking /  Dbl-Underline
   /    /   /      /    /  Future Use 
  |     |   |     |     |   |   |   |
|----|----|----|----|----|----|----|----|
| 7  | 6  | 5  | 4  | 3  | 2  | 1  | 0  |
|_______________________________________|
| 128| 64 | 32 | 16 | 8  | 4  | 2  | 1  |
|_______________________________________|
"""

log = lambda x: print("%3.i, %s" % (x, f"{x:0{8}b}"))

# 128
italic = 0b10000000
log(italic)

# italic + underline
underline_x_italic = italic | 16
log(underline_x_italic)

# turn off italic
underline = underline_x_italic ^ 128
log(underline)

