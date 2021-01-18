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


# this is our third model or class
class Printer:
    def printing_docs(self):
        return "Printing Documents is an objective."

    def printing_img(self):
        return "Printing Images is an objective."


'''

suppose you need 2 desktop, 1 scanners, 1 printers for different perposes....

(we know we can do also other three objectives with each desktop)


what will you do? you have to buy whose machines and your friend has the 
blueprint.He can provide that.

'''

# buying the 2 desktop
desktop1 = Desktop()  # Desktop 1 has been created according to its Blueprint
desktop2 = Desktop()  # Desktop 2 has been created according to its Blueprint

print("Desktop1 : ", desktop1.deployment())  # Desktop 1 is doing his job

print("Desktop2 : ", desktop2.graphics_design())  # Desktop 2 is doing his job

# lets do something else with this two desktops

print("Desktop1: ", desktop1.data_sotre())  # Desktop1 is doing another work
print("Desktop2: ", desktop2.playing_game()) # Desktop1 is doing another work

# now lets add your scanner and printer
scanner = Scanner()  # scanner has been created according to its Blueprint
printer = Printer()  # printer has been created according to its Blueprint

print("Scanner : ", scanner.scanning_img())  # scanner 2 is doing his job
print("Printer : ", printer.printing_img())  # printer is doing his job
# and you can also do the other objectives with this scanner and printer,

"""

Did you find out why we need Object? Till not? ok, Now think again, you need
2 more desktop with same congif and same objectives. What will you do? You just ask
your friend to provide you.

"""

#lest have to more desktops

desktop3=Desktop()
desktop4=Desktop()

"""So easy or not? you have same 4 objectives with this two desktops.  In this way
You can also add more scanners and printers. And this the power of object. A real
life problem in coding scenario. The qsn might be appereard in your head. Why? When?
Where?
Why we need this object oriented theorem and When and also Where? Believe me, 
just have a cristal clear basic about object. I will answer all of your qsn. Just
ensure that, YOU KNOW OBJECT AND CLASS FROM REAL LIFE TO CODING SCENARIO"""
