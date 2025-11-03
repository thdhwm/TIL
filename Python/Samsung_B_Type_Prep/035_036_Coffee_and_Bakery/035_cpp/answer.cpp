/*
* @file: [H2534][Pro] 커피점 & 제과점
   
* @brief: 모범 답안
   
* @copyright: All rights reserved (c) 2025 Samsung Electronics, Inc.
*/
  
  
  
  
  
  
#include <queue>
#include <vector>
#include <cstring>
  
  
using namespace std;
  
  
constexpr int MAX_N = 10000;
  
  
typedef unsigned long long ull;
  
  
vector<int> Graph[MAX_N];
  
  
void init(int N, int K, int sBuilding[], int eBuilding[], int mDistance[]) {
    for (int i = 0; i < N; ++i) {
        Graph[i].clear();
    }
    for (int i = 0; i < K; ++i) {
        Graph[sBuilding[i]].emplace_back(eBuilding[i] << 16 | mDistance[i]);
        Graph[eBuilding[i]].emplace_back(sBuilding[i] << 16 | mDistance[i]);
    }
}
  
  
void add(int sBuilding, int eBuilding, int mDistance) {
    Graph[sBuilding].emplace_back(eBuilding << 16 | mDistance);
    Graph[eBuilding].emplace_back(sBuilding << 16 | mDistance);
}
  
  
int calculate(int M, int mCoffee[], int P, int mBakery[], int R) {
    int cDist[MAX_N], bDist[MAX_N];
    memset(cDist, 0x7f, sizeof(cDist));
    memset(bDist, 0x7f, sizeof(bDist));
  
  
    priority_queue<ull, vector<ull>, greater<ull>> pq;
  
  
    for (int i = 0; i < M; ++i) {
        cDist[mCoffee[i]] = 0;
        pq.emplace(1 << 16 | mCoffee[i]);
    }
  
  
    for (int i = 0; i < P; ++i) {
        bDist[mBakery[i]] = 0;
        pq.emplace(mBakery[i]);
    }
  
  
    int ret = R * 2 + 1;
    while (!pq.empty()) {
        ull curr = pq.top();
        pq.pop();
  
  
        ull currCost = curr >> 32;
        ull isCoffee = (curr >> 16) & 0xffff;
        ull u = curr & 0xffff;
  
  
        if (currCost >= ret || currCost > R) break;
  
  
        if (isCoffee) {
            if (cDist[u] < currCost) continue;
            if (currCost > 0 && currCost <= R && bDist[u] > 0 && bDist[u] <= R && currCost + bDist[u] < ret) {
                ret = currCost + bDist[u];
            }
  
  
            for (int val : Graph[u]) {
                ull v = val >> 16;
                ull nextCost = currCost + val & 0xffff;
  
  
                if (nextCost >= ret) continue;
                if (cDist[v] > nextCost) {
                    cDist[v] = nextCost;
                    pq.emplace(nextCost << 32 | 1 << 16 | v);
                }
            }
        } else {
            if (bDist[u] < currCost) continue;
            if (currCost > 0 && currCost <= R && cDist[u] > 0 && cDist[u] <= R && currCost + cDist[u] < ret) {
                ret = currCost + cDist[u];
            }
  
  
            for (int val : Graph[u]) {
                ull v = val >> 16;
                ull nextCost = currCost + val & 0xffff;
  
  
                if (nextCost >= ret) continue;
                if (bDist[v] > nextCost) {
                    bDist[v] = nextCost;
                    pq.emplace(nextCost << 32 | v);
                }
            }
        }
    }
  
  
    return (ret <= 2 * R) ? ret : -1;
}
