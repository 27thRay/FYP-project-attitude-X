import openai

openai.api_base = 'https://api.deepinfra.com/v1/openai'
openai.api_key = 'UJGOceHjyxw1ONsrcllJzmXDffiF8XRK'

from pdfminer.high_level import extract_text
#Provide the Resume file path as an argument
file_path = "resume_data/Resume_1.pdf"  
resume = extract_text(file_path)

resume_temp = resume.replace('\n','')

prompt = f'''
Resume:
{resume}'''

system_prompt = f'''
Strictly extract name, all technical skills, all soft skills and languages in the format, Please focus only on the professional and work-related information in the resume. Do not extract or consider any personal interests or hobbies mentioned.
extract and include skills obtained from work experiences and education background under soft skills or technical skills (where ever it fits) from the resume: 
name: ...
technical skills: ... 
soft skills: ... 
languages: ...
'''

MODEL_DI = "meta-llama/Llama-2-70b-chat-hf"

response = openai.ChatCompletion.create(
  model=MODEL_DI, # Optional (user controls the default)
  messages=[
      {"role": "system", "content": system_prompt},
      {"role": "user", "content": prompt},
      # {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."}
  ],
  headers={
    "HTTP-Referer": "http://localhost:3000", # To identify your app. Can be set to e.g. http://localhost:3000 for testing
    # "X-Title": $YOUR_APP_NAME, # Optional. Shows on openrouter.ai
  },
  temperature = 0.2,
  max_tokens = 1000,
  top_p = 0.9
)

reply = response.choices[0].message

print(reply['content'])