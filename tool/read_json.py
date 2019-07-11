import json


# 定义读取函数
def read_json(filename):
    # 读取文件流
    with open("../data/" + filename, "r", encoding="utf-8")as f:
        # 解析文件
        return json.load(f)


if __name__ == '__main__':
    # 方式一
    # print(read_json("post_data.json"))
    # data_list = list()
    # data_list.append((read_json("post_data.json").get("post_data"),
    #                   read_json("post_data.json").get("status_code"),
    #                   read_json("post_data.json").get("expect_result")))
    # print(data_list)

    # 方式二
    data_list = list()
    data_list.append(tuple(read_json("get_one_data.json").values()))
    print(data_list)


