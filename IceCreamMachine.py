class IceCreamMachine:
    
    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings
        self.result = []
        
    def scoops(self):
        if len(self.ingredients) != 0 and len(self.toppings) != 0:
            for ingredient in self.ingredients:
                for topping in self.toppings:
                    res = []
                    res.append(ingredient)
                    res.append(topping)
                    self.result.append(res)
        
        return self.result


from math import sqrt

def find_roots(a, b, c):
    result = ()
    x1 = ((-b + sqrt(b**2 - 4*a*c)) / 2*a)
    x2 = ((-b - sqrt(b**2 - 4*a*c)) / 2*a)
    return x1, x2

print(find_roots(2, 10, 8));

print(sqrt(4*4))
                    
           
                
            

if __name__ == "__main__":
    machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
    print(machine.scoops()) #should print[['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]