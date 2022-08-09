from data import data
import re
import pprint
# create a regex for phone numbers
phoneRegex = re.compile(r"""
                        # 415-555-0000, 444-0000, (415) 555-0000, 555-000 ext 12345, 
                        # .ext 12345, x12345
                        (
                        ((\d\d\d)|(\(\d\d\d\)))?        # area code (optional)
                        (\s|-)              # first separator
                        \d\d\d              # first 3 digits
                        -                   # second separator
                        \d\d\d\d            # last 4 digits
                        (((ext(\.)?\s)|x)   # extension-literal-part
                        (\d{2,5}))?          # extension-number-part (optional) 
                        )""", re.VERBOSE)

# create a regex for email adresses

emailRegex = re.compile(r"""
                        #some.+_thing@some.+_thing.[com,eu,info...]
                        
                        [a-zA-Z0-9_.+]+ # name part
                        @               # @ symbol
                        [a-zA-Z0-9_.+]+ # domain name
                        
                        """, re.VERBOSE)

# extract email and phone numbers

extractedPhoneNumbers = phoneRegex.findall(data)
# pprint.pprint(extractedPhoneNumbers)

allPhoneNumbers = []
for phoneNumbers in extractedPhoneNumbers:
    allPhoneNumbers.append(phoneNumbers[0])
#pprint.pprint(allPhoneNumbers)

extractedEmailAdresses = emailRegex.findall(data)
#pprint.pprint(extractedEmailAdresses)

# TODO: copy the extracted data somewhere else

result = ""

for index in range(0, len(allPhoneNumbers)):
    result+=(f"{allPhoneNumbers[index]} {extractedEmailAdresses[index]}\n")

print(result)
