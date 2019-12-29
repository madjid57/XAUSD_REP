import os.path
import io
import datetime
#----------------------------------------------------
class candle:
    def __init__(self):
        self.date = datetime.datetime(2019,12,29)
        self.open = "0.0"
        self.high = "0.0"
        self.low = "0.0"
        self.close = "0.0"
        self.volume = "0"
#----------------------------------------------------
def find_entries(input_file,m):
    
    if(not isinstance(m,int) or not isinstance(input_file,io.IOBase)):
        print("Err: Callong function \"find_entries(...)\" with {} input parameter".format(type(i)))
        return
    fn = "Month"+str(m)+".txt"
    try:
        output_file = open(fn,"w")
    except Exception as exp:
        print(exp)
        return

    output_file.write("{:^20s}{:^15s}{:^15s}{:^15s}{:^15s}{:^15s}{:^15s}\n".
    format("Time","Open","High","Low","Close","Volume","Change"))
    cdl = candle()
    for line in input_file:
        index2 = line.find(",")
        index1 = index2 + 1
        index2 = line.find(",",index1)
        date_str = line[0:index2]
        #print(date_str)
        cdl.date = datetime.datetime.strptime(date_str,"%Y.%m.%d,%H:%M")

        index1 = index2 + 1
        index2 = line.find(",",index1)
        cdl.open = line[index1:index2]

        index1 = index2 + 1
        index2 = line.find(",",index1)
        cdl.high = line[index1:index2]
        index1 = index2 + 1
        index2 = line.find(",",index1)
        cdl.low = line[index1:index2]
        index1 = index2 + 1
        index2 = line.find(",",index1)
        cdl.close = line[index1:index2]
        index1 = index2 + 1

        l = len(line)
        cdl.volume = line[index1:l-1]

        if cdl.date.month == m:
            output_file.write("{:20s}{:^15s}{:^15s}{:^15s}{:^15s}{:^15s}{:^13.2f}\n".
            format(str(cdl.date),cdl.open,cdl.high,cdl.low,cdl.close,cdl.volume,float(cdl.close)-float(cdl.open)))

    
#----------------------------------------------------
def process():
    input_file = open("XAUUSD_Monthly.csv","r")
    for i in range(1,13) :
        input_file.seek(0)
        find_entries(input_file,i)

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