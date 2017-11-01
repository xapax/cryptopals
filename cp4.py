import collections 
import operator

points = {
"e": 12702,
"t": 9056,
"a": 8167,
"o": 7507,
"i": 6966,
"n": 6749,
"s": 6327,
"h": 6094,
"r": 5987,
"d": 4253,
"l": 4025,
"c": 2782,
"u": 2758,
"m": 2406,
"w": 2360,
"f": 2228,
"g": 2015,
"y": ,
"p": 8,
"b": 7,
"v": 6,
"k": 5,
"j": 4,
"x": 3,
"q": 2,
"z": 1,
}

scoreboard = {}


fil = open("cp4-file.txt", "r")


for line in fil:
    line = line.strip("\n")
    line = line.decode("hex")
    
    for char in range(0,123):
        res = ""

        # XORa en rad
        for x in range(len(line)):
           res += chr(ord(line[x]) ^ char)

        res_lower = res.lower()
        pt = collections.defaultdict(int)

        # Räkna ihop antalet gånger som varje karaktär finns
        for c in res_lower:
            pt[c] += 1
        
        total_points = 0
            
        # Beräkna antal poäng som strängen får
        for key in pt:
            if key in points:
                point = points[key] * pt[key]
                total_points = total_points + point

        # Stoppa in poängen i scoreboarden
        scoreboard[res] = total_points


#print max(scoreboard.iteritems(), key=operator.itemgetter(1))[0]

#first2vals = [scoreboard[k] for k in sorted(scoreboard.keys())[:2]]
#print first2vals


# Sortera scoreboarden och printa ut dom i ordning
for w in sorted(scoreboard, key=scoreboard.get, reverse=True):
    print w, scoreboard[w]
