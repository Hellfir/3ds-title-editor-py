# 3DS Title Editor (Python Edition)
Takes a filepath to a 3DS ROM as first input, will then check to see if it's a correct format (NCSD or NCCH), output the current Title ID, then take a second input to use as a new title ID.
Correct first input: any filepath to a 3ds rom file
Correct second input: any 8 character hex code

# Why use it?
	If you're using any kind of modified ROMs (such as randomized pokemon), this will allow you to have an independent save file from an unmodified file, or any other modified files that share the same title ID. Definitely works if using Citra emulator, unsure on interaction with homebrewed 3ds.

# TODO:
implement a proper check for second input to make sure it's actually hex
convert to proper CLI tool so that it can be used with 
	$ 3dstide [rompath] [newid]
