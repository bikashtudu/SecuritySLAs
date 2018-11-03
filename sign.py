#!/usr/bin/env python3

import os
import fs
from fs import open_fs
import gnupg

gpg = gnupg.GPG(gnupghome="/home/prasad/.gnupg")
home_fs = open_fs(".")

if os.path.exists("signatures/"):
        print("Signatures directory already created")
else:
        home_fs.makedir("signatures")
        print("Created signatures directory")

files_dir = []

files = [f for f in os.listdir(".") if os.path.isfile(f)]
for f in files:
    files_dir.append(f)

for x in files_dir:
    with open(x, "rb") as f:
        stream = gpg.sign_file(f,passphrase="pass1234",detach = True,output=files_dir[files_dir.index(x)]+".sig")
        os.rename(files_dir[files_dir.index(x)]+".sig", "signatures/"+files_dir[files_dir.index(x)]+".sig")
        print(x+stream.status)



