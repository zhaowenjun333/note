'''
【程序81】
题目：809*??=800*??+9*??+1 其中??代表的两位数,8*??的结果为两位数，9*??的结果为3位数。求??代表的两位数，及809*??后的结果。
1.程序分析：
2.程序源代码
这个程序实在是奇怪
0 = 1 :(
就写个程序而已，不去追究了
'''
a = 809
for i in range(10,100):
    b = i * a + 1
    if b >= 1000 and b <= 10000 and 8 * i < 100 and 9 * i >= 100:
        print b,'/',i,' = 809 * ',i,' + ', b % i
        
