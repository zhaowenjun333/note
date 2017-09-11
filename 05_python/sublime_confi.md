## plug

```
//插件越不运行越快
chineseLozation     =本地化
SideBarEnhancements = 侧栏右键功能增强
Block Cursor Everywhere =光标样式
Sublime CodeIntel    =代码自动提示
prettify              =HTML排版 ctrl+shift+h
ConvertToUTF8        =UTF8
Alignment           =代码对齐
Emmet               =快速生成HTML代码段的插件 zen coding
```

## my conf
```
//用户设置 Preferences -> Settings - User
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


## 右键
```
1. 打开注册表，开始→运行→regedit

2. 在 HKEY_CLASSSES_ROOT→ * → Shell 下面新建项命名为 Edit with SublimeText

3. 右键 Edit with SublimeText 项，
新建字符串值 Icon，值为 sublime_text.exe所在路径,0

4. 右键 Edit with SublimeText 项，
新建项 command，默认值为 sublime_text.exe所在路径 %1

```