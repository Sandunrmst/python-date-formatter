
def dateFormatter(date):

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

print(dateFormatter("12/05/2023"))


        