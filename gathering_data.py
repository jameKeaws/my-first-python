import csv
from string import Template

timing_data = []

with open('TestTimingData.csv') as my_csv_file:
    myCsvFileReader = csv.reader(my_csv_file)
    for anyRow in myCsvFileReader:
        print(anyRow)
        timing_data.append(anyRow)
        
column_chart_data = [["Test Name", "Diff from Average"]]
table_data = [["Test Name", "Run Time (s)"]]

for anyTimingData in timing_data[1:]:
    test_name = anyTimingData[0]
    current_run_time = anyTimingData[1] if anyTimingData[1] != '' else '0'
    average_run_time = anyTimingData[2] if anyTimingData[2] != '' else '0'
    # Compute the runtime difference
    run_time_difference = - int(average_run_time) - int(current_run_time) 
    
    column_chart_data_list_entry = [test_name, run_time_difference]
    table_data_list_entry = [test_name, current_run_time]
    
    column_chart_data.append(column_chart_data_list_entry)
    table_data.append(table_data_list_entry)
    

for anyColumnChartData in column_chart_data:
    print(anyColumnChartData)
    
for anyTableData in table_data:
    print(anyTableData)
    
html_string = Template("""
<html>
<head >
    <script src="https://www.gstatic.com/charts/loader.js"></script>
    <script>
    google.charts.load('current', {packages: ['corechart']});
    google.charts.setOnLoadCallback(drawChart);
    
    function drawChart()
    {
      var data = google.visualization.arrayToDataTable([
        $labels,
        $data
      ],
      false); // 'false' means that the first row contains labels, not data.
      
      var chart = new google.visualization.ColumnChart(document.getElementById('chart_div'));
      chart.draw(data);
    }
    </script>
</head>
<body>
    <div id="chart_div" style="width:800; height:600"></div>
</body>
</html>
""")

chart_data_str = ''

for row in column_chart_data[1:]:
    chart_data_str += '%s,\n'%row
    
completed_html = html_string.substitute(labels=column_chart_data[0],data=chart_data_str)

with open('column_chart.html','w') as f:
    f.write(completed_html)
    