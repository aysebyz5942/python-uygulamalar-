document="merhabalar arkadaşalr nasılsınız!! Sizlere çok önemli bir haberim var"


word_counts={} #dictionnaire

for word in  document: #document içerisindeki elemalar  burada get ile kontrol yapar
    previous_count=word_counts.get(word,0) # get(word,0)--> dictonnary içerisinde eleman yoksa 0 ıncı key ile oluşuyor
    word_counts[word]=previous_count +1 

from collections import defaultdict #anahtar yoksa degeri 0 olarak atar ve kontrol etmeye gerekmez
word_counts=defaultdict(int) #int() produces 0
for word in document:
    word_counts[word] +=1

dd_list=defaultdict(list)
dd_list[2].append(1)
dd_dist=defaultdict(dict)
dd_dist["joel"]["city"]="Seatle"

from collections import Counter #problemin en basit yoludur
c=Counter([0,1,2,0])
word_counts=Counter(document)
for word,count in word_counts.most_common(10): #en fazla gecen 10 tane harfi yazar
    print(word,count)
words=document.split() #kelimelere boler
word_conts1=Counter(words)
for word1,count1 in word_conts1.most_common(5):
    print(word1,count1)

