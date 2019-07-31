#密码重试程式
#password = 'a123456'
#让使用者重复输入密码
#最多输入三次
#如果正确 就打印“登录成功！”
#如果不正确 就打印“密码错误！还有一次机会”

password = 'a123456'
i = 3  #剩余机会
while i > 0:  #True/or当i>0,最后if就不用了
	i -= 1
	pwd = input('请输入密码:')
	if pwd == password:
		print('登录成功！')
		break #跳出循环
	else:
		print('密码错误!')
		if i > 0:
			print('还有', i ,'次机会')
		else:
			print('没机会尝试了，锁住账号了！')
