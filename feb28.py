"""

Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged.

""""

def not_string(str):
  if len(str)<=2 : return 'not '+str
  elif str[:3]=='not': return str
  return 'not '+str




"""
Given a non-empty string and an int n, return a new string where the char at index n has been removed. The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).

"""

def missing_char(str, n):
  return str.replace(str[n],'')


"""

Given a string and a non-negative int n, return a larger string that is n copies of the original string.

"""
def string_times(str, n):
  return n*str


"""

Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front;

"""

def front_times(str, n):
  if len(str) <3: return n*str
  return n*str[:3]

"""
Given a non-empty string like "Code" return a string like "CCoCodCode".
"""
def string_splosion(str):
  res=""
  for i in range(len(str)+1):
    res+=str[:i]
  return res


