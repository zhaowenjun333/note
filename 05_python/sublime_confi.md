## plug

```
//插件越不运行越快
chineseLozation     =本地化
SideBarEnhancements = 侧栏右键功能增强
Block Cursor Everywhere =光标样式
IMESupport          =中文输入法跟随
Sublime CodeIntel    =代码自动提示
prettify              =HTML排版 ctrl+shift+h
ConvertToUTF8        =UTF8
Alignment           =代码对齐
Emmet               =快速生成HTML代码段的插件 zen coding
MarkdownEditing     =markdownEditing编辑
```

## my conf
```
//Preferences -> Settings - User
{
    "auto_complete": false,
    "color_scheme": "Packages/Color Scheme - Default/Monokai.tmTheme",
    "draw_minimap_border": true,
    "font_face": "Consolas",
    "font_size": 14,
    "highlight_line": true,
    "highlight_modified_tabs": true,
    "ignored_packages":
    [
        //"Vintage"
    ],

    "rulers":[80],
    "word_wrap": true,
    "save_on_focus_lost": true,
    "tab_size": 4,
    "tab_completion": false,
    "translate_tabs_to_spaces": true,

    //unix
    "default_line_ending": "unix",
    "update_check": false,
}
```



### 快捷键

修改 SublimeREPL 菜单文件
```
// vi Data\Packages\SublimeREPL\config\Python\Main.sublime-menu
"id": "repl_python_run",
// add -i
"cmd": ["python", "-i", "-u", "$file_basename"],
```

```
 [
    // vim中kj进入普通模式 
    { "keys": ["k","j"], "command": "exit_insert_mode",
        "context":
        [
            { "key": "setting.command_mode", "operand": false },
            { "key": "setting.is_widget", "operand": false }
        ]
    },
    { "keys": ["k","j"], "command": "hide_auto_complete", "context":
        [
            { "key": "auto_complete_visible", "operator": "equal", "operand": true }
        ]
        },
    { "keys": ["k","j"], "command": "vi_cancel_current_action", "context":
        [
            { "key": "setting.command_mode" },
            { "key": "selection_empty", "operator": "equal", "operand": true, "match_all": false },
            { "key": "vi_has_input_state" }
        ]
    },

    // SublimeREPL使用F5和Ctrl+f5
    { "keys": ["ctrl+f5"],
        "caption": "SublimeREPL: Python",
        "command": "run_existing_window_command", "args":
        {
            "id": "repl_python_run",
            "file": "config/Python/Main.sublime-menu"
        }
    },
    { "keys": ["f5"],
        "caption": "SublimeREPL: Python",
        "command": "run_existing_window_command", "args":
        {
            "id": "repl_python",
            "file": "config/Python/Main.sublime-menu"
        }
    },
]


```





## 右键
```
1. 打开注册表，开始→运行→regedit

2. 在 HKEY_CLASSSES_ROOT→ * → Shell 下面新建项命名为 Edit with SublimeText

3. 右键 Edit with SublimeText 项，
新建字符串值 Icon，值为 sublime_text.exe所在路径,0

4. 右键 Edit with SublimeText 项，
新建项 command，默认值为 sublime_text.exe所在路径 %1

```