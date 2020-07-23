#Initiate the word and import the image library
import sys
from PyQt4 import QtCore, QtGui, uic


#Welcome the User
print("hello and welcome")

#Ask the user to input the word or words to be converted
qtCreatorFile = "trial.ui" # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.trans.clicked.connect(self.translate)
        
    def translate(self):
            sign_word = ''
            inp = str(self.user.toPlainText())
            length = len(inp)
            #Check and convert each letter in the inp
            i = 0
            while i <= length - 1:
                if (inp[i]) == 'a' :
                    sign_word = sign_word + 'a'
                    webbrowser.open('signs/a.jpg')
                elif (inp[i]) == 'b' :
                    sign_word = sign_word + 'b'
                    webbrowser.open('signs/b.jpg')
                elif (inp[i]) == 'c' :
                    sign_word = sign_word + 'c'
                    webbrowser.open('signs/c.jpg')
                elif (inp[i]) == 'd' :
                    sign_word = sign_word + 'd'
                    webbrowser.open('signs/d.jpg')
                elif (inp[i]) == 'e' :
                    sign_word = sign_word + 'e'
                    webbrowser.open('signs/e.jpg')
                elif (inp[i]) == 'f' :
                    sign_word = sign_word + 'f'
                    webbrowser.open('signs/f.jpg')
                elif (inp[i]) == 'g' :
                    sign_word = sign_word + 'g'
                    webbrowser.open('signs/g.jpg')
                elif (inp[i]) == 'h' :
                    sign_word = sign_word + 'h'
                    webbrowser.open('signs/h.jpg')
                elif (inp[i]) == 'i' :
                    sign_word = sign_word + 'i'
                    webbrowser.open('signs/i.jpg')
                elif (inp[i]) == 'j' :
                    sign_word = sign_word + 'j'
                    webbrowser.open('signs/j.jpg')
                elif (inp[i]) == 'k' :
                    sign_word = sign_word + 'k'
                    webbrowser.open('signs/k.jpg')
                elif (inp[i]) == 'l' :
                    sign_word = sign_word + 'l'
                    webbrowser.open('signs/l.jpg')
                elif (inp[i]) == 'm' :
                    sign_word = sign_word + 'm'
                    webbrowser.open('signs/m.jpg')
                elif (inp[i]) == 'n' :
                    sign_word = sign_word + 'n'
                    webbrowser.open('signs/n.jpg')
                elif (inp[i]) == 'o' :
                    sign_word = sign_word + 'o'
                    webbrowser.open('signs/o.jpg')
                elif (inp[i]) == 'p' :
                    sign_word = sign_word + 'p'
                    webbrowser.open('signs/p.jpg')
                elif (inp[i]) == 'q' :
                    sign_word = sign_word + 'q'
                    webbrowser.open('signs/q.jpg')
                elif (inp[i]) == 'r' :
                    sign_word = sign_word + 'r'
                    webbrowser.open('signs/r.jpg')
                elif (inp[i]) == 's' :
                    sign_word = sign_word + 's'
                    webbrowser.open('signs/s.jpg')
                elif (inp[i]) == 't' :
                    sign_word = sign_word + 't'
                    webbrowser.open('signs/t.jpg')
                elif (inp[i]) == 'u' :
                    sign_word = sign_word + 'u'
                    webbrowser.open('signs/u.jpg')
                elif (inp[i]) == 'v' :
                    sign_word = sign_word + 'v'
                    webbrowser.open('signs/v.jpg')
                elif (inp[i]) == 'w' :
                    sign_word = sign_word + 'w'
                    webbrowser.open('signs/w.jpg')
                elif (inp[i]) == 'x' :
                    sign_word = sign_word + 'x'
                    webbrowser.open('signs/x.jpg')
                elif (inp[i]) == 'y' :
                    sign_word = sign_word + 'y'
                    webbrowser.open('signs/y.jpg')
                elif (inp[i]) == 'z' :
                    sign_word = sign_word + 'z'
                    webbrowser.open('signs/z.jpg')
                else:
                    print("Invalid")
                    break
                i = i + 1
            self.output.setText(sign_word)
            #print the inp in sign language
            print('the inp ' + inp)
            print('Is shown as ' + sign_word)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


