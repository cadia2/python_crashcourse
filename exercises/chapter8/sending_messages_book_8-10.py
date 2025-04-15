
#def send_messages(message_list, send_messages_list):
    #'''Print messages in the list'''
    #while message_list:
        #send_messages_list.append(message_list.pop())
    #for message in send_messages_list[::-1]:
        #print(message)
#
#send_messages_list  = []
#message_list = ['one','two','three']
#send_messages(message_list, send_messages_list)
#
#send_messages_list.reverse()
#
#print(send_messages_list)
#print(message_list)


def  show_messages(messages):
    '''Print messages in the list'''
    for message in messages:
        msg = f'{message}'
        print(msg)

def sent_messages(messages,empty_messages):
    '''moves messages'''
    while messages:
        message = messages.pop()
        empty_messages.append(message)
        print(message)

empty_message_list = []
message_list = ['one','two','three']
show_messages(message_list)
sent_messages(message_list,empty_message_list)

print('lists')
print(f'empty message list: {empty_message_list}')
print(message_list)
