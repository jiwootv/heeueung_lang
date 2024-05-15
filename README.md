# 헤으응 언어 - 세상에서 가장 남 앞에서 코드쓰기 민망한 언어


## ❓ 헤으응 언어는 뭐에요? 
- python으로 개발된, 그렇고 그런 매우 난해한 언어입니다.
- 혀엉.. 언어는 있는데 왜 이건 없나 해서 제가 직접! 만들어 보았습니다
- 만드는데는 2시간밖에 안걸렸어요. (리드미 쓰는게 더오래걸림. 도중에 한번 날아감...)   
- 제작자는 중학생이에요! 계속 업데이트 예정입니다.



## 🛠 문법 엿보기   
### 숫자 표현 방법
. (dot) 를 찍어 **갯수만큼 수를 나타**냅니다.
ex) ... <- 3입니다.
하지만 여러자리의 수를 표현하는데에는 좀 많은 어려움이 있죠. 그래서 Heart열이 탄생했습니다.

### Heart 열 | 여러자리 수 나타내기
예를 들어, 위의 방법으로 200을 나타내려면 점 200개를 써야 합니다.
하지만 Heart열은 ♡.. ; ;♡로 쓸수 있습니다.
각각 공백으로 자릿수를 나타내고, 그 숫자를 점으로 표현합니다.
0은 ;로 나타냅니다.
```
# Heart열로 여러자리수 나타내기

# 200
♡.. ; ;♡

# 1972
♡. ......... ....... ..♡
```

### 헤으응 함수 | 데이터 저장하기
이 프로그래밍 언어에 변수 따위는 사치입니다!

스택을 이용해 나타내죠.

우리는 헤으응 함수를 이용해 스택에 데이터를 저장할수 있습니다.

사용방법은 헤으응이란 글씨를 적고 넣을 인덱스, 넣을 값을 순서대로 넣어주면 됩니다.
첫번째 인덱스는 사용하실수 없습니다. 왜냐하면 출력 전용이기 때문입니다.
즉 출력함수는 따로 없고 출력하시려면 ``헤으응 . (출력내용)``을 넣으셔야 합니다.

예시 )
```
# 두번째에 3 저장하기
헤으응 .. ...

# 1 출력하기
헤으응 . .
```

하지만 여기서 그냥 문자넣으면 오류납니다.
그러면 문자를 출력하려면 어떻게 해야할까요..? 좀 더 아래쪽에 있는 가버렷 함수를 참고하세요.

### 응기잇 함수 | 데이터 가져오기
이름이 좀 그렇긴 하지만 없으면 코딩이 불가능한 함수입니다.

이 함수는 무려.. 스택에서 데이터를 가져올 수 있습니다!!!!

바로 예시 보시져.

```
# 2번에 3을 저장하고 3번에 2번의 내용 복사하기
헤으응 .. ...
헤으응 ... 응기잇 ..
```

### 가버렷 함수
#### 이 함수는 무료로 해줍니다!! ( 글자 가져오기를 )
ASCII 코드는 누구나 아시죠? 모르면 검색해 보세요.
가버렷 ( 값을 가져올 아스키코드 ) 이런식으로 실행하면 됩니다.

```
# 59번째 아스키코드 A 출력
헤으응 . 가버렷 ♡..... .........♡
```

현재 개발된 함수는 여기까지입니다. 입력 넣을 예정이에요!
<br>   
