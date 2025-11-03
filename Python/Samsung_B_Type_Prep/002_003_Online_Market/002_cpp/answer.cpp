/*

기존 자주 출제되던.. 데이터 추가, 삭제, 변경, 조회 형태의 문제
PQ, SET 으로 풀면됨

특이한점은 품목과 회사로 분류가 되어있고,
특정 품목, 분류에 해당하는 전체 데이터를 discount 해야하는 상황 발생

품목, 분류 별로 discount를 따로관리하고,
이후에 추가되는 물건들은 이전 discount만큼 더해서 저장해야하는게 포인트!!!!! 

0.
sell 에서 data base와 PQ 에 품목추가하고
close sell에서 data base와 PQ에서 삭제하고
discount에서 data base와 PQ 수정하고
show에서 pq 에서 뽑아서 보여줌


1.
discount에서 data base와 PQ를 하나하나 수정할 경우
하나의 품목, 분류에 모든 데이터 50000개가 모두 들어있다면 50000이 걸림
호출횟수 10`000 * 데이터 50`000 = 5억으로 시간 초과

2.
품목, 분류별로 discount를 관리하고 show할때 discount 만큼 빼서 보여준다면,
discount 이후에 들어온 상품들은 관리가 안됨...

3.
discount 이후에 들어온 상품들은 이전 누적 discount만큼 더해서 추가
show할때 discount 만큼 빼서 보여준다면 가능

품목, 분류별 discount에 접근하여 더해주기만 하면 되기 때문에,
discount 시간복잡도는 1

품목 추가할때 discount 더해서 추가하고, 품목 고를때 discount 빼면서 하면
시간복잡도 추가되는 부분은 없음

4. 구현 ㄱㄱ

5. 디버깅
25개중 21개만 맞아서 디버깅 했더니 closeSale에서 존재하지 않는 mID 들어오는 경우 예외처리 안함

6. 후기
누적 discount가 최대 100억이 나오는데 longlong으로 해야되는거 아닌가?..

*/


#include<queue>
#include<set>
#include<unordered_map>
#include<algorithm>
#include<iostream>
using namespace std;

#define MAX_GOODS 50005
#define MAX_CATE 6
#define MAX_COMP 6

typedef set<pair<int, int>> myset;

struct RESULT
{
	int cnt;
	int IDs[5];
};

struct goods_group {
	myset goods_set;
	int discount_num;
	int goods_cnt;
};

struct goods_info {
	int mID, mCategory, mCompany, mPrice, mClosed; //상품의 ID, 카테고리, 회사, 가격
};

goods_group cate_comp_goods[MAX_CATE][MAX_COMP];
unordered_map<int, int> mID_to_idx; //상품의 ID를 인덱스로 변환하기 위한 맵
goods_info goods_list[MAX_GOODS]; //상품 정보 리스트
int goods_idx;

void init()
{
	goods_idx = 1;
	mID_to_idx.clear();
	for (int i = 0; i < MAX_CATE; i++) {
		for (int j = 0; j < MAX_COMP; j++) {
			cate_comp_goods[i][j].discount_num = 0;
			cate_comp_goods[i][j].goods_set = myset();
			cate_comp_goods[i][j].goods_cnt = 0;
		}
	}
	return;
}

int sell(int mID, int mCategory, int mCompany, int mPrice)
{
	int temp_price = mPrice + cate_comp_goods[mCategory][mCompany].discount_num;
	// 디스카운트 후 들어온 상품은 가격에 이전 디스카운트를 더하고 push
	// 나중에 price가 필요할 경우 디스카운트 값을 다시 빼줌
	goods_list[goods_idx] = { mID, mCategory, mCompany, temp_price, 0 };
	mID_to_idx[mID] = goods_idx;
	goods_idx++;

	cate_comp_goods[mCategory][mCompany].goods_set.insert({ temp_price, mID });
	cate_comp_goods[mCategory][mCompany].goods_cnt++;

	return cate_comp_goods[mCategory][mCompany].goods_cnt;
}

int closeSale(int mID)
{
	int idx = mID_to_idx[mID];
	if (idx == 0 || goods_list[idx].mClosed == 1) return -1;
	goods_list[idx].mClosed = 1;
	cate_comp_goods[goods_list[idx].mCategory][goods_list[idx].mCompany].goods_cnt--; // lazy delete를 위해 cnt를 따로 관리
	return goods_list[idx].mPrice - cate_comp_goods[goods_list[idx].mCategory][goods_list[idx].mCompany].discount_num;
}

int discount(int mCategory, int mCompany, int mAmount)
{
	goods_group* cur_group_p = &cate_comp_goods[mCategory][mCompany]; // 가독성을 위해
	cur_group_p->discount_num += mAmount; // 그룹별로 디스카운트를 관리하자
	for (auto temp_it = cur_group_p->goods_set.begin(); temp_it != cur_group_p->goods_set.end();) {
        if((*temp_it).first > cur_group_p->discount_num) break;
		int temp_idx = mID_to_idx[(*temp_it).second];
		if (goods_list[temp_idx].mClosed == 0) {
			cur_group_p->goods_cnt--;
			goods_list[temp_idx].mClosed = 1;
		}
		temp_it = cur_group_p->goods_set.erase(temp_it);
    }
	return cur_group_p->goods_cnt;
}

RESULT show(int mHow, int mCode)
{
	RESULT res;
	vector<pair<int, int>> temp_sort_goods;
	for (int i = 1; i < MAX_CATE; i++) {
		if (mHow == 1 && i != mCode) continue;
		for (int j = 1; j < MAX_COMP; j++) {
			if (mHow == 2 && j != mCode) continue;

			int push_cnt = 0;
			goods_group* cur_group_p = &cate_comp_goods[i][j]; // 가독성을 위해
            for(auto temp_goods : cur_group_p->goods_set){
                if( push_cnt >= 5 ) break;
				int temp_idx = mID_to_idx[temp_goods.second];
				if (goods_list[temp_idx].mClosed == 0) {
                    temp_goods.first -= cur_group_p->discount_num; // 분류, 회사 별 할인된 값 뺀후 push
                    temp_sort_goods.push_back(temp_goods);
                    push_cnt++;                
                }
            }
		}
	}

	sort(temp_sort_goods.begin(), temp_sort_goods.end()); // 최대 5 * 5 * 5 개라서 그냥 sort
	res.cnt = min(int(temp_sort_goods.size()), 5);
	for (int i = 0; i < res.cnt; i++) {
		res.IDs[i] = temp_sort_goods[i].second;
	}

	return res;
}

/*
Q: 해당 문제의 discount 함수에서 그룹안에 50,000개의 아이템들이 들어있고, 
mAmount가 모든 아이템의 price보다 큰 값으로 주어질 경우 50,000 초과의 최악 시간복잡도가 나오는 것으로 알고있습니다. 
단순히 이 방법으로 시간복잡도를 계산하여 10,000(호출횟수) * 50,000으로 시간초과라 판단하게 되었습니다.

하지만, 해당 worst case에서만 시간복잡도가 높고, 한 번 발생하게 되면 해당 그룹이 비어버려 이후 호출은 시간복잡도가 작아지고, 
discount함수는 평균적으로 시간복잡도가 작아 통과가 되는 것으로 알고있습니다.
이 문제의 discount 함수처럼 '단일 최악 시간 복잡도 x 호출 횟수'로 판단하기 어려운 알고리즘의 시간복잡도를 계산해야 하는 상황에서, 
시간복잡도를 계산하는 노하우나 사고방식이 있을까요?

A: 한 번에 50,000개가 제거되어 버릴 수도 있고, 여러번 나눠서 50,000개가 제거될 수도 있습니다.
하지만 한 번 제거되면, 다음부터 그 숫자만큼 줄어들게 됩니다.
그런 관점에서 복잡도를 계산해보면....
함수 호출횟수와 상관없이 한 테스트 케이스에서 최대 NlogN 이 걸릴 것이라고 생각할 수 있겠습니다!!
*/
