# something_like
# zeros_like, ones_like, empty_like
# 0으로만 가득참 / 1로만 가득참 / 다 비움

import numpy as np

a = np.arange(30).reshape(5, 6)

print(np.zeros_like(a))
print(np.ones_like(a))
print(np.empty_like(a))

