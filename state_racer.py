import os
from datetime import datetime
import SimonAlabamaParadox
import JoeyAlabamaParadox
import JoeyAlabamaParadox2


t = datetime.now()
simonTime = 0
joeyTime = 0
joeyTime2 = 0
rng = 10
states = [1, 5, 10, 25, 50, 100, 1000, 2500, 5000]#, 10000] #, 100000, 1000000]
print("   States    | Method |     Time")
print("-------------|--------|---------------")
for j in states:
    for i in range(0, rng):
        '''
        simonStart = datetime.now()
        os.system("python3 AlabamaParadox.py 500 " + str(j) + " > simon.out.txt")
        simonEnd = datetime.now()
        joeyStart = datetime.now()
        os.system("python3 Joey-AlabamaParadox.py 500 " + str(j) + " > joey.out.txt")
        joeyEnd = datetime.now()

        simonTime += simonEnd - simonStart
        joeyTime += joeyEnd - joeyStart'''
    
        simonTime += SimonAlabamaParadox.run(500, str(j), False)
        joeyTime += JoeyAlabamaParadox.run(500, str(j), False)
        joeyTime2 += JoeyAlabamaParadox2.run(500, str(j), False)

    print("  " + str(j).ljust(10) + " |  Simon | " + str(simonTime))
    print("  " + str(j).ljust(10) + " |  Joey  | " + str(joeyTime ))
    print("  " + str(j).ljust(10) + " |  Joey 2| " + str(joeyTime2))
    print("-------------|--------|---------------")