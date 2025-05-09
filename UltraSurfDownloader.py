import wget
from zipfile import ZipFile
import os
import subprocess
import atexit
import shutil

def SelfDeletion():
    shutil.rmtree("mjnbclmflcpookeapghfhapeffmpodij")
    subprocess.Popen(
        ["self_delete.bat"],
        creationflags=subprocess.DETACHED_PROCESS
    )
    
    if os.path.exits("callmekaii SchoolBypass main dist.zip"):
        os.remove("callmekaii SchoolBypass main dist.zip")
    else:
        pass


atexit.register(SelfDeletion)
filename = "mjnbclmflcpookeapghfhapeffmpodij.zip"

#Downloads the goods
if os.path.isfile("mjnbclmflcpookeapghfhapeffmpodij/app.js"):
    pass
else:
    wget.download('https://mrpa-crx-1308499021.cos.na-siliconvalley.myqcloud.com/recommend/vpn/mjnbclmflcpookeapghfhapeffmpodij/mjnbclmflcpookeapghfhapeffmpodij.crx?q-sign-algorithm=sha1&q-ak=AKIDnhS6YnoY1U5rdKmxtcx87tRWaVGn580c&q-sign-time=1725206395%3B1882886455&q-key-time=1725206395%3B1882886455&q-header-list=host&q-url-param-list=&q-signature=f679842c57f5659a9bfa147dbe9bc04db2c7ff9c', filename)
    #This kinda extracts the good stuff then finally deletes it
    ZipFile(filename).extractall("mjnbclmflcpookeapghfhapeffmpodij")
    os.remove(filename)
input("\nPress Enter to exit...")
