# myconfig 

## vsc
```
// 将设置放入此文件中以覆盖默认设置
{
    "editor.fontSize": 16,
    "vim.disableAnnoyingNeovimMessage": true,
    "vim.insertModeKeyBindings": [
        //vim模式中启用kj-->ESC
        {
            "before": ["k", "j"],
            "after": ["<Esc>"]
        }
    ],
    "workbench.colorTheme": "Visual Studio Light"
    //vim模式中禁用vim下Ctrl功能
    "vim.useCtrlKeys": false,"  
}
```