import shelve
import csv

"Class StockInformation"
class StockInfromation:
    def __init__(self, item_name, item_description, item_selling_price, item_stock_level, item_mac):
        self.item_name = item_name
        self.item_description = item_description
        self.item_selling_price = item_selling_price
        self.item_stock_level = item_stock_level
        self.item_mac = item_mac

#ADD ITEM
def additem():
    print("##############ADD###############")
    item_db = shelve.open("item_db")
    item_name = input("Enter the product name ")
    if item_name in item_db or item_name =="": #Check for duplicate names/ blank
        print('Duplicated Items/Invalid input')  #print and go back to the options
    else:
        item_description = input("Enter the product description ")


        while True:
            item_selling_price = input("Enter product's selling price: ") #Check if the product is an integer or string

            try:
                #Try if it's integer convert to float for  item_selling_price and break the loop
                item_selling_price = float(item_selling_price)
                break

            except ValueError: # print and loop back
                print(item_selling_price, " is not a integer \nPlease enter again ")

        while True:

            item_stock_level = input("Enter Product's stock level: ")#Check if the product is an integer or string

            try:
                # Try if it's integer convert to float for  item_stock_level and break the loop
                item_stock_level = int(item_stock_level)
                break

            # Exception if stock was not an integer
            except ValueError:# print and loop back
                print(item_stock_level, " is not a integer\nPlease enter again \n")



        item_mac = input("Enter the product manufacturer ")
        item = StockInfromation(item_name,item_description,item_selling_price,item_stock_level,item_mac) #Place all the input into a class
        item_db = shelve.open("item_db") #open shelve
        item_db[item_name] = item
        item_db.close()
        print("Item is recorded in the Database ")



#REMOVE ITEM
def removeitem():
    print("###############REMOVE###############")
    item_db = shelve.open("item_db")
    print("""1. Delete all of Inventory\n2. Delete individual Inventory """)
    option = input("Options: ")

    if option == "1":
        for name in item_db: #loop name in item_db to check for item_name
            del item_db[name] # delete all of the products
        print("All Inventories have been deleted ")

    elif option =="2" :
        for name in item_db: #loop name in item_db to check for item_name
            exist = item_db[name]  #exist set as a variable key for the data
            print("List of products : {}".format(exist.item_name))

        item_name = input("Enter the item Name  {Caps Sensitive} : ")
        if item_name in item_db:
            del item_db[item_name] #Delete inventory base on item_name {user_input}
            print("Item has been deleted")
        else:
            print("Invalid item name")

    item_db.close()




#DISPLAY ITEM
def display_item():

    print("##############Binary###########")
    item_db = shelve.open("item_db")
    list = []
    l = 0 # index
    for name in item_db:  # meat and fish
        exist = item_db[name]
        list.append(exist.item_name)
        l +=1
        print("{}. List of products : {}".format(l,exist.item_name))

#Binary Sort
    def binary_sort(list, target):
        start = 0
        end = len(list) - 1

        while start <= end:
            middle = (start + end) // 2
            midpoint = list[middle]
            if midpoint > target:
                end = middle - 1
            elif midpoint < target:
                start = middle + 1
            else:
                return midpoint
#Quicksort
    def quicksort(list):
        if not list:
            return []
        return (quicksort([x for x in list[1:] if x < list[0]])
                + [list[0]] +
                quicksort([x for x in list[1:] if x >= list[0]]))

    user = input("Enter to search product  {Caps Sensitive} : ") # User input the product name

    if user in item_db:
        list = quicksort(list) #to sort the list for binary
        bin = binary_sort(list, user)

        if bin in item_db:
            item = item_db[bin]
            print("""   
            [Item Name] : {}
            [Item Description] : {}
            [Item Selling Price] : ${:.2f}
            [Item Stock Level] : {} Stocks
            [Item Manufacture] : {}""".format(item.item_name, item.item_description, float(item.item_selling_price),
                                                item.item_stock_level, item.item_mac))
        else:
            print("invalid data")
    else:
        print('Invalid data')
        item_db.close()



#SORTING
#Sort base on the stock and selling price by ascensding order
#Note: Average/Sum features {under progress/later do }

def sort():
    print("##############SORTING###########")
    stock_list = []
    selling_list = []
    item_db = shelve.open("item_db")
    for name in item_db:  # meat and fish
        exist = item_db[name]
        stock_list.append(int(exist.item_stock_level))
        selling_list.append(float(exist.item_selling_price))

#Insertion Sort
    def insertionSort(selling_list):
        n = len(selling_list)
        #print("len of n " ,n) #2
        # Starts with the first item as the only sorted entry.
        for i in range(1, n):
           #print("loop",i)
            # Save the value to be positioned
            value = selling_list[i]
            #print("value in the list " ,value)
            # Find the position where value fits in the
            # ordered part of the list.
            pos = i
            while pos > 0 and value < selling_list[pos - 1]: # To compare the first number
                # Shift the items to the right during the search
                selling_list[pos] = selling_list[pos - 1]
                pos -= 1
                # Put the saved value into the open slot.
            selling_list[pos] = value


#Bubble Sort
    def bubbleSort_optimized(stock_list):
        n = len(stock_list)

        # Perform n-1 bubble operations on the sequence
        for i in range(n - 1, 0, -1):
            # Set boolean variable to check occurrence of swapping
            # in inner loop
            # Bubble the largest item to the end

            noSwap = True
            for j in range(i):
                if stock_list[int(j)] > stock_list[int(j) + 1]:
                    # swap the j and j + 1 items
                    tmp = stock_list[j]
                    stock_list[j] = stock_list[j + 1]
                    stock_list[j + 1] = tmp

                    # Set boolean variable value if swapping occured
                    noSwap = False


            # Exit the loop if no swapping occured
            # in the previous pass
            if noSwap:
                break

    sort = input("1. Display by Item selling price\n2. Display the Stock level\nUser input: ")
    #Sort base on the selling price / stock level
    if sort == '1':
        print("##########Displaying Selling price from accending ###########")
        print('Input List:', selling_list)
        print('total list: ',len(selling_list)) #len of the list
        insertionSort(selling_list)
        print('Ascending order')

        print('Sorted List:', selling_list)

    elif sort == '2':
        print("##########Displaying Stock level from accending ###########")
        print('Input List:', stock_list)
        print('total list: ',len(stock_list)) # len of the list
        bubbleSort_optimized(stock_list)
        print('Ascending order')
        print('Sorted List:', stock_list)
    else:
        print('Wrong input')
        pass



#Update Product
#Additonal features ??
#Decide to update selling price / stock level instead
def update_product():
    print("################Update##################")
    item_db = shelve.open("item_db")


    #Show the list of stock
    def list_stock():
        l = 0
        for product_name in item_db: # List all of the products
            l +=1
            print(l,"List of products : {}".format(product_name))
        while True:
            user = input("Enter the product name to make a change  {Caps Sensitive} : ")
                #Loop to check user in item_db
            if user in item_db:
                return user
            else:
                print('ERROR : Invalid data')



    #Update selling price
    def update_selling_price(user):
        exist = item_db[user]
        user_value = float(input("Please enter a value  for new selling price value {Caps Sensitive} "))
        item = StockInfromation(exist.item_name, exist.item_description, user_value, exist.item_stock_level,
                                exist.item_mac)
        item_db[exist.item_name] = item
        print("Product Selling price have been updated in the database")

    #Update stock level
    def update_stock_level(user):
        exist = item_db[user]
        user_value = int(input("Please enter a value for new stock level"))
        item = StockInfromation(exist.item_name, exist.item_description, exist.item_selling_price, user_value,
                                exist.item_mac)
        item_db[exist.item_name] = item
        print("Product Stock level have been updated in the database")


    #Options for selling price / stock level
    print("""1) Update Selling Price \n2) Update Stock Level """)
    user_option = input("Please enter an options: ")
    if user_option == "1":
        user = list_stock()  #return user
        update_selling_price(user)
    elif user_option == "2":
        user = list_stock() #return user
        update_stock_level(user)
    else:
        print('Invalid Data')






        item_db.sync()
        item_db.close()




#Exporting csv file from shelve
#Additional features (1)
#import csv

def exporting_csv():
    print("#################Exporting == CSV#################")
    item_db = shelve.open('item_db')
    data_dict = [] #dict in list
    #list = []
    header = ["Item Name","Item Description","Item Selling Price","Item Stock level","Item manufacturer"] # header for csv
    for item in item_db:
        exist = item_db[item]
        #list.append(
            #[exist.item_name, exist.item_description, exist.item_selling_price, exist.item_stock_level, exist.item_mac])
        data_dict.append(
            {"Item Name":exist.item_name, "Item Description":exist.item_description, "Item Selling Price":exist.item_selling_price, "Item Stock level":exist.item_stock_level, "Item manufacturer":exist.item_mac})

    def write_csv_from_dicts(data, header): # Write the data from the shelve to the csv file row by row
        with open("Inventory_data_backup.csv", "w") as csv_file: #write the file as csv_file
            dict_writer = csv.DictWriter(csv_file, fieldnames=header)
            dict_writer.writeheader()  # write header
            for row in data: #data == data_dict
                dict_writer.writerow(row)  # write each row

    write_csv_from_dicts(data_dict, header)


    print("Data has been export to Inventory_data_backup.csv")



    #csv_writer = csv.writer(inventory, delimiter='\t')

    # csv_writer.writerow([exist.item_name, exist.item_description, exist.item_selling_price, exist.item_stock_level,exist.item_mac])

#Importing csv
#read csv file to shelve
#Overwriting common existing data_attributes in the shelve with the csv file data

def importing_csv():
    item_db = shelve.open('item_db')
    list_dict = []
    print("WARNING This will overwrite the existing data you have in shelve \nif you like to leave type Q else Proceed type K")
    option = input("Option : Leave(Q) , Proceed(K) ")
    if option =="k":
        def read_csv(): # read the data from csv file to python and store it into the shelve database
            print("Overwriting with Inventory_data_backup.csv")
            with open("Inventory_data_backup.csv", 'r') as csv_file:
                dict_read = csv.DictReader(csv_file)
                len = 1
                for row in dict_read :
                    list_dict.append(row)
                    print(len,row['Item Name'])
                    len = len + 1
                    item = StockInfromation(row['Item Name'], row['Item Description'], row['Item Selling Price'],
                                            row['Item Stock level'], row['Item manufacturer'])
                    item_db[row['Item Name']] = item



        read_csv()
    elif option == "q":
        pass



# Stock Inventory Summary
#View sum/average  of the inventory
def stock_summary():
    print("###########################Stock Summary#############################")
    stock_list = []
    item_db = shelve.open("item_db")
    for name in item_db:
        exist = item_db[name]
        stock_list.append(exist.item_stock_level)

    print("""1) Sum of the stock inventory \n2) Average of the stock inventory""")
    option = input("Enter the options : ")

    def sum_stock(): #Sum of the inventory
        sum = 0
        for num in stock_list:
            sum+= int(num)
        return sum


    def average_stock(): #Average of the inventory
        avglen = len(stock_list)
        sum = sum_stock()
        avg = sum /avglen
        return avg

    if option == '1':
        sum = sum_stock()
        print("\nThe total sum of inventory stock is:", sum,"products")
    elif option == "2":
        avg = average_stock()

        print("\nThe average of the total inventory stock is:", avg)
###############################################################################




while True:
        print("                                                         ")
        print('''####################################################################################
Welcome to The EZy Shop Management Panel, select the following option to continue:
-----------------------------------------------------------------
1. Add a new procuct
2. Delete the product
3. View the product
4. Update ~stock value/selling price value
5. Sorting ~ Stock/ selling price ascending order
6. Export to CSV file
7. Import from CSV file
8. Inventory Summary ~ Sum/average of inventory size 
0. Close 
##################################################################''')
        option = input("Please enter your options ")
        print("                                                         ")
        if option == '':
            continue
        if option == '1':
            additem()
        if option == '2':
            removeitem()
        if option == '3':
            display_item()
        if option == '4' :
            update_product()
        if option == "5":
            sort()
        if option == "6":
            exporting_csv()
        if option == "7":
            importing_csv()
        if option == "8":
            stock_summary()
        if option == "0":
            break
        else:
            continue




