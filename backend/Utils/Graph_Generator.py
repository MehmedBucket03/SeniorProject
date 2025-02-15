import matplotlib.pyplot as plt

def generate_graph(data):
    """Generates and saves a line graph."""
    plt.plot(data)
    plt.savefig("backend/static/plots/graph.png")
