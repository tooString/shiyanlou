#!/usr/bin/env python3
# coding : utf-8
import sys

# 应纳税所得额 = 工资金额 － 各项社会保险费 - 起征点(3500元)
# 应纳税额 = 应纳税所得额 × 税率 － 速算扣除数
# 税后工资 = 工资金额 - 五险一金 - 应纳税额

'''税表'''


def table_tax(money):
    if money <= 1500:
        return 0.03, 0
    elif money <= 4500:
        return 0.1, 105
    elif money <= 9000:
        return 0.2, 555
    elif money <= 35000:
        return 0.25, 1005
    elif money <= 55000:
        return 0.3, 2755
    elif money <= 80000:
        return 0.35, 5505
    else:
        return 0.45, 13505


'''计算税后'''


def after_taxs():
    bx = salary * 0.165 #五险一金
    qz = 3500   #起征点
    ynsd = salary - bx - qz #应纳所得额
    if ynsd <= 0:
        ynsd = 0
    tax_rate, take_out = table_tax(ynsd)
    tax = ynsd * tax_rate - take_out    #应纳税额
    get_money = salary - tax - bx   #最终工资
    print("{:.2f}".format(get_money))


if __name__ == '__main__':
    try:
        for i in range(1, len(sys.argv)):
            salary = int(sys.argv[i].split(':')[1])
            if salary <= 0:
                print('please enter a number greater than 0 ')
            after_taxs()

    except (ValueError, IndexError):
        print("Parameter Error")
