#로컬에서 테스트 시
#solution.py와 main.py 파일을 구분해 주세요.
#main.py의 import와 from와 sys.stdin 주석을 해제해 주세요.
#####main.py
import sys
import time
from solution import init, add, calculate

CMD_INIT = 100
CMD_ADD = 200
CMD_CALC = 300

def run1():
	q = int(input())
	okay = False

	sBuildingArr = []
	eBuildingArr = []
	mDistArr = []

	for i in range(q):
		cmd = int(input())

		if cmd == CMD_INIT:
			inputarray = input().split()
			n = int(inputarray[0])
			k = int(inputarray[1])
			for _ in range(k):
				road = input().split()
				sBuildingArr.append(int(road[0]))
				eBuildingArr.append(int(road[1]))
				mDistArr.append(int(road[2]))

			init(n, k, sBuildingArr, eBuildingArr, mDistArr)
			okay = True
		elif cmd == CMD_ADD:
			inputarray = input().split()
			sBuilding = int(inputarray[0])
			eBuilding = int(inputarray[1])
			mDist = int(inputarray[2])
			add(sBuilding, eBuilding, mDist)
		elif cmd == CMD_CALC:
			inputarray = input().split()
			m = int(inputarray[0])
			p = int(inputarray[1])
			r = int(inputarray[2])
			mCoffee = []
			for _ in range(m):
				mCoffee.append(int(input()))
			mBakery = []
			for _ in range(p):
				mBakery.append(int(input()))

			ans = int(input())
			ret = calculate(m, mCoffee, p, mBakery, r)
			if ans != ret:
				okay = False
		else:
			okay = False

	return okay


if __name__ == '__main__':
	sys.stdin = open('sample_input.txt', 'r')
	inputarray = input().split()
	TC = int(inputarray[0])
	MARK = int(inputarray[1])

	for testcase in range(1, TC + 1):
		start = time.time()
		score = MARK if run1() else 0
		end = time.time()
		print("#%d %d" % (testcase, score,), (end - start), flush = True)