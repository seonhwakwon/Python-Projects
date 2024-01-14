#Parnet clas
class Person:
  #initialize variable
  def __init__ (self, chest_size, waist_size):
      self.waist_size = waist_size
      self.chest_size = chest_size
  #error occur if Dress methond is not implemented(override) in the child class
  def Dress(self):
      raise NotImplementedError
#child class
class Women(Person):
  #initialize variable
  def __init__(self, chest_size, waist_size):
    #accessing parents class variable
    super().__init__(chest_size, waist_size)
    self.skirt_size = 0
    self.blouse_size = 0

  #overriding method 
  def Dress(self):
    #to figure out the size
    if  self.chest_size <= 85:
        self.blouse_size = 'S'
    elif 86 <= self.chest_size <= 91:
        self.blouse_size = 'M'
    elif 92 <= self.chest_size <= 96:
        self.blouse_size = 'L'
    else:
        self.chest_size = 'No size in our brand'
 
    if  self.waist_size <= 26:
        self.skirt_size = 'S'
    elif 27 <= self.waist_size <=29:
        self.skirt_size = 'M'
    elif 30 <= self.waist_size <= 32:
        self.skirt_size = 'L'
    else:
        self.skirt_size = 'No size in our brand'
    print(f"\nYour(Women) size\n----------------\nBlouse size: {self.blouse_size}\nSkirt size: {self.skirt_size}")

#child class  
class Men(Person):
    #initialize variable
    def __init__(self, chest_size, waist_size):
      super().__init__(chest_size, waist_size)
      self.pants_size = 0
      self.tshirt_size = 0

    #overriding method
    def Dress(self):
      #to figure out the size
      if  self.chest_size <= 93:
          self.tshirt_size = 'S'
      elif 94 <= self.chest_size <= 102:
          self.tshirt_size = 'M'
      elif 103 <= self.chest_size <= 112:
          self.tshirt_size = 'L'
      else:
          self.tshirts_size = 'No size in our brand'
  
      if  self.waist_size <= 30:
          self.pants_size = 'S'
      elif 31 <= self.waist_size <=33:
          self.pants_size = 'M'
      elif 35 <= self.waist_size<= 37:
          self.pants_size = 'L'
      else:
          self.pants_size = 'No size in our brand'
      print(f"\nYour(Men) size\n----------------\nT-shirts size: {self.tshirt_size}\nPants size: {self.pants_size}")

#making the new instance and invoke the method "Dress" in woman and men  
Person_women = Women(83, 25)
Person_women.Dress()
 

Person_men= Men(105, 36)
Person_men.Dress()  





    