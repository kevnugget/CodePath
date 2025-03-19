class Pokemon:
    def __init__(self, name, types, evolution = None):
        self.name = name
        self.types = types
        self.is_caught = False
        self.evolution = evolution

    def print_pokemon(self):
        print({
            "name": self.name,   # Output: "name": "Squirtle",
            "types": self.types, # Output: "types": ["Water"],
            "is_caught": self.is_caught # Output: "is_caught": False
        })
    
    def catch(self): # Prob 4: Create a function that updates the Pokemon's is_caught attribute to be true
        self.is_caught = True

    def choose(self): # Prob 5: Create a function that prints "name + I choose you" if not caught, else print "name + is wild! Catch them if you can!"
        if self.is_caught:
            print(self.name + " I choose you!")
        else:
            print(self.name + " is wild! Catch them if you can!")
    
    def add_type(self, new_type): # Prob 6: Create a function that adds a new type to the type list of the Pokemon
        self.types.append(new_type)
    
    
def get_by_type(my_pokemon, pokemon_type): # Prob 7: Create a function get_by_type() that takes in a list of Pokemon instances my_pokemon and a string pokemon_type as parameters.
    result = []
    for pokemon in my_pokemon:
        if pokemon_type in pokemon.types:
            result.append(pokemon.name)
    return result

def get_evolutionary_line(starter_pokemon): # Prob 8: Write a function get_evolutionary_line() that takes in a Pokemon object starter_pokemon as a parameter. The function should return a list of itself and the Pokemon that the starter_pokemon can evolve into.
    result = [starter_pokemon.name]
    if starter_pokemon.evolution:
        result.extend(get_evolutionary_line(starter_pokemon.evolution))
    return result

class Node: 
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def main():
    my_pokemon = Pokemon("Pikachu", ["Electric"]) # Prob 1: Create an instance of Pokemon and store it in my_pokemon. Name should be "Pikachu" and types should be ["Electric"]
    squirtle = Pokemon("Squirtle", ["Water"])
    squirtle.print_pokemon() # Prob 2: Create an instance of Pokemon called squirtle whose name is "Squirtle" and type is ["Water"]
    squirtle.is_caught = True # Prob 3: Change the is_caught property to True
    squirtle.print_pokemon()

    my_pokemon = Pokemon("rattata", ["Normal"])
    my_pokemon.print_pokemon()

    my_pokemon.catch()
    my_pokemon.print_pokemon()

    my_pokemon = Pokemon("rattata", ["Normal"])
    my_pokemon.print_pokemon()

    my_pokemon.choose()
    my_pokemon.catch()
    my_pokemon.choose()

    jigglypuff = Pokemon("Jigglypuff", ["Normal"])
    jigglypuff.print_pokemon()

    jigglypuff.add_type("Fairy")
    jigglypuff.print_pokemon()

    # initializing pokemons
    jigglypuff = Pokemon("Jigglypuff", ["Normal", "Fairy"])
    diglett = Pokemon("Diglett", ["Ground"])
    meowth = Pokemon("Meowth", ["Normal"])
    pidgeot = Pokemon("Pidgeot", ["Normal", "Flying"])
    blastoise = Pokemon("Blastoise", ["Water"])

    my_pokemon = [jigglypuff, diglett, meowth, pidgeot, blastoise]
    normal_pokemon = get_by_type(my_pokemon, "Normal")
    print(normal_pokemon)

    charizard = Pokemon("Charizard", ["fire", "flying"])
    charmeleon = Pokemon("Charmeleon", ["fire"], charizard)
    charmander = Pokemon("Charmander", ["fire"], charmeleon)

    charmander_list = get_evolutionary_line(charmander)
    print(charmander_list)

    charmeleon_list = get_evolutionary_line(charmeleon)
    print(charmeleon_list)

    charizard_list = get_evolutionary_line(charizard)
    print(charizard_list)

    node_one = Node('a')
    node_two = Node('b')

    print(node_one.value) # Prob 9: sing the provided Node class below, create two nodes: The first node should have value a and be stored in a variable node_one. The second node should have value b and be stored in a variable node_two.
    print(node_one.next) 
    print(node_two.value)
    print(node_two.next) 
    node_one.next = node_two # Prob 10: To link the nodes, we can set a node's next attribute to hold another node. Update node_one from the Problem 9 to point to node_two.
    print(node_one.value)
    print(node_one.next.value)
    print(node_two.value)

    node_4 = Node('Toad')
    node_3 = Node('Wario', node_4)
    node_2 = Node('Luigi', node_3)
    node_1 = Node('Mario', node_2)

    print(node_1.value, "->", node_1.next.value)
    print(node_2.value, "->", node_2.next.value)
    print(node_3.value, "->", node_3.next.value)
    print(node_4.value, "->", node_4.next)

def print_linked_list(head): # Prob 12: Print the linked list, starting at the head
    current = head
    while current.next:
        print(current.value + " -> ", end='')
        current = current.next
    print(current.value)

node_4 = Node('Toad')
node_3 = Node('Wario', node_4)
node_2 = Node('Luigi', node_3)
node_1 = Node('Mario', node_2)
print_linked_list(node_1)
main()