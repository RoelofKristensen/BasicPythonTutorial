#creating own language by changing vowels into the letter r

def translate(phrase):
    translation = ""
    for letter in phrase:
       if letter in "AEIOUaeiou": # if letter.lower in "aeiou' . will work as itt convets the letter to lowercase
           if letter.isupper():
                translation = translation + "R"
           else:
               translation = translation + "r"
       else:
           translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))


