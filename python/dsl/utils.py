

from operator import contains
from pickle import TRUE
 
# def isFive(line) :
  # return len(line) == 5

def isFive(*foo):
  def fn(line):
    return len(line) == 5
  return fn

def charAt(character, location):
  def fn(line):
    return line[int(location)] == character
  return fn

def charNotAt(character, location):
  def fn(line):
    return not line[location] == character
  return fn

def combined(left, right):
  def fn(value):
    return left(value) and right(value)
  return fn

def all_predicates(*args):
  def fn(value):
    for arg in args:
      if(not arg(value)):
        return False
    return True
  return fn

def and_predicates(args):
  def fn(value):
    for arg in args:
      if(not arg(value)):
        return False
    return True
  return fn  

def doesNotContain(chars):
  def fn(line):
      return not any(ext in line for ext in chars)
  return fn

def mustContain(chars):
  def fn(line):
      return all(ext in line for ext in chars)
  return fn

def filterAndPrint(file, function) :
  Lines = file.readlines()
  for line in Lines:
      line = line.strip()
  
      if( function(line)  ):
        print("{}".format(line))


def filter(inArray, predicate) :
  result = []
  for x in inArray:
    if ( predicate(x) ) :
      result.append(x)
  return result

# Basic test to make sure this works/filters
# filter(file1, doesNotContain(["-", "f"]))

# a simple approach where we compose functions
# fn = combined(isFive, charAtFn('a',1))
# fn = combined(fn, charAtFn('r',4))
# fn = combined(fn, doesNotContain(["e", "t", "y", "u", "p"]))
# fn = combined(fn, mustContain(["v"]))
#filter(file1, fn)

# But really, we want the variadic approach
# filter(file1, all_predicates(isFive,
#   charAtFn('m',2),
#   charNotAtFn("o",1),


#   doesNotContain(["t", "i", "v", "e", "n", "e", "s", "g"]),
#   mustContain(['o'])
  
#   ))
