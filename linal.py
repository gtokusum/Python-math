import math

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

    def distance(self,other):
        return math.sqrt((other.x-self.x)**2 + (other.y-self.y)**2 + (other.z-self.z)**2)

    def __sub__(self,other):
        return Vector3D(self.x-other.x,self.y-other.y,self.z-other.z)

    def __add__(self,other):
        return Vector3D(self.x+other.x,self.y+other.y,self.z+other.z)

    def __mul__(self,scalar):
        return Vector3D(self.x*scalar,self.y*scalar,self.z*scalar)

    def __neg__(self):
        return Vector3D(-self.x,-self.y,-self.z)

    