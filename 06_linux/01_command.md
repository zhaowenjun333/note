# 基本命令

## shell通配符
```bash
文件名的通配符
	* 匹配零或多个任意字符 
	? 匹配任意一个单一字符
	~ 代表家目录
	[2-7]   表示数字范围
	[c-w]   表示字母范围  [a-zA-Z]
	[nihao]     匹配列表
	[^nihao]    取反，会匹配到列表中所有字符以外的字符
	[[:digit:]]     表示任意数字
	[[:alpha:]]     表示任意字母
	[[:alnum:]]     表示任意字母或数字
	[[:upper:]]     表示大写字母
	[[:lower:]]     表示小写字母
    [[:word:]]      表示一个单词(letters, numbers and underscores)
	[[:blank:]]     水平空白字符
	[[:space:]]     水平或垂直空白字符
	[[:punct:]]     特殊字符
```
### posix 的 shorthand

| posix      | description                              | ascii                                    | shorthand |
| ---------- | ---------------------------------------- | ---------------------------------------- | --------- |
| [:alnum:]  | alphanumeris characters                  | [a-zA-Z0-9]                              |           |
| [:alpha:]  | alphabetic characters                    | [a-zA-Z]                                 |           |
| [:ascii:]  | ASCII characters                         | [\x00-\x7F]                              | \h        |
| [:blank:]  | space and tab                            | [\t]                                     |           |
| [:cntrl:]  | control characters                       | [\x00-\x1F\x7F]                          |           |
| [:digit:]  | digits                                   | [0-9]                                    | \d        |
| [:\graph:] | visible characters (anything  except spaces and control characters) | [\x21-\x7E]                              |           |
| [:lower:]  | lowercase letters                        | [a-z]                                    | \l        |
| [:upper:]  | uppercase letters                        | [A-Z]                                    | \u        |
| [:print:]  | visible characters and space (anything except control characters) | [\x20-\x7E]                              |           |
| [:punct:]  | punctuation and symbols                  | `[!"\#$%&'()*+,\-./:;<=>?@\[\\\]^_\`{ \| }~]` |           |
| [:space:]  | all whitespace characters, including line breaks | [\t\r\n\v\f]                             | \s        |
| [:word:]   | word characters (letters, numbers and underscores) | [A-Za-z0-9]                              | \w        |
| [:xdigit:] | hexadecimal digits                       | [A-Fa-f0-9]                              |           |



## cp
### cp原理：
cp 与 inode
1. 分配一个空闲的inode号， 在inode表中生成新条目，在目录中创建一个目录项，将名称与inode号关联
2. 拷贝数据生成新的文件


## rm
### rm 原理
rm 与 inode
1. 链接数递减，从而释放的 inode 号可以被重新使用，把数据块放在空闲列表中删除目录项
2. 数据实际上不会马上被删除


## find命令

关于权限的解理
```
-perm xxx
-perm -xxx  # 相当于 x and x and x
-perm +xxx  # 相当于 x or x or 
```

关于时间
```
----- +4 ----->|4|------ -4 ----------- >
---------------------------------------->
-mtime 4
-mtime +4  # 4天之前
-mtime -4  # 4天之内
```