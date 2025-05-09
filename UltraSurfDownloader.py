import wget
from zipfile import ZipFile
import os
import subprocess
import atexit
import shutil


chrome_extension_filename = "mjnbclmflcpookeapghfhapeffmpodij"
zip_filename = f"{chrome_extension_filename}.zip"

def SelfDeletion():
    shutil.rmtree(chrome_extension_filename)

    
    if os.path.exists("../callmekaii SchoolBypass main dist.zip"):
        os.remove("../callmekaii SchoolBypass main dist.zip")
    elif os.path.exists("/callmekaii SchoolBypass main dist.zip"):
        os.remove("/callmekaii SchoolBypass main dist.zip")
    else:
        print("Zip not found!")

    subprocess.Popen(
        ["self_delete.bat"],
        creationflags=subprocess.DETACHED_PROCESS
    )

atexit.register(SelfDeletion)


#Downloads the goods
if os.path.isfile(f"{chrome_extension_filename}/app.js"):
    pass
else:
    try:
        wget.download('https://mrpa-crx-1308499021.cos.na-siliconvalley.myqcloud.com/recommend/vpn/mjnbclmflcpookeapghfhapeffmpodij/mjnbclmflcpookeapghfhapeffmpodij.crx?q-sign-algorithm=sha1&q-ak=AKIDnhS6YnoY1U5rdKmxtcx87tRWaVGn580c&q-sign-time=1725206395%3B1882886455&q-key-time=1725206395%3B1882886455&q-header-list=host&q-url-param-list=&q-signature=f679842c57f5659a9bfa147dbe9bc04db2c7ff9c', zip_filename)
        #This kinda extracts the good stuff then finally deletes it
        ZipFile(zip_filename).extractall(chrome_extension_filename)
        os.remove(zip_filename)
        input("\nDON'T CLOSE THE APP IF YOU'RE NOT YET DONE BROWSING. ONLY CLOSE THE APP WHEN DONE. PRESSING ENTER WILL EXIT THE APP\nPress Enter to exit...")
    except:
        input("No internet connection")

