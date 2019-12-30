import os.path
import io
import datatime
#----------------------------------------------------
def find_entries(input_file,i):
    
    if(not isinstance(i,int) or not isinstance(input_file,io.IOBase)):
        print("Err: Callong function \"find_entries(...)\" with {} input parameter".format(type(i)))
        return
    fn = "Month"+str(i)+".txt"
    try:
        output_file = open(fn,"w")
    except Exception as exp:
        print(exp)
        return
    for line in input_file:
        print(line)

    
#----------------------------------------------------
def process():
    input_file = open("XAUUSD.cfd30.csv","r")
    find_entries(input_file,i)
    for line in input_file:
        

    input_file.close()
#----------------------------------------------------
#----------------------------------------------------
print("Started...")
try:
    if(os.path.exists(".\XAUUSD_Monthly.csv") == True):
        process()
    else:
        Print("Input file not found!")
except Exception as exp:
    print(exp)
#----------------------------------------------------

print("Finished.")