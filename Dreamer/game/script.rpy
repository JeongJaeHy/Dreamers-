﻿# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"
init:
    image gray = "#B4B4B4"
    image white = "#FFFFFF"
    image red = "#FF0000"
    image pro_1 = "prologue/pro_1.png"
    image pro_2 = "prologue/pro_2.png"
    image pro_3 = "prologue/pro_3.png"
    image pro_4 = "prologue/pro_4.png"
    image pro_5 = "prologue/pro_5.png"
    image pro_exit = "prologue/pro_exit.png"

    #캐릭터 이미지 정의.
    #아이
    image ch 1 = "Character/ch_1.png"
    image ch 2 = "Character/ch_2.png"
    image ch hospital = "Character/ch_hospital.png"
    image ch shape_s = "Character/ch_shape_s.png"
    image ch shape_m = "Character/ch_shape_m.png"
    image ch shape_l = "Character/ch_shape_l.png"

    #S
    image s surprise = "Character/s_1.png"
    image s talk = "Character/s_2_talk.png"
    image s relax = "Character/s_relax.png"
    image s normal = "Character/s_평범.png"
    image s angry = "Character/s_angry.png"
    image s cold = "Character/s_cold.png"
    image s sit = "Character/s_sit.png"
    image s scream = "Character/s_scream.png"
    image s give_up = "Character/s_give_up.png"

    #카슈
    image k far = "Character/ka_1.png"
    image k close = "Character/ka_2.png"

    #J
    image j breathe = "Character/j1.png"
    image j normal = "Character/j2.png"
    image j worry = "Character/j3_worry.png"
    image j relief = "Character/j_relief.png"
    image j scream = "Character/j_scream.png"
    image j tear = "Character/j_tear.png"
    image j standup = "Character/j_standup.png"
    image j lonely = "Character/j_lonely.png"

    #T
    image t normal = "Character/t_normal.png"
    image t serious = "Character/t_serious.png"
    image t smile = "Character/t_smile.png"
    image t surprise = "Character/t_당황.png"
    image t far = "Character/t_등장.png"
    image t cold = "Character/t_cold.png"
    image t talk = "Character/t_talk.png"

    #A
    image a normal = "Character/a.png"
    image a talk = "Character/a_talk.png"
    image a anxious = "Character/a_anxious.png"
    image a point = "Character/a_point.png"
    image a help = "Character/a_help.png"

# 게임에서 사용할 캐릭터를 정의합니다.
    define s = Character("S", color = "#C8C8FF", image = "s")
    define j = Character("J", color = "#F0ACC6", image = "j")
    define uj = Character("???", color = "#F0ACC6", image = "j")
    define a = Character("A", color = "#7B593B", image = "a")
    #20425E
    define t = Character("T", color = "#E39861", image = "t")
    define k = Character("카슈", color = "#EBE3CE", image = "k")
    define c = Character("아이", color = "#cbcbcb", image = "ch")
    define uc = Character("???", color = "#cbcbcb", image = "ch")
    define sm = Character("어머니", color = "#ffc90e")
    define sf = Character("아버지", color = "#c67748")
    define narr_nvl = Character(None, kind = nvl)

    $ c_select = False
    $ j_para = 0
    $ a_para = 0
    $ aj_check = False
    #A와 J 비교하기 위한 Boolean 변수
    #A >= J인 경우 True
    #A < J인 경우 False

    $ k_check = False
    #카슈를 안았는가..에 대한 변수
    $ a_talk_c = False
    # a가 아이에 대한 얘기를 했는가. 에 대한 변수
    $ t_check = False
    # t의 방에서 사다리를 챙겼는가에 대한 변수.
    $ a_room_check = False
    # 두 번째 선택지.
    $ save_j = False
    # J에게 양보했는가.

    define flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')

    #transform 정리
    transform slightright:
        xalign 0.15
        yalign 1.0

    transform centerleft:
        xalign 0.25
        yalign 1.0

    transform centerright:
        xalign 0.75
        yalign 1.0

# 여기에서부터 게임이 시작합니다.
label start:
    jump prologue

    #디버깅용 시작코드
    #jump a_room_1


label prologue:

    play music "audio/Prologue.mp3" fadeout 1

    scene pro_1
    "나는 밀실에 갇혔다."

    #초코바 화면에 등장.
    scene pro_2
    "이 밀실엔 아무것도 없다. 밖으로 통하는 통로라 할만한 것은 오직 환기구 뿐이다."

    "......하지만 환기구는 천장에 뚫려 있어 닿을 수 없다."

    scene pro_3
    "바닥 한 귀퉁이에는 사탕과 초코바가 쌓여 있다."

    "그 식량이 바닥나면 나는 밀실에 갇혀 굶어 죽게 될 것이다."

    #초코바 화면
    scene pro_4
    "도대체 누가 나를 가두었는지 나는 알 수 없다. 그 뿐만이 아니다.
    나 자신에 대한 아무런 정보도 기억나지 않는다."

    "오직 기억나는 것은 S라는 내 이름뿐이다.
    그런 생각에 가 닿을 때면 나는 괴로움에 몸부림친다."

    #아이 환영 등장
    show ch 1 at left
    "...언젠가부터는 어느 아이의 환영이 보이기까지 한다."

    hide ch 1 with dissolve
    show ch 1:
        yzoom -1
        xalign 0.5
        linear 2 yalign 0.0

    with moveintop
    hide ch 1 with dissolve

    show ch 1:
        yzoom 1
        xalign 1.0
        yalign 1.0
    with dissolve
    "아이는 방 한 구석에 둥둥 떠 있기도 하고, 천장에 매달려 있기도 하고, 잠에서 깬 내 얼굴 바로
    바로 앞에 얼굴을 들이밀고 있기도하다."

    "내 곁에 가까이 붙어서 있을 때면 아이는 나에게 계속 무어라 말을 하지만 들리지 않는다."

    scene black


    #"{b}이곳은 꿈이다{/b}" (what_color = "#f00", what_size = 28)


    scene pro_5 with dissolve

    "잠에서 깨자 여전히 똑같은 방이었다. 아니… 똑같은 방이 아닌가?"

    "아, 어제까지만 해도 천장에 있던 환기구가 이젠 벽면에 달려 있다!"

    "가슴이 뛰기 시작한다. 환기구가 왜 벽면에 있는지는 모르겠지만 그런 이유 따위 필요없다."

    "드디어 이 밀실을 탈출할 수 있게 되었다."

    # 아이의 환영 추가
    show ch 2 at center with dissolve
    "그 순간 아이의 환영이 다시 나타났다. 저 모습..처음으로 무어라 말을 하려는 듯 입술을 달싹이고 있다."

    #"{size=+5}{color=#aaa}{i}나갈까?{/i}{/color}{/size}  그렇게 생각하는데 벽 한 구석에 또다시 아이의 환영이 나타났다."

    menu:
        "아이와는 어차피 말도 통하지 않아. 탈출하자.":
            scene black with fade
            "환퐁구는 비좁고 축축한 것이 손에 만져진다."

            "폐소공포증에 숨이 막혀 오지만 다시 돌아갈 수는 없다."

            "한참을 벌레처럼 기어간다. 출구는 언제쯤 나올까. 아니, 출구가 있기라도 할까.. 문득 불안해진다."

            scene pro_exit with dissolve

            "저 멀리 희미한 빛이 보이기 시작했다. 출구다!"

            pause .8

            jump scene_1_start

        "그래도 아이의 말을 들어보자.":
            #아이 환영 그대로
            $ c_select = True
            "환풍구 앞에 물끄러미 서 있자 아이가 입을 열었다."

            c "…마…ㄱ….해?"

            "환청이 들리기 시작한다."

            c "막아야 해.."
            show s surprise at left with dissolve
            show ch 2 at right with dissolve
            s "!"
            s "목소리…? 지금 네 목소리가 나한테 들리는 거야?"
            c "막아야 해. 아빠."
            s "누구를 막아야 한다고?"
            c "아빠. 아빠가 모두를 방해할 거야."
            s "?"
            c "아빠가 나를 너무 사랑해서 그런 거야. 하지만 조심해야 해."
            s "아빠가 누군데? 뭘 조심하라는 거야?"
            c "..ㅇ..어"
            s "뭐라고?"
            c "이제 나가야 해."
            c "가야 해."

            "이 아이는 도대체 정체가 뭐야."

            hide ch 2 with dissolve
            scene pro_exit with dissolve
            "환영에게 무언가를 더 물어보려 했지만 강한 빛이 나타났다."

            "엄청난 압력이다."

            "그 압력이 무엇인지, 빛이 무엇인지, 아이의 말이 무슨 말인지 이해하기도 전에 나는..."

            pause .8

            jump scene_1_start

    return

label a_larger_than_j:
    if int(a_para*1.4) >= j_para :
        $ aj_check = True
    else :
        $ aj_check = False

    return

screen stats_button_screen() :
    textbutton "친밀도 확인" :
        # action : "스탯"버튼이 눌렸을 때 실행할 행동
        # if문 해석 : stats_screen이 켜져있으면 Hide하고, 꺼져있으면 Show해라.
        action If(renpy.get_screen("stats_screen"), Hide("stats_screen"), Show("stats_screen"))

        # 버튼위치, 화면에서 가로방향으로 0.95, 세로방향으로 0.05 비율 되는 곳에 존재
        align (0.95, 0.05)

# label start에서 호출된 stats_button_screen의 텍스트버튼이 눌리면 호출됨

screen stats_screen() :
    frame:
        align(0.05,0.25)
#        xysize(180, 100)
        vbox:
            spacing 3
            align(1.0, 0.5)
            text "{u}친밀도:{/u}"
            text " J와의 친밀도: [j_para] "
            text " A와의 친밀도: [a_para] "
