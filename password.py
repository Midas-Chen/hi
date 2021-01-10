# 密碼輸入程式練習(允許的錯誤次數設定為變數，可以在程式開頭更改)
password = 'a123456'
x = 4  # 定義允許的錯誤次數
error_allow = x  # error_allow=剩餘的錯誤次數

while error_allow > 0:
    answer = input('請輸入您的密碼: ')
    if answer == password:
        print('登入成功')
        break
    elif error_allow == 1:
        print('對不起！密碼輸入連續錯誤', x, '次，登入程式自動結束')
        break
    else:
        error_allow = error_allow - 1
        print('密碼錯誤！還有', error_allow, '次機會')
