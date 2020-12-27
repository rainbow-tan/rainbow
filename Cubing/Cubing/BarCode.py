# -*- coding: utf-8 -*-
import os

from pystrich.code128 import Code128Encoder


class BarCode:
    def __init__(self):
        pass

    @staticmethod
    def create_folder(folder):
        abs_folder = os.path.abspath(folder)
        if not os.path.exists(abs_folder):
            try:
                os.makedirs(abs_folder)
            except Exception as e:
                print('Create folder fail:{}'.format(e))

    def generate(self, info, save_path):
        asb_save_path = os.path.abspath(save_path)
        folder = os.path.dirname(asb_save_path)
        self.create_folder(folder)
        options = {"bottom_border": 10, "height": 200, "label_border": 2}
        try:
            encoder = Code128Encoder(info, options)
            encoder.save(asb_save_path)
            print('Generate bar code success, save to:{}'.format(asb_save_path))
        except Exception as e:
            print('Generate bar code fail:{}'.format(e))


def debug():
    bar = BarCode()
    bar.generate('ADFF15645', './test.png')


if __name__ == '__main__':
    debug()
