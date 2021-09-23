def get_domain(email_address:str)->str:
    """Split on @ and return the last place"""
    return email_address.lower().split("@")[-1]

from collections import Counter,defaultdict

domain_counts=defaultdict(int)
with open("email.txt") as f: #dosya açar f e attar
    for line in f: #look at each line in the file
        if "@" in line:
            domain_counts[get_domain(line)]+=1

"""with open("email.txt") as f: #dosya açar f e attar
    domain_counts=Counter(get_domsin(line)
                          for line in f
                          if "@" in line)""" #yukarıdaki ile aynı farkı Counter kullandık

import matplotlib.pylot as plt  #grafik oluşturmak için
plt.bar(domain_counts.keys(),domain_counts.values())
plt.show()