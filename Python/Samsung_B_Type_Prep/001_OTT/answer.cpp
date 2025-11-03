/*
일반적 Heap을 활용한 문제
장르와 시청목록을 섞어서 조금 복잡하다.


영화가 삭제되면, 시청 목록에서도 삭제된다고 한다... (왜?)


suggest를 위한 설계를 시작해보자..

1.
사용자의 시청목록 최근 5개를 알아야한다.
watch 순서대로 쌓으면되니까 그냥 배열을 사용하면 되지 않을까?

하지만 erase에서 시청한 영화를 삭제해버리면,
배열에서 제거하야 하기 때문에 최대 1000(최대 시청 영화 수)이 걸린다.

suggest x 1,000 = 5,000 x 1,000 = 500만

나쁘지 않지만 최적화가 필요해 보인다.


2.
사용자의 시청목록을 linkedlist 혹은 queue로 관리하자.
erase에서 삭제 flag만 세우고,
suggest에서 시청목록을 확인할 때, flag를 확인하고 삭제해버리면 된다.
그러면 삭제된 영화는 한 번만 접근 후 제거되므로,
한 테스트케이스에서 erase(1,000) 만큼만 시간이 소모된다.
굳

erase 에서 flag 세우지않고, 실제로 삭제하면.
해당 영화를 본 시청자들의 시청목록에서 모두 삭제해야하기 때문에,
오래걸릴 수 있다.


3.
사용자가 준 평점을 알하야 하니까.. 총점과 평점은 따로 관리해야 하고....
최근 시청목록 5개 보면서 최고의 장르를 찾고,
장르 중 총점이 가장 높은영화를 5개를 추천한다.

총점이 높은 순서를 알아야하기 때문에.. sort? max5? heap?
add와 erase가 있기 때문에 heap을 쓰는게 좋겠다.

장르별로 추천하면 되기때문에.. 장르별로 heap을 만들자.
그리고 장르 상관없는 경우도 있기때문에, 5개 다 돌면 귀찮으니까 모든 영화넣는 heap도 만들자.
heap[0] = 모든장르
heap[1-5] = 장르별

heap으로 관리하면 (M = 최대 영화 수 = add = 10,000)
add x log(M) = 10,000 x 14.xx = 14만
erase x log(M) = 1,000 x 14.xx = 1.4만
watch x log(M) = 30,000 x 14.xx = 42만
suggest = 5,000

복잡도에 이상없다.


4.
구현 ㄱㄱ



5.. 디버깅
사용자가 이미 시청한 영화는 추천하면 안된다. 주의..
삭제된 영화는 시청목록에서도 삭제해야한다. ㅎ

*/


#include <set>
#include <unordered_map>
#include <unordered_set>
#include <list>
#include <iostream>
using namespace std;
 
#define MAX_GENRE (5)
#define MAX_MOVIES (10000)
#define MAX_USERS (1000)
 
struct movie{
    int mID, mGenre, mTotal, removed;
    unordered_set<int> watched_users;
};
 
movie movies[MAX_MOVIES + 5];
set<pair<int,int>, greater<pair<int,int>>> genre_to_movies[MAX_GENRE + 5];
list<pair<int, int>> user_to_movie[MAX_USERS + 5];
 
 
 
unordered_map<int,int> id_to_idx;
unordered_map<int,int> idx_to_id;
 
int m_idx;
 
struct RESULT
{
    int cnt;
    int IDs[5];
};
 
void init(int N)
{
 
    for(int i=0; i<MAX_GENRE + 1; i++) genre_to_movies[i].clear();
    for(int i=0; i<MAX_USERS + 5; i++) user_to_movie[i].clear();
    id_to_idx.clear();
    idx_to_id.clear();
    m_idx = 0;
    return;
}
 
int add(int mID, int mGenre, int mTotal)
{
    if(id_to_idx.find(mID)!= id_to_idx.end()) return 0;
    int cur_idx = m_idx;
    id_to_idx[mID] = cur_idx;
    idx_to_id[cur_idx] = mID;
 
    genre_to_movies[mGenre].insert({mTotal, cur_idx});
    genre_to_movies[0].insert({mTotal, cur_idx});
    movies[cur_idx] = {mID, mGenre, mTotal, 0, unordered_set<int>()};
     
    m_idx++;
    return 1;
}
 
int erase(int mID)
{
    if(id_to_idx.find(mID) == id_to_idx.end()) return 0;
     
    int cur_idx = id_to_idx[mID];
    movies[cur_idx].removed = 1;
    int cur_genre = movies[cur_idx].mGenre;
    int cur_total = movies[cur_idx].mTotal;
    genre_to_movies[cur_genre].erase({cur_total, cur_idx});
    genre_to_movies[0].erase({cur_total, cur_idx});
 
    id_to_idx.erase(mID);
    return 1;
}
 
 
 
 
int watch(int uID, int mID, int mRating)
{
    if(id_to_idx.find(mID) == id_to_idx.end()) return 0;
 
 
    int cur_idx = id_to_idx[mID];
    if( movies[cur_idx].watched_users.find(uID) != movies[cur_idx].watched_users.end()) return 0;
 
 
    int cur_genre = movies[cur_idx].mGenre;
    int cur_total = movies[cur_idx].mTotal;
    user_to_movie[uID].push_front({cur_idx, mRating});
 
    genre_to_movies[cur_genre].erase({cur_total, cur_idx});
    genre_to_movies[0].erase({cur_total, cur_idx});
     
    movies[cur_idx].mTotal += mRating;
 
    genre_to_movies[cur_genre].insert({movies[cur_idx].mTotal, cur_idx});
    genre_to_movies[0].insert({movies[cur_idx].mTotal, cur_idx});
 
    movies[cur_idx].watched_users.insert(uID);
     
    return 1;
}
 
RESULT suggest(int uID)
{
    RESULT res;
    int max_rating = 0;
    int max_genre = 0;
    int cnt = 0;
    auto it = user_to_movie[uID].begin();
 
    while(it!= user_to_movie[uID].end() && cnt < 5){
        int temp_idx = (*it).first;
        int temp_rating = (*it).second;
        if(movies[temp_idx].removed == 1){
            it = user_to_movie[uID].erase(it);
            continue;
        } else {
            if(max_rating < temp_rating){
                max_rating = temp_rating;
                max_genre = movies[temp_idx].mGenre;
            }
            cnt++;
            it++;
        }
    }
 
    res.cnt = 0;
    for(auto it : genre_to_movies[max_genre]){
        int temp_idx = it.second;
        int temp_id = idx_to_id[temp_idx];
 
        if(movies[temp_idx].watched_users.find(uID) != movies[temp_idx].watched_users.end()) continue;
        res.IDs[res.cnt++] = temp_id;
        if(res.cnt >= 5) break;
    }
 
    return res;
}
