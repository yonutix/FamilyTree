import datetime
import os

class Member:
    def __init__(self, id, name, gender, firstName, imgSrc="na.png", birthDate = None, fbPProfile = None, nameBefore=None):
        self.id = id
        self.name = name
        self.gender = gender
        self.firstName = firstName
        self.imgSrc = imgSrc
        self.birthDate = birthDate
        self.fbPProfile = fbPProfile
        self.nameBefore = nameBefore

        if imgSrc.endswith("\\na.png"):
            if gender == "F":
                self.imgSrc = imgSrc.replace("\\na.png", "\\woman.png")
            else:
                self.imgSrc = imgSrc.replace("\\na.png", "\\man.png")

    def getId(self):
        return self.id
    
    def getName(self):
        return self.name

    def getGender(self):
        return self.gender

    def getFirstName(self):
        return self.firstName

    def getImgSrc(self):
        return self.imgSrc

    def getBirthDate(self):
        return self.birthDate

    def getFBProfile(self):
        return self.fbPProfile

    def getNameBefore(self):
        return self.nameBefore

    def getLabelById(ID):
        result = ""

        nr = int(ID)
        result = result + chr(int(65 + nr % 10))
        nr = int(nr / 10)

        while nr > 0:
            result = result + chr(int(65 + nr % 10))
            nr = int(nr / 10)
            print(nr)
        return result

    def getLabel(self):
        return Member.getLabelById(self.id)

    def __repr__(self):
        return "[%d] %s %s (%s)" % (self.id, self.name, self.firstName, self.gender)

    def __str__(self):
        return "[%d] %s %s (%s)" % (self.id, self.name, self.firstName, self.gender)

    def __eq__(self, other):
        if other == None:
            return False
        return self.id == other.id and self.name == other.name and self.gender == other.gender