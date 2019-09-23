"""
Design a HashSet without using any built-in hash table libraries.

To be specific, your design should include these functions:

add(value): Insert a value into the HashSet.
contains(value) : Return whether the value exists in the HashSet or not.
remove(value): Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.

Example:
    MyHashSet hashSet = new MyHashSet();
    hashSet.add(1);
    hashSet.add(2);
    hashSet.contains(1);    // returns true
    hashSet.contains(3);    // returns false (not found)
    hashSet.add(2);
    hashSet.contains(2);    // returns true
    hashSet.remove(2);
    hashSet.contains(2);    // returns false (already removed)

Note:
    All values will be in the range of [0, 1000000].
    The number of operations will be in the range of [1, 10000].
    Please do not use the built-in HashSet library.
"""

# Time Limit Exceeded
"""
class MyHashSet(object):

    def __init__(self):
        self.data = [None] * 5000
        self.length = 5000
        self.num_of_data = 0


    def add(self, key):

        if float((self.num_of_data + 1)) / float(self.length) > 0.7:
            self.data = self.data + [None] * self.length
            self.length *= 2

        index = key % 5000

        if self.data[index] == None:
            self.data[index] = key
            self.num_of_data += 1
        else:
            if self.data[index] != key:
                is_exist = False
                # check if the key is already in the hashset
                for i in range(index + 1, self.length):
                    if self.data[i] == key:
                        is_exist = True
                # if the key is not in the hashset, store it in the next empty position
                if is_exist == False:
                    for i in range(index + 1, self.length):
                        if self.data[i] == None:
                            self.data[i] = key
                            self.num_of_data += 1
                            break


    def remove(self, key):
        index = key % 5000
        for i in range(index, self.length):
            if self.data[i] == key:
                self.data[i] = None
                self.num_of_data -= 1
                break


    def contains(self, key):
        print(self.data)
        is_exist = False
        index = key % 5000
        print(self.length)
        print(index)
        for i in range(index, self.length):
            if self.data[i] == key:
                is_exist = True
                print(i)
                break
        if is_exist:
            return True
        else:
            return False

"""
"""
hashSet = MyHashSet()
hashSet.add(1)
hashSet.add(2)
print(hashSet.contains(1))    # returns true
print(hashSet.contains(3))    # returns false (not found)
hashSet.add(2)
print(hashSet.contains(2))   # returns true
hashSet.remove(2)
print(hashSet.contains(2))    # returns false (already removed)
"""

#output =   "null,null,false,null,true,null,null,true,null,null,null,null,null,null,true,null,null,null,true,null,false,true,null,null,null,null,null,null,null,true,null,null,true,null,null,null,null,null,true,null,true,null,null,null,null,null,null,false,null,null,false,null,null,false,null,null,null,null,true,null,true,true,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,false,null,null,null,null,null,null,null,null,null,false,null,null,null,null,null,null,null,null"
#excepted = "null,null,false,null,true,null,null,true,null,null,null,null,null,null,true,null,null,null,true,null,false,true,null,null,null,null,null,null,null,true,null,null,true,null,null,null,null,null,true,null,true,null,null,null,null,null,null,false,null,null,false,null,null,false,null,null,null,null,true,null,true,true,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,true,null,null,null,null,null,null,null,null,null,false,null,null,null,null,null,null,null,null"

output = "null,null,null,null,null,false,null,null,null,null,false,null,null,null,null,null,null,null,null,null,null,null,null,true,null,null,null,null,null,null,null,null,null,null,null,null,null,null,false,true,null,null,null,null,null,null,null,true,true,null,null,null,null,null,null,true,null,null,null,null,null,null,null,null,null,null,null,false,null,null,null,null,null,null,null,null,true,null,null,null,null,null,null,null,true,false,null,null,true,null,null,null,null,null,true,true,null,null,null,null,null"
excepted = "null,null,null,null,null,false,null,null,null,null,false,null,null,null,null,null,null,null,null,null,null,null,null,true,null,null,null,null,null,null,null,null,null,null,null,null,null,null,false,true,null,null,null,null,null,null,null,true,true,null,null,null,null,null,null,true,null,null,null,null,null,null,null,null,null,null,null,false,null,null,null,null,null,null,null,null,true,null,null,null,null,null,null,null,true,false,null,null,false,null,null,null,null,null,true,true,null,null,null,null,null"
output = output.split(',')
excepted = excepted.split(',')




#operations =["MyHashSet","add","contains","add","contains","remove","add","contains","add","add","add","add","add","add","contains","add","add","add","contains","remove","contains","contains","add","remove","add","remove","add","remove","add","contains","add","add","contains","add","add","add","add","remove","contains","add","contains","add","add","add","remove","remove","add","contains","add","add","contains","remove","add","contains","add","remove","remove","add","contains","add","contains","contains","add","add","remove","remove","add","remove","add","add","add","add","add","add","remove","remove","add","remove","add","add","add","add","contains","add","remove","remove","remove","remove","add","add","add","add","contains","add","add","add","add","add","add","add","add"]
#parameters = [[],[58],[0],[14],[58],[91],[6],[58],[66],[51],[16],[40],[52],[48],[40],[42],[85],[36],[16],[0],[43],[6],[3],[25],[99],[66],[60],[58],[97],[3],[35],[65],[40],[41],[10],[37],[65],[37],[40],[28],[60],[30],[63],[76],[90],[3],[43],[81],[61],[39],[75],[10],[55],[92],[71],[2],[20],[7],[55],[88],[39],[97],[44],[1],[51],[89],[37],[19],[3],[13],[11],[68],[18],[17],[41],[87],[48],[43],[68],[80],[35],[2],[17],[71],[90],[83],[42],[88],[16],[37],[33],[66],[59],[6],[79],[77],[14],[69],[36],[21],[40]]

operations = ["MyHashSet","remove","remove","add","add","contains","add","add","add","remove","contains","add","add","add","remove","add","remove","add","add","add","remove","add","remove","contains","add","add","add","add","add","add","add","remove","remove","remove","add","add","remove","add","contains","contains","add","remove","add","add","add","add","add","contains","contains","add","add","add","add","add","remove","contains","remove","add","add","add","add","add","remove","add","add","add","add","contains","add","add","add","add","add","remove","add","add","contains","add","add","add","remove","remove","remove","remove","contains","contains","add","add","contains","add","add","add","add","add","contains","contains","add","remove","add","remove","add"]
parameters = [[],[88],[56],[17],[20],[83],[43],[27],[20],[21],[15],[90],[69],[95],[12],[60],[78],[94],[85],[70],[45],[84],[89],[17],[12],[47],[26],[90],[26],[63],[88],[83],[51],[10],[71],[85],[38],[1],[87],[27],[26],[30],[44],[39],[89],[54],[18],[84],[94],[63],[41],[77],[31],[9],[76],[85],[80],[6],[85],[13],[89],[49],[12],[35],[81],[32],[75],[48],[33],[33],[0],[6],[97],[3],[94],[90],[9],[87],[68],[32],[3],[85],[13],[89],[18],[78],[57],[47],[85],[94],[53],[14],[12],[62],[44],[31],[10],[69],[48],[38],[54]]

hashSet = None
for i in range(len(operations)):
    print(operations[i] + " " + str(parameters[i]))

    if operations[i] == "MyHashSet":
        hashSet = MyHashSet()
    elif operations[i] == "add":
        hashSet.add(parameters[i][0])
    elif operations[i] == "remove":
        hashSet.remove(parameters[i][0])
    elif operations[i] == "contains":
        print(hashSet.contains(parameters[i][0]))
        if output[i] != excepted[i]:

            print("error")
            print("output: " + output[i])
            print("excepted: " + excepted[i])
