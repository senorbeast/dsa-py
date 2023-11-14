from UnboundedKnapsack import dp, optimizedDp
from manim import *

class DPTable(Scene):
    def construct(self):
        # Define parameters
        profit = [1, 2, 5]
        weight = [1, 2, 3]
        capacity = 5

        # Choose the function you want to visualize (dfs, memoization, dp, optimizedDp)
        dp_function = dp

        # Get DP table
        dp_table = self.get_dp_table(profit, weight, capacity, dp_function)

        # Visualize the DP table
        self.play(FadeIn(dp_table))

    def get_dp_table(self, profit, weight, capacity, dp_function):
        # Get DP table values
        dp_values = dp_function(profit, weight, capacity)

        # Create a Matrix to represent the DP table
        dp_table = Matrix(dp_values)

        # Set row and column labels
        dp_table.add_row_labels([""] + [f"W={w}" for w in range(capacity + 1)])
        dp_table.add_column_labels([""] + [f"Item {i}" for i in range(len(profit))])

        # Highlight the cells for better visualization
        self.highlight_cells(dp_table, profit, weight)

        return dp_table

    def highlight_cells(self, dp_table, profit, weight):
        # Highlight cells based on the decision tree
        for i in range(len(profit)):
            for j in range(len(dp_table[0])):
                value = dp_table[i + 1][j + 1].get_value()
                if j >= weight[i]:
                    self.play(dp_table[i + 1][j + 1].animate.set_color(YELLOW), run_time=0.5)
                    self.play(dp_table[i][j + 1].animate.set_color(YELLOW), run_time=0.5)
                    if value > dp_table[i + 1][j - weight[i] + 1].get_value() + profit[i]:
                        self.play(dp_table[i + 1][j + 1].animate.set_color(RED), run_time=0.5)
                else:
                    self.play(dp_table[i + 1][j + 1].animate.set_color(RED), run_time=0.5)

        # Reset cell colors
        self.play(dp_table.animate.set_color(WHITE), run_time=0.5)
