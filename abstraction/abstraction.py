from abc import ABC, abstractmethod

class Subject(ABC):
  def __init__(self, subject_1, subject_2):
    self.subject_1 = subject_1
    self.subject_2 = subject_2
    super().__init__()
  def class_list(self):
    print(f"\nYou should take the {self.subject_1} and {self.subject_2} class.")
  
  @abstractmethod
  def class_info(self):
    pass


class Class_1(Subject):
  def class_info(self):
    print(f"Your first class is {self.subject_1}.")


class Class_2(Subject):
  def class_info(self):
    print(f"Your second class is {self.subject_2}.")



obj1 = Class_1('Math','English')
obj2 = Class_2('Math','English')
obj1.class_list()
obj1.class_info()
obj2.class_info()



