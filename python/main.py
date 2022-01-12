

file1 = open('../words/words.txt', 'r')

 
def isFive(line) :
  return len(line) == 5

def charAt(line):
  return line[1] == 'r'

def charAtFn(character, location):
  def fn(line):
    return line[location] == character
  return fn

def combined(left, right):
  def fn(value):
    return left(value) and right(value)
  return fn

def doesNotContain(chars):
  def fn(line):
      return not any(ext in line for ext in chars)
  return fn

def mustContain(chars):
  def fn(line):
      return all(ext in line for ext in chars)
  return fn

def filter(file, function) :
  Lines = file1.readlines()
  for line in Lines:
      line = line.strip()
  
      if( function(line)  ):
        print("{}".format(line))

fn = combined(isFive, charAtFn('a',1))
fn = combined(fn, charAtFn('r',4))
fn = combined(fn, doesNotContain(["e", "t", "y", "u", "p"]))
fn = combined(fn, mustContain(["v"]))
filter(file1, fn)
# filter(file1, doesNotContain(["-", "f"]))