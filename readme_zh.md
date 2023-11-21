# 通用文档版面分析

## 一、项目介绍：

本项目目标在于提供一个通用的文档版面分析模型。
版面分析在当下的作用，主要用于解决文档解析中，OCR的文字片段合并问题。
如双栏文字，ocr识别后可能会由于后处理不当导致乱序等。
文本乱序，对后续大模型解析等应用都会产生较大影响。你可以使用本项目解决扫描pdf解析，图片解析等问题。
ocr开源项目较多，排序模型参考xy_cut。本项目暂不添加此模块。


**模型框架为Yolo-V5，使用两阶段训练方式：**

* 一阶段：基于开源的科技论文及新闻等领域的数据集。旨在模型适应文档布局，各种要素（图像，文本，表格）的通用特征提取。

* 二阶段：自行构建更为丰富的领域文档标注数据集。自行收集复杂文档版面图片，使用一阶段模型，接入label-studio，进行预标注，随后人工调整。

**说明：**

1、支持3种版面元素：【文本块，图像，表格】。 

本项目简化冗余元素，如公式、页眉、页脚之类的元素。原因是这些元素对于文档文本内容还原并不重要。

2、表格 类型的元素，可供你接入table_paser 等三方客制模型。你可以藉此将表格图片切出，输入表格解析模型，输出结构化表格。

## 二、推理

1、单图推理 `python infer.py` 

2、批量推理 `python3 detect.py --source ./inference/images/ --weights weights/layout.pt --conf 0.5 --device cpu`

权重下载，权重主要包含两部分：

1、yolov5x：链接：https://pan.baidu.com/s/19PxE7iWRYhD2FSGln8960g 
提取码：4j3l

2、Layout：链接：https://pan.baidu.com/s/1HoERqJgErZR0p0-8ogA5Tg 
提取码：fveg


## 三、训练

`sh train.sh`

参数说明及注意事项：

1、`--data data/layout.yaml`

训练前，请注意你的数据配置正确：配置文件位于`data/layout.yaml`
若需更改支持的类型，请修改相应配置文件。
训练数据格式为yolo数据格式。

2、`--cfg models/score/yolov5x.yaml`

config 文件，若类型数量有变，请注意配置配置文件中的 nc = num your class


## 4、效果展示


<img align="center" src="inference/output/img.png" width="50%" height="50%">


<img align="center" src="inference/output/img_1.png" width="50%" height="50%">


<img align="center" src="inference/output/201805221604304170.png" width="50%" height="50%">


## 5、本项目基于如下项目开发，感谢原作及原始yolo作者。
https://github.com/DataXujing/YOLO-v5

