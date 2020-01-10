# 애니시아 애니 정보 모듈
## 정보
* Python 3.6.x 기반으로 만들었습니다. (모듈로 사용할 수 있도록 만들어 놓았으며 추가적으로 더욱 개선 할 예정입니다.)
* 이것은 AniTimeDL에 사용되는 모듈입니다. -> https://github.com/dlehdgud2380/AniTimeDL
* 애니시아 API 사용자규약 참고 -> https://www.anissia.net/?m=1&b=4 
* 애니시아 애니편성표 -> https://www.anissia.net/anitime/
## 사용방법
### 프로그램 체험
https://AniTimeDL.dlehdgud2380.repl.run

### 이미지
| 시작화면 | 선택한 요일의 편성표 | 선택한 애니의 정보 |
| -------- | -------- | -------- |
| ![](https://i.imgur.com/26pJbAO.png)     | ![](https://i.imgur.com/xAnAQWg.png)     | ![](https://i.imgur.com/IF8RjEh.png) |

### 개발자
pip3 install requests
Daytable(인자)
* print_data()

TitleInfo(인자1, 인자2)
* info()
* print_data()

```
## 예제코드

daycode = int(input("조회 할 요일 선택(0(일요일) - 6(토요일)): "))
    if daycode > 6 :
      print("\n올바른 숫자를 입력해주십시오")
    else:  
      os.system('cls' if os.name == 'nt' else 'clear')
      print("[애니메이션 타이틀 조회 프로그램 by Sc0@Nep]\n")
      a = DayTable(daycode)
      a.print_data()
      selectcode = int(input("\n상세정보를 알고싶은 타이틀 번호를 입력: "))
      os.system('cls' if os.name == 'nt' else 'clear')
      print("[애니메이션 타이틀 조회 프로그램 by Sc0@Nep]\n")
      b = TitleInfo(daycode, selectcode)
      #print(b.info())
      b.print_data()
```

### 일반 사용자
작성중
