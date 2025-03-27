class Pokemon():
	def  __init__(self, name, hp, damage):
		self.name = name
		self.hp = hp # hit points
		self.damage = damage # The amount of damage this pokemon does to its opponent every attack
		
	def attack(self, opponent): #  Prob 1: Write a method attack() that takes in a Pokemon object opponent and decreases opponent's hp by their self's damage amount. If damaging the opponent leads to the opponent having an hp of 0 or less, the function should set the opponent's hp to 0 and print out "<Opponent name> fainted>.
    # Otherwise, the function should print out "<Pokemon name> dealt <damage> damage to <opponent name>".
		opponent.hp -= self.damage
		if opponent.hp <= 0:
			opponent.hp = 0
			print(opponent.name + " fainted")
		else:
			print(self.name + " dealt " + str(self.damage) + " damage to " + opponent.name)
		
pikachu = Pokemon("Pikachu", 35, 20)
bulbasaur = Pokemon("Bulbasaur", 45, 30) 

opponent = bulbasaur
pikachu.attack(opponent)

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

pokemonList = ["Jigglypuff", "Wigglytuff"] # Prob 2: Create the normal Python list ["Jigglypuff", "Wigglytuff"] as a linked list.
node_1 = Node(pokemonList[0])
node_2 = Node(pokemonList[1])
node_1.next = node_2
print(node_1.value, "->", node_1.next.value)
print(node_2.value, "->", node_2.next)

def add_first(head, new_node): # Prob 3: Write a function that adds a new head
	new_node.next = head
	head = new_node
	return head

print(node_1.value, "->", node_1.next.value)

new_node = Node("Ditto")
node_1 = add_first(node_1, new_node)

print(node_1.value, "->", node_1.next.value)

def get_tail(head): # Prob 4: Return the value of the tail node
	if not head:
		return None
	current = head
	while current:
		if current.next is None:
			return current
		current = current.next
		
node = Node("num1", Node("num2", Node("num3")))

head = node
tail = get_tail(node)
print(tail.value)

def ll_replace(head, original, replacement): # Prob 5: Write a function that replaces all occurences of original to replacement
	current = head
	while current:
		if current.value == original:
			current.value = replacement
		current = current.next
	return current

num3 = Node(5)
num2 = Node(6, num3)
num1 = Node(5, num2)
# initial linked list: 5 -> 6 -> 5

head = num1
ll_replace(head, 5, "banana")

def listify_first_n(head, n): # Prob 6:  Write a function that returns a list of all the values of the first n nodes
    result = []
    count = 0
    current = head
    while current and count != n:
        result.append(current.value)
        count += 1
        current = current.next
    return result

# linked list: a -> b -> c
a = Node('a', Node('b', Node('c')))
head = a
lst = listify_first_n(head,2)
print(lst)

# linked list: j -> k -> l 
j = Node('j', Node('k', Node('l')))
head2 = j
lst2 = listify_first_n(head2,5)
print(lst2)

def ll_insert(head, val, i): # Prob 7: Write a function that inserts a node with value val at index i
	if i == 0:
		return Node(val, head)
	current = head
	count = 0
	while current and count < i - 1:
		current = current.next
		count += 1
	new_node = Node(val, current.next)
	current.next = new_node
	return head

node = Node(3, Node(8, Node(12, Node(9))))
current = ll_insert(node, 20, 2)
while current:
	print(str(current.value) + "->", end = "")
	current = current.next
	
def list_to_linked_list(lst): # Prob 8: Write a function that converts a list to a linked list
	head = Node(lst[0])
	current = head
	for val in lst[1:]:
		current.next = Node(val)
		current = current.next
	return head

normal_list = ["Betty", "Veronica", "Archie", "Jughead"]
linked_list = list_to_linked_list(normal_list)
print(linked_list.value) # Only prints the head element!

class Node:
	def __init__(self, value, next = None, prev = None):
		self.value = value
		self.next = next
		self.prev = prev

poliwag = Node('poliwag') # Prob 9: Given the Node class for a doubly linked list below, recreate the list ["Poliwag", "Poliwhirl", "Poliwrath"] as a doubly linked list.
poliwhirl = Node('poliwhirl', prev=poliwag)
poliwrath = Node('poliwrath', prev=poliwhirl)
poliwag.next = poliwhirl
poliwhirl.next = poliwrath
print(poliwhirl.prev.value, "<->", poliwhirl.value, "<->", poliwhirl.next.value)

def print_reverse(tail): # Prob 10: Write a function that takes a tail of a doubly linked list and prints out the values of the list in reverse order
	current = tail
	while current:
		print(current.value + " ", end ='')
		current = current.prev
	return current
print_reverse(poliwrath)