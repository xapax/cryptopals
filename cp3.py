a = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
a = a.decode("hex")
resultat = []
result = {}

for x in  range(64,122):
    
    res = ""
    
    for y in range(len(a)):
        res += chr(ord(a[y]) ^ x)
        
    #print res
    resultat.append(res)
    #print "Key for above: " + str(x)
    res.count("e")
    result[res] = res.count("e") + res.count("t") + res.count("a")
    result[res] = result[res] + res.count("E") + res.count("T") + res.count("A")
   # print res
    # print result[res]
     



print max(result, key=result.get)



