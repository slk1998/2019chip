import pandas as pd
import numpy as np
import os
import logging

# 获取基本路径变量
code_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(code_dir)
data_dir = os.path.join(project_dir, 'data')
log_dir = os.path.join(project_dir, 'log')

# 配置日志
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
# 日志输出文件
log_path = os.path.join(log_dir, 'filter.log')
handler = logging.FileHandler(log_path)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# 主程序
if __name__ == "__main__":
    # 索引
    head_label = [
        "question1",
        "question2",
        "label",
        "category"
    ]

    # 读取训练集
    train_path = os.path.join(data_dir, 'train.csv')
    train_df = pd.read_csv(train_path, header=0, encoding='utf-8')
    train_result = pd.DataFrame(columns = head_label)

    total_train_num = 0

    # 输出信息
    for index, row in train_df.iterrows():
            total_train_num += 1
            tra_q1 = row['question1']
            tra_q2 = row['question2']
            tra_l = row['label']
            tra_c = row['category']
            #创建序列
            train_series = pd.Series([tra_q1,
                                    tra_q2,
                                    tra_l,
                                    tra_c])
            train_series.index = head_label
            train_df = train_result.append(train_series, ignore_index=True)
            print(train_series)
    print(total_train_num)


