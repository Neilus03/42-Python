# Put this at the top of your kata02.py file 
kata = (2019, 9, 25, 3, 30)

s_out = ""
s_out += (str(kata[1]) + "/" if kata[1] >9 else "0"+str(kata[1])+ "/")
s_out += (str(kata[2]) + "/" if kata[2] >9 else "0"+str(kata[2])+ "/")
s_out += str(kata[0]) + " "
s_out += (str(kata[3]) + ":" if kata[3] >9 else "0"+str(kata[3])+ ":")
s_out += (str(kata[4]) if kata[4] >9 else "0"+str(kata[4]))
print(s_out)