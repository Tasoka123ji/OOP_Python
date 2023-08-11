from abc import ABC, abstractmethod

class Abstract_Class(ABC):
    @abstractmethod
    def foo():
        pass

class Foo(Abstract_Class):
    def foo(self):
        print("how are you")
    
obj1 = Foo()
obj1.foo()

print(isinstance(Abstract_Class,type))
print(issubclass(Abstract_Class,object))
print(Abstract_Class.__mro__)


from collections.abc import Container

class MyClass():
    def __container__(self):
        pass

print(isinstance(MyClass,Container))


