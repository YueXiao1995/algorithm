"""
A transaction is possibly invalid if:
    the amount exceeds $1000, or;
    if it occurs within (and including) 60 minutes of another transaction with the same name in a different city.

Each transaction string transactions[i] consists of comma separated values representing the name, time (in minutes), amount, and city of the transaction.

Given a list of transactions, return a list of transactions that are possibly invalid.  You may return the answer in any order.


Example 1:
    Input: transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
    Output: ["alice,20,800,mtv","alice,50,100,beijing"]
    Explanation: The first transaction is invalid because the second transaction occurs within a difference of 60 minutes, have the same name and is in a different city. Similarly the second one is invalid too.

Example 2:
    Input: transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
    Output: ["alice,50,1200,mtv"]

Example 3:
    Input: transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
    Output: ["bob,50,1200,mtv"]

Constraints:

transactions.length <= 1000
Each transactions[i] takes the form "{name},{time},{amount},{city}"
Each {name} and {city} consist of lowercase English letters, and have lengths between 1 and 10.
Each {time} consist of digits, and represent an integer between 0 and 1000.
Each {amount} consist of digits, and represent an integer between 0 and 2000
"""

def invalidTransactions(transactions):
    transactions_list = list()
    invalid_transactions = list()
    for t in transactions:
        if len(t) > 1000:
            invalid_transactions.append(t)
            continue
        t_list = t.split(",")
        transactions_list.append(t_list)
        try:
            int(t_list[1])
            if int(t_list[1]) < 0 or int(t_list[1]) > 1000:
                invalid_transactions.append(t)
                continue
        except ValueError:
            invalid_transactions.append(t)
            continue
        try:
            int(t_list[2])
            if int(t_list[2]) < 0 or int(t_list[2]) > 1000:
                invalid_transactions.append(t)
                continue
        except ValueError:
            invalid_transactions.append(t)
            continue
        try:
            int(t_list[0])
            invalid_transactions.append(t)
            continue
        except ValueError:
            if not t_list[0].islower() or len(t_list[0]) < 1 or len(t_list[0]) > 10:
                invalid_transactions.append(t)
                continue
        try:
            int(t_list[3])
            invalid_transactions.append(t)
            continue
        except ValueError:
            if not t_list[3].islower() or len(t_list[3]) < 1 or len(t_list[3]) > 10:
                invalid_transactions.append(t)
                continue
    data = dict()
    for t in transactions_list:
        if t[0] in data:
            for i in range(0, len(data[t[0]]['city'])):
                if t[3] != data[t[0]]['city'][i] and abs(int(data[t[0]]['time'][i]) - int(t[1])) <= 60:
                    if ','.join(t) not in invalid_transactions:
                        invalid_transactions.append(','.join(t))
                    old_transaction = ','.join([t[0], data[t[0]]['time'][i], data[t[0]]['amount'][i], data[t[0]]['city'][i]])
                    if old_transaction not in invalid_transactions:
                        invalid_transactions.append(old_transaction)
            data[t[0]]['time'].append(t[1])
            data[t[0]]['amount'].append(t[2])
            data[t[0]]['city'].append(t[3])
        else:
            data[t[0]] = {'time': [t[1]],'amount':[t[2]], 'city': [t[3]]}
    return invalid_transactions


transactions1 = ["alice,20,800,mtv","alice,50,100,beijing"]
transactions2 = ["alice,20,800,mtv","alice,50,1200,mtv"]
transactions3 = ["alice,20,800,mtv","bob,50,1200,mtv"]
transactions4 = ["bob,689,1910,barcelona","alex,696,122,bangkok","bob,832,1726,barcelona","bob,820,596,bangkok","chalicefy,217,669,barcelona","bob,175,221,amsterdam"]

transactions5 = ["bob,627,1973,amsterdam","alex,387,885,bangkok","alex,355,1029,barcelona","alex,587,402,bangkok","chalicefy,973,830,barcelona","alex,932,86,bangkok","bob,188,989,amsterdam"]
transactions6 = ["xnova,261,1949,chicago","bob,206,1284,chicago","xnova,420,996,bangkok","chalicefy,704,1269,chicago","iris,124,329,bangkok","xnova,791,700,amsterdam","chalicefy,572,697,budapest","chalicefy,231,310,chicago","chalicefy,763,857,chicago","maybe,837,198,amsterdam","lee,99,940,bangkok","bob,132,1219,barcelona","lee,69,857,barcelona","lee,607,275,budapest","chalicefy,709,1171,amsterdam"]

print(invalidTransactions(transactions6))



