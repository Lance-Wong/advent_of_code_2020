from collections import Counter

passwords= '''https://adventofcode.com/2020/day/2/input'''
key_pass = [x.split(': ') for x in passwords.split('\n')]

valid_count1 = 0
valid_count2 = 0
for x in key_pass:
    password = x[1]
    string_counts = Counter(x[1])
    match = x[0].split()[1]
    contain_count = x[0].split()[0].split('-')
    
    policy1 = password[int(contain_count[0])-1] == match
    policy2 = password[int(contain_count[1])-1] == match
    #     oneindexing
    
    
    if policy1 is True and policy2 is False:
        valid_count2 += 1
    elif policy1 is False and policy2 is True:
        valid_count2 +=1
        
        
    if  int(contain_count[0]) <= string_counts[match] <= int(contain_count[1]):
        valid_count1 += 1    

print(valid_count1,valid_count2)
