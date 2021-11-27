class mind:
    def __init__ (self,title,option):
        self.title = title
        self.option = option
        self.yes = None
        self.no = None
    def vactor(self,userinput):
        if "yes" == userinput:
            return self.yes
        else:
            return self.no

num1 = mind("시간 체크와 일정 체크에 둔감해져 약속을 자꾸 잊어버린다.","yes? or no? : ")
num2 = mind("술자리나 모임이 잦고 사람들과 어울리는 자리를찾는다.","yes? or no? : ")
num3 = mind("심심한 것을 견딜 수 없고 혼자있는 시간이 무료하다 못해 화가 난다.","yes? or no? : ")
num4 = mind("재미있는 일, 재미없는 일에 대한 구분이 모호해져 특별한 일을 계획하지 않는다.","yes? or no? : ")
num5 = mind("컴퓨터나 TV 앞에 앉아 있는 시간이 부쩍 많아졌다.","yes? or no? : ")
num6 = mind("가끔씩 남자(여자)친구가 생기면 하고싶은 일들을 생각해본다.","yes? or no? : ")
num7 = mind("쇼핑으로 스트레스를 푸는 버릇이 생겼다.","yes? or no? : ")
num8 = mind("휴일이나 긴 휴가 기간이 돌아오면 적극적으로 계획을 세운다.","yes? or no? : ")
num9 = mind("혼자서 할 수 있는 운동이나 문화 생활을 즐긴다.","yes? or no? : ")
num10 = mind("연예인이나 드라마, 만화 속 주인공 등 비현실적인 인물에 열광하는 경우가 많다.","yes? or no? : ")
num11 = mind("커플인 친구들이 부럽고 그 속에서 가끔 외로움을 느낀다.","yes? or no? : ")
num12 = mind("남의 연애담을 잘 들어주고 상담해주는 것을 좋아한다.","yes? or no? : ")

a_type = mind("A 타입","러브지수 0~20% '평생 혼자 살 수도 있는 것 아냐?' 자포자기형")
b_type = mind("B 타입","러브지수 30~50% '사랑? 그게 뭔데!' 겉으로만 천상천하 유아독존형")
c_type = mind("C 타입","러브지수 60~80% '거기 누구 없나요?' 킬리만자로의 표범형")
d_type = mind("D 타입","90~100% '끓어오르는 피를 주체할 수 없어!' 활화산형")

num1.yes = num5
num1.no = num6

num2.yes = num1
num2.no = num6

num3.yes = num4
num3.no = num7

num4.yes = num7
num4.no = num8

num5.yes = num9
num5.no = num6

num6.yes = num7
num6.no = num10

num7.yes = num11
num7.no = num10

num8.yes = num12
num8.no = num11

num9.yes = a_type
num9.no = num10

num10.yes = num11
num10.no = b_type

num11.yes = c_type
num11.no = b_type

num12.yes = d_type
num12.no = num11

blood = input("당신의 혈액형은 무엇입니까? A or B or O or AB : ")

if blood == "A":
    aaa=num1
elif blood == "B":
    aaa=num2
elif blood == "O":
    aaa=num3
else:
    aaa=num4

while aaa:
    print(aaa.title)

    answer = input(aaa.option)

    aaa = aaa.vactor(answer)
