"""Sets(kumeler)"""
primess_below_10={2,3,5,7}
s=set() #boş kume tanımı
s.add(1) #s={1}
s.add(2) #s={1,2}
s.add(2)# s is still {1,2}
x=len(s)  #uzunluk 2
other_words=["the","on","in","if","else","is","are"]
stopwords_list=["a","an","at"] + other_words +["yet","you"]
"zip" in stopwords_list #false,but have to check every element
stopwords_set=set(stopwords_list)
"zip" in stopwords_set #very fast to check

item_list=[1,2,3,1,2,3]
num_items=len(item_list) #6
item_set=set(item_list)  #{1,2,3} kume
num_distinct_items=len(item_set) #3
distinct_item_list=list(item_set)  #[1,2,3] liste