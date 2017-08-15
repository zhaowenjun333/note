## 1. sublime 配置
### 1.1 sublime 初始配置
```
{
	"auto_complete_triggers":
	[
		{
			"characters": " ",
			"selector": "text.html"
		}
	],
	"caret_style": "phase",             //使光标闪动更加柔和
	"default_line_ending": "unix",
	"email_account_default_identity": "sublimetext3 <sublimetext3@163.com>",
	"email_account_default_smtp": "smtp://sublimetext3:123456789abc@smtp.163.com:25",
	//"font_face": "Consolas",
	"font_size": 13,
	"highlight_line": true,             //高亮当前行
	"highlight_modified_tabs": true,    //高亮有修改的标签
	"ignored_packages":
	[
		"AngularJS",
		"caniuse_local",
		"CodeComplice",
		"CSS",
		"Git",
		"GoSublime",
		"Insert Nums",
		"LiveStyle",
		"Markdown",
		"SublimeClang",
		"SVN",
		"Vintageous"
	],
	"rulers":[80,100],        //显示行宽标识
	"show_encoding": true,
	"tab_size": 4,
	"translate_tabs_to_spaces": true,
	"trim_trailing_white_space_on_save": true,    //保存时去除行尾空白
	"update_check": false,                        //禁止更新
	"word_wrap": true                             //自动换行
}
```


### 1.2 sublime 插件
    sublimeREPL
    Sublime CodeIntel
    SideBarEnhancements
    sftp
    git

### 1.3 解决输入法不跟随问题
pcip ---> IMESupport


## 2. 按键绑定配置
### 2.1  配置语法
    [
    {"key": [XXX], "commnad": "xxxx"},
    {"key": [XXX], "commnad": "xxxx", "args": {"extensions": ["cpp", "cxx"]}}
    {...}
    ]

### 2.2 配置F5执行py文件
    // Preferences --> 浏览程序包
    // D:\Program Files\sublime text\Data\Packages\SublimeREPL\config\Python
    [
        { "keys": ["f5"], "caption": "SublimeREPL:Python",
                          "command": "run_existing_window_command", "args":
                          {
                               "id": "repl_python_run",
                               "file": "config/Python/Main.sublime-menu"
                          }
        },
    ]


