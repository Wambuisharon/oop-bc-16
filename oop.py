class Country(object):
   
    def __init__(self, name, region, official_language):
        self.name = name
        self.region = region
        self.official_language=official_language

    def description(self):
        print "I'm from %s and %s is my Country" % (self.region, self.name)

    def official_language (self):
      print "%s is our official language" % (self.official_language)

    def opinion(self): 
        print "I love %s" %(self.name)

  #implementing inheritance,city is inheriting from country

class City(Country):
    
     def __init__(self,city_name,recreation_centre, number_of_schools):
        self.name = name
        self.region = region
        self.official_language=official_language
        self.recreation_centre=recreation_centre
        self.number_of_schools=number_of_schools
        self.city_name=city_name

     def number_of_schools (self) :
         print "Nairobi"

   #Implementing polymophis ...The Country class share the opinion method with the city class test

     def opinion(self):
        print "I love %s" %(self.city_name)

if __name__ == '__main__':
      kenya = Country("EastAfrica", "Kenya", "English")
               