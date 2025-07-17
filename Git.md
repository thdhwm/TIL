# 2주차 목요일

## 평가 안내

객관식/주관식/서술형 평가 → 객주서형 평가

분반 시험 같은 유형

파일제출형 → 퀘스트형 평가

코딩, 알고리즘 → SWEA 유형

모든 월말평가

작성한 코드 파일 꼭 제출!!

오제출, 미제출 주의 (& 압축하고 제출)

## AI Governance

저작권과 개인정보

- AI 저작권 이슈
- Hallucination & Deepfake
- AI 개인정보
- Physical AI
    
    

## Git ( Revert, Push )

git remote add origin remote_repo_url

origin → 변경가능 편한 이름으로

remote_repo_url - https://github.com/thdhwm/ssafy.git 내 git 허브 Repo. 주소

### Push

git push origin master

origin master 처음 세팅 하면 다음부터 스킵 가능

commit 내역이 없으면 push 불가능

### Pull, Clone

git pull origin master 

git clone remote_repo_url

origin master, remote_repo_url 처음 세팅 하면 다음부터 스킵 가능

변경 사항 만 받아오기 (업데이트)

git clone remote_repo_url

원격 저장소 전체 복제 (다운로드)

→ 사이트 접속해서 다운로드 보다 더 빠름

clone된 프로젝트 이미 init 되어 있음

→  실무 시작하면 git 사용할 때 init 잘 안쓰게 됨

## Ignore

touch .gitignore 생성

생성된 gitignore에 파일명, 확장자까지로 저장  (ex. a.txt)