#parent class 
class Person:
  # initialize method
  def __init__(self):
    self.name ="Seonhwa"
    self.age = 26

#child class instance  
class Korean(Person):

  #initialize method
  def __init__(self):
    #call pearents method
    super().__init__()
    self.lang ='Korean'
    self.food ='Kimchi'

  #introduce method
  def introduce(self):
    print(f"My name is {self.name}, and I am {self.age} years old.\nMy native language is {self.lang}, and My favorite food is {self.food}.")  

#invoke the method of Korean()
Person2 = Korean()
Person2.introduce()