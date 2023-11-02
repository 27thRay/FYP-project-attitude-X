from pdfminer.high_level import extract_text
#Provide the Resume file path as an argument
file_path = "sample_data/Resume_1.pdf"  
text = extract_text(file_path)

#using spacy stopwords
import spacy
#loading the english language small model of spacy
en = spacy.load('en_core_web_sm')
stopwords = en.Defaults.stop_words

lst=[]
for token in text.split():
    if token.lower() not in stopwords:    #checking whether the word is not 
        lst.append(token)                    #present in the stopword list.
        
#Join items in the list
#print("Original text  : ",text)
print("Text after removing stopwords  :   ",' '.join(lst))



# #using nltk stopwords
# ##Import Libraries
# import re

# ##NLTK Stopwords
# import nltk
# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize
# # Fetch the stopwords list from NLTK
# stop_words = stopwords.words('english')
# # Additional stop words to add
# extra_stop_words = [':', ',', '.', '!', '?', '&', "’",'this', 'also']

# # Convert the NLTK WordListCorpusReader to a list
# stop_words_list = list(stop_words)
# # Now 'stop_words_list' is a regular Python list containing NLTK's stopwords
# # Add extra_stop_words to stop_words_list
# stop_words_list.extend(extra_stop_words)

# # Regular expressions for numbers, dates, and months
# number_pattern = re.compile(r'\b\d+\b')  # Matches numbers
# date_pattern = re.compile(r'\b\d{1,2}/\d{1,2}/\d{2,4}\b')  # Matches dates like 01/01/2023
# months = [
#     "january", "february", "march", "april", "may", "june", "july",
#     "august", "september", "october", "november", "december"
# ]

# def filter_function(text):
#     word_tokens = word_tokenize(text)
#     # converts the words in word_tokens to lower case and then checks whether 
#     #they are present in stop_words or not
#     filtered_sentence = [w for w in word_tokens if w.lower() not in stop_words_list
#                          and not number_pattern.match(w.lower())
#                          and not date_pattern.match(w.lower())
#                          and w.lower() not in months
#                          and len(w.lower())>1]
    
#     unique_words = set(filtered_sentence)
#     unique_filtered_words = list(unique_words)
            
#     print('BEFORE FILTERING:')
#     print(word_tokens)
#     print('THIS IS FILTERED SENTECNE:')
#     print(unique_filtered_words)
            
#     return filtered_sentence

# filter_function(text)