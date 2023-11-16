CUDA_VISIBLE_DEVICES=3 python3 train.py --adam --batch-size 16 --epochs 300 \
--data data/fund_three.yaml \
--cfg models/score/yolov5x.yaml \
--weights weights/best_cdla3.pt