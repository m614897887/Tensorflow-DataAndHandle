list1 = [['小米手环4', 209], ['荣耀手环5', 199], ['华为手环B5', 849], ['智能血压手环', 379]]
order = 0
price = 0
print('数字猜谜游戏！')
print('可以竞猜的商品如下:\n', '1', list1[0][0], '\n 2', list1[1][0], '\n 3', list1[2][0], '\n 4', list1[3][0])

number = input("请输入竞猜商品前面的数字: ")
if number.isdigit():
    order = int(number)
    if 0 < order <= 4:
        print("您选择的竞猜商品是:", list1[order - 1][0])
        price = list1[order - 1][1]
        guess = -1  # 初始化guess数
        while guess != price:
            guess = input("请输入竞猜价格(只能输入整数价格):")
            if guess.isdigit():
                guess = int(guess)
                if guess == price:
                    print("恭喜,你猜对了！")
                elif guess < price:
                    print("猜的价格小了 ...")
                elif guess > price:
                    print("猜的价格大了 ...")
            else:
                print("输入价格非法,请重新输入！")