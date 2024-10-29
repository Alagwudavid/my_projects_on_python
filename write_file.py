import os
with open("HackFile.txt", mode="w", encoding="utf-8") as HackFile:
    HackFile.write("About to hack your env:\nLoading hack...\nHack completed")
with open("HackFile.txt", encoding="utf-8") as HackFile:
    print(HackFile.read())