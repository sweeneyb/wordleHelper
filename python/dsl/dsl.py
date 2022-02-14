import utils

words = open('../../words/words.txt', 'r')
# dsl = open('dsl.txt', 'r')

def getWords(file) :
    words = []
    Lines = file.readlines()
    for line in Lines:
        line = line.strip()
        words.append(line)
    return words    

predicates = []

with open('dsl.txt', 'r') as file:
    for line in file:
        line = line.strip()
        if not line or line[0] == '#':
            continue
        parts = line.split()
        # print(parts)
        # print(parts[0])
        # print(getattr(utils, parts[0])(*parts[1:]))
        predicates.append(getattr(utils, parts[0])(*parts[1:]))  



result = utils.filter(getWords(words), utils.and_predicates(predicates))
for x in result:
    print("{}".format(x))
