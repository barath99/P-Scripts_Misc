#OM NAMO NARAYANA

#q1
s = "work hard, dream big"
print(len(s))

#q3

prefix = 'example prefix '

sentences = "This is first line.\nThis is second line.\nThis is third line."

s = prefix

s_temp = prefix

for idx in range(len(sentences)):
    if sentences[idx] == '\n' and idx != len(sentences)-1:
        s += '\n'
        s += s_temp
        s_temp = prefix
    else:
        s += sentences[idx]
print(s)
del s_temp
    
#q4

number  = 123
k = 5
s = str(number)
temp = '*'*(k - len(s))
s += temp
print(s)

#q5
s = "randomString"
l = len(s)
s_temp = ""
for i in range(l):
    s_temp += s[l - i - 1]
s = s_temp
print(s)
del s_temp

#q6
s = "This is sample string"
char = "a"
s_temp = ""
for ch in s:
    if ch != char:
        s_temp += ch
s = s_temp
print(s)
del s_temp

#q7
s1 = "This is first string."
s2 = "This is second string"
s1 += s2
print(s1)


#q8
s1 = "This is first string."
s2 = "This is second string"
s3 = s1
s1 = s2
s2 = s3
del s3

#q9
sentence = "I felt happy because I saw the others were happy and because I knew I should feel happy, but I wasn’t really happy."
s_replace = "happy"
s_replace_with = "sad"
count_max = 2
count = 0
s = ""
words = list(sentence.split())
for word in words:
    if count==count_max or word != s_replace:
        s += word
        s += " "
    else:
        s += s_replace_with
        s += " "
        count += 1

print(s)

#q10
sentences = "Man is still the most extraordinary computer of all.\nThe similarities between humans and computers are more numerous than the differences."
num_chars = 0
num_words = 0
num_lines = 1
for ch in sentences:
    if ch==" ":
        num_words += 1
    elif ch == "\n":
        num_lines += 1
    else:
        num_chars += 1
print("Number of characters {}.\nNumber of words {}.\nNumber of lines {}".format(num_chars, num_words, num_lines))








