# -*- encoding=utf-8 -*-
import json
import os


class ReadJson:
    def __init__(self, json_name):
        self.json_name = json_name

    def load_data(self, default=None):
        if default is None:
            default = {}
        json_data = default
        if os.path.isfile(self.json_name):
            try:
                with open(self.json_name, 'r', encoding='utf-8') as file_handler:
                    json_data = json.load(file_handler)
            except Exception as e:
                print('Load json file fail:{}'.format(self.json_name))
                print('Exception:{}'.format(e))
        else:
            print('Can not find json file:{}'.format(self.json_name))
        return json_data


if __name__ == '__main__':
    obj = ReadJson('UserInfo.json')
    print(obj.load_data().values())
