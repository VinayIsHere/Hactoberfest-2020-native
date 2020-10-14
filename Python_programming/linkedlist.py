#!/usr/bin/python3
class Node:
	def __init__(self,val):
		self.val=val
		self.next=None
	

class linkedList:
	def __init__(self):
		self.head=None
		
	def show(self):
		temp=self.head
		while(temp):
			print(temp.val)
			temp=temp.next
			
	def sum(self):
		temp=self.head
		sumOfNodes=0
		while(temp):
			sumOfNodes+=temp.val
			temp=temp.next
		return sumOfNodes
		
if __name__=='__main__':
	
	llist=linkedList()
	
	firstNode=Node(1)
	secondNode=Node(2)
	thirdNode=Node(3)
	
	firstNode.next=secondNode
	secondNode.next=thirdNod	e
	thirdNode.next=None
	
	llist=linkedList()
	llist.head=firstNode
	
	print("sum of elements: ",llist.sum())
