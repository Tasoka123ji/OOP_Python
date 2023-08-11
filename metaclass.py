class MyMeta(type):
    def __call__(cls,name,dic,doc) -> None:
        return super().__call__(cls,name,dic,doc)
    

class Mlass(metaclass = MyMeta):
    def __init__(self,name) -> None:
        super().__call__(self,name,'foo','fds')
        self.name = name 
        print(self.name)


obj1 = Mlass("foo")




