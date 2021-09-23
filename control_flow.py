message=" "
if 1>2:
    message="if only 1 were greater than two..."
elif 1>3:
    message="elif stands for else if"
else:
    message="when all else fails use else (if you want to)"
x=22
parity="even" if x%2==0 else "odd"

x=0
while x<10:
    print(f"{x} is less than 10")
    x+=1

#range(10 )is the numbers 0,1,2,...,9
for x in range(10):
    if x==3:
        continue #go immediatly to the next iteration
    if x==5:
        break #quit the loop entirely
    print(x)
    all([True,1,{3}]) #true, all are truthy
    all([True,1,{}])   #False, {} is false
    all([True,1,{}])  #true, true is truthy
    all ({})   #true, no falsy elemnts is in the list
    any({})  #False, no truthy elements in the list
