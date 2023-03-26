def anagram(kata1,kata2):
    kata1.lower()
    kata2.lower()

    kata1 = sorted(kata1)
    kata2 = sorted(kata2)
    
    if kata1 == kata2:
        print('Anagram!')
    else:
        print('Tidak Anagram!')

kata1 = input('Masukan Kata 1 : ')
kata2 = input('Masukan Kata 2 : ')

anagram(kata1,kata2)

    