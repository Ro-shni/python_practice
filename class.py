num1=int(input("num1: "))
num2 = int(input("num2: "))
class mathematics:
    def add(self,num1,num2):
        self.num1=num1
        self.num2=num2
        return self.num1+self.num2
    def sub(self,num1,num2):
        self.num1 = num1
        self.num2=num2
        return self.num1-self.num2
    def mul(self,num1,num2):
        self.num1 = num1
        self.num2=num2
        return self.num1*self.num2
    def div(self,num1,num2):
        self.num1=num1
        self.num2=num2
        return self.num1/self.num2
ob = mathematics()
while(True):
    print(" 1.add\n2.sub\n3.mul\n4.div\n5.exit")
    choice = int(input("enter your choice: "))

    if choice == 1:
        print(ob.add(num1,num2))
    elif choice == 2:
        print(ob.sub(num1,num2))
    elif choice ==3:
        print(ob.mul(num1,num2))
    elif choice ==4:
        print(ob.div(num1,num2))



  