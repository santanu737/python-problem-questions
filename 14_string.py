text = "Python Programming"

words = text.split()

print("Python:")
print(words[0])

print("Programming:")
print(words[1] )

if "Java" in text:
    print("Java present")
else:
    print("Java not present, adding")
    new_text = words[0]+ " Java " +words[1]

print("new string")
print(new_text)

print("length")
print(len(new_text) )

new_words =new_text.split()
print("no of words")
print(len(new_words))

print("capitalised")
capital_words=[]
for w in new_words:
    capital_words.append(w.capitalize() )
capitalised_string = " ".join(capital_words)
print(capitalised_string)

print("removing spaces")
no_space_string=new_text.replace(" ","")
print(no_space_string )

upper_text=new_text.upper()
print("frequency")
print("A" ,upper_text.count("A"))
print("P",upper_text.count("P") )
print("V",upper_text.count("V"))
print("M" ,upper_text.count("M"))