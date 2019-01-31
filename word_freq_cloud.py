import pandas as pd
import re # 正则表达式库
import collections # 词频统计库
import numpy as np # numpy数据处理库
import jieba # 结巴分词
from wordcloud import WordCloud # 词云展示库
from PIL import Image # 图像处理库
import matplotlib.pyplot as plt # 图像展示库
import codecs
import jieba.analyse
from scipy.misc import imread
import os
from os import path
import matplotlib.pyplot as plt


#载入停用词
stopwords = [line.strip() for line in codecs.open('stopwords.txt', 'r', 'gbk').readlines()]

rows=pd.read_excel('Chairman.xlsx',encoding='gbk',dtype=str)

#记录每条数据的分词情况
word_freq=[]

for i in range(5):
    cut_text = " ".join(jieba.cut(rows['背景'][i]))
    result = jieba.analyse.textrank(cut_text, topK=50, withWeight=True)
    # 生成关键词比重字典
    keywords = dict()
    for j in result:
        keywords[j[0]]=j[1]
        
    word_freq.append(keywords)
    
    d = path.dirname(r'C:\Users\chenyf\Desktop\Chairman') # 当前文件文件夹所在目录
    color_mask = imread("chairman.png") # 读取背景图片
    cloud = WordCloud(
        #设置字体，不指定就会出现乱码
        #font_path="./fonts/Simfang.ttf",
        font_path=path.join(d,'simsun.ttc'),
        width=200,
        height=200,
        #设置背景色
        background_color='white',
        #词云形状
        mask=color_mask,
        #允许最大词汇
        max_words=2000,
        #最大号字体
        max_font_size=60
    )
    word_cloud = cloud.generate(cut_text)# 产生词云
    output_name='result'+ str(i)+'.jpg'
    word_cloud.to_file(output_name) #保存图片
    #显示词云图片
    #plt.imshow(word_cloud)
    #plt.axis('off')
    #plt.show()
