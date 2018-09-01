import random

path =  'keysfile.txt'
abc = ['q', 'w', 'e', 'r', 't', 'z', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'y', 'x', 'c', 'v', 'b', 'n', 'm']
num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
def generate():
    key = ''
    keys = []
    keyunused = False
    file = open("keysfile.txt","r")
    for line in file:
        line = line.strip("\n")
        keys.append(line)
    file.close()
    file = open("keysfile.txt","a")
    while keyunused == False:
        for i in range (20):
            print "Char "+str(i)
            rand = random.randint(1, 2)
            if rand == 1:
                randabc = random.choice(abc)
                key = key + randabc
            else:
                randnum = random.choice(num)
                key = key + randnum
        if key in keys:
            keyunused = False
        else:
            keyunused = True
    # Write the key
    file.write(key)
    file.write('\n')
    file.close
    return key
print generate()