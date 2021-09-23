"""RANDOM"""
import random
random.seed(10) #this ensures we get the same results every time
#seed(x) --> rastgele sayılar üretirken kullanılacak başlangıç noktasını belirler
four_uniform_randoms=[random() for _ in range(4)]
#[0.5714025946899135, #random.random() produces numbers
# 0.4288890546751146, #uniformly between 0 and 1
# 0.5780913011344704, #ıt's the random function we will use
# 0.20609823213950174]# most often

random.seed(10) #set thhe seed to 10
print(random.random())# 0.57140259469
random.seed(10) #reset the seed to 10
print(random.random()) #0.57140259469
 #random() seed kaynagını kullanarak 0 ile 1 arası  sayi veri

 random.randrange(10) #choose randomly 1 den 10 a kadar seçer
 random.randrange(3,6) #3,4,6

 up_to_ten=[1,2,3,4,5,6,7,8,9,10]
 random.shuffle(up_to_ten) #listeyi karıştırır
print(up_to_ten) #[7,2,6,8,9,4,10,1,3,5] gibi değişebilir

my_best_friend=random.choice(["alice","bob","Charlie"]) #listeden rastgele bir tanesi seç

lottery_numbers=range(60)
winning_numbers=numbers.sample(lottery_numbers,6)# lootery deki 6 tane random sayı al

four_with_replacment=[random.choice(range(10)) for _ in range(4)]
print(four_with_replacment) #[9,4,4,2]

#choice aynı sayıyıtekrar getirebilir fakat sample farklı getirir!!!!!










