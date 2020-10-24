import csv

class Node:
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.next = None
		
class OrderedDictionary:
	def __init__(self):
		self.head = None
		
	def ordered_insert(self, key, value):
		new_node = Node(key, value)
		
		if self.head is None:
			self.head = new_node
			return
			
		temp = self.head
		if value >= temp.value:
			new_node.next = temp
			self.head = new_node
			return
		
		while temp.next:
			if value < temp.value and value >= temp.next.value:
				new_temp = temp.next
				temp.next = new_node
				new_node.next = new_temp
				return
			temp = temp.next
			
		new_node.next = temp.next
		temp.next = new_node
	
	def display_list(self):
		temp = self.head
		print('{:15s} | {:15s}'.format('Address','Frequency'))
		while temp is not None:
			print('{:15s} | {:15d}'.format(temp.key, temp.value))
			temp = temp.next
	
	def to_csv_file(self):
		temp = self.head
		with open('frequency_results.csv', mode='w', newline='') as result_file:
			csv_writer = csv.writer(result_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
			csv_writer.writerow(['Address', 'Frequency'])
			while temp is not None:
				cssv_writer.writerow([temp.key, temp.value])
				temp = temp.next
			
# Examples of use
#ordered_data = OrderedDictionary()
#ordered_data.ordered_insert('74.53.124.654', 1)
#ordered_data.ordered_insert('74.56.24.654', 1)
#ordered_data.ordered_insert('74.53.14.654', 2)
#ordered_data.ordered_insert('74.56.12.154', 1)
#ordered_data.ordered_insert('74.53.124.154', 1)
#ordered_data.ordered_insert('74.53.124.554', 4)
#ordered_data.ordered_insert('74.53.14.754', 6)
#ordered_data.ordered_insert('74.53.12.654', 3)
#ordered_data.display_list()
