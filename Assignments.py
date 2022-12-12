#!/usr/bin/env python
# coding: utf-8

# # EON-DA-WEEK1- Assignment on Python Basic Data Types 

# # Problem 1:
Data scientist getting time data as in string format from real-time IoT Machines like, time =
'20:26:45', 
Actuly they want to anaysis time data with hours , miniutes and seconds separatly. 
How will you help them to seperate this string data into the following output 

hours:20
miniutes:26
seconds:45
# # Code 1:

# In[14]:


time = '07:16:35'
hr = time.split(":")[0]
min = time.split(":")[1]
sec = time.split(":")[2]
output = "hours:"+hr+"\nminutes:"+min+"\nseconds:"+sec
print(output)


# # Problem 2:
Data Enginers needs to collect data from webpage firstpage.html , this file contents are given in
string
Task:
1.find How many paragraph elements present in the web_page
2.find any script file present in the web_page, if yes print web_page contain script file
3. print the line containing the script file : <script src="scripts/main.js"></script>
# # Code 2:

# In[29]:


web_page='''<html>
 <head>
 <title>first page</title>
 <script src="scripts/main.js"></script>
 </head>
 <body>
 <p>This is a paragraph. </p>
 <p>This is another paragraph. </p>
 </body>
</html>'''
#TO DO write your code Here

para_counts = web_page.count("<p>")
print(f"1. paragraph elements present in the web_page : {para_counts}")

if web_page.find("<script") != -1:
    start = web_page.find("<script")
    end = web_page.find("</script>")
    print(f"2. web_page contain script file")
    print("3. " + web_page[start:end] + "</script>")
else:
    print("2. web_page does not contain script file")
    


# # Problem 3:

# In[ ]:


Use the following dictionary objects for this assignment:
dict_aisle = { "A100": ['bananas', 'milk', 'bread'],
 "A101": ['pens', 'pencils', 'paper'],
 "A102": ['canned_peas', 'canned_carrots', 'canned_beans'],
 "A103": ['plates', 'glasses', 'table_cloth']
 }
Perform the following Operation on given dictionary data:
1.Prompt the user to enter the name of the item:
 a.If found, display the aisle number of the item.
 b.if not found, display a message "Item Not Found!!"
2.Add the following aisle to the dict_aisle:
 a.Aisle No: B101
 b.Items on aisle: kids toys, kids clothes
3. Print the dict_aisle as below:
A100 : ['bananas', 'milk', 'bread']
A101 : ['pens', 'pencils', 'paper']
A102 : ['canned peas', 'canned carrots', 'canned beans']
A103 : ['plates', 'glasses', 'table cloth']
B101 : ['Kids toys', 'Kids cloths']


# # Code 3:

# In[28]:


dict_aisle = { "A100": ['bananas', 'milk', 'bread'],
 "A101": ['pens', 'pencils', 'paper'],
 "A102": ['canned_peas', 'canned_carrots', 'canned_beans'],
 "A103": ['plates', 'glasses', 'table_cloth']
 }
#TO DO Write your code here

item = input("Enter an item : ")
    
found = False

print(dict_aisle["A100"])


for key in dict_aisle:
    if item in dict_aisle[key]:
        print(f"Item {item} found in aisle: {key}")
        found = True
        break

if not found:
    print("Item not found!!")
    
dict_aisle["B101"] = ["kids", "toys", "kids", "clothes"]

for x,y in dict_aisle.items():
    print(x ,":",y)
    
#print(dict_aisle)


# # Problem 4:

# In[ ]:


Use the following dictionary objects for this assignment:
# Fruit : price
inventory = { "banana": 0.25,
 "watermelon": 5.25,
 "orange": 0.50,
 "peer": 0.40,
 "apple": 0.30,
 "kiwi": 0.75,
 }
Perform the following Operation on given dictionary data:
1.Prompt the user to enter the quantity of each fruit and display the total cost of the purchase.


# # Code 4:

# In[114]:


inventory = { "banana": 0.25,
 "watermelon": 5.25,
 "orange": 0.50,
 "peer": 0.40,
 "apple": 0.30,
 "kiwi": 0.75,
 }
#TO DO Write your code here
banana_qty  = float(input("Enter the quantity of banana :"))
watermelon_qty  = float(input("Enter the quantity of watermelon :"))
orange_qty  = float(input("Enter the quantity of orange :"))
peer_qty  = float(input("Enter the quantity of peer :"))
apple_qty  = float(input("Enter the quantity of apple :"))
kiwi_qty  = float(input("Enter the quantity of kiwi :"))

total = inventory.get("banana") * banana_qty + inventory.get("watermelon") * watermelon_qty 
+ inventory.get("orange") * orange_qty + inventory.get("peer") * peer_qty + inventory.get("apple") * apple_qty 
+ inventory.get("kiwi") * kiwi_qty
print(f"Total cost : {total}")


# 
# # Problem 5:

# In[ ]:


Assume you as a Data analytics and you needs to analyze the data to find centeral tendency and
disperson using descriptive statistics.
given data is
age_set={'45','56','60','30','25','65','300','25','56','64','30','45','30','108'}
Task
1.find the distinct mean,median,mode
2.find the range,variange,standard deviation


# # Code 5:

# In[14]:


#age_set={'45','56','60','30','25','65','300','25','56','64','30','45','30','108'}
#TO DO write your code Here 

age_set={45,56,60,30,25,65,300,25,56,64,30,45,30,108}


age_list = list(age_set)
n = len(age_list)
age_list.sort()

mean = sum(age_list)/n
median = 0
if n%2 != 0:
    val = (n+1)//2
    median = age_list[val-1]
else:
    print(val)
    median = (age_list[val-1] + age_list[val])/2
    
print(age_list)
print("mean :" ,mean)
print("median:", median)


# In[17]:


n_num = [1, 2, 3, 4, 5,6]
n = len(n_num)
n_num.sort()
 
if n % 2 == 0:
    median1 = n_num[n//2]
    median2 = n_num[n//2 - 1]
    median = (median1 + median2)/2
else:
    median = n_num[n//2]
print("Median is: " + str(median))


# In[18]:


age_list = [1, 2, 3, 4, 5,6]
n = len(age_list)
age_list.sort()

mean = sum(age_list)/n
median = 0
if n%2 != 0:
    val = (n+1)//2
    median = age_list[val-1]
else:
    print(val)
    median = (age_list[val-1] + age_list[val])/2
    
print(age_list)
print("mean :" ,mean)
print("median:", median)

