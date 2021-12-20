
import pandas as pd



df = pd.read_csv("day2.csv")


  

def part2(df):  
    hori = 1
    dep = 0
    aim = 0
    for (index, colname) in enumerate(df):
            numbers = df[colname].values
            for x in numbers:
                
                if x[0] == 'f':
                    value = [int(s) for s in x.split() if s.isdigit()]
                    if(aim != 0):
                        newNum = value[0] * aim
                        dep += newNum
                    hori += value[0]
                    
                elif x[0] == 'd':
                    value = [int(s) for s in x.split() if s.isdigit()]
                    
                  
                    aim += value[0]
                elif x[0] == 'u':
                    value = [int(s) for s in x.split() if s.isdigit()]
                    newval = value[0]*-1
               
                    aim += newval
    print(hori)     
    print(aim)       
    print(hori*dep)
                    
  

    

part2(df)









