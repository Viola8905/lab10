import datetime

class Known_information_about_the_traveller:
    def __init__(self,name,profession,day,month,year):
        self.name=name
        self.profession=profession
        self.birthday=Data(day,month,year)
class Data:
    def __init__(self, day, month, year):
        self.now = datetime.datetime.now()
        self.day = day
        self.month = month
        self.year = year

    def isPassTime(self, tripDays):

        finalDay = (tripDays % 365) % 30 + self.day
        finalMonth = (tripDays % 365) // 30 + self.month
        finalYear = tripDays // 365 + self.year

        if finalDay > 31:
            finalDay -= 31
            finalMonth += 1
        if finalMonth > 12:
            finalYear += 1
            finalMonth -= 12
        finalDate = datetime.date(finalYear, finalMonth, finalDay)
        return finalDate >= self.now.date()

    def timeToEndTime(self, tripDays):
        finalDay = (tripDays % 365) % 30 + self.day
        finalMonth = (tripDays % 365) // 30 + self.month
        finalYear = tripDays // 365 + self.year

        if finalDay > 31:
            finalDay -= 31
            finalMonth += 1
        if finalMonth > 12:
            finalYear += 1
            finalMonth -= 12
        finalDate = datetime.date(finalYear, finalMonth, finalDay)
        return finalDate - self.now.date()

    def monthToStay(self, tripDays):
        return tripDays // 30

class AdressOfTraveller:
    def __init__(self,country,region,city,village,street,numberOfhouse,day,month,year,termin,name,profession,dayOfbirth,
                 monthOfbirth,yearOfbirth):
        self.country=country
        self.dateOfregistration=Data(day,month,year)
        self.region=region
        self.city=city
        self.village=village
        self.street=street
        self.numberOfhouse=numberOfhouse
        self.day=day
        self.month=month
        self.year=year
        self.termin=termin
        self.name=name
        self.profession=profession
        self.dayOfbirth=dayOfbirth
        self.monthOfbirth=monthOfbirth
        self.yearOfbirth=yearOfbirth

    def isPassTime(self):
        return self.dateOfregistration.isPassTime(self.termin)

    def timeToEndTime(self):
        return self.dateOfregistration.timeToEndTime(self.termin)

    def monthToStay(self):
        return self.dateOfregistration.monthToStay(self.termin)

country=input("Country:")
region=input("region:")
city=input("city")
village=input("Village:")
street=input("street:")
numberOfhouse=input("numberOfhouse:")
day=input("day:")
month=input("month:")
year=input("year:")
termin=input("termin:")
name=input("name:")
profession=input("profession:")
dayOfbirth=input("day of birth:")
monthOfbirth=input("month of birth:")
yearOfbirth=input("year of birth:")

a=AdressOfTraveller(country,region,city,village,street,numberOfhouse,day,month,year,termin,name,profession,dayOfbirth,
                 monthOfbirth,yearOfbirth)

print(a.isPassTime())
print(a.timeToEndTime())
print(a.monthToStay())
