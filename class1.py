class Student:
   def __init__(self, name, age):
       self.name = name
       self.age = age
   def display(self):
       print('Student name is : ', self.name)
       print('Student age is :', self.age)
       
s1 = Student('Mayur', 30)
s1.display()
s3 = Student('Ankush', 28)
s3.display()
   
