#create class My_subject
class My_Subject:
  def __init__(self, subject):
    #private variable  
    self.__subject = subject
    
  # create the get_subject and set_subject method for Encapsulation
  #get the value(subject) 
  def get_subject(self):
    print(f"I am taking the {self.__subject}.")

  # put a value(subject) in
  def set_subject(self,subject):
    if subject in ['math','science','English','PE'] :
      self.__subject = subject
    else:
      print("This is not my calss I am taking.")

#make the new instance and invoke the get_subject and set_subject
My_class = My_Subject('math')
My_class.get_subject()
My_class.set_subject('PE')
My_class.get_subject()

#create the class Can_drive
class Can_drive:
  def __init__(self, age):
    #protected variable for Encapsulation
    self._age = age
  
  #drive method: determine if the age is appropriate to drive
  def drive(self):
    if self._age > 15:
      print(f"\nI am {self._age} years old.\nYou can drive.")
    else:
      print(f"\nI am {self._age} years old.\nYou cannot drive.")

#make the instance and invoke the drive method
car = Can_drive(13)
car.drive()
car._age = 18
car.drive()