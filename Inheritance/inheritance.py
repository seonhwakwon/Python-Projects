class Person:
  def __init__(self):
    self.name ="Seonhwa"
    self.age = 26
  
class Korean(Person):
  def __init__(self):
    super().__init__()
    self.lang ='Korean'
    self.food ='Kimchi'

  def introduce(self):
    print(f"My name is {self.name}, and I am {self.age} years old.\nMy native language is {self.lang}, and My favorite food is {self.food}.")  

Person2 = Korean()

Person2.introduce()