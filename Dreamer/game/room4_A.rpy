#A의 방, 흑막 공개 할 수도 있고, 여튼 네 번째 방.
init:
    image bg_dreamers = "aroom/bg_dreamers.png"
    image bg_vip = "aroom/bg_vip.png"
    image bg_vip2 = "aroom/bg_vip2.png"
    image bg_viphole = "aroom/bg_viphole.png"
    image bg_vip2hole = "aroom/bg_vip2hole.png"
    image bg_hospital = "aroom/bg_hospital.png"
    image bg_hospital2 = "aroom/bg_hospital2.png"
    image bg_hospitalch = "aroom/bg_hospitalch.png"
    image bg_light = "aroom/bg_light.png"
    image bg_chpaint = "aroom/bg_chpaint.png"
    image hole = "aroom/hole.png"


label a_room_start :
    scene white with dissolve
    play music "audio/A_room.mp3" fadeout 1
    "소독약 냄새가 난다."
    "뭔가...기계음도 들리는데..."
    "이제 방이 얼마 남지 않았다는 게 느껴진다."
    "왠지 이 방을 끝으로 열쇠를 잡을 수 있을 거라는 확신이 들어."
    "열쇠를 잡고 이 곳을 나가면... 모두가 곁에 있는 채로 현실에서 깨어날까..?"

    scene bg_dreamers with dissolve

    "아무 말 하지 않고 눈만 마주 보더라도 우리가 해냈다는 걸 알 수 있겠지?"
    "상상만 해도 가슴이 벅차다. 어쩌면 앞으로 계속 이들과 연락을 주고 받으면 살 수도..."
    "생과 사를 함께 한 친구가 생긴 건가.."
    "어쨌거나 최선을 다 해야지. 조금만 더 하면 이곳을 나갈 수 있어!"

    scene white with dissolve

    show j normal at centerleft with dissolve
    j "A, 너의 공간이야?"
    show a point at right with dissolve
    a "....그런 것 같아."
    show t serious at centerright with dissolve
    t "온통 하얗네요..."
    t "어디서 아이가 웃는 소리가 들리는 것 같은데..."
    show s talk at left with dissolve
    s "병원 냄새인가?"
    s "..길이 있는 건가? 그냥 앞으로 가면 되려나?"
    j standup "일단 앞으로 가보자."
    j  "어? 저게 뭐지?"

    scene bg_chpaint with dissolve
    show t serious at centerright with dissolve
    t "벽인가요?"
    t talk "더 이상 나아갈 수가 없어요. 무슨 막 같은 게 있어요."
    show j normal at centerleft with dissolve
    j "겉보기엔 아이 그림인 것 같은데..."
    j lonely "이익..밀리지가 않아."
    show s talk at left with dissolve
    s "반대편에서 같은 힘으로 밀고 있는 것 같아."
    j "T, 혹시 나이프 있어요?"
    t "네 있어요. 찢어 봐야겠죠?"
    show a talk at right with dissolve
    a "안돼. 무의 공간에 나타난 것을 훼손하면 큰 화를 입을 수도 있어."
    j "우리에게 남은 시간이 별로 없어. 빨리 여길 나가지 않으면 더 큰 화를 입을 걸?"
    a "이곳의 규칙은 내가 더 잘 알아. 자칫 잘못하다 탈출은 커녕 목숨이 위험해질 수 있다고."
    j "아무것도 안 하다가 당하느니 차라리 뭐라도 하는 게 좋겠지. S, 어떻게 할거야?"
    a "내 말을 들어야 해. 신중할 필요가 있어."

    "어떻게 할까...?"

    menu:
        "다른 방법을 찾는다.":
            s "A말대로 조심해서 나쁠 건 없을 것 같아. 뒤로 다시 가보면 다른 길이 보이지 않을까?"
            j worry "정 그렇다면 알겠어. 하지만 그래도 길이 보이지 않으면 나는 찢어야 한다고 생각해."
            s "그래, 조금만 더 다른 길을 찾아보자."
            j "나는 저쪽으로 한 번 가볼게."
            hide j with moveoutright
            t "저는 저 막 근처를 다시 둘러볼게요."
            hide t with moveoutleft
            s "좋아요. 다들 너무 멀리 가진 말고!"

            scene white with dissolve

            "길이 어디에 있을까..."
            "아무래도 A가 신경 쓰인다. 가서 말을 걸어볼까? 한시가 급하기는 한데..."

            menu:
                "A에게 말을 건다.":
                    $ a_para += 2
                    show s talk at centerleft with dissolve
                    s "A, 아까 그 그림말이야… 아무래도 조금 마음에 걸려서..."
                    show a talk at centerright with dissolve
                    a "뭐가?"
                    s surprise "아니 그냥, 뭔가 사연이 있는 것 같아서 마음에 걸리네.."
                    s "A, 혹시 일전에 말한 가족과 관련이 있는 거야? 아 물론 말하기 어려우면 안 해도 좋아."
                    a "누군가에게 가족 이야기를 한 적이 없어서..."
                    a anxious "...아까 그 그림, 내 아이가 그렸던 그림이야."
                    s "아이가 있었어?"
                    a "아주 오랫동안 앓다가 떠났어."
                    s "아..."
                    a "아이가 나한테 준 마지막 생일 선물이 그 그림이었어."
                    s normal "..."
                    a talk "아까 그 그림을 찢지 말자고 한 것도 사실.. 마음이 너무 아파서 그랬어. 너무 오래 잊고 산 것 같아서 더...망설여졌지."
                    s talk "그런 일이 있었구나..."
                    a "물론 무의 공간에 속한 것을 훼손하면 위험하다는 것도 사실이야. 이런 무의 공간에서는 더욱 조심해야한다고 들었거든."
                    a "내가 너무 소극적이었다면 미안해. 아이에 대한 기억이 막 몰려오니까 생각보다 힘이 들어서 그래..."
                    s "아니야, 충분히 이해해. 다른 사람들에게도 얘기하면 이해해 줄 거야."
                    a "그럴까?"

                    $ a_talk_c = True

                    jump a_room_1

                "단서를 찾는 데에 집중한다.":
                    "아니야, 단서를 찾는 게 중요하지. 집중하자, S. 여기를 나가야 해."

                    jump a_room_1

        "막을 찢는다.":
            scene bg_chpaint with vpunch
            "{i}부욱-{/i}" (what_color = "#B42020", what_size = 24)

            show a anxious at right with dissolve
            a "..@#..$!.." (what_size = 20)

            "A…아까부터 혼잣말하고 있는 건가…?"

            scene white with dissolve

            show j lonely at centerright with dissolve
            j "아무래도 A가 조금 이상해."
            show s talk at left with dissolve
            s "A가?"
            j "여기, A의 기억 같은데 조금 이상하지 않아? 아까부터 말도 없고. 뭘 나서서 하려고 들지도 않아."
            j "그리고 무엇보다도, 막을 찢었는데 아무 일도 일어나지 않았잖아."
            j "이곳을 나가려면 기억의 주인이 어떤 단서라도 이야기해줘야 할 텐데... 도대체 왜 그러는 거지?"
            show t talk at right with dissolve
            t "그러고보니 이상하긴 하네요..."
            s normal "음..."

            "A에게 직접 물어봐야 하나? 조금 애매한데...그냥 생각할 시간을 좀 주는게 좋을까.."

            menu:
                "수긍하며 A를 지켜보기로 한다.":
                    s talk "조금 지켜보자. 조금 이상한 면이 있는 건 나도 공감해."
                    j worry "아무튼 조심할 필요가 있겠어. 넋 놓고 있다가 뒤통수 맞기 전에."
                    s "우리 각자 길을 좀 찾아볼까?"
                    t "좋아요. 저는 저 쪽을 가볼게요."
                    hide t with moveoutright
                    j "저는 이쪽. 조심해요 다들. 뭐가 보이면 말하고!"
                    hide j with moveoutleft
                    s "알았어."

                    jump a_room_1

                "A에게 가서 말을 건다.":
                    $ a_para += 2

                    s talk "내가 A한테 한번 물어볼게. 기다려봐."
                    j worry "글쎄...물어보는 게 정답인지는 잘 모르겠다. 아무튼 조심할 필요가 있겠어. 넋 놓고 있다가 뒤통수 맞기 전에."
                    s "일단 각자 길을 좀 찾아볼까?"
                    t "좋아요. 저는 저 쪽을 가볼게요."
                    hide t with moveoutright
                    j "저는 이쪽. 조심해요 다들. 뭐가 보이면 말하고!"
                    hide j with moveoutleft
                    s "알았어."

                    "일단 A에게 가봐야겠다."
                    show a normal at right with dissolve
                    "아, 저기 있네."

                    show s talk at centerleft with move
                    s "A!"
                    s "A, 아까 그 그림말이야… 아무래도 조금 마음에 걸려서..."
                    a talk "뭐가?"
                    s surprise "아니 그냥, 뭔가 사연이 있는 것 같아서 마음에 걸리네..."
                    s "A, 혹시 일전에 말한 가족과 관련이 있는 거야? 아 물론 말하기 어려우면 안 해도 좋아."
                    a "누군가에게 가족 이야기를 한 적이 없어서..."
                    a anxious "...아까 그 그림, 내 아이가 그렸던 그림이야."
                    s "아이가 있었어?"
                    a "아주 오랫동안 앓다가 떠났어."
                    s "아..."
                    a "아이가 나한테 준 마지막 생일 선물이 그 그림이었어."
                    s normal "..."
                    a talk "아까 그 그림을 찢지 말자고 한 것도 사실.. 마음이 너무 아파서 그랬어. 너무 오래 잊고 산 것 같아서 더...망설여졌지."
                    s talk "그런 일이 있었구나..."
                    a anxious "물론 무의 공간에 속한 것을 훼손하면 위험하다는 것도 사실이야. 이런 무의 공간에서는 더욱 조심해야한다고 들었거든."
                    a talk "내가 너무 소극적이었다면 미안해. 아이에 대한 기억이 막 몰려오니까 생각보다 힘이 들어서 그래..."
                    s "아니야, 충분히 이해해. 다른 사람들에게도 얘기하면 이해해 줄 거야."
                    a "그럴까?"

                    $ a_talk_c = True

                    jump a_room_1

label a_room_1:
    j "여기! 여기로 와 봐!"

    "어? 뭔가 찾았나?"

    hide s with moveoutleft
    hide a with moveoutleft

    show hole:
        xalign 0.5
        yalign 0.5
    with dissolve

    show j worry at left with dissolve
    j "구멍이야."
    show t serious at centerleft with dissolve
    t "안에 뭐가 있는지 전혀 보이지 않네요."
    j "조금 위험할 것 같은데..."
    show a talk at right with dissolve
    a "이곳에 들어가면 단서가 있을 거야."
    j "이 구멍에?"
    a "그래. 내가 이전에 이곳에 왔을 때도 구멍에서 단서를 찾았어. 물론 그때와 같은 구멍이라고 할 수는 없지만."
    t "너무 위험하지 않을까요..?"
    a "내 방이니 내가 앞장 설게. 따라와."
    j lonely "잠깐..! 너무 성급하게 결정하는 거 아니야?"
    hide a with dissolve
    show s surprise:
        xzoom -1
        xalign 0.8
        yalign 1.0
    with move
    s "A!"
    j "벌써 들어갔네."
    t talk "따라 가야겠죠..?"
    a "들어와!! 괜찮아!"
    s talk "괜찮다고 하니... 들어갈까요?"
    t "네, 다음에 제가 갈게요. 잠시만요."
    hide t with dissolve
    s "J, 따라 들어와. 괜찮을 거야."
    hide s with dissolve
    j "알았어."

    scene black with dissolve
    pause .5
    scene bg_hospital with dissolve

    show j lonely at centerright with dissolve
    j "여긴..."
    show a talk:
        xzoom -1
        xalign 0.0
        yalign 1.0
    with dissolve
    a "병원이야."
    show s talk at centerleft with dissolve
    s "아까 맡은 소독약 냄새가 여기에서 비롯된 건가..?"
    a "밖으로 향하는 문이 나올 수도 있으니 찾아보자고."
    j "좋아. 병실 하나하나 살펴봐야겠네."
    show t talk at right with dissolve
    t "병원... 누군가 아팠던 건가요...?"

    if a_talk_c == True :
        "아이가 있었던 병원인가..?"

    a "아내가 많이 고생했었지."
    j worry "가족이 있었다는 게, 결혼을 했다는 말이었어?"
    a "고생만 하다가 떠났어."
    t serious "아프셨던 건가요..?"
    a "아마 그랬을 수도..."
    a "어쩌면 어디서 잘 살고 있을 수도 있고."
    j "떠났다는 게.."
    a "나와 같이 있는 것에 아마 질려버렸을 거야. 그 사람한텐 정말 악연이 따로 없었지. 그래서 떠났을 거야."
    t "..."
    a "집 앞에 갔다 온 사이에 사라져 있었어."
    a "그 날 아침까진 정말 괜찮아 보였는데."
    j "붙잡지는 않은 거야?"
    a anxious "그 이후로 굳이 찾지는 않았어. 그 사람, 전화번호도 바꾸지 않은 것 같았지만... 차라리 떠난 게 다행이라고 생각했을 거야 아마."

    if a_talk_c == True :
        "아이에 대해서는 아무 말도 하지 않네..."
        "아마 아내분이 떠난 것도 아이와 관련이 있겠지..."

    a "자꾸 쓸데없는 얘기를 하게 되네. 문이나 찾자고."
    j "나는 저 앞의 병실에 가볼게."

    scene bg_hospital2 with dissolve

    show a talk at right with dissolve
    a "잠깐, 이 병실..."
    show j normal at centerright with dissolve
    j "뭐 찾았어?"
    a "아니 그건 아닌데.."
    show t talk at center with dissolve
    t "A씨?"
    a anxious "여기 맞는 것 같아...@#..$!.." (what_size = 20)
    show s talk at left with dissolve
    s "A, 너와 관련이 있는 곳이야?"
    a "탁자 위치랑 창문 위치도 똑같고... 그리고 저 작은 티비도..@#.." (what_size = 20)
    s surprise "아무래도 A랑 관련이 있는 병실인가봐."
    j lonely "A, 네 마음 충분히 이해하지만 우린 시간이 없잖아. 여긴 문이 없는 것 같으니 일단은 나가자."
    show a anxious:
        linear 1 xzoom -1
    a "먼지도 여전하네..."
    t serious "A씨, 우리 말이 안 들리는 것 같아요."
    j "일단 우리라도 나가자."
    t "저 방에 들어가 봐요."

    scene bg_vip
    show j normal at center with dissolve
    j "여기는 VIP룸이었나.. 굉장히 크네"
    show s talk at left with dissolve
    s "저 구석에 또 공간이 있어."
    show t serious at centerleft with dissolve
    t "어..?"
    j "왜 그래요?"
    t "바닥이 조금 이ㅅ..{b}아아아악!{/b}"
    scene bg_viphole with vpunch
    show j normal at center
    show s talk at left

    s surprise "T씨!!!"
    j worry "S, 도와줘!"
    s "다른 한 팔 잡았어 끌어올려!"
    show t serious at centerleft with dissolve
    t "으윽"
    j relief "후아.."
    s "휴..."
    j "저거, 구멍이지?"
    s "갑자기 생긴 거 같은데"
    t "후우...."
    s talk "T, 괜찮아요..?"
    t talk "처음엔 없었는데... 갑자기 바닥이 울렁이다가.."
    j worry "여기 너무 꺼림칙해. 아무래도..."
    show a anxious at right with moveinright
    a "무슨 일이야?"
    s "갑자기 싱크홀이 생겼어. T가 그 안으로 빠질 뻔했고."
    j lonely "이거 종종 있는 일이야? 너무 위험하지 않아?"
    a "가끔 생기는 일이야. 나도 듣기만 했지 보는 건 처음이고."
    t serious "하지만 지금 생겼다는 건.. 다음에도 충분히 또 생길 수 있다는 거 아닌가요?"
    a "드문 일이야. 그리고 설령 또 생길 수 있다고 하더라도 위험을 감수해야하지 않겠어?"
    j worry "그렇긴 하지만.."
    a "분명 이곳 어딘 가에 문이 있을 거야. 일단 이 병실에는 없는 것 같으니 나가자."
    t "다리에 힘이 풀렸어요.."
    s "제가 부축해 줄게요. 일단 일어나봐요."
    j "느낌이 안 좋아..."
    j "이 쪽 아직 안 가봤지?"
    s "응 거기 가보자."

    scene bg_hospital with dissolve

    show j lonely at centerleft with dissolve
    j "T, 괜찮아요?"
    show t talk at left with dissolve
    t "네 다리가 좀 후들거리긴 하지만... 근데 A씨는 어디갔죠?"
    show s surprise at center with dissolve
    s "아?"
    j "또 아까 그 병실에 들어간 모양인데..?"
    j "자기가 단서를 더 찾자고 해놓고선 저 방에 미련을 못 버리네."
    t "그 마음이 이해가 되긴 해요.."
    j worry "뭐 나도 이해를 못하는 건 아니야. 그래도 지금은 나가는 문을 찾는게 급선무니까.."

    "신경 쓰이네... A한테 가봐야 하나.."
    if a_talk_c == True :
        "아까 아이에 대한 이야기도 그렇고.. 아내 얘기도 그렇고 사연이 많아 보이는데..."
    "일단 달래서 같이 단서를 찾자고 설득해볼까..?"

    j "우리끼리라도 열심히 찾자고 일단."

    "어쩌지.. 그냥 내버려 둬야하나.."

    menu:
        "A에게 간다.":
            show s talk:
                xzoom -1
            with dissolve
            s "나는 A에게 가볼게."
            j normal "그래. 설득해서 데려와."

            scene bg_hospital2 with dissolve
            show s talk at centerleft with moveinleft
            s "A!"
            show a talk:
                xzoom -1
                xalign 0.75
                yalign 1.0
            with dissolve
            a "금방 갈게. 조금만 기다려."
            s "재촉하려던 건 아니야.. 그냥 괜찮나 해서."
            show a talk:
                xzoom 1
            with dissolve
            a "뭐가?"
            s "이 방, 너에게 특별해서 여기에 계속 있는 거 아니야?"
            a "그래. 특별하지.."
            s "얘기 들어줄 상대가 필요해?"

            if a_para <= 0:
                a anxious "아니, 딱히 말하고 싶지는 않아. 그냥 시간이 필요할 뿐이야."
                s normal "그래.."
                a "나도 알아, 이럴 시간 없다는 거."
                s talk "A.."
                a "곧 갈 테니까 나가줘."
                s "그래..."
                "{b}으아아아악!!{/b}" (what_color = "#f00", what_size = 20)
                s surprise "??? 무슨 일이지??"
                a "설마 또.."
                s "가보자!"
                #발자국 sound
                scene black with dissolve
                pause .5
                jump a_room_debug

            else:
                a anxious "..."
                s "말하면 조금 속이 시원해질 거야."
                a talk "나는 이 공간에 몇 번이고 왔었어."
                s surprise "아.. 이 얼음성에 여러 번 왔었다고 했었지..?"
                a "내 공간에 올때마다 들었던 생각은.."
                a "혹시 내가 여기서 내 아내를 다시 볼 수 있지 않을까? 하는 거였어."
                a "그렇게 보내주고 난 후에도 마음 한 편에는"
                a "다시 오지 않을까? 그 날처럼 집 앞에 갔다 온 그 잠깐 새에 돌아와 있지 않을까? 생각했었어."
                s normal "..."
                a "그런 말도 안되는 기대처럼.. 나는 여기서 혹시 내 아내를 볼 수 있지 않을까 생각해.."
                s talk "이전에는 혹시.."
                a "이 공간에서 본 적이 있냐고? 아니.."
                a "하지만 오늘은 정말 달라. 오늘은 정말 내 아내를 볼 수 있을 것 같아."
                s "a, 하지만.."
                a "확신할 수 있어. 오늘은 달라. 내가 원래 이렇게까지 멍청하게 지난 일에 집착하고 그런 부류가 아닌데..
                근데 오늘은 정말 달라."
                a "오늘은... 다시 볼 수 있을 것 같아. 그녀가 여기에 있어."
                a "분명해.."
                s normal "그래, 그럼..."
                "{b}으아아아악!!{/b}" (what_color = "#f00", what_size = 20)
                s surprise "??? 무슨 일이지??"
                a "설마 또.."
                s "가보자!"
                #발자국 sound
                scene black with dissolve
                pause .5
                jump a_room_debug


        "단서를 찾는 것에 집중한다.":
            show s talk:
                xzoom -1
            with dissolve
            s "나는 이쪽을 볼게."
            j "알았어."

            scene bg_vip2 with dissolve
            show t talk at center with dissolve
            t "이곳도 상당히 크기가 큰 병실이네요. 분명 돈이 많은 이들이나 입원했을 법한..."
            show s surprise at left with dissolve
            s "어?"
            show j normal at centerleft with dissolve
            j "왜? 뭐 찾았어?"
            s "여기 작은 문이 있는 것 같은데?"
            t "네?"
            s talk "작지만 문인 것 같아. 이것 봐봐."
            j "문이네!"
            t "밀어봐요!"
            s normal "이이익"
            s "뭐지...? 안 열려요. 자물쇠도 없는데..?"
            t serious "같이 밀어봐요."
            j "나도 같이 밀게."
            s talk "동시에 힘주는 거야. 하나 둘 셋!"
            show s normal at left with hpunch
            show t serious at center with hpunch
            show j lonely at centerleft with hpunch
            "T, J" "으으윽"
            s talk "하, 꿈쩍도 안 하네."
            j "뭔가로 내리치면 열리지 않을까? 내가 저쪽 가서 한번 {b}으아아!!!{b}"
            scene bg_vip2hole with vpunch
            show s surprise at left
            show t serious at center
            s "J!!"
            j "잡아줘!!!"
            t "제가 잡았어요! 잠시만요..!"
            s "또 구멍이야??"
            show a anxious at right with moveinright
            a "무슨일이야??"
            t talk "또 싱크홀이 생겼어요."
            show j breathe at centerleft with dissolve
            j "헉..헉.."
            j worry "정말 간신히 피했어. 조금만 늦었어도 죽을 뻔했다고!"
            t serious "정말 위험했어요. 여기 나가는 게 어떨까요?"
            j "나가야 해요. 나가자. 이곳에만 단서가 있는 건 아닐 거 아니야?"
            j "아니, 적어도 지금 이 순간만큼은 여기를 벗어나야 할 거 같아. 불안해서 뭘 할 수가 없어."
            a talk "이곳에 분명 단서가 있어. 저번에도 그랬고, 이번에도 그럴거야."
            show j scream:
                xzoom -1
            j "구멍이 생기는게 드문 일이라며! 지금 봐, 벌써 두번이나 생겼다고! 오늘은 뭔가가 이상하다니까!"
            a "나가고 싶으면 그 정도 위험은 감수해야하지 않겠어? 나가도 위험한 건 마찬가지야. 만약 여기에 문이 있으면 어쩔거야?"
            s talk "둘 다 일단 진정해."
            show j lonely:
                xzoom -1
            j "진정할 수가 없어. 죽을 뻔했다니까 S? 여기는 너무 불안정해. 나가야 해."
            a "이곳에 분명 나가는 문이 있어. 앞으론 조금 더 조심하면서 다니면 돼."
            j "T, 어떻게 생각해요?"
            t "저도 여기에 더 이상 머물 용기가 안나요. 우리 일단 나가보는게.."
            a "S, 너도 나가고 싶어?"
            s surprise "나?"

            "어쩌지..?"

            "A가 이곳에 몇 번 와봤다니까 A 말대로 여기서 단서를 찾는 게 맞는 것일 수도 있고.."
            "하지만 너무 위험해 보이긴 하는데.. 구멍에 빠지면 끝인 거잖아.. 어쩌지..."

            jump a_room_2


label a_room_2:
    menu:
        "A의 말대로 머물자고 한다.":
            $ a_para += 1
            s talk "그래도 이 방에 와 본 사람 말을 듣는 게 좋지 않을까..?"
            s "나가도 여기보다 안전하다는 보장이 없기도 하고.."
            a talk "맞아. 원래 이 공간은 불안정해. 아마 밖의 상황도 크게 다르지 않을 거야."
            j "일단 나가고 다시 생각해 보는 것도 괜찮지 않아?"
            uc "부우우우웅 부웅"
            a anxious "...!"
            t talk "어..? 잠깐만 이거 아이 목소리 아닌가요?"
            j lonely "뭐지..? 여기 사람이 있었나?"
            s angry "가보자!"
            j worry "하지만..!"
            s "뭔가 단서를 알려줄 수도 있잖아!"
            t "이쪽 방향이에요."
            hide t with moveoutleft

            scene bg_hospitalch with dissolve
            show j normal at centerright with dissolve
            j "어린이 병동인가봐. 온통 분홍색이네."
            uc "우우웅~"
            show s talk:
                xzoom -1
                xalign 0.5
                yalign 1.0
            with dissolve
            s "저쪽이다."

            show s talk at centerleft with move

            show t talk at right with dissolve
            t "잠깐, A씨가 안 보이는데요?"
            show s talk:
                xzoom 1
            s "A가?"
            show ch hospital at center with dissolve
            j "저기 아이가 보인다!"
            s "정말 있네!! 아이가 놀라지는 않겠지?"
            j "천천히 다가가자."

            jump a_room_3

        "J의 말대로 나가자고 한다.":
            $ a_para -= 1
            s talk "J가 맞는 것 같아. 너무 위험해."
            a talk "나가도 여기보다 안전하다는 보장이 있어?"
            a "원래 이 공간은 불안정해. 아마 밖의 상황도 크게 다르지 않을 거야."
            s "일단 나가고 다시 생각해 보는 것도 괜찮지 않아?"
            t talk "맞아요. 일단 나가서 확인해 보고 다시 생각해 보는 거 어때요?"

            uc "부우우우웅 부웅"
            a anxious "...!"
            t "어..? 잠깐만 이거 아이 목소리 아닌가요?"
            j lonely "뭐지..? 여기 사람이 있었나?"
            s angry "가보자!"
            j "하지만..!"
            s "나가기 전에 딱 한번만 소리가 나는 쪽으로 가보자 J. 사람이 있다면 뭔가 단서를 알려줄 수도 있을거야!"
            j worry "흠..알았어. 소득이 없으면 바로 나가자."
            s relax "좋아."
            t "이쪽 방향이에요."

            scene bg_hospital with dissolve

            show j normal at centerright with dissolve
            j "어린이 병동인가봐. 온통 분홍색이네."

            uc "우우웅~"
            show s talk:
                xzoom -1
                xalign 0.5
                yalign 1.0
            with dissolve
            s "저쪽이다."

            show s talk at centerleft with move

            show t talk at right with dissolve
            t "잠깐, A씨가 안 보이는데요?"
            show s talk:
                xzoom 1
            s "A가?"
            show ch hospital at center with dissolve
            j "저기 아이가 보인다!"
            s "정말 있네!! 아이가 놀라지는 않겠지?"
            j "천천히 다가가자."

            jump a_room_3

label a_room_3:
    scene bg_hospitalch:
        zoom 1.2
        xalign 0.5
        yalign 0.5
    with dissolve
    show ch shape_s at center
    show s normal at centerleft
    show t talk at right
    show j normal at centerright

    c "부우우우웅-"
    j worry "병원복을 입었네..아이가 너무 창백하고 작다.."
    t "딱하네요..기계도 주렁주렁 매달고 있고.. 아마 많이 아픈 아이인가 봐요.."

    if c_select == True:
        "어? 저 아이는 그 방에서 본...?"
    if a_talk_c == True:
        "저 아이가... A의 아이인가.."
    if t_check == True:
        "T가 말했던 아이 울음소리도, 이 아이 소리였을까..?"

    t serious "그런데..아이 뒤에 있는 저 검은 형체는 뭘까요..?"
    s talk "그러게요.. 저게 뭐지... 움직이는 것 같지 않아요? 조금 불안한데..."
    j "그래도 우리의 유일한 단서는 저 아이인 것 같아. 가보자. 근데 A는 어딨어?"

    "어? 방금까지 내 옆에 있었는데..?"

    j "일단 우리라도 가보자. 빨리 와!"
    t talk "안녕 꼬마야?"
    j "꼬마야 혹시 우리가 보이니?"
    c "부웅- 부우웅-"
    show ch shape_m with dissolve
    s surprise "저 검은 형체말이야.. 조금 더 커진 것 같지 않아...?"
    t normal "꼬마야?"
    c "? 안녕~ 부우우웅-"
    t "꼬마야, 이름이 뭐야?"
    c "하나만 대답해 줄 수 있어."
    t "응?"
    c "나는 딱 하나만 대답해 줄 수 있어. 그러니까 잘 골라야 해."
    s talk "무슨 뜻이지?"
    j lonely "우리가 질문을 하나만 할 수 있다는 뜻인가?"
    t talk "그런 것 같아요."
    s "하나만 물어볼 수 있다고...? 도저히 이해가.. 두개를 물으면 사라져 버린다는 건가..?"
    j "더 이상 이 공간에 대해 의문을 품는 건 무의미해."
    s "그래 그렇지.. 그럼 뭘 물어봐야 하는 거지?"
    j "당연히 이 방을 나가는 방법을 물어봐야 하지 않을까?"
    t serious "그보다 열쇠에 대한 걸 물어보는 건 어떨까요? 어쩌면 열쇠를 얻을 수 있는 더 빠른 지름길을 아이가 알려 줄 수도 있어요."
    j "이 아이도 결국 허상에 불과한데 그런 것까지는 모르지 않을까요?"
    j "대답을 얻을 수 없는 질문을 해서 기회를 날리는 것보다는 방을 나가는 방법을 물어보는게 좋을 것 같아요."
    j worry "S, 너는 어떻게 생각해?"
    t "저는 아무리 생각해도 열쇠에 대해 물어보는 게 낫다고 생각하는데..."

    show s normal at centerleft
    "어쩌지..?"

    menu:
        "방을 나가는 방법을 물어본다.":
            s talk "방을 나가는 방법에 대해서 묻는 게 좋을 것 같아요."
            t "흠... 그러죠. 어쩔 수 없네요"
            j "아이야, 혹시 이 방을 나가는 방법을 아니?"
            c "내 뒤에 있는 이 꼬물이 있잖아."
            j lonely "꼬물이?"
            c "까맣고 꼬물꼬물한 이거"
            s surprise "저 검은 형체를 말하나 봐."
            c "이게 마구마구 커진다? 이걸 피해서 저기 저 반대편으로 마구 달리면 돼."
            j "그 꼬물이가 뭔데?"
            c "아빠는 그게 종양이라고 했어. 근데 나는 그게 뭔지 잘 몰라서 꼬물이라고 해."
            s "아빠?"
            show a anxious:
                xzoom -1
                xalign 0.0
                yalign 1.0
            with moveinleft
            a "안돼!"
            j worry "A가 네 아빠라고?"

            scene bg_hospitalch with dissolve
            show ch shape_l at center
            show a anxious:
                xzoom -1
                xalign 0.0
                yalign 1.0
            show s surprise at centerleft
            show j worry at centerright
            show t serious at right
            a "그게 중요한게 아니야! 지금 저 검은 형체를 보라고. 내 아이를 집어 삼키려 하잖아!"

            "어... 언제 저게 저렇게 커졌지...? 아이 등이 거의 뒤덮이고 있는데?"

            j lonely "으아! 무슨 촉수 같은 게 막 뻗어 나와!"
            t talk "일단 몸을 피하는 게 좋겠어요!"
            a "도와줘, 내 아이가 저 형체에 잠식되면 안돼."
            j "일단 몸을 피해야 해. 우리까지 먹히겠어!"
            a "내가 어떻게 내 아이를 버리고 도망칠 수 있겠어?"
            t "아이는 허상에 불과하잖아요. 어서 도망가요!"
            hide t with moveoutright

            show j worry at right with move
            j worry "S 뭐해! 빨리 뛰어! 저 괴물에게 잡아먹히겠어!"
            a help "도와줘, 제발. 내 아이야. 내 아이가.. 내 아이가 저것 때문에 얼마나 아파했는데.."
            a "또 다시 그런 일이 있어서는 안돼. 다시 이 병에게 아이를 빼앗길 수는 없어 제발 도와줘 S!!!"
            show s surprise:
                xzoom -1
                xalign 0.25
                yalign 1.0
            with dissolve
            s "하지만.. 저 아이는 허상이잖아!"
            a "내 아이는 허상이 아니야. 내 말 믿어줘. 여기 있는 모든 것은 다 허상이어도 내 아이는 아니야!"
            s "무슨 소리야?"
            a "억지 부리는 것처럼 들릴 거 알아. 내가 다 설명해줄게 지금은 제발 도와줘 다시 아이를 빼앗길 순 없어!"
            j "아까 갑자기 사라진 것도 그렇고... 아무래도 A가 이상해."
            j "내가 알던 사람이 아닌 것 같아.. 더 이상 A의 말을 듣지 말고 뛰어 S!!"
            a "아이가 아파하는 모습을 또 다시 볼 용기가 안 나서 그랬어! 도와줘 제발! 아이가 힘들어하잖아!!"

            "도대체 어떻게 해야 하는거야...아이가 허상이 아니라는 A의 말은 또 뭐고... 도와주다 죽는 거 아냐...?"

            a "이 얼음성에는 비밀이 있어!!! 제발 나를 도와줘! 그럼 말해줄게!!!"
            j "S!!"

            menu:
                "A를 돕는다.":
                    jump a_room_end_a

                "검은 형체로부터 도망친다.":
                    jump a_room_end_evade

        "열쇠를 얻는 방법을 물어본다.":
            $ a_room_check = True
            c "그건 비밀인데"
            j lonely "이럴 줄 알았어.."
            t "아..."
            c "근데 아빠랑 같이 있잖아. 아빠한테 물어보면 되는데?"
            s surprise "아빠?"
            c "아빠가 여기 전부 다~ 만들었잖아. 아빠는 알거야. 아빠는 말할 수 있을 걸?"
            show a anxious:
                xzoom -1
                xalign 0.0
                yalign 1.0
            with moveinleft
            a "안돼!"
            j worry "A가 네 아빠라고?"
            a "그게 중요한게 아니야! 지금 저 검은 형체를 보라고. 내 아이를 집어 삼키려 하잖아!"

            scene bg_hospitalch with dissolve
            show ch shape_l at center
            show a anxious:
                xzoom -1
                xalign 0.0
                yalign 1.0
            show s surprise at centerleft
            show j worry at centerright
            show t serious at right
            "어... 언제 저게 저렇게 커졌지...? 아이 등이 거의 뒤덮이고 있는데?"

            j lonely "으아! 무슨 촉수 같은 게 막 뻗어 나와!"
            t talk "일단 몸을 피하는 게 좋겠어요!"
            a "도와줘, 내 아이가 저 형체에 잠식되면 안돼."
            j "일단 몸을 피해야 해. 우리까지 먹히겠어!"
            a "내가 어떻게 내 아이를 버리고 도망칠 수 있겠어?"
            t "아이는 허상에 불과하잖아요. 어서 도망가요!"
            hide t with moveoutright

            show j worry at right with move
            j "S 뭐해! 빨리 뛰어! 저 괴물에게 잡아먹히겠어!"
            a help "도와줘, 제발. 내 아이야. 내 아이가.. 내 아이가 저것 때문에 얼마나 아파했는데.."
            a "또 다시 그런 일이 있어서는 안돼."
            a "다시 이 병에게 아이를 빼앗길 수는 없어 제발 도와줘 S!!!"
            show s surprise:
                xzoom -1
                xalign 0.25
                yalign 1.0
            with dissolve
            s "하지만.. 저 아이는 허상이잖아!"
            a "내 아이는 허상이 아니야. 내 말 믿어줘. 여기 있는 모든 것은 다 허상이어도 내 아이는 아니야!"
            s "무슨 소리야?"
            a "억지 부리는 것처럼 들릴 거 알아. 내가 다 설명해줄게 지금은 제발 도와줘 다시 아이를 빼앗길 순 없어!"
            j "아까 A가 사라진 것도 이상하지 않아? S, 더 이상 A의 말 듣지 말고 어서 뛰어!!"
            a "아이가 아파하는 모습을 또 다시 볼 용기가 안 나서 그랬어! 도와줘 제발! 아이가 힘들어하잖아!!"

            "도대체 어떻게 해야 하는거야...아이가 허상이 아니라는 A의 말은 또 뭐고... 도와주다 죽는 거 아냐...?"

            a "아이가 밝혔잖아. 내가 이 세계를 설계한 사람이라고..내 말을 들어줘!!"
            j "S!!"

            menu:
                "A를 돕는다.":
                    jump a_room_end_a

                "검은 형체로부터 도망친다.":
                    jump a_room_end_evade


label a_room_end_a:
    show s surprise:
        xzoom 1
    s "어...어떻게 도와줘야 하는 거야?!"
    a "저걸 떼어 내야 해! 거기 아이 팔을 잡고 잡아당겨!"

    scene bg_shape with dissolve
    show ch shape_l at center
    show s surprise at centerleft
    show a help:
        xzoom -1
        xalign 0.0
        yalign 1.0
    show j worry at right

    s "너무 커졌어, 무리야!"
    a "이익"
    s "안 떨어져, 안 떨어져!!! 빠져나올 수가 없어!! A!!! 도와줘!!!"
    a "아아아아아악!!"
    j "S!!!! A!!!"

    scene black with dissolve

    "..."

    "먹혔다. 완전히 먹힌 게 분명해."
    "앞이 보이지 않는다."
    "뭐지..? 끝인가...?"

    if a_para >= 2:
        a "S, ㅈ.."
        s "어..?"
        a "S, 정신차려."

        "뭐야, 아무 것도 보이지 않아."

        s "나 아무 것도 안 보여. A, 어디에 있는 거야?"
        s "그 괴물은 어떻게 됐어? 아이는? A 이게 무슨 일이야, 설명해줘."
        s "A..?"
        a "괴물도 아이도 허상이 아니야. 내 아이와 관련된 그 모든 것들이 이 안에서는 허상이 아니니까."
        s "내가 죽었다는 거야..?"
        a "아니, 그건 아니야. 여기서는 글쎄.. 죽는다는 게 그 어떤 의미도 지니지 못할 테니까."
        s "어디에 있는 거야. 일단 내 눈 앞에 나와 봐. 네가 보이지 않아..!"
        a "도와줘서 고마워. 사실 조금 놀랐어. 덕분에 아이를... 아니 더 정확히 말하자면 조각난 아이의 의식 중 일부를 지킬 수 있었어."

        "무슨 말이야 도대체.."

        a "이 얼음성의 비밀에 대해서 이야기해준다고 했지?"
        s "..."
        a "이 세계는 오로지 그 아이를 위해 만들어졌어."
        a "그 아이가 이 세계 속에서 안전하게 살아가기 위해서 바로 너희 같은 사람들이 이곳에 머물러야 해."
        s "뭐?"
        a "그래야 이 세계가 무너지지 않아."
        s "너는 그걸 어떻게 다 아는 거야?"
        a "{b}내가 만들었으니까.{/b}"
        s "..뭐?"
        a "밀실도.. 그리고 얼음성도..."
        a "이 꿈의 세계를 전부 내가 만들었으니까."
        s "그러니까... 그러니까 네 말은 나 같은 사람이 여기에 머물러야 이 세계가 유지될 수 있다는 거야?"
        a "그래. 너희가 떠나면.. 이 꿈의 세계와 함께 내 아이도 사라질 거야."
        s "하지만...!"
        a "그래, 너희는 떠나고 싶겠지. 아니 떠나야하겠지."
        a "..."
        a "보내줄게."
        s "...?"
        a "어차피 이 세계는 붕괴 중이야. 나는... 아이 곁에서 마지막을 지키겠어."
        s "A.."
        a "또 다시 아이의 마지막을..."
        s "A 잠깐만, 천천히 다시 이야기를..!"
        a "시간이 없어. 이건 그냥... 그간 나를 신경 써준 거에 대한 답례라고 생각해."
        s "그러지 말고, A 내 말을.."
        a "S."
        a "열쇠를 잡을 수 있는 건..."
        s "?"
        a "{b}단 한사람{/b}이라는 걸 명심해."
        s "ㅁ.. 뭐라고...?"
        a "단 한사람만 열쇠를 쥐고 이 곳을 빠져나갈 수 있는 거야."
        s "그게 무슨..!"
        a "그럼 잘 있어, 친구."
        s "A, A!!"

        scene bg_light with dissolve

        "몽롱하다. 휘발유 냄새가 나는 것 같다."
        "주황 불빛도 보이고, 아이 웃음소리도..."
        "아이 웃음소리..."
        "A는..."

        scene bg_hospital with dissolve

        show j worry at centerleft with dissolve
        j "..신 차려..!!"
        show s normal:
            xzoom -1
            xalign 0.5
            yalign 1.0
        with dissolve
        s "...?"
        j "S!!! 정신 차려!!"
        j "눈 좀 떠봐!!!"
        s "J..."
        j relief "어떻게 된 거야? 아니다. 일단 여길 나가자! 문을 찾았어. 얼른 일어나!"
        s talk "나 어떻게.. 내가 어떻게.."
        show t serious at left with dissolve
        t "어서 가요!"
        j worry "아무래도 S를 부축해야겠어요."
        t "네, 일단 갑시다."
        scene black with dissolve
        pause .5

        jump climax_start_good_a

    else:
        jump end_4_bad

label a_room_end_evade:
    s surprise "미안해..! 그건 허상이잖아. 안되겠어!"
    a help "허상이 아니야!! 제발 S!"
    hide j with moveoutright
    show s talk:
        xzoom -1
        xalign 1.0
        yalign 1.0
    with move
    s "A, 너도 뛰어!!"
    hide s with moveoutright
    show a help at centerleft with move
    a "아악 - "
    j "S 이쪽이야 어서!!"
    t "저 멀리 문이 보여요!"

    "잠깐... 잠깐만 뒤돌아 보자."

    scene bg_shape with vpunch

    "...! A도 아이도 안보여.. 저 형체에게 먹힌 건가..?"

    j "헉헉 S 어서 뛰어!!"
    t "곧 문 앞이에요! 어서!"
    scene bg_hospital with dissolve
    show s sit at centerleft
    show j breathe at centerright
    show t serious at center
    "S, J, T" "허억..헉.."
    j lonely "나가자..."
    if a_room_check == True:
        s talk "어떻게 된 거지..? A..."
        j "이 세계를 설계했다는 건.."
        t talk "우리를 여기에 가둔 사람이라는 걸까요?"
        s "그런데...만약 A의 말이 진짜라면 어떻게 해..?"
        s "만약에 아이가 허상이 아니라면.. A가 이 세계를 설계했다면 그 말이 진실일 수도 있잖아..."
        j "...일단 이곳을 벗어나야 해. 내가 뭐랬어, A가 이상하다고 했잖아. 분명 우리를 쫓아 올거야."
        t "빨리 나가요!"
        show a help:
            xalign 1.2
            yalign 1.0
        with moveinright
        a "기다려!!!"
        s surprise "A? 어떻게..!"
        j worry "어디서 소리가 들리는 거지?"
        s "저 멀리, A가 보여."
        t "잠깐, 저 검은 형체가 A씨를 완전히 감싸고 있어요..!"
        s "공간이 완전히 뒤틀렸어. 무너지고 있나 봐..!"
        a "너희 때문에... 너희 때문에 내 아이의 일부가 소멸됐어..! 너희가 도와주지 않아서..!!!"
        a "너희가 이 세계를 탈출해도 잘 살 것 같아?!!"
        j "갑자기 무슨..."
        a "너희는 다 죽을 날만 기다리는 인간들이야!!! 한심하기 짝이 없는 인간들이라고!"
        s "뭐..?"
        a "S!!! 네가 어떻게 이곳에 갇히게 된 줄 알아?!! 이곳은 꿈의 세계니 뭐니 하는게 아니야!!"
        a "너희는 그냥 코마에 빠져서 내 세계에 갇힌 거지!!"
        a "S!! 매일 음식물 쓰레기만 처리하다가 뺑소니 당한 네 인생으로 돌아가면 행복할 것 같아?!"
        a "네가 깨어나도 너를 반기는 건 온갖 음식물 쓰레기에 불과하다고!!! 그리고 네가 불어난 치료비를 감당할 수나 있을까?!"
        s "코마..? 음식물 쓰레기 처리..?"
        a "잘 생각해 너희들!!! 그냥 여기에 남는 게 좋을지 너희들의 그 시궁창 같은 인생으로 돌아갈지!!"
        j "A가 하는 말.. 이해가 돼..?"
        s "아니.. 아니 전혀. 내가 노인이라고...? 뺑소니..? 코마..?"
        a "아, 그리고 하나 안 알려준 게 있는데!!"
        a "열쇠 말이야, 그거 {b}단 한사람{/b}만 잡을 수 있다는 거 명심해!!"
        a "멍청하게 양보하다가는 영원히 여기에 갇히게 될 테니까!!"
        j lonely "ㅁ...뭐?"
        s "열쇠를 한 사람만 잡을 수 있다고...? 그럼 이 세계를 나갈 수 있는 게 단 한명..."
        t serious "아..."
        t "이..일단 나가요! 저 형체가 곧 저 앞까지 다다르겠어요..!!"
        hide t with moveoutleft
        s "잠깐 A가 한 말이 이해가 안돼. 열쇠는 뭐고 코마 상태라는 건 또...!"
        j "S! 나가자!!"
        hide j with moveoutleft

        scene black with dissolve

        a "멍청한 선택 말고 이 세계에 머무는 게 좋을 거야!!" (what_size = 18)
        a "너희들은 어차피 현실에서 낙오자니까!!" (what_size = 18)

        show black with vpunch

        jump climax_start_bad_a


    else:
        s talk "잠깐만... A는..."
        j lonely "안타깝지만... 어쩔 수 없었어..."
        t talk "설득하기엔 시간이 너무 촉박했어요.."
        s "만약 A의 말이 진짜라면 어떻게 해..? 만약에 아이가 허상이 아니라면.. A가 이 세계의 비밀을 알려주겠다고 한 건 또 뭐고.."
        j "A...자기 아이가 허상이 아니라는 걸 믿고 싶었겠지..."
        j "나라도 그랬을 거야..."
        j "설득할 시간이 있었더라면..."
        t "병으로 잃은 아이니까 더욱 인정하기 싫었을 거예요."
        j "일단 이 방을 벗어나자. 저 형체가 언제 다가올지 몰라."
        show a help:
            xalign 1.2
            yalign 1.0
        with moveinright
        a "기다려!!!"
        s surprise "A? 어떻게..!"
        j worry "어디서 소리가 들리는 거지?"
        s "저 멀리, A가 보여."
        t "잠깐, 저 검은 형체가 A씨를 완전히 감싸고 있어요..!"
        s "공간이 완전히 뒤틀렸어. 무너지고 있나 봐..!"
        a "너희가 이 세계를 탈출해도 잘 살 것 같아?!!"
        j "갑자기 무슨..."
        a "너희 때문에... 너희 때문에 내 아이의 일부가 소멸됐어..! 너희가 도와주지 않아서..!!!"
        a "너희는 다 죽을 날만 기다리는 인간들이야!!! 한심하기 짝이 없는 인간들이라고!"
        s "뭐..?"
        a "S!!! 네가 어떻게 이곳에 갇히게 된 줄 알아?!! 이곳은 꿈의 세계니 뭐니 하는게 아니야!!"
        a "너희는 그냥 코마에 빠져서 내 세계에 갇힌 거지!!"
        a "S!! 매일 음식물 쓰레기만 처리하다가 뺑소니 당한 네 인생으로 돌아가면 행복할 것 같아?!"
        a "네가 깨어나도 너를 반기는 건 온갖 음식물 쓰레기에 불과하다고!!! 그리고 네가 불어난 치료비를 감당할 수나 있을까?!"
        s "뺑소니를...당했어..?"
        a "잘 생각해 너희들!!! 그냥 여기에 남는 게 좋을지 너희들의 그 시궁창 같은 인생으로 돌아갈지!!"
        j "A가 하는 말...이해가 돼...?"
        s "아니...아니 전혀. 뺑소니...? 코마..?"
        a "아, 그리고 하나 안 알려준 게 있는데!!"
        a "열쇠 말이야, 그거 {b}단 한사람{/b}만 잡을 수 있다는 거 명심해!!"
        a "멍청하게 양보하다가는 영원히 여기에 갇히게 될 테니까!!"
        j "ㅁ...뭐?"
        s "열쇠를 한 사람만 잡을 수 있다고...? 그럼 이 세계를 나갈 수 있는 게 단 한명..."
        t serious "아..."
        t "이..일단 나가요! 저 형체가 곧 저 앞까지 다다르겠어요..!!"
        hide t with moveoutleft
        s "잠깐 A가 한 말이 이해가 안돼. 열쇠는 뭐고 코마 상태라는 건 또...!"
        j "S! 나가자!!"

        hide j with moveoutleft

        scene black with dissolve

        a "멍청한 선택 말고 이 세계에 머무는 게 좋을 거야!!" (what_size = 18)
        a "너희들은 어차피 현실에서 낙오자니까!!" (what_size = 18)

        show black with vpunch

        jump climax_start_bad_a

label a_room_debug:
    scene bg_vip2hole with dissolve

    show s talk at left with moveinleft
    s "J!!"
    show t talk at center with dissolve
    t "또 싱크홀이 생겼어요."
    show j breathe at centerleft with dissolve
    j "헉..헉.."
    j worry "정말 간신히 피했어. 조금만 늦었어도 죽을 뻔했다고!"
    t serious "정말 위험했어요. 여기 나가는 게 어떨까요?"
    j "나가야 해요. 나가자. 이곳에만 단서가 있는 건 아닐 거 아니야?"
    j "아니, 적어도 지금 이 순간만큼은 여기를 벗어나야 할 거 같아. 불안해서 뭘 할 수가 없어."
    show a talk at right with dissolve
    a "이곳에 분명 단서가 있어. 저번에도 그랬고, 이번에도 그럴거야."
    show j scream:
        xzoom -1
    j "구멍이 생기는게 드문 일이라며! 지금 봐, 벌써 두번이나 생겼다고! 오늘은 뭔가가 이상하다니까!"
    a "나가고 싶으면 그 정도 위험은 감수해야하지 않겠어? 나가도 위험한 건 마찬가지야. 만약 여기에 문이 있으면 어쩔거야?"
    s "둘 다 일단 진정해."
    show j lonely:
        xzoom -1
    j "진정할 수가 없어. 죽을 뻔했다니까 S? 여기는 너무 불안정해. 나가야 해."
    a "이곳에 분명 나가는 문이 있어. 앞으론 조금 더 조심하면서 다니면 돼."
    j "T, 어떻게 생각해요?"
    t "저도 여기에 더 이상 머물 용기가 안나요. 우리 일단 나가보는게.."
    a "S, 너도 나가고 싶어?"
    s surprise "나?"

    "어쩌지..?"
    "A.. 아무래도 아내를 꼭 만나고 싶어하는 눈치인데.. 아무도 못 만나고 그냥 나가버리는 건 너무..."

    if a_talk_c == True :
        "어쩌면 아이도 만날 수 있을 텐데.."
        "말을 하지는 않았지만... 아이도 정말 만나고 싶을 거야..."
    "A가 이곳에 몇 번 와봤다니까 A 말대로 여기서 단서를 찾는 게 맞는 것일 수도 있고.."
    "하지만 너무 위험해 보이긴 하는데.. 구멍에 빠지면 끝인 거잖아.. 어쩌지..."

    jump a_room_2
