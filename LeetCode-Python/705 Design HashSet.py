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
class MyHashSet(object):

    def __init__(self):
        self.mod = 100000
        self.data = [None] * 100000
        self.num_of_keys = 0
        """
        Initialize your data structure here.
        """

    def add(self, key):
        # calculate the hash code to find the index
        index = key % self.mod
        # check if the place is empty
        if self.data[index] == None:
            self.data[index] = key
            self.num_of_keys += 1
        # move to find another empty place
        else:
            while True:
                index += 1
                if self.data[index % len(self.data)] == None:
                    self.data[index % len(self.data)] = key
                    self.num_of_keys += 1
                    break


        # check if the data list big enough, if not, resize it
        if self.num_of_keys/len(self.data) > 0.75:
            self.data.extend([None] * len(self.data))
        """
        :type key: int
        :rtype: None
        """

    def remove(self, key):
        # calculate the hash code to find the index
        index = key % self.mod
        # check if the place is empty
        if self.data[index] == key:
            self.data[index] = None
            self.num_of_keys -= 1
        # move to find another empty place
        elif self.data[index] != None:
            while True:
                index += 1
                if self.data[index % len(self.data)] == key:
                    self.data[index % len(self.data)] = None
                    self.num_of_keys -= 1
                    break
                elif self.data[index % len(self.data)] == None:
                    break

        """
        :type key: int
        :rtype: None
        """

    def contains(self, key):
        # calculate the hash code to find the index
        index = key % self.mod
        # check if the place is empty
        if self.data[index] == key:
            return True
        # move to find another empty place
        elif self.data[index] != None:
            while True:
                index += 1
                if self.data[index % len(self.data)] == key:
                    return True

                elif self.data[index % len(self.data)] == None:
                    return False
        else:
            return False


output = "null,null,null,null,null,false,null,null,null,null,false,null,null,null,null,null,null,null,null,null,null,null,null,true,null,null,null,null,null,null,null,null,null,null,null,null,null,null,false,true,null,null,null,null,null,null,null,true,true,null,null,null,null,null,null,true,null,null,null,null,null,null,null,null,null,null,null,false,null,null,null,null,null,null,null,null,true,null,null,null,null,null,null,null,true,false,null,null,true,null,null,null,null,null,true,true,null,null,null,null,null"
excepted = "null,null,null,null,null,false,null,null,null,null,false,null,null,null,null,null,null,null,null,null,null,null,null,true,null,null,null,null,null,null,null,null,null,null,null,null,null,null,false,true,null,null,null,null,null,null,null,true,true,null,null,null,null,null,null,true,null,null,null,null,null,null,null,null,null,null,null,false,null,null,null,null,null,null,null,null,true,null,null,null,null,null,null,null,true,false,null,null,false,null,null,null,null,null,true,true,null,null,null,null,null"
output = output.split(',')
excepted = excepted.split(',')






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

# The HashSet capacity is doubled when the load factor (0.75) is reached.
