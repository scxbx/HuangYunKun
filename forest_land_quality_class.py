from decimal import Decimal


def get_forest_land_quality_class(TCHD, TRMC, Podu, Powei, HaiBa):
    tchd_gv = 0
    trmc_gv = 0
    podu_gv = 0
    powei_gv = 0
    haiBa_gv = 0

    # 土层厚度
    tchd_int = str_to_int(TCHD)
    if tchd_int == 1:
        tchd_gv = 2
    elif tchd_int == 2:
        tchd_gv = 4
    elif tchd_int == 3:
        tchd_gv = 8
    else:
        print("土层厚度错误")

    # 土壤类型
    trmc_int = str_to_int(TRMC)
    if trmc_int in [104, 121]:
        trmc_gv = 4
    elif trmc_int in [101, 102, 167]:
        trmc_gv = 6
    elif trmc_int in [211, 182, 191, 173]:
        trmc_gv = 8
    elif trmc_int == 202:
        trmc_gv = 10
    else:
        print("土壤类型错误")

    # 坡度
    podu_int = str_to_int(Podu)
    podu_gv = podu_int * 2

    # 坡位
    powei_int = str_to_int(Powei)
    if powei_int in [6, 7]:
        powei_gv = 2
    elif powei_int in [4, 5]:
        powei_gv = 4
    elif powei_int == 3:
        powei_gv = 6
    elif powei_int == 2:
        powei_gv = 8
    elif powei_int == 1:
        powei_gv = 10
    else:
        print("坡位错误")

    # 海拔
    haiBa_int = str_to_int(HaiBa)
    if haiBa_int <= 300:
        haiBa_gv = 2
    elif 301 <= haiBa_int <= 700:
        haiBa_gv = 4
    elif 701 <= haiBa_int <= 1100:
        haiBa_gv = 6
    elif 1101 <= haiBa_int <= 1500:
        haiBa_gv = 8
    elif haiBa_int >= 1501:
        haiBa_gv = 10
    else:
        print("海拔错误")

    # 林地质量综合评分值
    overall_score = Decimal(tchd_gv) * Decimal(0.3) \
                    + Decimal(trmc_gv) * Decimal(0.2) \
                    + Decimal(podu_gv) * Decimal(0.2) \
                    + Decimal(powei_gv) * Decimal(0.1) \
                    + Decimal(haiBa_gv) * Decimal(0.1) \
                    + Decimal(0.1)

    overall_score = round(overall_score, 5)
    # print([trmc_gv, trmc_gv, podu_gv, powei_gv, haiBa_gv])
    # print([Decimal(tchd_gv) * Decimal(0.3), Decimal(trmc_gv) * Decimal(0.2), Decimal(powei_gv) * Decimal(0.1), Decimal(haiBa_gv) * Decimal(0.1), Decimal(0.1)])
    print(overall_score)

    # 等级
    quality_class = 0
    if overall_score <= 2:
        quality_class = 1
    elif 2 < overall_score <= 4:
        quality_class = 2
    elif 4 < overall_score <= 6:
        quality_class = 3
    elif 6 < overall_score <= 8:
        quality_class = 4
    elif 8 < overall_score <= 10:
        quality_class = 5

    return quality_class


def str_to_int(number):
    if type(number) == str:
        return int(number)
    return number


print(get_forest_land_quality_class('1', '101', '3', '2', '100'))
print(get_forest_land_quality_class('2', '211', '2', '2', '315'))
print(get_forest_land_quality_class('2', '173', '2', '2', '315'))
print(get_forest_land_quality_class('2', '101', '1', '7', '253'))
print(get_forest_land_quality_class('2', '101', '2', '7', '240'))

file = open('.//sample.txt')

lines = file.readlines()
print(len(lines))
# 1.手动一行一行读



for line in lines:
    list_line = line.split()
    print(list_line)
    if list_line[0] != 'HAIBA':
        print(get_forest_land_quality_class(list_line[4], list_line[3], list_line[1], list_line[2], list_line[0]))
file.close()