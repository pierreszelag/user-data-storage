class User:
    def __init__(self, idUser, data=[], node=[]):
        self.idUser = idUser
        self.data = data
        self.node = node
        
        self.node[0].nodeList.append([self,self.node[1]])
        
        self.place_data()
        
    
    def arrange_data(self):
        """
        this method sort the data the user is interested in by increasing idData
        and return the arranged data list
        """
        idList = []
        arrangedData = []
        for d in self.data:
            idList.append(d.idData)
        idList.sort()
        for i in idList:
            for d in self.data:
                if i == d.idData:
                    arrangedData.append(d)
        return arrangedData
        
    
    def time_to_node(self, target_node):
        """
        this method takes a target node id in parameter and return the time to get to
        the node from the user
        """
        return self.node[0].time_to_node(target_node,[],[], self.node[1])
    
    def closest_node_list(self):
        """
        this method return the sorted list of closest node for the user
        """
        nodes = self.node[0].nodeList_without_user()
        table = []
        closest = []
        
        for n in nodes:
            table.append(self.time_to_node(n[0].idNode))
        table.sort()
        
        for i in range(len(table)):
            for n in nodes:
                if self.time_to_node(n[0].idNode) == table[i]:
                    closest.append(n[0])

        return [self.node[0]] + closest
                
    
    def node_list_with_id(self):
        """
        this method return a list of size 2 lists within wich there is a node and its id
        """
        nodeID_list = []
        nodes = [self.node[0]]
        res = []
        
        for n in self.node[0].nodeList_without_user():
            nodes.append(n[0])
            
        for n in nodes:
            nodeID_list.append(n.idNode)
            
        for i in range(len(nodeID_list)):
            res.append([nodeID_list[i],nodes[i]])
            
        return res
    
    def meeting_point(self, user, data_size):
        """
        this method takes an user and a data size in parameter and return the
        node with enough free space and with the shortest time for both users
        """
        table1 = []
        table2 = []
        id_table = []
        nodes = self.node_list_with_id()
        #------------------------#creation of table3
        for n in range(len(nodes)):
            if nodes[n][1].free_space() >= data_size:
                table1.append(self.time_to_node(nodes[n][1].idNode))
                table2.append(user.time_to_node(nodes[n][1].idNode))
                id_table.append(n)
        table3 = []
        for i in range(len(table1)):
            table3.append(table1[i] + table2[i])
        #------------------------#
        #------------------------#check if there is occurences
        minimum = min(table3)
        occurences = []
        for i in range(len(table3)):
            if table3[i] == minimum:
                occurences.append(id_table[i])
        diff_min = [0,9999999]
        #------------------------#
        #------------------------#if there is multiple occurences, find the best track
        if len(occurences) != 1:
            for i in occurences:
                if abs(table1[i] - table2[i]) < diff_min[1]:
                    diff_min = [i,abs(table1[i] - table2[i])]
            res = diff_min[0]
        else:
            res = occurences[0]
        #------------------------#
        return self.node[0].get_node_with_id(res)
        
    
    def place_data(self):
        """
        this method place all the data in the list of the user in oreder that the data
        is the closest to the user
        """
        arrangedData = self.arrange_data()
        for d in arrangedData:
            if d.nodeLocation != None:
                pass
            else:
                for n in self.closest_node_list():
                    if d.size <= n.free_space():
                        n.dataList.append(d)
                        d.nodeLocation = n
                        break


