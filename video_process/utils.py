# encoding: utf-8
"""
@contact: liuguiyang15@mails.ucas.edu.cn
@file: utils.py
@time: 2018/5/28 13:22
"""

import os
import time
from multiprocessing import Pool

import cv2
import numpy as np


def read_video(video_path, is_show=False):
    if not os.path.isfile(video_path):
        raise IOError("{} file not found !".format(video_path))
    if is_show:
        cv2.namedWindow("src", 0)
    frame_list = []
    cap = cv2.VideoCapture(video_path)
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            frame_list.append(frame)
        if ret and is_show:
            cv2.imshow("src", frame)
            ch = cv2.waitKey()
            if ch == ord('q'):
                break
        elif ret == False:
            break
    return frame_list


def split_image(frame, sub_wid, sub_high, step_over=0.2):
    """
    :param frame: 待处理的图像
    :param sub_wid: 子图的宽
    :param sub_high: 子图的高
    :param step_over: 相邻子图之间像素的覆盖率
    """
    frame_detail_dict = dict()
    position_list = list()
    sub_frame_list = list()

    h, w = frame.shape[:2]
    step_wid = int(sub_wid * (1 - step_over))
    step_high = int(sub_high * (1 - step_over))
    for x in range(0, w, step_wid):
        for y in range(0, h, step_high):
            e_x = x + sub_wid
            e_y = y + sub_high
            if e_x >= w:
                e_x = w
                x = e_x - sub_wid
            if e_y >= h:
                e_y = h
                y = e_y - sub_high
            sub_frame = frame[y:e_y, x:e_x]
            frame_detail_dict[(x, y, e_x, e_y)] = sub_frame
            position_list.append([x, y, e_x, e_y])
            sub_frame_list.append(sub_frame)

    np_position_list = np.array(position_list)
    np_sub_frame_list = np.array(sub_frame_list)

    frame_detail_dict["np_position_list"] = np_position_list
    frame_detail_dict["np_sub_frame_list"] = np_sub_frame_list

    return frame_detail_dict


def long_time_task(frame_id, frame):
    start = time.time()

    sub_wid, sub_high = 300, 300
    frame_detail_dict = split_image(frame, sub_wid, sub_high)
    frame_detail_dict["frame_id"] = frame_id

    end = time.time()
    print('Task %s runs %0.2f seconds.' % (frame_id, (end - start)))

    return frame_detail_dict


if __name__ == '__main__':
    video_path = "/Users/liuguiyang/Desktop/satellite_video/JL101B_MSS_20160904180811_000013363_101_001_L1B_MSS.mp4"
    frame_list = read_video(video_path)

    print('Parent process %s.' % os.getpid())
    results = list()
    p = Pool(processes=3)
    f_id = -1
    for frame in frame_list:
        f_id += 1
        results.append(p.apply_async(long_time_task, args=(f_id, frame,)))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')

    video_detail_dict = dict()
    for res_iter in results:
        frame_detail_dict = res_iter.get()
        video_detail_dict[frame_detail_dict["frame_id"]] = frame_detail_dict
    print(video_detail_dict)
