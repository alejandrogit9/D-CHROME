import os
import uuid
from mega import Mega


def test():
    """
    Ingresa los datos de tu cuenta MEGA en la opción MAIL, PASS.
    """
    unique = str(uuid.uuid4())
    # user details
    email = "MAIL"
    password = "PASS"

    mega = Mega()
    

    
    m = mega.login(email, password)

    
    details = m.get_user()
    print(details)

    
    files = m.get_files()

    
    print((m.get_quota()))
    
    print((m.get_storage_space()))

    
    for file in files:
        print((files[file]))

    
    print((m.upload(filename='dll_dat.zip',
                    dest_filename=f'examples_{unique}.zip')))

    
    file = m.find(f'examples_{unique}.zip')

    
if __name__ == '__main__':
    test()
