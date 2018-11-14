 #!/usr/bin/env python3
import os
import fs
from fs import open_fs
import gnupg
import pathlib

gpg = gnupg.GPG(gnupghome="/home/prasad/.gnupg")
home_fs = open_fs(".")

if os.path.exists("check/"):
    print("check directory exists")
else:
    home_fs.makedir("check")
    print("Created check directory")

files_dir = []

for filename in os.listdir('/home/prasad/Desktop/btp/en_file'):                        
    files_dir.append('en_file/'+filename)

for x in files_dir:
    with open(x, "rb") as f:
        clean_file = files_dir[files_dir.index(x)]
        status = gpg.encrypt_file(f,recipients=["test@gmail.com"],output=clean_file[8:]+".gpg")
        print("ok: ", status.ok)
        print("status: ", status.status)
        print("stderr: ", status.stderr)
        os.rename(clean_file[8:] + ".gpg", "check/" +clean_file[8:] + ".gpg")

