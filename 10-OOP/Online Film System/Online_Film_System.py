# Online film satan veya kiralayan uygulamanın sistemini tasarlayın.

# Uygulamada filmler listelenebilir, sıralanabilir ve kullanıcılar uygulamaya abone olabilir.
# Kullanıcılar abonelik için sistem üzerinden kredi satın alır.
# Sadece abone olan kullanıcılar, kredileri ile film kiralayabilir ve kiraladığı filmin kredi bedeli kadar hesabından düşülür.
# Normal kullanıcılar ve aboneler film satın alabilirler.
# Eğer film mevcut değil ise talep edilebilir. 

class FilmSistemi:
    def __init__(self,film, kullanici, kredi, abonelik):
        self.film=film
        self.kullanici=kullanici
        self.kredi=kredi
        self.abonelik=abonelik

class User:
    def __init__(self,user_name,credit,isAbone):
        self.user_name=user_name
        self.credit=credit
        self.isAbone=isAbone

       
  
