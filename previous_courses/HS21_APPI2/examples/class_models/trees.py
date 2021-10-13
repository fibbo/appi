# Another example of inheritance

import math

class Tree:
    def biomass(self):
        print("Tree is an abstract class. It does not have a biomass.")
    def LAI(self):
        print("Tree is an abstract class. It does not have a leaf area index.")

# Equations for biomass differ for different tree classes (based on empirical regressions)

class Beech(Tree):
    def __init__(self, DBH, canopy_projection, total_leaf_area): # in cm or cm2
        self.DBH = DBH
        self.canopy_projection = canopy_projection
        self.total_leaf_area = total_leaf_area
    def biomass(self): # in kg/tree
        return math.exp(-2.134+2.530*math.log(self.DBH)) # from http://www.fao.org/3/w4095e/w4095e06.htm , eq 3.2.4
    def LAI(self): # dimensionless
        return self.total_leaf_area/self.canopy_projection

class Palm(Tree):
    def __init__(self, DBH, canopy_projection, total_leaf_area): # in cm or cm2
        self.DBH = DBH
        self.canopy_projection = canopy_projection
        self.total_leaf_area = total_leaf_area
    def biomass(self): # in kg/tree
        return 21.297-6.953*(self.DBH)+0.740*(self.DBH**2) # from http://www.fao.org/3/w4095e/w4095e06.htm , eq 3.2.5
    def LAI(self): # dimensionless
        return self.total_leaf_area/self.canopy_projection

tree = Tree()
tree.biomass()
tree.LAI()

beech = Beech(140, 90000, 900000)
print(beech.biomass())
print(beech.LAI())

palm = Palm(70, 10000, 100000)
print(palm.biomass())
print(palm.LAI())