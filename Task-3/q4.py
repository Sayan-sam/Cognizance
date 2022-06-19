import pandas as pd

ser = pd.Series(['amrita', 'school', 'of', 'engineering', 'chennai' , 'campus'])
print("Before capitalization: \n"+str(ser))
for i in range(0,ser.size):
    ser[i] = ser[i].capitalize()
print("After capitalization: \n"+str(ser))
