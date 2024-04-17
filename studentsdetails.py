class Box:
    def __init__(self,name,rollNo,dbmsMarks,pythonMarks,cMarks,osMarks,cnMarks):
        self.name=name
        self.rollNo=rollNo
        self.dbmsMarks=dbmsMarks
        self.pythonMarks=pythonMarks
        self.cMarks=cMarks
        self.osMarks=osMarks
        self.cnMarks=cnMarks
    def printall(self):
        print(self.name,self.rollNo,self.dbmsMarks,self.pythonMarks,self.cMarks,self.osMarks,self.cnMarks)
        
stu1=Box("Harika","5A1",78,67,77,89,46)
stu1.printall()
stu2=Box("Swapna","5A2",38,65,97,59,41)
stu2.printall()
stu3=Box("Sushma","5A3",88,95,47,89,31)
stu3.printall()
