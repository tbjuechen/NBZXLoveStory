default crab_affection = 70
default cbro_affection = 70
default cannon_affection = 70
default promise_points = 0
default honesty_points = 0
default turtle_pressure = 0
default s2_choice = ""
default brought_snack = False
default math_trial_correct = False
default unlocked_events = []
default event_count = 0


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


label EventUnlock(event_name):
    if event_name not in unlocked_events:
        $ unlocked_events.append(event_name)
        $ event_count += 1
        play sound "audio/sfx/event_unlock.wav" volume 0.75
        show text "{size=28}{color=#ffcfdf}◆ 回忆事件解锁{/color}{/size}\n{size=46}{color=#ffffff}[event_name]{/color}{/size}" at truecenter
        with dissolve
        pause 1.4
        hide text
        with dissolve
    return


label AffectionNotice(who, amount, reason):
    if amount > 0:
        $ change_text = "+" + str(amount)
        $ change_color = "#ffb8c8"
        play sound "audio/sfx/affection_up.wav" volume 0.65
    elif amount < 0:
        $ change_text = str(amount)
        $ change_color = "#9fc6ff"
        play sound "audio/sfx/affection_down.wav" volume 0.65
    else:
        $ change_text = "不变"
        $ change_color = "#ffffff"
    show text "{size=30}{color=[change_color]}[who] [change_text]{/color}{/size}\n{size=22}{color=#d8e2ef}[reason]{/color}{/size}" at truecenter
    with dissolve
    pause 1.0
    hide text
    with dissolve
    return


label EndingCard(title, subtitle):
    hide screen relationship_status
    stop music fadeout 1.5
    scene black
    with dissolve
    show text "{size=64}{color=#ffffff}[title]{/color}{/size}\n\n{size=30}{color=#b8c7dc}[subtitle]{/color}{/size}\n\n{size=22}{color=#7f91a8}解锁事件：[event_count]/[event_total]{/color}{/size}" at truecenter
    with dissolve
    pause 3.0
    hide text
    with dissolve
    return


label start:
    $ crab_affection = 70
    $ cbro_affection = 70
    $ cannon_affection = 70
    $ promise_points = 0
    $ honesty_points = 0
    $ turtle_pressure = 0
    $ s2_choice = ""
    $ brought_snack = False
    $ math_trial_correct = False
    $ unlocked_events = []
    $ event_count = 0
    show screen relationship_status
    play music "audio/bgm/campus_afterglow.wav" fadein 1.5 volume 0.48
    play sound "audio/sfx/school_bell.wav" volume 0.60

    call Aside("数学学考模拟，第一考场")
    scene bg
    with dissolve

    show Snake at center
    Snake "真是轻轻又松松，解析几何压轴题答案是4正负2倍根号3，还有0。"
    hide Snake

    show Crab at center
    Crab "最后一题好难啊，www学考数学不会真的要拿B了吧。"
    hide Crab

    "考试铃响。有人交卷，有人交代，有人的爱情函数甚至还没有定义域。"
    jump S1


label S1:
    call Aside("蛇哥自信地走出教室，遇到了数学之神超哥")
    scene bg4s1
    with dissolve

    show CBro at center
    "超哥站在走廊中央，神情平静得像一本已经被做完的五三。"
    hide CBro

    menu:
        "向数学天花板核对最后一题":
            show Snake at center
            Snake "超哥，最后一题是不是4正负2倍根号3，还有0？"
            hide Snake
            show CBro at center
            CBro "你真强。答案对了，但人生大题只写答案不给过程，通常要扣分。"
            $ cbro_affection += 10
            hide CBro
            call AffectionNotice("超哥", 10, "获得数学天花板认证")
            call EventUnlock("数学神谕")

        "承认这次数学考试确实有点难":
            show Snake at center
            Snake "超哥，这数学考试好难啊！"
            hide Snake
            show CBro at center
            CBro "难是题目的属性，慌是你的选择。藏嘞！"
            hide CBro
            call AffectionNotice("超哥", 0, "超哥留下了一句无法证明的话")

        "问超哥感情能不能用解析几何解决":
            show Snake at center
            Snake "如果两个人的距离越来越近，能不能直接证明最后会在一起？"
            hide Snake
            show CBro at center
            CBro "不能。两条渐近线也越来越近，但它们从不相交。"
            CBro "除非你主动改变坐标系。"
            $ cbro_affection += 5
            $ honesty_points += 1
            hide CBro
            call AffectionNotice("超哥", 5, "获得跨学科情感指导")
            call EventUnlock("数学神谕")

    jump MathTrial


label MathTrial:
    scene bg4s1
    with dissolve
    play music "audio/bgm/math_oracle.wav" fadeout 0.6 fadein 0.8 volume 0.48
    show CBro at center
    CBro "等等。既然你敢在我面前讨论数学，我需要确认你不是答案背诵型选手。"
    hide CBro
    "超哥从校服口袋里掏出一块便携式黑板。"
    "没有人知道一块一米二宽的黑板为什么能装进校服口袋。数学天花板附近的空间结构可能并不服从欧氏几何。"

    show text "{size=38}{color=#ffffff}超哥封神试炼{/color}{/size}\n\n{size=34}{color=#ffecb8}求 7^(7^7) 的末三位。{/color}{/size}\n\n{size=24}{color=#c6d4e5}禁止使用计算器，允许使用上一世的记忆。{/color}{/size}" at truecenter
    with dissolve
    pause 1.5
    hide text
    with dissolve

    menu:
        "043":
            show CBro at center
            CBro "你成功算出了指数除以一百的余数，然后把它直接当成了答案。属于努力地错。"
            hide CBro
            $ cbro_affection += 2
            call AffectionNotice("超哥", 2, "错误中检测到少量有效步骤")

        "143":
            show CBro at center
            CBro "很有勇气。可惜模运算不根据勇气给分。"
            hide CBro

        "343":
            $ math_trial_correct = True
            show Snake at center
            Snake "答案是343。七的幂在模1000下以100为周期，7的7次方除以100余43，再算7的43次方末三位。"
            hide Snake
            show CBro at center
            CBro "过程完整。你已经从会做题进化成了会让别人看懂。"
            hide CBro
            $ cbro_affection += 15
            call AffectionNotice("超哥", 15, "通过数学天花板入场验证")
            call EventUnlock("末三位审判")

        "807":
            show CBro at center
            CBro "这个答案看起来很像正确答案，这正是它最大的优点。"
            hide CBro

        "向刚说数学可能拿B的蟹宝王求助":
            show Crab at center
            Crab "你礼貌吗？"
            hide Crab
            $ crab_affection -= 3
            call AffectionNotice("蟹宝王", -3, "精准选择了全场最不想做这道题的人")

    show CBro at center
    CBro "标准过程：七的幂模1000每100次循环。7的7次方除以100余43，所以原式与7的43次方末三位相同。"
    CBro "连续平方：7的10次方末三位是249，7的20次方是001，因此7的40次方仍是001，再乘7的3次方，得到343。"
    hide CBro
    "超哥说完，把一米二宽的黑板重新塞回了校服口袋。走廊恢复了正常的空间曲率。"

    jump S2


label S2:
    play music "audio/bgm/campus_afterglow.wav" fadeout 0.6 fadein 0.8 volume 0.48
    call Aside("蛇哥去了一趟厕所，和好兄弟林诗谕在走廊聊完，出来时又看到了蟹宝王")
    scene bg4s2
    with dissolve

    menu:
        "去找蟹宝王装逼":
            $ s2_choice = "show_off"
            jump s2_A

        "看出蟹宝王没考好，先去安慰她":
            $ s2_choice = "comfort"
            jump s2_B

        "假装路过，等她主动开口":
            $ s2_choice = "hesitate"
            jump s2_C


label s2_A:
    scene bg4s2a
    with dissolve
    show Snake at center
    Snake "蟹宝王，我刚对完答案，真是轻轻又松松啊，又拿到100分了！你考得怎么样？"
    hide Snake
    show Crab at center
    "蟹宝王双眼通红，头顶仿佛出现了一个正在读秒的红色感叹号。"
    Crab "滚！你个臭蛇蛇！"
    hide Crab
    $ crab_affection -= 15
    call AffectionNotice("蟹宝王", -15, "在雷区上完成了一次托马斯全旋")
    jump S2_event


label s2_B:
    scene bg4s2b
    with dissolve
    show Snake at center
    Snake "蟹宝王，下周就学考了，要加油啊。这次模拟考有点难，我最后一题也没做出来……学考肯定比这简单！"
    hide Snake
    show Crab at center
    Crab "你最后一题明明做出来了。"
    hide Crab
    show Snake at center
    Snake "那是我的笔做出来的，我的心没有。我的心当时在担心你。"
    hide Snake
    show Crab at center
    Crab "油嘴滑舌……过会儿我要去二楼背书，你语文还没怎么复习吧？我来帮你。"
    hide Crab
    $ crab_affection += 12
    $ promise_points += 1
    call AffectionNotice("蟹宝王", 12, "安慰生效，获得二楼自习约定")
    call EventUnlock("走廊止哭术")
    jump S2_event


label s2_C:
    scene bg4s2
    with dissolve
    "蛇哥以每秒零点三米的速度从蟹宝王面前经过，试图把偶遇伪装成匀速直线运动。"
    show Crab at center
    Crab "蛇，你已经从我面前经过三次了。厕所是个闭合曲线吗？"
    hide Crab
    show Snake at center
    Snake "我只是在研究走廊的人流模型。"
    hide Snake
    $ crab_affection += 3
    call AffectionNotice("蟹宝王", 3, "笨拙得有一点好笑")
    jump S2_event


label S2_event:
    "走廊尽头的自动售货机发出低沉的嗡鸣，像一位见过太多青春期事故的老者。"

    menu:
        "买她平时会喝的饮料":
            show Snake at center
            Snake "给你。糖分不能提高数学成绩，但能暂时提高活着的意愿。"
            hide Snake
            show Crab at center
            Crab "你怎么知道我喜欢这个？"
            hide Crab
            menu:
                "坦白说自己一直有留意":
                    $ crab_affection += 8
                    $ honesty_points += 1
                    call AffectionNotice("蟹宝王", 8, "坦诚比饮料更甜一点")
                "说是售货机托梦告诉你的":
                    $ crab_affection += 4
                    call AffectionNotice("蟹宝王", 4, "售货机被迫承担月老职能")

        "把最后一枚硬币留着买晚饭":
            "蛇哥摸了摸口袋，决定先保证自己不会在晚饭前饿成一条直线。"
            call AffectionNotice("蟹宝王", 0, "理性消费，没有新增剧情事故")

    jump S3


label S3:
    call Aside("蛇哥饿得不行，叫上炮神去食堂美餐一顿")
    scene bg4s3
    with dissolve

    show Cannon at center
    Cannon "你今天怎么三句话不离蟹宝王？她初中跟我一个学校的时候，可没见过你这么抽象的生物。"
    hide Cannon

    menu:
        "请炮神讲讲蟹宝王初中的事":
            show Snake at center
            Snake "兄弟，展开说说。我要做一份高质量人物分析。"
            hide Snake
            show Cannon at center
            Cannon "她不喜欢别人替她作决定。真惹她生气了，别整花活，直接认错。"
            Cannon "还有，她说没事的时候，一般就是有事。说真没事，才有百分之三十可能没事。"
            hide Cannon
            $ cannon_affection += 8
            call AffectionNotice("炮神", 8, "兄弟共享了珍贵的初中版本更新日志")
            call EventUnlock("初中档案")

        "坚持兄弟吃饭不谈感情":
            show Snake at center
            Snake "吃饭的时候只研究碳水，不研究爱情。"
            hide Snake
            show Cannon at center
            Cannon "好兄弟。食堂阿姨刚才手抖的轨迹，才是真正的函数压轴题。"
            hide Cannon
            $ cannon_affection += 3
            call AffectionNotice("炮神", 3, "维护了纯粹的干饭秩序")

        "反问炮神是不是太了解蟹宝王":
            show Cannon at center
            Cannon "她是我初中同学，你是我高中兄弟。我只是怕你俩把我夹成关系图中间的连线。"
            Cannon "放心，我对她没有那个意思。你要是真喜欢，就别让我替你解释。"
            hide Cannon
            $ honesty_points += 1
            call AffectionNotice("炮神", 0, "人物关系获得官方澄清")
            call EventUnlock("初中档案")

    show Cannon at center
    Cannon "吃完去高地？上次百分大战还没打完。"
    hide Cannon

    menu:
        "欣然接受":
            $ cannon_affection += 10
            scene bg4court
            with dissolve
            play sound "audio/sfx/basketball.wav" volume 0.80
            "夕阳把篮筐照成橙色。蛇哥投进了球，也把二楼的约定投出了记忆。"
            call Aside("两个人打球打到了六点")
            if s2_choice == "show_off":
                jump end1
            elif promise_points > 0:
                jump s3_1_B
            else:
                jump end_bro

        "拒绝炮神，告诉他自己和蟹宝王有约":
            show Cannon at center
            Cannon "去吧去吧，真扫兴。以后结婚别让我坐小孩那桌就行。"
            hide Cannon
            $ cannon_affection -= 5
            $ promise_points += 1
            call AffectionNotice("炮神", -5, "兄弟局被爱情支线截胡")
            jump S3_5

        "约定复习结束后再打一场":
            show Snake at center
            Snake "今晚不行。学考结束，我陪你打到灯灭。"
            hide Snake
            show Cannon at center
            Cannon "成交。重色，但还没有完全轻友。"
            hide Cannon
            $ cannon_affection += 5
            $ promise_points += 1
            call AffectionNotice("炮神", 5, "同时维护了约会与兄弟局的未来")
            jump S3_5


label S3_5:
    scene bg4s1
    with dissolve
    "蛇哥抱着语文必修二往楼上走，迎面又撞见了超哥。"
    show CBro at center
    CBro "去二楼？"
    hide CBro

    if "数学神谕" in unlocked_events:
        show Snake at center
        Snake "去改变坐标系。"
        hide Snake
        show CBro at center
        CBro "孺子可教。记住：已知条件是她愿意见你，不代表结论自动成立。"
        hide CBro
        $ honesty_points += 1
    else:
        show Snake at center
        Snake "去复习语文。"
        hide Snake
        show CBro at center
        CBro "拿着数学满分的手去翻语文书，注意物种兼容。"
        hide CBro

    jump S4


label S4:
    call Aside("蛇哥来到二楼走廊。晚霞落在石栏杆上，蟹宝王旁边放着一袋没有吃完的面包")
    scene bg4s4
    with dissolve

    menu:
        "先为走廊上的表现认真道歉":
            show Snake at center
            if s2_choice == "show_off":
                Snake "我刚才不该装逼，更不该在你难过的时候只顾自己开心。对不起。"
            else:
                Snake "我有时候说话像乱码，但答应你的事，我想认真做到。"
            hide Snake
            show Crab at center
            Crab "错误原因分析得还算完整。暂时不给你判零分。"
            hide Crab
            $ crab_affection += 12
            $ honesty_points += 1
            call AffectionNotice("蟹宝王", 12, "没有借口的道歉最有效")

        "发现她没吃晚饭，把准备的小零食递给她":
            $ brought_snack = True
            show Snake at center
            Snake "先吃一点吧。饿着肚子背书，知识会以为你在拒绝接收。"
            hide Snake
            show Crab at center
            Crab "你居然注意到了……谢谢你，蛇哥。"
            hide Crab
            $ crab_affection += 15
            call AffectionNotice("蟹宝王", 15, "物质和精神同时获得补给")
            call EventUnlock("被保留的面包")

        "直接掏出数学卷，提出知识交换":
            show Snake at center
            Snake "你救我的语文，我救你的数学。知识换知识，童叟无欺。"
            hide Snake
            show Crab at center
            Crab "你谈个合作为什么像在学校门口收废品？"
            hide Crab
            $ crab_affection += 7
            call AffectionNotice("蟹宝王", 7, "学科互助协议正式生效")

    if crab_affection >= 95:
        show Crab at center
        Crab "其实我一直觉得，最后一题最讨厌的不是难，是我知道你会做。"
        hide Crab
        show Snake at center
        Snake "那以后我先告诉你过程，不只告诉你答案。"
        hide Snake
        $ crab_affection += 5
        call EventUnlock("晚霞定理")

    jump S5_turtle


label S5_turtle:
    play music "audio/bgm/dusk_tension.wav" fadeout 0.8 fadein 1.0 volume 0.45
    "两人刚翻开书，一个身影从楼梯口缓缓升起。"
    show Turtle at center
    Turtle "蟹，我给你买了奶茶。蛇这种只会数学的冷血动物，不懂怎么照顾人。"
    hide Turtle
    "龟把吸管插入奶茶的动作做得极其熟练，仿佛已经在脑内排练了四十七次。"

    menu:
        "不替蟹宝王回答，让她自己处理":
            show Crab at center
            play sound "audio/sfx/crab_power.wav" volume 0.70
            Crab "谢谢，但不用了。我和蛇哥在复习，请不要打扰我们。"
            hide Crab
            show Snake at center
            Snake "听见了吗？这是她自己的答案。"
            hide Snake
            show Turtle at center
            Turtle "选择题也可能改答案。"
            hide Turtle
            $ crab_affection += 12
            $ honesty_points += 1
            $ turtle_pressure = 0
            call AffectionNotice("蟹宝王", 12, "尊重她作出了自己的选择")
            call EventUnlock("龟的错误选项")

        "冲上去和龟进行低水平雄竞":
            show Snake at center
            Snake "她不喝你的奶茶，她只喝我买的饮料！"
            hide Snake
            show Crab at center
            Crab "你们两个能不能别把我当奖品？"
            hide Crab
            $ crab_affection -= 8
            $ turtle_pressure += 2
            call AffectionNotice("蟹宝王", -8, "低水平雄竞同时伤害了所有人的智商")

        "用超哥传授的数学理论击退龟":
            show Snake at center
            Snake "龟，你和蟹宝王之间不存在映射关系。请不要把单方面趋近误判成相交。"
            hide Snake
            show Turtle at center
            Turtle "感情不是数学！"
            hide Turtle
            show Snake at center
            Snake "这句话由数学天花板超哥最终解释。"
            hide Snake
            show Crab at center
            Crab "虽然完全没听懂，但龟你先走吧。"
            hide Crab
            $ crab_affection += 5
            $ turtle_pressure = 1
            call AffectionNotice("蟹宝王", 5, "抽象程度暂时压制了情敌")

    jump S6_study


label S6_study:
    play music "audio/bgm/campus_afterglow.wav" fadeout 0.8 fadein 1.0 volume 0.45
    call Aside("龟离开后，二楼终于恢复安静。语文和数学准备进行第一次正式会谈")
    scene bg4s4
    with dissolve

    show Crab at center
    Crab "先写作文。题目是《承诺》。八百字，不许列公式。"
    hide Crab

    menu:
        "认真写下今天没有去打球的原因":
            show Snake at center
            Snake "承诺不是因为说出口才重要，是因为对方真的会等。"
            hide Snake
            show Crab at center
            Crab "这句可以。虽然不像你能写出来的。"
            hide Crab
            $ crab_affection += 12
            $ promise_points += 1
            $ honesty_points += 1
            call AffectionNotice("蟹宝王", 12, "作文首次脱离数学答题模板")
            call EventUnlock("二楼联合自习")

        "全文使用解析几何论证爱情":
            show Snake at center
            Snake "设我为点S，你为点C。当SC趋近于零——"
            hide Snake
            show Crab at center
            Crab "停。你这篇作文唯一的优点是字数可以用积分凑。"
            hide Crab
            $ crab_affection += 4
            call AffectionNotice("蟹宝王", 4, "抽象作文获得情感分，没有语文分")

        "写到一半，把笔推给蟹宝王求救":
            show Crab at center
            Crab "作文不能让我替你写。感情也不能。"
            hide Crab
            show Snake at center
            Snake "那你教我怎么写，我自己补完。"
            hide Snake
            $ crab_affection += 6
            $ honesty_points += 1
            call AffectionNotice("蟹宝王", 6, "承认不会也是一种进步")

    "作文休战后，轮到蛇哥讲数学。"
    show Snake at center
    Snake "现在看这道概率题。已知龟每天偶遇你的概率是百分之八十——"
    hide Snake
    show Crab at center
    Crab "那不是概率，那是尾随。"
    hide Crab
    "两个人同时笑了起来。石栏杆上的面包袋被风吹得沙沙作响，像观众席里非常克制的掌声。"

    if brought_snack and math_trial_correct:
        show Snake at center
        Snake "你原来的面包一直没打开。"
        hide Snake
        show Crab at center
        Crab "在我打开袋子以前，它既是晚饭，也不是晚饭。"
        hide Crab
        show Snake at center
        Snake "薛定谔听了都得转来文科。"
        hide Snake
        "蟹宝王打开袋子。里面没有猫，只有一块已经被压成二维图形的面包。"
        call EventUnlock("薛定谔的面包")

    if crab_affection >= 100:
        $ crab_affection += 5
        call AffectionNotice("蟹宝王", 5, "共同笑点形成稳定闭环")
        call EventUnlock("晚霞定理")

    jump S6_meta


label S6_meta:
    if crab_affection < 100:
        jump S7_after_exam

    show Crab at center
    Crab "蛇，我问你一个问题。"
    Crab "你是不是一直在看右上角那个数字？"
    hide Crab
    "空气突然安静。蛇哥缓慢地抬头，看向只有玩家和他本应能够看见的关系面板。"

    menu:
        "承认看过，但好感度不是她本人":
            show Snake at center
            Snake "看过。但那个数字只能提醒我有没有做错，不能替你决定喜不喜欢我。"
            hide Snake
            show Crab at center
            Crab "这还差不多。那从现在开始，不许只看数字。"
            hide Crab
            $ crab_affection += 10
            $ honesty_points += 1
            call AffectionNotice("蟹宝王", 10, "成功与游戏系统划清边界")
            call EventUnlock("系统外的人")
            hide screen relationship_status

        "脱口而出：还差十二分就到下一等级":
            show Crab at center
            Crab "原来我在你眼里是一张经验条。"
            hide Crab
            $ crab_affection -= 18
            call AffectionNotice("蟹宝王", -18, "数值正确，回答完全错误")

        "反问她为什么能看见游戏界面":
            show Crab at center
            Crab "不要转移话题。还有，存档读档的事我也知道。"
            hide Crab
            "远处传来某个存档槽碎裂的声音。实际上什么都没有碎，但玩家下意识想按一下快速保存。"
            $ crab_affection += 5
            call AffectionNotice("蟹宝王", 5, "第四面墙出现轻微结构性裂缝")
            call EventUnlock("系统外的人")

    jump S7_after_exam


label S7_after_exam:
    play sound "audio/sfx/school_bell.wav" volume 0.55
    call Aside("一周后，学考结束。没有人知道成绩，但所有人都假装自己已经稳了")
    scene bg4s1
    with dissolve

    show Crab at center
    Crab "蛇，考完了。你之前说的话还算数吗？"
    hide Crab

    menu:
        "约她一起去高地走走":
            show Snake at center
            Snake "算数。今天不带篮球，只带我本人。"
            hide Snake
            $ crab_affection += 12
            $ promise_points += 1
            call AffectionNotice("蟹宝王", 12, "试卷之外的约定开始生效")

        "叫上炮神一起庆祝":
            show Snake at center
            Snake "我叫上炮神，我们三个去吃东西。你们初中同学也很久没聚了。"
            hide Snake
            show Crab at center
            Crab "可以。但下次我要单独预约你。"
            hide Crab
            $ crab_affection += 6
            $ cannon_affection += 8
            call AffectionNotice("蟹宝王", 6, "友情线与恋爱线和平并轨")

        "先回教室对答案":
            show Crab at center
            Crab "你就跟答案过去吧。"
            hide Crab
            $ crab_affection -= 10
            call AffectionNotice("蟹宝王", -10, "关键时刻再次选择了标准答案")

    if crab_affection >= 120 and promise_points >= 3 and honesty_points >= 3 and event_count >= 6:
        jump end_true
    elif crab_affection >= 100 and promise_points >= 2:
        jump end_good
    elif crab_affection >= 75:
        jump end_reconcile
    else:
        jump end_drift


label end_true:
    scene bg4court
    with dissolve
    show Crab at center
    Crab "蛇，我发现你这次真的不一样了。"
    hide Crab
    show Snake at center
    Snake "哪里不一样？"
    hide Snake
    show Crab at center
    Crab "以前你只记得答案。现在你会记得有人在等你。"
    hide Crab
    show Snake at center
    Snake "那我申请把这道题写一辈子。"
    hide Snake
    call EventUnlock("学考之后")
    call EndingCard("真结局：超纲答案", "数学有唯一答案，但喜欢你这件事可以有无数种证明。")
    return


label end_good:
    scene bg4s4
    with dissolve
    show Crab at center
    Crab "等下次考试结束，我们还来这里吧。"
    hide Crab
    show Snake at center
    Snake "好。这次我会把过程也写完整。"
    hide Snake
    call EventUnlock("学考之后")
    call EndingCard("好结局：晚霞与约定", "有些答案不在试卷上，但也值得认真写下。")
    return


label end_reconcile:
    scene bg4s4
    with dissolve
    show Crab at center
    Crab "你还有很多地方要补考。"
    hide Crab
    show Snake at center
    Snake "可以申请你当监考老师吗？"
    hide Snake
    show Crab at center
    Crab "看你表现。"
    hide Crab
    call EndingCard("普通结局：重新起笔", "关系没有标准答案，重要的是愿意认真改正。")
    return


label end_drift:
    scene bg4s1
    with dissolve
    "蛇哥和蟹宝王一起走出了教学楼，却谁也没有提出下一次见面。"
    "他们没有争吵，只是逐渐变成了两条方向相近、距离不再缩短的直线。"
    call EndingCard("遗憾结局：平行走廊", "不是所有错过都会有巨响，有些只是没有下一句。")
    return


label end1:
    play music "audio/bgm/dusk_tension.wav" fadeout 0.6 fadein 0.8 volume 0.44
    scene bg4e1
    with dissolve
    call Aside("蟹宝王一个人在二楼边背书边哭。晚自习快开始时，她看见蛇哥和炮神抱着篮球回来，终于彻底失望")
    $ crab_affection = 0
    call AffectionNotice("蟹宝王", -99, "好感度归零")
    call EndingCard("坏结局：数学会陪你", "赢下了压轴题，却弄丢了更重要的约定。")
    return


label s3_1_B:
    play music "audio/bgm/dusk_tension.wav" fadeout 0.6 fadein 0.8 volume 0.44
    scene bg4s3_1b
    with dissolve
    call Aside("蟹宝王晚饭只吃了一个面包，在二楼一直等到天黑。看到蛇哥和炮神抱着篮球回来，她终于拦住了两个人")
    $ crab_affection -= 25
    call AffectionNotice("蟹宝王", -25, "约定被篮球击中")
    show Crab at center
    Crab "蛇！你不是答应要来吗？"
    hide Crab

    menu:
        "坦诚告诉蟹宝王，自己忘了":
            jump end2
        "撒谎说炮神非要拉自己去打球":
            jump end3
        "立刻道歉，并提出现在补上复习":
            if honesty_points >= 2 and crab_affection >= 65:
                show Snake at center
                Snake "是我忘了，没有借口。你愿意的话，我现在陪你复习；不愿意，我也接受。"
                hide Snake
                show Crab at center
                Crab "迟到了这么久，你先站旁边反省五分钟。"
                hide Crab
                $ crab_affection += 10
                $ honesty_points += 1
                call AffectionNotice("蟹宝王", 10, "诚实获得一次极限补考机会")
                jump S6_study
            else:
                "蛇哥张了张嘴，却发现自己没有积累足够的坦诚来支撑这句话。"
                jump end2


label end2:
    scene bg4e2
    with dissolve
    show Crab at center
    Crab "为什么你每次都这样！这就是你说的一辈子对我好吗？再也不理你了。"
    hide Crab
    $ crab_affection = 0
    call EndingCard("坏结局：被忘记的约定", "坦白来得太迟，失望已经等了太久。")
    return


label end3:
    scene bg4e3
    with dissolve
    show Crab at center
    Crab "蛇！你能不能找一个好一点的借口！我真的生气了！"
    hide Crab
    $ crab_affection -= 30
    $ turtle_pressure += 2
    call AffectionNotice("蟹宝王", -30, "谎言为龟提供了可乘之机")
    show Turtle at center
    Turtle "蛇，你怎么可以这样对蟹！"
    hide Turtle
    call EndingCard("坏结局：拙劣借口", "一次失约已经很糟，谎言让它再也无法挽回。")
    return


label end_bro:
    scene bg4court
    with dissolve
    show Cannon at center
    Cannon "兄弟，球打得不错。你是不是忘了什么？"
    hide Cannon
    show Snake at center
    Snake "没有吧。"
    hide Snake
    "这一刻，炮神第一次意识到：有些助攻不是把球传出去，而是提醒兄弟别把人生打成单机模式。"
    call EndingCard("兄弟结局：百分大战", "炮神赢了球，蛇哥暂时输掉了恋爱主线。")
    return
