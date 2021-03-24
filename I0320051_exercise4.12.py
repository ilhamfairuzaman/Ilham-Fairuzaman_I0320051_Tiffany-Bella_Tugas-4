# !/usr/bin/python

a = 60    # 60 = 0011 1100
b = 13    # 13 = 0000 1101
c = 0

c = a & b
print('Line 1 - value of c is ', c,'binary :', format(c,'08b'))

c = a | b
print('Line 1 - value of c is ', c,'binary :', format(c,'08b'))

c = a ^ b
print('Line 1 - value of c is ', c,'binary :', format(c,'08b'))

c = ~a
print('Line 1 - value of c is ', c,'binary :', format(c,'08b'))

c = a >> 2
print('Line 1 - value of c is ', c,'binary :', format(c,'08b'))

c = a << 2
print('Line 1 - value of c is ', c,'binary :', format(c,'08b'))