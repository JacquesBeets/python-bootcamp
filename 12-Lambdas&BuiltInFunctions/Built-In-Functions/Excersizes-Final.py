# 1

def interleave(s1, s2):
  val = list(zip(s1, s2))
  joined = ["".join(s) for s in val]
  return "".join(joined)

# quicker way
def interleave(str1,str2):
    return ''.join(''.join(x) for x in (zip(str1,str2)))
   


#print(interleave("hi", "no"))


# 2

def triple_and_filter(li):
  return [l * 3 for l in (filter(lambda x: x % 4 == 0, li))]
  #return list(filter(lambda x: x % 4 == 0, li))



#print(triple_and_filter([1,2,3,4])) # [12]
#print(triple_and_filter([6,8,10,12])) # [24,36]



# 3

names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]

def extract_full_name(li):
  return [f"{l['first']} {l['last']}" for l in li]


[l['first']+" "+ l['last'] for l in li]



print(extract_full_name(names)) # ['Elie Schoppik', 'Colt Steele']

#another solution 

def extract_full_name(l):
    return list(map(lambda val: "{} {}".format(val['first'], val['last']), l))