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
                    
                elif (inp[i]) == 'b' :
                    sign_word = sign_word + 'b'
                    
                elif (inp[i]) == 'c' :
                    sign_word = sign_word + 'c'
                    
                elif (inp[i]) == 'd' :
                    sign_word = sign_word + 'd'
                   
                elif (inp[i]) == 'e' :
                    sign_word = sign_word + 'e'
                    
                elif (inp[i]) == 'f' :
                    sign_word = sign_word + 'f'
                    
                elif (inp[i]) == 'g' :
                    sign_word = sign_word + 'g'
                    
                elif (inp[i]) == 'h' :
                    sign_word = sign_word + 'h'
                   
                elif (inp[i]) == 'i' :
                    sign_word = sign_word + 'i'
                    
                elif (inp[i]) == 'j' :
                    sign_word = sign_word + 'j'
                   
                elif (inp[i]) == 'k' :
                    sign_word = sign_word + 'k'
                    
                elif (inp[i]) == 'l' :
                    sign_word = sign_word + 'l'
                    
                elif (inp[i]) == 'm' :
                    sign_word = sign_word + 'm'
                    
                elif (inp[i]) == 'n' :
                    sign_word = sign_word + 'n'
                    
                elif (inp[i]) == 'o' :
                    sign_word = sign_word + 'o'
                    
                elif (inp[i]) == 'p' :
                    sign_word = sign_word + 'p'
                    
                elif (inp[i]) == 'q' :
                    sign_word = sign_word + 'q'
                    
                elif (inp[i]) == 'r' :
                    sign_word = sign_word + 'r'
                    
                elif (inp[i]) == 's' :
                    sign_word = sign_word + 's'
                    
                elif (inp[i]) == 't' :
                    sign_word = sign_word + 't'
                   
                elif (inp[i]) == 'u' :
                    sign_word = sign_word + 'u'
                    
                elif (inp[i]) == 'v' :
                    sign_word = sign_word + 'v'
                    
                elif (inp[i]) == 'w' :
                    sign_word = sign_word + 'w'
                    
                elif (inp[i]) == 'x' :
                    sign_word = sign_word + 'x'
                   
                elif (inp[i]) == 'y' :
                    sign_word = sign_word + 'y'
                    
                elif (inp[i]) == 'z' :
                    sign_word = sign_word + 'z'
                   
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


