import random


class ArtificialBeeColony:

    def __init__(self):

        self.num_bees = 10

    # --------------------------
    # Fitness Function
    # --------------------------

    def fitness(self,
                annual_demand,
                ordering_cost,
                holding_cost,
                eoq):

        ordering = (annual_demand / eoq) * ordering_cost

        holding = (eoq / 2) * holding_cost

        return round(ordering + holding, 2)

    # --------------------------
    # Generate Food Sources
    # --------------------------

    def generate_food_sources(self,
                              annual_demand,
                              ordering_cost,
                              holding_cost):

        food_sources = []

        for i in range(self.num_bees):

            eoq = random.uniform(50, 200)

            cost = self.fitness(
                annual_demand,
                ordering_cost,
                holding_cost,
                eoq
            )

            food_sources.append({

                "bee": i + 1,

                "eoq": round(eoq, 2),

                "cost": cost

            })

        return food_sources
            # --------------------------
    # Employed Bee Phase
    # --------------------------

    def employed_bee_phase(
        self,
        food_sources,
        annual_demand,
        ordering_cost,
        holding_cost
    ):

        for source in food_sources:

            current_eoq = source["eoq"]

            new_eoq = current_eoq + random.uniform(-10, 10)

            if new_eoq < 1:
                new_eoq = 1

            new_cost = self.fitness(
                annual_demand,
                ordering_cost,
                holding_cost,
                new_eoq
            )

            if new_cost < source["cost"]:

                source["eoq"] = round(new_eoq, 2)
                source["cost"] = round(new_cost, 2)

        return food_sources
            # --------------------------
    # Onlooker Bee Phase
    # --------------------------

    def onlooker_bee_phase(self, food_sources):

        # Sort food sources by cost (lowest cost is best)
        sorted_sources = sorted(
            food_sources,
            key=lambda x: x["cost"]
        )

        # Select the best half
        selected_sources = sorted_sources[: len(sorted_sources) // 2]

        return selected_sources
            # --------------------------
    # Scout Bee Phase
    # --------------------------

    def scout_bee_phase(
        self,
        food_sources,
        annual_demand,
        ordering_cost,
        holding_cost
    ):

        worst_source = max(
            food_sources,
            key=lambda x: x["cost"]
        )

        new_eoq = random.uniform(50, 200)

        new_cost = self.fitness(
            annual_demand,
            ordering_cost,
            holding_cost,
            new_eoq
        )

        worst_source["eoq"] = round(new_eoq, 2)
        worst_source["cost"] = round(new_cost, 2)

        return food_sources
            # --------------------------
    # Best Solution
    # --------------------------

    def best_solution(self, food_sources):

        best = min(
            food_sources,
            key=lambda x: x["cost"]
        )

        return best