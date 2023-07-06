class Pet:
    all = []
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    
    def __init__(self, name, pet_type, owner=None):
        self.name = name
        if pet_type not in Pet.PET_TYPES:
            raise Exception('Invalid pet type')
        self.pet_type = pet_type
        self.owner = owner
        if owner is not None:
            owner.add_pet(self)
        Pet.all.append(self)


class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception('The pet must be an instance of the Pet class')
        pet.owner = self
        self._pets.append(pet)

    def pets(self):
        return self._pets

    def get_sorted_pets(self):
        return sorted(self._pets, key=lambda pet: pet.name)