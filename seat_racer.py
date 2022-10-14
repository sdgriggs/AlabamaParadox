import os
from datetime import datetime

t = datetime.now()
simonTime = t - t
joeyTime = t - t
rng = 10
seats = [10, 100, 1000, 10000, 100000, 1000000]
print("    SEATS    | Method |     Time")
print("-------------|--------|---------------")
for j in seats:
    for i in range(0, rng):
        simonStart = datetime.now()
        os.system("python3 AlabamaParadox.py " + str(j) + " 3 > simon.out.txt")
        simonEnd = datetime.now()
        joeyStart = datetime.now()
        os.system("python3 Joey-AlabamaParadox.py " + str(j) + " 3 > joey.out.txt")
        joeyEnd = datetime.now()

        simonTime += simonEnd - simonStart
        joeyTime += joeyEnd - joeyStart

    print("  " + str(j).ljust(10) + " |  Simon | " + str(simonTime))
    print("  " + str(j).ljust(10) + " |  Joey  | " + str(joeyTime ))
    print("-------------|--------|---------------")