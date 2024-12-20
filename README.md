# IKT457-Learning-Systems-Project

This repository contains the code and data for the **"Predicting Hex Game Winners Using a Graph Tsetlin Machine"** project.

---

## Repository Structure

### 1. **Main Directory**
- **`hex_data.csv`**  
  A CSV file containing 2000 rows of 4x4 boards.

### 2. **Experiments**  
Contains the various experimental configurations and feature engineering attempts:
- **Jupyter Notebooks:**  
  - `base.ipynb`: The baseline feature-stripped GTM.
  - `coordinates_with_edge_types.ipynb`: Experiments with coordinates and edge-specific features.  
  - `coordinates_without_edge_types.ipynb`: Experiments with coordinates features but without edge-specific features.  
  - `edge_distance.ipynb`: Experiments with feature encoding distance from edges.  
  - `stone_count.ipynb`: Experiments with stone counts per row and column features.  
  - `touching_edge.ipynb`: Experiments with adjacency to board-edge features.  
  - `coordinates-edge_distance-stone_count-touching_edge.ipynb`: Combines all above features for a multi-feature experiment.

- **Modules Folder:**  
  - `dataloader.py`: Helperfunction to load data.  
  - `trainer.py`: Helperfunction to train the GTM.

### 3. **Complete**  
Includes the successful runs for 4x4, 5x5, and 6x6 which are featured in the report.
- `4x4.ipynb`: Training and evaluation on $4 \times 4$ Hex boards.  
- `5x5.ipynb`: Training and evaluation on $5 \times 5$ Hex boards.  
- `6x6.ipynb`: Training and evaluation on $6 \times 6$ Hex boards.
