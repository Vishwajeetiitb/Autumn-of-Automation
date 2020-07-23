days = int(input("Enter number of days \n"))
stocks =[]
for i in range(days):
	stocks.append(int(input("")))

index = 0
selected_price = stocks[index]
selected_index = 0
profit = max(stocks[index:len(stocks)]) - selected_price
for price in stocks:
	if price < selected_price :
		if profit < max(stocks[index:len(stocks)]) - price:
			selected_index = index
		
	index += 1
print("selected date is ", selected_index+1)