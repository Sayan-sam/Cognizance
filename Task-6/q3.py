# Taking in the file data
file = open("about.txt", "r")
text = file.read()
print(text)
file.close()

# Splitting the words into list adn sorting
text = text.split(" ")
text.sort()

# Removing the useless words
i = 0
while i < len(text):
    if(len(text[i]) < 6):
        text.remove(text[i])
    else:
        i = i+1

# Counting the words into dictionary
dict = {}
for t in text:
    if t in dict:
        dict[t] = dict[t]+1
    else:
        dict[t] = 1

# Finding the maximum number of usage of the word
max = ""
val = 0
for k in dict:
    if(dict[k] > val):
        val = dict[k]
        max = k
print("The most used word is: {} used {} times.".format(max,val))