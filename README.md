# IKT457-Learning-Systems-Project

This repository contains the code and data for the **"Predicting Hex Game Winners Using a Graph Tsetlin Machine"** project. The aim of this project is to classify outcomes in the strategy game Hex using the Graph Tsetlin Machine (GTM). The repository is organized to streamline the experiments and analysis conducted on various board sizes.

---

## Repository Structure

### 1. **Main Directory**
- **`README.md`**  
  This file, providing an overview of the repository and instructions for usage.
- **`hex_data.csv`**  
  A CSV file containing the raw Hex board data (states and outcomes) used for training and evaluation.  

### 2. **Experiments**  
Contains the various experimental configurations and feature engineering attempts:
- **Jupyter Notebooks:**  
  - `base.ipynb`: A baseline implementation for understanding GTM performance.  
  - `coordinates_with_edge_types.ipynb`: Experiments with coordinates and edge-specific features.  
  - `coordinates_without_edge_types.ipynb`: Experiments without edge-specific features.  
  - `edge_distance.ipynb`: Tests features encoding distance from edges.  
  - `stone_count.ipynb`: Introduces aggregated statistics like stone counts per row or column.  
  - `touching_edge.ipynb`: Analyzes configurations emphasizing adjacency to board edges.  
  - `coordinates-edge_distance-stone_count-touching_edge.ipynb`: Combines all above features for a multi-feature experiment.

- **Modules Folder:**  
  - `dataloader.py`: Handles loading and preprocessing of Hex board data into graph representations.  
  - `trainer.py`: Contains the GTM training logic, including parameter tuning and monitoring.

### 3. **Complete**  
Includes the consolidated experiments on Hex boards of different sizes:
- `4x4.ipynb`: Training and evaluation on $4 \times 4$ Hex boards.  
- `5x5.ipynb`: Training and evaluation on $5 \times 5$ Hex boards.  
- `6x6.ipynb`: Training and evaluation on $6 \times 6$ Hex boards.  

---

## Key Components

### 1. **Data Preparation**  
Hex board states are converted into graph structures using `dataloader.py`. Nodes represent cells, while edges represent adjacency between cells. Features like cell occupancy, coordinates, and optional attributes (e.g., edge proximity) are encoded.

### 2. **Model Training**  
Training is conducted via the `trainer.py` script. The GTM parameters, such as clause count, specificity ($s$), and thresholds, are systematically tuned. Training involves clause evaluation and refinement to classify Hex winners based on board configurations.

### 3. **Feature Engineering**  
Extensive experiments are conducted to assess the impact of features:
- **Basic Features:** Cell occupancy and coordinates.  
- **Engineered Features:** Distance from edges, proximity categories, and stone counts.  
- The `experiments` folder notebooks detail the performance of each feature set.

### 4. **Performance Evaluation**  
Testing is performed on $4 \times 4$, $5 \times 5$, and $6 \times 6$ boards. Results include:
- **Accuracy:** Achieving up to 98% on smaller boards.  
- **Training Stability:** Analyzing convergence rates and resolving stalls.  
- **Clause Analysis:** Assessing the interpretability of learned clauses.

---

## How to Run

1. **Setup**  
   Ensure Python and Jupyter Notebook are installed. Install dependencies using:  
   ```bash
   pip install -r requirements.txt
