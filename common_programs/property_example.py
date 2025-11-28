class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # Private

    @property
    def age(self):
        # getter
        
        print("[Person] Reading age...")
        return self.__age

    @age.setter
    def age(self, new_age):
        # setter
        
        print(f"[Person] Setting age to {new_age}...")
        if not isinstance(new_age, int):
            raise TypeError("Age must be a hole number")
        if new_age < 0 or new_age > 150:
            raise ValueError("Age out of range")
        self.__age = new_age

# Demo
p = Person("Rene", 18)

try:
    print(p.name) # Direct access
    print(p.age)  # Use getter
    p.age = 25  # Use setter
except Exception as e:
    print(f"ERROR:{e}")

try:
    p.age = 200  # ValueError
except Exception as e:
    print(f"ERROR:{e}")

try:
    p.age = "25"  # TypeError
except Exception as e:
    print(f"ERROR:{e}")


