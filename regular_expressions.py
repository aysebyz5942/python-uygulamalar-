""" REGEX--> arama deseni oluşturan karakter dizisidir
ve bir dizenin bu deseni içerip içermediğini kontrol etmek
için kullanılır"""

import re
re_examples=[#All of this are true, because
    not re.match("a","cat"), #cat doesn't start with 'a'
    re.search("a","cat"),    #vat has an 'a' in it
    re.search("^it.*dogs$","it is raining cats and dogs"), #^:ile başlar|
                                                     #.*:sifir veya daha fazla karakter ile devam eder
                                                     #$:dogs ile biten ifade
    ["hello"]==re.findall("he..o","hello world"), # iki nokta yani iki karakter var
    3== len(re.split("[ab]","carbs")),   #Split in a or b to ['c','r','s']
    "R-D-"==re.sub("[0-9]","-","R2D2")#replace digits with dashes(-)
    ]
assert all(re_examples),"all the regex examples should be true"