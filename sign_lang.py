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
    elif (word[i]) == 'b' :
        sign_word = sign_word + 'b'
        webbrowser.open('signs/b.jpg')
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
        webbrowser.open('signs/g.jpg')
    elif (word[i]) == 'h' :
        sign_word = sign_word + 'h'
        webbrowser.open('signs/h.jpg')
    elif (word[i]) == 'i' :
        sign_word = sign_word + 'i'
        webbrowser.open('signs/i.jpg')
    elif (word[i]) == 'j' :
        sign_word = sign_word + 'j'
        webbrowser.open('signs/j.jpg')
    elif (word[i]) == 'k' :
        sign_word = sign_word + 'k'
        webbrowser.open('signs/k.jpg')
    elif (word[i]) == 'l' :
        sign_word = sign_word + 'l'
        webbrowser.open('signs/l.jpg')
    elif (word[i]) == 'm' :
        sign_word = sign_word + 'm'
        webbrowser.open('signs/m.jpg')
    elif (word[i]) == 'n' :
        sign_word = sign_word + 'n'
        webbrowser.open('signs/n.jpg')
    elif (word[i]) == 'o' :
        sign_word = sign_word + 'o'
        webbrowser.open('signs/o.jpg')
    elif (word[i]) == 'p' :
        sign_word = sign_word + 'p'
        webbrowser.open('signs/p.jpg')
    elif (word[i]) == 'q' :
        sign_word = sign_word + 'q'
        webbrowser.open('signs/q.jpg')
    elif (word[i]) == 'r' :
        sign_word = sign_word + 'r'
        webbrowser.open('signs/r.jpg')
    elif (word[i]) == 's' :
        sign_word = sign_word + 's'
        webbrowser.open('signs/s.jpg')
    elif (word[i]) == 't' :
        sign_word = sign_word + 't'
        webbrowser.open('signs/t.jpg')
    elif (word[i]) == 'u' :
        sign_word = sign_word + 'u'
        webbrowser.open('signs/u.jpg')
    elif (word[i]) == 'v' :
        sign_word = sign_word + 'v'
        webbrowser.open('signs/v.jpg')
    elif (word[i]) == 'w' :
        sign_word = sign_word + 'w'
        webbrowser.open('signs/w.jpg')
    elif (word[i]) == 'x' :
        sign_word = sign_word + 'x'
        webbrowser.open('signs/x.jpg')
    elif (word[i]) == 'y' :
        sign_word = sign_word + 'y'
        webbrowser.open('signs/y.jpg')
    elif (word[i]) == 'z' :
        sign_word = sign_word + 'z'
        webbrowser.open('signs/z.jpg')
    else:
        print("Invalid")
        break
    time.sleep(2)
    i = i + 1

#print the word in sign language
print('the word ' + word)
print('Is shown as ' + sign_word)
