from save_results import save_results
from load_data import load_all_data
from inventory_calculations import InventoryCalculator
from abc_algorithm import ArtificialBeeColony


def main():

    # Load datasets
    datasets = load_all_data()

    # Create inventory calculator
    calculator = InventoryCalculator(
        datasets["products"],
        datasets["inventory"],
        datasets["forecast"]
    )

    # Display inventory analysis
    calculator.inventory_analysis()

    print("\n")
    print("=" * 80)
    print("ARTIFICIAL BEE COLONY OPTIMIZATION")
    print("=" * 80)

    # Create ABC object
    abc = ArtificialBeeColony()

    # List to store optimized results
    results = []

    # Process each product
    for _, product in datasets["products"].iterrows():

        print("\n" + "-" * 60)
        print(f"Product : {product['product_name']}")

        # Calculate EOQ
        eoq = calculator.calculate_eoq(
            product["annual_demand"],
            product["ordering_cost"],
            product["holding_cost"]
        )

        print(f"EOQ : {eoq}")

        # Fitness
        total_cost = abc.fitness(
            product["annual_demand"],
            product["ordering_cost"],
            product["holding_cost"],
            eoq
        )

        print(f"Total Inventory Cost : {total_cost}")

        # Food Sources
        food_sources = abc.generate_food_sources(
            product["annual_demand"],
            product["ordering_cost"],
            product["holding_cost"]
        )

        print("\nFood Sources")
        for source in food_sources:
            print(source)

        # Employed Bee Phase
        improved_sources = abc.employed_bee_phase(
            food_sources,
            product["annual_demand"],
            product["ordering_cost"],
            product["holding_cost"]
        )

        print("\nAfter Employed Bee Phase")
        for source in improved_sources:
            print(source)

        # Onlooker Bee Phase
        best_sources = abc.onlooker_bee_phase(improved_sources)

        print("\nAfter Onlooker Bee Phase")
        for source in best_sources:
            print(source)

        # Scout Bee Phase
        final_sources = abc.scout_bee_phase(
            best_sources,
            product["annual_demand"],
            product["ordering_cost"],
            product["holding_cost"]
        )

        print("\nAfter Scout Bee Phase")
        for source in final_sources:
            print(source)

        # Best Solution
        best = abc.best_solution(final_sources)

        print("\nBest Inventory Solution")
        print(best)

        results.append({
            "Product": product["product_name"],
            "EOQ": best["eoq"],
            "Minimum Cost": best["cost"]
        })

    # Save all results
    save_results(results)

    print("\n")
    print("=" * 80)
    print("ABC OPTIMIZATION COMPLETED")
    print("=" * 80)


if __name__ == "__main__":
    main()