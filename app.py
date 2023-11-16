# -*- coding: utf-8 -*-
# @Time    : 2022/9/8 15:44
# @Author  : OKC
import json
from flask import request
from flask import Flask,make_response
from flask_cors import CORS
from infer import YOLOv5
import numpy as np
import cv2

app = Flask(__name__)
CORS(app, supports_credentials=True)
det = YOLOv5(device='0')

id2clss = {"0":'Text',"1":"Table"} #'Text','Title','Figure','Table
@app.route("/infer", methods=["POST"])
def predict():
    result = {"success": False}
    if request.method == "POST":
        if request.files.get("image") is not None:
            # 得到客户端传输的图像
            filename = request.files['image'].filename
            input_image = request.files["image"].read()
            imBytes = np.frombuffer(input_image, np.uint8)
            iImage = cv2.imdecode(imBytes, cv2.IMREAD_COLOR)
            save_img = request.form.get("save_img")
            if save_img=='Y':
                save_img = True
            else:
                save_img = False

            # 执行推理
            outs = det.infer(iImage,filename,save_img=save_img)
            if (outs is None) and (len(outs) < 0):
                result["success"] = False
            # 将结果保存为json格式
            original_list = []
            for box,conf,classid in zip(outs[0].tolist(),outs[1].tolist(),outs[2].tolist()):
                original_list.append({"type":id2clss.get(str(int(classid))),"conf":conf,"box":box})

            result_dict = {}
            [result_dict.setdefault(item.pop('type'), []).append(item) for item in original_list]

            result["out"] = result_dict
            result['success'] = True
            # 图片
            result["base64_img"] = outs[-1]
            # base64 图片保存
            import base64
            # decoded_data = base64.b64decode(outs[-1])
            # 将二进制数据保存为图片文件
            decoded_data = base64.b64decode(outs[-1])
            with open('fund.jpg', 'wb') as image_file:
                image_file.write(decoded_data)

            rst = json.dumps(result, ensure_ascii=False)
            response = make_response(rst)
            response.headers["Content-Type"] = "application/json; charset=utf-8"

    return response


if __name__ == "__main__":
    print(("* Loading yolov5 model and Flask starting server..."
           "please wait until server has fully started"))
    app.run(host='0.0.0.0', port=7401)

    # gunicorn app:app -c ./gunicorn_config.py

