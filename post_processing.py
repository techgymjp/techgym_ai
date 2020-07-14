# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 23:42:18 2019

@author: n.aoi
"""
import numpy as np
from utils import compute_iou_bb

def scale_bbox(bbox, in_shape, out_shape):
    height_ratio = out_shape[0]/in_shape[0]
    width_ratio = out_shape[1]/in_shape[1]
    out_bbox = bbox[0]*width_ratio, bbox[1]*height_ratio, bbox[2]*width_ratio, bbox[3]*height_ratio
    
    return out_bbox

def shift_bbox(bbox, offset):
    x1, y1, x2, y2 =  bbox
    out_bbox = offset[0] + x1, offset[1] + y1, offset[0] + x2, offset[1] + y2

    return out_bbox

def pad_image(img, size):
    height, width = size
    if img.shape[0]!=height or img.shape[1]!=width:
        img_pad = np.zeros((height, width, 3))
        img_pad[:img.shape[0], :img.shape[1], :] = img
        
        return img_pad
    else:
        return img
    
def nms(predictions, thresh=0.5):
    # initialize
    for i, prediction in enumerate(predictions):
        prediction.update({'bbox_id':i})
    
    out_predictions = []
    while len(predictions):
        # sort predictions in order of confidence
        predictions = sorted(predictions, key=lambda x:x['score'], reverse=True)
        
        # get bbox of the highest confidence
        index = predictions[0]['bbox_id']
        pred = _get_prediction_from_bbox_id(index, predictions)
        
        # add to the output
        out_predictions.append(pred)
        
        # remove the bbox and the bboxes which have higher iou than the threshold
        _remove_elements({index}, predictions)
        temp_not_show = {prediction['bbox_id'] for prediction in predictions if compute_iou_bb(pred['bbox'], prediction['bbox'])>thresh}
        _remove_elements(temp_not_show, predictions)
    
    return out_predictions

def _remove_elements(indices, predictions):
    for index in indices:
        pred = _get_prediction_from_bbox_id(index, predictions)
        predictions.remove(pred)
    
def _get_prediction_from_bbox_id(i, predictions):
    for prediction in predictions:
        if prediction['bbox_id']==i:
            return prediction

if __name__ == '__main__':
    predictions = [{'category_id':1, 'score': 0.8, 'bbox':(0,0,100,100)},
                   {'category_id':1, 'score': 0.9, 'bbox':(100,100,200,200)},
                   {'category_id':1, 'score': 0.5, 'bbox':(100,0,200,100)},
                   {'category_id':1, 'score': 0.3, 'bbox':(0,0,50,100)}]
    print(predictions[0])
    out = nms(predictions, thresh = 0.5)
    print(predictions[0])    