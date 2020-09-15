from cryptography.fernet import Fernet
from symmetric import *

try:
    print('''
   ____________    _________     ____        ___  ______________     ___________     __      __     ____________     ______      ___
   |  ________/    |  _____ \    \   \      /  /  |   |_______ |    |____   ____|   |  |    |  |   / /        \ \   |      \     |  |
   | |             |  |    | |    \   \    /  /   |   |      | |        |   |       |  |    |  |   | |        | |   |   |\  \    |  |
   | |             |  |    | |     \   \  /  /    |   |______| |        |   |       |  |____|  |   | |        | |   |   | \  \   |  |
   | |             |  |____| |      \       /     |   |________|        |   |       |   ____   |   | |        | |   |   |  \  \  |  |
   | |             |  _____\ \       |     |      |   |                 |   |       |  |    |  |   | |        | |   |   |   \  \ |  |
   | |_________    |  |     \ \      |     |      |   |                 |   |       |  |    |  |   | |        | |   |   |    \  \|  |
   |__________/    |__|      \_\     |_____|      |___|                 |___|       |__|    |__|   \_\________/_/   |___|     \_____| 
                                                                                                                          By:Tech-Sec
    For more visit: https://github/Tech-Sec
    ''')
    print('''
        [1]Generate the keys    [2]Encrypt a file   [3]Decryption
    ''')
    while True:
        command = input('crypthon>')
        # generating key
        if command == '1':
            write_key()
            print('Want to encrypt a file?(y/n)')
            command_1 = input('crypthon>')
            if command_1 =='y':
                encrypt_file()
            elif command_1 == 'n':
                break
        # encryption
        elif command == '2':
            encrypt_file()
        # decryption
        elif command == '3':
            decrypt_file()
        else:
            print('Choose correct option!!')
        break
except FileNotFoundError:
    print('''
File not found
    ''')
except KeyboardInterrupt:
    print('''
   ____________    _________     ____        ___  ______________     ___________     __      __     ____________     ______      ___
   |  ________/    |  _____ \    \   \      /  /  |   |_______ |    |____   ____|   |  |    |  |   / /        \ \   |      \     |  |
   | |             |  |    | |    \   \    /  /   |   |      | |        |   |       |  |    |  |   | |        | |   |   |\  \    |  |
   | |             |  |    | |     \   \  /  /    |   |______| |        |   |       |  |____|  |   | |        | |   |   | \  \   |  |
   | |             |  |____| |      \       /     |   |________|        |   |       |   ____   |   | |        | |   |   |  \  \  |  |
   | |             |  _____\ \       |     |      |   |                 |   |       |  |    |  |   | |        | |   |   |   \  \ |  |
   | |_________    |  |     \ \      |     |      |   |                 |   |       |  |    |  |   | |        | |   |   |    \  \|  |
   |__________/    |__|      \_\     |_____|      |___|                 |___|       |__|    |__|   \_\________/_/   |___|     \_____| 
                                                                                                                          By:Tech-Sec
    For more visit: https://github/Tech-Sec
    ''')
