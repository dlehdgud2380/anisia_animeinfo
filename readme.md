# 애니시아 애니 정보 모듈
## 정보
* Python 3.6.x 기반으로 만들었습니다. (모듈로 사용할 수 있도록 만들어 놓았으며 추가적으로 더욱 개선 할 예정입니다.)
* 애니시아 API 사용자규약 참고 -> https://www.anissia.net/?m=1&b=4 
* 애니시아 애니편성표 -> https://www.anissia.net/anitime/
## 사용방법
### 프로그램 체험
https://AniTimeDL.dlehdgud2380.repl.run

### 이미지
| 시작화면 | 선택한 요일의 편성표 | 선택한 애니의 정보 |
| -------- | -------- | -------- |
| ![](https://i.imgur.com/26pJbAO.png)     | ![](https://i.imgur.com/xAnAQWg.png)     | ![](https://i.imgur.com/IF8RjEh.png) |

### 개발자 사용법
pip3 install requests

```
## 객체 정보

1. Class Daytable(num)
출력함수: print_data()

2. Class TitleInfo(num1, num2)
      self.daycode = num1
      self.titlecode = num2
출력함수: print_data()


## 예제코드
      a = DayTable(num)
      a.print_data()

      b = TitleInfo(num1, num2)
      b.print_data()
```
