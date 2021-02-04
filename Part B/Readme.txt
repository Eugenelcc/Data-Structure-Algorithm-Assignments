FILES CONTAIN:
190507x_mini_project.py ~ Python code / main.py file
inventory_data_backup.csv ~ Contain csv data to either export or import to the python file 
{item_db.bak
item_db.dat
item_db.dir} ~ Shelve database

Phase4.py ~ python code for Phase 4




This is some instruction or guide for the inventory management system i coded 

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


~1. Add new product:
add a new product to the shelve base on :
	item_name = item_name
        item_description = item_description
        item_selling_price = item_selling_price
        item_stock_level = item_stock_level
        item_mac = item_mac

~2. Delete the product
Options:
	A1. Delete all of Inventory
	B2. Delete individual Inventory 
	* for options B2 inventory name is caps and space sensitive so type in the item names given 

~3. View the product
View the product data inside 
	names are caps and space sensitive

~4 Update ~stock value/selling price value
{not sure if this is considered as phase 3 of the additonal features}
I implement this just to allow it to increase the stock and selling price of the product 
product names are caps and space sensitive
Options:
	1) Update Selling Price 
	2) Update Stock Level 

~5 Sorting ~ Stock/ selling price ascending order
Sort the stock and selling price base on ascending orders

~6 Export to CSV
{Additonal features for phase 3}
This is use for when the admin want to collect the data in csv file format

can test out by adding new product into the inventory system and then export once export it would be save in
inventory_data_backup



~7 Import to CSV
{Additonal features for phase 3 } 
This is use for importing data in csv file into the inventory management system

can test out by deleting all the data in the inventory system and import the inventory_data_backup.csv file after that
view the product in the inventory system , it will load up the data saved in the csv

~8 Inventory Summary ~ Sum/average of inventory size 
Allow the admin to view the total sum of inventory stocks in the database or the average 