import os
entries = os.listdir('./')

for entry in entries:
    if '.sha' in entry:
        print(entry)
        os.remove('./'+entry)
