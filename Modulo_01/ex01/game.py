class GotCharacter:
    def __init__(self, first_name: str, is_alive: bool = True):
        self.first_name = first_name
        self.is_alive = is_alive


class Stark(GotCharacter):
    def __init__(self, first_name: str = None, is_alive: bool = True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"
    
    def print_house_words(self):
        return(print(self.house_words))
    
    def die(self):
        self.is_alive = False


arya = Stark("Arya", True)
arya.print_house_words()
print(arya.__dict__)
print(arya.is_alive)
