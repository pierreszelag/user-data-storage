from user import User

existing_nodes=[]

class Node:
    def __init__(self, idNode, capacity, nodeList=[], dataList=[]):
        self.idNode = idNode
        self.capacity = capacity
        
        if dataList == []:
            self.dataList = []
        else :
            self.dataList = dataList
        
        if nodeList == []:
            self.nodeList = []
        else :
            self.nodeList = nodeList
        
        self.nodeList = self.nodeList
        
        for n in existing_nodes:
            for h in self.nodeList:
                if h[0] == n:
                    n.nodeList.append([self,h[1]])
        
        existing_nodes.append(self)

    
    def free_space(self):
        """
        this method return free space of a node
        """
        usage = 0
        for d in self.dataList:
            usage += d.size
        return self.capacity - usage
    
    def nodeList_without_user(self):
        """
        this method return the nodeList of the the node without any user
        """
        nlwu = []
        for n in self.nodeList:
            if type(n[0]) is Node:
                nlwu.append(n)
        return nlwu
    
    def attached_user(self):
        """
        this method return the attached user of a node if it has one
        """
        for n in self.nodeList:
            if type(n[0]) is User:
                return n
        return None
    
    
    def arrange_node(self):
        """
        this method return the nodeList of the the node without any user
        and sorted by increasing idNode
        """
        idList = []
        arrangedNode = []
        for n in self.nodeList_without_user():
            idList.append(n[0].idNode)
        idList.sort()
        for i in idList:
            for n in self.nodeList:
                if i == n[0].idNode:
                    arrangedNode.append(n)
        return arrangedNode
    
    
    def get_node_with_id(self, numb):
        """
        this method takes an node id in parameter and return the corresponding node
        """
        for n in (self.nodeList_without_user() + [[self,0]]):
            if n[0].idNode == numb:
                return n[0]
    
    
    def time_to_node(self, target_id_node, visited_nodes=[], nodes_to_visit=[], time=0, max_time=None):
        """
        this method takes a target node id in parameter and return the time to get to
        the target node from the node
        
        this method is recursive and can also be called by the time_to_node method in
        the user class
        """
        if not len(nodes_to_visit) == 0:
            del nodes_to_visit[0]
        
        if self.idNode == target_id_node:
            if max_time == None:
                max_time = time
            elif time < max_time:
                max_time = time
            
        
        visited_nodes.append(self)
        
        for n in self.nodeList_without_user():
            if not n[0] in visited_nodes:
                nodes_to_visit.append([n[0], time + n[1]])

        if len(nodes_to_visit) == 0:
            return max_time
        
        return nodes_to_visit[0][0].time_to_node(target_id_node, visited_nodes, nodes_to_visit, nodes_to_visit[0][1], max_time)
            
            
            
            
            
            
            
            
                