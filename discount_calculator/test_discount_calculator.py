import unittest

from discount_calculator import calculate_discount

class DiscountCalculatorTests(unittest.TestCase):
	def testCorrectDiscount(self):
		discount = calculate_discount(200, 10, 30)
		self.assertEqual(discount, 150)
	
	def testZeroRelativeDiscount(self):
		discount = calculate_discount(200, 0, 40)
		self.assertEqual(discount, 160)
	
	def testZeroAbsoluteDiscount(self):
		discount = calculate_discount(200, 50, 0)
		self.assertEqual(discount, 100)
	
	def testBigDiscount(self):	# make sure total price is equal to 0 when the discounts are larger than the price 
		discount = calculate_discount(100, 50, 60)
		self.assertEqual(discount, 0)
	
	def testBigRelativeDiscount(self):	# make sure error is raised when user inputs relative discount above 100
		with self.assertRaises(ValueError):
			discount = calculate_discount(150, 200, 10)
		
if __name__ == "__main__":
	unittest.main()
