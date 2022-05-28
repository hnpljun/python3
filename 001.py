#!/usr/bin/env python3

#打印乘法口诀
for x in range(1, 10):
    for y in range(1, x+1):
        print(y, "*", x, "=", y * x, end="  ")
    print()
