from kivy.app import App
from kivy.uix.widget import Widget

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
    return max(pal, key=len)

class MainWidget(Widget):
    pass

class TheLabApp(App):

    pass


TheLabApp().run()



    

