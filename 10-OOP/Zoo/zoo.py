#Derste Yapıldı. 
# Bir hayvanat bahçesindeki hayvanlar hakkındaki bilgileri takip etmek için bir sistem tasarlıyorsunuz.

# Hayvanlar:
# Atlar (atlar, zebralar, eşekler vb.),
# Kedigiller (kaplanlar, aslanlar vb.),
# Kemirgenler (sıçanlar, kunduzlar vb.) gibi gruplardaki türlerle karakterize edilir.
# Hayvanlar hakkında depolanan bilgilerin çoğu tüm gruplamalar için aynıdır.
# tür adı, ağırlığı, yaşı vb.
# Sistem ayrıca her hayvan için belirli ilaçların dozajını alabilmeli => getDosage ()
# Sistem Yem verme zamanlarını hesaplayabilmelidir => getFeedSchedule ()
# Sistemin bu işlevleri yerine getirme mantığı, her gruplama için farklı olacaktır. Örneğin, atlar için yem verme algoritması farklı olup, kaplanlar için farklı olacaktır.

# Polimorfizm modelini kullanarak, yukarıda açıklanan durumu ele almak için bir sınıf diyagramı tasarlayın.

class Hayvan:
    def __init__(self, tur_adi, agirligi, yas):
        self.tur_adi = tur_adi
        self.agirligi = agirligi
        self.yas = yas

    def getFeedSchedule(self):
        return [10, 20]
    
    def getDosage(self):
        return 2

class Atlar(Hayvan):
    def __init__(self, tur_adi, agirligi, yas):
        super().__init__(tur_adi, agirligi, yas)

    def getFeedSchedule(self):
        return [6, 12, 18]
    
    def getDosage(self):
        return 3
class Kemirgenler(Hayvan):
    def __init__(self, tur_adi, agirligi, yas):
        super().__init__(tur_adi, agirligi, yas)

    def getFeedSchedule(self):
        return [8, 18]
    
    def getDosage(self):
        return 1        

class Kedigiller(Hayvan):
    def __init__(self, tur_adi, agirligi, yas):
        super().__init__(tur_adi, agirligi, yas)

    def getFeedSchedule(self):
        return [6, 13, 20]
    
    def getDosage(self):
        return 2

at = Atlar("At", 150, 3)
aslan = Kedigiller("Aslan", 90, 1)
kemirgen = Kemirgenler("Kemirgen", 2, 1)                     


print(f"Atlar için:\nİlaç Dozu: {at.getDosage()}\nYem Saatleri: {at.getFeedSchedule()}\n\n")
print(f"Kedigiller için:\nİlaç Dozu: {aslan.getDosage()}\nYem Saatleri: {aslan.getFeedSchedule()}\n\n")
print(f"Kemirgenler için:\nİlaç Dozu: {kemirgen.getDosage()}\nYem Saatleri: {kemirgen.getFeedSchedule()}\n\n")