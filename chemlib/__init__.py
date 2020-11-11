from chemlib.chemistry import PeriodicTable

pte = PeriodicTable()
SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
AVOGADROS_NUMBER = 6.02e+23

from chemlib.chemistry import Element, Compound, Reaction
from chemlib.chemistry import Combustion, Solution
from chemlib.chemistry import empirical_formula_by_percent_comp

c = 2.998*10**8    #Speed of light
h = 6.626*10**-34  #Planck's constant
R = 1.0974*10**7  #Rydberg constant

from chemlib.quantum_mechanics import Wave, rydberg
from chemlib.quantum_mechanics import energy_of_hydrogen_orbital

