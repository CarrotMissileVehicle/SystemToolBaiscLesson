import numpy
import torch
from utils import calc, greet

print(calc(12.5, 4))
print(greet("lab"))
m = torch.nn.Linear(1, 1)
a = numpy.zeros((2, 2))
print(m, a)