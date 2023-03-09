while True:
    import time
    vize1 = input('birinci vize notunu girin: ')
    vize2 = input('ikinci vize notunu girin: ')
    final = input('final notunu girin: ')
    time.sleep(1.5)
    toplam_not = (float(vize1)*30/100) + (float(vize2)*30/100) + (float(final)*40/100)
    if toplam_not >= 90:
        print("harf notu: AA")
    elif toplam_not >=85:
        print("harf notu: BA")
    elif toplam_not >= 80:
        print("harf notu: BB")
    elif toplam_not >= 75:
        print("harf notu: CB")
    elif toplam_not >= 70:
        print("harf notu: CC")
    elif toplam_not >= 65:
        print("harf notu: DC")
    elif toplam_not >= 60:
        print("harf notu: DD")
    elif toplam_not >= 55:
        print("harf notu: FD")
    else:
        print("harf notu: FF")
