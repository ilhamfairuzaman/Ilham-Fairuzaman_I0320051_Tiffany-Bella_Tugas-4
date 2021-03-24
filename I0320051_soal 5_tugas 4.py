# String yang akan dimodifikasi
s = 'Hey there! what should this string be?'

# Memodifikasi string sesuai dengan permintaan
s = s[:20]
print(s)
s = s.replace('re','ra')
s = s.replace('Hey ','Stro')
s = s.replace('shou','ome!')

# String hasil modifikasi
print('-'*30)
print(s)
print('-'*30)

# Panjang harusnya 20
print('\npanjang dari s = %d' % len(s))
print('-'*30)

# huruf pertama 'a' harusnya di index no 8
print('\nkemunculan pertama a = %d' % s.index('a'))
print('-'*30)

# jumlah huruf a harusnya 2
print('\na muncul sebanyak %d' % s.count('a'), 'kali')
print('-'*30)

# memotong string berdasarkan index
print("Lima karakter pertama adalah '%s'" % s[:5])
print("Lima karakter berikutnya adalah '%s'" % s[5:10])
print("Karakter ketiga belas adalah '%s'" % s[12])
print("Karakter dengan indeks ganjil adalah '%s'" %s[1::2])
print("\nLima karakter terakhir adalah '%s'" % s[-5:])
print('-'*30)

# konversi ke uppercase
print('\nString dalam huruf besar : %s' % s.upper())
print('-'*30)

# konversei ke lowercas
print('\nString dalam huruf kecil : %s' % s.lower())
print('-'*30)

# cek bagaimana string dimulai
if s.startswith("Str"):
    print('\nString dimulai dengan "Str". Good!')
    print('-'*30)

# cek bagaimana string selesai
if s.endswith("ome!"):
    print('\nString dikahiri dengan "ome!". Good!')
    print('-'*30)

# Pisahkan string menjadi tiga string yang berbeda

# masing-masing hanya berisi satu kata
print(s)
print('pisahkan kata-kata dari string tersebut: %s' % s.split(' '))
print('-'*30)