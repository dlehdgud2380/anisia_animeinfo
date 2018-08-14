import json
import urllib.request

#가져올 데이터의 주소(상수) 
URL = "https://www.anissia.net/anitime/list?w="
#자막정보를 가져올 데이터의 주소(상수)
SUB_URL = "https://www.anissia.net/anitime/cap?i="

def api_request(url):
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    get_jsondata = response.read().decode('utf-8')
    json_data = json.loads(get_jsondata)

    return json_data

#예: 월요일 방영하는 애니면 월요일치 애니만 받아온다. 0(일요일) ~ 6(토요일까지)
#참고: dict로 return하니 꼭 list로 변환 필수
class DayTable:
    def __init__(self, num):
        self.num = num

    def get_data(self):
        getlist = api_request(URL + str(self.num))
        title_data = {}
        count = 0
        for i in getlist:
            title_data[getlist[count]['s']] = str(getlist[count]['i'])
            count += 1
        return title_data

    def print_data(self):
        data = list(self.get_data().keys())

        count = 0
        for i in data:
            print(str(count)+ " " + data[count] )
            count += 1
        print("\n")
        

#애니 한 작품에 대한 정보
class AnimeInfo:
    def __init__(self, day, target):
        self.num_day = day
        self.num_target = target

    def get_titlename(self):
        dayinfo = DayTable(self.num_day).get_data()
        titlelist = list(dayinfo.keys())
        return titlelist[self.num_target]

    def get_code(self):
        dayinfo = DayTable(self.num_day).get_data()
        codelist = list(dayinfo.values())
        return codelist[self.num_target]

    def get_fullinfo(self):
        return str("타이틀명: " + self.get_titlename()) + "\n" + "고유코드: " + str(self.get_code())

    def get_subdata(self):
        data = api_request(SUB_URL + str(self.get_code()))
        #for i in data:
            
        return data


"""
<사용방법>
일반사용자:
    프로그램을 실행하면 질문에 따라 진행하시면 됩니다.
    
소스사용자:
    DayInfo와 AnimeInfo라는 클래스가 있습니다.
    
    DayInfo는 예를 들어 월요일이면 월요일 전체 애니목록을 가져 옵니다.
    매개변수는 0부터 6까지 즉 일~토까지의 정보를 가져옵니다. -> 예: DayInfo(0)
    입력후 get_data()로 json으로 이루어진 데이터를 dict로 변환하여 리턴합니다.
    print_data 함수는 dict의 key값만 가져와 list로 변환 후 애니이름들을 순서대로 보여줍니다.

    AnimeInfo클래스는 DayInfo클래스의 get_data()함수를 통해 데이터를 받고 한 작품의 정보를 보여줍니다.
    매개변수는 두 개를 입력 해야합니다. 첫번째는 DayInfo클래스에 입력되는 매개변수이며 두번째는 그 요일의 애니목록중 한가지를 조회합니다.  -> 예: AnimeInfo(0, 0)
    get_title()통해 리턴된 dict의 key값(애니명)만 가져오고
    get_code()통해 리턴된 dict의 value값(애니고유코드)만 가져옵니다.
    get_fullinfo() 위의 두 함수가 리턴한 값들을 한꺼번에 출력하여 한 작품에 대한 정보를 볼 수 있습니다.
    get_subdata는 해당작품에 대한 자막정보를 불러옵니다.
    
"""
#구동 테스트
if __name__ == '__main__':
    input_num1 = int(input("타이틀정보를 불러올 요일 번호를 입력하세요(일0~토6): "))
    titlelist = DayTable(input_num1)
    print(titlelist.print_data())
    input_num2 = int(input("얻고 싶은 타이틀의 순서번호를 입력하세요(0번이 1번째): "))
    animeinfo = AnimeInfo(input_num1, input_num2)
    print(animeinfo.get_fullinfo())
   
