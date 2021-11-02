#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 09:44:47 2021

@author: carolyndavis
"""
import matplotlib.pyplot as plt
import seaborn as sns

import nltk
import unicodedata
import re
import json
import pandas as pd 
# # Opening JSON file
# f = open('data.json',)
 
# returns JSON object as
# a dictionary
# data = json.load(f)



df = pd.read_csv('data/processed.csv')



#data is cleaned 
df.info()



df.language.value_counts()



df.readme.unique().value_counts()


# import plotly.express as px

# fig = px.histogram(df, x='lang_freq', template='plotly_white', title='readme counts by language')
# fig.update_xaxes(categoryorder='total descending').update_yaxes(title='Number of readme counts')
# fig.show()

read_me_df = df[['readme', 'language']].copy()



#how many language observations do we have?
read_me_df.language.value_counts(normalize = True)



read_me_df['language'].value_counts()
# Go            106
# Python        102
# Java          102
# Swift         100
# C++           100
# JavaScript     97
# C              94



# combine all readmes in single string by language
def clean(language):
    '''Simplified text cleaning function'''
    language = language.lower()
    language = unicodedata.normalize('NFKD', language).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    return re.sub(r"[^a-z0-9\s]", '', language)





go_words = clean(' '.join(read_me_df[read_me_df.language == 'Go'].readme))
python_words = clean(' '.join(read_me_df[read_me_df.language == 'Python'].readme))
java_words = clean(' '.join(read_me_df[read_me_df.language == 'Java'].readme))
cplus_plus_words = clean(' '.join(read_me_df[read_me_df.language == 'C++'].readme))
javascript_words = clean(' '.join(read_me_df[read_me_df.language == 'JavaScript'].readme))
swift_words = clean(' '.join(read_me_df[read_me_df.language == 'Swift'].readme))
c_words = clean(' '.join(read_me_df[read_me_df.language == 'C'].readme))


all_words = clean(' '.join(read_me_df.readme))



# Represent text as word frequencies.

go_freq = pd.Series(go_words.split()).value_counts()
python_freq = pd.Series(python_words.split()).value_counts()
java_freq = pd.Series(java_words.split()).value_counts()
cplus_plus_freq = pd.Series(cplus_plus_words.split()).value_counts()
javascript_freq = pd.Series(javascript_words.split()).value_counts()
swift_freq = pd.Series(swift_words.split()).value_counts()
c_freq = pd.Series(c_words.split()).value_counts()
all_freq = pd.Series(all_words.split()).value_counts()


pd.concat([go_freq, python_freq, java_freq, cplus_plus_freq, javascript_freq, swift_freq, c_freq, all_freq], axis = 1).fillna(0).astype(int)



# concat all frequencies together into a dataframe

word_counts = pd.concat([go_freq, python_freq, java_freq, cplus_plus_freq, javascript_freq, swift_freq, c_freq, all_freq], axis=1).fillna(0).astype(int)
word_counts.columns = ['Go', 'Python', 'Java', 'C++', 'JavaScript', 'Swift', 'C', 'all']
word_counts.head()



# sort by 'all'

word_counts.sort_values('all', ascending=False).head(20)


# word_counts.sort_values(['Go', 'Python', 'Java', 'C++', 'JavaScript', 'Swift', 'C'], ascending=[True, False]).head(20)


plt.rc('font', size=18)
word_counts.sort_values('all', ascending=False).head(20)[['Go', 'Python', 'Java', 'C++', 'JavaScript', 'Swift', 'C']].plot.barh()
plt.title('Count by Language for the top 20 most frequent words')




plt.figure(figsize=(16, 9))
plt.rc('font', size=16)

(word_counts.sort_values('all', ascending=False)
 .head(20)
 .apply(lambda row: row/row['all'], axis = 1)
 .drop(columns = 'all')
 .sort_values(by = 'Go')
 .plot.barh(stacked = True, width = 1, ec = 'k')
)
plt.title('% of Go vs all for the most common 20 words')
