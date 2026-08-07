# 游戏素材映射。
# 背景图由 ImageGen 生成；人物占位将在收到参考照片后替换为正式立绘。

image bg = Transform("images/backgrounds/classroom.png", size=(1920, 1080))
image bg4s1 = Transform("images/backgrounds/corridor_day.png", size=(1920, 1080))
image bg4s2 = Transform("images/backgrounds/corridor_day.png", size=(1920, 1080))
image bg4s2a = Transform("images/backgrounds/corridor_day.png", size=(1920, 1080))
image bg4s2b = Transform("images/backgrounds/corridor_day.png", size=(1920, 1080))
image bg4s3 = Transform("images/backgrounds/cafeteria.png", size=(1920, 1080))
image bg4court = Transform("images/backgrounds/basketball_court.png", size=(1920, 1080))
image bg4s4 = Transform("images/backgrounds/corridor_sunset.png", size=(1920, 1080))
image bg4e1 = Transform("images/backgrounds/stairwell_dusk.png", size=(1920, 1080))
image bg4s3_1b = Transform("images/backgrounds/stairwell_dusk.png", size=(1920, 1080))
image bg4e2 = Transform("images/backgrounds/stairwell_dusk.png", size=(1920, 1080))
image bg4e3 = Transform("images/backgrounds/stairwell_dusk.png", size=(1920, 1080))

# 临时人物标记，确保在正式立绘完成前项目仍可完整运行。
image Snake = Text("蛇哥\n（立绘待导入）", size=48, color="#ffffff", text_align=0.5, outlines=[(3, "#244a73", 0, 0)])
image Crab = Text("蟹宝王\n（立绘待导入）", size=48, color="#ffffff", text_align=0.5, outlines=[(3, "#b34f68", 0, 0)])
image CBro = Text("超哥\n（立绘待导入）", size=48, color="#ffffff", text_align=0.5, outlines=[(3, "#5a477d", 0, 0)])
image Turtle = Text("龟\n（立绘待导入）", size=48, color="#ffffff", text_align=0.5, outlines=[(3, "#39714d", 0, 0)])
image Cannon = Text("炮神\n（立绘待导入）", size=48, color="#ffffff", text_align=0.5, outlines=[(3, "#87522f", 0, 0)])

init python:
    def crab_rank(value):
        if value < 40:
            return "拉黑边缘"
        elif value < 60:
            return "低气压区"
        elif value < 80:
            return "观察期"
        elif value < 100:
            return "好感区"
        elif value < 120:
            return "心动共振"
        else:
            return "关系超纲"

define event_catalog = [
    ("数学神谕", "超哥认证：感情不能只写答案，也要写过程。"),
    ("末三位审判", "在恋爱游戏里真的算完了一道模运算。"),
    ("走廊止哭术", "一句不太熟练、但足够认真的安慰。"),
    ("初中档案", "炮神提供的蟹宝王相处说明书。"),
    ("被保留的面包", "有人注意到了她没有吃晚饭。"),
    ("晚霞定理", "两个人第一次得到了同一个结论。"),
    ("龟的错误选项", "尊重比替别人作答更重要。"),
    ("二楼联合自习", "语文和数学达成了暂时停战。"),
    ("薛定谔的面包", "在打开袋子以前，晚饭同时存在与不存在。"),
    ("系统外的人", "她看见了本不该被角色看见的数字。"),
    ("学考之后", "试卷之外的约定正式生效。"),
]


screen relationship_status():
    zorder 90

    frame:
        xalign 0.985
        yalign 0.025
        padding (18, 12)
        background Solid("#152238cc")

        vbox:
            spacing 3
            text "关系面板" size 24 color "#ffffff" xalign 0.5
            text "蟹宝王  [crab_affection] · [crab_rank(crab_affection)]" size 20 color "#ffb8c8"
            text "超哥  [cbro_affection]" size 22 color "#cbb8ff"
            text "炮神  [cannon_affection]" size 22 color "#ffd0a8"
            text "承诺  [promise_points]    坦诚  [honesty_points]" size 19 color "#b8e3ff"
            textbutton "回忆事件  [len(unlocked_events)]/[len(event_catalog)]":
                xalign 0.5
                text_size 18
                action Show("event_gallery")


screen event_gallery():
    modal True
    zorder 200

    add Solid("#08101bcc")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1080
        ysize 760
        padding (45, 35)
        background Solid("#152238f2")

        vbox:
            spacing 17
            text "回忆事件" size 42 color "#ffffff" xalign 0.5

            for event_name, event_desc in event_catalog:
                if event_name in unlocked_events:
                    text "◆ [event_name]" size 25 color "#ffcfdf"
                    text "　[event_desc]" size 19 color "#d8e2ef"
                else:
                    text "◇ 尚未解锁" size 23 color "#697789"

            textbutton "返回":
                xalign 0.5
                text_size 24
                action Hide("event_gallery")
