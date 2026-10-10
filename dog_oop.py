class dog:
    def __init__(self,name,age):
        self.name = name 
        self.age = age
        

    def bark (self ):
        print (self.name, "say bark ")

    def have_bd(self):
        self.age = self.age + 1
        print ("new age is ",self.age)

rex = dog("rex",3)
rex.bark()
rex.have_bd()
rex.have_bd()

