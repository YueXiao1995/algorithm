"""
You have an array of logs.  Each log is a space delimited string of words.

For each log, the first word in each log is an alphanumeric identifier.  Then, either:

Each word after the identifier will consist only of lowercase letters, or;
Each word after the identifier will consist only of digits.
We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.

Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in their original order.

Return the final order of the logs.

Example 1:
    Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
    Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]

Constraints:
    0 <= logs.length <= 100
    3 <= logs[i].length <= 100
    logs[i] is guaranteed to have an identifier, and a word after the identifier.
"""

def reorderLogFiles(logs):
    # store all of the unique letter-logs and its identifiers into a dict
    letter_logs_identifier = dict()
    # store all of the digit logs into a list
    digit_logs = list()
    for log in logs:
        # get the identifier and the log content
        log = log.split(" ")
        identifier = log[0]
        log_content = (" ").join(log[1:])
        # check if it is a digit log
        if log[1].isdigit():
            digit_logs.append(identifier + " " + log_content)
        else:
            # check if the log_content is already in the dict
            if log_content not in letter_logs_identifier:
                letter_logs_identifier[log_content] = [identifier]
            else:
                letter_logs_identifier[log_content].append(identifier)
    # sort the letter_logs content, and sort their identifiers,
    # combine the identifier and log content to get the original log, and store them into a new list
    letter_logs = list()
    # sort the letter_logs content
    letter_logs_in_order = sorted(letter_logs_identifier.keys())
    for log in letter_logs_in_order:
        # sort the identifiers
        for identifier in sorted(letter_logs_identifier[log]):
            # get the original log, and store it
            letter_logs.append(identifier + " " + log)
    # generate a new list, where letter logs are in front of the digit logs
    return letter_logs + digit_logs

logs1 = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
logs2 = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","a2 act car"]
print(reorderLogFiles(logs2))
