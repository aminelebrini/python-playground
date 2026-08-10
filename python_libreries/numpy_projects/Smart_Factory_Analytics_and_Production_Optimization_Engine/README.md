# 🏭 Smart Factory Analytics & Production Optimization Engine

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/Library-NumPy-0172B2.svg)](https://numpy.org/)
[![SciPy](https://img.shields.io/badge/Library-SciPy-8CAAE6.svg)](https://scipy.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An industrial decision-support system built purely on **NumPy** and **SciPy**. This engine translates manufacturing constraints into mathematical models to optimize production planning, simulate stochastic market demand, forecast machinery health, and calculate executive financial metrics.

---

## 📌 Project Architecture

The system uses a modular **Object-Oriented Programming (OOP)** framework composed of 4 core mathematical modules:

```text
┌─────────────────────────────────────────────────────────────────┐
│                    Factory Analytics Console                     │
│               (KPI Calculation & Financial Metrics)              │
└───────────────▲─────────────────▲─────────────────▲─────────────┘
                │                 │                 │
┌───────────────┴─────────┐ ┌─────┴──────────┐ ┌────┴────────────┐
│   Demand Simulator      │ │ Production     │ │ Reliability     │
│   (Monte Carlo Engine)  │ │ Optimizer      │ │ Engine          │
│                         │ │ (Linear Prog)  │ │ (Markov Chain)  │
└─────────────────────────┘ └────────────────┘ └─────────────────┘
```

## 🚀 Key Features

- 🎲 **Monte Carlo Demand Simulation (NumPy)** — Generates stochastic market demand scenarios over multi-period horizons using statistical probability distributions.
- ⚡ **Multi-Product Production Optimizer (SciPy)** — Solves profit-maximization problems using constrained linear programming (`scipy.optimize.linprog`) under factory resource limits.
- ⚙️ **Equipment Reliability Forecast (NumPy)** — Models machine degradation and maintenance states across time using discrete-time Markov Transition Matrices.
- 📊 **Executive Analytics Console (NumPy)** — Computes financial KPIs, including Net Present Value (NPV) and Monte Carlo percentile risk metrics.

## 🛠️ Tech Stack & Requirements

- **Language:** Python 3.10+
- **Core Libraries:**
  - `numpy` — Vectorized matrix operations & linear algebra.
  - `scipy` — Constrained optimization solvers (`scipy.optimize`).

## 🧮 Mathematical Modeling Summary

### 1. Production Optimization (Linear Programming)

$$\max Z = c^T x \quad \text{subject to} \quad A \cdot x \le b, \quad x \ge 0$$

- $c$: Unit profit vector per product
- $x$: Decision variable vector (production quantities)
- $A$: Resource usage matrix (hours/material per product)
- $b$: Maximum capacity limits

### 2. Machinery Health (Markov Chain Exponentiation)

$$S_t = S_0 \cdot P^t$$

- $S_0$: Initial state vector of machine fleet
- $P$: State transition probability matrix
- $t$: Projection horizon (in months)

## ⚙️ Installation & Usage

Clone the repository:

```bash
git clone https://github.com/your-username/smart-factory-optimizer.git
cd smart-factory-optimizer
```

Install dependencies:

```bash
pip install numpy scipy
```

Run the main engine:

```bash
python main.py
```

## 📄 Project Specifications (Cahier des Charges)

**Module 1: Demand Simulation Engine**
- Generates a 3D matrix of shape `(Simulations, Products, Time Periods)`.
- Applies non-negativity bounds to prevent negative demand modeling.

**Module 2: Production Plan Optimizer**
- Formulates resource allocation matrices.
- Employs the HiGHS dual-simplex solver via `scipy.optimize.linprog`.

**Module 3: Machine Reliability Engine**
- Tracks state transitions: `[Operational, Needs Maintenance, Out of Order]`.
- Computes matrix powers ($P^t$) to forecast asset availability.

**Module 4: Financial Analytics Console**
- Calculates NPV given a monthly discount rate $r$.
- Provides terminal formatted summaries of financial outcomes.

## 📜 License

This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).
