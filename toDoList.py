import pandas as pd
import numpy as np
import datetime as dt

def load(fileName):
    df = pd.DataFrame()
    print("Heips") 
    
    df = pd.read_csv(fileName)
    
    print(df)
        
    return df


def save(data,to = "tasks.csv"):

    data.to_csv(to)

    return

def calculateUrgency(df):
    print(df['DL'][0])
    d,m,y = df['DL'][0].split('/')

    print(d)

if __name__ == '__main__':
    
    data = {'Task':['Homework'],'DL':['8/3/2018'],'Importance':[4]}

    df = pd.DataFrame(data,columns=['Task','DL','Importance'])

#    save(df)
 #   df = load("tasks.csv")

    calculateUrgency(df)
