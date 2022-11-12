# Uçuşların ve pilotların yönetimi için bir sistem tasarlayın.

# Hava yolu şirketleri uçuşları gerçekleştirir. Her hava yolunun bir kimliği vardır.
# Hava yolu şirketi, farklı tipteki uçaklara sahiptir.
# Uçaklar çalışır veya onarım durumunda olabilir.
# Her uçuşun benzersiz kimliği, kalkacağı ve ineceği havaalanı, kalkış ve iniş saatleri vardır.
# Her uçuşun bir pilotu ve yardımcı pilotu vardır ve uçağı kullanırlar.
# Havaalanlarının benzersiz kimlikleri ve isimleri vardır.
# Hava yolu şirketlerinin pilotları vardır ve her pilotun bir deneyim seviyesi mevcuttur.
# Bir uçak tipi, belirli sayıda pilota ihtiyaç duyabilir. 

class AirlineCompany:
    def __init__(self,company_name ,numof_aircraft,numof_pilots):
        self.company_name = company_name
        self.numof_aircraft=numof_aircraft
        self.numof_pilots = numof_pilots

class Aircraft(AirlineCompany):
    def __init__(self,aircraft_status,model_aircraft, numof_pilots):
        self.aircraft_status = aircraft_status
        self.model_aircraft = model_aircraft
        self.numof_pilots = numof_pilots

    def isSolid(aircraft_status):
        if(aircraft_status=="Working"):
            print("Ready to Flight.")
        else:
            print("Aircraft Defective.")
        return aircraft_status

class Pilot(AirlineCompany):#or Aircraft
    def __init__(self, pilot_name,pilot_surname, experience_year, pilot_title):
            self.pilot_name = pilot_name
            self.pilot_surname=pilot_surname
            self.experience_year = experience_year
            self.pilot_title = pilot_title
            def __str__(self):
                return self.pilot_name + pilot_surname

            def pilot_title(self):
                if self.pilot_title == "Kaptan":
                    print("Captain Pilot")
                else:
                    print("Co-pilot")



class Flight(Aircraft):
    def __init__(self, flight_id,departure_time, landing_time, departure_airport, landing_airport):
        self.flight_id = flight_id
        self.departure_time = departure_time
        self.landing_time = landing_time
        self.departure_airport = departure_airport
        self.landing_airport = landing_airport

        def getDeparture_time(self):
            return self.departure_time
        def getLanding_time(self):
            return self.landing_time
        def getDeparture_airport(self):
            return self.departure_airport
        def getLanding_airport(self):
            return self.landing_airport

class Airport(Flight):
    def __init__(self,city,airport_name,airport_code):
        self.city=city
        self.airport_name = airport_name
        self.airport_code = airport_code
       




obj_Company=AirlineCompany("THY",2300,245)
print(f"{obj_Company.company_name} şirketi {obj_Company.numof_aircraft} adet uçağa ve {obj_Company.numof_pilots} pilota sahiptir.\n\n")

obj_Aircraft = Aircraft("Çalışıyor", "E213",3)
print(f"Uçak Bilgileri:\n Uçak durumu:\n {obj_Aircraft.isSolid}\n Uçak tipi: {obj_Aircraft.model_aircraft}\n Pilot sayısı: {obj_Aircraft.numof_pilots}\n\n")

obj_Pilot = Pilot("Aysu","Yılmaz",5, "Kaptan")
print(f"Pilot Bilgileri:\n ismi: {obj_Pilot.pilot_name}\n Sosm: {obj_Pilot.pilot_surname}\n Deneyim yılı: {obj_Pilot.experience_year}\n Pilot unvanı: {obj_Pilot.pilot_title}\n\n")

obj_Flight = Flight("71145","9.00 AM","11.00 AM","İzmir","Mersin")
print(f"Uçuş Bilgileri:\n Uçuş kodu: {obj_Flight.flight_id}\n Kalkış saati: {obj_Flight.departure_time}\n İniş saati: {obj_Flight.landing_time}\n Kalkacağı havalimanı: {obj_Flight.departure_airport}\n İniş yapacağı havalimanı: {obj_Flight.landing_airport}\n\n")

obj_Airport=Airport("12","İzmir","Adnan Menderes Airport")
print(f"Havaalanı Bilgileri :\n Id:{obj_Airport.airport_code}\n Şehir:{obj_Airport.city} \n İsim:{obj_Airport.airport_name}")