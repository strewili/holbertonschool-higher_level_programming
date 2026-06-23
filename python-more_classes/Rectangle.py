#!/usr/bin/python3le
class Rectangle:
 number_of_instances=0
 print_symbol= "#"
 def __init__(self, width=0,height=0):
  self.width=width
  self.height=height
  Rectangle.number_of_instances+=1
  self.__initialized= True

@property
def width (self):
 return self.__width

@width.setter
def width(self,value):
  if type (value) is not int:
        raise TypeError ("width must be an intger")
  if value<0 :
        raise ValueError("must be >=0")
  self.__width=value


@property
def height(self):
   return self.__height 

@height.setter
def height(self,value):
   if type (value)is not int :
        raise TypeError("must be an intger")
   if value<0:
        raise ValueError("must be >= 0")
   self.__hieght = value

def area(self):
   return self.__width * self.__height

def perimeter(self):
   if self.__width== 0 or self.__height==0 :
        return 2* (self.__width +self.__height)
   
def __str__(self):
   if self.__width==0 or self.__height==0:
    return ""
   symbol = str(self.print_symbol)
   return "\n".join(symbol*self.__width for i in range (self.__height))

def __repr__(self):
   return "rectangle({},{})".format(self.__width,self.__height)

def __del__(self):
   if getattr(self,"_rectangle__initialized,",False):
        Rectangle.number_of_instances-=1
        print("bye rectangle")

def bigger_or_equal(rect_1,rect_2):
   if not isinstance(rect_1,Rectangle):
        raise TypeError("error must be instance")
   if not isinstance(rect_2,Rectangle):
        raise TypeError("rect_2 must me an instance of rectangle")
   if rect_1.area()>=rect_2.area():
        return rect_1
   return rect_2

def square (cls,size=0):
    return cls (size,size)
    
    
    