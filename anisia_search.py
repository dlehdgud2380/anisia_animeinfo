import sys
import requests
import os

os.system('cls' if os.name == 'nt' else 'clear')
print("[애니메이션 타이틀 조회 프로그램 by Sc0@Nep]\n")

URL = "https://www.anissia.net/anitime/list?w="
DAY = ["일요일", "월요일", "화요일", "수요일", "목요일", "금요일", "토요일"]
mod = sys.modules[__name__]

#7개의 변수를 리스트안에 생성
animedata = [setattr(mod, 'day_{}'.format(i), i) for i in range(0, 7)]

#서버체크
servercheck = str(requests.get(URL).status_code)
if servercheck == "200" :
  print(servercheck + " - OK")
  print("최신 데이터 불러오는 중 ...")
elif servercheck == "404" :
  print(servercheck + " - 서버 점검중")
  print("서버조회 불가로 종료합니다")
else:
  print(servercheck + " - 서버 또는 인터넷 문제")
  print("서버조회가 불가로 종료합니다. 인터넷 접속 확인후 다시 실행해주세요")

#정보 파싱
for i in range(0, 7):
  response = requests.get(URL + str(i))
  animedata[i] = response.json()

#그날의 애니방영시간표를 가져오는 클래스
class DayTable:
  def __init__ (self, num):
    self.num = num

  #하루 치 애니 시간표 가져오는 함수
  def dayinfo(self):
    daylist = []
    for i in range(0, len(animedata[self.num])):
      title = animedata[self.num][i]
      daylist.append(title['t'] + " " + title['s'])
    return daylist
  
  #dayinfo 함수를 통해 가져온 값을 보기좋게 출력
  def print_data(self):
    data = self.dayinfo()
    print("\n" + " [" + DAY[self.num] + " 방영시간표" + "] " + "\n")
    print("번호 | 방영시간 | 제목" + "\n")
    for i in range(0, len(data)):
      print(str(i).zfill(2) + " " + data[i])

''' 일주일치 애니시간표 출력 테스트 알고리즘
  for i in range(0, 7):
    temp_list = []
    for j in range(0, len(animedata)):
      temp = animedata[i][0]
      temp_list.append(temp['s'])
    print(temp_list[i], end=" | ")
'''

#타이틀 하나의 정보를 불러오는 클래스
class TitleInfo:
  def __init__ (self, num1, num2):
    self.daycode = num1
    self.titlecode = num2
  #제목, 방영요일, 방영시간, 장르, 방영 및 결방 확인, 방영시작일
  def info(self):
    data = animedata[self.daycode][self.titlecode]
    titleinfo = []
    titleinfo.append("제목: " + data['s'])
    titleinfo.append("방영요일: " + DAY[self.daycode])
    titleinfo.append("방영시각: " + data['t'])
    titleinfo.append("장르: " + data['g'])
    titleinfo.append("금주 방영 여부: " + data['g'])
    titleinfo.append("방영시작일: " + data['sd'])
    return titleinfo
  
  #info 함수를 통해 가져온 값을 보기좋게 출력
  def print_data(self):
    data = self.info()
    print("------------------\n선택한 타이틀 정보\n------------------\n")
    for i in range(0, len(data)):
      print(data[i])

#실행테스트(또는 일반 유저용)
if __name__ == "__main__" :

  def program():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("[애니메이션 타이틀 조회 프로그램 by Sc0@Nep]\n")
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

  while(True):
    os.system('cls' if os.name == 'nt' else 'clear')
    if servercheck == "200" :
      program()
      mainmenu = input("\n다른 정보를 검색하시겠습니까? (Y = 새로 검색, 아무키 = 프로그램종료): ")
      if mainmenu == "y" and "Y" and "ㅛ" :
        os.system('cls' if os.name == 'nt' else 'clear')
        continue
      else:
        break
    elif servercheck == "404" :
      break
    else:
      break