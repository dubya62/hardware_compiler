
class Component:
    """
    Base circuitry component.
    Has some number of inputs and some number of outputs.
    Does nothing on its own.
    """
    def __init__(self, inputs:list=[], outputs:list=[]):
        self.inputs = inputs
        self.outputs = outputs

    def get_output(self):
        print("ERROR: Cannot get output of a basic Component.")
        exit(-1)


class Wire(Component):
    """
    A basic wire. Simply outputs its input.
    """
    
    def __init__(inputs:list=[], outputs:list=[]):
        Component.__init__(self, inputs, outputs)

    def get_output(self):
        pass

    
    

