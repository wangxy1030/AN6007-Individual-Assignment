"""
AN6007 ADVANCED PROGRAMMING 
Individual Practical Assignment
Name: Wang Xiaoyi
Matriculation Number: G2403550G
"""
# sub problem 1: extract data from the original txt files
# convert the data in txt into different lists
def extract_data():
    area=[]
    with open("D:\材料\研究生阶段\Trimester 2\Advanced Programming\Assignment 1\Area.txt","r") as area_file:
        for each in area_file:
            area_data=each.strip("\n").split(";")
            area.append(area_data)
    dwelling=[]
    with open("D:\材料\研究生阶段\Trimester 2\Advanced Programming\Assignment 1\Dwelling.txt","r") as dwelling_file:
        for each in dwelling_file:
            dwelling_data=each.strip("\n").split(",")
            dwelling.append(dwelling_data)
    electricity=[]
    with open("D:\材料\研究生阶段\Trimester 2\Advanced Programming\Assignment 1\Electricity.txt","r",encoding='utf-8') as electricity_file:
        for each in electricity_file:
            electricity_data=each.strip("\n").split(";")
            electricity.append(electricity_data)
    datedim=[]
    with open("D:\材料\研究生阶段\Trimester 2\Advanced Programming\Assignment 1\DateDim.txt","r") as datedim_file:
        for each in datedim_file:
            datedim_data=each.strip("\n").split(";")
            datedim.append(datedim_data)
    return area,dwelling,electricity,datedim
if __name__=="__main__":
    extract_data()
#%%
# sub problem 2: merge all the extracted data from sub problem 1
# convert the lists into dataframes and then use pandas to merge
def merge_data():
    import pandas as pd
    area,dwelling,electricity,datedim = extract_data()
    area_df=pd.DataFrame(area[1:],columns=area[0])
    dwelling_df=pd.DataFrame(dwelling[1:],columns=("dwelling_type_id","dwelling_type"))
    electricity_df=pd.DataFrame(electricity[1:],columns=electricity[0])
    datedim_df=pd.DataFrame(datedim[1:],columns=datedim[0])
    electricity_info= pd.merge(electricity_df,datedim_df,on="DateID",how="inner")
    electricity_info= pd.merge(electricity_info,area_df,on="AreaID",how="inner")
    electricity_info= pd.merge(electricity_info,dwelling_df,on="dwelling_type_id",how="inner")
    electricity_info=electricity_info[["Region","Area","year","month","dwelling_type","kwh_per_acc"]]
    electricity_info=[list(electricity_info.columns)]+electricity_info.values.tolist()
    return electricity_info
if __name__=="__main__":
    merge_data()
#%%
# show the final dataset in list format:
merge_data()
electricity_info=merge_data()
print(electricity_info)