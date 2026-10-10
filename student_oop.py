class student:
    def __init__(self,name):
        self.name = name 
        self.grade = []
    
    def add_gread(self,grade):
        self.grade.append(grade)
        print (self.name ,"has ", self.grade)

    def average(self):
        if len(self.grade) == 0:
            return 0 
        return sum(self.grade) / len(self.grade)
    print
    
wktor = student("wiktor")
wktor.add_gread(5)
wktor.add_gread(6)
print(wktor.average())

    