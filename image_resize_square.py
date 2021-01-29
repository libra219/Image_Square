#!/usr/bin/python
# -*- coding: utf-8 -*-
''' image resize square

    Make the image square
    画像サイズをすべて正方形にする

TODO:
    * add more ドラッグアンドドロップの複数ファイル対応すること

'''
import datetime
import sys

from PIL import Image

# ドラッグアンドドロップでファイル読み取り
file_paths = sys.argv[1:]

def imagesquare(pil_img, background_color):
    ''' Check image size

        Resize confirmation
        画像サイズの変更確認

    '''
    width, height = pil_img.size
    if width == height:
        return pil_img
    elif width > height:
        result = Image.new(pil_img.mode, (width, width), background_color)
        result.paste(pil_img, (0, (width - height) // 2))
        return result
    else:
        result = Image.new(pil_img.mode, (height, height), background_color)
        result.paste(pil_img, ((height - width) // 2, 0))
        return result

for file_path in file_paths:
    # 現在時刻の取得(ファイル名になる)
    dt_now = datetime.datetime.now()
    nowtime = dt_now.strftime('%Y_%m_%d_%H_%M_%S')

    im = Image.open(file_path).convert('RGB')
    im_new = imagesquare(im, (0, 0, 0))
    im_new.save(nowtime + '_square.jpg', quality=95)
