#1

class Circle():
   
   def __init__(self,r):
      self.radius = r
      
   def getArea(self):
      return(3.14*self.radius*self.radius)
     
   def getCircumference(self):
      return(2*3.14*self.radius)

x = Circle(4)
print("Area: ", x.getArea())
print("Circumference: ", x.getCircumference())

#2

class Student():

   def __init__(self,n,r):
      self.name = n
      self.roll_no = r

   def display(self):
      print("Name: ",self.name)
      print("Roll no: ",self.roll_no)

x = Student('bharti',28)
x.display()

#3

class Temperature():

   def __init__(self,c,f):
      self.celsius = c
      self.fahrenheit = f

   def convertFahrenheit(self):
      return(self.celsius*1.8+32)

   def convertCelsius(self):
      return((self.fahrenheit-32)/1.8)

x = Temperature(54,28)
print("Fahrenheit from Celsius: ", x.convertFahrenheit())

print("Celsius from Fahrenheit: ", x.convertCelsius())


#4

class MovieDetails():

   def __init__(self,mn,an,yr,r):
      self.movie_name = mn
      self.artist_name = an
      self.year_of_release = yr
      self.ratings = r

   def display(self):
      print("movie name: ", self.movie_name)
      print("artist name: ",self.artist_name)
      print("year of release: ", self.year_of_release)
      print("ratings: ",self.ratings)

   def update(self,val):
      self.ratings = val
      print("updated ratings: ",self.ratings)
      

x = MovieDetails('avengers','chris',2018,8)
x.display()

x.update(9)


#5

class Expenditure():

   def __init__(self,e,s):
      self.expenditure = e
      self.savings = s

   def display(self):
      print("Expenditure: ", self.expenditure)
      print("Savings: ",self.savings)

   def calc(self):
      self.total_salary = self.expenditure+self.savings

   def displaySalary(self):
      print("Total salary: ",self.total_salary)
      
x = Expenditure(30000,30000)
x.display()
x.calc()
x.displaySalary()
