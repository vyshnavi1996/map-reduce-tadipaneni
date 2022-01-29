r = open("tadipaneni_01.txt","r")  # open file, read-only
w = open("tadipaneni_02.txt", "w") # open file, write
lines = r.readlines()
lines.sort()

for line in lines:
	w.write(line)
r.close()
w.close()