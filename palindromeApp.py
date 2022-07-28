from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

# Code that returns the largets palindrom within the string passed
def longestPalindromicSubstring(string):
    # Write your code here.
    def check(palindrom):
        leftIdx = 0
        rightIdx = len(palindrom)-1
        while leftIdx<rightIdx:
            if palindrom[leftIdx] != palindrom[rightIdx]:
                return False
            leftIdx +=1
            rightIdx-=1
        return True
    
    x= len(string)
    
    if(x==1): #edge case check
        return string
    pal = []
    
    for i in range(x):
        for j in range(x-1, i, -1):
            if(string[i]==string[j]):
                st = string[i:j+1]
                if(check(st)):
                    pal.append(st)

    if (len(pal)==0):
        return "There are no palindrome's in the input string"
    else:
        return max(pal, key=len)

# Code that builds the app 
class Palindrome(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6,0.7)
        self.window.pos_hint = {"center_x":0.5, "center_y":0.5}


        # Lable Widget
        self.greeting = Label(
                        text="Enter the string: ",
                        font_size = 18,
                        color = "#00FFCE"
                        )
        self.window.add_widget(self.greeting)

        # text input widget
        self.user = TextInput(
                    multiline = False,
                    padding_y=(20,20),
                    size_hint = (1,0.5)
                    )

        self.window.add_widget(self.user)

        #Button Widget
        self.button = Button(
                        text = "Enter",
                        size_hint = (1,0.5),
                        bold = True,
                        background_color ="#00FFCE"

                        )
        self.button.bind(on_press = self.callback)
        self.window.add_widget(self.button)
        return self.window

    def callback(self, instance):
        self.greeting.text = longestPalindromicSubstring(self.user.text)



        




if __name__ == '__main__':
    Palindrome().run()





    

