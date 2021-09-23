x=[4,1,2,3]
y=sorted(x) # yis [1,2,3,4], x is unchanged
x.sort() # now x is [1,2,3,4]

#sort the list by absolute value from largest to smallest
x=sorted([-4,1,-2,3],key=abs,reverse=true)

#sort th wprds and counts from highest count to lowest
wc=sorted(word_count.items(), # ["ahmet",3] gibi
         key=lambda  word_and_count: word_and_count[1],
         reverse=True)#isimsiz fonsyon lambda