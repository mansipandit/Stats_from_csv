import csv
from stats import min_temp, max_temp, mean_temp, median_temp, warmest_day

csv_dialect = dict(delimiter=',')

with open('/home/mansi/Documents/personal/stats/uk_ec46_tt.csv','r') as file_a:
    reader1 = csv.reader(file_a, **csv_dialect)
    next(reader1)
    list_values=[]
    for row in reader1:
        list_values.append((row[1], row[3]))

    min_temperature = min_temp(list_values)
    print("Minimum temperature = ", min_temperature[1], "on", min_temperature[0])
    # output : ('Minimum temperature = ', '-0.2', 'on', '2018-01-21 12:00:00')

    max_temperature = max_temp(list_values)
    print("Maxinum temperature = ", max_temperature[1], "on", max_temperature[0])
    # output : ('Maxinum temperature = ', '9.6', 'on', '2018-01-28 12:00:00')

    mean_temperature = mean_temp(list_values)
    print("Mean temperature = ", mean_temperature)
    # output : ('Mean temperature = ', 4.068508287292812)

    median_temperature = median_temp(list_values)
    print("Median temperature = ", median_temperature)
    # output : ('Median temperature = ', 5.5)

    #[0=Monday, 1=Tuesday ....6=Sunday]
    for day_week in [0,1,2,3,4,5,6]:
        warmest_days = warmest_day(list_values, day_week)

    # output : warmest monday = ('2018-02-19 00:00:00', '8.9')



