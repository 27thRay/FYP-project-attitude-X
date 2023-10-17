import docx2txt

#extract text
text = docx2txt.process("Resume_5.docx")

# # extract text and write images in /tmp/img_dir
# text = docx2txt.process("Resume_5.docx", "/tmp/img_dir") 
# #Resume_1, Resume_2 works
# #Resume Ray, Shaun, Resume_3, Resume_4, Resume_5 does not work

print(text)