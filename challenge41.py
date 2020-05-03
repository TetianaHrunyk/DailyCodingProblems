"""
Given an unordered list of flights taken by someone, each represented 
as (origin, destination) pairs, and a starting airport, compute the person's 
itinerary. If no such itinerary exists, return null. If there are multiple
 possible itineraries, return the lexicographically smallest one. 
 All flights must be used in the itinerary.

For example, given the list of flights 
[('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')] 
and starting airport 'YUL', you should return the list 
['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].

Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] 
and starting airport 'COM', you should return null.

"""


class Itinerary:
    
    def __init__(self, flights, ffrom):
        self.flights = flights
        self.itinerary = []
        self.iter = len(flights)
        self.ffrom = ['start', ffrom]
        
    def isOption(self, ffrom):
        fto = None
        for f in self.flights:
            if ffrom[1] == f[0]:
                if fto == None:
                    fto = f
                else:
                    if fto[0] > f[0]:
                        fto = f
        return fto
        
    def getItinerary(self):
        
        def innerItinerary(itineraty, flights, ffrom):
            
            if len(itinerary) == self.iter:
                #print("Lenths are the same")
                return True
             
            for i in range(self.iter):
                option = self.isOption(ffrom)
                if option:
                    itinerary.append(option)
                    flights.remove(option)
#                    print(f"There is an potion {option}")
#                    print(f"Itinerary: {itinerary}, flights{flights}")
#                    print()
                    if innerItinerary(itinerary, flights, option) == True:
                         return True
                     
                    flights.append(option)
                    #print(f"Backtrack, append {option} to flights: ")
                    #print("Flights: ", flights)
                    #print()
                    
            
            return False
        
        ffrom = self.isOption(self.ffrom)
        itinerary = [ffrom]
        self.flights.remove(ffrom)
        res = innerItinerary(itinerary, self.flights.copy(), ffrom = ffrom)
        
        self.itinerary = itinerary
        return res
    
    def printItinerary(self):
        if self.getItinerary():
            res = [self.itinerary[0][0]]
            for r in self.itinerary:
                res.append(r[1])
            return res
            
        else:
            return None
    
if __name__ == "__main__":
    itinerary = Itinerary([('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')], 'YUL')
    print(itinerary.printItinerary())
    
    itinerary = Itinerary([('SFO', 'COM'), ('COM', 'YYZ')] , 'COM')
    print(itinerary.printItinerary())
                     
    itinerary = Itinerary([('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] , 'A')
    print(itinerary.printItinerary())
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                 
        
    