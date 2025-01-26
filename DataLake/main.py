from datalake import DataLake

if __name__ == "__main__":
    datalake = DataLake()
    print("Want to enter dummy data?")
    print("=>")
    decision = input()
    if decision == "Yes":
        datalake.collect_data(10.5)
        datalake.collect_data(15.2)
        datalake.collect_data(23.3)    
    retrieve_data = datalake.retrieve_data()
    print("Retrieved Data is : ")
    print(retrieve_data)
    mean,std_dev = datalake.analyze_data()
    print("\n Data Analysis")
    print("Mean Value : {}".format(mean))
    print("Std Value : {}".format(std_dev))
    datalake.visualize_data()