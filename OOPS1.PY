#CREATING STUDENT CLASS THAT TAKES NAME AND MARKS OF 3 SUBJECT AS ARGUMENT IN CONSTRUCTOR .THEN CREATE A MEATHOD TO PRINT AVERAGE.

class student():
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum+=val
        print("hii",self.name,"your avg is",sum/3)

s1 =student("tony",[45,55,65])
s1.get_avg()



#Abstraction

#hiding the implementation details of a class and only showing the essential features to the users

class car():
  def __init__(self):
    self.acc=False 
    self.brk=False
    self.clutch=False

  def start(self):
    self.clutch=True
    self.acc=True
    print("car started")

  def stop(self):
    self.acc=False
    print("car stopped")

car1 =car()
car1.start()



