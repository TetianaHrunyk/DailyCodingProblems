"""Given a linked list, sort it in O(n log n) time and constant space.

For example, the linked list 4 -> 1 -> -3 -> 99 should become -3 -> 1 -> 4 -> 99."""

#source: https://www.techiedelight.com/merge-sort-singly-linked-list/

# A linked list node
class Node:
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next

def printList(head):

	ptr = head
	while ptr:
		print(ptr.data, end=" -> ")
		ptr = ptr.next
	print("None")


def SortedMerge(a, b):

	# Base cases
	if a is None:
		return b
	elif b is None:
		return a

	# Pick either a or b, and recur
	if a.data <= b.data:
		result = a
		result.next = SortedMerge(a.next, b)
	else:
		result = b
		result.next = SortedMerge(a, b.next)

	return result


def FrontBackSplit(source):

	# if length is less than 2, handle separately
	if source is None or source.next is None:
		return source, None

	(slow, fast) = (source, source.next)

	# Advance 'fast' two nodes, and advance 'slow' one node
	while fast:

		fast = fast.next
		if fast:
			slow = slow.next
			fast = fast.next

	# 'slow' is before the midpoint the list, so split it in two
	# at that point.
	ret = (source, slow.next)
	slow.next = None

	return ret


# Sort given linked list using Merge sort algorithm
def MergeSort(head):

	# Base case -- length 0 or 1
	if head is None or head.next is None:
		return head

	# Split head into 'a' and 'b' sublists
	front, back = FrontBackSplit(head)

	# Recursively sort the sublists
	front = MergeSort(front)
	back = MergeSort(back)

	# answer = merge the two sorted lists together
	return SortedMerge(front, back)


# Sort given linked list using Merge sort algorithm
if __name__ == '__main__':

	# input keys
	keys = [8, 6, 4, 9, 3, 1]

	head = None
	for key in keys:
		head = Node(key, head)

	# sort the list
	head = MergeSort(head)

	# print the sorted list
	printList(head)


            