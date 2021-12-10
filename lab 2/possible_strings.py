# import random
# char_list = ['a','e','i','o','u']
# random.shuffle(char_list)
# print(''.join(char_list))


import itertools
s='aeiou'
t=list(itertools.permutations(s,len(s)))
for i in range(0,len(t)):
    print (''.join(t[i]))