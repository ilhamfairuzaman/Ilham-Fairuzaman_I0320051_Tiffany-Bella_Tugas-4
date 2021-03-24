a = 4
b = 11
print('a = 4')
print('b = 11')
print('------------------------')

print('binary', a, 'adalah =' ,format(a, '08b'))
print('binary', b, 'adalah =' ,format(b, '08b'))

# 4 | 11
print('----------- 4 | 11 -------------')
c = a | b
print('binary', c, 'adalah =' ,format(c, '08b'))

# 4 >> 11
print('----------- 4 >> 11 -------------')
d = a >> b
print('binary', d, 'adalah =' ,format(d, '08b'))

# 4 ^ 11
print('----------- 4 ^ 11 -------------')
e = a ^ b
print('binary', e, 'adalah =' ,format(e, '08b'))

# ~4
print('----------- ~4 -------------')
f = ~a
print('binary', f, 'adalah =' ,format(f, '08b'))

# 11 & 4
print('----------- 11 & 4 -------------')
g = a & b
print('binary', g, 'adalah =' ,format(g, '08b'))