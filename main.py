class CustomerManager:
    def __init__(self):
        self.customers = {}
        self.tax_rate = 0.2
        self.tax_threshold = 100
        self.discount_threshold = 500

    def add_customer(self, name, purchases):
        """Add a customer or extend their purchases."""
        if name in self.customers:
            self.customers[name].extend(purchases)
        else:
            self.customers[name] = purchases

    def add_purchase(self, name, purchase):
        """Add a single purchase for a customer."""
        self.add_customer(name, [purchase])

    def add_purchases(self, name, purchases):
        """Add multiple purchases for a customer."""
        self.add_customer(name, purchases)

    def _calculate_total_purchases(self, purchases):
        """Calculate the total price of purchases, applying tax if necessary."""
        total = 0
        for purchase in purchases:
            price = purchase['price']
            if price > self.tax_threshold:
                price *= (1 + self.tax_rate)
            total += price
        return total

    def _determine_customer_status(self, total):
        """Determine the status of a customer based on their total purchases."""
        status = []
        if total > self.discount_threshold:
            status.append("Eligible for discount")
        elif total > 300:
            status.append("Potential future discount customer")
        else:
            status.append("No discount")

        if total > 1000:
            status.append("VIP Customer!")
        elif total > 800:
            status.append("Priority Customer")

        return status

    def generate_report(self):
        """Generate a report for all customers."""
        for name, purchases in self.customers.items():
            total = self._calculate_total_purchases(purchases)
            print(name)
            for status in self._determine_customer_status(total):
                print(status)

    @staticmethod
    def _has_heavy_item(purchases):
        """Check if any purchase is heavy."""
        return any(purchase.get('weight', 0) > 20 for purchase in purchases)

    @staticmethod
    def _has_fragile_item(purchases):
        """Check if any purchase is fragile."""
        return any(purchase.get('fragile', False) for purchase in purchases)

    def calculate_shipping_fee(self, purchases):
        """Calculate shipping fee based on purchase weight."""
        return 50 if self._has_heavy_item(purchases) else 20

def calculate_shipping_fee_for_heavy_items(purchases):
    """Calculate shipping fee for heavy items."""
    return 50 if CustomerManager._has_heavy_item(purchases) else 20

def calculate_shipping_fee_for_fragile_items(purchases):
    """Calculate shipping fee for fragile items."""
    return 60 if CustomerManager._has_fragile_item(purchases) else 25

flat_tax = 0.2