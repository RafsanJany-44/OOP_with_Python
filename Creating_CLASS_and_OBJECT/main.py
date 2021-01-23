# this is our main function

#first you have to create  classes . Lets make 3 classes according to our example.

# We have to make a Desktop class where all the objective will be remain inside

class Desktop:

    def playing_game(self):
        return "Playing game is an objective."

    def graphics_design(self):
        return "Graphics Designing is an objective."

    def deployment(self):
        return "Deploying is an objective."

    def data_sotre(self):
        return "Data Storing is an objective."


# We have to make a Scanner class where all the objective will be remain inside
class Scanner:

    def scannind_docs(self):
        return "Scanning Documents is an objective."

    def scanning_img(self):
        return "Scanning Images is an objective."


# We have to make a Printer class where all the objective will be remain inside
class Printer:

    def printing_docs(self):
        return "Printing Documents is an objective."

    def printing_img(self):
        return "Printing Images is an objective."


# back to main programme file

#making a Desktop1 object
desktop1 = Desktop()

desktop2 = Desktop()

# desktop1 and desktop2 has all the properties of Desktop class.

# now we can use the desktop1 and desktop2 to use the
# properties of Desktop class

print("Desktop-1 : ", desktop1.deployment())

print("Desktop-2 : ", desktop2.graphics_design())

# But why? this? we can have the direct access with Desktop.graphics_design(0)  (need to pass a arg)

print(Desktop.graphics_design(0))

# but this can be a cause of lost of data..
# remember Desktop is only a model.
#So it will erase all data when ever it will be re-called. So this why we need object to
# get memory inside ram


# you can make object of other classes

printer1=Printer()

print(printer1.printing_docs())
