import docx
import pandas as pd


document = docx.Document('Sample3.docx')
df = pd.DataFrame(columns = ['title', 'paragraph'])


def fetch_title_subtitle():

	docText = []
	title_and_sub_title = {}
	title = []
	subtitle = []

	for paragraph in document.paragraphs:

	    if paragraph.text:
	    			
	    	docText.append(paragraph.text)
	print(len(docText))


	for para in docText:
		if para.isupper():
			title.append(para)

	for i in range(len(title) - 1):
		first = docText.index(title[i])
		last = docText.index(title[i+1])
		val = ""
		for j in range(first+1, last):
			# print(j)
			val += docText[j]
		subtitle.append(val)
		val =""

	end = docText.index(title[i])
	for j in range(end + 1, len(docText)):
		val += docText[j]
	subtitle.append(val)

	assert len(subtitle) == len(title)


	for i in range(len(title)):
		title_and_sub_title[title[i]] = subtitle[i]
	return title_and_sub_title

val = fetch_title_subtitle()

for key, value in val.items():
	df = df.append({'title' : key, 'paragraph' : value}, ignore_index = True)
df.to_csv("title_and_sub_title.csv")












