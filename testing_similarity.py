from pdfminer.high_level import extract_text
#Provide the Resume file path as an argument
file_path = "resume_data/Resume_1.pdf"  
text = extract_text(file_path)

#using spacy stopwords
import spacy
#loading the english language small model of spacy
en = spacy.load('en_core_web_trf')
stopwords = en.Defaults.stop_words

lst=[]
for token in text.split():
    if token.lower() not in stopwords:    #checking whether the word is not 
        lst.append(token)                    #present in the stopword list.
        
#Join items in the list
#print("Original text  : ",text)
#print("Text after removing stopwords  :   ",' '.join(lst))



# import math

# comparisions = {'resume5': {'Technical Skills': ['Investment Management', 'Analytical Accounting', 'Fixed Income', 'Capital Market', 'Futures and Options']},
#                 'job desc':{'Technical Skills':['Proven track record in business development and sales','Strong understanding of the Swiss market and ideally the learning and development landscape',
#                             'Good knowledge of technology and social networking tools']}}

# def cosine_similarity(vec1,vec2):
#         sum11, sum12, sum22 = 0, 0, 0
#         for i in range(len(vec1)):
#             x = vec1[i]; y = vec2[i]
#             sum11 += x*x
#             sum22 += y*y
#             sum12 += x*y
#         return sum12/math.sqrt(sum11*sum22)

# list1 = list(comparisions['resume5'].values())
# list2 =  list(comparisions['job desc'].values())

# sim = cosine_similarity(list1,list2)
# print(sim)



# # Program to measure the similarity between  
# # two sentences using cosine similarity. 
# from nltk.corpus import stopwords 
# from nltk.tokenize import word_tokenize 
  
# # X = input("Enter first string: ").lower() 
# # Y = input("Enter second string: ").lower() 
# X = 'Investment Management', 'Analytical Accounting', 'Fixed Income', 'Capital Market', 'Futures and Options'
# Y = 'Proven track record in business development and sales','Strong understanding of the Swiss market and ideally the learning and development landscape', 'Good knowledge of technology and social networking tools'
# # tokenization 
# X_list = word_tokenize(X)  
# Y_list = word_tokenize(Y) 
  
# # sw contains the list of stopwords 
# sw = stopwords.words('english')  
# l1 =[];l2 =[] 
  
# # remove stop words from the string 
# X_set = {w for w in X_list if not w in sw}  
# Y_set = {w for w in Y_list if not w in sw} 
  
# # form a set containing keywords of both strings  
# rvector = X_set.union(Y_set)  
# for w in rvector: 
#     if w in X_set: l1.append(1) # create a vector 
#     else: l1.append(0) 
#     if w in Y_set: l2.append(1) 
#     else: l2.append(0) 
# c = 0
  
# # cosine formula  
# for i in range(len(rvector)): 
#         c+= l1[i]*l2[i] 
# cosine = c / float((sum(l1)*sum(l2))**0.5) 
# print("similarity: ", cosine) 



# from collections import Counter

# # word-lists to compare
# #resume 1
# #a = ['Customer relationship management', 'Facilitation of customer UX journeys', 'Market and product segmentation', 'Strategic forecasting', 'Project management', 'Storytelling and sales pitches', 'Digital transformation', 'Risk- and portfolio management', 'M&A', 'Strategic business expansion', 'Statistical modelling', 'Thought leadership','People and communication skills', 'Leadership and can-do attitude', 'Time management', 'Collaboration', 'Creativity', 'Problem-solving', 'Adaptability', 'Resilience','English (full proficiency)', 'German (upper intermediate)', 'French (upper intermediate)', 'Spanish (upper intermediate)', 'Dutch (native)']
# #resume 2
# #a =  ['Salesforce', 'Canvas', 'RMS', 'WordPress Elementor', 'Bridge-builder','Leadership', 'Coaching', 'Mental & physical health', 'Public speaking & Copywriting', 'Digital Marketing', 'Cross-cultural competency', 'Sport & Wellness Coaching', 'Leadership Development', 'Fitness & Martial Arts', 'ThaÃ¯ Boxing (ex-fighter)','French (mother tongue)', 'English (C1)', 'Spanish (C1)', 'ThaÃ¯ (B1)']
# #resume 3
# #a = ['PC literacy: Microsoft Office (MS Word', 'MS Excel', 'MS PowerPoint', 'MS Outlook', 'Power BI)', 'Adobe Acrobat Reader', '1C', 'SAP', 'Zendesk', 'Pandadoc', 'Bitrix', 'Languages: Fluent in English', 'German', 'Ukrainian', 'Russian; conversational French', 'Spanish','Details-oriented international sales professional', 'Strong organizational and time management skills', 'Experienced in change management and solving problems', 'Passionate and enthusiastic', 'Good team player with excellent communication skills', 'Able to work in a diverse', 'multicultural environment with a strong appetite to learn and deliver the best results','Strong focus on the positive client experience', 'Sales increase', 'Solution-oriented', 'High attention to details', 'Forming and implementation of sales plans', 'Market research and strategy formation', 'Negotiation with partners and potential clients', 'Management of expanding marketing representation', "Participation in the development of the company's"]
# #resume 4
# a = ['IoT security services and solutions', 'AR/MR collaboration and productivity tool for enterprise', 'Digital Media Broadcast technology', 'Customer Relationship Management', 'Project Management IoT Security','Consulting & Sales Team Management', 'Communication Skills Sales Force', 'Customer Relationship Management', 'Project Management IoT Security', 'Negotiating affiliations agreements', 'Supervising and directing sales agents worldwide', 'Introduced and implemented new business development strategy and products', 'Performed and arranged successful product demonstrations for customers', 'Building closer relationships', 'Motivating and conducting teams and projects across our platform', 'Successfully achieved joined target of Â£8.5m a year in a team of 2','French (Native or Bilingual Proficiency)', 'English (Native or Bilingual Proficiency)', 'Portuguese (Full Professional Proficiency)', 'Spanish (Limited Working Proficiency)', 'German (Elementary Proficiency)']
# #resume 5
# #a = ['Investment Management', 'Analytical Accounting', 'Fixed Income', 'Capital Market', 'Futures and Options','Excellent Customer Service Skills', 'Friendly and Outgoing Attitude', 'Initiative and Problem-solving Abilities', 'Strong Communication Skills', 'Excellent Presentation Skills', 'Ability to Work in a Team and Independently','Sales', 'Marketing', 'Business Development', 'Relationship Building', 'Negotiation', 'Lead Generation', 'Customer Satisfaction','Chinese', 'English', 'French']

# b = ['Proven track record in business development and sales', 'Strong understanding of the Swiss market and ideally the learning and development landscape', 'Excellent communication and interpersonal skills', 'Results-oriented mindset with a drive to meet and exceed sales targets', 'Excellent time management skills and ability to prioritize efficiently', 'Fluency in English and French or/and German', 'Good knowledge of technology and social networking tools','Strong sales acumen', 'Excellent relationship-building skills', 'Ability to understand needs', 'challenges', 'and business objectives', 'Strong negotiation and closing skills', 'Ability to collaborate with internal teams', 'Provide feedback from the market to help shape the product roadmap', 'Team player who can also demonstrate the self-drive to work independently']

# # count word occurrences
# a_vals = Counter(a)
# b_vals = Counter(b)

# # convert to word-vectors
# words  = list(a_vals.keys() | b_vals.keys())
# a_vect = [a_vals.get(word, 0) for word in words]        # [0, 0, 1, 1, 2, 1]
# b_vect = [b_vals.get(word, 0) for word in words]        # [1, 1, 1, 0, 1, 0]

# # find cosine
# len_a  = sum(av*av for av in a_vect) ** 0.5             # sqrt(7)
# len_b  = sum(bv*bv for bv in b_vect) ** 0.5             # sqrt(4)
# dot    = sum(av*bv for av,bv in zip(a_vect, b_vect))    # 3
# cosine = dot / (len_a * len_b)                          # 0.5669467
# print(cosine)



# # word-lists to compare
# #resume 1
# #a = ['Customer relationship management', 'Facilitation of customer UX journeys', 'Market and product segmentation', 'Strategic forecasting', 'Project management', 'Storytelling and sales pitches', 'Digital transformation', 'Risk- and portfolio management', 'M&A', 'Strategic business expansion', 'Statistical modelling', 'Thought leadership','People and communication skills', 'Leadership and can-do attitude', 'Time management', 'Collaboration', 'Creativity', 'Problem-solving', 'Adaptability', 'Resilience','English (full proficiency)', 'German (upper intermediate)', 'French (upper intermediate)', 'Spanish (upper intermediate)', 'Dutch (native)']
# #resume 2
# #a =  ['Salesforce', 'Canvas', 'RMS', 'WordPress Elementor', 'Bridge-builder','Leadership', 'Coaching', 'Mental & physical health', 'Public speaking & Copywriting', 'Digital Marketing', 'Cross-cultural competency', 'Sport & Wellness Coaching', 'Leadership Development', 'Fitness & Martial Arts', 'ThaÃ¯ Boxing (ex-fighter)','French (mother tongue)', 'English (C1)', 'Spanish (C1)', 'ThaÃ¯ (B1)']
# #resume 3
# #a = ['PC literacy: Microsoft Office (MS Word', 'MS Excel', 'MS PowerPoint', 'MS Outlook', 'Power BI)', 'Adobe Acrobat Reader', '1C', 'SAP', 'Zendesk', 'Pandadoc', 'Bitrix', 'Languages: Fluent in English', 'German', 'Ukrainian', 'Russian; conversational French', 'Spanish','Details-oriented international sales professional', 'Strong organizational and time management skills', 'Experienced in change management and solving problems', 'Passionate and enthusiastic', 'Good team player with excellent communication skills', 'Able to work in a diverse', 'multicultural environment with a strong appetite to learn and deliver the best results','Strong focus on the positive client experience', 'Sales increase', 'Solution-oriented', 'High attention to details', 'Forming and implementation of sales plans', 'Market research and strategy formation', 'Negotiation with partners and potential clients', 'Management of expanding marketing representation', "Participation in the development of the company's"]
# #resume 4
# a = ['IoT security services and solutions', 'AR/MR collaboration and productivity tool for enterprise', 'Digital Media Broadcast technology', 'Customer Relationship Management', 'Project Management IoT Security','Consulting & Sales Team Management', 'Communication Skills Sales Force', 'Customer Relationship Management', 'Project Management IoT Security', 'Negotiating affiliations agreements', 'Supervising and directing sales agents worldwide', 'Introduced and implemented new business development strategy and products', 'Performed and arranged successful product demonstrations for customers', 'Building closer relationships', 'Motivating and conducting teams and projects across our platform', 'Successfully achieved joined target of Â£8.5m a year in a team of 2','French (Native or Bilingual Proficiency)', 'English (Native or Bilingual Proficiency)', 'Portuguese (Full Professional Proficiency)', 'Spanish (Limited Working Proficiency)', 'German (Elementary Proficiency)']
# #resume 5
# #a = ['Investment Management', 'Analytical Accounting', 'Fixed Income', 'Capital Market', 'Futures and Options','Excellent Customer Service Skills', 'Friendly and Outgoing Attitude', 'Initiative and Problem-solving Abilities', 'Strong Communication Skills', 'Excellent Presentation Skills', 'Ability to Work in a Team and Independently','Sales', 'Marketing', 'Business Development', 'Relationship Building', 'Negotiation', 'Lead Generation', 'Customer Satisfaction','Chinese', 'English', 'French']

# b = ['Proven track record in business development and sales', 'Strong understanding of the Swiss market and ideally the learning and development landscape', 'Excellent communication and interpersonal skills', 'Results-oriented mindset with a drive to meet and exceed sales targets', 'Excellent time management skills and ability to prioritize efficiently', 'Fluency in English and French or/and German', 'Good knowledge of technology and social networking tools','Strong sales acumen', 'Excellent relationship-building skills', 'Ability to understand needs', 'challenges', 'and business objectives', 'Strong negotiation and closing skills', 'Ability to collaborate with internal teams', 'Provide feedback from the market to help shape the product roadmap', 'Team player who can also demonstrate the self-drive to work independently']

# import difflib

# seq = difflib.SequenceMatcher(None,a,b)
# d = seq.ratio()*100
# print(d) 



# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity

# sample documents
#Resume 1
# doc1 = 'Customer relationship management, Facilitation of customer UX journeys, Market and product segmentation, Strategic forecasting, Project management, Storytelling and sales pitches, Digital transformation, Risk- and portfolio management, M&A, Strategic business expansion, Statistical modelling, Thought leadership,People and communication skills, Leadership and can-do attitude, Time management, Collaboration, Creativity, Problem-solving, Adaptability, Resilience,English (full proficiency), German (upper intermediate), French (upper intermediate), Spanish (upper intermediate), Dutch (native)'
# doc2 = 'Proven track record in business development and sales, Strong understanding of the Swiss market and ideally the learning and development landscape, Excellent communication and interpersonal skills, Results-oriented mindset with a drive to meet and exceed sales targets, Excellent time management skills and ability to prioritize efficiently, Fluency in English and French or/and German, Good knowledge of technology and social networking tools,Strong sales acumen, Excellent relationship-building skills, Ability to understand needs, challenges, and business objectives, Strong negotiation and closing skills, Ability to collaborate with internal teams, Provide feedback from the market to help shape the product roadmap, Team player who can also demonstrate the self-drive to work independently'
#Resume 2
# doc1 = 'Salesforce, Canvas, RMS, WordPress Elementor, Bridge-builder,Leadership, Coaching, Mental & physical health, Public speaking & Copywriting, Digital Marketing, Cross-cultural competency, Sport & Wellness Coaching, Leadership Development, Fitness & Martial Arts, ThaÃ¯ Boxing (ex-fighter),French (mother tongue), English (C1), Spanish (C1), ThaÃ¯ (B1)'
# doc2 = 'Proven track record in business development and sales, Strong understanding of the Swiss market and ideally the learning and development landscape, Excellent communication and interpersonal skills, Results-oriented mindset with a drive to meet and exceed sales targets, Excellent time management skills and ability to prioritize efficiently, Fluency in English and French or/and German, Good knowledge of technology and social networking tools,Strong sales acumen, Excellent relationship-building skills, Ability to understand needs, challenges, and business objectives, Strong negotiation and closing skills, Ability to collaborate with internal teams, Provide feedback from the market to help shape the product roadmap, Team player who can also demonstrate the self-drive to work independently'
#Resume 3
# doc1 = "PC literacy: Microsoft Office (MS Word, MS Excel, MS PowerPoint, MS Outlook, Power BI), Adobe Acrobat Reader, 1C, SAP, Zendesk, Pandadoc, Bitrix, Languages: Fluent in English, German, Ukrainian, Russian; conversational French, Spanish,Details-oriented international sales professional, Strong organizational and time management skills, Experienced in change management and solving problems, Passionate and enthusiastic, Good team player with excellent communication skills, Able to work in a diverse, multicultural environment with a strong appetite to learn and deliver the best results,Strong focus on the positive client experience, Sales increase, Solution-oriented, High attention to details, Forming and implementation of sales plans, Market research and strategy formation, Negotiation with partners and potential clients, Management of expanding marketing representation, Participation in the development of the company's"
# doc2 = 'Proven track record in business development and sales, Strong understanding of the Swiss market and ideally the learning and development landscape, Excellent communication and interpersonal skills, Results-oriented mindset with a drive to meet and exceed sales targets, Excellent time management skills and ability to prioritize efficiently, Fluency in English and French or/and German, Good knowledge of technology and social networking tools,Strong sales acumen, Excellent relationship-building skills, Ability to understand needs, challenges, and business objectives, Strong negotiation and closing skills, Ability to collaborate with internal teams, Provide feedback from the market to help shape the product roadmap, Team player who can also demonstrate the self-drive to work independently'
#Resume 4
# doc1 = 'IoT security services and solutions, AR/MR collaboration and productivity tool for enterprise, Digital Media Broadcast technology, Customer Relationship Management, Project Management IoT Security,Consulting & Sales Team Management, Communication Skills Sales Force, Customer Relationship Management, Project Management IoT Security, Negotiating affiliations agreements, Supervising and directing sales agents worldwide, Introduced and implemented new business development strategy and products, Performed and arranged successful product demonstrations for customers, Building closer relationships, Motivating and conducting teams and projects across our platform, Successfully achieved joined target of Â£8.5m a year in a team of 2,French (Native or Bilingual Proficiency), English (Native or Bilingual Proficiency), Portuguese (Full Professional Proficiency), Spanish (Limited Working Proficiency), German (Elementary Proficiency)'
# doc2 = 'Proven track record in business development and sales, Strong understanding of the Swiss market and ideally the learning and development landscape, Excellent communication and interpersonal skills, Results-oriented mindset with a drive to meet and exceed sales targets, Excellent time management skills and ability to prioritize efficiently, Fluency in English and French or/and German, Good knowledge of technology and social networking tools,Strong sales acumen, Excellent relationship-building skills, Ability to understand needs, challenges, and business objectives, Strong negotiation and closing skills, Ability to collaborate with internal teams, Provide feedback from the market to help shape the product roadmap, Team player who can also demonstrate the self-drive to work independently'
#Resume 5
# doc1 = 'Investment Management, Analytical Accounting, Fixed Income, Capital Market, Futures and Options,Excellent Customer Service Skills, Friendly and Outgoing Attitude, Initiative and Problem-solving Abilities, Strong Communication Skills, Excellent Presentation Skills, Ability to Work in a Team and Independently,Sales, Marketing, Business Development, Relationship Building, Negotiation, Lead Generation, Customer Satisfaction,Chinese, English, French'
# doc2 = 'Proven track record in business development and sales, Strong understanding of the Swiss market and ideally the learning and development landscape, Excellent communication and interpersonal skills, Results-oriented mindset with a drive to meet and exceed sales targets, Excellent time management skills and ability to prioritize efficiently, Fluency in English and French or/and German, Good knowledge of technology and social networking tools,Strong sales acumen, Excellent relationship-building skills, Ability to understand needs, challenges, and business objectives, Strong negotiation and closing skills, Ability to collaborate with internal teams, Provide feedback from the market to help shape the product roadmap, Team player who can also demonstrate the self-drive to work independently'
# doc1 = 'Investment Management, Analytical Accounting, Fixed Income, Capital Market, Futures and Options'
# doc2 = 'Proven track record in business development and sales, Strong understanding of the Swiss market and ideally the learning and development landscape, Excellent communication and interpersonal skills, Results-oriented mindset with a drive to meet and exceed sales targets, Excellent time management skills and ability to prioritize efficiently, Good knowledge of technology and social networking tools'

# doc1 = 'animal'
# doc2 = 'dog'

# # create TF-IDF vectorizer
# tfidf_vectorizer = TfidfVectorizer()

# # fit and transform the documents
# tfidf_matrix = tfidf_vectorizer.fit_transform([doc1, doc2])

# # compute cosine similarity between doc1 and doc2
# cosine_sim = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])[0][0]
# print("Cosine similarity between doc1 and doc2:", cosine_sim)



# import gensim
# from gensim.models.doc2vec import Doc2Vec, TaggedDocument
# from nltk.tokenize import word_tokenize
# from gensim.models.doc2vec import Doc2Vec

# data = ['Proven track record in business development and sales, Strong understanding of the Swiss market and ideally the learning\
#          and development landscape, Excellent communication and interpersonal skills, Results-oriented mindset with a drive to meet\
#          and exceed sales targets, Excellent time management skills and ability to prioritize efficiently, Fluency in English and\
#          French or/and German, Good knowledge of technology and social networking tools,Strong sales acumen, Excellent \
#          relationship-building skills, Ability to understand needs, challenges, and business objectives, Strong negotiation and closing\
#          skills, Ability to collaborate with internal teams, Provide feedback from the market to help shape the product roadmap, \
#          Team player who can also demonstrate the self-drive to work independently',
#         'Customer relationship management, Facilitation of customer UX journeys, Market and product segmentation, Strategic forecasting,\
#           Project management, Storytelling and sales pitches, Digital transformation, Risk- and portfolio management, M&A, Strategic\
#           business expansion, Statistical modelling, Thought leadership,People and communication skills, Leadership and can-do\
#           attitude, Time management, Collaboration, Creativity, Problem-solving, Adaptability, Resilience,English (full proficiency),\
#           German (upper intermediate), French (upper intermediate), Spanish (upper intermediate), Dutch (native)',
#         'Salesforce, Canvas, RMS, WordPress Elementor, Bridge-builder,Leadership, Coaching, Mental & physical health, Public speaking &\
#           Copywriting, Digital Marketing, Cross-cultural competency, Sport & Wellness Coaching, Leadership Development, Fitness &\
#           Martial Arts, ThaÃ¯ Boxing (ex-fighter),French (mother tongue), English (C1), Spanish (C1), ThaÃ¯ (B1)',
#         "PC literacy: Microsoft Office (MS Word, MS Excel, MS PowerPoint, MS Outlook, Power BI), Adobe Acrobat Reader, 1C, SAP, Zendesk,\
#           Pandadoc, Bitrix, Languages: Fluent in English, German, Ukrainian, Russian; conversational French, Spanish,Details-oriented\
#           international sales professional, Strong organizational and time management skills, Experienced in change management and\
#           solving problems, Passionate and enthusiastic, Good team player with excellent communication skills, Able to work in a\
#           diverse, multicultural environment with a strong appetite to learn and deliver the best results,Strong focus on the positive\
#           client experience, Sales increase, Solution-oriented, High attention to details, Forming and implementation of sales plans,\
#           Market research and strategy formation, Negotiation with partners and potential clients, Management of expanding marketing\
#           representation, Participation in the development of the company's",
#         'IoT security services and solutions, AR/MR collaboration and productivity tool for enterprise, Digital Media Broadcast\
#           technology, Customer Relationship Management, Project Management IoT Security,Consulting & Sales Team Management,\
#           Communication Skills Sales Force, Customer Relationship Management, Project Management IoT Security, Negotiating affiliations\
#           agreements, Supervising and directing sales agents worldwide, Introduced and implemented new business development strategy\
#           and products, Performed and arranged successful product demonstrations for customers, Building closer relationships,\
#           Motivating and conducting teams and projects across our platform, Successfully achieved joined target of Â£8.5m a year in a\
#           team of 2,French (Native or Bilingual Proficiency), English (Native or Bilingual Proficiency), Portuguese (Full Professional\
#           Proficiency), Spanish (Limited Working Proficiency), German (Elementary Proficiency)',
#         'Investment Management, Analytical Accounting, Fixed Income, Capital Market, Futures and Options,Excellent Customer Service\
#           Skills, Friendly and Outgoing Attitude, Initiative and Problem-solving Abilities, Strong Communication Skills, Excellent\
#           Presentation Skills, Ability to Work in a Team and Independently,Sales, Marketing, Business Development, Relationship\
#           Building, Negotiation, Lead Generation, Customer Satisfaction,Chinese, English, French'
 
#         ]

# tagged_data = [TaggedDocument(words=word_tokenize(_d.lower()), tags=[str(i)]) for i, _d in enumerate(data)]
# model = gensim.models.doc2vec.Doc2Vec(vector_size=30, min_count=2, epochs=80)
# model.build_vocab(tagged_data)
# model.train(tagged_data, total_examples=model.corpus_count, epochs=80)
# model.save("d2v.model")

# model = Doc2Vec.load("d2v.model")
# similar_doc = model.docvecs.most_similar('0')
# print(similar_doc)

# data = ['Proven track record in business development and sales, Strong understanding of the Swiss market and ideally the learning\
#          and development landscape, Excellent communication and interpersonal skills, Results-oriented mindset with a drive to meet\
#          and exceed sales targets, Excellent time management skills and ability to prioritize efficiently',
#         'Customer relationship management, Facilitation of customer UX journeys, Market and product segmentation, Strategic forecasting,\
#           Project management, Storytelling and sales pitches, Digital transformation, Risk- and portfolio management, M&A, Strategic\
#           business expansion, Statistical modelling, Thought leadership',
#         'Salesforce, Canvas, RMS, WordPress Elementor, Bridge-builder',
#         "PC literacy: Microsoft Office (MS Word, MS Excel, MS PowerPoint, MS Outlook, Power BI), Adobe Acrobat Reader, 1C, SAP, Zendesk,\
#           Pandadoc, Bitrix",
#         'IoT security services and solutions, AR/MR collaboration and productivity tool for enterprise, Digital Media Broadcast\
#           technology, Customer Relationship Management, Project Management IoT Security',
#         'Investment Management, Analytical Accounting, Fixed Income, Capital Market, Futures and Options,Excellent Customer Service\
#           Skills, Friendly and Outgoing Attitude, Initiative and Problem-solving Abilities, Strong Communication Skills, Excellent\
#           Presentation Skills, Ability to Work in a Team and Independently,Sales, Marketing, Business Development, Relationship\
#           Building, Negotiation, Lead Generation, Customer Satisfaction,Chinese, English, French'
 
#         ]

# data = ["I enjoy coding in python a lot","I enjoy using programming languages a lot"]
# tagged_data = [TaggedDocument(words=word_tokenize(_d.lower()), tags=[str(i)]) for i, _d in enumerate(data)]
# model = gensim.models.doc2vec.Doc2Vec(vector_size=30, min_count=2, epochs=80)
# model.build_vocab(tagged_data)
# model.train(tagged_data, total_examples=model.corpus_count, epochs=80)
# similar_doc = model.dv.most_similar('0')
# print(similar_doc)