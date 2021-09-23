import matplotlib.pyplot as plt

class PlotVector:
    """Plotting several vectors in cartesian coordinate system"""

    def __init__(self, *vectors) -> None:
        x, y = [], []

        for vector in vectors:
            x.append(vector[0])
            y.append(vector[1])

        self.x, self.y = x, y
        # (0,0,...,0)
        self.originX = self.originY = tuple(0 for _ in range(len(x)))


    def plot(self) -> None:
        """Visualize vectors"""

        plt.quiver(self.originX, self.originY, self.x, self.y, scale=1, scale_units="xy", angles="xy")

        plt.xlim(-2,10)
        plt.ylim(-2,10)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.show()

