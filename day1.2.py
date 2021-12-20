

    
import pandas as pd



df = pd.read_csv("day1.csv")



def part2(df):  
    count = 1
    for (index, colname) in enumerate(df):
            numbers = df[colname].values
            for i in range(len(numbers)-3):
                first = numbers[i] + numbers[i+1] + numbers[i+2]
                second = numbers[i+1] + numbers[i+2] + numbers[i+3]
                if first < second:
                    count += 1
    print(count)
  

    


part2(df)









