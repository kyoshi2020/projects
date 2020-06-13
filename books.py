# Total Wholesale Book Cost Calculator
cover_price=24.95
number_of_books=int(input("How many books do you want to order at wholesale?"))
def ship_cost (number_of_books):
	if number_of_books==1:
		return(number_of_books * 3) #Cost of shipping 1 book is $3
	else:
		return(3 + (number_of_books - 1) * 0.75) #each additional book is .75 to ship
def discounted_price(number_of_books):
	return(cover_price - (cover_price *.4)) #40% discount on wholesale per book
def wholesale_cost(number_of_books):
	return ((discounted_price(number_of_books) * number_of_books) + ship_cost(number_of_books))
print("The cost of buying and shipping", number_of_books, "books is $",round(wholesale_cost(number_of_books), 2))

print("The cost of the books wholesale is", ((cover_price * .6) * number_of_books))
print("The cost of shipping alone is", ((number_of_books -1) * 0.75) +3)

# print("YOU FINALLY FIGURED IT OUT YOU PICKLE RICK MOTHER FUCKER") - my personal celebration of figuring out the last couple lines
