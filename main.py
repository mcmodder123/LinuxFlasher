import subprocess
subprocess.run("sudo fdisk -l", shell=True)
isopath = input("Input file directory (double check spelling): ")
flashpath = input("What device to flash to? (double check spelling) ")
prompt = input("Are you sure? Y/N: ")

if prompt == "Y" or "y":
    subprocess.run(f"sudo dd bs=4M if={isopath} of={flashpath} status=progress", shell=True)
else:
    exit()
