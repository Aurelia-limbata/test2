from periodictable import ptable
inpfilename = input("Please input file name.\n")
inp = open(inpfilename, "r")
#read file.
coordinate = []
connectivity = []
atomnum = input("How many atoms in your input file?\n")
for i in inp:
    if i[0] == "#" or i[0] == "%" or i == "\n":
        pass
    else:
        line = i.split()
        if line[0] in ptable:
            coordinate.append(line)
        elif line[0] in range(int(atomnum)):
            connectivity.append(line)

inp.close()
#extract coordinate & connectivity from input file.

term = ("Do you have correspondable table file?\nyes/no\n")
beforenum = []
afternum = []
if term == yes or term == y:
    correspondabletablefilename = input("Please enter file name containing corrspondable table\n")
    ctf = open(correspondabletablefilename, "r")
    for j in ctf:
        line2 = j.split()
        if cnt == 1:
            beforenum = line2
            cnt += 1
elif term == no or term == n:
    term2 = input("Do you make temporaly correspondable table?\n")
    if term2 == yes or term2 == y:
        temporalybefore = input("Please enter current atom number corresponding to 1,2,3......\ne.g.)1,2,3,4,......\n")
        beforenum = temporalybefore.split(",")
    elif term2 == no or term2 == n:
        print("Please make corresponding table file by yourself.\n")