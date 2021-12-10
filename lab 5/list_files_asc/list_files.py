
import os
list_dir = os.listdir('.')
list_dir = [f.lower() for f in list_dir]
print(sorted(list_dir))