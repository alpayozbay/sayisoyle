def sayısöyle(sayı):
    """
        Sayının Türkçe okunuşunu döndürür.
        1 Kentilyon'a dek (10e18 veya 1000 Katrilyon) sayısına kadar Türkçe okur

        Ondalık sayıları 1000 in altında ise üç haneli sayı olarak 1000 üzeri ise tek tek sayıları okur

        Parametre:
            sayı: Okunacak sayı

        Döndürdüğü Sonuç:
            Türkçe okunuş

    """
    birlik = ['bir','iki','üç','dört','beş','altı','yedi','sekiz','dokuz']
    onluk = ['on','yirmi','otuz','kırk','elli','altmış','yetmiş','seksen','doksan']
    binlik = ['','bin','milyon','milyar','trilyon','katrilyon']

    def üçlüsayısöyle(sayı):
        sonuç = ''
        if (sayı==0): sonuç = 'sıfır'
        elif (sayı<1000):
            sayı = int(sayı)
            if (sayı>199): sonuç = birlik[sayı//100 - 1] + ' yüz'
            elif (sayı>99): sonuç = 'yüz'
            if ((sayı%100)>9): sonuç += ' '+onluk[(sayı%100)//10 -1]
            if (sayı%10>0): sonuç += ' '+birlik[sayı%10-1]

        return sonuç.strip()

    def sıraileoku(sayı):
        sonuç = ''
        s = str(sayı)
        for i in s:
          if (i=='0'): sonuç += ' sıfır '
          else: sonuç += ' ' + birlik[int(i)-1]
        return sonuç.strip()

    def ondalıksöyle(sayı):
        sonuç = ''
        if (sayı<1000): sonuç = üçlüsayısöyle(sayı)
        else: sonuç = sıraileoku(sayı)
        return sonuç.strip()

    sonuç = ''
    if (sayı==0): sonuç = 'sıfır'
    else:
        ondalık = int(str(sayı).split('.')[1])

        for i in range(0,6):
            kontrol = 10**((5-i)*3)
            if (sayı>=kontrol):
                if ((i==4) and (sayı<2000)): sonuç += ' bin'
                else: sonuç += ' ' + üçlüsayısöyle(sayı//kontrol ) + ' ' + binlik[5-i]
                sayı = sayı % kontrol

        if (ondalık>0):
            sonuç += 'nokta '+ondalıksöyle(ondalık)

    return sonuç.strip()
