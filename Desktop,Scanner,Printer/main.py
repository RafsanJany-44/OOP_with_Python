# this is our first model or class
class Desktop:
    def playing_game(self):
        return "Playing game is an objective."

    def graphics_design(self):
        return "Graphics Designing is an objective."

    def deployment(self):
        return "Deploying is an objective."

    def data_sotre(self):
        return "Data Storing is an objective."


# this is our second model or class
class Scanner:
    def scannind_docs(self):
        return "Scanning Documents is an objective."

    def scanning_img(self):
        return "Scanning Images is an objective."


#this is our third model or class
class Printer:
    def printing_docs(self):
        return "Printing Documents is an objective."

    def Printing_img(self):
        return "Printing Images is an objective."


'''

 supose you need 2 desktop, 1 scanners, 1 printers for different perposes....

 desktop1-> deploying,
 desktop2-> Graphics Design,
   
 (but we know we can do also other three objectives with each desktop)
 
 
 what will you do? you have to buy whose machines and your frnd has the 
 blueprint. He can provide that.
 
'''


# buying the 2 desktop
desktop1=Desktop()    #Desktop 1 has been created according to its Bluprint
desktop2=Desktop()    #Desktop 2 has been created according to its Bluprint

print("Desktop1 : ",desktop1.deployment()) #Desktop 1 is doing his job

print("Desktop2 : ",desktop2.graphics_design()) #Desktop 2 is doing his job