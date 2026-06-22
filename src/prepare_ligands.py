"""
Prepare ligands for molecular docking.
Converts SMILES to 3D structures.
"""

import pandas as pd
from rdkit import Chem
from rdkit.Chem import AllChem
import os


def smiles_to_pdb(smiles, name, output_dir="data/processed"):
    """
    Convert SMILES string to a 3D PDB file.
    """
    # Create output folder if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Convert SMILES to molecule
    mol = Chem.MolFromSmiles(smiles)
    
    if mol is None:
        print(f"  ✗ Failed: {name} - invalid SMILES")
        return False
    
    # Add hydrogens and build 3D structure
    mol = Chem.AddHs(mol)
    AllChem.EmbedMolecule(mol, randomSeed=42)
    AllChem.MMFFOptimizeMolecule(mol)
    
    # Save as PDB file
    pdb_path = os.path.join(output_dir, f"{name}.pdb")
    Chem.MolToPDBFile(mol, pdb_path)
    
    print(f"  ✓ Success: {name}")
    return True


def batch_prepare(csv_path="data/raw/ligand_library.csv"):
    """
    Prepare all ligands from the CSV file.
    """
    df = pd.read_csv(csv_path)
    print(f"Preparing {len(df)} compounds...\n")
    
    success = 0
    for _, row in df.iterrows():
        result = smiles_to_pdb(row['smiles'], row['name'])
        if result:
            success += 1
    
    print(f"\nDone: {success}/{len(df)} compounds ready for docking")


if __name__ == "__main__":
    batch_prepare()