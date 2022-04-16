# -*- coding: utf-8 -*-
import os
import re
import socket
import subprocess
from libqtile import qtile
from libqtile.config import Click, Drag, Group, KeyChord, Key, Match, Screen
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from libqtile.lazy import lazy
from typing import List  # noqa: F401

mod = "mod4"                                     
myTerm = "alacritty"                             

keys = [
         ### The essentials
         Key([mod], "Return",
             lazy.spawn("alacritty"),
             desc='Launches My Terminal'
             ),
         Key([mod, "shift"], "Return",
             # lazy.spawn("dmenu_run -p 'Run: '"),
             lazy.spawn("rofi -show drun -config ~/.config/rofi/themes/center.rasi -display-drun \"Run: \" -drun-display-format \"{name}\""),
             desc='Run Launcher'
             ),
         Key([mod], "Tab",
             lazy.next_layout(),
             desc='Toggle through layouts'
             ),
         Key([mod, "shift"], "c",
             lazy.window.kill(),
             desc='Kill active window'
             ),
         Key([mod, "shift"], "r",
             lazy.restart(),
             desc='Restart Qtile'
             ),
         Key([mod, "shift"], "q",
             lazy.shutdown(),
             desc='Shutdown Qtile'
             ),
         ### Switch focus to specific monitor (out of three)
         Key([mod], "w",
             lazy.to_screen(0),
             desc='Keyboard focus to monitor 1'
             ),
         Key([mod], "e",
             lazy.to_screen(1),
             desc='Keyboard focus to monitor 2'
             ),
         Key([mod], "r",
             lazy.to_screen(2),
             desc='Keyboard focus to monitor 3'
             ),
         ### Switch focus of monitors
         Key([mod], "period",
             lazy.next_screen(),
             desc='Move focus to next monitor'
             ),
         Key([mod], "comma",
             lazy.prev_screen(),
             desc='Move focus to prev monitor'
             ),
         ### Treetab controls
          Key([mod, "shift"], "h",
             lazy.layout.move_left(),
             desc='Move up a section in treetab'
             ),
         Key([mod, "shift"], "l",
             lazy.layout.move_right(),
             desc='Move down a section in treetab'
             ),
         ### Window controls
         Key([mod], "j",
             lazy.layout.down(),
             desc='Move focus down in current stack pane'
             ),
         Key([mod], "k",
             lazy.layout.up(),
             desc='Move focus up in current stack pane'
             ),
         Key([mod, "shift"], "j",
             lazy.layout.shuffle_down(),
             lazy.layout.section_down(),
             desc='Move windows down in current stack'
             ),
         Key([mod, "shift"], "k",
             lazy.layout.shuffle_up(),
             lazy.layout.section_up(),
             desc='Move windows up in current stack'
             ),
         Key([mod], "h",
             lazy.layout.shrink(),
             lazy.layout.decrease_nmaster(),
             desc='Shrink window (MonadTall), decrease number in master pane (Tile)'
             ),
         Key([mod], "l",
             lazy.layout.grow(),
             lazy.layout.increase_nmaster(),
             desc='Expand window (MonadTall), increase number in master pane (Tile)'
             ),
         Key([mod], "n",
             lazy.layout.normalize(),
             desc='normalize window size ratios'
             ),
         Key([mod], "m",
             lazy.layout.maximize(),
             desc='toggle window between minimum and maximum sizes'
             ),
         Key([mod, "shift"], "f",
             lazy.window.toggle_floating(),
             desc='toggle floating'
             ),
         Key([mod], "f",
             lazy.window.toggle_fullscreen(),
             desc='toggle fullscreen'
             ),
         ### Stack controls
         Key([mod, "shift"], "Tab",
             lazy.layout.rotate(),
             lazy.layout.flip(),
             desc='Switch which side main pane occupies (XmonadTall)'
             ),
          Key([mod], "space",
             lazy.layout.next(),
             desc='Switch window focus to other pane(s) of stack'
             ),
         Key([mod, "shift"], "space",
             lazy.layout.toggle_split(),
             desc='Toggle between split and unsplit sides of stack'
             ),
         # Dmenu scripts launched using the key chord SUPER+p followed by 'key'
         KeyChord([mod], "p", [
             Key([], "e",
                 lazy.spawn("./dmscripts/dm-confedit"),
                 desc='Choose a config file to edit'
                 ),
             Key([], "i",
                 lazy.spawn("./dmscripts/dm-maim"),
                 desc='Take screenshots via dmenu'
                 ),
             Key([], "k",
                 lazy.spawn("./dmscripts/dm-kill"),
                 desc='Kill processes via dmenu'
                 ),
             Key([], "l",
                 lazy.spawn("./dmscripts/dm-logout"),
                 desc='A logout menu'
                 ),
             Key([], "m",
                 lazy.spawn("./dmscripts/dm-man"),
                 desc='Search manpages in dmenu'
                 ),
             Key([], "o",
                 lazy.spawn("./dmscripts/dm-bookman"),
                 desc='Search your qutebrowser bookmarks and quickmarks'
                 ),
             Key([], "r",
                 lazy.spawn("./dmscripts/dm-reddit"),
                 desc='Search reddit via dmenu'
                 ),
             Key([], "s",
                 lazy.spawn("./dmscripts/dm-websearch"),
                 desc='Search various search engines via dmenu'
                 ),
             Key([], "p",
                 lazy.spawn("passmenu"),
                 desc='Retrieve passwords with dmenu'
                 )         
         ])
]
               
group_names = [("", {'layout': 'monadtall'}),
               ("", {'layout': 'monadtall'}),
               ("", {'layout': 'monadtall'}),
               ("", {'layout': 'monadtall'}),
               ("", {'layout': 'monadtall'}),
               ("", {'layout': 'monadtall'}),
               ("", {'layout': 'monadtall'}),
               ("", {'layout': 'monadtall'}),
               ("", {'layout': 'floating'})]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))        
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name)))

layout_theme = {"border_width": 1,
                "margin": 10,
                "border_focus": "f22516",
                "border_normal": "1D2330"
                }

layouts = [
    layout.MonadTall(**layout_theme),
    layout.Floating(**layout_theme)
    #layout.MonadWide(**layout_theme),
    #layout.Bsp(**layout_theme),
    #layout.Stack(stacks=2, **layout_theme),
    #layout.Columns(**layout_theme),
    #layout.RatioTile(**layout_theme),
    #layout.Tile(shift_windows=True, **layout_theme),
    #layout.VerticalTile(**layout_theme),
    #layout.Matrix(**layout_theme),
    #layout.Zoomy(**layout_theme),
    #layout.Max(**layout_theme),
    #layout.Stack(num_stacks=2),
    #layout.RatioTile(**layout_theme),
    #layout.TreeTab(
    #     font = "Ubuntu",
    #     fontsize = 10,
    #     sections = ["FIRST", "SECOND", "THIRD", "FOURTH"],
    #     section_fontsize = 10,
    #     border_width = 2,
    #     bg_color = "1c1f24",
    #     active_bg = "f22516",
    #     active_fg = "000000",
    #     inactive_bg = "282c34",
    #     inactive_fg = "282c34",
    #     padding_left = 0,
    #     padding_x = 0,
    #     padding_y = 5,
    #     section_top = 10,
    #     section_bottom = 20,
    #     level_shift = 8,
    #     vspace = 3,
    #     panel_width = 200
    #     ),
]

colors = [["#282c34", "#282c34"], # panel background
          ["#3d3f4b", "#434758"], # background for current screen tab
          ["#ffffff", "#ffffff"], # font color for group names
          ["#f22516", "#ff5555"], # border line color for current tab
          ["#3d3f4b", "#3d3f4b"], # border line color for 'other tabs' and color for 'odd widgets'
          ["#3d3f4b", "#3d3f4b"], # color for the 'even widgets'
          ["#ebe6ed", "#ebe6ed"], # window name
          ["#f22516", "#ffffff"]] # backbround for inactive screens

prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

##### DEFAULT WIDGET SETTINGS #####
widget_defaults = dict(
    font="Ubuntu Mono",
    fontsize = 12,
    padding = 2,
    background=colors[2]
)
extension_defaults = widget_defaults.copy()

def init_widgets_list():
    widgets_list = [
              widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       foreground = colors[2],
                       background = colors[0]
                       ),
              widget.Image(
                       filename = "~/.config/qtile/icons/hack1.png",
                       scale = "False",
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm)}
                       ),
             widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       foreground = colors[2],
                       background = colors[0]
                       ),
              widget.GroupBox(
                       font = "Ubuntu Bold",
                       fontsize = 14,
                       margin_y = 3,
                       margin_x = 0,
                       padding_y = 5,
                       padding_x = 3,
                       borderwidth = 3,
                       active = colors[2],
                       inactive = colors[7],
                       rounded = False,
                       highlight_color = colors[1],
                       highlight_method = "line",
                       this_current_screen_border = colors[6],
                       this_screen_border = colors [4],
                       other_current_screen_border = colors[6],
                       other_screen_border = colors[4],
                       foreground = colors[2],
                       background = colors[0]
                       ),
              widget.Prompt(
                       prompt = prompt,
                       font = "Ubuntu Mono",
                       padding = 10,
                       foreground = colors[3],
                       background = colors[1]
                       ),
              widget.Sep(
                       linewidth = 0,
                       padding = 40,
                       foreground = colors[2],
                       background = colors[0]
                       ),
              widget.WindowName(
                       foreground = colors[6],
                       background = colors[0],
                       padding = 0
                       ),
              widget.Systray(
                       background = colors[0],
                       padding = 5
                       ),
              widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       foreground = colors[0],
                       background = colors[0]
                       ),
                       
              widget.TextBox(
                       text = '',
                       background = colors[0],
                       foreground = colors[4],
                       padding = 0,
                       fontsize = 37
                       ),
             widget.Net(
                       interface = "wlan0",
                       format = '{down} ↓↑ {up}',
                       foreground = colors[2],
                       background = colors[4],
                       padding = 5
                       ),
              widget.TextBox(
                       text = '',
                       background = colors[0],
                       foreground = colors[4],
                       padding = 0,
                       fontsize = 37
                       ),
              widget.TextBox(
                       text = " 🌡 :",
                       padding = 2,
                       foreground = colors[2],
                       background = colors[5],
                       fontsize = 11
                       ),
              widget.ThermalSensor(
                        foreground = colors[2],
                        background = colors[5],
                        threshold = 90,
                        padding = 5
                        ),
                        
                        
              #widget.TextBox(
              #         text='',
              #         background = colors[5],
              #         foreground = colors[4],
              #         padding = 0,
              #         fontsize = 37
              #         ),
              #widget.TextBox(
              #         text = " ⟳" ,
              #         padding = 2,
              #         foreground = colors[2],
              #         background = colors[4],
              #         fontsize = 14
              #         ),
              #widget.CheckUpdates(
              #         update_interval = 1800,
              #         distro = "Arch_checkupdates",
              #         display_format = "{updates} Updates",
              #         foreground = colors[2],
              #         mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e sudo apt upgrade')},
              #         background = colors[4]
              #         ),
              
              
              
              widget.TextBox(
                       text = '',
                       background = colors[0],
                       foreground = colors[4],
                       padding = 0,
                       fontsize = 37
                       ),
              widget.TextBox(
                       text = " 🖬",
                       foreground = colors[2],
                       background = colors[5],
                       padding = 0,
                       fontsize = 14
                       ),
              widget.Memory(
                       foreground = colors[2],
                       background = colors[5],
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e bashtop')},
                       padding = 5
                       ),
                       
                       
                       
              #widget.TextBox(
              #         text='',
              #         background = colors[5],
              #         foreground = colors[4],
              #         padding = 0,
              #         fontsize = 37
              #         ),
              #widget.TextBox(
              #         text = "₿",
              #         padding = 0,
              #         foreground = colors[2],
              #         background = colors[4],
              #         fontsize = 12
              #         ),
              #widget.BitcoinTicker(
              #         foreground = colors[2],
              #         background = colors[4],
              #         padding = 5
              #         ),
              
              
              
              widget.TextBox(
                       text = '',
                       background = colors[0],
                       foreground = colors[4],
                       padding = 0,
                       fontsize = 37
                       ),
              widget.TextBox(
                      text = " :",
                       foreground = colors[2],
                       background = colors[5],
                       padding = 0
                       ),
              widget.Volume(
                       foreground = colors[2],
                       background = colors[5],
                       padding = 5
                       ),                                                  
                       
              #widget.TextBox(
              #         text = '',
              #         background = colors[0],
              #         foreground = colors[4],
              #         padding = 0,
              #         fontsize = 37
              #         ),
              #widget.CurrentLayoutIcon(
              #         custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
               #        foreground = colors[0],
               #        background = colors[4],
               #        padding = 0,
               #        scale = 0.7
               #        ),
               #widget.CurrentLayout(
               #        foreground = colors[2],
               #        background = colors[4],
               #        padding = 5
               #        ),                                             
               
              widget.TextBox(
                       text = '',
                       background = colors[0],
                       foreground = colors[4],
                       padding = 0,
                       fontsize = 37
                       ),
              widget.Clock(
                       foreground = colors[2],
                       background = colors[5],                      
                       format = "%A, %B %d - %H:%M "
                       ),
              ]
    return widgets_list

def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    del widgets_screen1[7:8]               
    return widgets_screen1

def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2                

def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=1.0, size=20)),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), opacity=1.0, size=20)),
            Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=1.0, size=20))]

if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_screen1()
    widgets_screen2 = init_widgets_screen2()

def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)

def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)

def window_to_previous_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group)

def window_to_next_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group)

def switch_screens(qtile):
    i = qtile.screens.index(qtile.current_screen)
    group = qtile.screens[i - 1].group
    qtile.current_screen.set_group(group)

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

floating_layout = layout.Floating(float_rules=[
         
    *layout.Floating.default_float_rules,
    Match(title='Confirmation'),      
    Match(title='Qalculate!'),        
    Match(wm_class='kdenlive'),       
    Match(wm_class='pinentry-gtk-2'), 
])
auto_fullscreen = True
focus_on_window_activation = "smart"

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])

wmname = "0x3n0"
