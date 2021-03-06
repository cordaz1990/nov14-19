from molecule import Molecule
from atom import Atom
from typing import TextIO

def read_moleculer(r: TextIO) -> Molecule:
    """ Read a single molecule from r and return it,
    or return None to signal end of file.
    """ 
    #If there isn't another line, we're at the end of the file.
    line = r.readline()
    if not line:
      return None
    #Name of the molecule: "COMPND name"
    key, name = line.split()
    
    molecule = Molecule(name)
    reading = True
    
    while reading:
      line = r.readline()
      if line.startswith('END'):
         reading = False
          
      else:
        key, num, kind x, y, z = line.split()
        molecule.add(Atom(int(num), kind, float(x), float(y), float(z)))
    
    return molecule
