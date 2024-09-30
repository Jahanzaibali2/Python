import re

quote = "My name is Jahanzaib Ali. My phone number 0313-2656524. my email is abc@gmail.comad and abcedfgh@Knysys.com."

# email = re.findall(r"@[A-Za-z]+\.com", quote)
# # email = re.findall(r"[\w]+@[\w\.]+", quote)
# print(email)



# for all the numerica values
# findall = re.findall('\d', quote)
# print(findall)
 
# For all the non- numeric values
# x = re.findall(r'\D{5}', quote)
# print(x)

#  # For only numbers and letters, /S for all but spaces
# nospace = re.findall(r'\w{2}', quote)
# print(nospace)

#  # For including everything but numbers and letters, /s for only spaces
# space = re.findall(r'\W', quote)
# print(space)


# For Searching a specifin pattern in the string
# search = re.search("Jahanzaib",quote)
# print(search)

# phone = re.findall(r"[\d{4}\-\d{7}]+ | ", quote)
# print(phone)

# # For splitting the string
# slit = re.split(r"\.",quote)
# print(slit)


# # For splitting the string
# sub = re.sub("Jahanzaib", "Zhumail" , quote ,1)
# print(sub)

# ---------------------------------------------------------------- #
 # For including everything but numbers and letters, /s for only spaces
# space = re.findall(r'[a-zA-Z0-9]', quote)
# print(space)

# Guessing game
# string = "My name is Jahanzaib Ali. My Brother is Shahzaib"
# x = re.findall(r"....zaib\.",string)
# x1 = re.findall(r".{4}zaib$",string)
# print(x)
# print(x1)

# $ for the end of the string eg. .com$ /Z
# ^ for the beginning of the string eg. ^my /A

# * 0 or more
# + 1 or more
# ? one or zero

# kleene and closure
# x = re.findall(r"M.+i\.",quote)
# x2 = re.findall(r"m.*i\.",quote)
# x3 = re.findall(r"M.|0.*5",quote)
# # x = re.findall(r".{4}zaib",quote)
# print(x)
# print(x2)
# print(x3)