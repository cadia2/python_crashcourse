def  show_messages(messages):
    '''Print messages in the list'''
    for message in messages:
        msg = f'{message}'
        print(msg)

message_list = ['one','two','three']
show_messages(message_list)
