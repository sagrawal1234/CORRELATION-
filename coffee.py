import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
  coffee = []
  sleep = []
  with open(data_path) as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
      coffee.append(float(row["Coffee in ml"]))
      sleep.append(float(row["sleep in hours"]))
  return {"x": coffee, "y": sleep}

def findCorrelation(data_source):
    correlation = np.corrcoef(data_source["x"], data_source["y"])
    print("correlation is: ",correlation[0,1])

def setup():
    data_path = "coffee.csv"
    data_source = getDataSource(data_path)
    findCorrelation(data_source)
setup()
