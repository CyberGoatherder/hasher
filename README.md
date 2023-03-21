# Hasher
A python script that will take an input folder path and return file information including hashes of all files at that path. Recursion is optional with (-r) (requires python >3.5). You can also output to a .CSV with (-d).

---

### Usage

Simply provide a target folderpath

```
usage: hasher.py [-h] [-d] [-r] [-o OUTPUT] path

Hasher

positional arguments:
  path                  input folderpath, the folder of files you want to hash

optional arguments:
  -h, --help            show this help message and exit
  -d, --dump            dump results to a CSV
  -r, --recursive       recursively check subdirectories (Requires python >3.5)
  -o OUTPUT, --output OUTPUT
                        output folder path for CSV

Example:
python hasher.py /path/to/Files -r -d -o /path/to/preferred/Output
```

### Example

![Example use of the tool.](/image/hasher_ex2.png "Example use of the tool.")
