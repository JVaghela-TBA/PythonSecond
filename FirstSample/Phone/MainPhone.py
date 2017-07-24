class Parent:
    parentAttr=100;
    def __init__(self):
        print("Calling Parent Constructor");
    def parentMethod(self):
        print("Calling Parent Method");
    def setAttr(self,attr):
        Parent.parentAttr=attr;
    def getAttr(self):
        print("Print Attribute : "+str(Parent.parentAttr));

class Child(Parent):
    def __init__(self):
        print("Child Constructor Called ");
    def childMethod(self):
        print("Calling Child Method ");

