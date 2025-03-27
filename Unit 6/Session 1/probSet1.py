class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

def print_list(node):
    current = node
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()


# Prob 1: Write a single line of code that creates the linked list 4 -> 3 -> 2
node_4 = Node(4, Node(3, Node(2)))

# Prob 2: Create a function that returns the frquency of val in the linked list.
def count_element(head, val):
	if not head:
		return
	counter = 0
	current = head
	while current is not None:
		if current.value == val:
			counter += 1
		current = current.next
	return counter

head = Node(3, Node(1, Node(2, Node(1))))
print(count_element(head, 1))

# Prob 3: Debug this function such that it removes the tail of the list.
def remove_tail(head):
    if head is None: # If the list is empty, return None
        return None
    if head.next is None: # If there's only one node, removing it leaves the list empty
        return None 
		
	# Start from the head and find the second-to-last node
    current = head
    while current.next.next: # make this go from current.next to current.next.next; the second to last element cannot have a next.next if we want to remove the last element
        current = current.next

    current.next = None # Remove the last node by setting second-to-last node to None
    return head

head = Node(1, Node(2, Node(3, Node(4))))
print_list(head)
head = remove_tail(head)
print_list(head)

# Prob 4: Write a function that finds the middle node of a linked list. Return the second middle node if there is 2 (even length)
def find_middle_element(head):
    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow

head = Node(1, Node(2, Node(3)))
print(find_middle_element(head).value)

# Prob 5: Write a function that returns if a linked list is a palindrome
def is_palindrome(head):
    if not head or not head.next: # empty or single node linked list
          return True
    middle = find_middle_element(head) # O(n)
    current = head
    while current is not middle:  # O(n)
        if current.value != remove_tail(current).value: # O(n)
            return False
        current = current.next # Overall of loop is O(n^2) as for each current node, we remove its tail node, which takes O(n*n) = O(n^2) time
		# Space: O(1) as only space used is for variables
    return True
node = Node(1, Node(2, Node(1)))
print(is_palindrome(head))
    
# Prob 6: Reverse a linked list in place
def reverse(head):
	prev = None
	current = head
	while current:
		next_node = current.next
		current.next = prev
		prev = current
		current = next_node
	return prev

node = Node(1, Node(2, Node(3, Node(4))))
print_list(node)
print_list(reverse(node))