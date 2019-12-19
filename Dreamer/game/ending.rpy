#엔딩에 관련된 모든 것들을 적어두는 스크립트(도중 하차 엔딩 포함)
init :
    image bg_frozen_door = "jroom/bg_frozen_door.png"
    image bg_avalanche = "jroom/bg_avalanche.png"
    image end_hospital = "ending/end_hospital.png"
    image ending = "ending/ending.png"
    image ending2 = "ending/ending2.png"
    image s_dead = "ending/s_dead.png"

label end_1_bad :
    scene black
    "J가 말했던 사냥꾼을 만났다. 사지가 묶여 어딘가로 끌려가고 있다."
    "J의 말을 들어볼 걸 그랬다.."
    "{b}GAME OVER{/b}" (what_color = "#f00", what_size = 28)

    return

label end_2_bad:
    t "네 알겠어요. 안녕히계세요..."
    hide t with dissolve
    scene black
    "우리는 방들을 통과했지만, 결국 T가 없이는 통과하지 못하는 방에 맞딱뜨렸다."
    "{i}열린 마음으로 새 친구를 받아줄 걸.{/i} 후회했지만 이미 때는 늦었다."
    "{b}GAME OVER{/b}" (what_color = "#f00", what_size = 28)

    return

label end_3_bad:
    scene bg_frozen_door
    "뒤를 돌아 문고리를 잡으려는데 문이 얼어서 열리지 않는다."

    show s angry at left with dissolve
    s "문이 얼어서 열리지 않아, 봐 결국 우리 모두 죽게되었다고!"

    scene bg_avalanche
    "멀리서 큰소리가 나며 눈사태가 몰려온다. 이게 무슨..."

    show a talk at right with dissolve
    a "왜 얼음성을 탈출하려고 하지? 이 곳이 그냥 꿈의 세계일까?"
    a "아니, 너희는 모두 산 것도 아니고 죽은 것도 아닌 상태야. 현실에서는 코마라고 부르던데, 혼수상태 말이야."
    a "너희는 모두 외롭게 살다가 지금은 코마에 빠져서 산 것도 아니고 죽은 것도 아닌 채로 누워있어."
    a "나도 마찬가지지. 돌아가고 싶지 않지 않나?"
    a "그래서 내 꿈은 이런 불쌍한 너희들을 모두 모아서 얼음성에서 같이 사는거야. 아무도 돌아가지 말고 이 얼음성에서 영원히..."

    scene black with dissolve
    "{b}GAME OVER{/b}" (what_color = "#f00", what_size = 28)
    return

label end_4_bad:
    a "S.. 내 말 들려?"
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

    a "이 세계의 비밀에 대해서 이야기해준다고 했지?"
    s "..."
    a "이 세계는 오로지 그 아이를 위해 만들어졌어."
    a "그 아이가 이 세계 속에서 안전하게 살아가기 위해서 바로 너희 같은 사람들이 이곳에 머물러야 해."
    s "뭐?"
    s "우리 같은 사람들..?"
    a "그래. 너희 같은 사람들. 코마에 빠진... 죽음에 임박한 사람들. 너희를 심연에 붙들어 놓아야... 이 세계가 무너지지 않아."
    s "죽음에 임박했다니...? 그게 무슨 소리야?"
    s "내가 곧 죽는다고...? 그런 거야..??"
    s "A?? 그게 무슨 말인지 설명해줘 A!"
    a "미안해."
    s "...뭐?"
    a "미안해. 너는 깨어날 수 없을 거야."
    a "너를 이곳에 붙잡아 두지 않으면 내 아이가 죽어."
    a "나는 이 세계를 지켜야 해. 도와준 건 정말 고맙지만… 어쩔 수 없어. 어쩔 수 없는 거야 이건."
    s "하나도 이해가 안돼 A, 무슨 소리야??"
    a "어차피 너는 코마에 빠진 상태니까...그래.. 어쩔 수 없는 거야..@$.." (what_size = 20)
    s "A??"
    a "미안해." (what_size = 16)

    "점점 의식이 멀어진다. 나지막히 A의 목소리가 들리지만 무슨 의미인지 파악할 수가 없다..."

    #화면 1. 꿈의 세계에서 무너지듯 화면이 어두워짐..
    #자신의 상태를 자각 + 병실 소리
    # 쓸쓸한 죽음. 삐-

    "{b}GAME OVER{/b}" (what_color = "#f00", what_size = 28)

    return

label end_true_1: #2번 엔딩.
    #화면 1 연습. 어두워지고 밝아짐.
    scene black with dissolve
    scene white with dissolve
    pause .5
    play music "audio/Ending.mp3" fadeout 1
    $ save_j = True

    scene end_hospital with dissolve
    pause 2
    scene ending with dissolve
    pause 4
    scene s_dead with dissolve
    pause 3

    scene black with dissolve

    "결국 나는 열쇠를 잡지 않았다."
    "이 꿈의 세계에서 사냥꾼을 피해 떠돌아다니다, 한 가지 사실을 알게 되었다."
    "현실에서 내 육체는 이미 노인이지만, J는 여기서 보았던 젊은 모습 그대로라는 것을."

    "그 말을 듣고 나는 내 육체가 곧 사라진다는 것에 대한 두려움보다, 아직 살 날이 많은 J를 위해 열쇠를 양보해 주었다는 사실에 대한 안도감이 컸다."
    "그렇기에 나는 그 때의 선택을 후회하지 않는다..."

    jump endnote

    #"{b}- END -{/b}" (what_color = "#F0ACC6", what_size = 28)

    return

label end_true_2: #3번 엔딩.
    #화면 1. + 병실 소리
    scene black with dissolve
    scene white with dissolve
    pause .5
    play music "audio/Ending.mp3" fadeout 1
    scene end_hospital with dissolve
    s "여긴… 병실인가…?"

    "고개를 돌려보니 {i}<S, 68세, 교통사고, 코마 환자>{/i} 라는 진료 카드가 보인다."
    "옆 침대엔...."

    scene ending2 with dissolve
    "꿈의 세계에서 본 것과 똑같은 모습의 젊은 J가 고요히 눈을 감고 누워있다."

    "옆 침대에 누워 있는 J의 젊은 얼굴과, 나의 늙은 손을 번갈아 바라보았다."
    "나는 왜 그런 선택을 했을까."
    "꿈의 세계를 홀로 나오고 나서야 나는 모든 것을 알게 되었다…."

    #6.2 슬퍼하는 S 눈물 떨어지는 것.

    jump endnote
    #"{b}- END -{/b}" (what_color = "#CBCBCB", what_size = 28)

label end_true_3: #4번 엔딩.
    #화면 1. 어두워지고 밝아짐.
    scene black with dissolve
    scene white with dissolve
    pause .5
    play music "audio/Ending.mp3" fadeout 1
    scene end_hospital with dissolve
    s "여긴… 병실인가…?"

    "고개를 돌려보니 {i}<S, 68세, 교통사고, 코마 환자>{/i} 라는 진료 카드가 보인다."
    "옆 침대엔...."

    scene ending2 with dissolve
    "꿈의 세계에서 본 것과 똑같은 모습의 젊은 J가 고요히 눈을 감고 누워있다."

    "옆 침대에 누워 있는 J의 젊은 얼굴과, 나의 늙은 손을 번갈아 바라보았다."
    "나는 왜 그런 선택을 했을까."
    "꿈의 세계를 홀로 나오고 나서야 나는 모든 것을 알게 되었다…."

    jump endnote
    #"{b}- END -{/b}" (what_color = "#CBCBCB", what_size = 28)
