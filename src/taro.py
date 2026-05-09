import subprocess
import sys
import os
import tarfile
import wslPath
import time

start_time = time.time()

#Flags to use with the "tar" command; v is recommended (verbose)
flags = "-xvf"

#Start of tar checks

try:
    filepassed = sys.argv[1]
except IndexError:
    sys.exit("A file must be passed. Syntax: ./taro.py ./tarball.tar.xz")

if os.path.exists(filepassed):
    if not os.path.isfile(filepassed):
        sys.exit("The file passed must be a file")

fpath = os.path.abspath(filepassed)
print(wslPath.to_posix(fpath))
dirname = wslPath.to_posix(os.path.dirname(fpath))
filename = os.path.basename(wslPath.to_posix(fpath))
print(dirname)
print(filename)

if not fpath.endswith((".tar.gz", ".tar.bz2", ".tar.xz", ".tar.zst", ".tar")):
    sys.exit("File passed must be a tarball")

if not tarfile.is_tarfile(fpath):
    sys.exit("The tarball provided seems to be invalid.")

#End of tar checks

if os.name != "nt":
    sys.exit("This program is intended for use on Windows only.")

def main():
    fileconfirm = input("The file to be extracted is: " + wslPath.to_posix(fpath) + "\nContinue? [y/N]: ")
    if fileconfirm.strip("") == "y":
        pass
    elif fileconfirm.strip("") == "n" or "":
        sys.exit()

    subprocess.run(["wsl", "-d", "ubuntu", "tar", flags, wslPath.to_posix(fpath), "-C", "~/"])
    #os.path.dirname(file_path)
    end_time = time.time()
    print("Finished after " + str(end_time - start_time) + " seconds")
    sys.exit("Folder saved in WSL ~/ !")

if __name__ == "__main__":
    main()