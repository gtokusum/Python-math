class Vector3D:
    
    def __init__(self,x,y,z):
        self.x,self.y,self.z = x,y,z

    def __str__(self):
        return '{}i + {}j + {}k'.format(self.x,self.y,self.z)

    def dot(self,other):
        return self.x*other.x + self.y*other.y + self.z*other.z

    def cross(self,other):
        first = self.y*other.z - self.z*other.y
        second = self.x*other.z - self.z*other.z
        third = self.x*other.y - self.y*other.x
        return Vector3D(first - second + third)

    