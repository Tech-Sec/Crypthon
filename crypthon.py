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
    command = input('crypthon>')
    # generating key
    if command == '1':
        write_key()
    # encryption
    elif command == '2':
        encrypt_file()
    # decryption
    elif command == '3':
        decrypt_file()
    else:
        print('Choose correct option!!')
except FileNotFoundError:
    print('''
Enter the correct file name!!!
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