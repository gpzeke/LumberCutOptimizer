from user_input import get_part_dimension

class DataStore:
    def __init__(self):
         self.parts = []

    def add_dimension_store(self, length, width, quantity):
        part = (length, width, quantity)
        self.parts.append(part)
    
    #def remove_dimension_store():
    #    global parts
    