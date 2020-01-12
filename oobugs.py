# vim: tw=80 ts=2 sw=2 et

class NumberGenerator:
  """A simple class that contains functions to generate ranges of numbers"""

  @classmethod
  def generate( quantity, value ):
      quantity = []
      while value:
          quantity.append(int(value))
          value -= 1

      return quantity

class Figure:
  """Abstract class for geometric figures"""

  def __init__(self, name ):
    """This is the constructor"""
    _name = name

  def name( self ):
    return self._name

class Rectangle(Figure):
    """Rectangle figure"""

    def __init__( self, width, height ):
        Figure("rectangle")
        self.width  = width
        self.height = height

    def width(self):
        return self.width

    def height(self):
        return self.height

    def size(self):
        return self.width * self.height

  
if __name__ == "__main__":
    # We print the range(10,0,-1)
    obj = NumberGenerator.generate(10)
    print(obj)
    # We print the range(20,0,-1)
    obj = NumberGenerator.generate(20)
    print(obj)

    # We create a rectangle
    r = Rectangle(10, 10)
    print(r.size())

# EOF



