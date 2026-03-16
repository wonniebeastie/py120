# Consider the following code:
class Tree:
    def __init__(self):
        self.type = "Generic Tree"

class Pine(Tree):
    def __init__(self):
        super().__init__()
        self.type = "Pine Tree"

# Answer the following question without running the code.

# When an instance of Pine is created, what value will its type attribute have?
# Why?
