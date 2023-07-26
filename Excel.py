import csv


dates = []
down_speeds = []
up_speeds = []

with open("data.txt", "r") as file:
    for line in file:
        if line is not None:
            data = line.split()
            dates.append(data[0][:-1])

            speeds = data[1].split("-")
            down_speeds.append(int(speeds[0]))
            up_speeds.append(int(speeds[1]))


data = []
for i in range(len(dates)):
    data.append([dates[i], down_speeds[i], up_speeds[i]])

with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
