from abc import ABC,abstractmethod


class Demo(ABC):

    @abstractmethod
    def demo_function(self):
        pass


class Child(Demo):

    def demo_function(self):
        print('hello world')

    def fun(self,a:int):
        print('hello python')
        
    
# d=Demo()
c= Child()
c.demo_function()
x=[c]

# d.demo_function()
# c.demo_function()



