#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      91902
#
# Created:     04-02-2025
# Copyright:   (c) 91902 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------
N = int(input())
for i in range(1, N):
    print((10**i - 1) // 9 * i)

#10**i - 1) // 9 creates numbers made of all 1s:

# When i = 1 → 1
#When i = 2 → 11
#When i = 3 → 111
#When i = 4 → 1111

#Multiplying by i repeats the number i times:

#1 × 1 = 1
#11 × 2 = 22
#111 × 3 = 333