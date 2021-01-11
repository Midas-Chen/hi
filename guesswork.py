# 設計一個猜數字的遊戲
# 產生一個 mi ~ ma 的隨機整數(不要印出來)
# 讓使用者輸入(mi ~ ma)整數去猜
# 前3次猜對的話，印出 '好棒！第_次就猜對了'
# 第4次以後猜對的，印出 '終於在第_次猜對了'
# 猜錯的話，要告訴使用者 '比答案大／小'

import random
print('歡迎參加猜數遊戲')
mi = int(input('請輸入數字區間的最小值'))
ma = int(input('請輸入數字區間的最大值'))
r = random.randint(mi, ma)
answer = 0
count = 1

while answer != r:
    print('請輸入', mi, '~', ma, '的整數')
    answer = int(input())
    if answer == r:
        if count <= 3:
            print('好棒！第', count, '次就猜對了')
            break
        else:
            print('終於在第', count, '次猜對了')
            break
    else:
        count = count + 1
        if answer < r:
            print('您這次猜的數字比答案小')
        else:
            print('您這次猜的數字比答案大')
