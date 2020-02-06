def main():
	items = []
	isdone = True
	while (isdone):
		item =  input("Item (enter \"done\" when finished): ")
		if "done" not in item.lower():
			items.append({
			"name": item ,
			"price" : float(input("please enter the price of the item:  ")),
			"quantity": int(input("please enter the quantity of item/s:  "))
			})
		else:
			isdone = False
	print("-------------------\nrecepit\n-------------------")
	totalPrice = 0.0
	if len(items) > 0:
		for item in items:
			totalItemPrice = item["price"] * item["quantity"]
			print(str(item["quantity"]) + " " + item["name"] + " " + str(totalItemPrice)+"KD" )
			totalPrice += totalItemPrice
		print("-------------------\nTotal Price: {}KD".format(totalPrice))

if __name__ == '__main__':
	main()
