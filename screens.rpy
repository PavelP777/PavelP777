
    config.thumbnail_width = 318
    config.thumbnail_height = 179







    style.file_picker_ss_window.xpos = 0
    style.file_picker_ss_window.ypos = 0



    style.file_picker_text = Style(style.default)
    style.file_picker_text.antialias = True
    style.file_picker_text.font  = "fonts/calibri.ttf"
    style.file_picker_text.color = "#bdbdbd"
    style.file_picker_text.selected_color = "#ffffff"
    style.file_picker_text.hover_color = "#ffffff"
    style.file_picker_text.size = 24
    style.file_picker_text.drop_shadow=(2, 2)
    style.file_picker_text.drop_shadow_color = "#000"





    style.save_load_button = Style(style.button)
    style.save_load_button.background = get_image("gui/save_load/thumbnail_idle.png")
    style.save_load_button.hover_background = get_image("gui/save_load/thumbnail_hover.png")
    style.save_load_button.selected_background = get_image("gui/save_load/thumbnail_selected.png")
    style.save_load_button.selected_hover_background = get_image("gui/save_load/thumbnail_selected.png")
    style.save_load_button.selected_idle_background = get_image("gui/save_load/thumbnail_selected.png")




    style.blank_button = Style(style.button)
    style.blank_button.background = "images/misc/none.png"
    style.blank_button.hover_background = "images/misc/none.png"
    style.blank_button.selected_background = "images/misc/none.png"
    style.blank_button.selected_hover_background = "images/misc/none.png"
    style.blank_button.selected_idle_background = "images/misc/none.png"





    style.base_font = Style(style.default)
    style.base_font.font  = "fonts/calibri.ttf"
    style.base_font.size = 28
    style.base_font.line_spacing = 2

    style.settings_header = Style(style.base_font)
    style.settings_header.font  = "fonts/corbel.ttf"
    style.settings_header.size = 50
    style.settings_header.color = "#4d2e19"
    style.settings_header.hover_color = "#a27146"

    style.settings_text = Style(style.settings_header)
    style.settings_text.size = 36
    style.settings_text.selected_color = "#4d2e19"
    style.settings_text.hover_color = "#a27146"

    style.settings_link = Style(style.base_font)
    style.settings_link.font  = "fonts/gothic.ttf"
    style.settings_link.size = 60
    style.settings_link.kerning = 3
    style.settings_link.color = "#909ca3"
    style.settings_link.hover_color = "#ffffff"
    style.settings_link.selected_color = "#909ca3"
    style.settings_link.selected_idle_color = "#909ca3"
    style.settings_link.selected_hover_color = "#ffffff"
    style.settings_link.insensitive_color = "#909ca3"

    style.hyperlink_text = Style(style.settings_link)
    style.hyperlink_text.underline = True
    style.hyperlink_text.hover_color = "#0ff"
    style.hyperlink_text.idle_color = "#08f"

    style.music_link = Style(style.settings_link)
    style.music_link.insensitive_color = "#4f4f4f"
    style.music_link.selected_color = "#ffffff"

    style.sprite_menu = Style(style.settings_text)
    style.sprite_menu.size = 37
    style.sprite_menu.color = "#466123"
    style.sprite_menu.selected_color = "#466123"
    style.sprite_menu.hover_color = "#9dcd55"

    style.say_dialogue = Style(style.base_font)
    style.say_label = Style(style.base_font)
    style.say_label.size = 28
    style.say_label.drop_shadow=(2, 2)
    style.say_label.drop_shadow_color = "#000"

    style.chapter = Style(style.base_font)
    style.chapter.font  = "fonts/corbel.ttf"
    style.chapter.size = 120
    style.chapter.color = "#fff"

    style.chapter.outlines = [ (1, "#ffdd7d", 0, 0) ]

    style.daynum = Style(style.chapter)
    style.daynum.font  = "fonts/corbel.ttf"
    style.daynum.size = 45

    style.normal_day = Style(style.base_font)
    style.normal_day.color = "#ffdd7d"
    style.normal_day.drop_shadow=(2, 2)
    style.normal_day.drop_shadow_color = "#000"
    style.narrator_day = Style(style.normal_day)
    style.narrator_day.italic = False
    style.thoughts_day = Style(style.normal_day)
    style.thoughts_day.bold = False

    style.normal_sunset = Style(style.base_font)
    style.normal_sunset.color = "#ffdd7d"
    style.normal_sunset.drop_shadow=(2, 2)
    style.normal_sunset.drop_shadow_color = "#000"
    style.narrator_sunset = Style(style.normal_sunset)
    style.narrator_sunset.italic = False
    style.thoughts_sunset = Style(style.normal_sunset)
    style.thoughts_sunset.bold = False

    style.normal_night = Style(style.base_font)
    style.normal_night.color = "#ffdd7d"
    style.normal_night.drop_shadow=(2, 2)
    style.normal_night.drop_shadow_color = "#000"
    style.narrator_night = Style(style.normal_night)
    style.narrator_night.italic = False
    style.thoughts_night = Style(style.normal_night)
    style.thoughts_night.bold = False

    style.normal_prolog = Style(style.base_font)
    style.normal_prolog.color = "#ffdd7d"
    style.normal_prolog.drop_shadow=(2, 2)
    style.normal_prolog.drop_shadow_color = "#000"
    style.narrator_prolog = Style(style.normal_prolog)
    style.narrator_prolog.italic = False
    style.thoughts_prolog = Style(style.normal_prolog)
    style.thoughts_prolog.bold = False

    style.cards_button = Style(style.button)
    style.cards_button.background = RoundRect("#000", False)
    style.cards_button.hover_background = RoundRect("#555", False)
    style.cards_button.insensitive_background = RoundRect("#404040", False)

    style.cards_button_text = Style(style.button_text)
    style.cards_button_text.color = "#FFF"
    style.cards_button_text.selected_color = "#777"
    style.cards_button_text.insensitive_color = "#c8c8c8"

    style.log_button = Style(style.button)
    style.log_button.child = None
    style.log_button.focus_mask = None
    style.log_button.background  = None

    style.log_button_text = Style(style.normal_day)
    style.log_button_text.selected_color = "#115bc0"
    style.log_button_text.hover_color = "#115bc0"
    style.log_button_text.selected_color = "#b6ff00"
    style.log_button_text.hover_color = "#b6ff00"

init python:

    def translate():
        if _preferences.language == None:
            layout.MAIN_MENU = 'Вы действительно хотите выйти в главное меню?\nНесохраненные данные будут потеряны.'
            layout.ARE_YOU_SURE = "Вы уверены?"
            layout.DELETE_SAVE = "Вы уверены, что хотите удалить это сохранение?"
            layout.OVERWRITE_SAVE = "Вы уверены, что хотите переписать это сохранение?"
            layout.LOADING = "Загрузка приведёт к потере несохранённых данных.\nВы уверены, что хотите сделать это?"
            layout.QUIT = "Вы уверены, что хотите выйти?"
            layout.SLOW_SKIP = "Вы уверены, что хотите начать пропуск?"
            layout.FAST_SKIP_UNSEEN = "Вы уверены, что хотите пропустить всё до следующего выбора?"
            layout.FAST_SKIP_SEEN = "Вы уверены, что хотите пропустить всё до следующего нового диалога или выбора?"
        else:
            layout.ARE_YOU_SURE = "Are you sure?"
            layout.DELETE_SAVE = "Are you sure you want to delete this save?"
            layout.OVERWRITE_SAVE = "Are you sure you want to overwrite your save?"
            layout.LOADING = "Loading will lose unsaved progress.\nAre you sure you want to do this?"
            layout.QUIT = "Are you sure you want to quit?"
            layout.MAIN_MENU = "Are you sure you want to return to the main menu?\nThis will lose unsaved progress."
            layout.SLOW_SKIP = "Are you sure you want to begin skipping?"
            layout.FAST_SKIP_UNSEEN = "Are you sure you want to skip to the next choice?"
            layout.FAST_SKIP_SEEN = "Are you sure you want to skip to unseen dialogue or the next choice?"

screen help:


    modal True tag menu

    window background get_image("gui/settings/history_bg.jpg"):

        if _preferences.language == None:
            python:
                ln = 0.5 - (len("информация")*0.03)/2
            add get_image("gui/settings/star.png") xalign ln yalign 0.093
        else:
            python:
                ln = 0.5 - (len("information")*0.03)/2 + 0.015
            add get_image("gui/settings/star.png") xalign ln yalign 0.093
        text translation["INFO"][_preferences.language] style "settings_link" xalign 0.5 yalign 0.08 color "#ffffff"
        if _preferences.language == None:
            python:
                ln = 0.5 + (len("информация")*0.03)/2
            add get_image("gui/settings/star.png") xalign ln yalign 0.093
        else:
            python:
                ln = 0.5 + (len("information")*0.03)/2 - 0.017
            add get_image("gui/settings/star.png") xalign ln yalign 0.093
        textbutton translation["Back"][_preferences.language] style "log_button" text_style "settings_link" xalign 0.015 yalign 0.92 action Return()

        grid 1 2 xpos 0.25 ypos 0.2 xmaximum 1150:
            text translation["info_text"][_preferences.language] style "settings_link" xalign 0.5
            text translation["android_text"][_preferences.language] style "settings_link" xalign 0.5

init python:
    _main_menu_screen = "main_menu"
    renpy.music.register_channel("test_one", "sfx", False)
    renpy.music.register_channel("test_two", "sfx", False)
screen main_menu:

    modal True tag menu


    imagemap:
        if _preferences.language == "english":
            auto "images/gui/title_menu/mainmenu_en_%s.jpg"
        else:
            auto "images/gui/title_menu/mainmenu_%s.jpg"
        hotspot (439,265,318,621) clicked Start()
        hotspot (787,261,270,537) clicked ShowMenu('load')
        hotspot (1067,748,252,312) clicked ShowMenu('preferences')
        hotspot (1083,258,229,538) clicked (Function(collect_all), ShowMenu('gallery'))
        hotspot (1459,532,149,295) clicked ShowMenu('quit') hovered Play("test_one", "sound/sfx/menu_gate.ogg")
        hotspot (494, 125,  768, 86) clicked ShowMenu('help')
        if config.developer:
            hotspot (1578,953,342,127) clicked ShowMenu('show_me_game')
    if True in persistent.endings.values():
        imagebutton auto "images/gui/title_menu/owl_%s.png" xpos 135 ypos 606 action ShowMenu('history') hovered Play("test_two", "sound/test.ogg")



init python:
    _game_menu_screen = "game_menu_selector"
screen game_menu_selector:

    $ timeofday = persistent.timeofday

    modal True tag menu


    button style "blank_button" xpos 0 ypos 0 xfill True yfill True action Return()

    add get_image("gui/ingame_menu/"+timeofday+"/ingame_menu.png") xalign 0.5 yalign 0.5
    imagemap:
        if _preferences.language == "english":
            auto get_image("gui/ingame_menu/"+timeofday+"/ingame_menu_en_%s.png") xalign 0.5 yalign 0.5
        else:
            auto get_image("gui/ingame_menu/"+timeofday+"/ingame_menu_%s.png") xalign 0.5 yalign 0.5
        hotspot (0, 83, 660, 65) focus_mask None clicked MainMenu()
        hotspot (0, 148, 660, 65) focus_mask None clicked ShowMenu('save')
        hotspot (0, 213, 660, 65) focus_mask None clicked ShowMenu('load')
        hotspot (0, 278, 660, 65) focus_mask None clicked (ShowMenu('preferences'), Hide('game_menu_selector'))
        hotspot (0, 343, 660, 65) focus_mask None clicked ShowMenu('quit')


screen save:


    modal True tag menu

    window background get_image("gui/save_load/save_bg.jpg"):

        textbutton translation["settings"][_preferences.language] style "log_button" text_style "settings_link" xalign 0.02 yalign 0.08 action ShowMenu('preferences')
        textbutton translation["LOAD"][_preferences.language] style "log_button" text_style "settings_link" xalign 0.98 yalign 0.08 action ShowMenu('load')
        if _preferences.language == None:
            python:
                ln = 0.5 - (len("сохранить")*0.03)/2
            add get_image("gui/settings/star.png") xalign ln yalign 0.093
        else:
            python:
                ln = 0.5 - (len("save")*0.03)/2 - 0.015
            add get_image("gui/settings/star.png") xalign ln yalign 0.093
        text translation["SAVE"][_preferences.language] style "settings_link" xalign 0.5 yalign 0.08 color "#ffffff"
        if _preferences.language == None:
            python:
                ln = 0.5 + (len("сохранить")*0.03)/2
            add get_image("gui/settings/star.png") xalign ln yalign 0.093
        else:
            python:
                ln = 0.5 + (len("save")*0.03)/2 + 0.015
            add get_image("gui/settings/star.png") xalign ln yalign 0.093
        textbutton translation["Back"][_preferences.language] style "log_button" text_style "settings_link" xalign 0.015 yalign 0.92 action Return()

        textbutton translation["Save_game"][_preferences.language] style "log_button" text_style "settings_link" yalign 0.92 xalign 0.5 action (FunctionCallback(on_save_callback, selected_slot), FileSave(selected_slot))
        textbutton "{size=-12}{b}x{/b} {/size}"+translation["Delete"][_preferences.language] style "log_button" text_style "settings_link" yalign 0.92 xalign 0.97 action FileDelete(selected_slot)

        vbox xalign 0.023 yalign 0.5:
            grid 1 10:
                for i in range(0, 10):
                    if i == 0:
                        textbutton translation["Auto"][_preferences.language] text_size 50 style "log_button" text_style "settings_link" action (FilePage("auto"), SetVariable("selected_slot", False))
                    else:
                        textbutton str(i) text_size 50 right_padding 50 style "log_button" text_style "settings_link" action (FilePage(i), SetVariable("selected_slot", False))

        grid 4 3 xpos 0.13 ypos 0.2 xmaximum 0.81 ymaximum 0.65:
            transpose False
            xfill True
            yfill True
            for i in range(1, 13):

                fixed:
                    add FileScreenshot(i) xpos 10 ypos 10

                    button:
                        action SetVariable("selected_slot", i)
                        xfill False
                        yfill False
                        style "save_load_button"
                        has fixed
                        text ( "%2d." % i
                               + FileTime(i, format=' %d.%m.%y, %H:%M', empty=" "+translation["Empty_slot"][_preferences.language])
                               + "\n" +FileSaveName(i)) style "file_picker_text" xpos 15 ypos 15



init python:
    _load_prompt = "load"
screen load:


    modal True tag menu

    window background get_image("gui/save_load/load_bg.jpg"):

        textbutton translation["settings"][_preferences.language] style "log_button" text_style "settings_link" xalign 0.02 yalign 0.08 action ShowMenu('preferences')
        textbutton translation["SAVE"][_preferences.language] style "log_button" text_style "settings_link" xalign 0.98 yalign 0.08 action ShowMenu('save')
        if _preferences.language == None:
            python:
                ln = 0.5 - (len("загрузить")*0.03)/2
            add get_image("gui/settings/star.png") xalign ln yalign 0.093
        else:
            python:
                ln = 0.5 - (len("load")*0.03)/2 - 0.015
            add get_image("gui/settings/star.png") xalign ln yalign 0.093
        text translation["LOAD"][_preferences.language] style "settings_link" xalign 0.5 yalign 0.08 color "#ffffff"
        if _preferences.language == None:
            python:
                ln = 0.5 + (len("загрузить")*0.03)/2
            add get_image("gui/settings/star.png") xalign ln yalign 0.093
        else:
            python:
                ln = 0.5 + (len("load")*0.03)/2 + 0.015
            add get_image("gui/settings/star.png") xalign ln yalign 0.093
        textbutton translation["Back"][_preferences.language] style "log_button" text_style "settings_link" xalign 0.015 yalign 0.92 action Return()

        textbutton translation["Load_game"][_preferences.language] style "log_button" text_style "settings_link" yalign 0.92 xalign 0.5 action (FunctionCallback(on_load_callback,selected_slot), FileLoad(selected_slot))
        textbutton "{size=-12}{b}x{/b} {/size}"+translation["Delete"][_preferences.language] style "log_button" text_style "settings_link" yalign 0.92 xalign 0.97 action FileDelete(selected_slot)

        vbox xalign 0.023 yalign 0.5:
            grid 1 10:
                for i in range(0, 10):
                    if i == 0:
                        textbutton translation["Auto"][_preferences.language] text_size 50 style "log_button" text_style "settings_link" action (FilePage("auto"), SetVariable("selected_slot", False))
                    else:
                        textbutton str(i) text_size 50 right_padding 50 style "log_button" text_style "settings_link" action (FilePage(i), SetVariable("selected_slot", False))

        grid 4 3 xpos 0.13 ypos 0.2 xmaximum 0.81 ymaximum 0.65:
            transpose False
            xfill True
            yfill True
            for i in range(1, 13):

                fixed:
                    add FileScreenshot(i) xpos 10 ypos 10

                    button:
                        action SetVariable("selected_slot", i)
                        xfill False
                        yfill False
                        style "save_load_button"
                        has fixed
                        text ( "%2d." % i
                               + FileTime(i, format=' %d.%m.%y, %H:%M', empty=" "+translation["Empty_slot"][_preferences.language])
                               + "\n" +FileSaveName(i)) style "file_picker_text" xpos 15 ypos 15

screen hentai_ach:

    if persistent.show_achievements:
        if persistent.hentai and persistent.show_hentai_ach:
            add "achievement3" at achievement_trans
            $ persistent.show_hentai_ach = False

screen collector_ach:

    if persistent.show_achievements:
        add "collector" at achievement_trans

screen preferences:

    $ translate()


    modal True tag menu

    $ bar_null = Frame(get_image("gui/settings/bar_null.png"),12,12)
    $ bar_full = Frame(get_image("gui/settings/bar_full.png"),12,12)

    window background get_image("gui/settings/preferences_bg.jpg"):

        textbutton translation["SAVE"][_preferences.language] style "log_button" text_style "settings_link" xalign 0.02 yalign 0.08 action ShowMenu('save')
        textbutton translation["LOAD"][_preferences.language] style "log_button" text_style "settings_link" xalign 0.98 yalign 0.08 action ShowMenu('load')
        if _preferences.language == None:
            python:
                ln = 0.5 - (len("настройки")*0.03)/2
            add get_image("gui/settings/star.png") xalign ln yalign 0.093
        else:
            python:
                ln = 0.5 - (len("settings")*0.03)/2 + 0.015
            add get_image("gui/settings/star.png") xalign ln yalign 0.093
        text translation["settings"][_preferences.language] style "settings_link" xalign 0.5 yalign 0.08 color "#ffffff"
        if _preferences.language == None:
            python:
                ln = 0.5 + (len("настройки")*0.03)/2
            add get_image("gui/settings/star.png") xalign ln yalign 0.093
        else:
            python:
                ln = 0.5 + (len("settings")*0.03)/2 - 0.015
            add get_image("gui/settings/star.png") xalign ln yalign 0.093
        textbutton translation["Back"][_preferences.language] style "log_button" text_style "settings_link" xalign 0.015 yalign 0.92 action Return()

        side "c b r":
            area (0.27, 0.24, 0.47, 0.70)
            viewport id "preferences":
                draggable True
                mousewheel True
                scrollbars None

                has grid 1 25 xfill True spacing 15
                text translation["Window_mode"][_preferences.language] style "settings_header" xalign 0.5
                grid 2 1 xfill True xanchor -0.05:

                    hbox:
                        if _preferences.fullscreen:
                            add get_image("gui/settings/leaf.png") ypos 0.12
                        else:
                            null width 22
                        textbutton translation["Fullscreen"][_preferences.language] style "log_button" text_style "settings_text" action Preference("display", "fullscreen")

                    hbox:
                        if not _preferences.fullscreen:
                            add get_image("gui/settings/leaf.png") ypos 0.12
                        else:
                            null width 22
                        textbutton translation["Window"][_preferences.language] style "log_button" text_style "settings_text" action Preference("display", "window")



                text translation["Skip"][_preferences.language] style "settings_header" xalign 0.5
                grid 2 1 xfill True xanchor -0.05:

                    hbox:
                        if _preferences.skip_unseen:
                            add get_image("gui/settings/leaf.png") ypos 0.12
                        else:
                            null width 22
                        textbutton translation["Skip_all"][_preferences.language] style "log_button" text_style "settings_text" action Preference("skip", "all")

                    hbox:
                        if not _preferences.skip_unseen:
                            add get_image("gui/settings/leaf.png") ypos 0.12
                        else:
                            null width 22
                        textbutton translation["Skip_seen"][_preferences.language] style "log_button" text_style "settings_text" action Preference("skip", "seen")


                text translation["Volume"][_preferences.language] style "settings_header" xalign 0.5

                grid 2 1 xfill True xanchor -0.075:
                    textbutton translation["Music_lower"][_preferences.language] style "log_button" text_style "settings_text" action Play("sound", "sound/test.ogg")
                    bar value Preference("music volume") left_bar bar_full right_bar bar_null thumb "images/misc/none.png" hover_thumb "images/misc/none.png" xmaximum 1.4 xalign -0.6 xanchor 0.0 ypos 0.2

                grid 2 1 xfill True xanchor -0.075:
                    textbutton translation["Sound"][_preferences.language] style "log_button" text_style "settings_text" action Play("sound", "sound/test.ogg")
                    bar value Preference("sound volume") left_bar bar_full right_bar bar_null thumb "images/misc/none.png" hover_thumb "images/misc/none.png" xmaximum 1.4 xalign -0.6 xanchor 0.0 ypos 0.2

                grid 2 1 xfill True xanchor -0.075:
                    textbutton translation["Ambience"][_preferences.language] style "log_button" text_style "settings_text" action Play("sound", "sound/test.ogg")
                    bar value Preference("voice volume") left_bar bar_full right_bar bar_null thumb "images/misc/none.png" hover_thumb "images/misc/none.png" xmaximum 1.4 xalign -0.6 xanchor 0.0 ypos 0.2


                text translation["Text_speed"][_preferences.language] style "settings_header" xalign 0.5
                bar value Preference("text speed") left_bar bar_full right_bar bar_null thumb "images/misc/none.png" hover_thumb "images/misc/none.png" xalign 0.5 xmaximum 0.8

                text translation["Autoforward"][_preferences.language] style "settings_header" xalign 0.5
                grid 2 1 xfill True xanchor -0.05:

                    hbox:
                        if _preferences.afm_time != 0:
                            add get_image("gui/settings/leaf.png") ypos 0.12
                        else:
                            null width 22
                        textbutton translation["Adult_content_on"][_preferences.language] style "log_button" text_style "settings_text" action Preference("auto-forward after click", "enable")

                    hbox:
                        if _preferences.afm_time == 0:
                            add get_image("gui/settings/leaf.png") ypos 0.12
                        else:
                            null width 22
                        textbutton translation["Adult_content_off"][_preferences.language] style "log_button" text_style "settings_text" action (Preference("auto-forward time", 0), Preference("auto-forward after click", "disable"))

                text translation["Autoforward_time"][_preferences.language] style "settings_header" xalign 0.5
                bar value Preference("auto-forward time") left_bar bar_full right_bar bar_null thumb "images/misc/none.png" hover_thumb "images/misc/none.png" xalign 0.5 xmaximum 0.8


                text translation["Font"][_preferences.language] style "settings_header" xalign 0.5
                grid 2 1 xfill True xanchor -0.05:
                    hbox:
                        if persistent.font_size == "small":
                            add get_image("gui/settings/leaf.png") ypos 0.12
                        else:
                            null width 22
                        textbutton translation["Normal_font"][_preferences.language] style "log_button" text_style "settings_text" action SetField(persistent, "font_size", "small")

                    hbox:
                        if not persistent.font_size == "small":
                            add get_image("gui/settings/leaf.png") ypos 0.12
                        else:
                            null width 22
                        textbutton translation["Big_font"][_preferences.language] style "log_button" text_style "settings_text" action SetField(persistent, "font_size", "large")


                text translation["Adult_content"][_preferences.language] style "settings_header" xalign 0.5
                grid 2 1 xfill True xanchor -0.05:
                    hbox:
                        if not persistent.hentai:
                            add get_image("gui/settings/leaf.png") ypos 0.12
                        else:
                            null width 22
                        textbutton translation["Adult_content_off"][_preferences.language] style "log_button" text_style "settings_text" action (SetField(persistent, "hentai", False), Play("test_two", "sound/code_breaker_2.ogg"))

                    hbox:
                        if persistent.hentai:
                            add get_image("gui/settings/leaf.png") ypos 0.12
                        else:
                            null width 22
                        textbutton translation["Adult_content_on"][_preferences.language] style "log_button" text_style "settings_text" action (SetField(persistent, "hentai", True), Play("test_one", "sound/code_breaker_1.ogg"), SetField(persistent, "show_hentai_ach", True), Show("hentai_ach"))

                text translation["Language"][_preferences.language] style "settings_header" xalign 0.5
                grid 2 1 xfill True xanchor -0.05:
                    hbox:
                        if _preferences.language == None:
                            add get_image("gui/settings/leaf.png") ypos 0.12
                        else:
                            null width 22
                        textbutton translation["Russian"][_preferences.language] style "log_button" text_style "settings_text" action (SetField(config, "window_title", "Бесконечное Лето"), SetField(persistent, "show_hentai_ach", False), Language(None), Function(reload_names), Function(stop_music), Function(renpy.utter_restart))

                    hbox:
                        if _preferences.language == "english":
                            add get_image("gui/settings/leaf.png") ypos 0.12
                        else:
                            null width 22
                        textbutton translation["English"][_preferences.language] style "log_button" text_style "settings_text" action (SetField(config, "window_title", "Everlasting Summer"), SetField(persistent, "show_hentai_ach", False), Language("english"), Function(reload_names), Function(stop_music), Function(renpy.utter_restart))

                text translation["show_achievments"][_preferences.language] style "settings_header" xalign 0.5
                grid 2 1 xfill True xanchor -0.05:

                    hbox:
                        if persistent.show_achievements:
                            add get_image("gui/settings/leaf.png") ypos 0.12
                        else:
                            null width 22
                        textbutton translation["Yes"][_preferences.language] style "log_button" text_style "settings_text" action SetField(persistent, "show_achievements", True)

                    hbox:
                        if not persistent.show_achievements:
                            add get_image("gui/settings/leaf.png") ypos 0.12
                        else:
                            null width 22
                        textbutton translation["No"][_preferences.language] style "log_button" text_style "settings_text" action SetField(persistent, "show_achievements", False)

                textbutton translation["mods"][_preferences.language] style "log_button" text_style "settings_header" xalign 0.5 action ShowMenu('mods')
                textbutton translation["filters"][_preferences.language] style "log_button" text_style "settings_header" xalign 0.5 action ShowMenu('filters')

                null

            bar value XScrollValue("preferences") left_bar "images/misc/none.png" right_bar "images/misc/none.png" thumb "images/misc/none.png" hover_thumb "images/misc/none.png"
            vbar value YScrollValue("preferences") bottom_bar "images/misc/none.png" top_bar "images/misc/none.png" thumb "images/gui/settings/vthumb.png" thumb_offset -12

screen mods:


    modal True tag menu

    $ bar_null = Frame(get_image("gui/settings/bar_null.png"),12,12)
    $ bar_full = Frame(get_image("gui/settings/bar_full.png"),12,12)

    window background get_image("gui/settings/preferences_bg.jpg"):

        if _preferences.language == None:
            python:
                ln = 0.5 - (len(translation["mods"][_preferences.language])*0.03)/2 + 0.125
            add get_image("gui/settings/star.png") xalign ln yalign 0.093
        else:
            python:
                ln = 0.5 - (len(translation["mods"][_preferences.language])*0.03)/2 + 0.11
            add get_image("gui/settings/star.png") xalign ln yalign 0.093
        text translation["mods"][_preferences.language] style "settings_link" xalign 0.5 yalign 0.08 color "#ffffff"
        if _preferences.language == None:
            python:
                ln = 0.5 + (len(translation["mods"][_preferences.language])*0.03)/2 - 0.125
            add get_image("gui/settings/star.png") xalign ln yalign 0.093
        else:
            python:
                ln = 0.5 + (len(translation["mods"][_preferences.language])*0.03)/2 - 0.11
            add get_image("gui/settings/star.png") xalign ln yalign 0.093
        textbutton translation["Back"][_preferences.language] style "log_button" text_style "settings_link" xalign 0.015 yalign 0.92 action ShowMenu('preferences')

        if mods:
            side "c b r":
                area (0.27, 0.24, 0.47, 0.70)
                viewport id "mods":
                    draggable True
                    mousewheel True
                    scrollbars None
                    yinitial 0.0

                    has grid 1 len(mods)
                    for lbl, name in sorted(mods.iteritems()):
                        textbutton name style "log_button" text_style "settings_text" action (SetField(persistent, "jump_to", lbl), SetVariable(backdrop, 'prologue'), Start())



                bar value XScrollValue("mods") left_bar "images/misc/none.png" right_bar "images/misc/none.png" thumb "images/misc/none.png" hover_thumb "images/misc/none.png"
                vbar value YScrollValue("mods") bottom_bar "images/misc/none.png" top_bar "images/misc/none.png" thumb "images/gui/settings/vthumb.png" thumb_offset -12


init 9000 python:
    if  not persistent.filters:
        persistent.filters = []
    for i in sorted(filters.keys()):
        if  not i in [item["id"] for item in persistent.filters]:
            persistent.filters += [{"id":i,"is_active":False}]
    for item in persistent.filters:
        if  item["id"] in filters and item["id"] in renpy.store.__dict__:
            if  item["is_active"]:
                renpy.store.__dict__[item["id"]]()
        else:
            persistent.filters.remove(item)

    def apply_filter(n):
        persistent.filters[n]["is_active"] = not persistent.filters[n]["is_active"]

screen filters:


    modal True tag menu

    $ bar_null = Frame(get_image("gui/settings/bar_null.png"),12,12)
    $ bar_full = Frame(get_image("gui/settings/bar_full.png"),12,12)

    window background get_image("gui/settings/preferences_bg.jpg"):

        if _preferences.language == None:
            python:
                ln = 0.5 - (len(translation["filters"][_preferences.language])*0.03)/2 + 0.05
            add get_image("gui/settings/star.png") xalign ln yalign 0.093
        else:
            python:
                ln = 0.5 - (len(translation["filters"][_preferences.language])*0.03)/2 + 0.055
            add get_image("gui/settings/star.png") xalign ln yalign 0.093
        text translation["filters"][_preferences.language] style "settings_link" xalign 0.5 yalign 0.08 color "#ffffff"
        if _preferences.language == None:
            python:
                ln = 0.5 + (len(translation["filters"][_preferences.language])*0.03)/2 - 0.05
            add get_image("gui/settings/star.png") xalign ln yalign 0.093
        else:
            python:
                ln = 0.5 + (len(translation["filters"][_preferences.language])*0.03)/2 - 0.055
            add get_image("gui/settings/star.png") xalign ln yalign 0.093
        textbutton translation["Back"][_preferences.language] style "log_button" text_style "settings_link" xalign 0.015 yalign 0.92 action ShowMenu('preferences')

        if filters:
            side "c b r":
                area (0.27, 0.24, 0.47, 0.70)
                viewport id "filters":
                    draggable True
                    mousewheel True
                    scrollbars None
                    yinitial 0.0

                    has grid 2 len(filters)
                    for i,(item) in enumerate(persistent.filters):
                        textbutton filters[item["id"]] style "log_button" text_style "settings_text" action (Function(apply_filter, i), ShowMenu('filters'))
                        if item["is_active"]:
                            add get_image("gui/settings/leaf.png") ypos 0.12
                        else:
                            null

                bar value XScrollValue("filters") left_bar "images/misc/none.png" right_bar "images/misc/none.png" thumb "images/misc/none.png" hover_thumb "images/misc/none.png"
                vbar value YScrollValue("filters") bottom_bar "images/misc/none.png" top_bar "images/misc/none.png" thumb "images/gui/settings/vthumb.png" thumb_offset -12

        textbutton translation["apply"][_preferences.language] style "log_button" text_style "settings_link" yalign 0.92 xalign 0.9 action (Function(stop_music), Function(renpy.utter_restart))



screen history:


    modal True tag menu

    python:
        screen_endings=[
        (translation["me_good"][_preferences.language],persistent.endings["main_good"], "main_good", "epilogue_main"),
        (translation["me_bad"][_preferences.language],persistent.endings["main_bad"], "main_bad", "main_bad_ending"),
        (translation["sl_good"][_preferences.language],persistent.endings["sl_good"], "sl_good", "epilogue_sl"),
        (translation["sl_bad"][_preferences.language],persistent.endings["sl_bad"], "sl_bad", "epilogue_sl"),
        (translation["dv_good"][_preferences.language],persistent.endings["dv_good"], "dv_good", "epilogue_dv"),
        (translation["dv_bad"][_preferences.language],persistent.endings["dv_bad"],"dv_bad", "epilogue_dv"),
        (translation["un_good"][_preferences.language],persistent.endings["un_good"], "un_good", "epilogue_un_good"),
        (translation["un_bad"][_preferences.language],persistent.endings["un_bad"], "un_bad", "epilogue_un_bad"),
        (translation["us_good"][_preferences.language],persistent.endings["us_good"],"us_good", "epilogue_us"),
        (translation["us_bad"][_preferences.language],persistent.endings["us_bad"], "us_bad", "epilogue_us"),
        (translation["miku"][_preferences.language],persistent.endings["mi"], "mi", "epilogue_mi"),
        (translation["yulia"][_preferences.language],persistent.endings["uv_unknown_fucken_shit"], "uv_good", "epilogue_uv_ulya"),
        (translation["all_together"][_preferences.language],persistent.endings["uv_city"], "uv_city", "epilogue_uv_city")
        ]

    $ void = "??????????"

    window background get_image("gui/settings/history_bg.jpg"):

        if _preferences.language == None:
            python:
                ln = 0.5 - (len("концовки")*0.03)/2
            add get_image("gui/settings/star.png") xalign ln yalign 0.093
        else:
            python:
                ln = 0.5 - (len("endings")*0.03)/2
            add get_image("gui/settings/star.png") xalign ln yalign 0.093
        text translation["ENDINGS"][_preferences.language] style "settings_link" xalign 0.5 yalign 0.08 color "#ffffff"
        if _preferences.language == None:
            python:
                ln = 0.5 + (len("концовки")*0.03)/2
            add get_image("gui/settings/star.png") xalign ln yalign 0.093
        else:
            python:
                ln = 0.5 + (len("endings")*0.03)/2
            add get_image("gui/settings/star.png") xalign ln yalign 0.093
        textbutton translation["Back"][_preferences.language] style "log_button" text_style "settings_link" xalign 0.015 yalign 0.92 action Return()

        side "c b r":
            area (0.23, 0.15, 0.61, 0.75)
            viewport id "history":
                draggable True
                mousewheel True
                scrollbars None
                has grid 2 13
                for name, val, ach, lbl in screen_endings:
                    if val:
                        textbutton name text_size 40 style "log_button" text_style "settings_link" ypos 15 action (SetField(persistent, "jump_to", lbl), SetField(persistent, "replay", ach), Start())
                    else:
                        text void size 40 style "settings_link" xalign 0.0 ypos 15

                    if val:
                        if _preferences.language == "english" and ach != "main_bad" and ach != "uv_city" and ach != "mi":
                            add "images/misc/ach/"+ach+"_en.png"
                        else:
                            add "images/misc/ach/"+ach+".png"
                    else:
                        add "images/misc/ach/void.png"

            $ vbar_null = Frame(get_image("gui/settings/vbar_null.png"),0,0)

            bar value XScrollValue("history") left_bar "images/misc/none.png" right_bar "images/misc/none.png" thumb "images/misc/none.png" hover_thumb "images/misc/none.png"
            vbar value YScrollValue("history") bottom_bar vbar_null top_bar vbar_null thumb "images/gui/settings/vthumb.png" thumb_offset -12


screen choice:

    modal True

    python:
        choice_colors_hover={                        
        'day': "#9dcd55",
        'night': "#3ccfa2",
        'sunset': "#dcd168",
        'prologue': "#98d8da"
                            }

        choice_colors={
        'day': "#466123",
        'night': "#145644",
        'sunset': "#69652f",
        'prologue': "#496463"
                            }

        choice_colors_selected={                        
            'day': "#2a3b15",
            'night': "#0b3027",
            'sunset': "#42401e",
            'prologue': "#2d3d3d",
                        }

    window background Frame(get_image("gui/choice/"+persistent.timeofday+"/choice_box.png"),50,50) xfill True yalign 0.5 left_padding 75 right_padding 75 bottom_padding 50 top_padding 50:

        has vbox xalign 0.5

        for caption, action, chosen in items:
            if action and caption:

                button background None:
                    action action
                    if caption in persistent.choices and caption != "Налево" and caption != "Направо" and caption != "Go left" and caption != "Go right":
                        text caption font "fonts/corbel.ttf" size 37 hover_size 37 color choice_colors_selected[persistent.timeofday] hover_color choice_colors_hover[persistent.timeofday] xcenter 0.5
                    else:
                        text caption font "fonts/corbel.ttf" size 37 hover_size 37 color choice_colors[persistent.timeofday] hover_color choice_colors_hover[persistent.timeofday] xcenter 0.5
            else:
                text caption font "fonts/corbel.ttf" size 37 color choice_colors[persistent.timeofday]

screen yesno_prompt:

    modal True

    image get_image("gui/o_rly/base.png")
    text _(message) text_align 0.5 yalign 0.46 xalign 0.5 color "#64483c" font "fonts/corbel.ttf" size 30
    textbutton translation["Yes"][_preferences.language] text_size 60 style "log_button" text_style "settings_link" yalign 0.65 xalign 0.3 action yes_action
    textbutton translation["No"][_preferences.language] text_size 60 style "log_button" text_style "settings_link" yalign 0.65 xalign 0.7 action no_action


screen say:

    window background None id "window":

        $ timeofday = persistent.timeofday

        if persistent.font_size == "large":

            imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/backward_%s.png") xpos 38 ypos 924 action ShowMenu("text_history")

            add get_image("gui/dialogue_box/"+timeofday+"/dialogue_box_large.png") xpos 174 ypos 866

            imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/hide_%s.png") xpos 1508 ypos 883 action HideInterface()
            imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/save_%s.png") xpos 1567 ypos 883 action ShowMenu('save')
            imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/menu_%s.png") xpos 1625 ypos 883 action ShowMenu('game_menu_selector')
            imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/load_%s.png") xpos 1682 ypos 883 action ShowMenu('load')

            if not config.skipping:
                imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/forward_%s.png") xpos 1768 ypos 924 action Skip()
            else:
                imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/fast_forward_%s.png") xpos 1768 ypos 924 action Skip()

            text what id "what" xpos 194 ypos 914 xmaximum 1541 size 35 line_spacing 1
            if who:
                text who id "who" xpos 194 ypos 877 size 35 line_spacing 1

        elif persistent.font_size == "small":

            imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/backward_%s.png") xpos 38 ypos 949 action ShowMenu("text_history")

            add get_image("gui/dialogue_box/"+timeofday+"/dialogue_box.png") xpos 174 ypos 916

            imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/hide_%s.png") xpos 1508 ypos 933 action HideInterface()
            imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/save_%s.png") xpos 1567 ypos 933 action ShowMenu('save')
            imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/menu_%s.png") xpos 1625 ypos 933 action ShowMenu('game_menu_selector')
            imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/load_%s.png") xpos 1682 ypos 933 action ShowMenu('load')

            if not config.skipping:
                imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/forward_%s.png") xpos 1768 ypos 949 action Skip()
            else:
                imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/fast_forward_%s.png") xpos 1768 ypos 949 action Skip()

            text what id "what" xpos 194 ypos 964 xmaximum 1541 size 28 line_spacing 2
            if who:
                text who id "who" xpos 194 ypos 931 size 28 line_spacing 2


screen nvl:

    $ timeofday = persistent.timeofday

    window background Frame(get_image("gui/choice/"+timeofday+"/choice_box.png"),50,50) xfill True yfill True yalign 0.5 left_padding 175 right_padding 175 bottom_padding 150 top_padding 150:
        has vbox
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id
                has hbox:
                    spacing 10
                if persistent.font_size == "large":
                    if who is not None:
                        text who id who_id size 35
                    text what id what_id size 35
                elif persistent.font_size == "small":
                    if who is not None:
                        text who id who_id size 28
                    text what id what_id size 28
        if items:
            vbox:
                id "menu"
                for caption, action, chosen in items:
                    if action:
                        button:
                            style "nvl_menu_choice_button"
                            action action
                            text caption style "nvl_menu_choice"
                    else:
                        text caption style "nvl_dialogue"

    imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/backward_%s.png") xpos 38 ypos 924 action ShowMenu("text_history")

    if not config.skipping:
        imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/forward_%s.png") xpos 1768 ypos 949 action Skip()
    else:
        imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/fast_forward_%s.png") xpos 1768 ypos 949 action Skip()



init python:

    g = Gallery()

    page = 0
    gallery_mode = "cg"

    g.locked_button = get_image("gui/gallery/not_opened_idle.png")
    g.navigation = False

    rows = 4
    cols = 3
    cells = rows * cols

    show_spr = False
    show_spr_emo = ""
    show_spr_dress = ""
    show_spr_acc = ""
    show_spr_menu = []
    spr_menu_spr = False
    spr_menu_dress = False
    spr_menu_emo = False
    spr_menu_acc = False

    gallery_cg = [
    "d1_food_normal", "d1_food_skolop", "d1_grasshopper",
    "d1_rena_sunset", "d1_sl_dinner", "d1_sl_dinner_0",
    "d1_uv", "d1_uv_2", "d2_2ch_beach",
    "d2_lineup", "d2_micu_lib", "d2_miku_piano",
    "d2_miku_piano2", "d2_mirror", "d2_mt_undressed",
    "d2_mt_undressed_2", "d2_slavya_forest", "d2_sovenok",
    "d2_ussr_falling", "d2_water_dan", "d3_disco",
    "d3_dv_guitar", "d3_dv_scene_1", "d3_dv_scene_2",
    "d3_sl_bathhouse", "d3_sl_dance", "d3_sl_evening",
    "d3_sl_library", "d3_soccer", "d3_un_dance",
    "d3_un_forest", "d3_us_dinner", "d3_us_library_1",
    "d3_us_library_2", "d3_us_library_3", "d3_us_library_4",
    "d3_ussr_catched", "d4_catac", "d4_catac_dv",
    "d4_catac_sl", "d4_catac_un", "d4_catac_us",
    "d4_catac_us_2", "d4_dv_mt", "d4_el_wash",
    "d4_mi_guitar", "d4_mi_sing", "d4_sh_sit",
    "d4_sh_stay", "d4_us_cancer", "d4_us_morning",
    "d4_uv", "d4_uv_1", "d5_boat",
    "d5_boat_2", "d5_cake", "d5_clubs_robot",
    "d5_cs", "d5_dv_argue", "d5_dv_argue_2",
    "d5_dv_argue_3", "d5_dv_island", "d5_dv_us_wash",
    "d5_dv_us_wash_2", "d5_dv_us_wash_3", "d5_dv_us_wash_4",
    "d5_mi", "d5_sh_us", "d5_sl_sleep",
    "d5_sl_sleep_2", "d5_strawberry_race", "d5_un_island",
    "d5_un_sleep", "d5_us_ghost", "d5_us_ghost_2",
    "d5_us_kiss", "d5_us_sit", "d5_uv",
    "d5_uv_2", "d6_dv_fight", "d6_dv_fight_2",
    "d6_dv_fight_3", "d6_dv_hentai", "d6_dv_hentai_2",
    "d6_pioneer", "d6_sl_forest", "d6_sl_forest_2",
    "d6_sl_swim", "d6_sl_hentai_1", "d6_sl_hentai_2",
    "d6_un_evening_1", "d6_un_evening_2", "d6_un_punch",
    "d6_us_film", "d6_us_night_2", "d6_uv",
    "d6_uv_2", "d7_dv", "d7_dv_2",
    "d7_pioneers_leaving", "d7_pioneers_leaving_without_us", "d7_sl_morning",
    "d7_sl_morning_2", "d7_un_hentai", "d7_un_hentai_3",
    "d7_un_suicide", "d7_uv", "day4_us_morning",
    "epilogue_dv_2", "epilogue_dv_3", "epilogue_mi_1",
    "epilogue_mi_2", "epilogue_mi_3", "epilogue_mi_4",
    "epilogue_mi_5", "epilogue_mi_6", "epilogue_mi_7",
    "epilogue_mi_8", "epilogue_mi_9", "epilogue_sl",
    "epilogue_sl_2", "epilogue_un", "epilogue_un_bad",
    "epilogue_un_good", "epilogue_us", "epilogue_us_3_a",
    "epilogue_us_alone", "epilogue_uv", "epilogue_uv_2",
    "miku_h_1_cenz", "miku_h_2_cenz", "uvao_h_cenz",
    "final_all_2", "d2_sl_swim", "epilogue_uv_uv",
    "epilogue_uv_sl", "epilogue_uv_dv", "epilogue_uv_un",
    "epilogue_uv_us", "epilogue_uv_mi"
    ]

    gallery_bg = [
    "bus_stop", "ext_aidpost_day", "ext_aidpost_night",
    "ext_bathhouse_night", "ext_beach_day", "ext_beach_night",
    "ext_beach_sunset", "ext_boathouse_day", "ext_boathouse_night",
    "ext_bus", "ext_bus_night", "ext_camp_entrance_day",
    "ext_camp_entrance_night", "ext_clubs_day", "ext_clubs_night",
    "ext_dining_hall_away_day", "ext_dining_hall_away_night", "ext_dining_hall_away_sunset",
    "ext_dining_hall_near_day", "ext_dining_hall_near_night", "ext_dining_hall_near_sunset",
    "ext_house_of_dv_day", "ext_house_of_dv_night", "ext_house_of_mt_day",
    "ext_house_of_mt_night", "ext_house_of_mt_night_without_light", "ext_house_of_mt_sunset",
    "ext_house_of_sl_day", "ext_house_of_un_day", "ext_houses_day",
    "ext_houses_sunset", "ext_island_day", "ext_island_night",
    "ext_library_day", "ext_library_night", "ext_musclub_day",
    "ext_no_bus", "ext_no_bus_night", "ext_no_bus_sunset",
    "ext_old_building_night", "ext_old_building_night_moonlight", "ext_path_day",
    "ext_path_night", "ext_path_sunset", "ext_path2_day",
    "ext_path2_night", "ext_playground_day", "ext_playground_night",
    "ext_polyana_day", "ext_polyana_night", "ext_polyana_sunset",
    "ext_road_day", "ext_road_night", "ext_road_night2",
    "ext_road_sunset", "ext_square_day", "ext_square_day_city",
    "ext_square_night", "ext_square_night_party", "ext_square_night_party2",
    "ext_square_sunset", "ext_stage_big_night", "ext_stage_normal_day",
    "ext_stage_normal_night", "ext_washstand_day", "ext_washstand2_day",
    "int_aidpost_day", "int_aidpost_day_apple", "int_aidpost_night",
    "int_bus", "int_bus_black", "int_bus_night",
    "int_bus_people_day", "int_bus_people_night", "int_catacombs_door",
    "int_catacombs_entrance", "int_catacombs_hole", "int_catacombs_living",
    "int_catacombs_living_nodoor", "int_clubs_male_day", "int_clubs_male_sunset",
    "int_clubs_male2_night", "int_clubs_male2_night_nolight", "int_dining_hall_day",
    "int_dining_hall_night", "int_dining_hall_people_day", "int_dining_hall_sunset",
    "int_house_of_dv_day", "int_house_of_dv_night", "int_house_of_mt_day",
    "int_house_of_mt_night", "int_house_of_mt_night2", "int_house_of_mt_noitem_night",
    "int_house_of_mt_sunset", "int_house_of_sl_day", "int_house_of_un_day",
    "int_house_of_un_night", "int_liaz", "int_library_day",
    "int_library_night", "int_library_night2", "int_mine",
    "int_mine_coalface", "int_mine_crossroad", "int_mine_door",
    "int_mine_exit_night_light", "int_mine_exit_night_nolight", "int_mine_exit_night_torch",
    "int_mine_halt", "int_mine_room", "int_musclub_day",
    "int_old_building_night", "intro_xx", "semen_room",
    "semen_room_window"
    ]

    gallery_sp_emo = {
    "el" : [ "normal", "grin", "smile", "scared", "shocked", "fingal", "surprise", "angry", "upset", "laugh", "serious", "sad" ],
    "uv" : [ "normal", "sad", "smile", "surprise", "laugh", "dontlike", "grin", "shocked", "upset", "surprise2", "rage", "guilty" ],
    "mi" : [ "shocked", "normal", "smile", "happy", "shy", "upset", "serious", "surprise", "sad", "dontlike", "angry", "grin", "scared", "rage", "cry", "laugh", "cry_smile" ],
    "us" : [ "grin", "surp3", "laugh", "normal", "dontlike", "laugh2", "surp2", "smile", "calml", "shy2", "angry", "fear", "upset", "sad", "surp1", "shy", "cry2", "cry" ],
    "sh" : [ "normal", "normal_smile", "upset", "serious", "laugh", "rage", "scared", "cry", "surprise", "smile" ],
    "mt" : [ "normal", "smile", "surprise", "rage", "angry", "sad", "grin", "laugh", "scared", "shocked" ],
    "un" : [ "normal", "surprise", "shy", "smile", "scared", "smile2", "serious", "laugh", "sad", "shocked", "smile3", "angry", "cry", "grin", "cry_smile", "rage", "evil_smile" ],
    "sl" : [ "normal", "smile", "surprise", "smile2", "angry", "laugh", "happy", "serious", "shy", "sad", "scared", "tender" ],
    "dv" : [ "angry", "normal", "smile", "sad", "rage", "grin", "guilty", "shy", "laugh", "surprise", "shocked", "scared", "cry" ],
    "pi" : [ "normal", "smile" ],
    "cs" : [ "normal", "smile", "shy" ],
    "mz" : [ "normal", "angry", "bukal", "shy", "smile", "rage", "laugh" ]
    }

    gallery_sp_dress = {
    "dv" : [ "pioneer", "pioneer2", "swim" ],
    "sl" : [ "pioneer", "swim", "sport", "dress" ],
    "un" : [ "pioneer", "swim", "sport", "dress" ],
    "us" : [ "pioneer", "swim", "sport", "dress" ],
    "mt" : [ "pioneer", "dress", "swim" ],
    "el" : [ "pioneer" ],
    "mi" : [ "pioneer", "swim" ],
    "mz" : [ "pioneer" ],
    "uv" : [ "" ],
    "pi" : [ "" ],
    "sh" : [ "" ],
    "cs" : [ "" ]
    }

    gallery_sp_acc = {
    "cs" : [ "stethoscope", "glasses" ],
    "mt" : [ "panama" ],
    "mz" : [ "glasses" ]
    }

    for cg in gallery_cg:
        g.button(cg)
        g.unlock_image("cg "+cg)
        g.Action(cg)

    for bg in gallery_bg:
        g.button(bg)
        g.unlock_image("bg "+bg)
        g.Action(bg)

    g.transition = fade

    def collect_all():
        if persistent.collector:
            found = False
            for i in gallery_cg:
                found = False
                for k in persistent._seen_images:
                    if i in k:
                        found = True
                        break
            if not found:
                return
            for i in gallery_bg:
                found = False
                for k in persistent._seen_images:
                    if i in k:
                        found = True
                        break
            if not found:
                return
            
            renpy.show_screen("collector_ach")
            steam.unlock_achievement("ACH_COLLECTOR")
            steam.push_achievement()
            persistent.collector = False


screen gallery:


    modal True tag menu

    $ gallery_table = []

    frame background get_image("gui/settings/history_bg.jpg"):

        if gallery_mode == "cg":
            textbutton translation["MUSIC"][_preferences.language] style "log_button" text_style "settings_link" xalign 0.02 yalign 0.08 action (SetVariable('page', 0), ShowMenu("music_room"))
            textbutton translation["BG"][_preferences.language] style "log_button" text_style "settings_link" xalign 0.98 yalign 0.08 action (SetVariable('gallery_mode', "bg"), SetVariable('page', 0), ShowMenu("gallery"))
            if _preferences.language == None:
                python:
                    ln = 0.5 - (len("иллюстрации")*0.03)/2 - 0.015
                add get_image("gui/settings/star.png") xalign ln yalign 0.093
            else:
                python:
                    ln = 0.5 - (len("CG")*0.03)/2 - 0.03
                add get_image("gui/settings/star.png") xalign ln yalign 0.093
            text translation["CG"][_preferences.language] style "settings_link" xalign 0.5 yalign 0.08 color "#ffffff"
            if _preferences.language == None:
                python:
                    ln = 0.5 + (len("иллюстрации")*0.03)/2 + 0.015
                add get_image("gui/settings/star.png") xalign ln yalign 0.093
            else:
                python:
                    ln = 0.5 + (len("CG")*0.03)/2 + 0.03
                add get_image("gui/settings/star.png") xalign ln yalign 0.093
            $ gallery_table = gallery_cg
        elif gallery_mode == "bg":
            textbutton translation["CG"][_preferences.language] style "log_button" text_style "settings_link" xalign 0.02 yalign 0.08 action (SetVariable('gallery_mode', "cg"), SetVariable('page', 0), ShowMenu("gallery"))
            textbutton translation["SPRITES"][_preferences.language] style "log_button" text_style "settings_link" xalign 0.98 yalign 0.08 action (SetVariable('page', 0), ShowMenu("gallery_sp"))
            if _preferences.language == None:
                python:
                    ln = 0.5 - (len("фоны")*0.03)/2 - 0.03
                add get_image("gui/settings/star.png") xalign ln yalign 0.093
            else:
                python:
                    ln = 0.5 - (len("bg")*0.03)/2 - 0.03
                add get_image("gui/settings/star.png") xalign ln yalign 0.093
            text translation["BG"][_preferences.language] style "settings_link" xalign 0.5 yalign 0.08 color "#ffffff"
            if _preferences.language == None:
                python:
                    ln = 0.5 + (len("фоны")*0.03)/2 + 0.03
                add get_image("gui/settings/star.png") xalign ln yalign 0.093
            else:
                python:
                    ln = 0.5 + (len("bg")*0.03)/2 + 0.03
                add get_image("gui/settings/star.png") xalign ln yalign 0.093
            $ gallery_table = gallery_bg

        textbutton translation["Back"][_preferences.language] style "log_button" text_style "settings_link" xalign 0.015 yalign 0.92 action Return()

        if gallery_mode == "cg" or gallery_mode == "bg":
            grid rows cols xpos 0.09 ypos 0.18:
                $ i = 0
                $ next_page = page + 1
                if next_page > int(len(gallery_table)/cells):
                    $ next_page = 0
                for cg in gallery_table:
                    $ i += 1
                    if i <= (page+1)*cells and i>page*cells:
                        python:
                            if gallery_mode == "cg":
                                _t = im.Crop("images/cg/"+cg+".jpg" , (0,0,1920,1080))
                            elif gallery_mode == "bg":
                                _t = im.Crop("images/bg/"+cg+".jpg" , (0,0,1920,1080))
                            th = im.Scale(_t, 320, 180)
                            img = im.Composite((336,196),(8,8),im.Alpha(th,0.9),(0,0),im.Image(get_image("gui/gallery/thumbnail_idle.png")))
                            imgh = im.Composite((336,196),(8,8),th,(0,0),im.Image(get_image("gui/gallery/thumbnail_hover.png")))
                        add g.make_button(cg, get_image("gui/gallery/blank.png"), None, imgh, img, style="blank_button", bottom_margin=50, right_margin=50)
                for j in range(i, (page+1)*cells):
                    null

            if page != 0:
                imagebutton auto get_image("gui/dialogue_box/day/backward_%s.png") yalign 0.5 xalign 0.01 action (SetVariable('page', page-1), ShowMenu("gallery"))
            imagebutton auto get_image("gui/dialogue_box/day/forward_%s.png") yalign 0.5 xalign 0.99 action (SetVariable('page', next_page), ShowMenu("gallery"))

            python:
                pages = str(page+1)+"/"+str(len(gallery_table)/cells+1)
            text pages style "settings_link" xalign 0.985 yalign 0.92

screen sprite_menu:

    modal True

    $ show_spr_menu = []

    if spr_menu_acc:
        for k in gallery_sp_acc.values():
            for acc in k:
                $ found = False
                for i in persistent._seen_images:
                    if show_spr in i and show_spr_emo in i and (show_spr_dress or show_spr) in i and acc in i:
                        if not found:
                            if (show_spr, acc) not in show_spr_menu:
                                $ show_spr_menu.append((show_spr, acc))
                                $ found = True
                $ found = False

    elif spr_menu_emo:
        for k in gallery_sp_emo.values():
            for emo in k:
                $ found = False
                for i in persistent._seen_images:
                    if show_spr in i and emo in i and (show_spr_dress or show_spr) in i:
                        if not found:
                            if (show_spr, emo) not in show_spr_menu:
                                $ show_spr_menu.append((show_spr, emo))
                                $ found = True
                $ found = False

    elif spr_menu_dress:
        for k in gallery_sp_dress.values():
            for dress in k:
                $ found = False
                for i in persistent._seen_images:
                    if dress in i and show_spr in i:
                        if not found:
                            if (show_spr, dress) not in show_spr_menu:
                                $ show_spr_menu.append((show_spr, dress))
                                $ found = True
                $ found = False

    elif spr_menu_spr:
        for spr in gallery_sp_emo.keys():
            $ found = False
            for i in persistent._seen_images:
                if spr in i:
                    if not found:
                        if (spr, spr) not in show_spr_menu:
                            $ show_spr_menu.append((spr, spr))
                            $ found = True
            $ found = False


    button style "blank_button" xpos 0 ypos 0 xfill True yfill True action (Hide('sprite_menu'), ShowMenu("gallery_sp"))

    frame background Frame(get_image("gui/choice/day/choice_box.png"),50,50) xfill True yalign 0.5 left_padding 75 right_padding 75 bottom_padding 50 top_padding 50:

        has vbox xalign 0.5

        for i in show_spr_menu:
            if spr_menu_acc:
                textbutton translation[i[1]][_preferences.language] style "log_button" text_style "sprite_menu" action (SetVariable('show_spr_acc', i[1]), Hide('sprite_menu'), ShowMenu("gallery_sp"))
            elif spr_menu_emo:
                textbutton translation[i[1]][_preferences.language] style "log_button" text_style "sprite_menu" action (SetVariable('show_spr_emo', i[1]), Hide('sprite_menu'), ShowMenu("gallery_sp"))
            elif spr_menu_dress:
                textbutton translation[i[1]][_preferences.language] style "log_button" text_style "sprite_menu" action (SetVariable('show_spr_dress', i[1]), Hide('sprite_menu'), ShowMenu("gallery_sp"))
            elif spr_menu_spr:
                textbutton translation[i[1]][_preferences.language] style "log_button" text_style "sprite_menu" action (SetVariable('show_spr', i[1]), Hide('sprite_menu'), ShowMenu("gallery_sp"))

        if spr_menu_acc:
            textbutton "x" style "log_button" text_style "sprite_menu" action (SetVariable('show_spr_acc', False), Hide('sprite_menu'), ShowMenu("gallery_sp"))


screen gallery_sp:


    modal True tag menu

    $ persistent.sprite_time = "day"

    frame background get_image("gui/settings/history_bg.jpg"):

        textbutton translation["BG"][_preferences.language] style "log_button" text_style "settings_link" xalign 0.02 yalign 0.08 action (SetVariable('gallery_mode', "bg"), SetVariable('page', 0), SetVariable('show_spr', False), ShowMenu("gallery"))
        textbutton translation["MUSIC"][_preferences.language] style "log_button" text_style "settings_link" xalign 0.98 yalign 0.08 action (SetVariable('page', 0), SetVariable('show_spr', False), ShowMenu("music_room"))
        if _preferences.language == None:
            python:
                ln = 0.5 - (len("спрайты")*0.03)/2 - 0.015
            add get_image("gui/settings/star.png") xalign ln yalign 0.093
        else:
            python:
                ln = 0.5 - (len("sprites")*0.03)/2 + 0.015
            add get_image("gui/settings/star.png") xalign ln yalign 0.093
        text translation["SPRITES"][_preferences.language] style "settings_link" xalign 0.5 yalign 0.08 color "#ffffff"
        if _preferences.language == None:
            python:
                ln = 0.5 + (len("спрайты")*0.03)/2 + 0.015
            add get_image("gui/settings/star.png") xalign ln yalign 0.093
        else:
            python:
                ln = 0.5 + (len("sprites")*0.03)/2 - 0.015
            add get_image("gui/settings/star.png") xalign ln yalign 0.093
        textbutton translation["Back"][_preferences.language] style "log_button" text_style "settings_link" xalign 0.015 yalign 0.92 action (Return(), SetVariable('show_spr', False))




        textbutton translation["Sprites2"][_preferences.language] text_size 30 style "log_button" text_style "settings_link" xalign 0.02 yalign 0.28 action (ShowMenu("sprite_menu"), SetVariable('spr_menu_spr', True), SetVariable('spr_menu_dress', False), SetVariable('spr_menu_emo', False), SetVariable('show_spr', False), SetVariable('show_spr_dress', False), SetVariable('show_spr_emo', False), SetVariable('show_spr_acc', False), SetVariable('spr_menu_acc', False))

        if show_spr:
            text translation[show_spr][_preferences.language] size 30 style "settings_link" xalign 0.03 yalign 0.35

            textbutton translation["Dress2"][_preferences.language] text_size 30 style "log_button" text_style "settings_link" xalign 0.02 yalign 0.42 action (ShowMenu("sprite_menu"), SetVariable('show_spr_emo', False), SetVariable('spr_menu_dress', True), SetVariable('spr_menu_emo', False), SetVariable('show_spr_dress', False), SetVariable('show_spr_acc', False), SetVariable('spr_menu_acc', False))

            if show_spr_dress or show_spr in ('pi', 'sh', 'cs', 'uv'):
                if show_spr_dress:
                    text translation[show_spr_dress][_preferences.language] size 30 style "settings_link" xalign 0.03 yalign 0.49

                textbutton translation["Emotion2"][_preferences.language] text_size 30 style "log_button" text_style "settings_link" xalign 0.02 yalign 0.56 action (ShowMenu("sprite_menu"), SetVariable('spr_menu_emo', True), SetVariable('spr_menu_acc', False), SetVariable('show_spr_emo', False), SetVariable('show_spr_acc', False))

                if show_spr_emo:
                    text translation[show_spr_emo][_preferences.language] size 30 style "settings_link" xalign 0.03 yalign 0.63

                    if show_spr in ('mt', 'mz', 'cs'):
                        textbutton translation["Accessory"][_preferences.language] text_size 30 style "log_button" text_style "settings_link" xalign 0.02 yalign 0.7 action (ShowMenu("sprite_menu"), SetVariable('spr_menu_acc', True), SetVariable('show_spr_acc', False))

                        if show_spr_acc:
                            text translation[show_spr_acc][_preferences.language] size 30 style "settings_link" xalign 0.03 yalign 0.77



        if show_spr and show_spr_emo and show_spr_acc:
            if show_spr_dress:
                add show_spr+" "+show_spr_emo+" "+show_spr_acc+" "+show_spr_dress xalign 0.5
            else:
                add show_spr+" "+show_spr_emo+" "+show_spr_acc xalign 0.5
        elif show_spr and show_spr_emo:
            if show_spr_dress:
                add show_spr+" "+show_spr_emo+" "+show_spr_dress xalign 0.5
            else:
                add show_spr+" "+show_spr_emo xalign 0.5


init python:

    music_box = {
    "Opening Theme" : "sound/music/everlasting_summer_op_edition.ogg",
    "A Promise From Distant Days" : "sound/music/a_promise_from_distant_days.ogg",
    "A Promise From Distant Days v.2" : "sound/music/a_promise_from_distant_days_v2.ogg",
    "Afterword" : "sound/music/afterword.ogg",
    "Always Ready" : "sound/music/always_ready.ogg",
    "Awakening Power" : "sound/music/awakening_power.ogg",
    "Blow With The Fires" : "sound/music/blow_with_the_fires.ogg",
    "Confession" : "sound/music/confession.ogg",
    "Dance Of Fireflies" : "sound/music/dance_of_fireflies.ogg",
    "Doomed To Be Defeated" : "sound/music/doomed_to_be_defeated.ogg",
    "Door To Nightmare" : "sound/music/door_to_nightmare.ogg",
    "Drown" : "sound/music/drown.ogg",
    "Eat Some Trouble" : "sound/music/eat_some_trouble.ogg",
    "Eternal Longing" : "sound/music/eternal_longing.ogg",
    "Everlasting Summer" : "sound/music/everlasting_summer.ogg",
    "Feeling Good" : "sound/music/feeling_good.ogg",
    "Faceless" : "sound/music/faceless.ogg",
    "Farewell To The Past (Short ver.)" : "sound/music/farewell_to_the_past_short.ogg",
    "Farewell To The Past" : "sound/music/farewell_to_the_past.ogg",
    "Forest Maiden" : "sound/music/forest_maiden.ogg",
    "Gentle Predator" : "sound/music/gentle_predator.ogg",
    "Get To Know Me Better" : "sound/music/get_to_know_me_better.ogg",
    "Glimmering Coals" : "sound/music/glimmering_coals.ogg",
    "Goodbye Home Shores" : "sound/music/goodbye_home_shores.ogg",
    "Heather" : "sound/music/heather.ogg",
    "I Don't Blame You" : "sound/music/i_dont_blame_you.ogg",
    "I Want To Play" : "sound/music/i_want_to_play.ogg",
    "Into The Unknown" : "sound/music/into_the_unknown.ogg",
    "Just Think" : "sound/music/just_think.ogg",
    "Let's Be Friends" : "sound/music/lets_be_friends.ogg",
    "Lightness" : "sound/music/lightness.ogg",
    "Lightness (Radio edit)" : "sound/music/lightness_radio.ogg",
    "Meet Me There" : "sound/music/meet_me_there.ogg",
    "Memories" : "sound/music/memories.ogg",
    "Memories (Piano Outdoors)" : "sound/music/memories_piano_outdoors.ogg",
    "Miku Song" : "sound/music/miku_song_voice.ogg",
    "My Daily Life" : "sound/music/my_daily_life.ogg",
    "Mystery Girl" : "sound/music/mystery_girl.ogg",
    "No Tresspassing" : "sound/music/no_tresspassing.ogg",
    "Orchid" : "sound/music/orchid.ogg",
    "Pile" : "sound/music/pile.ogg",
    "Raindrops" : "sound/music/raindrops.ogg",
    "Reflection On Water" : "sound/music/reflection_on_water.ogg",
    "Reminiscences" : "sound/music/reminiscences.ogg",
    "Revenga" : "sound/music/revenga.ogg",
    "Scarytale" : "sound/music/scarytale.ogg",
    "She Is Kind" : "sound/music/she_is_kind.ogg",
    "Silhouette In Sunset" : "sound/music/silhouette_in_sunset.ogg",
    "Smooth Machine" : "sound/music/smooth_machine.ogg",
    "So Good To Be Careless" : "sound/music/so_good_to_be_careless.ogg",
    "Sparkles" : "sound/music/sparkles.ogg",
    "Sunny Day" : "sound/music/sunny_day.ogg",
    "Sweet Darkness" : "sound/music/sweet_darkness.ogg",
    "Take Me Beautifully" : "sound/music/take_me_beautifully.ogg",
    "That's Our Madhouse" : "sound/music/that_s_our_madhouse.ogg",
    "Timid Girl" : "sound/music/timid_girl.ogg",
    "Torture" : "sound/music/torture.ogg",
    "Trapped In Dreams" : "sound/music/trapped_in_dreams.ogg",
    "Tried To Bring It Back" : "sound/music/tried_to_bring_it_back.ogg",
    "Two Glasses Of Melancholy" : "sound/music/two_glasses_of_melancholy.ogg",
    "Waltz Of Doubts" : "sound/music/waltz_of_doubts.ogg",
    "Went Fishing Caught A Girl" : "sound/music/went_fishing_caught_a_girl.ogg",
    "What Do You Think Of Me" : "sound/music/what_do_you_think_of_me.ogg",
    "You Lost Me" : "sound/music/you_lost_me.ogg",
    "You Won't Let Me Down" : "sound/music/you_won_t_let_me_down.ogg",
    "Your Bright Side" : "sound/music/your_bright_side.ogg",
    "410" : "sound/music/410.ogg"
    }

    mr = MusicRoom(fadeout=1.0)

    for name in music_box.values():
        mr.add(name)


screen music_room:


    modal True tag menu

    frame background get_image("gui/settings/history_bg.jpg"):

        textbutton translation["SPRITES"][_preferences.language] style "log_button" text_style "settings_link" xalign 0.02 yalign 0.08 action (ShowMenu("gallery_sp"), SetVariable('page', 0))
        textbutton translation["CG"][_preferences.language] style "log_button" text_style "settings_link" xalign 0.98 yalign 0.08 action (SetVariable('gallery_mode', "cg"), ShowMenu("gallery"), SetVariable('page', 0))
        if _preferences.language == None:
            python:
                ln = 0.5 - (len("музыка")*0.03)/2 - 0.015
            add get_image("gui/settings/star.png") xalign ln yalign 0.093
        else:
            python:
                ln = 0.5 - (len("music")*0.03)/2 - 0.015
            add get_image("gui/settings/star.png") xalign ln yalign 0.093
        text translation["MUSIC"][_preferences.language] style "settings_link" xalign 0.5 yalign 0.08 color "#ffffff"
        if _preferences.language == None:
            python:
                ln = 0.5 + (len("музыка")*0.03)/2 + 0.015
            add get_image("gui/settings/star.png") xalign ln yalign 0.093
        else:
            python:
                ln = 0.5 + (len("music")*0.03)/2 + 0.015
            add get_image("gui/settings/star.png") xalign ln yalign 0.093

        textbutton translation["Back"][_preferences.language] style "log_button" text_style "settings_link" xalign 0.015 yalign 0.92 action Return()

        side "c b r":
            area (0.23, 0.15, 0.61, 0.75)
            viewport id "music_box":
                draggable True
                mousewheel True
                scrollbars None

                has grid 1 len(music_box)
                for name, track in sorted(music_box.iteritems()):
                    textbutton name style "log_button" text_style "music_link" action mr.Play(track)

            $ vbar_null = Frame(get_image("gui/settings/vbar_null.png"),0,0)

            bar value XScrollValue("music_box") left_bar "images/misc/none.png" right_bar "images/misc/none.png" thumb "images/misc/none.png" hover_thumb "images/misc/none.png"
            vbar value YScrollValue("music_box") bottom_bar vbar_null top_bar vbar_null thumb "images/gui/settings/vthumb.png" thumb_offset -12




    on "replaced" action Play("music", "sound/music/blow_with_the_fires.ogg")

init python:
    def force_quit():
        renpy.quit()

screen quit:


    modal True tag menu

    add get_image("maps/exit.jpg")

    text translation["Quit_confirm"][_preferences.language] style "settings_link" size 60 text_align 0.5 xalign 0.7 yalign 0.33 color "#031a68" antialias True kerning 2

    textbutton translation["Yes"][_preferences.language] text_size 70 style "log_button" text_style "settings_link" xalign 0.51 yalign 0.55 text_color "#3b5bc2" text_hover_color "#ff7b02" action Quit(confirm=False)
    textbutton translation["No"][_preferences.language] text_size 70 style "log_button" text_style "settings_link" xalign 0.85 yalign 0.55 text_color "#3b5bc2" text_hover_color "#ff7b02" action Return()

label _compat_confirm_quit:
    $ renpy.call_screen('quit')









init -3 python:




    style.readback_window = Style(style.nvl_window)
    '''style.readback_window.xmaximum = 760
    style.readback_window.ymaximum = 500
    style.readback_window.align = (.5, .5)'''

    style.readback_frame.background = None
    style.readback_frame.xpadding = 10
    style.readback_frame.xmargin = 5
    style.readback_frame.ymargin = 5

    style.readback_text.color = "#ffdd7d"

    '''style.create("readback_button", "readback_text")
    style.readback_button.background = None
    
    style.create("readback_button_text", "readback_text")
    style.readback_button_text.selected_color = "#f12"
    style.readback_button_text.hover_color = "#f12"'''

    style.readback_label_text.bold = True
    style.readback_label_text.color = "#ffffff"


    config.locked = False 


    config.readback_buffer_length = 100 
    config.readback_full = False 
    config.readback_disallowed_tags = ["size"] 
    config.readback_choice_prefix = ">> "   


    config.locked = True

init -2 python:


    class ReadbackADVCharacter(ADVCharacter):
        def do_done(self, who, what, who_args):
            store_say(who, what, who_args)
            store.current_voice = ''
            return

    class ReadbackNVLCharacter(NVLCharacter):
        def do_done(self, who, what, who_args):
            store_say(who, what, who_args)
            store.current_voice = ''
            return


    def say_wrapper(who, what, **kwargs):
        store_current_line(who, what)
        return renpy.show_display_say(who, what, **kwargs)

    config.nvl_show_display_say = say_wrapper

    adv = ReadbackADVCharacter(show_function=say_wrapper)
    nvl = ReadbackNVLCharacter()
    NVLCharacter = ReadbackNVLCharacter


    readback_buffer = []
    current_line = None
    current_voice = None

    def store_say(who, what, who_args):
        say_color = " "
        try:
            say_color = '#%02x%02x%02x' % who_args['color'][0:3]
        except:
            pass
        global readback_buffer, current_voice
        new_line = (who, preparse_say_for_store(what), current_voice, say_color)
        readback_buffer = readback_buffer + [new_line]
        readback_prune()

    def store_current_line(who, what):
        global current_line, current_voice
        current_line = (who, preparse_say_for_store(what), current_voice, " ")


    disallowed_tags_regexp = ""
    for tag in config.readback_disallowed_tags:
        if disallowed_tags_regexp != "":
            disallowed_tags_regexp += "|"
        disallowed_tags_regexp += "{"+tag+"=.*?}|{"+tag+"}|{/"+tag+"}"

    import re
    remove_tags_expr = re.compile(disallowed_tags_regexp) 
    def preparse_say_for_store(input):
        global remove_tags_expr
        if input:
            return re.sub(remove_tags_expr, "", input)

    def readback_prune():
        global readback_buffer
        while len(readback_buffer) > config.readback_buffer_length:
            del readback_buffer[0]











screen text_history:
    tag menu


    if not current_line and len(readback_buffer) == 0 and d2_cardgame_block_rollback:
        $ lines_to_show = []

    elif not current_line and len(readback_buffer) == 0:
        $ lines_to_show = []

    elif current_line and len(readback_buffer) == 0:
        $ lines_to_show = [current_line]

    elif current_line and not ( current_line == readback_buffer[-1] or False 
            if len(readback_buffer) == 1 else (current_line == readback_buffer[-2]) ):
        $ lines_to_show = readback_buffer

    else:
        $ lines_to_show = readback_buffer




    button style "blank_button" xpos 0 ypos 0 xfill True yfill True action Return()

    window background Frame(get_image("gui/choice/"+persistent.timeofday+"/choice_box.png"),50,50) xmaximum 0.83 xalign 0.01 yalign 0.01 left_padding 75 right_padding 75 bottom_padding 50 top_padding 50:
        style_group "readback"

        side "c t r":
            viewport id "readback":
                draggable True
                mousewheel True
                scrollbars None
                yinitial 1.0





                has vbox
                null height 10

                python:
                    count=1
                    total=0

                    mass = lines_to_show
                    for i in mass:
                        if i[1]:
                            if not i[2]:
                                total+=1


                for line in lines_to_show:

                    if line[0] and line[0] != " ":

                        if line[3] and line[3] != " ":
                            python:
                                sayer =  line[0]



                            text sayer color line[3]

                        else:
                            text line[0]

                    if line[1]:

                        if not line[2]:
                            python:
                                cn=total-count                   
                                count+=1
                            if persistent.font_size == "small":
                                textbutton __(line[1]) text_size 28 style "log_button" text_style "log_button_text" action FunctionCallback(do_rollback,cn)
                            elif persistent.font_size == "large":
                                textbutton __(line[1]) text_size 35 style "log_button" text_style "log_button_text" action FunctionCallback(do_rollback,cn)
                            else:
                                null height 1


                        else:
                            textbutton line[1] action Play("voice", line[2] )

                    null height 10
                python:
                    count=None
                    total=None
                    mass=None


        $ vbar_null = Frame(get_image("gui/settings/vbar_null.png"),0,0)

        bar value XScrollValue("readback") left_bar "images/misc/none.png" right_bar "images/misc/none.png" thumb "images/misc/none.png" hover_thumb "images/misc/none.png"
        vbar value YScrollValue("readback") bottom_bar vbar_null top_bar vbar_null thumb "images/gui/settings/vthumb.png" thumb_offset -12 xalign 1.0

screen notify(message):

    modal False
    zorder 100

    python:
        choice_colors_hover={
        'day': "#9dcd55",
        'night': "#3ccfa2",
        'sunset': "#dcd168",
        'prologue': "#98d8da"
                            }
        choice_colors={
        'day': "#466123",
        'night': "#145644",
        'sunset': "#69652f",
        'prologue': "#496463"
                            }


    if not config.skipping:
        window background Frame(get_image("gui/choice/"+persistent.timeofday+"/choice_box.png"),50,50) xmaximum 0.4 xalign 0.01 yalign 0.01 left_padding 75 right_padding 75 bottom_padding 50 top_padding 50:
            text message font "fonts/corbel.ttf" size 37 color "#ffdd7d"
    else:
        timer 0.01 action Hide('notify')



    key "dismiss" action (Hide('notify'), Return())
    key "toggle_skip" action (Hide('notify'), Return())
    key "skip" action (Hide('notify'), Return())

  # Decompiled by unrpyc_v1.2.0-alpha: https://github.com/CensoredUsername/unrpyc
