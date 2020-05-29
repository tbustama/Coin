import random

class Coin:
    def __init__(self, rare=False, clean=True, heads=True, **kwargs):
       
        for key,value in kwargs.items():
            setattr(self,key,value)

        self.is_rare = rare
        self.is_clean = clean
        self.heads = True
        
        if self.is_rare:
            self.value = self.original_value * 1.25
        else:
            self.value = self.original_value

        if self.is_clean:
            self.color = self.clean_color
        else:
            self.color = self.rusty_color

    def __del__(self):
        print("Coin Spent!")

    def rust(self):
        self.color = self.rusty_color

    def clean(self):
        self.color = self.clean_color

    def flip(self):
        head_options = [True, False]
        choice = random.choice(head_options)
        self.heads = choice

    def __str__(self):
        if self.original_value > 0.10:
            return "Quarter"
        elif self.original_value > 0.05:
            return "Dime"
        elif self.original_value > 0.01:
            return "Nickel"
        else:
            return "Penny"


class Penny(Coin):
    def __init__(self):
        data = {
            "original_value": 0.01,
            "clean_color": "copper",
            "rusty_color": "greenish",
            "num_edges": 1,
            "diameter": 22.5,
            "thickness": 3.15,
            "mass": 9.5
        }
        super().__init__(**data)

class Nickel(Coin):
    def __init__(self):
        data = {
            "original_value": 0.05,
            "clean_color": "silver",
            "rusty_color": "brownish",
            "num_edges": 1,
            "diameter": 5.5,
            "thickness": 4.15,
            "mass": 15.5
        }
        super().__init__(**data)

class Dime(Coin):
    def __init__(self):
        data = {
            "original_value": 0.1,
            "clean_color": "silver",
            "rusty_color": "brownish",
            "num_edges": 1,
            "diameter": 22.5,
            "thickness": 3.15,
            "mass": 9.5
        }
        super().__init__(**data)


class Quarter(Coin):
    def __init__(self):
        data = {
            "original_value": 0.25,
            "clean_color": "silver",
            "rusty_color": "brownish",
            "num_edges": 1,
            "diameter": 45.5,
            "thickness": 5.15,
            "mass": 20.5
        }

    
        super().__init__(**data)


coins = [Penny(), Nickel(), Dime(), Quarter()]

for coin in coins:
    arguments = [coin, coin.color, coin.value, coin.diameter, coin.thickness, coin.num_edges, coin.mass]

    string = "{} - Color: {}, Value: {}, Diameter: {}, Thickness: {}, Number of Edges: {}, Mass: {}".format(*arguments)
    print(string)
