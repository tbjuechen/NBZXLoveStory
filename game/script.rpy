label Aside(text):
    scene black
    with dissolve

    pause 0.5

    show text "{color=#ffffff}[text]{/color}"
    with dissolve
    pause 1.0

    hide text
    with dissolve

    pause 0.5

    return


# 游戏在此开始。

label start:
    call Aside("数学学考模拟，第一考场")
    scene bg

    show Snake
    Snake "真是轻轻又松松，解析几何压轴题4±2√3和0"
    hide Snake

    show Crab
    Crab "这最后一题好难啊，www学考数学不会真的要拿B了吧"
    hide Crab

    jump S1
    
    return

# 场景一

label S1:
    call Aside("蛇哥自信地走出教室，遇到了数学之神超哥")
    scene bg4s1

    menu:
        "超哥，最后一题是不是4±2√3和0？":

            call s1_A
        
        "超哥，这数学考试好难啊！":
            call s1_B

    jump S2

# 场景一分支A
label s1_A:
    show Snake
    Snake "超哥，最后一题是不是4±2√3和0？"
    hide Snake

    show CBro
    CBro "你真强！（比大拇指）"
    
    "超哥好感度+10（80）"
    hide CBro

    return

# 场景一分支B
label s1_B:
    show Snake
    Snake "超哥，这数学考试好难啊！"
    hide Snake

    show CBro
    CBro "藏嘞！（开始喘气）"
    
    "超哥好感度不变"
    hide CBro

    return

label S2:
    call Aside("蛇哥准备去厕所尿一个，遇到好兄弟林诗谕，二人在走廊有说有笑，尿完出了厕所")
    scene bg4s2
    with dissolve

    menu:
        "去找蟹宝装逼":
            $ s2 = 'A'
            call s2_A
        
        "知道蟹宝肯定没考好，决定去安慰她":
            $ s2 = 'B'
            call s2_B
    
    jump S3


label s2_A:
    scene bg4s2a
    with dissolve

    show Snake
    Snake "蟹宝，我刚对完答案，真是轻轻又松松啊，又拿到100分了！你考得怎么样啊？"
    hide Snake

    show Crab
    "蟹宝双眼通红，十分委屈"
    Crab "滚！你个臭蛇蛇！"
    hide Crab

    "蟹宝说完转身就跑了，好感度-10（60）"

    return

label s2_B:
    scene bg4s2b
    with dissolve

    show Snake
    Snake "蟹宝，下周就学考了，要加油啊，这次模拟考出的有点难了，最后一题我没做出来……学考肯定比这简单！"
    hide Snake

    show Crab
    Crab "嗯嗯，蛇哥我们一起加油！过会儿我要去二楼背书，你不是语文还没怎么复习嘛，我来帮你呀！"
    hide Crab

    show Snake
    Snake "没问题！"
    hide Snake

    "蟹宝好感度+10（80）"

    return

label S3:
    call Aside("蛇哥感到非常饥饿，急需去食堂进食，于是叫上炮神一起去食堂美餐一顿，吃完后炮神盛情邀请去高地打球")
    scene bg4s3
    with dissolve
    menu:
        "欣然接受":
            call Aside("两个人打球打到了6点")
            if s2 == 'A':
                jump end1
            else:
                call s3_1_B
        "拒绝炮神，并告诉他跟蟹宝有约了":
            show Cannon
            Cannon "去吧去吧，真扫兴！"
            "炮神好感度-10（60）"

label S4:
    call Aside("蛇哥吃完饭后，拿着语文必修二，径直走到二楼走廊，看到了正在背书的蟹宝")
    scene bg4s4
    with dissolve

    menu:
        "偷偷走到蟹宝身后并用蛇身缠绕住她":
            if s2=='A':
                "蟹宝用力挣脱了蛇哥的缠绕"
                show Crab
                Crab "滚！"
                hide Crab

                "看到蟹宝一脸嫌弃，蛇哥顿时汗流浃背"
                menu:
                    "为自己的冒失而道歉":
                        show Snake
                        Snake "蟹，对不起，我们一起复习语文学考吧！"
                        hide Snake

                        show Crab
                        Crab "好吧"
                        "蟹宝好感度不变（60）"
                        hide Crab
                    "为自己的装逼行为以及刚才的冒失而道歉":
                        show Snake
                        Snake "蟹，我不该跟林诗谕那个神人一起装逼的，对不起！刚刚只是想安慰你，但有点冒失了。下周就学考了，我们一起好好复习吧，你教我语文，我教你数学！"
                        hide Snake

                        show Crab
                        Crab "好吧，这次原谅你了，下次可不要这样了哦！"
                        "蟹宝好感度+10（70）"
                        hide Crab
            else:
                "蟹宝稍稍用力，但发现蛇的缠绕是如此有力，于是选择放弃"
                "蟹宝俏脸微红"
                show Crab
                Crab "蛇，人这么多要注意点，我害羞！"
                "蛇哥松开了缠绕"
                hide Crab
                call Aside("开始一起复习语文必修三")
                "蟹宝好感度+20（100）"
        "看到蟹宝放在石栏杆上的面包袋，知道她没吃晚饭，为她带了一点小零食":
            if S2=='A':
                "蟹宝虽然一脸傲娇，但内心窃喜，心中的郁闷一扫而空"
                show Crab
                Crab "还算你有良心，这次原谅你了。"
                "蟹宝好感度+10（70）"    
                hide Crab

                call Aside("开始一起复习语文必修三")
            else:
                "蟹宝开心到了极点，蛇哥这波既安慰她，又给她送吃的，蟹宝在物质和精神上大大地满足"
                "蟹宝好感度+30（110）"
                call Aside("开始一起复习语文必修三")
                                
label end1:
    scene bg4e1
    with dissolve

    call Aside("蟹宝一个人在二楼背书，边背边哭，被龟少看到了，龟少安慰蟹宝，在晚自习快开始的时候发现蛇哥和炮神拿着篮球从高地回来，终于死心，二人决定不上晚自习，一起回家")

    "蟹宝好感度归零（0）"

    call Aside("回到家后，蟹宝泪如泉涌，想起那条装逼的蛇，又气又哭，最终给蛇哥编辑了一条消息：傻逼，你就跟你的数学去过一辈子吧！发完就把蛇哥拉黑了")

    return

label s3_1_B:
    scene bg4s3_1b
    with dissolve

    call Aside("蟹宝一个人在二楼背书，晚饭草草吃了一个面包，一直苦等蛇哥，等得又累又饿，在晚自习快开始的时候看到蛇哥和炮神拿着篮球从高地回来")

    "蟹宝好感度-20（40）"
    "蟹宝决定找蛇哥问责，于是在蛇哥和炮神上楼的路上拦住了他俩"

    show Crab
    Crab "蟹宝决定找蛇哥问责，于是在蛇哥和炮神上楼的路上拦住了他俩"
    "看到蟹宝满脸生气，蛇哥瞬间汗流浃背，才想起自己忘了跟蟹宝的约定"
    hide Crab

    menu:
        "坦诚地告诉蟹宝，自己忘了":
            jump end2
        "向蟹宝撒谎，说炮神非得拉他去把上次的百分大战打完，并解释自己心里一直想着她，于是打完百分大战就马上赶过来了":
            jump end3
    
    return

label end2:
    scene bg4e2
    with dissolve

    show Crab
    Crab "蛇！为什么你每次都这样！这就是你说的一辈子对我好吗？再也不理你了www"
    hide Crab
    "蟹宝说完把语文必修三往地上狠狠一摔，瞬间跑得没影了"
    "蟹宝好感度归零（0）"

    call Aside("回到家后，蟹宝泪如泉涌，想起那条的健忘的蛇，又气又哭，最终给蛇哥编辑了一条消息：傻逼！你就跟你的炮神去过一辈子吧！发完就把蛇哥拉黑了")

    return

label end3:
    scene bg4e3
    with dissolve

    show Crab
    Crab "蛇！你能不能找一个好一点的借口！我生气了！"
    "蟹宝好感度-30（10）"
    hide Crab
    "蟹宝把语文必修三扔到楼下，瞬间跑得没影了"
    "一旁的龟少看到了，立刻冲了出来"
    show Turtle
    Turtle "蛇，你怎么可以这样对蟹！说完便追了上去"
    hide Turtle

    return