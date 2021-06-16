import numpy as np
from sklearn.datasets import load_iris
from sklearn.neural_network import MLPClassifier


iris = load_iris()
X = iris.data[:,(0,1)] # 꽂의 너비와 높이만을 입력으로

Y = (iris.target == 0).astype(np.int) # 출력은 "Iris Setosa인가 아닌가"


model = MLPClassifier(activation='relu',solver='lbfgs',hidden_layer_sizes=[150], random_state=1)
model.fit(X,Y)

# 결과 출력
print('X : ')
for i in range(0,149,5):
    print(X[i],X[i+1],X[i+2],X[i+3],X[i+4])
print('\n\nY : ')
for i in range(0,149,5):
    print(Y[i],Y[i+1],Y[i+2],Y[i+3],Y[i+4])

print('\n\naccuracy : ',model.score(X,Y))

