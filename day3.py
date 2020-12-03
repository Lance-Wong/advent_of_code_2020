pattern = '''https://adventofcode.com/2020/day/3/input'''
shape = pattern.split('\n')


dimensions = len(shape),len(shape[0])
policies = [[1,1],[3,1],[5,1],[7,1],[1,2]]
tree_product= 1
for policy in policies:
    i,j=0,0
    counter = 0
    for x in range(dimensions[0]-1):

        i+=policy[1]
        j+=policy[0]
        if j > dimensions[1]-1:
            j-= dimensions[1]
        if i > dimensions[0]:
            break
        if shape[i][j] == '#':
            counter +=1
    print(f'''Trees for policy {policy} - {counter}''')
    # 3,1 is the solution for problem 1
    tree_product *= counter



#secondquestion
print( tree_product)
