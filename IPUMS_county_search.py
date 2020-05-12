import csv             #package for csv manipulation

f = open('usa_00003.csv')

csv_f = csv.reader(f) #read original file into python

print(csv_f)

relevant_obs = [] #list to be filled with relevant observations

of_interest = [29] #StateFIPS we are interested in


for a in range(len(of_interest)):         #converts of_interest list to strings
    of_interest[a] = str(of_interest[a])    #because excel sheet numbers were entered as text
    

for row in csv_f:                           #scans for CountyFIPS
    if row[6] in of_interest:               #and adds relevant observations to list
        relevant_obs.append(row)
        #print(row)


##
##
###print(relevant_obs,"Hi")
##
##print(len(relevant_obs))

with open('mo occ analysis data_WK.csv', 'w', newline='') as myfile:   #writes relevant observations to another csv,  mo occ analysis data_WK 
     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     for i in relevant_obs:
         wr.writerow(i)

#input()
