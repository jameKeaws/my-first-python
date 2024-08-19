import csv

# TODO List the dialects that are available to use
print(csv.list_dialects())

# TODO Open a csv file and read each row of data
# with open("TestTimingData.csv") as csv_file:
#     csv_file_reader = csv.reader(csv_file)
#     for any_row in csv_file_reader:
#         print(any_row)

def reader_sample():
    with open("StockQuotes.csv") as csv_data_file:
        csv_data_file_reader = csv.reader(csv_data_file)
        for any_row in csv_data_file_reader:
            print(any_row)
            
# TODO Use the CSV module Sniffer to see what dialect of CSV this is
def use_sniffer():
    with open("StockQuotes.csv") as csv_file:
        dialect = csv.Sniffer().sniff(csv_file.read(1024))
        csv_file.seek(0)
        hasHeader = csv.Sniffer().has_header(csv_file.read(1024))
        csv_file.seek(0)
        print("Headers found: ", str(hasHeader))
        print("dialect.delimiter: ", dialect.delimiter)
        print("dialect.escapechar: ", dialect.escapechar)
        print("dialect.quotechar: ", dialect.quotechar)

# TODO Write data to a csv file
def writer_sample():
    with open("jd_sample_data.csv",mode="w+") as my_csv_file:
        csvwriter = csv.writer(my_csv_file)
        csvwriter.writerow(["Name","Department","Location"])
        csvwriter.writerow(["John Doe", "Accounting", "San Francisco"])
        csvwriter.writerow(["Jane Dae", "Engineering", "San Francisco"])
        csvwriter.writerow(["June Due", "IT", "New York"])


# Exercise the samples
# reader_sample()
# use_sniffer()
writer_sample()