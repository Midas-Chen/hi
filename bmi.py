# BMI值計算公式: BMI = 體重(公斤) / 身高2(公尺2)
height = float(input('請輸入您的身高(公分): '))
weight = float(input('請輸入您的體重(公斤): '))
bmi = weight / (height / 100) ** 2
if bmi < 18.5:
    print('您的BMI為: ',bmi,'代表您的體重過輕 (BMI < 18.5)')
elif bmi >= 18.5 and bmi < 24:
    print('您的BMI為: ',bmi,'代表您的體重正常 (18.5 ≦ BMI ＜ 24)')
elif bmi >= 24 and bmi < 27:
    print('您的BMI為: ',bmi,'代表您的體重過重 (24 ≦ BMI ＜ 27)')
elif bmi >= 27 and bmi < 30:
    print('您的BMI為: ', bmi, '代表您為輕度肥胖 (27 ≦ BMI ＜ 30)')
elif bmi >= 30 and bmi < 35:
    print('您的BMI為: ', bmi, '代表您為中度肥胖 (30 ≦ BMI ＜ 35)')
else:
    print('您的BMI為: ', bmi, '代表您為重度肥胖 (BMI >= 35)')