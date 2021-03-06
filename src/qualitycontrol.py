# -*- coding: utf-8 -*-
"""QualityControlv3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eO4ys2_EySflyi6Nk4PEarlKtFQYCqnI
"""

import numpy as np
import pandas as pd
import glob

results_df = pd.read_csv('final_delete_results.csv')
print(results_df)
results_df.head()

#Convert input to string instead of number
def zero_string(x):
  val = ""
  for i in range(x):
    val = val + "0"
  return val

processed_results = []
sentence_dict = []
row_num = 0
for index, row in results_df.iterrows():
  for j in range(3): 
    if(row["Answer.deletion_mask_" + str(j+1)] != row["Answer.deletion_mask_" + str(j+1)]):
      deletion_mask = 0
    else:
      deletion_mask = int(row["Answer.deletion_mask_" + str(j+1)])
    paragraph = str(row["Input.paragraph_" + str(j+1)])
    article_num = int(row["Input.article"])
    passage_num = int(row["Input.passage"])
    paragraph_num = j + 1
    sentences = paragraph.split("#$")
    paragraph_length = len(sentences)
    processed_mask = zero_string(paragraph_length - len(str(deletion_mask))) + str(deletion_mask)
    
    for k in range(len(sentences)):
      sentence_dict.append (
       {
          'sentence' : sentences[k],
          'sentence_id' : (article_num, ((passage_num - 1) * 3 + paragraph_num) * 100 + k)
       }
      )
    
      processed_results.append (
       {
          'hit' : row_num,
          'sentence_id' : (article_num, ((passage_num - 1) * 3 + paragraph_num) * 100 + k) ,
          'sentence_vote' : int(processed_mask[k])
       }
      )
    row_num += 1

processed_df = pd.DataFrame.from_dict(processed_results)
sentence_df = pd.DataFrame.from_dict(sentence_dict)
sentence_df.to_csv("delete_senetence_dict.csv")

from collections import Counter

counts = Counter()
maxVotes = Counter()

for index, row in processed_df.iterrows():
    is_relevant = row['sentence_vote'] == 1
    sentence_id = row['sentence_id']
    article = int(row['sentence_id'][0])
    if is_relevant == 1:
      counts[sentence_id] += 1
    else:
      counts[sentence_id] += 0
    if counts[sentence_id] >= maxVotes[article]:
      maxVotes[article] = counts[sentence_id]

print(counts)

final_df = pd.DataFrame.from_dict(counts, orient='index')

dict_list = []

for index, row in final_df.iterrows():
  dict_list.append ( 
    {
    'article_id': row.name[0],
    'sentence_order': row.name,
    'votes': row[0],
    'max_votes': maxVotes[row.name[0]],     
    'agreement': row[0] / maxVotes[row.name[0]] * 100      
    }
  )
 
transform_df = pd.DataFrame.from_dict(dict_list)

print(transform_df)

transform_df.to_csv("delete_qc_output.csv")