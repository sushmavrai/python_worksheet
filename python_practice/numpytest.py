import numpy as np
height = [1.73, 1.65, 1.54]
weight = [65.4, 66.4, 70.3]
np_height = np.array(height)
np_weight = np.array(weight)
bmi = np_weight/ np_height ** 2
print(bmi)
print(bmi > 23)
print(bmi[0]>21.33)
