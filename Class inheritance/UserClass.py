class User:
  def __init__(self, name):
    self.name = name

  def greet(self):
    """Greetings"""
    print(f"Welcome - {self.name}")