from data import Data
from user import User
from node import Node


data0 = Data(0,100)
data1 = Data(1,50)
data2 = Data(2,30)
data3 = Data(3,70)
data4 = Data(4,20)
data5 = Data(5,25)
data6 = Data(6,5)

node0 = Node(0,100)
node1 = Node(1,40,[[node0,7]])
node2 = Node(2,150,[[node0,1],[node1,4]])
node3 = Node(3,75,[[node0,5],[node1,3],[node2,2]])
node4 = Node(4,30,[[node0,2],[node1,2],[node2,8],[node3,1]])

user0 = User(0,[data0,data1,data5],[node0,2])
user1 = User(1,[data2,data4],[node1,3])
user2 = User(2,[data3],[node2,1])
