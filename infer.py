# -*- coding: utf-8 -*-
# @Time    : 2022/9/8 15:37
# @Author  : OKC
from utils.datasets import *
from utils.utils import *
import base64

class YOLOv5(object):
    # 参数设置
    _defaults = {
        "weights": "./weights/yolov5x.pt",
        "imgsz": 640,
        "iou_thres": 0.45,
        "conf_thres": 0.3,
         "classes": 0  # 只检测表格
    }

    @classmethod
    def get_defaults(cls, n):
        if n in cls._defaults:
            return cls._defaults[n]
        else:
            return "Unrecognized attribute name '" + n + "'"

    # 初始化操作，加载模型
    def __init__(self, device='0', **kwargs):
        self.__dict__.update(self._defaults)
        self.device = torch_utils.select_device(device)
        self.half = False
        self.weights = './weights/layout.pt'
        self.model = torch.load(self.weights, map_location=self.device)['model']  # load FP32 model
        self.imgsz = 640 # check img_size

    # 推理部分
    def infer(self, inImg , filename, save_img = False):
        # 使用letterbox方法将图像大小调整为640大小
        img = letterbox(inImg, new_shape=self.imgsz)[0]
        # 归一化与张量转换
        img = img[:, :, ::-1].transpose(2, 0, 1)  # BGR to RGB, to 3x416x416
        img = np.ascontiguousarray(img)
        img = torch.from_numpy(img).to(self.device)
        img = img.half() if self.half else img.float()  # uint8 to fp16/32
        img /= 255.0  # 0 - 255 to 0.0 - 1.0
        im0 = inImg

        if img.ndimension() == 3:
            img = img.unsqueeze(0)

        # 推理
        pred = self.model(img, augment=True)[0]
        # NMS
        pred = non_max_suppression(pred, self.conf_thres, self.iou_thres, classes=self.classes, agnostic=True)

        bbox_xyxy = []
        confs = []
        cls_ids = []
        names = ['Text','Table',"Figure"]
        colors = [[random.randint(0, 255) for _ in range(3)] for _ in range(len(names))]

        # 解析检测结果
        for i, det in enumerate(pred):  # detections per image
            if det is not None and len(det):
                # 将检测框映射到原始图像大小
                det[:, :4] = scale_coords(img.shape[2:], det[:, :4], inImg.shape).round()
                # 保存结果
                for *xyxy, conf, cls in reversed(det):
                    bbox_xyxy.append(xyxy)
                    confs.append(conf.item())
                    cls_ids.append(int(cls.item()))

                    if save_img:  # Add bbox to image
                        label = '%s %.2f' % (names[int(cls)], conf)
                        plot_one_box(xyxy, im0, label=label, color=colors[int(cls)], line_thickness=2)

                xyxys = torch.Tensor(bbox_xyxy)
                confss = torch.Tensor(confs)
                cls_ids = torch.Tensor(cls_ids)
            else:
                xyxys = torch.Tensor(bbox_xyxy)
                confss = torch.Tensor(confs)
                cls_ids = torch.Tensor(cls_ids)

        if save_img:
            retval, buffer = cv2.imencode('.jpg', im0)
            img_base64 = base64.b64encode(buffer).decode('utf-8')
        else:
            img_base64 = ''
            # cv2.imwrite('saved_imgs/'+filename, im0)

        return xyxys, confss, cls_ids, img_base64


    def crop_img(self):
        # 图片裁切并且归档
        return


if __name__ == '__main__':
    det = YOLOv5(device='0')
    filename = ''
    iImage = cv2.imread('inference/images/val_0007.jpg')
    outs = det.infer(iImage, filename)
    print(outs[0].tolist())
