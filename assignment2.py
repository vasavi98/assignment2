fileName = input("Enter the file name : ")
inputFile= open(fileName,'r')
text = inputFile.read()


sentences=text.count('.')+text.count('?')+\
           text.count(':')+text.count(';')+\
           text.count('!')

words=len(text.split())


syllables = 0
for word in text.split():
    for vowel in ['a','e','i','o','u']:
        syllables+=word.count(vowel)
    for ending in ['es','ed','e']:
        if word.endswith(ending):
            syllables-=1
        if word.endswith('le'):
            syllables+=1

index = 206.835-1.015*(words/float(sentences))-\
        84.6*(syllables/words)
level =int(round(0.39*(words/float(sentences))+11.8*\
                 (syllables/float(words))-15.59))


print ("THE FLESCH INDEX IS",index)
print ("THE GRADE LEVEL EQAIVALENT IS",level)
print ("SENTENCES",sentences)
print ("WORDS",words)
print ("SYLLABLES",syllables)
