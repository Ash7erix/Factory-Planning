# Factory-Planning

## Mathematical Formulation

### Decision Variables:
Let \( x_{ij} \) be the number of units of product \( i \) produced in month \( j \), where:
- \( i = 1, 2, \dots, 7 \) (for 7 products)
- \( j = 1, 2, \dots, 6 \) (for 6 months)

### Objective Function:
The objective is to maximize the total profit, which is the contribution per unit multiplied by the number of units produced, minus the stock holding cost and other constraints.

$$
\text{Maximize} \quad Z = \sum_{i=1}^{7} \sum_{j=1}^{6} C_i \cdot x_{ij} - \text{Stock Cost}
$$

Where:
- \( C_i \) is the contribution to profit per unit for product \( i \).
- The **Stock Cost** is calculated as \( 0.5 \times \text{stock} \), and we have stock balance constraints to ensure the stock at the end of June is 50 units for each product.

### Constraints:

#### 1. **Marketing Constraints (Demand)**:
For each product \( i \) and month \( j \), the production should not exceed the available demand:

\[
x_{ij} \leq \text{Demand}_{ij}, \quad \forall i, j
\]

Where:
- \( \text{Demand}_{ij} \) is the demand for product \( i \) in month \( j \).

#### 2. **Machine Capacity Constraints**:
Each machine has a limited number of working hours per month. For each process (e.g., grinding, vertical drilling), the total time spent on that process by all products should not exceed the available machine hours, taking into account the number of machines available and the maintenance downtime in each month.

\[
\sum_{i=1}^{7} \text{Time}_{p, i} \cdot x_{ij} \leq \text{Available Hours}_{p, j}, \quad \forall p, j
\]

Where:
- \( \text{Time}_{p, i} \) is the time required for product \( i \) on process \( p \).
- \( \text{Available Hours}_{p, j} \) is the number of available hours for process \( p \) in month \( j \), considering the machine availability and maintenance.

#### 3. **Stock Balance Constraints**:
The stock of each product should be carried forward from one month to the next, ensuring that the total stock at the end of June for each product is exactly 50 units. This is formulated as:

\[
\text{Stock at end of month } j = \text{Stock at end of month } (j-1) + \text{Production in month } j - \text{Demand in month } j
\]

For the final month (June), we enforce that the stock should be exactly 50 units for each product:

\[
\text{Stock}_{i, 6} = 50, \quad \forall i
\]

#### 4. **Maintenance Constraints**:
Each machine may be unavailable during certain months due to maintenance. This constraint ensures that the total production time on each machine does not exceed the available machine hours, considering the downtime. For example, if 1 grinder is down in January, the available machine hours for grinding in January would be reduced accordingly.

- If \( m \) machines are down for a process in month \( j \), then the available hours for that process in month \( j \) would be:

\[
\text{Available Hours}_{p, j} = (N_p - m) \times \text{Total Machine Hours Per Month}
\]

Where:
- \( N_p \) is the total number of machines available for process \( p \) (e.g., 4 for grinding).
- \( m \) is the number of machines down during month \( j \).

### Final Mathematical Formulation:

#### **Objective:**
\[
\text{Maximize} \quad Z = \sum_{i=1}^{7} \sum_{j=1}^{6} C_i \cdot x_{ij} - 0.5 \times \left( \sum_{i=1}^{7} \text{Stock}_{i, 6} \right)
\]

#### **Subject to:**

1. **Marketing Constraints:**
\[
x_{ij} \leq \text{Demand}_{ij}, \quad \forall i, j
\]

2. **Machine Capacity Constraints:**
\[
\sum_{i=1}^{7} \text{Time}_{p, i} \cdot x_{ij} \leq \text{Available Hours}_{p, j}, \quad \forall p, j
\]

3. **Stock Balance Constraints:**
\[
\text{Stock}_{i, j} = \text{Stock}_{i, j-1} + x_{ij} - \text{Demand}_{ij}, \quad j = 1, 2, \dots, 6
\]

4. **Stock End Constraint (for June):**
\[
\text{Stock}_{i, 6} = 50, \quad \forall i
\]

5. **Non-negativity Constraints:**
\[
x_{ij} \geq 0, \quad \forall i, j
\]
