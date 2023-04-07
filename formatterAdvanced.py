import string

lower = string.ascii_lowercase #simply you can try this for validate the date if user enter the letters with date 
upper = string.ascii_uppercase #simply you can try this for validate the date if user enter the letters with date 

def dateFormatter(date):

    list_date = list(date)
    if len(date) <= 10 and not("/" in list_date and "." in list_date):
               
        if "/" in list_date:
            
            year = ""
            month = ""
            day = ""
            split_list=[]
            new_Date = ""

            tempHolder = date.split("/")
            
            year = tempHolder[2]
            month = tempHolder[1]
            day = tempHolder[0]

            split_list.append(year)
            split_list.append(month)
            split_list.append(day)
            
            new_Date = "/".join(split_list)

            return "Befor -> "+ date + " After -> " + new_Date
        
        elif "." in list_date:
            year = ""
            month = ""
            day = ""
            split_list=[]
            new_Date = ""

            tempHolder = date.split(".")
            
            year = tempHolder[2]
            month = tempHolder[1]
            day = tempHolder[0]

            split_list.append(year)
            split_list.append(month)
            split_list.append(day)
            
            new_Date = ".".join(split_list)

            return "Befor -> "+ date + " After -> " + new_Date
        else:
            print("please Enter valid date like in example e.g -> 08/04/2022")

        
    else:
        print("please Enter valid date like in example e.g -> 08/04/2022")
        

            

user_input = str(input("Enter your date formate: e.g-> 12/05/2023 : "))
 
print(dateFormatter(user_input))