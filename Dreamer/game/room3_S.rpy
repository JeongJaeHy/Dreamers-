#S의 방. 세 번째 방
init:
    image bg_road = "sroom/bg_road.png"
    image bg_crossroad = "sroom/bg_crossroad.png"
    image bg_end_s = "sroom/bg_end.png"
    image bg_table = "sroom/bg_table.png"
    image bg_table_collapse = "sroom/bg_table_collapse.png"
    image bg_table_blur = "sroom/bg_table_blur.png"
    image bg_table2_frozen = "sroom/bg_table2_frozen.png"
    image bg_table2_collapse = "sroom/bg_table2_collapse.png"
    image bg_parent_lever = "sroom/bg_parent_lever.png"
    image bg_parent_door = "sroom/bg_parent_door.png"
    image bg_parent_coldoor = "sroom/bg_parent_coldoor.png"

label s_room_start :
    call a_larger_than_j from _call_a_larger_than_j
    play music "audio/S_room.mp3" fadeout 1
    #scene 1 : 검정 배경에 네 갈래 갈림길

    scene bg_crossroad with dissolve
    "웨이터 T의 방에서 뻗어나온 검은 복도는 유난히 긴 것만 같다."
    "한참을 걷다 네 갈래 길에 맞딱뜨렸다."
    "어느 곳이 열쇠가 있는 방으로 가는지 모르겠다."

    show s talk:
        xzoom 1
        xalign 0.0
        yalign 1.0
    with dissolve
    s "어떻게 할까?"
    show a talk at right with dissolve
    a "한 명씩 나눠서 가 보는 게 효율적일 것 같은데."
    show j worry at centerright with dissolve
    j "만약에 그러다 계속 서로 만나지 못하게 되면 어떡하지?"
    a "그럴 일은 없어. 지금까지의 경험으로는, 얼마나 많은 복도가 갈라지든 결국엔 하나의 방으로 모였다가, 다시 갈라지기를 반복하니까."
    j "복도 몇 개를 지나서?"
    a "최대 두 개. 그 정도면 할 만한 일이야."
    s "맞는 말인 것 같아."
    show t talk at centerleft with dissolve
    t "그럼 그렇게 하도록 해요."

    "나는 맨 오른 쪽 길이 배정되었다."

    t "혹시 복도 두 개를 지나도, 서로 만나지 못하면 다시 돌아와 여기서 만나도록 해요. 서로 떨어지는 건 처음이니까."
    a "그래. 하지만 복도 두 개를 지나도 만나지 못할 일은 없을거야."
    s "다들 무사히 다시 만나자."
    j "S, 조심해."

    scene bg_road with dissolve

    "혼자 걷는 길은 어색하다. 그새 네 명이서 왁자지껄한 분위기에 적응이 되었는지."
    "열쇠가 있는 방으로 향하기 위해 몇 개의 방을 더 거쳐야 하는지는 모른다. 다만 아직 나의 방은 나오지 않았다."
    "내 방이 나오면 내 유년기에 어떤 힌트라도 더 얻게 되지 않을까."
    "복도 저 멀리 문이 보인다."

    scene white with dissolve

    "문을 열자 밝은 빛이 쏟아진다."

    scene bg_table_blur with dissolve

    "눈을 천천히 뜨자 흐릿하게 방 안의 풍경이 보인다."
    "화려한 샹들리에...흰 식탁보..여러 음식들.."
    "미디움 레어로 구운 스테이크, 아스파라거스의 고소한 냄새, 에스까르고의 비릿하면서 달큰한 향, 한 접시에 하나씩 놓여 있는 색색가지 디저트.."
    "잠시만, 나는 어떻게 이 음식들을 다 아는 거지?"
    "어쩐지 익숙한 풍경이다. 식탁에는 몇몇 사람들이 일렬로 앉아 있다. 누구일까."
    "식탁 쪽으로 발걸음을 옮긴다."

    scene bg_table with dissolve
    "아, 그들은 내 젊은 아버지와 어머니다. 머리가 깨질 듯이 아파온다."
    "그만 바닥에 주저앉아버렸다."

    show s sit:
        xzoom -1
        xalign 0.8
        yalign 1.0
    with dissolve
    s "어머니! 아버지!"

    "식탁으로 달려갔지만 투명한 벽 같은 것에 부딪혀 다시 튕겨져나왔다. 내 부모님이 있는 풍경으로 도저히 다가갈 수가 없다."
    "...투명한 막 너머로 어린 내 모습이 보인다. 자수가 놓인 새하얀 턱받이를 하고 있다.
    젊은 어머니가 어린 나에게 온기가 흐르는 수프를 떠 먹여 주고 계신다."
    "흰 옷을 입은 직원이 새로운 메뉴를 가져다 주고, 덮개를 열자 트러플 향이 훅 끼쳐온다. 모두 내가 기억하는 맛들, 향들, 수프의 온기.."

    s "트러플..."

    if aj_check == True :
        jump s_room_1_a
    else :
        jump s_room_1_j

label s_room_1_a:
    show a talk:
        xzoom 1
        xalign 1.0
        yalign 1.0
    with moveinright
    a "S!"

    "A가 내 어깨를 잡고 흔든다."

    a "S, 정신차려. 여기서 이러면 안 돼."

    "A가 언제 이 방까지 왔는지도 모르겠다. 머릿속이 혼란스럽다."

    s scream "저 안에 우리 가족이 있어. 저기로 가야 해."
    a "막 뒤에 있다는 건 죽었다는 말이야."
    s "어린 나도?"
    a "어린 시절의 너도 어딘가에서 죽어있다는 거지."
    s "저 풍경으로 들어가고싶어."
    a "이봐 친구. 그럴 방법은 없어."

    if k_check == True :
        s "지금까지, T도, J도, 결국엔 정원에 발을 디디고, 카슈를 품에 안았잖아. 왜 나는 가 닿는 것 조차 안 되는 걸까."
        a "어린 카슈는 꽁꽁 얼어붙었잖아."

    s surprise "얼어붙더라도 만나고 싶어. 단 한 번이라도 안겨 보고 싶다고."
    a "그게 과연 저들이 원하는 일일까?"

    "A의 말은 귀에 들어오지 않았다."
    "나는 물밀듯이 밀려 들어오는 과거의 기억과 싸우며 간신히 바닥을 딛고 서 있다. 이렇게 갑작스럽게, 모든 것을 알려주고 모든 것을 다시 빼앗아간다고?"

    s scream "아버지! 어머니!"
    a anxious "그래봤자 너만 손해야. 아까 T가 했던 일이랑 똑같아. 백날 이미 없어진 주인같은 걸 그리워해봤자 아무것도 바뀌지 않는다고."
    s "아니야. T가 문을 닫기 직전에 정원이 빛나고 있었다고 이야기했잖아."
    a talk "그게 진짜일 것 같아?"
    s talk "나는 진짜라고 믿어."
    a "믿음과 사실은 별개야."
    s scream "두 분 모두 안녕을 말 할 시간도 없이 돌아가셨어. 너무나 갑작스럽게. 하지 못 한 이야기들이 너무 많아. 너무 많아서 무슨 말을 먼저 해야 할 지 모를 정도로.."
    a "이봐, 그렇다고 여기 눌러앉아서 벽을 두드릴 수는 없어."
    s "부모님이 불러주시는 내 이름을 한 번이라도 더 듣고 싶어."
    a "환상에게 네 이름을 듣는 건 의미가 없어. J와 T가 너를 기다리고 있잖아."
    a "여기에 오래 있으면 네 몸 전체가 얼어붙기 시작할거야. 이미 발이 얼고 있어."

    show s give_up:
        xalign 0.8
        yalign 1.0
    "발을 내려다보자 발목 부근까지 성에가 매달려 있다."

    s "..."
    a "환상이 강력한 것은 나도 인정해. 알아. 하지만 환상을 깨부숴야 현실을 살지."
    a "..너를 생각해서 해 주는 말이야. 진심으로."

    menu:
        "A의 말이 맞다. 몸 전체가 얼기 전에 방을 나가자." :
            show s surprise:
                xzoom 1
                xalign 0.8
                yalign 1.0
            with dissolve
            s "..그래 네 말이 맞아."
            a "카슈도, 정원도, 그런 환상이었지. 그렇지만 다들 잘 떠나왔어. 열쇠를 향해 가려고."
            s "나를 기다린다고 했지."
            a "가자. 다들 다음 복도에서 모여 기다리고 있어."
            s normal "..."

            "A는 나를 끌어당기기 시작했다."
            show a talk:
                linear 3 xalign 1.2
                yalign 1.0
            with move
            show s normal:
                linear 3 xalign 1.0
                yalign 1.0
            with move
            "내 두 발은 이미 감각이 없어 무거운 모래주머니를 매달고 있는 것만 같은 느낌이다."
            "젊은 어머니가 어린 나에게 부드러운 브로콜리를 잘라 먹여 준다. 가기 싫어 몸부림치지만 A를 힘으로 이길 수 없다."
            scene black with dissolve
            pause .5
            scene bg_table with dissolve
            show s normal at centerright
            show a talk at right
            "그런데 분명히 A에게 이끌려 문 밖으로 나섰는데, 다시 이 방으로 들어와버렸다."

            a anxious "...다시 이 방이잖아."
            a "그러면..."

            "A가 무어라 중얼거릴 때도, 나는 막 뒤에 있는 부모님 생각 뿐이었다."

            a normal "저 풍경으로 들어가야 되겠군."

            jump s_room_2_a

        "A의 말은 틀렸다. 부모님을 한 번 더 불러보자." :
            jump s_room_2_a

label s_room_2_a:
    show s scream:
        xzoom -1
        xalign 0.75
        yalign 1.0
    with move
    s "어머니! 아버지!"
    a "{i}(.....그래 여기 레버가 있었지){/i}" (what_color = "#B4B4B4", what_size = 24)

    a  "S, 이것 봐. 여기 레버가 있어. 이게 아마도..저 막을 없애지 않을까?"
    show s talk:
        xzoom 1
    s "레버라고?"
    a "레버가 꽤 무거워서 같이 돌려야 해."

    "미친듯이 레버를 돌렸다. 레버를 한 바퀴 돌릴 때 마다 테이블에서의 말소리가 짙어진다."
    "막이 허물어진 것이 온 몸으로 느껴졌다. 나는 식탁으로 달려갔다."
    show s surprise:
        xzoom -1
        xalign 0.5
        yalign 1.0
    with move
    scene bg_parent_door with dissolve
    show s surprise:
        xzoom -1
        xalign 0.5
        yalign 1.0
    "내가 한 걸음을 내딛자마자 식탁 끝 오른쪽 벽에 문이 생겨났다."
    "갑자기 생겨나는 문이든 뭐든 하나도 신기하지 않았다. 오로지 내겐 부모님을 부르고 싶다는 생각이 전부였다."

    show a anxious at right with dissolve
    a "이봐, 방이 무너지고 있어."

    "A의 말마따나 방이 무너지고 있었다. 나는 휘청였다."
    scene bg_parent_coldoor with vpunch
    show a anxious at right
    show s surprise:
        xzoom -1
        xalign 0.5
        yalign 1.0
    "방 끝에서부터 샹들리에가 천천히 흔들리고 있다."

    a "S, 시간이 없어. 그대로 문으로 달려가! 어차피 말을 걸어도 들을 수 없어. 손을 잡아도-"

    menu:
        "부모님을 마지막으로 안아본다.":
            "A를 뿌리치고 테이블 쪽으로 달려갔다."

            show s scream:
                xzoom -1
                xalign 0.40
                yalign 1.0
            with move
            s "어머니! 아버지! 저에요."

            "아버지는 행복한 표정으로 어린 내 입 안에 으깬 감자를 먹여 주고 있다."
            scene bg_parent_lever with dissolve
            "어머니는 트러플 파스타를 한 입 먹고 있는데.."

            sm "우리 아들도 얼른 트러플 파스타 맛을 아는 나이가 되었으면 좋겠어."
            sf "이십 년 정도 지나면 그러지 않을까."
            sm "까마득한데."
            sf "언젠가 그런 시간이 오겠지."

            "아버지와 어머니가 서로를 바라보며 웃고 있다. 내 목소리가 들리지 않는 것일까."

            show s scream:
                xzoom -1
                xalign 0.7
                yalign 1.0
            with moveinright
            s "아버지!"
            "아버지의 손을 잡았다."

            scene bg_table2_frozen with dissolve
            "아버지는 내 손이 닿는 순간 말을 잇지 못하고 얼어붙었다."
            "나는 다를 것이라 생각했는데 결국 A의 말이 맞았다."
            "다리에 힘이 풀려 주저앉았다. 어머니가 망연자실한 표정으로 나와 얼어붙은 아버지를 번갈아 바라보았다."

            sm "S야. 우리 아들!"

            "어머니까지 얼음으로 만들 수는 없다. 나는 바닥에 앉은 채로 뒷걸음칠진다."
            "이 순간에도 어머니의 품에 안기고 싶은 마음과, 그저 도망쳐 버리고 싶은 마음이 공존하고 있다."

            sm "어딜 가는 거니, 한 번 안아 보자."

            menu:
                "어머니를 피해 도망친다.":
                    a "그래. 어머니까지 얼게 할 수는 없어. 빨리 도망쳐와!"

                    "A의 목소리가 어디선가 환청처럼 들린다."
                    scene bg_table2_frozen with hpunch
                    "방이 점점 붕괴하기 시작하고, 나는 어머니 머리 위로 큰 샹들리에가 떨어지는 것을 마지막으로 눈에 담고, 방을 빠져나왔다."
                    "어린 나의 울음소리가 머릿속에서 맴돌았다."
                    scene bg_end_s with dissolve
                    pause .8

                    call note5 from _call_note5
                    jump a_room_start

                "혹시 모를 기적이 있지 않을까. 도저히 도망칠 수가 없다.":
                    "일어서지 못하고 있던 찰나, 어머니가 내 볼에 손을 가져다 대었다."
                    "그 손은 정말이지 따스했으나.."
                    "어머니는 그와 동시에 내 이름을 부르려는 입모양 그대로 얼어붙었다."
                    "천장에서 샹들리에가 떨어져 접시들을 박살나고 있다."

                    a "말 했잖아. 환상일 뿐이라고! 닿으면 얼어붙어. 얼음성은 그래. 아무 의미가 없단 말이야."

                    "A의 목소리가 어디선가 환청처럼 들려온다."
                    "A가 나를 아무렇게나 질질 끌고서 문으로 달려간다."
                    scene bg_table2_frozen with vpunch
                    "문이 닫히기 전 마지막으로 본 방 안에는 새하얗게 얼은 어머니와 아버지가 못 박힌 듯 서 있었다."

                    call note5 from _call_note5_1
                    jump a_room_start

        "A를 따라 문으로 달려간다.":
            scene bg_parent_lever with dissolve
            "아버지는 행복한 표정으로 어린 내 입 안에 으깬 감자를 먹여 주고 있다. 어머니는 트러플 파스타를 한 입 먹으며 이야기한다."

            sm "우리 아들도 얼른 트러플 파스타 맛을 아는 나이가 되었으면 좋겠어."
            sf "이십 년 정도 지나면 그러지 않을까."
            sm "까마득한데."
            sf "언젠가 그런 시간이 오겠지."

            "아버지와 어머니가 서로를 바라보며 웃고 있다. 그 말소리는 점점 멀어져간다."
            scene bg_table2_collapse with vpunch
            "방을 흔드는 진동이 점점 강해지고, 천장에서 샹들리에가 떨어져 접시들을 박살내며 테이블이 이상한 모양으로 뒤틀리기 시작한다."
            "다시 멈춰 서고 싶지만 A가 나를 떠미는 탓에 멈춰 설 수 없다."
            "간발의 차이로 방이 붕괴되고, 나는 문 밖으로 나동그라졌다."
            scene bg_end_s with dissolve
            pause .8

            call note5 from _call_note5_2
            jump a_room_start

label s_room_1_j:
    show j worry at right with dissolve
    j "S!"

    "J가 내 어깨를 잡고 흔든다."

    j "S, 정신차려. 여기서 이러면 안 돼."

    "J가 언제 이 방까지 왔는지도 모르겠다. 머릿속이 혼란스럽다."

    s scream "저 안에 우리 가족이 있어. 저기로 가야 해."
    j "막 뒤에 있다는 건 진짜가 아니야."
    s "저 풍경으로 들어가고싶어."
    j lonely "S... 그럴 방법은 없어."

    if k_check == True :
        s "지금까지, T도, J도, 결국엔 정원에 발을 디디고, 카슈를 품에 안았잖아. 왜 나는 가 닿는 것 조차 안 되는 걸까."
        j "어린 카슈는 꽁꽁 얼어붙었잖아."

    s surprise "얼어붙더라도 만나고 싶어. 단 한 번이라도 안겨 보고 싶다고."
    j worry "그게 과연 네 가족이 원하는 일일까? 나는 여기서 어린 카슈를 품에 안은 게 가장 후회되는 일이라고."

    "J의 말은 귀에 들어오지 않았다."
    "나는 물밀듯이 밀려 들어오는 과거의 기억과 싸우며 간신히 바닥을 딛고 서 있다. 이렇게 갑작스럽게, 모든 것을 알려주고 모든 것을 다시 빼앗아간다고?"

    s scream "아버지! 어머니!"
    j "그래봤자 너만 손해야. S.."
    s "두 분 모두 안녕을 말 할 시간도 없이 돌아가셨어. 너무나 갑작스럽게. 하지 못 한 이야기들이 너무 많아. 너무 많아서 무슨 말을 먼저 해야 할 지 모를 정도로.."
    j lonely "그렇다고 여기 눌러앉아서 벽을 두드릴 수는 없어. 응?"
    s "부모님이 불러주시는 내 이름을 한 번이라도 더 듣고 싶어."
    j "환상에게 네 이름을 듣는 건 의미가 없어. A와 T가 너를 기다리고 있잖아."
    j "여기에 오래 있으면 네 몸 전체가 얼어붙기 시작할거야. 이미 발이 얼고 있어. S, 제발..."

    show s give_up:
        xalign 0.8
        yalign 1.0

    "발을 내려다보자 발목 부근까지 성에가 매달려 있다."

    s "..."
    j worry "환상이 강력한 것은 나도 인정해. 알아. 하지만 환상을 깨부숴야 현실을 살지."
    j "우리 지금까지 잘 버텨 왔잖아. 돌아가신 네 부모님도 네가 무사히 꿈에서 빠져나오길 바랐을 거야."

    menu:
        "J의 말이 맞다. 몸 전체가 얼기 전에 방을 나가자." :
            show s surprise:
                xzoom 1
                xalign 0.8
                yalign 1.0
            with dissolve
            s "..그래 J,네 말이 맞아."
            j lonely "카슈도, 정원도, 그런 환상이었잖아. 그렇지만 다들 잘 떠나왔어. ...열쇠를 향해 가려고."
            s "나를 기다린다고 했지."
            j "가자. 힘들겠지만. 다들 다음 복도에서 모여 기다리고 있어."
            s normal "..."

            "J는 나를 끌어당기기 시작했다."
            show j standup:
                linear 3 xalign 1.2
                yalign 1.0
            with move
            show s normal:
                linear 3 xalign 1.0
                yalign 1.0
            with move

            "내 두 발은 이미 감각이 없어 무거운 모래주머니를 매달고 있는 것만 같은 느낌이다."
            "젊은 어머니가 어린 나에게 부드러운 브로콜리를 잘라 먹여 준다. J에게 이끌려, 쉽사리 떨어지지 않는 발걸음을 옮겼다."
            scene black with dissolve
            pause .5
            scene bg_table with dissolve
            show s normal at centerright
            show j worry at right
            "그런데 분명히 J에게 이끌려 문 밖으로 나섰는데, 다시 이 방으로 들어와버렸다."

            j "...다시 이 방이잖아. 그럼 어떻게 해야 하지...?"

            "J가 무어라 중얼거릴 때도, 나는 막 뒤에 있는 부모님 생각 뿐이었다."

            jump s_room_2_j

        "J의 말은 틀렸다. 부모님을 한 번 더 불러보자." :
            jump s_room_2_j

label s_room_2_j:
    show s scream:
        xzoom -1
        xalign 0.75
        yalign 1.0
    with move
    s "어머니! 아버지!"

    j worry "{i}(....잠시만 저건 뭐지? 레버잖아..?){/i}" (what_color = "#B4B4B4", what_size = 24)
    j "S, 이것 봐. 여기 레버가 생겨났어! 이게 아마도..저 막을 없애지 않을까?"
    show s talk:
        xzoom 1
    s "레버라고?"
    j "레버가 꽤 무거워서 같이 돌려야 해."

    "미친듯이 레버를 돌렸다. 레버를 한 바퀴 돌릴 때 마다 테이블에서의 말소리가 짙어진다."
    "막이 허물어진 것이 온 몸으로 느껴졌다. 나는 식탁으로 달려갔다."
    show s surprise:
        xzoom -1
        xalign 0.5
        yalign 1.0
    with move
    scene bg_parent_door with dissolve
    show s surprise:
        xzoom -1
        xalign 0.5
        yalign 1.0
    "내가 한 걸음을 내딛자마자 식탁 끝 오른쪽 벽에 문이 생겨났다."
    "갑자기 생겨나는 문이든 뭐든 하나도 신기하지 않았다. 오로지 내겐 부모님을 부르고 싶다는 생각이 전부였다."

    show j lonely at right with dissolve
    j "S. 빨리 와. 방이 무너지고 있어."

    "J의 말마따나 방이 무너지고 있었다. 나는 휘청였다."
    scene bg_parent_coldoor with vpunch
    show j lonely at right
    show s surprise:
        xzoom -1
        xalign 0.5
        yalign 1.0
    "방 끝에서부터 샹들리에가 천천히 흔들리고 있다."

    j "S, 시간이 없어. 그대로 문으로 달려가! 어차피 말을 걸어도 들을 수 없어. 손을 잡아도-"

    menu:
        "부모님을 마지막으로 안아본다.":
            "J를 뿌리치고 테이블 쪽으로 달려갔다."
            show s scream:
                xzoom -1
                xalign 0.40
                yalign 1.0
            with move

            s "어머니! 아버지! 저에요."

            "아버지는 행복한 표정으로 어린 내 입 안에 으깬 감자를 먹여 주고 있다."
            scene bg_parent_lever with dissolve
            "어머니는 트러플 파스타를 한 입 먹고 있는데.."

            sm "우리 아들도 얼른 트러플 파스타 맛을 아는 나이가 되었으면 좋겠어."
            sf "이십 년 정도 지나면 그러지 않을까."
            sm "까마득한데."
            sf "언젠가 그런 시간이 오겠지."

            "아버지와 어머니가 서로를 바라보며 웃고 있다. 내 목소리가 들리지 않는 것일까."

            show s scream:
                xzoom -1
                xalign 0.7
                yalign 1.0
            with moveinright
            s "아버지!"
            "아버지의 손을 잡았다."

            scene bg_table2_frozen with dissolve

            "아버지는 내 손이 닿는 순간 말을 잇지 못하고 얼어붙었다."
            "나는 다를 것이라 생각했는데 결국 J의 말이 맞았다."
            "다리에 힘이 풀려 주저앉았다. 어머니가 망연자실한 표정으로 나와 얼어붙은 아버지를 번갈아 바라보았다."

            sm "S야. 우리 아들!"

            "어머니까지 얼음으로 만들 수는 없다. 나는 바닥에 앉은 채로 뒷걸음칠진다."
            "이 순간에도 어머니의 품에 안기고 싶은 마음과, 그저 도망쳐 버리고 싶은 마음이 공존하고 있다."

            sm "어딜 가는 거니, 한 번 안아 보자."

            menu:
                "어머니를 피해 도망친다.":
                    j "그래. 어머니까지 얼게 할 수는 없어. 빨리 도망쳐와!"

                    "J의 목소리가 어디선가 환청처럼 들린다."
                    scene bg_table2_frozen with hpunch
                    "방이 점점 붕괴하기 시작하고, 나는 어머니 머리 위로 큰 샹들리에가 떨어지는 것을 마지막으로 눈에 담고, 방을 빠져나왔다."
                    "어린 나의 울음소리가 머릿속에서 맴돌았다."
                    scene bg_end_s with dissolve
                    pause .8

                    call note5 from _call_note5_3
                    jump a_room_start

                "혹시 모를 기적이 있지 않을까. 도저히 도망칠 수가 없다.":
                    "일어서지 못하고 있던 찰나, 어머니가 내 볼에 손을 가져다 대었다."
                    "그 손은 정말이지 따스했으나.."
                    "어머니는 그와 동시에 내 이름을 부르려는 입모양 그대로 얼어붙었다."
                    "천장에서 샹들리에가 떨어져 접시들을 박살나고 있다."

                    j "말 했잖아. 환상일 뿐이라고! 닿으면 얼어붙어. A도 말했잖아. 얼음성은 그래. 아무 의미가 없단 말이야."

                    "J의 목소리가 어디선가 환청처럼 들려온다."
                    "J가 나를 부축하고서 문으로 달려간다."
                    scene bg_table2_frozen with vpunch
                    "문이 닫히기 전 마지막으로 본 방 안에는 새하얗게 얼은 어머니와 아버지가 못 박힌 듯 서 있었다."

                    call note5 from _call_note5_4
                    jump a_room_start

        "J를 따라 문으로 달려간다.":
            "아버지는 행복한 표정으로 어린 내 입 안에 으깬 감자를 먹여 주고 있다. 어머니는 트러플 파스타를 한 입 먹으며 이야기한다."
            scene bg_parent_lever with dissolve

            sm "우리 아들도 얼른 트러플 파스타 맛을 아는 나이가 되었으면 좋겠어."
            sf "이십 년 정도 지나면 그러지 않을까."
            sm "까마득한데."
            sf "언젠가 그런 시간이 오겠지."

            "아버지와 어머니가 서로를 바라보며 웃고 있다. 그 말소리는 점점 멀어져간다."
            scene bg_table2_collapse with vpunch
            "방을 흔드는 진동이 점점 강해지고, 천장에서 샹들리에가 떨어져 접시들을 박살내며 테이블이 이상한 모양으로 뒤틀리기 시작한다."
            "다시 멈춰 서고 싶지만 J가 나를 떠미는 탓에 멈춰 설 수 없다."
            "간발의 차이로 방이 붕괴되고, 나는 문 밖으로 나동그라졌다."
            scene bg_end_s with dissolve
            pause .8

            call note5 from _call_note5_5
            jump a_room_start
