# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 12:03:30 2019

@author: n.aoi
"""

def compute_iou_bb(pred_bb, true_bb):
    pred_area = (pred_bb[2]-pred_bb[0])*(pred_bb[3]-pred_bb[1])
    true_area = (true_bb[2]-true_bb[0])*(true_bb[3]-true_bb[1])
    intersection_x = max(min(pred_bb[2],true_bb[2])-max(pred_bb[0],true_bb[0]),0)
    intersection_y = max(min(pred_bb[3],true_bb[3])-max(pred_bb[1],true_bb[1]),0)
    intersection_area = intersection_x*intersection_y
    union_area = pred_area+true_area-intersection_area
    if union_area>0:
        return intersection_area/union_area
    else:
        return 0