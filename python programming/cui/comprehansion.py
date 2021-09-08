#list comprehansion
'''ls = []
for i in range(100):
    if i%3==0:
         ls.append(i)'''


#es upper walle code ko ham ek line me likh sakte the jese ham list comprehansion khate hai
ls = [i for i in range(100) if i%3==0]

print(ls)