class User:
  def __init__(self, name):
    self.name = name

  def greet(self):
    """Greetings"""
    print(f"Welcome - {self.name}")
    
class FrenchUser(User):
  def __init__(self,name):
    
    self.name = name
    
class SpanishUser(User):
  def __init__(self,name):
    self.name = name
  
violet = FrenchUser("violet").greet()
violetta = SpanishUser("violetta").greet()


class Weather:
  
  def __init__(self,city,temp,conditions):
    """Initialising"""
    
    self.city = city
    self.temp = temp
    self.conditions = conditions
    
  def set_weather(self):
    
    self.city = city
    self.temp = temp
    self.conditions = conditions
      
  def display_weather(self):
    
    print(f"{self.city},{self.temp},{self.conditions}")
        
        
city1 = Weather("Pretoria",25,"sunny").display_weather()


  
