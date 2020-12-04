import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import OneHotEncoder
import sklearn.metrics as metrics
import missingno as msg


def deal_data(data):
    """
    数据清洗,处理NaN数据
    :param data:
    :return:
    """
    # 处理train_data nan的需要处理
    # 查看数据完整性
    # msg.matrix(data, figsize=(12, 8))
    # plt.show()
    # 发现Age Cabin Embarkea存在空
    # 需要处理 Age Cabin Embarkea

    # 处理Age 取Age的平均数填充NaN值
    # 求年龄的平均数
    mean_age = data["Age"].mean()
    mean_age = int(mean_age)
    # 将空值填充为平均数
    data.loc[data["Age"].isna(), ["Age"]] = mean_age

    # 处理Cabin
    # 查看Cabin空值
    # print(data.loc[data["Cabin"].isna(), "Cabin"])
    # 使用fillna()方法填充NaN值,并使用前一个客舱号填充
    data["Cabin"].fillna(method="ffill", inplace=True)
    data["Cabin"].fillna(method="bfill", inplace=True)

    # 处理Embarked
    data["Embarked"].fillna(method="bfill", inplace=True)

    # 再次查看数据完整性
    # msg.matrix(data, figsize=(12, 8))
    # plt.show()

    return data


def get_features(data):
    """
    对数据进行研究,获取特征
    :param data:
    :return:
    """

    # 对年龄切片
    age_cut_labels = [0, 1, 2, 3]
    age_cut = pd.qcut(data["Age"], 4, labels=age_cut_labels)
    # 转为年龄分组后的结果
    data["AgeCutLabels"] = pd.Series(age_cut)
    # 性别转为01分组
    data.loc[data["Sex"] == "female", ["Sex"]] = 0
    data.loc[data["Sex"] == "male", ["Sex"]] = 1

    # sns.barplot(x="Sex", y="Survived", data=data)
    # plt.show()

    features = ["AgeCutLabels", "Sex", "Pclass", "SibSp", "Parch", "Fare"]
    print("提取特征为", features)
    return features, data


def split_data(data, features):
    """
    对样本数据进行处理,分割为训练集和测试集
    :param data:
    :param features:
    :return:
    """
    data_y = data["Survived"]
    data_x = data.loc[:, features]
    # train_x, test_x, train_y, test_y = train_test_split(data_x, data_y, test_size=0.2)
    # return train_x, test_x, train_y, test_y
    return data_x, data_y


def fit_model(train_x, train_y):
    """
    训练模型
    :param train_x: 特征
    :param train_y: 标签
    :return:
    """
    # 创建多个算法
    models = [KNeighborsClassifier(), LogisticRegression(), GaussianNB(), RandomForestClassifier(),
              DecisionTreeClassifier(), GradientBoostingClassifier(), SVC()]
    names = ["KNN", "LR", "NB", "RF", "Tree", "GB", "SVC"]

    for (name, model) in zip(names, models):
        score = cross_val_score(model, train_x, train_y, cv=10, scoring="accuracy")
        print("%s 得分%s=====平均值***%s***" % (name, score, score.mean()))
    # # 线性回归算法
    # lr = linear.LogisticRegression()
    # # 训练模型
    # lr.fit(train_x, train_y)
    # return lr


def evaluation_model(lr, test_x, test_y_true):
    """
    评估模型
    :param test_y: 测试标签
    :return:
    """
    # 获取测试结果
    test_y = lr.predict(test_x)

    # 评估模型
    # mse 均方误差评分
    mse = metrics.mean_squared_error(test_y_true, test_y)

    # r2_score r2score评分
    r2_score = metrics.r2_score(test_y_true, test_y)

    # 打印
    print("均方误差MSE为%s" % mse)
    print("r2Score为%s" % r2_score)


def predict_data(predict_x, lr):
    """
     预测数据
    :param predict_x: 准备预测的样本数据
    :param lr: 模型
    :return:
    """
    predict_y = lr.predict(predict_x)
    return predict_y


if __name__ == '__main__':
    train_data = pd.read_csv("../titanic/train.csv")

    # 处理数据
    train_data = deal_data(train_data)
    # 提取特征
    features, train_data = get_features(train_data)
    # 获取训练集 测试集
    # train_x, test_x, train_y, test_y = split_data(train_data, features)
    data_x, data_y = split_data(train_data, features)
    # 训练模型 并评分
    fit_model(data_x, data_y)
    # 预测数据

