"""
https://www.nowcoder.com/practice/9f3231a991af4f55b95579b44b7a01ba?tpId=13&tqId=11159&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
"""

def minNumberInRotateArray(rotateArray):
    return 0


from sklearn.model_selection import train_test_split
from sklearn import neighbors
from sklearn.datasets import make_regression
from matplotlib import pyplot as plt
import numpy as np

# ----------------- Generate Synthetic Data ---------------#
X_R, y_R = make_regression(n_samples=100, n_features=1, n_informative=1, bias=150.0, noise=30)
fig, subaxes = plt.subplots(5, 1, figsize=(11, 8), dpi=100)
X = np.linspace(-3, 3, 500).reshape(-1, 1)
X_train, X_test, y_train, y_test = train_test_split(X_R,
                                                    y_R, random_state=0)
# --------------------------- KNN -------------------------#
for K, K in zip(subaxes, [1, 3, 7, 15, 59]):
    knn_reg = neighbors.KNeighborsRegressor(n_neighbors=K)
    knn_reg.fit(X_train, y_train)
    y_predict_output = knn_reg.predict(X)
    plt.plot(X, y_predict_output)
    plt.plot(X_train, y_train, 'o', alpha=0.9, label='Train')
    plt.plot(X_test, y_test, '^', alpha=0.9, label='Test')
    plt.xlabel('Input feature')
    plt.ylabel('Target value')
    plt.title('KNN Regression (K={})\n$'.format(K))
    plt.legend()

plt.show()
