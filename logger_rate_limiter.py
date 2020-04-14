# a double linked lists
class Nodes(object):
    def __init__(self, message_value, printed_time):
        self.message_value = message_value
        self.printed_time = printed_time
        self.next = None
        self.prev = None
class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = None # a root for linkedlist that at most have 10 nodes

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """

        if self.root is None:
            self.root = Nodes(message, timestamp)
            return True
        else:
            pointer = self.root
            while pointer is not None:
                if timestamp - pointer.printed_time  >= 10:
                    if pointer.prev is None:
                        self.root = Nodes(message, timestamp)
                    else:
                        prev_pointer = pointer.prev
                        prev_pointer.next = None
                        new_root = Nodes(message, timestamp)
                        new_root.next = self.root
                        self.root.prev = new_root
                        self.root = new_root
                    del pointer
                    return True
                else:
                    if pointer.message_value == message:
                        return False
                    else:
                        pointer = pointer.next

        new_root = Nodes(message, timestamp)
        new_root.next = self.root
        self.root.prev = new_root
        self.root = new_root
        return True

actions = ["shouldPrintMessage","shouldPrintMessage","shouldPrintMessage","shouldPrintMessage","shouldPrintMessage","shouldPrintMessage"]
inputs = [[1,"foo"],[2,"bar"],[3,"foo"],[8,"bar"],[10,"foo"],[11,"foo"]]
logger = Logger()
for a_index in range(len(actions)):
    print(logger.shouldPrintMessage(inputs[a_index][0],inputs[a_index][1]))
