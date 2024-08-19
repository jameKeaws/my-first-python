import statistics
import csv
import array

# simple statistics operations
sample_data_1 = [1, 3, 5, 7]
sample_data_2 = [2, 3, 5, 4, 3, 5, 3, 2, 5, 6, 4, 3]

# TODO Use the mean function.  Calculate the average values
# print(statistics.mean(sample_data_1))

# TODO Use the different median functions
# print(statistics.median(sample_data_1))
# print(statistics.median(sample_data_2))
# print(statistics.median_low(sample_data_2))
# print(statistics.median_high(sample_data_2))

# TODO The mode function indicate which data item occurs most frequently
# print(statistics.mode(sample_data_2))

# Read data from a csv file and calculate statistics
def read_data():
    with open("StockQuotes.csv") as dataFile:
        data = array.array('f', [])
        reader = csv.reader(dataFile)
        
        curLine =0
        for row in reader:
            if curLine == 0:
                # This is the headers row
                pass 
            else:
                # get the closing value from column 4
                item = float(row[4])
                data.append(item)
            curLine += 1
            
        print(f'Read {curLine+1} rows of data')
        return data
    
def calcStats():
    # TODO Read the data from the csv file
    data = read_data()
    
    # Calculate interesting data points
    data_mean = round(statistics.mean(data), 2)
    data_med = round(statistics.median(data), 2)
    data_stdvar = round(statistics.stdev(data), 2)
    data_var = round(statistics.variance(data), 2)
    
    print("Mean : ", data_mean)
    print("Median : ", data_med)
    print("Standard deviation : ", data_stdvar)
    print("Variance : ", data_var)
    
calcStats()

