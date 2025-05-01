import csv
import matplotlib.pyplot as plt
from datetime import datetime
from pathlib import Path

path = Path("OHUR.csv")
lines = path.read_text(encoding="utf-8").splitlines()

reader = csv.reader(lines)
header_row = next(reader)

dates = []
unemployment_rates = []

for row in reader:
    try:
        date = datetime.strptime(row[0], "%Y-%m-%d")
        unemployment_rate = float(row[1])
    except ValueError as e:
        print(row)
    else:
        dates.append(date)
        unemployment_rates.append(unemployment_rate)

plt.style.use("dark_background")
figure, graph = plt.subplots()

graph.plot(dates, unemployment_rates, color="blue")

graph.set_title("Ohio Unemployment Rate", fontsize=20)
graph.set_xlabel("Date")
graph.set_ylabel("Unemployment Rate")
figure.autofmt_xdate()

plt.show()