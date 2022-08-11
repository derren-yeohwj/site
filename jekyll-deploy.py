#!/usr/bin/python3

import os

confirm = "N"

#build jekyll project into _site
os.chdir(os.environ["HOME"] + "/site")
build = os.system("jekyll build -q")

if build != 0:
	print("Jekyll build failed! Skipping commit.")
	exit()

while(True):
	commitMsg = input("Please enter commit message: ")
	confirm = input("Please confirm commit message (Y/N): ")

	if confirm in ('y', 'Y'):
		break
	elif confirm in ('n', 'N'):
		print("\nPlease re-enter commit message.\n")
	else:
		print("\nInvalid option. Please re-enter commit message.\n")

os.system("git add *")
os.system("git commit -am '" + commitMsg + "'")
os.system("git push -u origin main")
