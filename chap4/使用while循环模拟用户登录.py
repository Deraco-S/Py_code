i=0
while i<3:
    user_name=input("请输入您的用户名：")
    user_passwd=input("请输入您的密码：")
    if user_name == 'mario' and user_passwd=='20040917':
        print("系统正在登录，请稍后......")
        i=10
    else:
        if i<2:
            print("您还有",2-i,"次机会")
        i=i+1

if i==3:
    print("您的系统已经锁定，请三分钟后再尝试输入密码")
