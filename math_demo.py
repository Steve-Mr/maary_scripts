import numpy as np 
arr = [4,2,3,4,2,3]
 
# 求均值
arr_mean = np.mean(arr)
 
# 求方差
arr_var = np.var(arr)
 
# 求总体标准差
arr_std_1 = np.std(arr)
 
# 求样本标准差
arr_std_2 = np.std(arr, ddof=1)
 
print("平均值为：%f" % arr_mean)
print("方差为：%f" % arr_var)
print("总体标准差为: %f" % arr_std_1)
print("样本标准差为: %f" % arr_std_2)