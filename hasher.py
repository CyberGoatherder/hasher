import argparse
import pathlib
import re
import os
import hashlib
import magic
import csv
import glob
from datetime import datetime as dt2
from time import sleep

print("""    __  __           __
   / / / ____ ______/ /_  ___  _____
  / /_/ / __ `/ ___/ __ \/ _ \/ ___/
 / __  / /_/ (__  / / / /  __/ /
/_/ /_/\__,_/____/_/ /_/\___/_/
@Cybergoatherder
""")

### Set sleep time
delay = 0.20

### Set Args
parser = argparse.ArgumentParser(description="Hasher")
parser.add_argument("path", type=pathlib.Path, help="input filepath, the folder of files you want to hash")
parser.add_argument("-d", "--dump", action="store_true", help="dump results to a CSV")
parser.add_argument("-r", "--recursive", action="store_true", help="recursively check subdirectories (Requires python >3.5)")
parser.add_argument("-o", "--output", help="output folder path for CSV", default = os.getcwd())
args = parser.parse_args()
args_path = (str(args.path))
args_output = (str(args.output))
if re.match(r".*\\.*[a-zA-Z0-9]$", args_output):
    args_output = args_output + "\\"
elif re.match(r".*/.*[a-zA-Z0-9]$", args_output):
    args_output = args_output + "/"
sleep(delay)
print("Selected Folder: '" + args_path + "'");sleep(delay)
if args.dump:
    print("Selected Output Folder: '" + args_output + "'");sleep(delay)
    # Setup CSV
    header = ['#','File Name','File Path','File Size (Bytes)','File Type','MD5','SHA1','SHA256']
    # Generate timestamp
    now = dt2.now()
    dt = now.strftime("%Y-%m-%d_%H-%M-%S")
    # Set name for output file
    csvname = args_output + "hash_out_" + dt + ".csv"
    with open(csvname, 'w', encoding='UTF8',newline='') as c:
        writer = csv.writer(c)
        # write the header
        writer.writerow(header)

# Determine the pool of files to be parsed
if args.recursive:
    group = glob.glob(args_path + '/**/*', recursive=True)
else:
    group = glob.glob(args_path + '/*')
group = [f for f in group if os.path.isfile(f)]

# Get file count
count = 0
# Iterate directory
for filename in group:
        count += 1
print('\n[+] Files Found:', count)
print("\n[+] Parsing Entries:" + "\n");sleep(delay)

i = 1 # Set file counter to 1
for filename in group:
    my_a = [i]
    print("["+str(i)+"]")
    # Naming
    print("File Name: " + (os.path.basename(filename)))
    my_a.append((os.path.basename(filename)))
    # Pathing
    print("File Path: " + (os.path.dirname(filename)))
    my_a.append((os.path.dirname(filename)))
    # Sizing
    file_stat = os.stat(filename)
    print("File Size: " + str(file_stat.st_size) + " bytes")
    my_a.append(file_stat.st_size)
    # Typing
    m = magic.from_file(filename)
    print("File Type: " + str(m))
    my_a.append(m)
    # Hashing
    BUF_SIZE = 65536  # lets read stuff in 64kb chunks!

    md5 = hashlib.md5()
    sha1 = hashlib.sha1()
    sha256 = hashlib.sha256()

    with open(filename, 'rb') as g:
        for chunk in iter(lambda: g.read(4096), b''):
            md5.update(chunk)
            sha1.update(chunk)
            sha256.update(chunk)
    h = md5.hexdigest()
    print("MD5: " + str(h))
    my_a.append(h)
    h = sha1.hexdigest()
    print("SHA1: " + str(h))
    my_a.append(h)
    h = sha256.hexdigest()
    print("SHA256: " + str(h))
    my_a.append(h)
    if args.dump:
        with open(csvname, 'a', encoding='UTF8', newline='') as c:
            writer = csv.writer(c)
            writer.writerow(my_a)
    # Finishing
    i = i + 1
    print(" ")
if args.dump:
    print("[+] Dumped to CSV: \'" + str(csvname) + "\'" + "\n");sleep(delay)
else:
    print("[i] Consider using -d to dump output to a CSV!")
if not args.recursive:
    print("[i] Consider using -r to run recursively!")
