"""
You are given a data structure of employee information, which includes the employee's unique id, his importance value and his direct subordinates' id.

For example, employee 1 is the leader of employee 2, and employee 2 is the leader of employee 3. They have importance value 15, 10 and 5, respectively. Then employee 1 has a data structure like [1, 15, [2]], and employee 2 has [2, 10, [3]], and employee 3 has [3, 5, []]. Note that although employee 3 is also a subordinate of employee 1, the relationship is not direct.

Now given the employee information of a company, and an employee id, you need to return the total importance value of this employee and all his subordinates.

Example 1:
    Input: [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1
    Output: 11
    Explanation:
    Employee 1 has importance value 5, and he has two direct subordinates: employee 2 and employee 3. They both have importance value 3. So the total importance value of employee 1 is 5 + 3 + 3 = 11.

Note:
    One employee has at most one direct leader and may have several subordinates.
    The maximum number of employees won't exceed 2000.
"""
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates

def getImportance(employees, id):
    # store the important values and subordinates list into two separate dict. and use the id as key
    values_dict = dict()
    subordinates_dict = dict()
    for employee in employees:
        values_dict[employee.id] = employee.importance
        subordinates_dict[employee.id] = employee.subordinates
    # record the total important value of target employee and its subordinates
    total_value = values_dict[id]
    # maintain a subordinates list
    subordinates_list = subordinates_dict[id]
    # check if the subordinates list is empty
    while len(subordinates_list) != 0:
        # maintain a list to store the direct subordinates of the direct subordinates
        new_subordinates = list()
        # iterate the subordinate list
        for subordinate in subordinates_list:
            # update the total important value
            total_value += values_dict[subordinate]
            # append the subordinates of the subordinate to the new list
            new_subordinates += subordinates_dict[subordinate]
        # update the subordinates list
        subordinates_list = new_subordinates
    return total_value

employee1 = Employee(1, 5, [2, 3])
employee2 = Employee(2, 3, [])
employee3 = Employee(3, 3, [])

employees1 = [employee1, employee2, employee3]
id1 = 1
print(getImportance(employees1, id1))
