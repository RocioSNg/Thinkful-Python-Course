# Program:  Calculate the discount on an item from a shopping cart.

def calculate_discount(item_cost, relative_discount, absolute_discount):
	''' Takes the item cost and removes the relative discount
	as a percentage and removes the absolute discount 
	> calculate_discount(200, 10, 30)
	> 150
	'''
	relative_discount_amount <- item_cost*(relative_discount/100)
	final price = item_cost - relative_discount_amount - absolute_discount
	return final price
