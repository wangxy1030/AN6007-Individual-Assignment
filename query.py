"""
AN6007 ADVANCED PROGRAMMING 
Individual Practical Assignment
Name: Wang Xiaoyi
Matriculation Number: G2403550G
"""
# preparing information for interactive interfaces
from complete import merge_data
electricity_info=merge_data()
year_info=[]
region_info=[]
dwelling_info=[]
for each in electricity_info:
    if each[0] not in region_info:
        region_info.append(each[0])
    if each[2] not in year_info:
        year_info.append(each[2])
    if each[4] not in dwelling_info:
        dwelling_info.append(each[4])
print(year_info)
print(region_info)
print(dwelling_info)
# define the function for handling interactive information
def menu():
    items ="""Welcome! Here is a program for you to query the average household usage of electricity by month for a particular year, region and dwelling type.
    Please enter enter a year, a region and a dwelling type. 
    If you want to quit, please enter a "-" for year selection.
"""
    print(items)
    year_query=input("Please choose a year raning from 2010 to 2023:")
    region_query=input("Please choose a region from 'Central Region', 'North Region', 'West Region', 'North East Region', 'East Region':")
    dwelling_query=input("Please choose a dwelling type from '1-room / 2-room', 'Private Apartments and Condominiums', 'Landed Properties', '5-room and Executive', '3-room', '4-room':")
    return year_query,region_query,dwelling_query
# define the main query function
import pandas as pd
def main():
    while True:
        year_query,region_query,dwelling_query = menu()
        if year_query!="-":
            electricity_info = merge_data()
            average_usage= {} 
            for each in electricity_info:
                if each[0]==region_query and each[2]==year_query and each[4] == dwelling_query: 
                    area_info=each[1]
                    month=int(each[3])
                    if area_info not in average_usage:
                        average_usage[area_info]={}
                    if month not in average_usage[area_info]:
                        average_usage[area_info][month]={"sum_usage": 0, "count": 0}
                    average_usage[area_info][month]["sum_usage"] += float(each[5])
                    average_usage[area_info][month]["count"] += 1
            if average_usage!={}:
                columns=[range(1,13)]
                results=pd.DataFrame(index=average_usage.keys(), columns=columns)
                for area_info,value1 in average_usage.items():
                    for month,value2 in value1.items():
                        avg_usage=round(value2["sum_usage"]/value2["count"],2)
                        results.loc[area_info, month]=avg_usage
                results=results.iloc[:,1:]
                results.index.name="Area"
                print(results)
            else:
                print('''No relevant records were found. Please check the contents you entered and try again.
                              ''')
        else:
            return "Thanks for your query. Good Bye!"
print(main())