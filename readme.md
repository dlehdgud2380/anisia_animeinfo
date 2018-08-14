# 애니시아 애니 정보 모듈
## 정보
* Python 3.7.0 기반으로 만들었습니다. (모듈로 사용할 수 있도록 만들어 놓았으며 추가적으로 더욱 개선 할 예정입니다.)
* 이것은 AniSudo에 사용되는 모듈입니다. -> https://github.com/dlehdgud2380/AniSudo
* 애니시아 API 사용자규약 참고 -> https://www.anissia.net/?m=1&b=4 
* 애니시아 애니편성표 -> https://www.anissia.net/anitime/
## 사용방법

일반사용자:

    프로그램을 실행하면 질문에 따라 진행하시면 됩니다.

    

소스사용자:

    DayInfo와 AnimeInfo라는 클래스가 있습니다.

    DayInfo는 예를 들어 월요일이면 월요일 전체 애니목록을 가져 옵니다.
    매개변수는 0부터 6까지 즉 일~토까지의 정보를 가져옵니다. -> 예: DayInfo(0)
    
    입력후 get_data()로 json으로 이루어진 데이터를 dict로 변환하여 리턴합니다.
    print_data 함수는 dict의 key값만 가져와 list로 변환 후 애니이름들을 순서대로 보여줍니다.


    AnimeInfo클래스는 DayInfo클래스의 get_data()함수를 통해 데이터를 받고 한 작품의 정보를 보여줍니다.

    매개변수는 두 개를 입력 해야합니다. 첫번째는 DayInfo클래스에 입력되는 매개변수이며 
    두번째는 그 요일의 애니목록중 한가지를 조회합니다. 
    -> 예: AnimeInfo(0, 0)

    get_title()통해 리턴된 dict의 key값(애니명)만 가져오고
    get_code()통해 리턴된 dict의 value값(애니고유코드)만 가져옵니다.
    get_fullinfo() 위의 두 함수가 리턴한 값들을 한꺼번에 출력하여 한 작품에 대한 정보를 볼 수 있습니다.
    get_subdata는 해당작품에 대한 자막정보를 불러옵니다.
