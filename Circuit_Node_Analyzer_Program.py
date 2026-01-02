import numpy as np


class Circuit:
    def init(self, nodes, resistors, currents, ground):
        self.nodes = nodes
        self.resistors = resistors
        self.currents = currents
        self.ground = ground

        self.main_nodes = []
        for n in nodes:
            if n != ground:
                self.main_nodes.append(n)

        self.index = {}
        for i in range(len(self.main_nodes)):
            self.index[self.main_nodes[i]] = i

    def make_matrix(self):
        n = len(self.main_nodes)
        Y = np.zeros((n, n))
        I = np.zeros(n)

        for r in self.resistors:
            n1, n2, R = r
            g = 1 / R

            if n1 != self.ground:
                i = self.index[n1]
                Y[i][i] += g

            if n2 != self.ground:
                j = self.index[n2]
                Y[j][j] += g

            if n1 != self.ground and n2 != self.ground:
                i = self.index[n1]
                j = self.index[n2]
                Y[i][j] -= g
                Y[j][i] -= g

        for c in self.currents:
            node, value = c
            if node != self.ground:
                I[self.index[node]] += value

        return Y, I

    def solve(self):
        Y, I = self.make_matrix()
        V = np.linalg.solve(Y, I)

        voltages = {}
        for i in range(len(self.main_nodes)):
            voltages[self.main_nodes[i]] = V[i]
        voltages[self.ground] = 0

        branch_currents = []
        for r in self.resistors:
            n1, n2, R = r
            branch_currents.append((voltages[n1] - voltages[n2]) / R)

        return voltages, branch_currents


# ----------------------------
# user input
# ----------------------------
nodes = []
n = int(input("Number of nodes (including ground): "))
for i in range(n):
    nodes.append(input("Node name: "))

ground = input("Ground node: ")

resistors = []
m = int(input("Number of resistors: "))
for i in range(m):
    print("Resistor", i + 1)
    n1 = input("First node: ")
    n2 = input("Second node: ")
    R = float(input("Resistance value: "))
    resistors.append((n1, n2, R))

currents = []
k = int(input("Number of current sources: "))
for i in range(k):
    node = input("Current source node: ")
    I = float(input("Current value: "))
    currents.append((node, I))

circuit = Circuit(nodes, resistors, currents, ground)
voltages, branch_currents = circuit.solve()

print("\nNode voltages:")
for v in voltages:
    print("V", v, "=", round(voltages[v], 4))

print("\nBranch currents:")
for i in range(len(branch_currents)):
    print("I_R", i + 1, "=", round(branch_currents[i], 4))


# I used AI tools only for debugging; the program was written by me.