# < magic card >
# Think any number in 1 ~ 31
# 5 cards are here
# Is there the number you picked?  

A = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]
B = [2, 3, 6, 7, 10, 11, 14, 15, 18, 19, 22, 23, 26, 27, 30, 31]
C = [4, 5, 6, 7, 12, 13, 14, 15, 20, 21, 22, 23, 28, 29, 30, 31]
D = [8, 9, 10, 11, 12, 13, 14, 15, 24, 25, 26, 27, 28, 29, 30, 31]
E = [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]

print(A)
a = 0 if input("is there?(Y/N)")=='N' else 1

print(B)
b = 0 if input("is there?(Y/N)")=='N' else 1

print(C)
c = 0 if input("is there?(Y/N)")=='N' else 1

print(D)
d = 0 if input("is there?(Y/N)")=='N' else 1

print(E)
e = 0 if input("is there?(Y/N)")=='N' else 1

answer = a*1 + b*2 + c*4 + d*8 + e*16
print(answer)
