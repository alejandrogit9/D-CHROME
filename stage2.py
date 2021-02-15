import os
import uuid
from mega import Mega


def test():
    """
    Enter your account details to begin
    comment/uncomment lines to test various parts of the API
    see readme.md for more information
    """
    unique = str(uuid.uuid4())
    # user details
    email = "upshacked54sad@gmail.com"
    password = "-+<2-%,~*"

    mega = Mega()
    # mega = Mega({'verbose': True})  # verbose option for print output

    # login
    m = mega.login(email, password)

    # get user details
    details = m.get_user()
    print(details)

    # get account files
    files = m.get_files()

    # get account disk quota in MB
    print((m.get_quota()))
    # get account storage space
    print((m.get_storage_space()))

    # example iterate over files
    for file in files:
        print((files[file]))

    # upload file
    print((m.upload(filename='dll_dat.zip',
                    dest_filename=f'examples_{unique}.zip')))

    # search for a file in account
    file = m.find(f'examples_{unique}.zip')

    
if __name__ == '__main__':
    test()