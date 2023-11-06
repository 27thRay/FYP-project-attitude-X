import pymongo
import pandas as pd
from bson import Decimal128

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["resumeDB"]
mycol = mydb["scores"]

th_style = {  # for row hover use <tr> instead of <td>
    'selector': 'th',
    'props': [('background-color', 'rgba(108,142,191,0.5)')]
}
headers = {
    'selector': 'th:not(.index_name)',
    'props': 'color: white; font-size: 16px'
}
td_style = {
    'selector': 'td',
    'props': 'background-color: rgba(108,142,191,0.3)'
}
tdhover_style = {
    'selector': 'tr:hover',
    'props': [('background-color', 'rgba(108,142,191,0.9)'),('color','white')]
}

def set_table_style(table):
    blankIndex=[''] * len(table)
    table.index=blankIndex
    return table.style.set_table_styles([th_style,headers,td_style,tdhover_style])

def insert_score(resume_dict, techsk_score, softsk_score, lang_score, overall_score):
    mydict =  {
        "name": resume_dict["Name"],
        "email":resume_dict["email"],
        "contact_number":resume_dict["contact_number"], 
        "technical_skills" : Decimal128(str(techsk_score)), 
        "soft_skills": Decimal128(str(softsk_score)), 
        "languages": Decimal128(str(lang_score)), 
        "overall_score": Decimal128(str(overall_score))
        }

    x = mycol.insert_one(mydict)

    return

def get_ovr_score_desc():
    table = pd.DataFrame(mycol.find().sort('overall_score',-1))
    if len(table) != 0:
        table = table.drop(['_id'],axis=1)
        table = set_table_style(table)
    return table

def get_techsk_score_desc():
    table = pd.DataFrame(mycol.find().sort('technical_skills',-1)).drop(['_id'],axis=1)
    return table

def get_softsk_score_desc():
    table = pd.DataFrame(mycol.find().sort('soft_skills',-1)).drop(['_id'],axis=1)
    return table

def get_lang_score_desc():
    table = pd.DataFrame(mycol.find().sort('languages',-1)).drop(['_id'],axis=1)
    return table

def search_score(score):
    myquery = {"overall_score" : {"$gte": score}}
    table = pd.DataFrame(mycol.find(myquery)).drop(['_id'],axis=1)

    return table