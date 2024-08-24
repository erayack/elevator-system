# Singleton ElevatorSystem class that represents the entire system and a Building class that contains instances of Floor and ElevatorCar.

class __ElevatorSystem(object):
  __instances = None
  
  def __new__(cls):
    if cls.__instances is None:
        cls.__instances = super(__ElevatorSystem, cls).__new__(cls)
    return cls.__instances

class ElevatorSystem(metaclass=__ElevatorSystem):
    def __init__(self, building):
      self.__building = building

    def monitoring():
        None

    def dispatcher():
        None


class __Building(object):
  __instances = None
  
  def __new__(cls):
    if cls.__instances is None:
        cls.__instances = super(__Building, cls).__new__(cls)
    return cls.__instances

class Building(metaclass=__Building):
  def __init__(self):
    self.__floor = []
    self.__elevator = []