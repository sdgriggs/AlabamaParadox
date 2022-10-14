from datetime import datetime
import sys
import random
class State:
    name = ''
    population = 0
    seats = 0
    remainder = 0
    priorSeats = 0
    
    def __init__(self, n, p):
        self.name = n
        self.population = p
        
    def __lt__(self, other):
        return self.remainder > other.remainder
    
    def __eq__(self, other):
        return self.remainder > other.remainder
    
    def __gt__(self, other):
        return other.__lt__(self)
        
    def __ne__(self, other):
        return not self.__eq__(other)

        
        
class Nation:
    states = []
    totalPop = 0
    totalSeats = 0
    
    def __init__(self, seats):
        self.totalSeats = seats
    
    def addState(self, st):
        self.states.append(st)
        self.totalPop += st.population 
    
    def printSeats(self):
        for x in self.states:
            print(x.name + " " + str(x.seats))
            
    def part(self):
        allocated = 0
        toBeAllocated = 0
        for s in self.states:
            #print("Prior Seats: " + str(s.priorSeats))
            s.priorSeats = s.seats
            f = s.population / self.totalPop * self.totalSeats
            s.seats = int(f)
            s.remainder = f - s.seats
            
            #print(s.name + ' ' + str(f) + ' ' + str(s.seats) + ' ' + str(s.remainder))
            allocated += s.seats
        toBeAllocated = self.totalSeats - allocated
        #print("To Be Allocated " + str(toBeAllocated))
        
        self.states.sort()
        
        
        
        for i in range(0, toBeAllocated):
            self.states[i].seats += 1
        sum = 0   
        for i in self.states:
            sum += i.seats
        
        #self.printSeats()
            
    def findAlabama(self, i):
        for x in self.states:
            if(x.priorSeats > x.seats):
                #print("Paradox found from " + str(i - 1) + " to " + str(i))
                print("(" + str(i-1) + ", " + str(i)+ ")")
                #for x in self.states:
                #    print(x.name + ' ' + str(x.priorSeats) + "==>" + str(x.seats))
    
    def reset(self):
        self.states.clear()
        self.totalPop = 0
        self.totalSeats = 0
        
            
            
            
            
if __name__ == '__main__':

    s = []
    random.seed(10)
    print(sys.argv[2])
    for q in range(int(sys.argv[2])):
        i = State(str(q), random.randint(1000, 50000))
        s.append(i)

    t = datetime.now()
    for i in range(1, int(sys.argv[1])):
        #print("*************************I: " + str(i))
        griggsLandia = Nation(i)
        for x in s:
            griggsLandia.addState(x)
        #print("Length: " + str(len(griggsLandia.states)))
        griggsLandia.part()
        griggsLandia.findAlabama(i)
        griggsLandia.reset();
        #griggsLandia.printSeats()

    print("Total Seconds: " + str(datetime.now() - t))


