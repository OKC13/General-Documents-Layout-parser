<a href="https://apps.apple.com/app/id1452689527" target="_blank">
<img src="readmepic/readme1/82944393-f7644d80-9f4f-11ea-8b87-1a5b04f555f1.jpg" width="1000"></a>
&nbsp

This repository represents Ultralytics open-source research into future object detection methods, and incorporates our lessons learned and best practices evolved over training thousands of models on custom client datasets with our previous YOLO repository https://github.com/ultralytics/yolov3. **All code and models are under active development, and are subject to modification or deletion without notice.** Use at your own risk.

<img src="readmepic/readme1/84200349-729f2680-aa5b-11ea-8f9a-604c9e01a658.png" width="1000">** GPU Latency measures end-to-end latency per image averaged over 5000 COCO val2017 images using a V100 GPU with batch size 32, and includes image preprocessing, PyTorch FP32 inference, postprocessing and NMS.

- **June 9, 2020**: [CSP](https://github.com/WongKinYiu/CrossStagePartialNetworks) updates to all YOLOv5 models. New models are faster, smaller and more accurate. Credit to @WongKinYiu for his excellent work with CSP. 
- **May 27, 2020**: Public release of repo. YOLOv5 models are SOTA among all known YOLO implementations, YOLOv5 family will be undergoing architecture research and development over Q2/Q3 2020 to increase performance. Updates may include [CSP](https://github.com/WongKinYiu/CrossStagePartialNetworks) bottlenecks, [YOLOv4](https://github.com/AlexeyAB/darknet) features, as well as PANet or BiFPN heads.
- **April 1, 2020**: Begin development of a 100% PyTorch, scaleable YOLOv3/4-based group of future models, in a range of compound-scaled sizes. Models will be defined by new user-friendly `*.yaml` files. New training methods will be simpler to start, faster to finish, and more robust to training a wider variety of custom dataset.


## Pretrained Checkpoints

| Model | AP<sup>val</sup> | AP<sup>test</sup> | AP<sub>50</sub> | Latency<sub>GPU</sub> | FPS<sub>GPU</sub> || params | FLOPs |
|---------- |------ |------ |------ | -------- | ------| ------ |------  |  :------: |
| YOLOv5-s ([ckpt](https://drive.google.com/open?id=1Drs_Aiu7xx6S-ix95f9kNsA6ueKRpN2J))    | 35.5     | 35.5     | 55.0     | **2.5ms** | **400** || 7.1M   | 12.6B
| YOLOv5-m ([ckpt](https://drive.google.com/open?id=1Drs_Aiu7xx6S-ix95f9kNsA6ueKRpN2J))    | 42.7     | 42.7     | 62.4     | 4.4ms     | 227     || 22.0M  | 39.0B
| YOLOv5-l ([ckpt](https://drive.google.com/open?id=1Drs_Aiu7xx6S-ix95f9kNsA6ueKRpN2J))    | 45.7     | 45.9     | 65.1     | 6.8ms     | 147     || 50.3M  | 89.0B
| YOLOv5-x ([ckpt](https://drive.google.com/open?id=1Drs_Aiu7xx6S-ix95f9kNsA6ueKRpN2J))    | **47.2** | **47.3** | **66.6** | 11.7ms    | 85      || 95.9M | 170.3B
| YOLOv3-SPP ([ckpt](https://drive.google.com/open?id=1Drs_Aiu7xx6S-ix95f9kNsA6ueKRpN2J))  | 45.6     | 45.5     | 65.2     | 7.9ms     | 127     || 63.0M  | 118.0B

** AP<sup>test</sup> denotes COCO [test-dev2017](http://cocodataset.org/#upload) server results, all other AP results in the table denote val2017 accuracy.  
** All AP numbers are for single-model single-scale without ensemble or test-time augmentation. Reproduce by `python test.py --img 736 --conf 0.001`  
** Latency<sub>GPU</sub> measures end-to-end latency per image averaged over 5000 COCO val2017 images using a GCP [n1-standard-16](https://cloud.google.com/compute/docs/machine-types#n1_standard_machine_types) instance with one V100 GPU, and includes image preprocessing, PyTorch FP32 inference at batch size 32, postprocessing and NMS. Average NMS time included in this chart is 1-2ms/img.  Reproduce by `python test.py --img 640 --conf 0.1`  
** All checkpoints are trained to 300 epochs with default settings and hyperparameters (no autoaugmentation). 


## Requirements

Python 3.7 or later with all `requirements.txt` dependencies installed, including `torch >= 1.5`. To install run:
```bash
$ pip install -U -r requirements.txt
```


## Tutorials

* <a href="https://colab.research.google.com/github/ultralytics/yolov5/blob/master/tutorial.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"></a>
* [Train Custom Data](https://github.com/ultralytics/yolov5/wiki/Train-Custom-Data)
* [Google Cloud Quickstart Guide](https://github.com/ultralytics/yolov5/wiki/GCP-Quickstart)
* [Docker Quickstart Guide](https://github.com/ultralytics/yolov5/wiki/Docker-Quickstart) 


## Inference

Inference can be run on most common media formats. Model [checkpoints](https://drive.google.com/open?id=1Drs_Aiu7xx6S-ix95f9kNsA6ueKRpN2J) are downloaded automatically if available. Results are saved to `./inference/output`.
```bash
$ python detect.py --source file.jpg  # image 
                            file.mp4  # video
                            ./dir  # directory
                            0  # webcam
                            rtsp://170.93.143.139/rtplive/470011e600ef003a004ee33696235daa  # rtsp stream
                            http://112.50.243.8/PLTV/88888888/224/3221225900/1.m3u8  # http stream
```

To run inference on examples in the `./inference/images` folder:

```bash
$ python detect.py --source ./inference/images/ --weights yolov5s.pt --conf 0.4

Namespace(agnostic_nms=False, augment=False, classes=None, conf_thres=0.4, device='', fourcc='mp4v', half=False, img_size=640, iou_thres=0.5, output='inference/output', save_txt=False, source='./inference/images/', view_img=False, weights='yolov5s.pt')
Using CUDA device0 _CudaDeviceProperties(name='Tesla P100-PCIE-16GB', total_memory=16280MB)

Downloading https://drive.google.com/uc?export=download&id=1R5T6rIyy3lLwgFXNms8whc-387H0tMQO as yolov5s.pt... Done (2.6s)

image 1/2 inference/images/bus.jpg: 640x512 3 persons, 1 buss, Done. (0.009s)
image 2/2 inference/images/zidane.jpg: 384x640 2 persons, 2 ties, Done. (0.009s)
Results saved to /content/yolov5/inference/output
```

<img src="readmepic/readme1/83082816-59e54880-a039-11ea-8abe-ab90cc1ec4b0.jpeg" width="500">  

## Reproduce Our Training

Run command below. Training times for yolov5s/m/l/x are 2/4/6/8 days on a single V100 (multi-GPU times faster).
```bash
$ python train.py --data coco.yaml --cfg yolov5s.yaml --weights '' --batch-size 16                                      
```
<img src="readmepic/readme1/84186698-c4d54d00-aa45-11ea-9bde-c632c1230ccd.png" width="900">


## Reproduce Our Environment

To access an up-to-date working environment (with all dependencies including CUDA/CUDNN, Python and PyTorch preinstalled), consider a:

- **GCP** Deep Learning VM with $300 free credit offer: See our [GCP Quickstart Guide](https://github.com/ultralytics/yolov5/wiki/GCP-Quickstart) 
- **Google Colab Notebook** with 12 hours of free GPU time. <a href="https://colab.research.google.com/github/ultralytics/yolov5/blob/master/tutorial.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"></a>
- **Docker Image** https://hub.docker.com/r/ultralytics/yolov5. See [Docker Quickstart Guide](https://github.com/ultralytics/yolov5/wiki/Docker-Quickstart) ![Docker Pulls](https://img.shields.io/docker/pulls/ultralytics/yolov5?logo=docker)


## Citation

[![DOI](https://zenodo.org/badge/146165888.svg)](https://zenodo.org/badge/latestdoi/146165888)


## About Us

Ultralytics is a U.S.-based particle physics and AI startup with over 6 years of expertise supporting government, academic and business clients. We offer a wide range of vision AI services, spanning from simple expert advice up to delivery of fully customized, end-to-end production solutions, including:
- **Cloud-based AI** surveillance systems operating on **hundreds of HD video streams in realtime.**
- **Edge AI** integrated into custom iOS and Android apps for realtime **30 FPS video inference.**
- **Custom data training**, hyperparameter evolution, and model exportation to any destination.

For business inquiries and professional support requests please visit us at https://www.ultralytics.com. 


## Contact

**Issues should be raised directly in the repository.** For business inquiries or professional support requests please visit https://www.ultralytics.com or email Glenn Jocher at glenn.jocher@ultralytics.com. 
