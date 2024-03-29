#J방에서 일어나는 여러가지 선택들에 대한 것 & 첫번째방.
init:
    image bg_box = "jroom/bg_box.png"
    image bg_cliff = "jroom/bg_cliff.png"
    image bg_end_j = "jroom/bg_end.png"
    image bg_frozen_door = "jroom/bg_frozen_door.png"
    image bg_j_run = "jroom/bg_j_run.png"
    image bg_jroom = "jroom/bg_jroom.png"
    image bg_ka = "jroom/bg_ka.png"
    image bg_ka_frozen = "jroom/bg_ka_frozen.png"
    image bg_ka_run = "jroom/bg_ka_run.png"
    image bg_avalanche = "jroom/bg_avalanche.png"


label j_room_start :
    play music "audio/J_room.mp3" fadeout 1
    scene bg_jroom

    "방에 들어오니 눈보라가 치는 눈밭이 우리를 맞이한다."
    "옆에 누군가가 있다는 것만 확인할 수 있을 뿐 그 이상의 시야가 확보되지 않는 눈보라다."

    "갑자기 카슈가 짖더니 어디론가 달려간다."
    scene bg_ka_run with dissolve
    j "카슈…!"
    scene bg_j_run with dissolve

    "J가 카슈를 뒤쫓아 저 멀리 보이지 않는 곳으로 사라져버렸다. J를 쫓아가볼까?"

    menu:
        "J 혼자 가도록 둘 수 없다. J를 쫓아간다.":
            $ j_para += 2
            scene bg_jroom

            show t cold at left with dissolve
            t "이 방은 정말 춥네요, 무슨 일이 있었길래 이렇게 추운걸까요?"
            show s cold at right with dissolve
            s "이 방이 J의 삶과 관련이 있다면... 그러게요, J는 활발하고 따뜻한 사람이라 이런 방을 맞게 될거라고는 생각 못했는데..."
            t "정말 J씨에게는 무슨 일이 있었던 걸까요? S씨는 J씨를 나보다 더 먼저 만났으니까, 그 동안 들은 이야기 뭐 없어요?"
            s "글쎄요, 저도 그건 잘..."

            jump j_room_1 #2

        "J를 쫓아가지 않는다. 뭐가 있을지 알고 함부로 움직인단 말인가?":
            $ j_para -= 2

            "돌아가려는 찰나, J가 떠난 쪽에서 갑자기 큰 소리가 난다." #쿠궁
            "{b}쿠궁!{/b}" (what_color = "#f00", what_size = 20)
            menu:
                "걱정되네.. 아무래도 쫓아가 봐야겠다.":
                    $ j_para += 1
                    scene bg_jroom

                    show t cold at left with dissolve
                    t "이 방은 정말 춥네요, 무슨 일이 있었길래 이렇게 추운걸까요?"
                    show s cold at right with dissolve
                    s "이 방이 J의 삶과 관련이 있다면... 그러게요, J는 활발하고 따뜻한 사람이라 이런 방을 맞게 될거라고는 생각 못했는데..."
                    t "정말 J씨에게는 무슨 일이 있었던 걸까요? S씨는 J씨를 나보다 더 먼저 만났으니까, 그 동안 들은 이야기 뭐 없어요?"
                    s "글쎄요, 저도 그건 잘..."

                    jump j_room_1 #2

                "내 알 바야? 여기 있는게 좋을 것 같다":
                    $ j_para -= 1
                    scene bg_jroom

                    show s normal at left with dissolve
                    s "그냥 가죠, 어차피 4명 채워서 얼음성에 들어왔으니. 어차피 열쇠는 1명 밖에 못 잡는다면서요."
                    jump j_room_end #6, end


label j_room_1: #2
    "{b}꺄아아아악{/b}" (what_color = "#f00", what_size = 20)
    "어디선가 J의 비명소리가 들린다!"
    hide s with moveoutleft
    hide t with moveoutleft
    scene bg_cliff with dissolve
    "소리가 나는 방향으로 뛰어가니 절벽이 등장했다."
    "절벽 앞에 J가 눈보라에 휩싸여 몸이 둥둥 떠있다."
    scene white with dissolve
    scene bg_cliff with vpunch
    "갑자기 빛이 번쩍이고 땅이 흔들린다."

    menu:
        "어떻게든 J를 구해보자!":
            $ j_para += 2

            show s surprise:
                xzoom -1
                xalign 1.0
                yalign 1.0

            with dissolve
            s "일단 J를 끌어내려봐야겠어!"

            show s surprise:
                xalign 0.2
                yalign 0.5

            with move
            "눈보라에 휩싸인 J의 다리를 잡고 끌어내리려 노력한다."
            "하지만 내 몸도 따라 올라가기 시작한다."

            t "S씨, 당신 몸도 J씨를 따라 올라가고 있는걸요!"
            s "어떡하죠? 점점 절벽으로 가는데... 이대로 가면 떨어질 것 같은데!!"

            "T가 급히 내 옷을 잡는 게 느껴진다. 하지만 힘에 부친 것 같다."
            show k close at right with moveinright
            k "멍멍!!"
            show k close:
                xzoom -0.5
                xalign 0.2
                yalign 0.5
            with move

            hide s with moveoutright
            "갑자기 카슈가 나타나 나와 T를 쳐내고 J를 붙잡는다."
            "눈보라가 절벽 끝에 다다랐을 때, 카슈는 J를 힘차게 끌어내리고 절벽 밑으로 사라져간다..."
            hide k with moveoutbottom

            jump j_room_2 #3

        "위험해보인다. J를 돕지 않는다.":
            $ j_para -= 2

            show k close at right with moveinright
            k "멍멍!!"
            show k close:
                xzoom -0.5
                xalign 0.2
                yalign 0.5
            with move

            "갑자기 카슈가 나타나 멍하니 있던 나와 T를 쳐내고 J를 끌어내리려 한다."
            k "끼잉.."
            "안간힘을 써보지만, J와 카슈를 담은 눈보라는 점점 절벽을 향해간다."
            hide k with moveoutbottom
            "눈보라가 절벽 끝에 다다랐을 때, 카슈는 J를 힘차게 끌어내리고 절벽 밑으로 사라져간다..."

            jump j_room_2 #3

label j_room_2:
    show j worry at right with dissolve
    j "무슨 일이 일어난거지? 언제 왔어? 카슈는?"
    show s surprise:
        xzoom 1
        xalign 0.0
        yalign 1.0
    with dissolve
    s "너를 쫓아오다 비명소리가 들려서 왔더니 너는 눈보라 속에 있었고 카슈는..."
    s "...너를 구하려다 저기 절벽 밑으로 떨어졌어"
    j scream "뭐?!!"
    j "그럴리가 없어… 카슈가…. 카슈가 사라졌다고…? 카슈가? 카슈!"

    "이 때, A가 무슨 말을 하려는 듯 하다."
    menu:
        "A의 말을 들어보기로 한다.":
            $ a_para += 1
            hide j
            show a talk at right with dissolve
            a "카슈는 사라졌네, 안타깝게도."
            a "이게 다 얼음성을 탈출하려는 욕심 때문일지도 몰라. 왜 우리는 소중한 것들을 잃게 되는 거지?"
            a "결국 욕심만 내다가 소중한 것을 잃고 나면 그때야 깨닫게 되는거지, 내가 잘못했다는 걸."
            a "그리고 우리는 허울뿐인 그 명예를 뒤집어 쓰고 마음은 공허하게 빈 채 살게 되는거야."
            a "그 누구도 없는 혼자만 남은 세계에 빠지게 되는거지..."

            show t serious at center with dissolve
            t "A씨가 무슨 소리를 하고 있는거죠?"
            s "저도 모르겠어요. 근데 기분이 뭔가 썩 좋아지는 말은 아니네요."

            jump j_room_3 #4

        "A의 말을 들어보지 않는다.":
            jump j_room_3 #4

label j_room_3: #4
    scene bg_box with dissolve
    "갑자기 어디선가 강아지가 짖는 소리가 들린다."

    "강아지" "멍멍!" (who_color = "#ebe3ce")
    show j scream at right with dissolve
    j "카슈...?"

    "소리가 나는 쪽을 보니 눈밭 한 가운데 버려진 상자가 보인다."
    scene bg_ka with dissolve
    "J가 다가가서 상자를 열자 오들오들 떨고 있는 털 빠진 작은 개가 있다."

    show j scream at center with moveinright
    j "카슈..!"

    "J가 카슈에게 손을 대려고 한다."
    menu:
        "J를 말린다.":
            $ j_para += 1

            show s talk at left with dissolve
            s " 손대지 마. 알잖아, 손대면 얼어버린다는 걸."

            "내가 그 말을 하자 J가 흐느끼며 주저 앉는다."

            j tear "카슈를 만나기 전까지 나는 늘 혼자였어. 내 곁엔 아무도 없었다고."
            j "난 늘 혼자였고 나를 둘러싼 빈 공간이 너무 춥고 시렸어 이 겨울처럼..."
            j "카슈도 나와 같았어, 버려지고 사라져도 아무도 모르는 그런 존재였어."
            j "우리는 이렇게 만나서 서로의 빈 공간을 채워 나갔어. 카슈는 내 유일한 친구였다고."

            show t talk at right with dissolve
            t "카슈는 여기 있잖아요, 저건..."
            hide t
            show a talk at right with dissolve
            a "환영이지."

            "나는 울고 있는 J의 어깨에 손을 올렸다."

            s "그래 가자고, 환영일뿐이야."
            s "어서 털고 여기를 벗어나야해! 여기에 오래 있으면 우리는 여기서 얼어버리고 곧 방이 무너질거야, 영원히 얼음성에 갇히게 된다고."

            "J의 흐느낌이 잦아든다. J가 눈물을 닦고 일어선다."

            j standup "그래, 카슈도 내가 살아서 행복하기를 바랄거야, 가자."

            scene bg_end_j with dissolve
            "우리는 방을 나섰다."

            call note3 from _call_note3
            jump t_room_start

        "J를 말리지 않는다.":
            $ j_para -= 1
            $ k_check = True

            scene bg_ka_frozen
            "J가 카슈를 품에 안는다. 하지만 J가 품에 안자마자 과거의 카슈는 얼어붙어 버린다."
            show j tear at center
            "J는 놀라며 얼어붙어버린 카슈를 계속 어루만졌다. 머지않아 J는 얼어붙은 카슈를 품에 안고 흐느끼기 시작했다."

            menu:
                "J를 위로한다.":
                    $ j_para += 2

                    show s talk at left with dissolve
                    "나는 울고 있는 J의 어깨에 손을 올렸다."

                    j "카슈를 만나기 전까지 나는 늘 혼자였어. 내 곁엔 아무도 없었다고."
                    j "난 늘 혼자였고 나를 둘러싼 빈 공간이 너무 춥고 시렸어 이 겨울처럼..."
                    j "카슈도 나와 같았어, 버려지고 사라져도 아무도 모르는 그런 존재였어."
                    j "우리는 이렇게 만나서 서로의 빈 공간을 채워 나갔어. 카슈는 내 유일한 친구였다고."

                    show t talk at right with dissolve
                    t "카슈는 여기 있잖아요, 저건..."
                    hide t
                    show a talk at right with dissolve
                    a "환영이지."

                    s "그래 가자고, 환영일뿐이야."
                    s "어서 털고 여기를 벗어나야해! 여기에 오래 있으면 우리는 여기서 얼어버리고 곧 방이 무너질거야, 영원히 얼음성에 갇히게 된다고."

                    "J의 흐느낌이 잦아든다. J가 눈물을 닦고 일어선다."

                    j standup "그래, 카슈도 내가 살아서 행복하기를 바랄거야, 가자."

                    scene bg_end_j with dissolve
                    "우리는 방을 나섰다."

                    call note3 from _call_note3_1
                    jump t_room_start

                "J를 위로하지 않는다.":
                    $ j_para -= 2

                    jump j_room_4 #5

label j_room_4: #5
    "나는 울고 있는 J를 거칠게 일으켜세웠다."

    show s angry at left with dissolve
    s "가자고, 여기 남아서 얼어 죽고 싶어? 우리한테까지 피해주지 말고 얼른 가자고!"

    "J가 일어나 나를 밀치며 말한다."

    j scream "네가 뭘 알아? 우리 카슈가 나에게 어떤 존재였는지 네가 알아?"
    show s normal at left
    j "나 혼자였던 세상 속에서 유일하게 나와 함께 있어준게 카슈였단 말이야! 네가 내 마음을 알아?"

    "J의 말을 듣더니 A가 반응한다."

    show a talk at right with dissolve
    a "혼자라, 우리 중에 혼자이지 않았을 사람이 어디 있겠나?"
    a "세상은 혼자인 법이지. 누군가를 만나 잠깐의 따뜻함을 느낄 수는 있어도, 이걸 봐. 우리 모두 결국 혼자가 되었잖아."
    a "세상은 혼자 살아가는 우리를 돌봐주지 않아, 눈길 한 번 주지 않는다고. 결국 우리는 혼자 살다, 아무에게도 기억되지 못하고 잊혀진 채 사라지는거야."

    a "그래도 얼음성은 그렇지 않잖아."
    a "이 곳에서는 말을 걸 사람도 있고. J, 너는 카슈도 만났어."
    a "뭐, 조금 시간을 줄까? 우리는 먼저 가고 있을게. 마음이 정리되면 나중에 천천히 따라오라고."
    hide a with moveoutright

    "A의 말을 듣더니 J가 고민을 한다."

    j standup "그래 카슈, 얼음성 밖 세계에는 네가 없어..."

    "J가 카슈를 쓰다듬으며 고민하고 있다.."
    menu:
        "J를 데리고 이 곳을 빠져나간다.":

            s angry "정신차려, 이 곳에 있다는 건 너는 죽은 것도 아니고 산 것도 아니라는 거야. 얼음성 이후에는 뭐가 있을지 몰라."
            s "봐 우리 벌써 얼기 시작했다고. 곧 있으면 이 방이 무너질거야. 카슈가 원하는 건 네가 죽어서 카슈와 함께 하는 건 아닐거야. 나가자 빨리."

            scene black with dissolve
            scene bg_end_j
            "나는 J를 억지로 끌고 방을 나갔다."

            call note3 from _call_note3_2
            jump t_room_start

        "J가 얼음성에 남으면 내가 열쇠를 가지고 이 곳을 탈출할 수 있잖아? J를 얼음성에 남도록 한다.":

            s surprise "누가 가자고 해도 안 갈 기세구만. 그래, 남으려면 남아. 나는 떠날거야."
            j tear "카슈를 두고 떠날 수 없어..."

            jump end_3_bad

label j_room_end: #6
    "T와 A가 각자 무슨 말을 하려 한다. 누구의 말을 들을까?"
    menu:
        "T의 말을 듣는다.":
            $ j_para += 2
            $ a_para += 2

            show t talk at center with dissolve
            t "잠깐만... 잘 생각해봐요... J씨를 이대로 두고 가면 혼자 이 얼음성에 영영 갇히게 될지도 몰라요."
            t "저 소리를 들었잖아요, J씨에게 무슨 일이 생긴게 분명해요. 다음 방에서 우리에게 무슨 일이 일어나지 않을거라는 보장있어요?"
            t "그 때도 우리가 지금처럼 당신을 놓고 가기를 원하나요? 아니면 누군가 당신과 함께 있어주기를 원하나요?"

            "t의 말을 듣고 나니.."

            menu:
                "맞는 말 같다. T의 의견에 따르기로 한다.":
                    t serious "J씨도 우리가 가주기를 원하고 있을거에요, 우리 같이 이 성을 탈출하기를요."
                    s "그래요. 가자고요."

                    jump j_room_1 #2

                "아닌 것 같다. T의 의견을 듣지 않는다.":
                    $ j_para -= 2

                    "그 때, J가 눈물을 흘리며 돌아왔다."

                    show j at right with moveinright
                    j "카슈가... 카슈가 나를 살리려다 죽었어..."
                    j "눈보라가 불어서 내가 절벽으로 떨어질 뻔했는데... 카슈가 나를 살리고 절벽 아래로 떨어졌어... 카슈..."

                    jump j_room_3 #4

        "A의 말을 듣는다.":
            $ j_para -= 2
            $ a_para -= 2

            show a talk at center with dissolve
            a "그래, 혼자 사는 세상이지. 우리가 혼자 외롭게 산 그 시간동안 우리와 함께 있어준 사람이 있었나?"
            a "세상은 외로운 법이지. 누군가를 만나 잠깐의 따뜻함을 느낄 수는 있어도, 이걸 봐. 우리 모두 결국 혼자가 되었잖아."
            a "세상은 외로운 우리를 돌봐주지 않아, 눈길 한 번 주지 않는다고."
            a "결국 우리는 외롭게 살다, 아무에게도 기억되지 못하고 잊혀진 채 사라지는거야."
            a "어차피 우리는 모두 혼자라고, 각자 살 길을 찾아야하는거지."

            "그 때, J가 눈물을 흘리며 돌아왔다."

            show j at right with moveinright
            j "카슈가... 카슈가 나를 살리려다 죽었어..."
            j "눈보라가 불어서 내가 절벽으로 떨어질 뻔했는데... 카슈가 나를 살리고 절벽 아래로 떨어졌어... 카슈..."

            jump j_room_3 #4
