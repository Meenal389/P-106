#marks/present

import plotly.express as px
import csv
import numpy as np

def GetDataSource(data_path):
    Student_marks=[]
    Days_present=[]

    with open(data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            Student_marks.append(float(row[" Marks attained"]))
            Days_present.append(float(row["no of Days Present"]))
    return{"x":Student_marks,"y":Days_present}

def findCorrelation(dataSource):
    correlation=np.corrcoef(dataSource["x"],dataSource["y"])
    print("correlation in Marks and Days Attended",correlation[0,1])

def setup():
    data_path="MARKSPRESENT.csv"
    dataSource=GetDataSource(data_path)
    findCorrelation(dataSource)
setup()