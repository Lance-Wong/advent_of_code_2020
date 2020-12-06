#questions is the input

groups = questions.split('\n\n')

yes_summation = 0
unique_yes_summation = 0

for group in groups:
    answered_yes_dict = {}
    individual_answers = group.replace('\n',' ')
    for response in individual_answers:
        if response not in answered_yes_dict.keys():
            answered_yes_dict[response] = 1
        else:
            answered_yes_dict[response] += 1
            
    #part 1
    yes_summation += len([x for x in answered_yes_dict if x != ' '])

    
    #part 2
    if ' ' in answered_yes_dict.keys():
        total_elements = answered_yes_dict[' ']+1
    else:
        total_elements = 1
        unique_yes = len([x for x in answered_yes_dict if answered_yes_dict[x] == total_elements])
    unique_yes_summation += unique_yes
        
print(yes_summation)
print(unique_yes_summation)
