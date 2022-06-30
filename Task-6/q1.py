toRead = open("onlinefile.txt")
toWrite = open("filename2.txt", "w")
data = toRead.read()

counter = 0
i = 0

while i < len(data):
    while i < len(data) and (data[i] <= '9' and data[i] >= '0') or (data[i] == "."):
        toWrite.write(data[i])
        i = i + 1
    else:
        toWrite.write(",")
        counter = (counter+1)%4
        
    while i < len(data) and (data[i] <= 'z' and data[i] >= 'a') or (data[i] <= 'Z' and data[i] >= 'A'):
        toWrite.write(data[i])
        i += 1
    else:
        if(counter == 3):
            toWrite.write("\n")
        else:
            toWrite.write(",")
        counter = (counter+1)%4
    if(i >= len(data)):
        break