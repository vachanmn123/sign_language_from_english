#Initiate the word and import the image library
import webbrowser
import time
sign_word = ''

#Welcome the User
print("hello and welcome")

#Ask the user to input the word or words to be converted
word = input("Enter the word to be converted:")
length = len(word)

#Check and convert each letter in the word
i = 0
while i <= length - 1:
    if (word[i]) == 'a' :
        sign_word = sign_word + 'a'
        webbrowser.open('signs/a.jpg')
        time.sleep(0.3)
    elif (word[i]) == 'b' :
        sign_word = sign_word + 'b'
        webbrowser.open('signs/b.jpg')
        time.sleep(0.3)
    elif (word[i]) == 'c' :
        sign_word = sign_word + 'c'
        webbrowser.open('signs/c.jpg')
    elif (word[i]) == 'd' :
        sign_word = sign_word + 'd'
        webbrowser.open('signs/d.jpg')
    elif (word[i]) == 'e' :
        sign_word = sign_word + 'e'
        webbrowser.open('signs/e.jpg')
    elif (word[i]) == 'f' :
        sign_word = sign_word + 'f'
        webbrowser.open('signs/f.jpg')
    elif (word[i]) == 'g' :
        sign_word = sign_word + 'g'
    elif (word[i]) == 'h' :
        sign_word = sign_word + 'h'
    elif (word[i]) == 'i' :
        sign_word = sign_word + 'i'
    elif (word[i]) == 'j' :
        sign_word = sign_word + 'j'
    elif (word[i]) == 'k' :
        sign_word = sign_word + 'k'
    elif (word[i]) == 'l' :
        sign_word = sign_word + 'l'
    elif (word[i]) == 'm' :
        sign_word = sign_word + 'm'
    elif (word[i]) == 'n' :
        sign_word = sign_word + 'n'
    elif (word[i]) == 'o' :
        sign_word = sign_word + 'o'
    elif (word[i]) == 'p' :
        sign_word = sign_word + 'p'
    elif (word[i]) == 'q' :
        sign_word = sign_word + 'q'
    elif (word[i]) == 'r' :
        sign_word = sign_word + 'r'
    elif (word[i]) == 's' :
        sign_word = sign_word + 's'
    elif (word[i]) == 't' :
        sign_word = sign_word + 't'
    elif (word[i]) == 'u' :
        sign_word = sign_word + 'u'
    elif (word[i]) == 'v' :
        sign_word = sign_word + 'v'
    elif (word[i]) == 'w' :
        sign_word = sign_word + 'w'
    elif (word[i]) == 'x' :
        sign_word = sign_word + 'x'
    elif (word[i]) == 'y' :
        sign_word = sign_word + 'y'
    elif (word[i]) == 'z' :
        sign_word = sign_word + 'z'
    elif (word[i]) == '1' :
        sign_word = sign_word + '1'
    else:
        print("Invalid")
        break
    i = i + 1

#print the word in sign language
print('the word ' + word)
print('Is shown as ' + sign_word)
