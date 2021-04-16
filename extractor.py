import re,requests
res=requests.get('https://www.washington.edu/about/common-phone-numbers-and-emails/')
source=res.text[0:]

mobile = re.compile(r'''(
 (\d{3}|\(\d{3}\))? # area code(optional)  #
 (\s|-|\.)? # separator or bitwise
 (\d{3}) # first 3 digits
 (\s|-|\.) # separator
 (\d{4}) # last 4 digits
 (\s*(ext|x|ext.)\s*(\d{2,5}))? # extension(optional)
 )''', re.VERBOSE)
 
mailId = re.compile(r'''([\w\.-]+@[\w\.-]+)''',re.VERBOSE)

result1 = mailId.findall(source)
result2 = mobile.findall(source)

allPhoneNumbar = []
for phoneNumbar in result2:
    allPhoneNumbar.append(phoneNumbar[0])

results = ' '.join(result1) +' '.join(allPhoneNumbar)
print(tuple(zip(result1,allPhoneNumbar)))