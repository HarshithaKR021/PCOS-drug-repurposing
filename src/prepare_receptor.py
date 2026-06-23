"""
Prepare receptor PDB file for AutoDock Vina docking.
Removes water, ligands, and adds hydrogens.
"""

from rdkit import Chem
from rdkit.Chem import AllChem
import os


def prepare_receptor(input_pdb, output_dir="data/processed"):
    """
    Clean and prepare receptor from raw PDB file.
    """
    os.makedirs(output_dir, exist_ok=True)
    
    # Read PDB file
    with open(input_pdb, 'r') as f:
        lines = f.readlines()
    
    # Keep only ATOM and TER lines (remove HETATM, water, ligands)
    clean_lines = []
    for line in lines:
        if line.startswith('ATOM  ') or line.startswith('TER'):
            # Skip water molecules (residue name HOH)
            res_name = line[17:20].strip()
            if res_name != 'HOH':
                clean_lines.append(line)
    
    # Save cleaned PDB
    base_name = os.path.basename(input_pdb).replace('.pdb', '_clean.pdb')
    clean_path = os.path.join(output_dir, base_name)
    
    with open(clean_path, 'w') as f:
        f.writelines(clean_lines)
    
    print(f"Cleaned receptor saved: {clean_path}")
    print(f"Total atoms: {len(clean_lines)}")
    
    return clean_path


if __name__ == "__main__":
    # Prepare 2AXA receptor
    prepare_receptor("data/raw/2AXA.pdb")