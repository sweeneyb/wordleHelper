

file1 = open('../words/words.txt', 'r')
Lines = file1.readlines()
 
count = 0
# Strips the newline character
for line in Lines:
    line = line.strip()
    if( len(line) == 5 ):
      print("{}".format(line))