# find duplicates in the list
my_list = [1,2,3,4,4,5,6,3]

# for loop approach with list attribute .count
new_list = []
for i in my_list:
    if my_list.count(i) > 1:
        new_list.append(i)

new_set = set(new_list)
output = ', '.join(map(str, new_set))
print(f'Duplicate numers are {output}') 

# same result with lambda function and filer
lambda_set = set(filter(lambda item: my_list.count(item) > 1, my_list))
output = ', '.join(map(str, lambda_set))
print(f'Duplicate numers are {output}') 