from SQS_Operation import read_messages_from_queue
from DatabaseOperations import create_table

if __name__ == '__main__':
    # First, create the table
    create_table()
    # Then, read messages from the queue
    read_messages_from_queue()
