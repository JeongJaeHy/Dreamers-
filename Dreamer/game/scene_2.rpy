#전개 파트 2 얼음성 까지의 여로 T와의 만남 등등 파트.
init:
    image bg_ice_castle = "scene2/얼음성.png"
    image bg_hall = "scene2/연회장.png"
    image bg_hall_running = "scene2/연회장_running.png"
    image bg_hall_enter = "scene2/연회장입구.png"
    image bg_hall_hide = "scene2/연회장숨기.png"
    image bg_hall_hide_wt = "scene2/연회장숨기_t팔.png"

label scene_2_start :
    #화면 검은색 + 멀리 보이는 얼음성 조그맣게.
    scene bg_ice_castle with dissolve
    "멀리 얼음성이 보인다."

    "멀리서 보아도 얼음성의 위용은 엄청났다. 하늘 끝까지 뻗은 뾰족한 얼음 첨탑과, 두꺼운 기둥들..."

    show a talk at right with dissolve
    a "여기서부터는 정신 똑바로 차려야 해."
    show s surprise at left with dissolve
    s "왜?"
    a "들어가면 웨이터가 있을거야. 웨이터를 따돌려야 해."
    a "얼음성 안엔 죽은 사람만 들어갈 수 있고, 웨이터는 살아 있는 사람을 추려내어 사냥꾼에게 넘겨주거든."

    hide a
    hide s
    "A는 얼음성 안엔 드레스를 입고 춤을 추는 죽은 사람들이 즐비하다고 했다. 죽은 사람들이 춤을 춘다니..얼음성은 도대체 누가 만들었을까."

    scene black with dissolve

    scene bg_hall_enter with dissolve
    "A는 얼음성의 문을 열었다. 살짝 열린 틈으로 흥겨운 노랫소리가 흘러나왔다."

    show a normal at right with dissolve
    a "다행히 한창 연회 중이야. 몰래 들어가자. 나를 따라와."
    hide a with moveoutright

    "J와 카슈가 먼저 따라 들어가고, 내가 그 뒤를 이어 들어간다."
    scene bg_hall with fade
    "얼음성에 들어오자 저 멀리서 온통 어울려 춤을 추는 사람들과, 그 위로 번쩍거리는 샹들리에와 각종 장식들로 눈이 부시다."

    show a anxoius at right with dissolve
    a "이런. 웨이터에게 들켜버렸어. 내가 준비한 출입증을 꺼내."

    "얼음성으로 오는 길에 A는 위조한 출입증을 하나씩 주었는데. 이게 과연 쓸모가 있을까..."
    show t far at center with dissolve
    "키 큰 웨이터가 이리로 걸어오고 있다. 명찰에 ‘T’라는 이름이 적혀 있다."

    show t normal with dissolve
    t "얼음성을 방문하신 여러분, 안녕하세요. 잠시 출입증 검사가 있겠습니다."
    a talk "여기."
    t "....."

    "웨이터가 A의 위조 출입증을 한참을 돌려보고 있다. 손에 땀이 배어나온다."

    t smile "네, 확인되었습니다. 얼음성에서 좋은 시간 보내십시오. 나머지 손님들도 출입증을 주세요. 귀여운 강아지 손님도 있네요."

    "J와 나의 출입증도 통과되었다. T는 인사를 하고 저 멀리 사라져갔다."
    hide t with moveoutleft
    "연회장 한 켠엔 너무나 맛있어 보이는 음식들이 한가득 쌓여 있었다. 컵케잌 하나라도 집어먹을 수 있으면..."

    a anxious "정신 차려! 우린 여기 연회를 즐기러 온 게 아니야. 저 뒤편 복도로 눈에 띄지 않고 가야 해. 최대한 자연스럽게 행동해."
    show j worry at center with dissolve
    j "알겠어."
    "J는 카슈를 가슴에 꼭 안았다."
    show s surprise at left with dissolve
    s "그래."

    hide a
    hide j
    hide s

    "복도까지 가는 길엔 등에서 식은땀이 줄줄 흘렀다. 복도 끝 즈음에 다다르자 작은 방 문이 하나 보였다."
    "문득 뒤에서 요란한 발소리가 들려온다. 맨 앞엔 아까 보았던 웨이터가 달려오고 있다."

    "웨이터들" "거기서!"
    show a anxious:
        xzoom -1
        xalign 0.0
        yalign 0.0
    with moveinleft
    a "J, S. 뛰어! 문을 열고 들어가!"
    hide a with moveoutright

    scene bg_hall_running

    "우리 셋은 달리기 시작한다."
    "숨이 가빠오고, A가 작은 방 문을 열고 우리는 방 안으로 몸을 던져 굴러들어갔다.."
    "문이 닫혔다. 웨이터들의 소리가 멀어져간다."

    jump scene_2_1

label scene_2_1:
    scene bg_hall_hide with fade

    show t far at center with dissolve
    t "여러분"
    show j worry at left with dissolve
    j "으아아아아악!"
    k "....!!"
    show a anxious:
        xzoom 1
        xalign 1.0
        yalign 1.0

    with dissolve
    a "....."

    "웨이터?"
    "맙소사, 웨이터가 있다. 웨이터가 무릎을 짚고 일어난다."

    t surprise "괜찮아요. 무서워하지 마세요."
    a "언제 들어온거야."
    t "문이 닫히고 난 뒤에요. 통과해서 들어왔죠."

    menu :
        "괜찮기는 개뿔. 얼음성의 꿍꿍이가 분명하다. T를 당장 문 밖으로 내보내자." :
            hide t with dissolve
            scene bg_hall_hide_wt
            "간신히 웨이터를 문 밖으로 내보냈다. 그런데 문 중앙에서부터 손이 불쑥 들어오더니 웨이터가 다시 문을 통과해 들어왔다."

            show t normal at center with dissolve
            t "말씀드렸잖아요. 얼음성 웨이터는 문을 통과할 수 있다니까요."
            j "아..."
            t serious "제 이야기를 들어봐 주세요. 간절해요.."

            jump scene_2_2
        "T의 이야기를 더 들어보자." :
            jump scene_2_2


label scene_2_2:
    t serious "저는 T에요. 얼음성의 선임 웨이터죠. 그동안 얼음성에 종종 산 사람들이 들어오곤 했어요. 그래서..."

    "T는 말을 아끼는 눈치다."

    t "어쨌든, 궁금했어요. 그 사람들이 어디로 가게 되는지, 왜 들어오는지..."
    t "그러다 알게 되었어요. 제가 얼음성을 빠져가나는 산 사람을 그냥 보내 준 적이 있었거든요."
    show j normal at left with dissolve
    j "그래서 아까 출입증도..."
    t "봐준 거죠. 다른 웨이터가 봤으면 국물도 없었을 거에요. 누가봐도 위조였거든요. "
    k "멍!"
    show a anxious at right with dissolve
    a "너무 티났나..."
    t "저도 함께 이 꿈을 탈출하고 싶어요. 저는 얼음성에서 오래 근무했지만, 요즘엔 얼음성 웨이터 일도 아무런 의미가 없어졌어요."
    j "무슨 일이 있었나요?"
    t "..."

    "T는 더 이상은 말하지 않겠다는 듯 입을 다물었다."
    "A가 가족 이야기를 하지 않는 것 처럼 T도 얼음성 이야기를 잘 하지 않는다.."

    j "T, 당신이 정말 우리에게 적대적인 사람이 아니라면 함께 방들을 통과해도 좋아요. 당신에게 어떤 사연이 있는지는 모르겠지만..."
    a "J, 이건 혼자 정할 일이 아니야."
    t "..저는 이미 웨이터로 돌아갈 수 없는 몸이 되었어요. 지금쯤 제가 없어서 연회가 엉망이 되었을 거에요."
    t "기대하지는 않을게요. 하지만 저는 진심으로 여러분들과 함께하고 싶어요."
    k "멍!"
    a talk "J, S. 의논을 하도록 하자."

    menu :
        "T를 무리에 받아준다.":
            jump scene_2_end

        "T를 돌려보낸다.":
            jump end_2_bad

label scene_2_end:
    t "고마워요. 여러분을 열심히 도와 함께 꿈에서 깨어나고 싶어요. 얼음성은 이젠... 지긋지긋하거든요."
    a normal "우리 뒤에 문이 하나 더 있어."

    "T, A, 카슈, 나, J… 우리는 또 다시 나 있는 문 앞으로 함께 다가갔다."
    "J가 문을 열었다. 세찬 한기가 훅 끼쳐왔다."

    call note2
    jump j_room_start
