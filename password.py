password = 'a123456'
i = 3
while i > 0 :
	password1 = input('請輸入密碼:')
	if password1 == password:
		print('登入成功!')
		i = 0
	else:
		print('密碼錯誤!')
		i = i - 1
		if i > 0 :
			print('還有', i, '次機會')
            
