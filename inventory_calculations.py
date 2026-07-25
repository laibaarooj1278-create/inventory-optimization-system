import math


class InventoryCalculator:

    def __init__(self, products, inventory, forecast):

        self.products = products
        self.inventory = inventory
        self.forecast = forecast

    # Calculate EOQ
    def calculate_eoq(self, annual_demand, ordering_cost, holding_cost):

        eoq = math.sqrt((2 * annual_demand * ordering_cost) / holding_cost)

        return round(eoq, 2)

    # Inventory Analysis
    def inventory_analysis(self):

        print("\n" + "=" * 80)
        print("INTELLIGENT INVENTORY ANALYSIS")
        print("=" * 80)

        for _, product in self.products.iterrows():

            product_id = product["product_id"]

            product_name = product["product_name"]

            annual_demand = product["annual_demand"]

            ordering_cost = product["ordering_cost"]

            holding_cost = product["holding_cost"]

            lead_time = product["lead_time"]

            inventory = self.inventory[
                self.inventory["product_id"] == product_id
            ]

            forecast = self.forecast[
                self.forecast["product_id"] == product_id
            ]

            if inventory.empty or forecast.empty:
                continue

            current_stock = inventory.iloc[0]["current_stock"]

            safety_stock = inventory.iloc[0]["safety_stock"]

            reorder_point = inventory.iloc[0]["reorder_point"]

            predicted_demand = forecast.iloc[0]["predicted_demand"]

            eoq = self.calculate_eoq(
                annual_demand,
                ordering_cost,
                holding_cost
            )

            print("\n" + "-" * 60)

            print(f"Product Name      : {product_name}")
            print(f"Current Stock     : {current_stock}")
            print(f"Annual Demand     : {annual_demand}")
            print(f"Predicted Demand  : {predicted_demand}")
            print(f"Lead Time         : {lead_time}")
            print(f"Safety Stock      : {safety_stock}")
            print(f"Reorder Point     : {reorder_point}")
            print(f"Economic Order Qty: {eoq}")