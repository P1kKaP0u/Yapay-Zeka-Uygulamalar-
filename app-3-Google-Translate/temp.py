# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 19:25:36 2022

@author: Mustafa-Kemal-Aktas
@mail: mustafaktaskemal@gmail.com

"""

import googletrans
from googletrans import Translator
import pandas as pd



#Kaç dil arasında çalışabileceğini gösterir.
#print(len(googletrans.LANGUAGES))

#Dil kısaltmaları ve isimlerini verir.
#print(googletrans.LANGUAGES)

#Önce dil sonra kısaltma ismini verir.
#print(googletrans.LANGCODES)


translator=Translator()
text="Merhaba, ben yazılımcı Mustafa Kemal."
example=translator.translate(text, dest="de")


#Nesne tipini verir.
print(type(example))

#Kaynak cümle dilini verir.
print(example.src)

#Hedef cümle dilini verir.
print(example.dest)

#Orijinal cümleyi verir.
print(example.origin)

#Çevirilmiş cümleyi verir.
print(example.text)


print("*************************")


word_tr=["elma","armut","kalem","kulaklık","araba","bilgisayar","fare","çay"]


df=pd.DataFrame(columns=["Türkçe","İngilizce","Fransızca","Rusça"])

#print(df)
for word in word_tr:
    df=df.append({
        "Türkçe": word,
        "İngilizce": translator.translate(word, dest="en").text,
        "Fransızca": translator.translate(word, dest="fr").text,
        "Rusça": translator.translate(word, dest="ru").text,
        },ignore_index=True)



print(df)
print("*************************")


print(df.head(2))
print("*************************")

print(df.iloc[0])
print("*************************")

print(df[{"Türkçe","İngilizce"}].values[1])





