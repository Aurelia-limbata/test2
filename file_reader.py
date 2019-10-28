inpfilename = input("Please enter file name you want to read.\n")
inp = open(inpfilename, "r")
for i in inp:
    print(i)
inp.close()