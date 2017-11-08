a = str(input('Put your sentence here: '))
a = a.split()
unique_list = []
repeat_list = []

for i in range(0, (len(a))):
    if ',' in a[i]:
        a[i] = (a[i])[:-1]
    elif '.' in a[i]:
        a[i] = (a[i])[:-1]

counter = 0
for i in a:
    i = i.title()
    if i not in unique_list:
        unique_list.append(i)
    elif i in unique_list:
        if i not in repeat_list:
            repeat_list.append(i)
    counter += 1

print(repeat_list)
    
            
            
                       
               
