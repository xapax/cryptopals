import collections 


fil = open("cp4-file.txt", "r")


for line in fil:
    line = line.strip("\n")
    line = line.decode("hex")
    
    for char in range(65,123):
        res = ""
        for x in range(len(line)):
           xor = chr(ord(line[x]) ^ char)
           res += xor
           #print xor

        print res

        d = collections.defaultdict(int)
        for c in res:
            d[c] += 1
        print d

