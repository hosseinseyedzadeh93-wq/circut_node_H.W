```markdown
# Circuit Node Voltage Solver (Python)

This is a **Python-based circuit analysis tool** that solves electrical circuits using the **Node Voltage Method (Nodal Analysis)**.  
It can handle resistors, independent current sources, and a user-defined ground node. The program automatically constructs the nodal admittance matrix and computes node voltages using **NumPy**.

---

## Features

- Solves circuits using the **Node Voltage Method** (KCL-based analysis)
- Supports:
  - Any number of nodes
  - Any number of resistors
  - Independent current sources
- Automatic ground node handling
- Calculates:
  - Node voltages relative to ground
  - Currents through each resistor
- Efficient linear algebra computation using `numpy.linalg.solve`

---

## How It Works

The solver is based on **nodal analysis**, where Kirchhoff’s Current Law (KCL) is applied at each non-ground node:

```

Y · V = I

```

- `Y` → Nodal admittance matrix  
- `V` → Node voltage vector  
- `I` → Current injection vector  

Branch currents are then computed using Ohm’s Law:

```

I_R = (V_node1 - V_node2) / R

````

---

## Requirements

- Python 3.x  
- NumPy

Install NumPy if needed:

```bash
pip install numpy
````

---

## Usage

1. Clone the repository:

```bash
git clone https://github.com/your-username/circuit-node-voltage-solver.git
cd circuit-node-voltage-solver
```

2. Run the program:

```bash
python main.py
```

3. Input the requested information:

   * Number of nodes (including ground)
   * Node names
   * Ground node
   * Number of resistors and their connections
   * Number of current sources and their values

---

## Example Output

```
Node voltages:
V A = 5.0 V
V B = 2.5 V
V GND = 0 V

Branch currents:
I_R1 = 0.01 A
I_R2 = 0.005 A
```

---

## Future Improvements

* Support for voltage sources
* AC analysis with complex impedance
* GUI interface for easy input
* Netlist file input
* Enhanced error handling for singular matrices

---

## Author

Developed as an educational tool for **Electrical Engineering and Circuit Analysis**.
Open to improvements and contributions.

```
```

