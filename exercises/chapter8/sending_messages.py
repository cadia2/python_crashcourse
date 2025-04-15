
def send_messages(message_list):
    '''Print messages in the list'''
    while message_list:
        message = message_list.pop()
        print(message)
        send_messages_list.append(message)

send_messages_list  = []
message_list = ['one','two','three']
send_messages(message_list)

send_messages_list.reverse()

print('Lists')
print(send_messages_list)
print(message_list)
