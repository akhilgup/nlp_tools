import pandas as pd
from gensim.summarization.summarizer import summarize



df = pd.read_csv("title_and_sub_title.csv")

paragraphs = df.paragraph.values.tolist()
title = df.title.values.tolist()

for i in range(len(title)):
	print('----------------------------------')
	print(title[i])
	try:
		print(summarize(paragraphs[i]))
	except Exception as e:
		print(str(e))






