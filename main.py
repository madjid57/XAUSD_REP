import os.path
import io
import datetime
import Common
#----------------------------------------------------
def process():
    time_frame_list = [Common.ctr() for i in range(0,Common.ListSize)]
    
    input_file = open("XAUUSD.cfd30.csv","r")
    cdl1 = Common.candle()
    
    line = input_file.readline()
    Common.get_candle_data(line,cdl1)
    for line in input_file:
        index = Common.find_time_index(cdl1.date)

        cdl2 = Common.candle()
        Common.get_candle_data(line,cdl2)
        
        delta_t = cdl2.date - cdl1.date

        if(delta_t.seconds == Common.TimeFrame*60):
            time_frame_list[index].total_ctr += 1
            if(cdl1.close > cdl1.open):
                if(cdl2.close > cdl2.open):
                    time_frame_list[index].ctr += 1
            if(cdl1.close < cdl1.open):
                if(cdl2.close < cdl2.open):
                    time_frame_list[index].ctr += 1
        del cdl1
        cdl1 = cdl2
        del cdl2
        
        
    output_file = open("Out.txt","w")
    for i in range(0,Common.ListSize):
        output_file.write("{:0>2d}:{:0>2d}  Total={:^6d} , Count={:^6d} , Probability={:>6.2f}%\n"
        .format(int((i*Common.TimeFrame)/60),int((i*Common.TimeFrame)%60),time_frame_list[i].total_ctr,time_frame_list[i].ctr,
        100*time_frame_list[i].ctr/time_frame_list[i].total_ctr))

    output_file.close()

        
        

    input_file.close()
#----------------------------------------------------
#----------------------------------------------------
print("Started...")
try:
    if(os.path.exists(".\XAUUSD.cfd30.csv") == True):
        process()
    else:
        print("Input file not found!")
except Exception as exp:
    print(exp)
#----------------------------------------------------

print("Finished.")