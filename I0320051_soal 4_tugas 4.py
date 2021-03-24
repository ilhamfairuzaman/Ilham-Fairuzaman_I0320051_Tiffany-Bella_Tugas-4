def kursus():
    usia = float(input('Berapa umurmu?\n= '))
    if usia >= 21:
        spesifikasi = str(input('Apakah anda lulus ujian kualifikasi? (Y/T) >> '))
        if spesifikasi == 'y' or 'Y':
            print('Anda dapat mendaftar di kursus')
        elif spesifikasi == 't' or 'T':
            print('Anda tidak dapat mendaftar di kursus')
        else:
            print('Perintah salah')
    else:
        print('Anda tidak dapat mendaftar di kursus')
        kursus()

kursus()