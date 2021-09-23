from collections import Counter
import re
f=open("content.txt")
lines=f.readlines()
total_count=sum(len(line) for line in lines)

line=lines[0] #sozluge atılabilir
word_count=Counter(re.split(r"\s",line))
f.close()

f=open("content.txt") #sozluk olusturuyor
files=f.read()
word_count=Counter(re.split(r"\s",files))

print(word_count)
for word,count in word_count.most_common(10):
    print(word,count)

f.close()