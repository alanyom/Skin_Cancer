
import statistics

data = []
num = input()
data = num.split(" ")
for i in range(0, len(data)):
    data[i] = int(data[i])

mean = sum(data) / len(data)
std = statistics.stdev(data)

def reading(mean, std):
    if 40 <= mean <= 80 and std >= 10:
        return "Skin Cancer"
    elif mean < 40 or mean > 230:
        return "Recalibrate Microscope"
    elif std < 10 or 80 < mean <= 230:
        return "Benign Skin Mole"

print(reading(mean, std))
