
class Item():
    def __init__(self, name, power):
        self._name = name
        self._description = None
        self.strength = power

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, desc):
        self._description = desc

    def describe(self):
        print("")
        print("A", self._name, "is here!")
        print(self._description)

    
