from random import randint
import random
from matplotlib import pyplot as plt

NumberOfTotalGame = 1000
NumberOfSimulation = 100 # 시뮬레이션 횟수
WinList1 = []; WinList2 = [] # matplot을 위한 리스트

# 한 번의 시뮬레이션 당 100번씩 1000번 반복
for i in range(NumberOfTotalGame):

    WinCnt1, WinCnt2 = 0, 0 # 승리 카운트

    #---------------선택을 바꾸지 않았을 때---------------#

    for i in range(NumberOfSimulation): # 시뮬레이션 횟수만큼 반복

        Answer = randint(1,3) # 정답 생성

        FirstPick = randint(1,3) # 사용자의 첫 번째 선택

        Doors = [1,2,3] # 문 리스트

        Doors.remove(Answer) # 정답인 문 삭제

        if FirstPick != Answer : # 사용자가 고른 문이 정답이 아니면
            Doors.remove(FirstPick) # 문 리스트에서 사용자의 픽 삭제

        HostPick = random.choice(Doors) # 사회자의 선택

        if FirstPick == Answer: # 사용자가 고른 문이 정답이면
            WinCnt1 = WinCnt1 + 1 # 승리 카운트 증가

    WinList1.append(WinCnt1) # 리스트에 승리 카운트 추가

    #-----------------선택을 바꾸었을 때-----------------#

    for i in range(NumberOfSimulation): # 시뮬레이션 횟수만큼 반복

        Answer = randint(1,3) # 정답 생성

        FirstPick = randint(1,3) # 사용자의 첫 번째 선택

        Doors = [1,2,3] # 문 리스트

        Doors.remove(Answer) # 정답인 문 삭제

        if FirstPick != Answer: # 사용자가 고른 문이 정답이 아니면
            Doors.remove(FirstPick) # 문 리스트에서 사용자 픽 삭제

        HostPick = random.choice(Doors) # 사회자의 선택

        #사용자는 선택을 바꿈
        Doors = [1,2,3]
        Doors.remove(HostPick); Doors.remove(FirstPick) # 사용자의 두 번째 선택을 위한 번호 남기기

        SecondPick = Doors[0] # 사용자의 두 번째 선택

        if SecondPick == Answer: # 사용자가 고른 문이 정답이면
            WinCnt2 = WinCnt2 + 1 # 승리 카운트 증가

    WinList2.append(WinCnt2) # 리스트에 승리 카운트 추가

#----------------------결과 출력----------------------#

x = range(len(WinList1))
plt.plot(x,WinList1)
plt.plot(x,WinList2)
plt.xlabel('Total simulation cnt')
plt.ylabel('success probability')
plt.legend(['Change X', 'Change O'])
plt.show()
