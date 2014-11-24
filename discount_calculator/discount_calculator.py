# Program:  Calculate the discount on an item from a shopping cart.

def calculate_discount(item_cost, relative_discount, absolute_discount):
	''' Takes the item cost and removes the relative discount
	as a percentage and removes the absolute discount 
	> calculate_discount(200, 10, 30)
	> 150
	'''
  if relative_discount > 100:
     raise ValueError("Discount cannot be above 100")
      
	relative_discount_amount = item_cost * (float(relative_discount)/100)
	final_price = item_cost - relative_discount_amount - absolute_discount
  
	if final_price < 0:
		final_price = 0
    
	return final_price
