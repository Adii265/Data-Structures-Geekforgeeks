inorder = []
preorder = []
postorder = []
levelorder = []
class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None
	def insertNode(self,element):
		if(not(Node)):
			Node.data = int(element)
		if self.data > element:
			if self.left == None:
				self.left = Node(element)
			else:
				self.left.insertNode(element)
		else:
			if self.right == None:
				self.right = Node(element)
			else:
				self.right.insertNode(element)

	def InorderTraversal(self,Node):
		
		if(not(Node)):
			return
		self.InorderTraversal(Node.left)
		inorder.append(Node.data)
		self.InorderTraversal(Node.right)
		return inorder
	def PreOrderTraversal(self,Node):
		if(not(Node)):
			return
		preorder.append(Node.data)
		self.PreOrderTraversal(Node.left)
		self.PreOrderTraversal(Node.right)
		return preorder
	def PostOrderTraversal(self,Node):
		if(not(Node)):
			return
		self.PostOrderTraversal(Node.left)
		self.PostOrderTraversal(Node.right)
		postorder.append(Node.data)
		return postorder
	def LevelOrderTraversal(self,Node):
		h = self.FindHeight(Node)
		for i in range(1,h+1):
			a = self.LevelOrderCall(Node,i)
		return a
	def LevelOrderCall(self,Node,level):
		if Node == None:
			return 
		if level == 1:
			levelorder.append(Node.data)
		else:
			self.LevelOrderCall(Node.left,level-1)
			self.LevelOrderCall(Node.right,level-1)		
		return levelorder	
	
	def FindMaxElement(self,Node):
		if not(Node):
			return
		else:
			maximum = Node.data
			return(max(maximum,max(self.FindMaxElement(Node.left),self.FindMaxElement(Node.right))))		
		
	def SearchAnElement(self,Node,element):
		if(not(Node)):
			return 0	
		if Node.data == element:
			return 1
		else:
			l = self.SearchAnElement(Node.left,element)
			r = self.SearchAnElement(Node.right,element)
		return l or r
		
	def FindHeight(self,Node):
		if Node == None:
			return 0
		else:
			return(max(self.FindHeight(Node.left),self.FindHeight(Node.right))+1)
	
	def FindSize(self,Node):
		if Node == None:
			return 0
		else:
			return(self.FindSize(Node.left)+self.FindSize(Node.right)+1)		

	def DeleteTree(self,Node):
		if Node == None:
			return
		else:
			self.DeleteTree(Node.left)
			self.DeleteTree(Node.right)
			print(Node.data)
	def deepestNode(self,Node):
		if Node == None:
			return
		else:
			a = self.LevelOrderTraversal(Node)
			return a[-1]
			
	def sumofElements(self,Node):
		if Node == None:
			return 0
		else:
			return sum(inorder)
		
	def NoofFullNodes(self,Node,count):
		
		if Node == None:
			return
		else:
			if Node.left and Node.right:
				count = count+1
				print(Node.data,count)
				self.NoofFullNodes(Node.left,count)
				self.NoofFullNodes(Node.right,count)
			return count
		

	def NoofHalfNodes(Self,Node):
		pass

	def StructurallyIdentical(self,Node1,Node2):
		pass

	def Diameter(self,Node):
		pass

	def LevelWithMaxSum(self,Node):
		pass

	def RoottoLeafPath(self,Node):
		pass

	#Check if a path exist for given sum
	def  pathwithSum(self,Node):
		pass
	
	def Mirror(self,Node):
		pass
	
	def CheckMirror(self,Node1,Node2):
		pass

	def LCA(self,Node,e1,e2):
		pass  
		
	#Create a binary tree using preorder traversal and inorder traversal
	def InPre(self,Node,i,p):
		pass
	
	def AllAncestors(self,Node,e):
		pass
	
	def ZigZagTraversal(self,Node):
		pass

	def VerticalSum(self,Node):
		pass
	
	




root = Node(27)
root.left = Node(2) 
root.right = Node(3)
root.left.left = Node(4)
root.left.left.right = Node(45)
root.left.left.right.left = Node(32)
root.right.left = Node(5)
root.right.right = Node(8) 
root.right.left.left = Node(6)
root.right.left.right = Node(7)
root.right.right.left = Node(9)
root.right.right.right = Node(10)
'''
print("Inorder")
root.InorderTraversal(root)
print(inorder)

print("PreOrder")
root.PreOrderTraversal(root)
print(preorder)

print("PostOrder")
root.PostOrderTraversal(root)
print(postorder)

print("LevelOrder")
print(root.LevelOrderTraversal(root))

print("Max Element of the tree ",root.FindMaxElement(root))


ele = int(raw_input("Enter element to be searched"))
if root.SearchAnElement(root,ele) == 1:
	print("Found")
else:
	print("Not Found")

print("Height of the tree is ",root.FindHeight(root))

print("Size of the Binary Tree ",root.FindSize(root))


print("Deepest Node ",root.deepestNode(root))

print("Sum of elements",root.sumofElements(root))
'''

print("Number of FullNodes", root.NoofFullNodes(root,0))








'''
root.DeleteTree(root)
root = None
print("Tree deleted")'''

