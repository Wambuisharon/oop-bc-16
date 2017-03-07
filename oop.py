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