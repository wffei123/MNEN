# MNEN
#Influential node identification method based on multi-order neighbors and exclusive neighborhood


In a complex network, the identification of node influence and the localization of key nodes play a crucial role in analyzing network structure and determining the positioning of nodes for information transmission control, resource redistribution, and network regulation. In this study, we propose a method for identifying influential nodes called "Multi-order Neighbors and Exclusive Neighborhood" (MNEN) after analyzing and investigating existing methods in the field.

#requirements
Python== 3.7.3
networkx==2.3
matplotlist==3.1.0


# Execution

The algorithm can be used as standalone program as well as integrated in python scripts.

## Standalone

MNEN can be executed as standalone script with the following parameters:

**arguments**
Name  |  Type | Description | Default 
-------------  | ------------- |------------- | -------------
allpath | string| It cotains the file path of networks | './datasets/filelist_dataset.txt'
files|string|The rank list of IDME algorithm on each network| './datasets/+pt+/data/+pt+.txt'


#Input
All network file path names are placed in the './datasets/filelist_dataset.txt' file. E.g:<br>
Protein<br>
Email<br>
Ca-Erdos<br>
Ca-Astroph<br>
Karate<br>
Dolphins<br>
USAir<br>
Euroroad<br>
Ca-GrQc<br>
Powergrid<br>
# Output
path = 'dataset.txt'#dataset为具体数据集名字
The rank list of MNEN algorithm on each network, which are written to the '.\outputdata\MNEN_'+path' file.

Instructions for using DCDME code:

1.Install networkx  python libraries before running the script.

2.Unzip datasets.zip to the current directory. 

3.Run the python file MNEN.py.
