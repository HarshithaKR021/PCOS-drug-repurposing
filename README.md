Author: Harshitha K R
# PCOS/PMOS Drug Repurposing: Targeting Androgen Receptor

Computational screening of natural products against the Androgen Receptor (AR) to identify candidates for Polycendocrine Metabolic Ovarian Syndrome (PCOS/PMOS).

## Overview
- **Target:** Androgen Receptor Ligand-Binding Domain 
- **Methods:** Molecular docking (PyRx), ADMET profiling
- **Status:** Work in progress

## Repository Structure
data/         - Raw and processed datasets
notebooks/    - Analysis notebooks
src/          - Python scripts
figures/      - Result plots

## Tools Used
- PyRx
- SWISS-ADME
- Python (RDKit, Pandas, Matplotlib)

## Citation
If you use this code, please cite the upcoming manuscript.

## License
MIT License

## Results

### Molecular Docking
| Rank | Compound | Binding Affinity (kcal/mol) | Source |
|------|----------|----------------------------|--------|
| 1 | Naringenin | -7.8 | Natural product |
| 2 | Kaempferol | -7.2 | Natural product |
| 3 | Quercetin | -7.1 | Natural product |
| 4 | Resveratrol | -6.8 | Natural product |
| 5 | Metformin | -5.2 | FDA approved |

### ADMET Profile
All compounds pass Lipinski's Rule of 5 and show high GI absorption with low hepatotoxicity risk.

### Conclusion
Naringenin, kaempferol, and quercetin show promising binding to the Androgen Receptor and favorable drug-like properties, warranting further experimental validation for PCOS/PMOS treatment.

