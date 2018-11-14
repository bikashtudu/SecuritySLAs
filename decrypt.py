 #!/usr/bin/env python3

import os
import fs
from fs import open_fs
import gnupg

gpg = gnupg.GPG(gnupghome="/home/prasad/.gnupg")
home_fs = open_fs(".")

files_dir = []
files_dir_clean = []

if os.path.exists("decrypted/"):
    print("Decrypted directory already exists")
else:
    home_fs.makedir("decrypted/")
    print("Created decrypted directory")

if os.path.exists("decrypted/file_data"):
    print("Decrypted directory already exists")
else:
    home_fs.makedir("decrypted/file_data")
    print("Created decrypted directory")

if os.path.exists("decrypted/service_data"):
    print("Decrypted directory already exists")
else:
    home_fs.makedir("decrypted/service_data")
    print("Created decrypted directory")

if os.path.exists("decrypted/login_data"):
    print("Decrypted directory already exists")
else:
    home_fs.makedir("decrypted/login_data")
    print("Created decrypted directory")

files_dir = []

for filename in os.listdir('/home/prasad/Desktop/btp/check'):                        
    files_dir.append('check/'+filename)

for x in files_dir:
    length = len(x)
    endLoc = length - 4
    clean_file = x[6:endLoc]
    files_dir_clean.append(clean_file)

for x in files_dir:
    with open(x, "rb") as f:
       status = gpg.decrypt_file(f, passphrase="pass1234",output=files_dir_clean[files_dir.index(x)])
       file = files_dir_clean[files_dir.index(x)]
       l = len(file)-9
       print("ok: ", status.ok)
       print("status: ", status.status)
       print("stderr: ", status.stderr)
       os.rename(files_dir_clean[files_dir.index(x)],"decrypted/"+file[0:l]+'/'+files_dir_clean[files_dir.index(x)])

