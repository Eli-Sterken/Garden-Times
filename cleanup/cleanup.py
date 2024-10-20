# Made by Eli Steken! Project started on 10/18/2024

import os, platform

oS = platform.system()
temp = ""

if(oS == "Windows"):
    temp = f"C:\\Users\\{os.getenv("USERNAME")}\\AppData\\Local\\Temp\\"
else:
    temp = "/tmp/" 

os.remove(f"{temp}i.jpg")
os.remove(f"{temp}config.json")
os.remove("./decrypt.html")
print("\n\nCleanup complete! Make sure to delete this file as well as the ransomware file.")    
