default crab_affection = 70
default cbro_affection = 70
default cannon_affection = 70
default s2_choice = ""


label Aside(text):
    scene black
    with dissolve
    pause 0.35
    show text "{color=#ffffff}[text]{/color}" at truecenter
    with dissolve
    pause 1.0
    hide text
    with dissolve
    pause 0.35
    return


label EndingCard(title, subtitle):
    hide screen relationship_status
    scene black
    with dissolve
    show text "{size=64}{color=#ffffff}[title]{/color}{/size}\n\n{size=30}{color=#b8c7dc}[subtitle]{/color}{/size}" at truecenter
    with dissolve
    pause 2.5
    hide text
    with dissolve
    return


label start:
    $ crab_affection = 70
    $ cbro_affection = 70
    $ cannon_affection = 70
    $ s2_choice = ""
    show screen relationship_status

    call Aside("数学学考模拟，第一考场")
    scene bg
    with dissolve

    show Snake at center
    Snake "真是轻轻又松松，解析几何压轴题4±2√3和0。"
    hide Snake

    show Crab at center
    Crab "这最后一题好难啊，www学考数学不会真的要拿B了吧。"
    hide Crab

    jump S1


label S1:
    call Aside("蛇哥自信地走出教室，遇到了数学之神超哥")
    scene bg4s1
    with dissolve

    menu:
        "超哥，最后一题是不是4±2√3和0？":
            show Snake at center
            Snake "超哥，最后一题是不是4±2√3和0？"
            hide Snake
            show CBro at center
            CBro "你真强！"
            $ cbro_affection += 10
            "超哥好感度+10（[cbro_affection]）"
            hide CBro

        "超哥，这数学考试好难啊！":
            show Snake at center
            Snake "超哥，这数学考试好难啊！"
            hide Snake
            show CBro at center
            CBro "藏嘞！"
            "超哥好感度不变（[cbro_affection]）"
            hide CBro

    jump S2


label S2:
    call Aside("蛇哥去了一趟厕所，和好兄弟林诗谕在走廊聊完，出来时又看到了蟹宝")
    scene bg4s2
    with dissolve

    menu:
        "去找蟹宝装逼":
            $ s2_choice = "show_off"
            jump s2_A

        "知道蟹宝没考好，决定去安慰她":
            $ s2_choice = "comfort"
            jump s2_B


label s2_A:
    scene bg4s2a
    with dissolve
    show Snake at center
    Snake "蟹宝，我刚对完答案，真是轻轻又松松啊，又拿到100分了！你考得怎么样？"
    hide Snake
    show Crab at center
    "蟹宝双眼通红，十分委屈。"
    Crab "滚！你个臭蛇蛇！"
    $ crab_affection -= 10
    "蟹宝转身跑了，好感度-10（[crab_affection]）"
    hide Crab
    jump S3


label s2_B:
    scene bg4s2b
    with dissolve
    show Snake at center
    Snake "蟹宝，下周就学考了，要加油啊。这次模拟考有点难，我最后一题也没做出来……学考肯定比这简单！"
    hide Snake
    show Crab at center
    Crab "嗯嗯，蛇哥我们一起加油！过会儿我要去二楼背书，你不是语文还没怎么复习嘛，我来帮你呀！"
    hide Crab
    show Snake at center
    Snake "没问题！"
    hide Snake
    $ crab_affection += 10
    "蟹宝好感度+10（[crab_affection]）"
    jump S3


label S3:
    call Aside("蛇哥饿得不行，叫上炮神去食堂美餐一顿。吃完后，炮神盛情邀请他去高地打球")
    scene bg4s3
    with dissolve

    menu:
        "欣然接受":
            $ cannon_affection += 10
            scene bg4court
            with dissolve
            call Aside("两个人打球打到了六点")
            if s2_choice == "show_off":
                jump end1
            else:
                jump s3_1_B

        "拒绝炮神，并告诉他跟蟹宝有约了":
            show Cannon at center
            Cannon "去吧去吧，真扫兴！"
            $ cannon_affection -= 10
            "炮神好感度-10（[cannon_affection]）"
            hide Cannon
            jump S4


label S4:
    call Aside("蛇哥拿着语文必修二，径直走到二楼走廊，看到了正在背书的蟹宝")
    scene bg4s4
    with dissolve

    menu:
        "走到蟹宝身边，轻轻拍她的肩膀":
            if s2_choice == "show_off":
                show Crab at center
                Crab "干嘛？你不是考得轻轻松松吗？"
                hide Crab
                menu:
                    "只为刚才的冒失道歉":
                        show Snake at center
                        Snake "蟹，对不起。我们一起复习语文学考吧！"
                        hide Snake
                        show Crab at center
                        Crab "好吧。"
                        hide Crab
                        "蟹宝好感度不变（[crab_affection]）"

                    "认真承认装逼和冒失":
                        show Snake at center
                        Snake "蟹，我刚才不该装逼，也不该只顾着自己开心。对不起。你教我语文，我教你数学，我们一起好好复习吧！"
                        hide Snake
                        show Crab at center
                        Crab "这次原谅你了，下次可不要这样了哦！"
                        hide Crab
                        $ crab_affection += 10
                        "蟹宝好感度+10（[crab_affection]）"
            else:
                show Crab at center
                Crab "蛇，你真的来啦。"
                hide Crab
                show Snake at center
                Snake "答应你的事，当然要做到。"
                hide Snake
                $ crab_affection += 20
                "蟹宝好感度+20（[crab_affection]）"

        "发现她没吃晚饭，把准备的小零食递给她":
            show Snake at center
            Snake "先吃一点吧，饿着肚子可背不进去。"
            hide Snake
            show Crab at center
            if s2_choice == "show_off":
                Crab "还算你有良心，这次原谅你了。"
                $ crab_affection += 10
                "蟹宝好感度+10（[crab_affection]）"
            else:
                Crab "你居然注意到了……谢谢你，蛇哥！"
                $ crab_affection += 30
                "蟹宝好感度+30（[crab_affection]）"
            hide Crab

    call Aside("晚霞落在书页上，两个人并肩开始复习语文必修三")
    if crab_affection >= 90:
        jump end_good
    else:
        jump end_reconcile


label end_good:
    scene bg4s4
    with dissolve
    show Crab at center
    Crab "等学考结束，我们也一起去高地走走吧。不是打球，就我们两个。"
    hide Crab
    show Snake at center
    Snake "好，一言为定。"
    hide Snake
    call EndingCard("好结局 · 晚霞与约定", "有些答案不在试卷上，但也值得认真写下。")
    return


label end_reconcile:
    scene bg4s4
    with dissolve
    show Crab at center
    Crab "今天的事我还没有完全消气，不过……先复习吧。"
    hide Crab
    show Snake at center
    Snake "嗯。我会慢慢把扣掉的分补回来。"
    hide Snake
    call EndingCard("普通结局 · 重新起笔", "关系没有标准答案，重要的是愿意认真改正。")
    return


label end1:
    scene bg4e1
    with dissolve
    call Aside("蟹宝一个人在二楼边背书边哭。晚自习快开始时，她看见蛇哥和炮神抱着篮球回来，终于彻底失望")
    $ crab_affection = 0
    "蟹宝好感度归零（[crab_affection]）"
    call Aside("回到家后，蟹宝给蛇哥发出最后一条消息，随后把他拉黑了")
    call EndingCard("坏结局 · 数学会陪你", "赢下了压轴题，却弄丢了更重要的约定。")
    return


label s3_1_B:
    scene bg4s3_1b
    with dissolve
    call Aside("蟹宝晚饭只吃了一个面包，在二楼一直等到天黑。看到蛇哥和炮神抱着篮球回来，她终于拦住了两个人")
    $ crab_affection -= 20
    "蟹宝好感度-20（[crab_affection]）"
    show Crab at center
    Crab "蛇！你不是答应要来吗？"
    hide Crab

    menu:
        "坦诚告诉蟹宝，自己忘了":
            jump end2
        "撒谎说炮神非要拉自己去打球":
            jump end3


label end2:
    scene bg4e2
    with dissolve
    show Crab at center
    Crab "为什么你每次都这样！这就是你说的一辈子对我好吗？再也不理你了。"
    hide Crab
    $ crab_affection = 0
    "蟹宝好感度归零（[crab_affection]）"
    call EndingCard("坏结局 · 被忘记的约定", "坦白来得太迟，失望已经等了太久。")
    return


label end3:
    scene bg4e3
    with dissolve
    show Crab at center
    Crab "蛇！你能不能找一个好一点的借口！我真的生气了！"
    $ crab_affection -= 30
    "蟹宝好感度-30（[crab_affection]）"
    hide Crab
    show Turtle at center
    Turtle "蛇，你怎么可以这样对蟹！"
    hide Turtle
    call EndingCard("坏结局 · 拙劣借口", "一次失约已经很糟，谎言让它再也无法挽回。")
    return
