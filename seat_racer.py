import os
from datetime import datetime
import SimonAlabamaParadox
import JoeyAlabamaParadox

t = datetime.now()
simonTime = 0
joeyTime = 0
rng = 10
seats = [10, 100, 1000, 10000, 100000, 1000000]
print("    SEATS    | Method |     Time")
print("-------------|--------|---------------")
for j in seats:
    for i in range(0, rng):
        """simonStart = datetime.now()
        
        os.system("python3 AlabamaParadox.py " + str(j) + " 3 > simon.out.txt")
        simonEnd = datetime.now()
        joeyStart = datetime.now()
        os.system("python3 Joey-AlabamaParadox.py " + str(j) + " 3 > joey.out.txt")
        joeyEnd = datetime.now()

        simonTime += simonEnd - simonStart
        joeyTime += joeyEnd - joeyStart"""
        
        simonTime += SimonAlabamaParadox.run(str(j), 3, False)
        joeyTime += JoeyAlabamaParadox.run(str(j), 3, False)

    print("  " + str(j).ljust(10) + " |  Simon | " + str(simonTime))
    print("  " + str(j).ljust(10) + " |  Joey  | " + str(joeyTime ))
    print("-------------|--------|---------------")