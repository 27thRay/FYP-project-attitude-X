from pdfminer.high_level import extract_text
#Provide the Resume file path as an argument
file_path = "resume_data/Resume_2.pdf"  
text = extract_text(file_path)

# import re
# matchlist = ["Master's","Bachelor's","M.Sc","B.Sc","University"]
# p = re.compile('^(.*?),\s+(.*?),(.*?)\.')
# edumatch = [m.group(1) if any(x in m.group(1) for x in matchlist) else m.group(2) for m in re.finditer(p,text)]
# print(edumatch)



# import re
# from nltk.corpus import stopwords

# # load pre-trained model
# nlp = spacy.load('en_core_web_trf')

# # Grad all general stop words
# stopwords = set(stopwords.words('english'))

# # Education Degrees
# education = [
#             'BE','B.E.', 'B.E', 'BS', 'B.S','C.A.','c.a.','B.Com','B. Com','M. Com', 'M.Com','M. Com .',
#             'ME', 'M.E', 'M.E.', 'MS', 'M.S','M.Sc','B.Sc','MSc','BSc'
#             'BTECH', 'B.TECH', 'M.TECH', 'MTECH',
#             'PHD', 'phd', 'ph.d', 'Ph.D.','MBA','mba','graduate', 'post-graduate','5 year integrated masters','masters',
#             'SSC', 'HSC', 'CBSE', 'ICSE', 'X', 'XII', 'University'
#         ]

# def extract_education(resume_text):
#     nlp_text = nlp(resume_text)
#     # Sentence Tokenizer
#     nlp_text = [sent.text.strip() for sent in nlp_text.sents]
#     edu = {}
#     # Extract education degree
#     for index, text in enumerate(nlp_text):
#         #print(index, text), print('-'*50)
#         for tex in text.split():
#             # Replace all special symbols
#             tex = re.sub(r'[?|$|.|!|,]', r'', tex)
#             print(tex)
#             if tex.upper() in education and tex not in stopwords:
#                 edu[tex] = text + nlp_text[index + 1]
#                 print(edu.keys())
#                 return list(edu.keys())

# print(extract_education(text)) #resume parsed into text



# import re
# # Education Degrees
# EDUCATION = [
#             'BE','B.E.', 'B.E', 'BS', 'B.S','C.A.','c.a.','B.Com','B. Com','M. Com', 'M.Com','M. Com .',
#             'ME', 'M.E', 'M.E.', 'MS', 'M.S','M.Sc','B.Sc','MSc','BSc'
#             'BTECH', 'B.TECH', 'M.TECH', 'MTECH',
#             'PHD', 'phd', 'ph.d', 'Ph.D.','MBA','mba','graduate', 'post-graduate','5 year integrated masters','masters',
#             'SSC', 'HSC', 'CBSE', 'ICSE', 'X', 'XII', 'University'
#         ]

# def extract_education(resume_text):
#   # regex = re.compile(r"(B\.Tech|MSc).*?(?<=-)\s+(\d+)")
#   # match = regex.match(resume_text)
#   list123 = []
#   for i in EDUCATION:
#     reg = "(" + re.escape(i) + ").*?(?<=-)\s+(\d+)"
#     regex = re.compile(reg, flags=re.M | re.IGNORECASE)
#     for mat in regex.findall(resume_text):
#       list123.append(mat)
#   return list123 

# print(extract_education(text))



# import re
# import spacy
# from nltk.corpus import stopwords

# # load pre-trained model
# nlp = spacy.load('en_core_web_sm')

# # Grad all general stop words
# STOPWORDS = set(stopwords.words('english'))

# # Education Degrees
# EDUCATION = [
#             'BE','B.E.', 'B.E', 'BS', 'B.S','C.A.','c.a.','B.Com','B. Com','M. Com', 'M.Com','M. Com .',
#             'ME', 'M.E', 'M.E.', 'MS', 'M.S','M.Sc','B.Sc','MSc','BSc'
#             'BTECH', 'B.TECH', 'M.TECH', 'MTECH',
#             'PHD', 'phd', 'ph.d', 'Ph.D.','MBA','mba','graduate', 'post-graduate','5 year integrated masters','masters',
#             'SSC', 'HSC', 'CBSE', 'ICSE', 'X', 'XII', 'University'
#         ]

# def extract_education(resume_text):
#     nlp_text = nlp(resume_text)

#     # Sentence Tokenizer
#     nlp_text = [sent.text.strip() for sent in nlp_text.sents]

#     edu = {}
#     # Extract education degree
#     for index, text in enumerate(nlp_text):
#         for tex in text.split():
#             # Replace all special symbols
#             tex = re.sub(r'[?|$|.|!|,]', r'', tex)
#             if tex.upper() in EDUCATION and tex not in STOPWORDS:
#                 edu[tex] = text + nlp_text[index + 1]

#     education = []
#     for key in edu.keys():
#         year = re.search(re.compile(r'(((20|19)(\d{2})))'), edu[key])
#         if year:
#             education.append((key, ''.join(year[0])))
#         else:
#             education.append(key)
#     return education

# education = extract_education(text)
# print(education)



# import re
# sub_patterns = ['[A-Z][a-z]* University','[A-Z][a-z]* Educational Institute',
#                 'University of [A-Z][a-z]*',
#                 'Master\'s degree in [A-z][a-z]*',
#                 'Bachelor\'s degree in [A-z][a-z]*',
#                 'Ecole [A-Z][a-z]*']
# pattern = '({})'.format('|'.join(sub_patterns))
# matches = re.findall(pattern, text)
# print(matches)


# # flair 
# from flair.data import Sentence
# from flair.models import SequenceTagger

# # load tagger
# tagger = SequenceTagger.load("flair/ner-english")

# # make example sentence
# sentence = Sentence(text)

# # predict NER tags
# tagger.predict(sentence)

# # print sentence
# print(sentence)

# # print predicted NER spans
# print('The following NER tags are found:')
# # iterate over entities and print
# for entity in sentence.get_spans('ner'):
#     print(entity)



# from nltk.tokenize import word_tokenize
# from spacy.lang.en.stop_words import STOP_WORDS
# #extract skills from job_description
# filteredtext = []
# word_tokens = word_tokenize(text)
# for word in word_tokens:
#     if word not in STOP_WORDS:
#         filteredtext += word
# print(filteredtext)


from pyresparser import ResumeParser
data = ResumeParser('/path/to/resume/file').get_extracted_data()