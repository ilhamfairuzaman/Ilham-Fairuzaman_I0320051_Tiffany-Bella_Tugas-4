def koper():
    berat_koper = float(input('Masukkan berat koper(kg)>> '))
    berat_koper = berat_koper * 2.2
    y = berat_koper <= 50
    if y == True:
        print(True, ': diperbolehkan masuk ke dalam pesawat')
    else:
        print(False, ': tidak diperbolehkan masuk ke dalam pesawat')

koper()