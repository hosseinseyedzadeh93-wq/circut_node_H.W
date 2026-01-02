
.
# Circuit Node Voltage Solver (Python) This project is a **Python-based circuit analysis tool** that solves electrical circuits using the **Node Voltage Method (Nodal Analysis)**. It supports resistors, independent current sources, and a defined ground node. The program automatically builds the admittance matrix and solves for node voltages using **NumPy**. --- ## 📌 Features - Node Voltage Method (KCL-based analysis) - Supports: - Any number of nodes - Any number of resistors - Independent current sources - Automatic ground node handling - Computes: - Node voltages - Branch currents through resistors - Uses linear algebra (`numpy.linalg.solve`) --- ## 🧠 Theory Used This solver is based on **nodal analysis**, where: - Kirchhoff’s Current Law (KCL) is applied at each non-ground node - The circuit is represented as: \[ Y \cdot V = I \] where: - `Y` is the nodal admittance matrix - `V` is the vector of node voltages - `I` is the current injection vector --- ## 🛠 Requirements - Python 3.x - NumPy Install NumPy if not already installed: ```bash pip install numpy 

▶️ How to Run

Clone the repository:
git clone https://github.com/your-username/circuit-node-voltage-solver.git 

Navigate to the project directory:
cd circuit-node-voltage-solver 

Run the script:
python main.py 

🧾 User Inputs

When running the program, you will be prompted to enter:

Number of nodes (including ground)

Node names

Ground node

Number of resistors

First node

Second node

Resistance value (Ohms)

Number of current sources

Node

Current value (Amps)

📤 Output

Node Voltages

Voltage at each node relative to ground

Branch Currents

Current through each resistor calculated using:
[
I = \frac{V_1 - V_2}{R}
]

📁 Code Structure

Circuit class:

make_matrix() → builds admittance matrix and current vector

solve() → solves node voltages and branch currents

Uses dictionaries to map node names to matrix indices

📌 Example

Node voltages: V A = 5.0 V B = 2.5 V GND = 0 Branch currents: I_R1 = 0.01 I_R2 = 0.005 

🚀 Future Improvements

Support for voltage sources

AC analysis (complex impedance)

GUI interface

Netlist file input

Error checking for singular matrices

👨‍💻 Author

Developed for educational purposes in Electrical Engineering & Circuit Analysis.
Feel free to fork, improve, and use it in your projects!

