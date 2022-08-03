class Dog():
    
    num_of_limbs = 4
    
    def __init__(self, breed : str, color : str, weight : int):
        self.breed = breed
        self.color = color
        self.weight = weight
        
    
    
    def __str__(self):
        return self.breed
        
    def __add__(self, other):
        
        if isinstance(other, Dog):
            
            return self.weight + other.weight
        
        raise TypeError("Expected type of Dog but got %s" % type(other))
    
    
    def run(self):
        return f"This dog with {self.weight}kg is running"
        
        
    
dog1 = Dog("German shepherd", "black", 20)
dog2 = Dog("Bull dog", "black", 14)


print(dog1 + dog2)
# print(dog1.breed, dog1.weight, dog1.color)

# print(Dog.num_of_limbs)


print(dog1.run())
print(dog2.run())
