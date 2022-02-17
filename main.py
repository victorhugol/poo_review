class School:
    __name = ""
    __level = ""
    __numberOfStudents = 0
    
    def __init__(self,name,level,numberOfStudents):
      self.__name = name
      self.__level = level
      self.__numberOfStudents = numberOfStudents

    def get_name(self):
        return self.__name
    
    def get_level(self):
        return self.__level
    
    def get_numberOfStudents(self):
        return self.__numberOfStudents
    
    def set_name(self,name):
        self.__name = name
    def set_level(self,level):
        self.__level = level
    def set_numberOfStudents(self,numberOfStudents):
        self.__numberOfStudents = numberOfStudents
    def __repr__(self):
        return f"A {self.__level} school named {self.__name} with {self.__numberOfStudents} students"
    

class Primary(School):
    __pickupPolicy = ""

    def __init__(self,name,numberOfStudents,pickupPolicy):
      self.__name = name
      self.__level = "primary"
      self.__numberOfStudents = numberOfStudents
      self.__pickupPolicy = pickupPolicy

    def get_pickupPolicy(self):
        return self.__pickupPolicy

    def set_pickupPolicy(self,pickupPolicy):
        self.__pickupPolicy = pickupPolicy

    def __repr__(self):
      return super().__repr__()
        
class Middle(School):
    pass

class High(School):
    sportsTeams = []
    
    def get_sportsTeams(self):
        return self.__sportsTeams

    def set_sportsTeams(self,sportsTeams):
        self.__sportsTeams = sportsTeams

    def __repr__(self):
      return self.__sportsTeams

