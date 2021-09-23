import os

client_id=os.environ.get('udemy_client_id')
client_secret=os.environ.get('udemy_client_secret')

from pyudemy import Udemy
udemy=Udemy(client_id,client_secret)
courslist=udemy.courses(page=1,page_size=10)
courseID=udemy.course_detail(362328) #kurs ıd si

with open('udemy_courses.csv','w') as f:
    f.write('ID,TİTLE,PRICE,URL\n')
    for k in courselist['results']:
        f.write("%s,%s,%s,%s\n"%(k["id"],k["title"],k["price"][1:],k["url"]))

import csv
with open('udemy_courses.csv','w',newline='') as file:
    writer=csv.writer(file)
    writer.writerow(["ID","TITLE","PRICE","URL"])
    for key in courslist['results']:
        tlist=[key["id"],key["title"],key["price"][1:],key["url"]]
        writer.writerow(tlist)