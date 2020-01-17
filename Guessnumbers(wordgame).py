import random

dif = int(input('请选择难度等级(1~5): '))
while dif > 5 or dif < 1:
	print('输入不合法')
	dif = int(input('请重新输入难度等级(1~5): '))
fre = 1
a = random.randint(1,dif*10)
print('您要从1~' + str(dif*10) + '之内猜一个数字')
guess = int(input('苹果心里想的数字是: '))
while guess != a:
	if guess > a:
		print('大了')
	elif guess < a:
		print('小了')
	fre += 1
	guess = int(input('猜错了，再猜一次: '))
print('猜对了！')
print('您用了' + str(fre) + '次猜对，游戏结束')
