from collections import Counter


# 数据集

data = [
    ("高", "重", "大", "男"),
    ("中", "重", "大", "男"),
    ("中", "中", "大", "男"),
    ("矮", "中", "中", "男"),
    ("矮", "轻", "小", "女"),
    ("矮", "轻", "小", "女"),
    ("矮", "中", "小", "女"),
    ("中", "中", "中", "女"),
]


# 新数据

new_data = ("中", "中", "中")


# 计算先验概率

gender_counts = Counter([d[3] for d in data])

P_male = gender_counts["男"] / len(data)

P_female = gender_counts["女"] / len(data)


# 计算条件概率

height_counts = {g: Counter() for g in ["男", "女"]}

weight_counts = {g: Counter() for g in ["男", "女"]}

shoe_size_counts = {g: Counter() for g in ["男", "女"]}


for d in data:

    height_counts[d[3]][d[0]] += 1

    weight_counts[d[3]][d[1]] += 1

    shoe_size_counts[d[3]][d[2]] += 1


# 计算后验概率

P_height_given_male = height_counts["男"][new_data[0]] / sum(
    height_counts["男"].values()
)

P_weight_given_male = weight_counts["男"][new_data[1]] / sum(
    weight_counts["男"].values()
)

P_shoe_size_given_male = shoe_size_counts["男"][new_data[2]] / sum(
    shoe_size_counts["男"].values()
)


P_height_given_female = height_counts["女"][new_data[0]] / sum(
    height_counts["女"].values()
)

P_weight_given_female = weight_counts["女"][new_data[1]] / sum(
    weight_counts["女"].values()
)

P_shoe_size_given_female = shoe_size_counts["女"][new_data[2]] / sum(
    shoe_size_counts["女"].values()
)


# 计算最终概率

P_male_given_data = (
    P_height_given_male * P_weight_given_male * P_shoe_size_given_male
) * P_male

P_female_given_data = (
    P_height_given_female * P_weight_given_female * P_shoe_size_given_female
) * P_female


# 判断性别

if P_male_given_data > P_female_given_data:

    print("判断结果：男")

else:

    print("判断结果：女")
