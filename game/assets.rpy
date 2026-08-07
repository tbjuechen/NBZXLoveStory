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
image Crab = Text("蟹宝\n（立绘待导入）", size=48, color="#ffffff", text_align=0.5, outlines=[(3, "#b34f68", 0, 0)])
image CBro = Text("超哥\n（立绘待导入）", size=48, color="#ffffff", text_align=0.5, outlines=[(3, "#5a477d", 0, 0)])
image Turtle = Text("龟哥\n（立绘待导入）", size=48, color="#ffffff", text_align=0.5, outlines=[(3, "#39714d", 0, 0)])
image Cannon = Text("炮神\n（立绘待导入）", size=48, color="#ffffff", text_align=0.5, outlines=[(3, "#87522f", 0, 0)])

screen relationship_status():
    zorder 90

    frame:
        xalign 0.985
        yalign 0.025
        padding (18, 12)
        background Solid("#152238cc")

        vbox:
            spacing 3
            text "关系" size 24 color "#ffffff" xalign 0.5
            text "蟹宝  [crab_affection]" size 22 color "#ffb8c8"
            text "超哥  [cbro_affection]" size 22 color "#cbb8ff"
            text "炮神  [cannon_affection]" size 22 color "#ffd0a8"
