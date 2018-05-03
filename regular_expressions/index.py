import re
# s = '100 BROAD ROAD APT. 3'
# # s.replace('ROAD', 'RD.')  
# re.sub(r'\bROAD\b', 'RD.', s)  
# print(s)

sentence = 'Other practices dictate who is allowed in the birthing room and how the birth is announced to the British public.'
text_to_search = '''   
abcderfg
FGHKKLL
wkel;fjrn;efn;r
0987-372938                
'''
# print(r'\tTab')
# pattern = re.split(r'(\s*)', sentence)
# pattern = re.split(r'(sa*)', sentence)
# pattern = re.split(r'[a-fA-F0-9p-q][a-f]', 'sdflkkjkgwdJFJLHSDLKAJ', re.I|re.M)   
# pattern = re.findall(r'\d*', 'sdsd334 main st.sddsa')
# pattern = re.findall(r'\d?', 'sdsd334 main st.sddsa')
pattern = re.findall(r'\d{1,5}\s\w+\s\w+\.', 'sdsd334 main st.sddsa')


print(pattern)


# help(pattern.finditer())
# print(dir(pattern))
# print(help(pattern.finditer))