import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.axes as ax
from matplotlib_venn import venn2, venn2_unweighted, venn2_circles
import numpy

class Diagram():
    def union(self,set_a, set_b):
        """Return the union of two sets."""
        return set_a | set_b


    def difference(self,set_a, set_b):
        """Return the difference of two sets."""
        return set_a - set_b


    def intersection(self,set_a, set_b):
        """Return the intersection of two sets."""
        return set_a & set_b


    def draw_venn(self,set_a, set_b, operation):
        """Draw a Venn diagram based on the given sets and operation."""
        if operation == "union":
            union_result = self.union(set_a, set_b)
            items = [
                sorted(self.difference(set_a, set_b)),
                sorted(self.difference(set_b, set_a)),
                sorted(self.intersection(set_a, set_b)),
            ]
            venn2_unweighted((items), set_labels=("A", "B"))
            plt.title(f"Union of Sets A and B\n{union_result}")
        elif operation == "intersection":
            intersection_result = self.intersection(set_a, set_b)
            items = [
                sorted(self.difference(set_a, set_b)),
                sorted(self.difference(set_b, set_a)),
                sorted(self.intersection(set_a, set_b)),
            ]
            venn2_unweighted((items), set_labels=("A", "B"))
            plt.title(f"Intersection of Sets A and B\n{intersection_result}")
        elif operation == "difference":
            diff_A_B = self.difference(set_a, set_b)
            diff_B_A = self.difference(set_b, set_a)
            intersection_result = self.intersection(set_a, set_b)
            venn2_circles(subsets=(len(diff_A_B), len(diff_B_A), len(intersection_result)))
            plt.title(f"Difference of Sets A and B\n{diff_A_B}")

            plt.text(
                -0.5, 0, diff_A_B, ha="center", va="center", fontsize=12, color="black"
            )
            plt.text(0.5, 0, diff_B_A, ha="center", va="center", fontsize=12, color="black")
            plt.text(
                -0.03,
                0,
                intersection_result,
                ha="center",
                va="center",
                fontsize=12,
                color="black",
            )
        elif operation == "complement":
            diff_B_A = self.difference(set_a, set_b)
            fig, ax = plt.subplots()

            # Create a rectangle that represents the universal set
            universal_rect = patches.Rectangle(
                (-2.5, -2.5), 5, 5, linewidth=2, edgecolor="r", facecolor="pink"
            )
            ax.add_patch(universal_rect)

            # Create a circle that represents set A
            set_a_circle = patches.Circle(
                (0, 0), 1, linewidth=2, edgecolor="b", facecolor="white"
            )
            ax.add_patch(set_a_circle)

            # Annotate the elements of set A inside the circle
            for i, element in enumerate(set_b):
                ax.text(
                    -0.5 + i * 0.25,
                    0,
                    str(element),
                    color="blue",
                    fontsize=12,
                    ha="center",
                )

                # Annotate the elements of the complement of set A outside the circle

            for i, element in enumerate(set_a - set_b):

                ax.text(
                    -0.45 + i * 0.25,
                    -1.2,
                    str(element),
                    color="black",
                    fontsize=12,
                    ha="center",
                )

            # Set the limits of the plot
            ax.set_xlim(-2, 2)
            ax.set_ylim(-2, 2)

            # Set the aspect of the plot to be equal
            ax.set_aspect("equal")

            # Set the title of the plot
            ax.set_title("Complement of Set A in the Universal Set")

            # Remove the axes
            plt.axis("off")

            plt.title(f"Complement of Sets A  (U - A)\nUniversal set:{set_a}\nSet A:{set_b}")
            # plt.text(
            # -0.6, 0, diff_B_A, ha="center", va="center", fontsize=12, color="black"
            # )
        plt.show()


# Get user input for sets and operation
# operation = input(
#     "Enter the set operation (union, intersection, difference, complement): "
# )
# if operation == "complement":
#     set_a = set(
#         map(
#             int,
#             input("Enter elements of the universal set separated by spaces: ").split(),
#         )
#     )
#     set_b = set(
#         map(int, input("Enter elements of set A separated by spaces: ").split())
#     )
# else:
#     set_a = set(
#         map(int, input("Enter elements of set A separated by spaces: ").split())
#     )
#     set_b = set(
#         map(int, input("Enter elements of set B separated by spaces: ").split())
#     )


# # Perform the requested set operation and visualize it
# if operation in ["union", "intersection", "difference", "complement"]:
#     draw_venn(set_a, set_b, operation)
# else:
#     print(
#         "Invalid operation! Please enter one of: union, intersection, difference, complement."
#     )
