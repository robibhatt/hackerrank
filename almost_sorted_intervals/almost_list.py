class Min_max_struct:

    def __init__(self):
        self.total_intervals = 0
        self.max_list = []
        self.min_list = []

    def insert(self, key):
        if len(self.min_list) == 0:
            self.max_list.append((key, 0))
            self.min_list.append(key)
        else:
            last = self.min_list[-1]
            if key > last:
                added_intervals = 1
                done = False
                while not done:
                    if len(self.max_list) == 0:
                        self.max_list.append((key, len(self.min_list)))
                        self.min_list.append(key)
                        done = True
                    else:
                        (value, intervals) = self.max_list[-1]
                        if value < key:
                            added_intervals += intervals
                            self.max_list.pop()
                        else:
                            self.max_list.append((key,added_intervals))
                            self.min_list.append(key)
                            done = True
                self.total_intervals += added_intervals
            else:
                self.min_list.pop()
                max_list_index = len(self.max_list) - 1
                done = False
                def reduce_max_list_intervals(index):
                    (value, intervals) = self.max_list[index]
                    if intervals > 0:
                        self.max_list[index] = (value, intervals - 1)
                        return index
                    else:
                        return reduce_max_list_intervals(index - 1)
                while not done:
                    if len(self.min_list) == 0:
                        self.min_list.append(key)
                        self.max_list.append((key, 0))
                        done = True
                    else:
                        value = self.min_list[-1]
                        if value > key:
                            self.min_list.pop()
                            max_list_index = reduce_max_list_intervals(max_list_index)
                        else:
                            self.min_list.append(key)
                            self.max_list.append((key, 0))
                            done = True
                    

struct = Min_max_struct()
N = int(raw_input())
raw_list = raw_input()
for x in raw_list.split(' '):
    struct.insert(int(x))
print (struct.total_intervals + N)

    
                                              
        

            
        
        

        
        
        
        
            
        


    
