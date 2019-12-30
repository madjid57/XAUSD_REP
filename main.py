import os.path
import io
import datetime
import Common
#----------------------------------------------------
def process():
    input_file = open("XAUUSD.cfd30.csv","r")
    cdl = candle()
    for line in input_file:
        get_candle_data(line,cdl)

    input_file.close()
#----------------------------------------------------
#----------------------------------------------------
print("Started...")
try:
    if(os.path.exists(".\XAUUSD.cfd30.csv") == True):
        process()
    else:
        Print("Input file not found!")
except Exception as exp:
    print(exp)
#----------------------------------------------------

print("Finished.")