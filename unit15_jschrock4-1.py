import csv
import matplotlib.pyplot as plt
from datetime import datetime
from pathlib import Path

path = Path("OHUR.csv")
lines = path.read_text(encoding="utf-8").splitlines()
