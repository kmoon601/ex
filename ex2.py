class Set:
    def __init__(self, value = []):    # Constructor
        self.data = []                 # Manages a list
        self.concat(value)

    def intersection(self, other):        # other is any sequence
        res = []                       # self is the subject
        for x in self.data:
            if x in other:             # Pick common items
                res.append(x)
        return Set(res)                # Return a new Set

    def union(self, other):            # other is any sequence
        res = self.data[:]             # Copy of my list
        for x in other:                # Add items in other
            if not x in res:
                res.append(x)
        return Set(res)

    def concat(self, value):
        for x in value:                
            
            if not x in self.data:     # Removes duplicates
                self.data.append(x)

    def __len__(self):          return len(self.data)        # len(self)
    def __getitem__(self, key): return self.data[key]        # self[i], self[i:j]
    def __and__(self, other):   return self.intersection(other) # self & other
    def __or__(self, other):    return self.union(other)     # self | other
    def __repr__(self):         return 'Set({})'.format(repr(self.data))  
    def __iter__(self):         return iter(self.data)       # for x in self:  
    def __le__(self, other):    return self.issubset(other)                     
    def __lt__(self, other):    return self.issubset(other)
    def __ge__(self, other):    return self.issuperset(other)
    def __gt__(self, other):    return self.issuperset(other)
    def __ior__(self, other):   return self.issuperset(other)
    
    
    def issubset(self, other):
        sub = self.intersection(other)
        if self.data == sub.data:
            return print('x<=y')
        elif self.data in sub.data and self.data != sub.data: 
            return print('x<y')
        else: 
            return print('not subset')
        
    def issuperset(self,other): 
        superset = other.intersection(self)
        if other.data == superset.data:
            return print('x>=y')
        elif other.data in superset.data and other.data != superset.data: 
            return print('x>y')
        else: 
            return print('not superset')
        
            
    
    def intersection_update(self,other):                                      
        result = []                      
        for x in self.data:
            if x in other.data:             
                result.append(x)
        return result             

                    
    def difference_update(self,other): 
        for x in self.data:
            if x in other.data:             
                self.data.remove(x)
        return self.data 
    
    def symmetric_difference_update(self,other):
        u= self.data + other.data
        dif= self.intersection(other)
        sym=[]
        for x in u:
            if x not in dif:
                sym.append(x)
        return sym
    
    def add(self, other):
        adder = []
        for x in other.data:
            if not x in self.data:
                adder.append(x)
        a=self.data + adder
        return a
          
    def remove(self, other):
        for x in self.data:
            if x in other.data:
                self.data.remove(x)
        return self.data
               
    
x = Set([2,1,2,6,7,8])
y = Set([2,3,4,5,6])

print(x, y, len(x))
print(x.intersection(y), y.union(x))
print(x & y, x | y)

print(x[2], y[:2])
for element in x:
    print(element, end=' ')
print()
print(3 not in y)  # membership test
print(list(x))   # convert to list because x is iterable
print(x<=y)
print(x<y)
print(x>=y)
print(x>y)

print(x.intersection_update(y))
print(x.difference_update(y))
print(x.symmetric_difference_update(y))
print(x.add(y))
print(x.remove(y))

