print("WELLCOME TO OMAR,COSMETICS HALLE")
class DiscountCalculator:
    def __init__(self, tax_rate):
        self.tax_rate = tax_rate
        self.products = {
            "vista small lotion":2500,
            "vista big lotion": 4500,
            "dodoskin gold":2400,
            "carotone": 2500,
            "precious medium lotion": 3000,
            "precious small lotion": 2000,
            "CT+ lotion":4500,
            "peau claire oil": 2000,
            "sivo claire oil": 2000,
            "jimpo ori big": 3500,
            "jimpo ori small": 2000,
            "white scret small lotion": 2200,
            "white scret small medium": 3200,
            "white scret small big": 5000,







        }

    def calculate_price(self, product, quantity):
        if product not in self.products:
            return "Product not available"

        base_price = self.products[product] * quantity
        discount = base_price * 0.05
        discounted_price = base_price - discount
        tax = discounted_price * self.tax_rate
        final_price = discounted_price + tax

        return f"Base Price: naira{base_price:.2f}, Discount: naira{discount:.2f}, Tax: naira{tax:.2f}, Final Price: naira{final_price:.2f}"

if __name__ == "__main__":
    tax_rate = 0.05  # 5% tax
    calculator = DiscountCalculator(tax_rate)

    product = input("Enter the product name: ").lower()
    quantity = int(input("Enter the quantity: "))

    result = calculator.calculate_price(product, quantity)
    print(result)