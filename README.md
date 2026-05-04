1. **Clone Repository**
    ```
    git clone https://github.com/yourusername/cloud-stable-matching.git
    cd cloud-stable-matching
    ```

2.  **Install dependencies:**
    ```bash
    pip install pandas numpy scipy seaborn matplotlib
    ```

3.  **Run the script:**
    You can run the provided `.py` file or import the code into a# CloudMatch: Gale-Shapley Stable Matching for Cloud Services

This project implements a modified **Gale-Shapley Stable Matching Algorithm** to pair Cloud Service Providers (AWS, Azure, GCP) with clients based on technical requirements, budget constraints, and provider reputation. 

It compares the performance of the **Stable Matching** approach against **Greedy** and **Random** baselines using metrics like blocking pairs, client satisfaction, and provider profit.

---

## 🚀 Features

*   **Real-World Data Integration:** Scrapes/defines instance data from AWS (T3, M5, C5, R5), Azure (D-series v6/v7), and GCP (E2, N1, N2).
*   **Synthetic Service Generation:** Generates 200+ services with calibrated attributes (latency, bandwidth, and SLA-based trust scores).
*   **Dynamic Preference Logic:**
    *   **Clients:** Rank services based on the lowest cost among those meeting their hardware and trust requirements.
    *   **Services:** Rank clients based on their total budget (economic tier).
*   **Evaluation Suite:** Includes statistical validation (KS-Test), profit analysis, and stability checking (counting **Blocking Pairs**).
*   **Visualizations:** Rich data plots using Seaborn and Matplotlib for cost distribution, profit per provider, and algorithm comparison.

---

## 🛠️ Tech Stack

*   **Language:** Python 3.x
*   **Data Manipulation:** `pandas`, `numpy`
*   **Analysis:** `scipy` (KS-Test)
*   **Visualization:** `matplotlib`, `seaborn`
*   **Environment:** Optimized for Jupyter Notebook / Google Colab

---

## 📊 How It Works

### 1. Data Calibration
The system starts with real pricing data. It then uses a log-normal distribution to generate synthetic client requirements and additional service attributes to ensure the simulation reflects real-world cloud market volatility.

### 2. The Matching Algorithm
The core is the **Gale-Shapley Algorithm**, which ensures that no "blocking pairs" exist. A blocking pair occurs if a client and a service both prefer each other over their current matches.

### 3. Economic Modeling
The project calculates platform profit by assuming:
*   **Operational Cost:** 70% of the service bundle cost.
*   **Net Profit:** 30% margin, analyzed across AWS, Azure, and GCP.

---

## 📈 Evaluation Results

The script generates a comprehensive comparison table:

| Metric | Stable Matching | Greedy Baseline | Random Baseline |
| :--- | :--- | :--- | :--- |
| **Match Count** | High | Medium | Medium |
| **Blocking Pairs** | **0 (Stable)** | High | Very High |
| **Client Sat. Rank** | Optimized | Sub-optimal | Poor |
| **Provider Sat. Rank**| Optimized | Sub-optimal | Poor |

---

## 🎥 Project Demo Guideline

To demonstrate this project effectively, follow these steps to showcase the algorithm's intelligence and economic viability.

### **Step 1: Environment & Initialization**
*   **Action:** Run the first few cells to import libraries and load the cloud provider datasets (AWS, Azure, GCP).
*   **Highlight:** Point out the **Total Instances Loaded**. This shows the foundation of real-world pricing that informs the simulation.

### **Step 2: The Trust & Calibration Showcase**
*   **Action:** Execute the "Synthetic Service Generation" section.
*   **Observe:** Look at the **KDE Plot** (Kernel Density Estimate). 
*   **Talking Point:** Explain that the **KS-Test (Kolmogorov-Smirnov)** ensures our synthetic "Cloud Market" isn't just random noise—it statistically mimics the distribution of real AWS/Azure/GCP pricing.

### **Step 3: Preference Ranking Logic**
*   **Action:** Show the code generating `client_prefs` and `service_prefs`.
*   **Insight:** Explain the "Economic Tiering" (Platinum to Iron). This demonstrates that the algorithm isn't just matching technical specs; it’s simulating a **market economy** where high-budget clients get priority.

### **Step 4: The Stable Matching Execution**
*   **Action:** Run the Gale-Shapley loop.
*   **Demo Focus:** Watch the `iteration_count` and `proposal_count`. 
*   **Key Result:** Note the **Blocking Pairs** count in the Stable Matching column. In a successful demo, this must be **0**, proving the stability of the CloudMatch solution.

### **Step 5: Visualizing Profit & Fairness**
*   **Action:** Scroll to the Seaborn bar charts.
*   **Highlights:**
    *   **Profit Distribution:** Which provider (AWS vs Azure vs GCP) is most "profitable" under this matching?
    *   **Client Satisfaction:** Compare the average "Rank" of matches. A lower rank (closer to 1) means clients got their top-choice cloud instance.

---

## 💻 Installation & Usage

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/cloud-stable-matching.git
    cd cloud-stable-matching
    ```

2.  **Install dependencies:**
    ```bash
    pip install pandas numpy scipy seaborn matplotlib
    ```

3.  **Run the script:**
    You can run the provided `.py` file or import the code into a **Google Colab** environment to view the inline visualizations.

---

## 📝 License
This project is open-source and available under the [MIT License](LICENSE).# CloudMatch: Gale-Shapley Stable Matching for Cloud Services

This project implements a modified **Gale-Shapley Stable Matching Algorithm** to pair Cloud Service Providers (AWS, Azure, GCP) with clients based on technical requirements, budget constraints, and provider reputation. 

It compares the performance of the **Stable Matching** approach against **Greedy** and **Random** baselines using metrics like blocking pairs, client satisfaction, and provider profit.

---

## 🚀 Features

*   **Real-World Data Integration:** Scrapes/defines instance data from AWS (T3, M5, C5, R5), Azure (D-series v6/v7), and GCP (E2, N1, N2).
*   **Synthetic Service Generation:** Generates 200+ services with calibrated attributes (latency, bandwidth, and SLA-based trust scores).
*   **Dynamic Preference Logic:**
    *   **Clients:** Rank services based on the lowest cost among those meeting their hardware and trust requirements.
    *   **Services:** Rank clients based on their total budget (economic tier).
*   **Evaluation Suite:** Includes statistical validation (KS-Test), profit analysis, and stability checking (counting **Blocking Pairs**).
*   **Visualizations:** Rich data plots using Seaborn and Matplotlib for cost distribution, profit per provider, and algorithm comparison.

---

## 🛠️ Tech Stack

*   **Language:** Python 3.x
*   **Data Manipulation:** `pandas`, `numpy`
*   **Analysis:** `scipy` (KS-Test)
*   **Visualization:** `matplotlib`, `seaborn`
*   **Environment:** Optimized for Jupyter Notebook / Google Colab

---

## 📊 How It Works

### 1. Data Calibration
The system starts with real pricing data. It then uses a log-normal distribution to generate synthetic client requirements and additional service attributes to ensure the simulation reflects real-world cloud market volatility.

### 2. The Matching Algorithm
The core is the **Gale-Shapley Algorithm**, which ensures that no "blocking pairs" exist. A blocking pair occurs if a client and a service both prefer each other over their current matches.

### 3. Economic Modeling
The project calculates platform profit by assuming:
*   **Operational Cost:** 70% of the service bundle cost.
*   **Net Profit:** 30% margin, analyzed across AWS, Azure, and GCP.

---

## 📈 Evaluation Results

The script generates a comprehensive comparison table:

| Metric | Stable Matching | Greedy Baseline | Random Baseline |
| :--- | :--- | :--- | :--- |
| **Match Count** | High | Medium | Medium |
| **Blocking Pairs** | **0 (Stable)** | High | Very High |
| **Client Sat. Rank** | Optimized | Sub-optimal | Poor |
| **Provider Sat. Rank**| Optimized | Sub-optimal | Poor |

---

## 🎥 Project Demo Guideline

To demonstrate this project effectively, follow these steps to showcase the algorithm's intelligence and economic viability.

### **Step 1: Environment & Initialization**
*   **Action:** Run the first few cells to import libraries and load the cloud provider datasets (AWS, Azure, GCP).
*   **Highlight:** Point out the **Total Instances Loaded**. This shows the foundation of real-world pricing that informs the simulation.

### **Step 2: The Trust & Calibration Showcase**
*   **Action:** Execute the "Synthetic Service Generation" section.
*   **Observe:** Look at the **KDE Plot** (Kernel Density Estimate). 
*   **Talking Point:** Explain that the **KS-Test (Kolmogorov-Smirnov)** ensures our synthetic "Cloud Market" isn't just random noise—it statistically mimics the distribution of real AWS/Azure/GCP pricing.

### **Step 3: Preference Ranking Logic**
*   **Action:** Show the code generating `client_prefs` and `service_prefs`.
*   **Insight:** Explain the "Economic Tiering" (Platinum to Iron). This demonstrates that the algorithm isn't just matching technical specs; it’s simulating a **market economy** where high-budget clients get priority.

### **Step 4: The Stable Matching Execution**
*   **Action:** Run the Gale-Shapley loop.
*   **Demo Focus:** Watch the `iteration_count` and `proposal_count`. 
*   **Key Result:** Note the **Blocking Pairs** count in the Stable Matching column. In a successful demo, this must be **0**, proving the stability of the CloudMatch solution.

### **Step 5: Visualizing Profit & Fairness**
*   **Action:** Scroll to the Seaborn bar charts.
*   **Highlights:**
    *   **Profit Distribution:** Which provider (AWS vs Azure vs GCP) is most "profitable" under this matching?
    *   **Client Satisfaction:** Compare the average "Rank" of matches. A lower rank (closer to 1) means clients got their top-choice cloud instance.

---

## 💻 Installation & Usage

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/cloud-stable-matching.git
    cd cloud-stable-matching
    ```

2.  **Install dependencies:**
    ```bash
    pip install pandas numpy scipy seaborn matplotlib
    ```

3.  **Run the script:**
    You can run the provided `.py` file or import the code into a **Google Colab** environment to view the inline visualizations.

---

## 📝 License
This project is open-source and available under the [MIT License](LICENSE).

---
*Generated for the Gale-Shapley Stable Matching Algorithm Project.*
