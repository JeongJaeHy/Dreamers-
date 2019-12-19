#웨이터 T의 방에서 일어나는 이야기들 & 두 번째 방.
init:
    image bg_door = "troom/bg_door.png"
    image bg_hallway = "troom/bg_hallway.png"
    image bg_boxroom = "troom/bg_boxroom.png"
    image bg_a_strange = "troom/bg_a_strange.png"
    image bg_a_strange2 = "troom/bg_a_strange2.png"
    image bg_a_strange3 = "troom/bg_a_strange3.png"
    image bg_enter = "troom/bg_enter.png"
    image bg_house_in = "troom/bg_house_in.png"
    image bg_background = "troom/bg_background.png"
    image bg_fountain = "troom/bg_fountain.png"
    image bg_frozen = "troom/bg_frozen.png"

label t_room_start :
    play music "audio/T_room.mp3" fadeout 1

    scene bg_background with dissolve
    "방문을 열었다. 정원의 풍경이 펼쳐졌다."

    show j lonely at right with dissolve
    j "카슈가 없으니까 허전해."
    show s talk at left with dissolve
    s "..좋은 곳에 갔을 거야."
    j relief "뻔한 말이지만 그렇게 생각하니..왠지 위로가 되네."
    hide j
    show a normal at right with dissolve
    a "이번엔 정원이군."
    s "유럽 정원같아. 생소해."
    show j normal at center with dissolve
    j "유럽이라면 어디?"
    s "그건 모르겠어. 사실 내가 유럽을 가 봤는지도 기억이 안 나니까."

    "말을 하면서도 마음이 답답해진다."

    j "그야 그래."
    s "그런데 좀 음산하지 않아? 정원에 있는 모든 식물들이 다, 죽어있어."

    scene bg_frozen with hpunch
    "나뭇가지를 살짝 흔들자 나뭇가지를 타고 성에가 맺히기 시작했다."
    "그러니 말라 쭈그러든 초록 나뭇잎들이 우수수 떨어져내렸다."

    show a point at right with dissolve
    a "분수가 있네."

    scene bg_fountain with dissolve
    "옆을 바라보자 분수가 있었다. 날개가 달린 아기천사 석상이 있는 흔한 분수였다."
    "자세히 들여다보니 석상의 몸체는 부식되어 표면에 자잘하게 금이 가 있다."

    show j normal at left with dissolve
    j "이것도 방치된 지 오래된 것 같아. 금이 갔네."
    show a point at right with dissolve
    a "이 정도로 부식되려면 얼마나 시간이 흐른 거야."
    j "원래는 물이 나왔겠지? 이 항아리 입구에서"
    show t talk at center with dissolve
    t "맞아요. 항아리 입구에서 물이 쏟아져요."
    j "아, 여기가 T님이 일하던 곳이었군요 프랑스라고 하셨나요?"
    t "네. 로어 노르망디에 있었어요."
    a talk "이봐, 유럽이고 뭐고 다 좋은데 여기서 시간을 지체하면 안 돼. 열쇠를 찾으러 가야 하잖아."
    t "...그래요. 일단 여기서 멈춰 있지 말고 이 방을 어서 통과해요."
    hide j
    show s talk at left with dissolve
    s "어디로 가야 하지?"
    t "대저택을 통과해야 될 거에요. 저희가 방금 들어온 곳은 저택 정문이고, 저택을 통과하지 않고서는 밖으로 나갈 수 없어요."
    hide s
    show j normal at left with dissolve
    j "이렇게 큰 줄은 몰랐어요."
    t "...큰 저택이었죠."

    "T는 더 이상 말 할 것이 없다는 듯 앞서 걸어갔다. 나와 J는 T의 말이 무슨 말인지 알 수가 없어 서로를 바라보며 어깨를 으쓱했다."

    a anxious "이봐, 얼마나 더 가야 해. 이런 지독한 곳은 또 처음이네."
    t "눈으로 뒤덮인 곳도 지나왔잖아요. 산책로 십 분쯤 걷는 거라고 좋게 생각하세요."
    hide t with moveoutright

    "A는 왜인지 짜증이 난 눈치다. 발로 자갈을 차며 걸어갔다."
    hide a with moveoutright
    scene bg_house with dissolve
    "한참을 걷다 보니 대저택이 서서히 모습을 드러냈다."

    show j worry at right with dissolve
    j "집까지 가는 데만 십 오 분이라니."
    show s talk at left with dissolve
    s "집 주인은 차 타고 가겠지."
    show t talk at center with dissolve
    t "차를 타고 가면 더 빨리 갈 수 있겠죠. 그렇지만 걸어가기에도 좋은 길이에요."

    scene black with dissolve
    pause .8
    scene bg_house:
        zoom 1.5
        xalign 0.5
        yalign 0.5
    with dissolve
    "문은 낡아 이가 빠져 있거나 부식되어 있다."
    "T가 경칩이 너덜거리는 문고리를 잡으며 말한다."

    show t talk at center with dissolve
    t "원래 문을 열어주는 사람이 넷 있었어요. 지금은 없으니까, 우리가 함께 문을 밀어야 해요."

    scene bg_enter with dissolve
    "우리는 다 함께 문을 밀기 시작했다. 넷이 힘을 합치자 문이 서서히 열렸다."

    scene bg_a_strange with dissolve
    pause .5
    scene bg_a_strange2 with dissolve
    pause .5
    scene bg_a_strange3 with dissolve
    pause .5
    scene black with dissolve
    pause .8

    jump t_room_1

label t_room_1:
    scene bg_house_in with dissolve

    show j normal at centerleft with dissolve
    j "이 큰 저택을 혼자 관리했던거에요?"
    show t talk at center with dissolve
    t "그럼요. 여기 저희가 발을 딛고 서 있는 대리석 바닥부터, 천장에 걸린 샹들리에,
    저 나선형 계단과 그 뒤에 걸린 그림 액자들까지, 모든 곳을 매일매일 쓸고 닦았어요."
    show a talk at right with dissolve
    a "천성이 웨이터군."

    "밑에서 올려다보아도 샹들리에에는 먼지가 가득 쌓여 있다."

    show s talk at left with dissolve
    s "샹들리에는 어떻게 청소하죠?"
    t "긴 사다리를 이용해요. 창고에는 별별 것들이 다 있죠."
    t serious "그런데 지금은 먼지가 너무 많이 쌓였네요. 지금까지 본 저택 풍경은 정말 최악이에요. 이런 더러움은 용납할 수가 없어요."
    j worry "T..."
    t talk "기억 속에 있는 공간이 방의 형태로 펼쳐진다 해서 저도 내심 기대를 했어요. 아마 정원이 나오지 않을까, 하고요"
    t "제 인생에서 제일 행복했던 순간이 여기서 일 하던 때였거든요. 샹들리에를 닦고 테이블에 냅킨과 수저를 가지런히 정렬하고..."

    "테이블? 냅킨..? 무언가 기억날 것 같은데.."

    t "콘도가 아니라 저택이 나온 건 좋아요. 그런데 이런 모습도 편하지는 않네요."
    j "콘도?"
    a anxious "이봐, 다 환상이잖아."
    t "...이 샹들리에라도 청소하면 안 될까요?"

    menu :
        "A의 말이 맞다. T에게 환상에 잡아먹히지 말자고 이야기하자":
            s surprise "T, 슬플 수 있어요. 그렇지만 A 말대로 다 환상이에요.
            일부러 좋지 않은 모습을 보여주어 혼란에 빠트리는 거예요. 그렇게 생각하면..."
            t serious "...."
            t "..얼음성은 나쁜 곳이에요."
            s normal "..."
            t talk "샹들리에를 청소할 시간조차 주지 않네요. 맞아요. 우리에겐 열쇠가 중요하죠."

            hide t with moveoutleft
            "T는 그렇게 말하더니 앞서 걸어간다. 괜히 말을 했나..."

            j lonely "S, 어쩐지 좋지 않은 위로를 한 것 같아.." (what_size = 15)
            s surprise "그런 것 같네.. 내가 생각이 짧았어."
            a talk "아니야. 현실을 말 해 주는 것도 중요해."
            a "환상은 환상이고, 얼음성은 나쁜 곳이라기보단 어떻게 보느냐에 따라 달라지는 거울과 같지."
            j worry "S는 저택을 그런 방식으로 본 적이 없어요."
            a "모르지. 자기가 사라진 뒤로는 황량해진 저택을 바라 왔을수도 있는 거야. 그래야 자신이 쓸모가 있었다는 뜻이 되니까."

            "A의 말을 듣고 어떤 대꾸도 할 수 없었다. J도 동의한다는 듯 입을 다물고 있었다."

            j lonely "...일단 지금은 T의 기분을 풀어 주는 게 좋을 것 같아요."
            j "T!"

            hide j with moveoutleft
            "J는 T를 부르며 달려갔다. 나도 J의 뒤를 따라 달린다."
            hide s with moveoutleft

            $ a_para += 1

            jump t_room_2

        "A의 말도 맞지만, 여기서는 T의 편을 들어주자.":
            s "A, 환상이라도 슬픈 건 마찬가지에요."
            a normal "..."
            s "T, 제가 사다리를 꺼내 올게요. 같이 청소해요."
            j standup "그래요. 저도 카슈를 힘들게 보내서, 그 마음이 뭔지 알아요."
            t smile "고마워요. S, 같이 가요."
            a talk "나도 가야 하나?"
            t "두 분은 여기에 있는 게 좋을 것 같아요."

            scene bg_hallway with dissolve

            show t smile at centerright with dissolve
            t "고마워요. 선뜻 사다리를 꺼내 오겠다고 이야기를 해 주셔서."
            show s talk at centerleft with dissolve
            s "뭘요.."
            t talk "얼음성에 온 뒤로 이 저택 생각을 많이 했었어요. 얼음성 웨이터가 된 이유도 그것이었고요."
            s "저택을 떠올리며 얼음성 웨이터가 된 거라고 하셨죠?"
            t serious "그렇죠. 얼음성도 이 저택의 주인님처럼, 주인이 있다고 들었어요. 얼음성을 창조한 사람이요."
            t "그 사람이 누구인지 아무도 얼굴을 본 적은 없지만, 분명히 존재한다고 해요."
            s normal "얼음성의 주인.."
            t talk "제가 하는 또 다른 일은 그 사람들을 감시하고 얼음성 방에 계속 머물게 하는 역할이었어요 얼굴도 모르는 얼음성의 주인이 시킨 일이죠."
            s "그런 일을 시켰어요?"
            t "네. 그래서 얼음성은 저택이 될 수 없다는 걸 알았죠. 심지어 어떤 날은 아이 울음소리도 들린다니까요."
            $ t_check = True
            t "창고에 도착했네요. 제가 사다리를 꺼내올게요. 사다리가 좀 무거워서 복도부터는 함께 들어야 될 거에요."

            scene bg_house_in with dissolve
            # 샹들리에 깨끗해진 풍경
            show t smile at centerright with dissolve
            t "다들 감사해요."
            show a talk at right with dissolve
            a "사다리가 덜컹거려서, 잡아주는 데 팔이 나갈 것 같았다구."
            t "하하.."
            a "...닦아 놓으니 예쁘긴 하네."
            show j normal at centerleft with dissolve
            j "이렇게 영롱했군요."
            t "그럼 다시 가볼까요?"

            $ a_para -= 1

            jump t_room_2

label t_room_2:
    scene black with dissolve
    pause .5
    scene bg_door with dissolve

    "복도 오른쪽 끝방 쪽에 다다랐다."
    "먼지가 가득 쌓여 발을 디딜 때 마다 퍼석거리는 소리가 나지만 그럼에도 복도는 고풍스럽다."

    show t talk at center with dissolve
    t "...이 문으로 나가면 후문으로 갈 수 있어요. 어쩐지 이번 방은 쉽게 나갈 것 같네요."

    "T는 문 앞에 무릎을 꿇고 대리석 바닥 하나를 들어냈다. 그리고는 그 안에 숨겨져 있는 무언가를 꺼내는 듯 손을 넣어 휘휘 저었다."
    show t serious at center
    "T의 표정이 좋지 않아진다."

    t "...경칩이 없어요."
    show a talk at centerright with dissolve
    a "계획대로 되는 게 하나도 없네."
    t talk "원래 경칩을 여기 넣어두거든요. 그런데 왜..."
    show j normal at centerleft with dissolve
    j "경칩이라면 나무로 된 건가요?"
    t "네. 홈에 맞는 경칩을 꽂아야 문이 열리는데, 그게 없으니.."
    show s talk at left with dissolve
    s "혹시 부식됐을까요?"
    t "그렇다면 이 방에서 나가지 못해요."
    a point "다른 무언가를 넣어본다면 열릴까."
    t "아니요. 경칩 앞면에 복잡한 홈이 그려져 있어요. 정확한 문양이 있어야 열려요."

    "..문득 아까부터 불룩한 A의 주머니가 눈에 띄었다."
    "상의로 가려져있지만 눈에 띄게 불룩하다. 생각해보면 정원을 들어올 때만 해도 A는 바지 주머니에 손을 넣고 있었는데,
    이제는 주머니에 손이 들어갈 공간조차 없어 보인다."

    j lonely "경칩이 어디에 있나 조를 나눠서 찾아보는 건 어떨까요?"
    t smile "그래야 할 것 같아요."

    "누구와 함께 갈까.."
    menu:
        "A와 조를 이뤄, A와 단 둘이 있을 때 주머니에 있는 물건에 대해 직접적으로 물어본다.":

            jump t_room_3_a

        "J와 조를 이뤄, J와 단 둘이 있을 때 A의 주머니에 무언가 있어 보인다고 이야기한다.":

            jump t_room_3_j

label t_room_3_a:
    scene bg_hallway with dissolve
    "나와 A는 저택의 왼쪽 방들을 살펴보기로 했다."
    "말수가 없는 A와 단 둘이 걷는 건 어색한데, 게다가 저 불룩한 주머니까지 신경쓰인다."
    "어떻게 말을 꺼내야 할까..."

    show a point at centerright with dissolve
    a "하나씩 나눠서 탐사하자고. 나는 복도 맨 끝 방부터 훑을게."
    show s surprise at centerleft with dissolve
    s "알겠어."

    "얼떨결에 대답해버렸다."

    s "나는 바로 옆 방에 있을게."
    a "그래."

    scene bg_boxroom with dissolve

    "방을 뒤졌지만 온통 상자에 담긴 식기류밖에 없었다. 이 접시들... 상당히 비싸 보인다."
    "그런데 이런 접시들을 예전에도 많이 본 것 같은 이상한 기시감이 든다."
    "아, 부모님과의 식사.. 그 때의 접시.. 부모님이 돌아가시기 전에.."

    show a talk at right with dissolve
    a "다 했어?"
    show s talk at left with dissolve
    s "방금 막 끝났어."
    a "다음 방도 나눠서 하자."

    "A의 주머니는 여전히 불룩하다."
    show a talk:
        xzoom -1
        xalign 1.1
        yalign 1.0
    with move
    "나는 다음 방으로 들어가는 A를 따라 들어갔다."
    "이제는 물어봐야 한다.. A가 인기척을 느꼈는지 뒤를 돌아봤다."

    show a talk:
        xzoom 1
        xalign 0.9
        yalign 1.0
    with move
    a "나눠서 찾아보자니까."
    s "아니야. 그 전에 물어볼 게 있어."
    a "뭔데?"
    s "주머니에 든 거, 뭐야?"
    a "주머니?"

    "A는 불룩한 자기 주머니를 내려다보다니 웃었다."

    a "설마 이게 경칩일 거라고 생각하는거야?"
    s "그런 건 아니야."
    a "그런데 왜 물어보는거야."
    s normal "..."
    a "나를 신뢰하는 거 아니었어?"
    s talk "그래도 보여 줘. 확실히 하고 싶어."

    show a anxious:
        xalign 0.9
        yalign 1.0
    with dissolve
    "A는 침묵하다, 할 수 없다는 듯 주머니에 손을 넣어 안에 든 것을 꺼냈다."
    "경칩일까.."
    "그런데 주머니에서 나온 것은..."
    show a normal:
        xalign 0.9
        yalign 1.0
    with dissolve
    "..."
    "길쭉하게 생긴 돌이었다."

    s surprise "돌은 어디서 챙긴 거야."
    a talk "정원에서. 하나쯤 주워도 나쁠 건 없잖아."
    s "...의심해서 미안해. 하지만 확실히 해야 했어."

    "차마 너를 의심한 건 아니야, 라는 말은 할 수 없었다."

    a "나도 이해해. 그래도..."

    "A는 도둑으로 몰렸음에도 침착했다."

    a "이런 상황일수록 누군가를 믿기가 힘들지. 자꾸 이상하게 일이 꼬이잖아."

    scene bg_hallway with dissolve
    "우리는 함께 방을 탐사하다 복도로 나갔다."
    "오른쪽 방은 이미 다 탐사했지만 J와 T는 돌아올 기색이 없다."
    "결국 왼쪽 구역으로 건너가다 J와 T를 마주쳤다."

    show t serious at centerleft with dissolve
    t "오른쪽은 다 찾아봤나요?"
    show s talk:
        xzoom -1
        xalign 0.75
        yalign 1.0
    with dissolve
    s "찾아봤지만..없었어요."
    t "J와 제가 한번 더 찾아볼게요. 놓친 부분이 있을 수 있으니까..."
    s "...고마워요. 끝방부터 보시면 돼요."
    show j breathe:
        xzoom -1
        xalign 0.1
        yalign 1.0
    with moveinleft
    j "찾았다!"

    "J가 끝 방에서 뛰어나왔다."

    show j normal:
        xzoom 1
        xalign 0.1
        yalign 1.0
    with dissolve
    j "이 방에서 경칩을 찾았어! 장식용 돌들 사이에 끼어있었어."

    "J의 밝은 외침에 나는 마음이 복잡해진다. 쓸데없이 A를 의심해버렸다."

    $ a_para -= 2

    jump t_room_end

label t_room_3_j:
    scene bg_hallway with dissolve
    "나와 J는 저택의 오른쪽 방들을 살펴보기로 했다."
    "A의 불룩한 주머니는 신경쓰이는데, J에게 어떻게 말을 꺼내야 할 지 모르겠다..."

    show j normal at centerright with dissolve
    j "S,하나씩 나눠서 탐사하자고. 나는 복도 맨 끝방부터 훑을게."
    show s surprise at centerleft with dissolve
    s "알겠어."

    "얼떨결에 대답해벼렸다."

    s talk "그럼 나는 바로 옆 방에 있을게."
    j "그래. 혹시 일찍 끝나면 바로 내 방으로 와."
    s "알겠어."

    scene bg_boxroom with dissolve

    "방을 뒤졌지만 온통 상자에 담긴 식기류밖에 없었다. 이 접시들... 상당히 비싸 보인다."
    "그런데 이런 접시들을 예전에도 많이 본 것 같은 이상한 기시감이 든다."
    "아, 부모님과의 식사.. 그 때의 접시.. 부모님이 돌아가시기 전에.."

    show j normal at right with dissolve
    j "아직 덜 끝냈어?"
    show s talk:
        xzoom -1
        xalign 0.0
        yalign 1.0
    with dissolve
    s "응. 접시가 너무 많아."

    "나는 접시를 들어 보였다. J는 방 안으로 들어오더니 함께 접시를 옮기기 시작했다."

    j "정말 비싸 보인다."
    show s relax:
        xzoom 1
        xalign 0.0
        yalign 1.0
    s "그러게. 한 눈에 봐도 고급이야. 왜 내가 그렇게 생각하는지는 모르겠지만."
    j "하나쯤 슬쩍하고 싶은데." #smile

    "그래, J는 믿을 만 한 친구다. 그만큼 J와 먼저 논의하는 게 맞겠지.."

    show s talk:
        xzoom 1
        xalign 0.0
        yalign 1.0
    s "J, 할 말이 있어."
    j "뭔데?"
    s "A의 주머니가, 아까 정원 초입에서 분수를 볼 때만 해도 홀쭉했어. 안에 아무것도 없었던 거야. 그런데 아까 T가 경칩 이야기를 할 때 문득 A 주머니가 눈에 띄었는데.."

    "J는 접시를 옮기던 손길을 멈췄다."

    s "뭔가 들어 있었어. 문에 파인 홈을 보면 딱 경칩만한 크기야."
    j worry "그러니까 네 말은, 지금 A가 경칩을 일부러 어떤 방식으로든 훔쳐서.. 주머니에 넣었다는 거야?"
    s "말이 안 되지만, 그래."
    j "그게 경칩인 지 어떻게 알아."
    s "나도 확신할 수는 없어."
    j lonely "확신 없이 사람을 의심할 수 없는데... 음...그래도 네가 그렇게 이야기한다면..."

    "J의 반응은 생각보다 회의적이었다. 아, A는 J에게도 소중한 친구라는 것을 간과해버렸다."
    "J는 A에 대한 믿음과 내 말에 대한 믿음 사이에서 고민하고 있는 것 처럼 보인다."

    #scene black
    scene bg_hallway with dissolve

    "우리는 복잡해진 마음으로 복도를 걸었다. 오른쪽 방은 이미 다 탐사했지만 A와 T는 돌아올 기색이 없다."
    "결국 왼쪽 구역으로 건너가다 T와 마주쳤다."

    show t serious at centerleft with dissolve
    t "오른쪽은 다 찾아봤나요?"
    show s talk:
        xzoom -1
        xalign 0.75
        yalign 1.0
    with dissolve
    s "찾아봤지만..없었어요. 혹시 왼쪽은 어디까지 찾았죠?"
    t "이제 방 하나가 남았어요."
    s "우리가 한번 더 찾아볼게요. 놓친 부분이 있을 수 있으니까요..."
    t talk "..고마워요. 끝방부터 보시면 돼요."

    scene bg_boxroom with dissolve
    "복도 맨 끝 방에는 장식용 돌들이 있었다. 우리는 돌들 사이에서 경칩을 발견했다."

    show j normal at center with dissolve
    j "찾았다!"

    hide j with moveoutright
    "J가 방에서 뛰어나갔다."

    j "경칩을 찾았어요!"

    scene bg_hallway with dissolve
    show j normal at centerleft
    show s normal at left
    "J의 밝은 목소리에 나는 마음이 복잡해진다. J의 목소리에 A와 T가 달려왔다."
    show t talk at centerright with moveinright
    show a normal at right with moveinright
    "A와 눈이 마주쳤다. A는 내 표정을 보더니 무슨 일 있냐는 듯 한 표정을 짓는다."

    j "A, 그런데 주머니에 든 건 뭐에요?"
    a point "아 이거?"
    "A가 주머니에서 돌을 꺼냈다."
    a "돌이야. 정원에 있던 건데, 하나쯤 간직하고 싶어서..."
    t "정원의 돌이요?"
    t serious "방을 나가기 전에는 다시 저택에 놓아두고 가요." #표정 변화
    a talk "거 참 까다롭네."

    "..쓸데없이 A를 의심해버렸다."

    $ j_para -= 2

    jump t_room_end

label t_room_end:
    scene bg_door with dissolve

    "T가 경칩을 꽂으니 문이 열린다. 문 밖엔 또다시 까마득한 암흑이 펼쳐져 있다."

    show t talk at center with dissolve
    t "먼저 가세요."

    show j worry:
        linear 5 xalign 2.0
        yalign 1.0
    with moveinleft
    show a normal:
        linear 5 xalign 2.0
        yalign 1.0
    with moveinleft

    "T의 말에 J와 A는 T의 어깨를 두드려주고 문 밖으로 건너간다."
    show s normal:
        xzoom 1
        linear 4 xalign 0.9
        yalign 1.0
    with moveinleft
    "나도 뒤따라 문 밖으로 건너가다 문참에 멈춰 섰다."
    "혼자 남은 T는 쓸쓸한 복도와 창 너머의 회색빛 정원을 찬찬히 바라보고 있었다."
    "나는 다시 발걸음을 옮겼다."

    call note4 from _call_note4

    jump s_room_start
