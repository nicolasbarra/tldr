# -*- coding: utf-8 -*-
"""section_maker.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Lbq9GPYtj5ctQL1c-gCDB3mhtNsISHms
"""

import nltk
from nltk import sent_tokenize
nltk.download('punkt')
from google.colab import files

chunks = ['HTB00','HTB01','HTB02','HTB03','HTB04','HTB05','HTB06','HTB07','HTB08','HTB09','HTB10','HTB11','HTB12']

def process(chunk):
  section = ""
  count = 0
  pref = '<span style="color:Blue;"><b>'
  suf = '</b></span>.'
  nums = ['①','②','③','④','⑤','⑥','⑦','⑧','⑨','⑩','⑪','⑫','⑬','⑭','⑮','⑯','⑰','⑱','⑲','⑳']
  with open(chunk + '.txt','r') as f:
    for line in f:
      sentences = sent_tokenize(line)
      for s in sentences:
        s = s[:-1]
        if count < 20:
          data = s + pref + nums[count] + suf
        else:
          cnt = str(count)
          data = s + " " + pref + nums[int(cnt[0])-1] + nums[int(cnt[1])] + suf
        count += 1
        section = section + data + " "

  tagged = open(chunk + "Tagged.txt","w")
  tagged.write(section)

  
for chunk in chunks:
  process(chunk)
  print ('done')