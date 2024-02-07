#Rhinoscriptsyntax does not work outside of rhino so the wheel will become reinvented!!

class Point3d:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"Point3d({self.x}, {self.y}, {self.z})"
    
    
def CreatePoint(x, y, z): #Rhino.Geometry.Point3d
    return Point3d(x, y, z)


    
    
    
