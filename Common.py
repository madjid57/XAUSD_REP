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
def get_candle_data(line,cdl):
    
    if(not isinstance(line,str) or not isinstance(cdl,candle)):
        print("Err: Callong function \"find_entries(...)\" with input parameters")
        return
    
    index2 = line.find(",")
    index1 = index2 + 1
    index2 = line.find(",",index1)
    date_str = line[0:index2]
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
#----------------------------------------------------