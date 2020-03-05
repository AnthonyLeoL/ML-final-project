fn = "winequality-red.csv"
filein = open(fn)
fileout = open("formatted_reds", "w")

lines = filein.readlines()

for line in lines:
    ind = 1
    line = line.strip("\n")
    line = line.split(";")
    for i in range(len(line[:-1])):
        line[i] = "{}:{}".format(ind, line[i])
        ind += 1
    quality = str(float(line[-1])/10)
    newLine = [quality, " ".join(line[:-1])]
    newLine = " ".join(newLine)
    fileout.write(newLine)
    fileout.write("\n")
print("done")
