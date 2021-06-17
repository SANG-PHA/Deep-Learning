import numpy as np
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt


# 뉴론의 출력 계산 함수
def calculate(input):
    global weights
    global bias
    activation = bias  # 바이어스
    for i in range(2):  # 입력신호 총합 계산
        activation += weights[i] * input[i]
    if activation >= 0.0:  # 스텝 활성화 함수
        return 1
    else:
        return 0


# 학습 알고리즘
def train_weights(X, y, l_rate, n_epoch):
    global weights
    global bias
    for epoch in range(n_epoch):  # 에포크 반복
        sum_error = 0.0
        for row, target in zip(X, y):  # 데이터셋을 반복
            actual = calculate(row)  # 실제 출력 계산
            error = target - actual  # 실제 출력 계산
            bias = bias + l_rate * error
            sum_error += error ** 2  # 오류의 제곱 계산
            for i in range(2):  # 가중치 변경
                weights[i] = weights[i] + l_rate * error * row[i]
    return weights


# MAIN

# --------------- Make Dataset ---------------#
X, Y = make_blobs(n_samples=20, n_features=2, centers=2)  # 임의의 2개 집합을 구성한다. sample은 20개, 레이블 2개
plt.scatter(X[:, 0], X[:, 1], marker='o', c=Y, s=25, edgecolor='k')  # 구성한 2개의 집합을 plt 객체에 표시

# 생성된 2개의 집합을 구성하는 점들의 좌표와 레이블 출력
print("점들의 좌표");
print(X)
print("\n데이터의 실제 레이블 : " + str(Y))

# 가중치와 바이어스 초기값
weights = [0.0, 0.0]
bias = 0.0

# ----------------- Learning -----------------#
l_rate = 0.1  # 학습률
n_epoch = 50  # 에포크 횟수
weights = train_weights(X, Y, l_rate, n_epoch)  # 퍼셉트론을 학습하고 가중치를 리턴받는다.
results = []
for i in range(X.shape[0]):  # 퍼셉트론의 예측 결과를 리스트에 저장한다.
    results.append(calculate(X[i]))
print("\n데이터의 예측 레이블 : " + str(results))

# ------------------ Print ------------------#
Xintercept = (0, -bias / weights[1])  # X절편
Yintercept = (-bias / weights[0], 0)  # Y절편
plt.axline(Xintercept, Yintercept)  # decision boundary 그리기
plt.show()  # 그래프 그리기
