import pandas as pd

path = 'C:/Users/Jinbo Jonez/Desktop/python stuff/reto5xcl.xlsx'
dataFrame = pd.read_excel(path)

dataFrame.to_csv("reto5.csv", index=None, header= True)

result = pd.DataFrame(pd.read_csv("reto5.csv"))
