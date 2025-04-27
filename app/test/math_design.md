Here’s a structured mathematical framework to implement **phase-based percentage triggers** and **yield aggregation** for your fuzzy logic system:

---

### **1. Phase Segmentation & Thresholds**
Define **success thresholds** for each phase to trigger progression to the next stage. 
*(Example thresholds based on Starke Ayres guidelines)*:

| **Phase**              | **Success Threshold** | **Failure Action**                          |
|-------------------------|-----------------------|---------------------------------------------|
| Germination             | ≥80%                  | Resow or adjust soil conditions.            |
| Vegetative Growth       | ≥75%                  | Increase fertilization or irrigation.       |
| Flowering               | ≥70%                  | Optimize temperature/calcium.               |
| Fruit Set               | ≥65%                  | Improve pollination or pest control.        |
| Green Fruit             | ≥60%                  | Adjust potassium/magnesium.                 |
| Mature Green            | ≥55%                  | Monitor ethylene exposure.                  |
| Color Breaker           | ≥50%                  | Extend ripening time.                       |
| Half-Ripe               | ≥45%                  | Adjust harvest timing.                      |
| Red/Full Ripe           | ≥40%                  | Harvest immediately.                        |

---

### **2. Mathematics for Phase Success Percentage**
Each phase’s success percentage \( P_i \) is calculated using fuzzy logic outputs (e.g., germination success = 85%). 
**Formula**: 
\[
P_i = \text{Fuzzy Output for Phase } i \quad (0 \leq P_i \leq 1)
\]

**Example**: 
- Germination inputs: Soil temp = 25°C, moisture = 60%. 
- Fuzzy rules → Germination success = 85% (\( P_1 = 0.85 \)).

---

### **3. Phase Transition Logic**
A phase progresses to the next **only if** its success percentage meets the threshold. 
**Formula**: 
\[
\text{Proceed to Phase } i+1 \text{ if } P_i \geq \text{Threshold}_i
\]
**Failure Handling**: 
- If \( P_i < \text{Threshold}_i \), apply corrective actions (e.g., extend phase duration, adjust inputs). 
- Recalculate \( P_i \) until the threshold is met or the crop fails.

---

### **4. Aggregating Phase Percentages for Yield Prediction**
Assign **weights** (\( W_i \)) to phases based on their impact on yield (e.g., flowering is critical). 
**Weighting Example**: 

| **Phase**              | **Weight (\( W_i \))** | Rationale                                     |
|-------------------------|------------------------|-----------------------------------------------|
| Germination             | 0.10                   | Foundation for plant health.                  |
| Vegetative Growth       | 0.15                   | Root/canopy development.                      |
| Flowering               | 0.20                   | Directly impacts fruit count.                 |
| Fruit Set               | 0.20                   | Determines viable fruit.                      |
| Green → Full Ripe       | 0.35                   | Fruit quality and marketability.              |

**Aggregated Health Score (\( H \))** 
\[
H = \sum_{i=1}^n (P_i \times W_i)
\]

**Example**: 
\[
H = (0.85 \times 0.10) + (0.75 \times 0.15) + \dots + (0.90 \times 0.35) = 0.76 \quad (76\%)
\]

---

### **5. Mapping Health Score to Yield**
Use a **linear or fuzzy function** to convert \( H \) to yield (tons/ha). 

#### **Linear Model** 
\[
\text{Yield} = H \times \text{Max Potential Yield}
\]
*Example*: 
If max yield = 15 tons/ha and \( H = 0.76 \): 
\[
\text{Yield} = 0.76 \times 15 = 11.4 \text{ tons/ha}
\]

#### **Fuzzy Model** 
Define output MFs for yield: 
- **Low** (0–5 tons/ha): \( H < 0.4 \) 
- **Medium** (5–10 tons/ha): \( 0.4 \leq H < 0.7 \) 
- **High** (10–15 tons/ha): \( H \geq 0.7 \)

---

### **6. Penalty Adjustments**
Account for **critical phase failures** (e.g., germination <30% → crop failure): 
\[
\text{Yield} =
\begin{cases}
0 & \text{if } P_1 < 0.3 \text{ (germination failure)} \\
H \times \text{Max Yield} & \text{otherwise}
\end{cases}
\]

---

### **7. Implementation Workflow**
1. **Phase 1 (Germination)**: Calculate \( P_1 \). If \( P_1 \geq 0.8 \), proceed. 
2. **Phase 2 (Vegetative Growth)**: Calculate \( P_2 \). If \( P_2 \geq 0.75 \), proceed. 
3. **Repeat** for all phases. 
4. **Aggregate**: Compute \( H = \sum (P_i \times W_i) \). 
5. **Yield Prediction**: Apply linear/fuzzy model to estimate tons/ha.

---

### **Example Calculation**
Assume phase percentages and weights: 
| Phase               | \( P_i \) | \( W_i \) | \( P_i \times W_i \) |
|---------------------|-----------|-----------|----------------------|
| Germination         | 0.85      | 0.10      | 0.085                |
| Vegetative Growth   | 0.75      | 0.15      | 0.113                |
| Flowering           | 0.70      | 0.20      | 0.140                |
| Fruit Set           | 0.65      | 0.20      | 0.130                |
| Green → Full Ripe   | 0.90      | 0.35      | 0.315                |
| **Total**           |           | **1.00**  | **0.783**            |

\[
\text{Yield} = 0.783 \times 15 = 11.7 \text{ tons/ha}
\]

---

### **8. Tools for Implementation**
- **Fuzzy Logic Libraries**: Python `scikit-fuzzy` for phase-specific \( P_i \). 
- **Linear Algebra**: NumPy for aggregation (\( H \)). 
- **Visualization**: Matplotlib/Seaborn for phase thresholds and yield curves.

---

This framework ensures phase dependencies are respected, thresholds drive transitions, and aggregated scores reflect real-world yield outcomes. Adjust weights and thresholds based on crop variety (determinate/indeterminate) and local conditions.