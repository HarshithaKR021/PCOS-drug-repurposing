"""
Batch molecular docking using AutoDock Vina.
"""

import subprocess
import pandas as pd
import os
from pathlib import Path


def dock_ligand(ligand_name, config_file="config.txt", output_dir="data/processed"):
    """
    Dock a single ligand and extract top affinity.
    """
    ligand_path = f"{output_dir}/{ligand_name}.pdbqt"
    out_path = f"{output_dir}/{ligand_name}_docked.pdbqt"
    log_path = f"{output_dir}/{ligand_name}_log.txt"
    
    cmd = [
        "vina",
        "--config", config_file,
        "--ligand", ligand_path,
        "--out", out_path,
        "--log", log_path
    ]
    
    print(f"Docking {ligand_name}...")
    subprocess.run(cmd, check=True)
    
    # Parse log file for top affinity
    affinity = None
    with open(log_path) as f:
        for line in f:
            if line.strip().startswith("1 "):
                parts = line.split()
                affinity = float(parts[1])
                break
    
    print(f"  Top affinity: {affinity} kcal/mol")
    return affinity


def dock_all(ligands, config_file="config.txt"):
    """
    Dock all ligands and return results table.
    """
    results = []
    for ligand in ligands:
        try:
            affinity = dock_ligand(ligand, config_file)
            results.append({
                "ligand": ligand,
                "affinity_kcal_mol": affinity,
                "status": "success"
            })
        except Exception as e:
            print(f"  Error: {e}")
            results.append({
                "ligand": ligand,
                "affinity_kcal_mol": None,
                "status": "failed"
            })
    
    df = pd.DataFrame(results)
    df.to_csv("data/processed/docking_results.csv", index=False)
    print(f"\nResults saved to data/processed/docking_results.csv")
    return df


if __name__ == "__main__":
    ligands = ["quercetin", "resveratrol", "naringenin", "kaempferol"]
    results = dock_all(ligands)
    print("\n" + "="*50)
    print("DOCKING RESULTS SUMMARY")
    print("="*50)
    print(results.to_string(index=False))