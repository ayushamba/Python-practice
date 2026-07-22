##BELOW IS THE WRITE FUNCTION WHICH IS USED TO WRITE THE FILE
r = open("superman.txt",'a')
r.write("\n")
r.write("and now i am appending some text to the file")

r.close()