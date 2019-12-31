import datetime
TimeFrame = 30
ListSize = int((24*60)/30)
#----------------------------------------------------
class candle:
    def __init__(self):
        self.date = datetime.datetime(2019,12,29)
        self.open = 0
        self.high = 0
        self.low = 0
        self.close = 0
        self.volume = 0
#----------------------------------------------------
class ctr:
    def __init__(self):
        self.total_ctr = 0
        self.ctr = 0
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
    cdl.open = float(line[index1:index2])

    index1 = index2 + 1
    index2 = line.find(",",index1)
    cdl.high = float(line[index1:index2])

    index1 = index2 + 1
    index2 = line.find(",",index1)
    cdl.low = float(line[index1:index2])

    index1 = index2 + 1
    index2 = line.find(",",index1)
    cdl.close = float(line[index1:index2])

    index1 = index2 + 1
    l = len(line)
    cdl.volume = int(line[index1:l-1])
#----------------------------------------------------
def find_time_index(time=datetime.datetime):
    index = time.hour *60 + time.minute
    index /= TimeFrame
    return(int(index))
