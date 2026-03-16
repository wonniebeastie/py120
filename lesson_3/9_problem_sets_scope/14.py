# Consider the following code:
class A:
  def __init__(self):
      self.var_a = "A class variable"

class B(A):
    def __init__(self):
        self.var_b = "B class variable"

b = B()
print(b.var_a)

# Without running this code, what will happen if you were to run it? Why?
"""
This will raise an error because defining an `__init__` for class `B` causes it
to override class `A`'s initialization signature. So `var_a` is never 
initialized.
"""
