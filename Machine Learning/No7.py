import numpy as np
from sklearn.datasets import load_iris
from sklearn.neural_network import MLPClassifier

def actf(x):
    return 1/(1+np.exp(-x))

def actf_deriv(x):
    return x*(1-x)

iris = load_iris()
X = iris.data[:,(0,1)] # 꽂의 너비와 높이만을 입력으로
Y = (iris.target == 0).astype(np.int) # 출력은 "Iris Setosa인가 아닌가"
y = np.array(Y).reshape((150,1))
#print(y) # 50개만 True
#print("x,y",X.shape,y.shape)

np.random.seed(5)

inputs = 2 # X.Shape = (150,2) 이므로 입력층은 2개
hiddens = 5 # 은닉층도 바이어스를 위해 1개 추가
outputs = 1

# 가중치 초기화 (-1.0 ~ 1.0 사이의 난수)
weight0 =2*np.random.random((inputs,hiddens))-1 # 입력층 -> 은닉층의 가중치 넘파이 배열
weight1 =2*np.random.random((hiddens,outputs))-1 # 은닉층 -> 출력층의 가중치 넘파이 배열
print("w0,w1",weight0.shape, weight1.shape)

for i in range(1000):

    # 순방향 계산
    layer0 =X # 입력 대입
    #print("l,w",layer0.shape, weight0.shape)
    net1 =np.dot(layer0,weight0) # 행렬 곱 계산
    #print("net1",net1.shape)
    layer1 =actf(net1) # 활성화 함수 적용
    #print("layer1",layer1.shape)
    #layer1[:,-1]=1.0 # 바이어스 1.0으로 세팅
    net2 = np.dot(layer1,weight1) # 행렬 곱 계산
    #print("net2",net2.shape)
    layer2 = actf(net2) # 활성화 함수 적용
    #print("layer2",layer2.shape)

    # 역방향 전파
    #print(layer2)
    layer2_error = layer2-y # 오차 계산
    #print("layer2_error",layer2_error.shape)
    layer2_delta = layer2_error*actf_deriv(layer2) # 델타 값 계산
    #print("layer2_delta",layer2_delta.shape)

    layer1_error = np.dot(layer2_delta,weight1.T) # 가중치의 전치행렬을 구한 후 은닉층에서 델타 계산
    layer1_delta = layer1_error * actf_deriv(layer1)

    weight1 += -0.2*np.dot(layer1.T,layer2_delta)
    weight0 += -0.2*np.dot(layer0.T,layer1_delta)

    print("-----",i+1,"번째 반복-----")
    print("I1의 가중치 : ", weight0[0])
    print("I2의 가중치 : ", weight0[1])
    print("H1의가중치 : ",weight1[0])
    print("H2의가중치 : ",weight1[1])
    print("H3의가중치 : ",weight1[2])
    print("H4의가중치 : ",weight1[3])
    print("H5의가중치 : ",weight1[4])
    print("\n\n")

np.set_printoptions(precision=4)

for i in range(0,149,5):
    print(layer2[i],layer2[i+1],layer2[i+2],layer2[i+3],layer2[i+4])
