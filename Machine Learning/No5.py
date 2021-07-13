import numpy as np

def actf(x):
    return 1/(1+np.exp(-x))

def actf_deriv(x):
    return x*(1-x)

X = np.array([[0,0,1],[0,1,1],[1,0,1],[1,1,1]])
print(X.shape)
y = np.array([[0],[1],[1],[0]])
#y = np.array([[0],[0],[0],[1]])

np.random.seed(5)

inputs =3 # 입력층 노드는 바이어스를 위해 1개 추가
hiddens =6 # 은닉층도 바이어스를 위해 1개 추가
outputs =1

# 가중치 초기화 (-1.0 ~ 1.0 사이의 난수)
weight0 =2*np.random.random((inputs,hiddens))-1 # 입력층 -> 은닉층의 가중치 넘파이 배열
weight1 =2*np.random.random((hiddens,outputs))-1 # 은닉층 -> 출력층의 가중치 넘파이 배열

for i in range(10000):

    # 순방향 계산
    layer0 =X # 입력 대입
    net1 =np.dot(layer0,weight0) # 행렬 곱 계산
    layer1 =actf(net1) # 활성화 함수 적용
    layer1[:,-1]=1.0 # 바이어스 1.0으로 세팅
    net2 = np.dot(layer1,weight1) # 행렬 곱 계산
    layer2 = actf(net2) # 활성화 함수 적용

    
    # 역방향 전파
    layer2_error = layer2-y # 오차 계산
    layer2_delta = layer2_error*actf_deriv(layer2) # 델타 값 계산

    layer1_error = np.dot(layer2_delta,weight1.T) # 가중치의 전치행렬을 구한 후 은닉층에서 델타 계산
    layer1_delta = layer1_error * actf_deriv(layer1)

    weight1 += -0.2*np.dot(layer1.T,layer2_delta)
    weight0 += -0.2*np.dot(layer0.T,layer1_delta)

    print("-----",i+1,"번째 반복-----")
    print("I1의 가중치 : ", weight0[0])
    print("I2의 가중치 : ", weight0[1])
    print("I3의 가중치 : ", weight0[2],"(바이어스와 같음)")
    print("H1의가중치 : ",weight1[0])
    print("H2의가중치 : ",weight1[1])
    print("H3의가중치 : ",weight1[2])
    print("H4의가중치 : ",weight1[3])
    print("H5의가중치 : ",weight1[4])
    print("H6의가중치 : ",weight1[5])
    print("\n\n")

print(layer2)
