class animal:
    species = "dog" 
    def make_sound(self):
        print("Bark")

print("The species of animal:",animal().species)
animal().make_sound()


obj = animal()

print(obj.species)