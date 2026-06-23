"""
Extract Ligand-Binding Domain (LBD) from full-length AR structure.
AR LBD: residues 662-919
"""

def extract_lbd(input_pdb, output_pdb, start_res=662, end_res=919):
    """
    Extract specific residue range from PDB file.
    """
    with open(input_pdb, 'r') as f:
        lines = f.readlines()
    
    lbd_lines = []
    for line in lines:
        if line.startswith('ATOM  ') or line.startswith('HETATM'):
            res_num = int(line[22:26].strip())
            if start_res <= res_num <= end_res:
                lbd_lines.append(line)
        elif line.startswith('TER'):
            # Keep TER if last atom was in range
            if lbd_lines and int(lbd_lines[-1][22:26].strip()) <= end_res:
                lbd_lines.append(line)
    
    with open(output_pdb, 'w') as f:
        f.writelines(lbd_lines)
    
    print(f"Extracted LBD (residues {start_res}-{end_res})")
    print(f"Total atoms: {len(lbd_lines)}")
    print(f"Saved to: {output_pdb}")


if __name__ == "__main__":
    extract_lbd(
        "data/raw/AF_structure.pdb",
        "data/processed/AR_LBD.pdb"
    )