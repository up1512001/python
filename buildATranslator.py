# Building a Translator
# all vowels -> g
# ex dog = dgg

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":   # if letter in "AEIOUaeiou" is modified by that
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation +  letter
    return translation

print(translate(input("Enter a Phrase:")))



