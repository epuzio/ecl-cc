class point3:
    def __init__(self, X:float, Y:float, Z:float):
        self.X = X
        self.Y = Y
        self.Z = Z
    def __add__(self, other):
        return self.X + other.X, self.Y + other.Y, self.Z + other.Z
    def __sub__(self, other):
        return self.X - other.X, self.Y - other.Y, self.Z - other.Z
    def __mul__(self, other):
        return self.X * other.X, self.Y * other.Y, self.Z * other.Z
    def __truediv__(self, other):
        return self.X / other.X, self.Y / other.Y, self.Z / other.Z
    def __floordiv__(self, other):
        return self.X // other.X, self.Y // other.Y, self.Z // other.Z
    def __mod__(self, other):
        return self.X % other.X, self.Y % other.Y, self.Z % other.Z
    def __pow__(self, other):
        return self.X ** other.X, self.Y ** other.Y, self.Z ** other.Z
    def __eq__(self, other):
        return self.X == other.X and self.Y == other.Y and self.Z == other.Z
    def __ne__(self, other):
        return self.X != other.X or self.Y != other.Y or self.Z != other.Z
    def __lt__(self, other):
        return self.X < other.X and self.Y < other.Y and self.Z < other.Z
    def __le__(self, other):
        return self.X <= other.X and self.Y <= other.Y and self.Z <= other.Z
    def __gt__(self, other):
        return self.X > other.X and self.Y > other.Y and self.Z > other.Z
    def __ge__(self, other):
        return self.X >= other.X and self.Y >= other.Y and self.Z >= other.Z
    def __len__(self):
        return (self.X * self.X + self.Y * self.Y + self.Z * self.Z)**0.5
    def __str__(self):
        return f"({self.X}, {self.Y}, {self.Z})"
    
class vec(point3): #added vector functionality, may be a bit useless
    def cross(self, other):
        return point3(self.Y * other.Z - self.Z * other.Y, self.Z * other.X - self.X * other.Z, self.X * other.Y - self.Y * other.X)
    def dot(self, other):
        return self.X * other.X + self.Y * other.Y + self.Z * other.Z

    