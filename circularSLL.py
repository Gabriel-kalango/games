class Node:
    def __init__(self,value=None) :
        self.value=value
        self.next=None
    
class cSLinkedlist:
    def __init__(self) :
        self.head=None
        self.tail=None
    def __iter__(self):
        node=self.head
        while node:
            yield node
            if node.next==self.head:
                break
            node=node.next
    def createCSLL(self,nodeValue):
        node=Node(nodeValue)
        node.next=node
        self.head=node
        self.tail=node
    def insertSCLL(self,nodeValue,location):
        if self.head is None:
            return "CSLL doesnt exist"
        else:
            node=Node(nodeValue)
            if location==0:
                node.next=self.head
                self.head=node
                self.tail.next=node
            elif location==1:
                node.next=self.tail.next

                self.tail.next=node
                self.tail=node
            else:
                tempnode=self.head
                index=0
                while index< location-1:
                    tempnode=tempnode.next
                    index+=1
                nextnode=tempnode.next
                tempnode.next=node
                node.next=nextnode
    def traverseCSLL(self):
        if self.head is None:
            print("doesnt exist")
        else:
            tempnode=self.head
            while self.head is not None:
                print(tempnode.value)
                tempnode=tempnode.next
                if tempnode==self.tail.next:
                    break
    def searchSCLL(self,nodevalue):
        if self.head is None:
            return "the linked list doesnt exixt"                
        else:
            tempnode=self.head
            while self.head is not None:
                if tempnode.value==nodevalue:
                    return tempnode.value
                tempnode=tempnode.next
                if tempnode==self.tail.next:
                    return "the node is not in this list"


    def deleteSCLL(self,location):
        if self.head is None:
            return "the linked list doesnt exist"
        else:
            if location==0:
                if self.head.next==self.head:
                    self.head.next=None
                    self.head=None
                    self.tail=None
                else:
                    self.head =self.head.next
                    self.tail.next=self.head
            elif location==1:
                if self.tail==self.head:
                    self.head.next=None
                    self.head=None
                    self.tail=None
                else:
                    node=self.head
                    while self.head is not None:
                        if node.next==self.tail:
                            break
                        node=node.next
                    node.next=self.head
                    self.tail=node
            else:
                tempnode=self.head
                index=0
                while index<location-1:
                    tempnode=tempnode.next
                    index+=1
                nextnode=tempnode.next
                tempnode.next=nextnode.next

    def deleteEntireCSLL(self):

        self.head=None
        self.tail.next=None
        self.tail=None
        







CSlinked=cSLinkedlist()
CSlinked.createCSLL(2)
CSlinked.insertSCLL(6,1)
CSlinked.insertSCLL(5,1)
CSlinked.insertSCLL(3,2)
CSlinked.insertSCLL(3,0)
#CSlinked.traverseCSLL()
#print(CSlinked.searchSCLL(2))
print([node.value for node in CSlinked])
CSlinked.deleteEntireCSLL()
print([node.value for node in CSlinked])
