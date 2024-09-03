class User:
  """ Define the User """
  def __init__(self, name, year_of_birth):
    """Initialize the user"""
    self.name = name
    self.year = year_of_birth

  def century(self):
    """ Caculate the user century based on their year of birth"""
    if self.year < 2000:
      return "20th"
    else:
      return "21st"

  def welcome(self):
    """ Return a welcome message """
    return f"Wecome {self.name}, you were born in the {self.century()} century"
