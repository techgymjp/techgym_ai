# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 14:22:27 2019

@author: n.aoi
"""
import cv2
import numpy as np
import sys
from math import ceil
from post_processing import scale_bbox, shift_bbox
from generator import SlidingWindowGenerator

sys.path.append('./ssd_keras')
from models.keras_ssd7 import build_model
from models.keras_ssd300 import ssd_300
from models.keras_ssd512 import ssd_512
from data_generator.object_detection_2d_geometric_ops import Resize
from data_generator.object_detection_2d_photometric_ops import ConvertTo3Channels
from data_generator.object_detection_2d_data_generator import DataGenerator
from data_generator.data_augmentation_chain_constant_input_size import DataAugmentationConstantInputSize
from data_generator.data_augmentation_chain_original_ssd import SSDDataAugmentation
from ssd_encoder_decoder.ssd_input_encoder import SSDInputEncoder
from keras_loss_function.keras_ssd_loss import SSDLoss

class SSD():
    def __init__(self, model_name, n_classes = 1, mode = 'inference'):
        self.model_name = model_name
        self.n_classes = n_classes
        self.mode = mode
        
        if self.model_name == 'ssd_7':
            self.image_size = (300, 300, 3)
            self.intensity_mean = 127.5
            self.intensity_range = 127.5
            self.scales = [0.08, 0.16, 0.32, 0.64, 0.96]
            self.aspect_ratios_per_layer = None
            self.two_boxes_for_ar1 = True
            self.steps = None
            self.offsets = None
            self.clip_boxes = False
            self.variances = [1.0, 1.0, 1.0, 1.0]
            self.normalize_coords = True
            
            self.model = build_model(image_size=self.image_size,
                                     n_classes=self.n_classes,
                                     mode=self.mode,
                                     l2_regularization=0.0005,
                                     scales=self.scales,
                                     aspect_ratios_global=[0.5, 1.0, 2.0],
                                     aspect_ratios_per_layer=self.aspect_ratios_per_layer,
                                     two_boxes_for_ar1=self.two_boxes_for_ar1,
                                     steps=self.steps,
                                     offsets=self.offsets,
                                     clip_boxes=self.clip_boxes,
                                     variances=self.variances,
                                     normalize_coords=self.normalize_coords,
                                     subtract_mean=self.intensity_mean,
                                     divide_by_stddev=self.intensity_range)
        elif self.model_name == 'ssd_300':
            self.image_size = (300, 300, 3)
            self.mean_color = [123, 117, 104]
            self.swap_channels = [2, 1, 0]
            self.scales = [0.1, 0.2, 0.37, 0.54, 0.71, 0.88, 1.05]
            self.aspect_ratios_per_layer = [[1.0, 2.0, 0.5],
                                            [1.0, 2.0, 0.5, 3.0, 1.0/3.0],
                                            [1.0, 2.0, 0.5, 3.0, 1.0/3.0],
                                            [1.0, 2.0, 0.5, 3.0, 1.0/3.0],
                                            [1.0, 2.0, 0.5],
                                            [1.0, 2.0, 0.5]]
            self.two_boxes_for_ar1 = True
            self.steps = [8, 16, 32, 64, 100, 300]
            self.offsets = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5]
            self.clip_boxes = False
            self.variances = [0.1, 0.1, 0.2, 0.2]
            self.normalize_coords = True
            
            self.model = ssd_300(image_size=self.image_size,
                                 n_classes=self.n_classes,
                                 mode=self.mode,
                                 l2_regularization=0.0005,
                                 scales=self.scales,
                                 aspect_ratios_per_layer=self.aspect_ratios_per_layer,
                                 two_boxes_for_ar1=self.two_boxes_for_ar1,
                                 steps=self.steps,
                                 offsets=self.offsets,
                                 clip_boxes=self.clip_boxes,
                                 variances=self.variances,
                                 normalize_coords=self.normalize_coords,
                                 subtract_mean=self.mean_color,
                                 swap_channels=self.swap_channels)
        elif self.model_name == 'ssd_512':            
            self.image_size = (512, 512, 3)
            self.mean_color = [123, 117, 104]
            self.swap_channels = [2, 1, 0]
            self.scales = [0.07, 0.15, 0.3, 0.45, 0.6, 0.75, 0.9, 1.05]
            self.aspect_ratios_per_layer = [[1.0, 2.0, 0.5],
                                  [1.0, 2.0, 0.5, 3.0, 1.0/3.0],
                                  [1.0, 2.0, 0.5, 3.0, 1.0/3.0],
                                  [1.0, 2.0, 0.5, 3.0, 1.0/3.0],
                                  [1.0, 2.0, 0.5, 3.0, 1.0/3.0],
                                  [1.0, 2.0, 0.5],
                                  [1.0, 2.0, 0.5]]
            self.two_boxes_for_ar1 = True
            self.steps = [8, 16, 32, 64, 128, 256, 512]
            self.offsets = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]
            self.clip_boxes = False
            self.variances = [0.1, 0.1, 0.2, 0.2]
            self.normalize_coords = True
            
            self.model = ssd_512(image_size=self.image_size,
                                 n_classes=self.n_classes,
                                 mode=self.mode,
                                 l2_regularization=0.0005,
                                 scales=self.scales,
                                 aspect_ratios_per_layer=self.aspect_ratios_per_layer,
                                 two_boxes_for_ar1=self.two_boxes_for_ar1,
                                 steps=self.steps,
                                 offsets=self.offsets,
                                 clip_boxes=self.clip_boxes,
                                 variances=self.variances,
                                 normalize_coords=self.normalize_coords,
                                 subtract_mean=self.mean_color,
                                 swap_channels=self.swap_channels)
        else:
            print('creating ssd_7')
            self.model_name = 'ssd_7'
            self.image_size = (300, 300, 3)
            self.intensity_mean = 127.5
            self.intensity_range = 127.5
            self.scales = [0.08, 0.16, 0.32, 0.64, 0.96]
            self.aspect_ratios_per_layer = None
            self.two_boxes_for_ar1 = True
            self.steps = None
            self.offsets = None
            self.clip_boxes = False
            self.variances = [1.0, 1.0, 1.0, 1.0]
            self.normalize_coords = True
            
            self.model = build_model(image_size=self.image_size,
                                     n_classes=self.n_classes,
                                     mode=self.mode,
                                     l2_regularization=0.0005,
                                     scales=self.scales,
                                     aspect_ratios_global=[0.5, 1.0, 2.0],
                                     aspect_ratios_per_layer=self.aspect_ratios_per_layer,
                                     two_boxes_for_ar1=self.two_boxes_for_ar1,
                                     steps=self.steps,
                                     offsets=self.offsets,
                                     clip_boxes=self.clip_boxes,
                                     variances=self.variances,
                                     normalize_coords=self.normalize_coords,
                                     subtract_mean=self.intensity_mean,
                                     divide_by_stddev=self.intensity_range)
    
    def load_weights(self, model_path, by_name=False):
        self.model.load_weights(model_path, by_name=by_name)
    
    def set_generator(self, train_images_dir, train_annotation_path, batch_size, val_images_dir = None, val_annotation_path = None):
        train_dataset = DataGenerator(load_images_into_memory=True, hdf5_dataset_path=None)
        train_dataset.parse_json(images_dirs=[train_images_dir],
                                 annotations_filenames=[train_annotation_path],
                                 ground_truth_available=True,
                                 include_classes='all',
                                 ret=False,
                                 verbose=True)
        train_dataset_size = train_dataset.get_dataset_size()
        if self.model_name == 'ssd_7':
            # Define the image processing chain.
            ssd_data_augmentation = DataAugmentationConstantInputSize(random_brightness=(-48, 48, 0.5),
                                                                      random_contrast=(0.5, 1.8, 0.5),
                                                                      random_saturation=(0.5, 1.8, 0.5),
                                                                      random_hue=(18, 0.5),
                                                                      random_flip=0.5,
                                                                      random_translate=((0.03,0.5), (0.03,0.5), 0.5),
                                                                      random_scale=(0.5, 2.0, 0.5),
                                                                      n_trials_max=3,
                                                                      clip_boxes=True,
                                                                      overlap_criterion='area',
                                                                      bounds_box_filter=(0.3, 1.0),
                                                                      bounds_validator=(0.5, 1.0),
                                                                      n_boxes_min=1,
                                                                      background=(0,0,0))
            
            # Instantiate an encoder that can encode ground truth labels into the format needed by the SSD loss function.
            
            # The encoder constructor needs the spatial dimensions of the model's predictor layers to create the anchor boxes.
            predictor_sizes = [self.model.get_layer('classes4').output_shape[1:3],
                               self.model.get_layer('classes5').output_shape[1:3],
                               self.model.get_layer('classes6').output_shape[1:3],
                               self.model.get_layer('classes7').output_shape[1:3]]
            
        
        elif self.model_name == 'ssd_300':
            # For the training generator:
            ssd_data_augmentation = SSDDataAugmentation(img_height=self.image_size[0],
                                                        img_width=self.image_size[1],
                                                        background=self.mean_color)
            
            # 5: Instantiate an encoder that can encode ground truth labels into the format needed by the SSD loss function.
            
            # The encoder constructor needs the spatial dimensions of the model's predictor layers to create the anchor boxes.
            predictor_sizes = [self.model.get_layer('conv4_3_norm_mbox_conf').output_shape[1:3],
                               self.model.get_layer('fc7_mbox_conf').output_shape[1:3],
                               self.model.get_layer('conv6_2_mbox_conf').output_shape[1:3],
                               self.model.get_layer('conv7_2_mbox_conf').output_shape[1:3],
                               self.model.get_layer('conv8_2_mbox_conf').output_shape[1:3],
                               self.model.get_layer('conv9_2_mbox_conf').output_shape[1:3]]
        elif self.model_name == 'ssd_512':
            # For the training generator:
            ssd_data_augmentation = SSDDataAugmentation(img_height=self.image_size[0],
                                                        img_width=self.image_size[1],
                                                        background=self.mean_color)
            # 5: Instantiate an encoder that can encode ground truth labels into the format needed by the SSD loss function.
            
            # The encoder constructor needs the spatial dimensions of the model's predictor layers to create the anchor boxes.
            predictor_sizes = [self.model.get_layer('conv4_3_norm_mbox_conf').output_shape[1:3],
                               self.model.get_layer('fc7_mbox_conf').output_shape[1:3],
                               self.model.get_layer('conv6_2_mbox_conf').output_shape[1:3],
                               self.model.get_layer('conv7_2_mbox_conf').output_shape[1:3],
                               self.model.get_layer('conv8_2_mbox_conf').output_shape[1:3],
                               self.model.get_layer('conv9_2_mbox_conf').output_shape[1:3],
                               self.model.get_layer('conv10_2_mbox_conf').output_shape[1:3]]

        ssd_input_encoder = SSDInputEncoder(img_height=self.image_size[0],
                                            img_width=self.image_size[1],
                                            n_classes=self.n_classes,
                                            predictor_sizes=predictor_sizes,
                                            scales=self.scales,
                                            aspect_ratios_per_layer=self.aspect_ratios_per_layer,
                                            two_boxes_for_ar1=self.two_boxes_for_ar1,
                                            steps=self.steps,
                                            offsets=self.offsets,
                                            clip_boxes=self.clip_boxes,
                                            variances=self.variances,
                                            matching_type='multi',
                                            pos_iou_threshold=0.5,
                                            neg_iou_limit=0.5,
                                            normalize_coords=self.normalize_coords)
        
        self.generator = train_dataset.generate(batch_size=batch_size,
                                                shuffle=True,
                                                transformations=[ssd_data_augmentation],
                                                label_encoder=ssd_input_encoder,
                                                returns={'processed_images',
                                                         'encoded_labels'},
                                                keep_images_without_gt=False)
        self.steps_per_epoch = ceil(train_dataset_size/batch_size)
            
        if val_images_dir is not None and val_annotation_path is not None:
            val_dataset = DataGenerator(load_images_into_memory=True, hdf5_dataset_path=None)
            val_dataset.parse_json(images_dirs=[val_images_dir],
                                   annotations_filenames=[val_annotation_path],
                                   ground_truth_available=True,
                                   include_classes='all',
                                   ret=False,
                                   verbose=True)
            val_dataset_size   = val_dataset.get_dataset_size()

            if self.model_name == 'ssd_300' or self.model_name == 'ssd_512':
                # For the validation generator:
                convert_to_3_channels = ConvertTo3Channels()
                resize = Resize(height=self.image_size[0], width=self.image_size[1])
                transformations = [convert_to_3_channels, resize]
            else:
                transformations = []
            
            self.validation_data = val_dataset.generate(batch_size=batch_size,
                                                 shuffle=False,
                                                 transformations=transformations,
                                                 label_encoder=ssd_input_encoder,
                                                 returns={'processed_images',
                                                          'encoded_labels'},
                                                 keep_images_without_gt=False)
            self.validation_steps = ceil(val_dataset_size/batch_size)
            
        else:
            self.validation_data = None
            self.validation_steps = None
    
    def freeze_layers(self):
        assert self.model_name == 'ssd_300' or self.model_name == 'ssd_512'
        freeze_layers = ['conv1_1', 'conv1_2',
                         'conv2_1', 'conv2_2',
                         'conv3_1', 'conv3_2', 'conv3_3']
        for layer in self.model.layers:
            if layer.name in freeze_layers:
                layer.trainable = False
        
    def train(self, epochs, optimizer, callbacks=None):
        ssd_loss = SSDLoss(neg_pos_ratio=3, alpha=1.0)
        self.model.compile(optimizer=optimizer, loss=ssd_loss.compute_loss)
        
        self.model.fit_generator(generator=self.generator,
                                 steps_per_epoch=self.steps_per_epoch,
                                 epochs=epochs,
                                 callbacks=callbacks,
                                 validation_data=self.validation_data,
                                 validation_steps=self.validation_steps)
    
    def predict(self, img_path, transform=None):
        """
        args:
            img_path: path to image file
            transform: transformation function
        returns: predicted bounding boxes
            - category_id
            - score
            - bbox
               - x1
               - y1
               - x2
               - y2
        """
        
        img = cv2.imread(img_path)
        if img is not None:
            original_height_width = img.shape[:-1]
            predictions = []
            img_resized = cv2.resize(img, self.image_size[:-1])[:,:,::-1]
            if transform is not None:
                img_resized = transform[0](img_resized)
            y_pred = self.model.predict(np.array([img_resized]))[0]
            for bbox in y_pred:
                result = self._post_process_bb(bbox, original_height_width, transform)
                predictions.append(result)
            
            return predictions
        else:
            print('could not read the image file.')
    
    def predict_sw(self, img_path, window_size, stride, transform = None, batch_size=32):
        """
        args:
            img_path: path to image file
            window_size: window size
            srtide: length of stride
            transform: transformation function
        returns: predicted bounding boxes
            - category_id
            - score
            - bbox
               - x1
               - y1
               - x2
               - y2
        """
        predictions = []
        gen = SlidingWindowGenerator(img_path=img_path,
                                     image_size=self.image_size,
                                     window_size=window_size,
                                     stride=stride,
                                     batch_size=batch_size,
                                     transform=transform)
        original_height_width = gen.height, gen.width    # window size
        
        for coords, mini_batch in gen:
            y_preds = self.model.predict_on_batch(mini_batch)
            for coord, y_pred in zip(coords, y_preds):
                for bbox in y_pred:
                    result = self._post_process_bb(bbox, original_height_width, transform)
                    result['bbox'] = shift_bbox(result['bbox'], coord)
                    predictions.append(result)
        
        return predictions
    
    def _post_process_bb(self, bbox, original_height_width, transform=None):
        category_id = bbox[0]
        score = bbox[1]
        x1, y1, x2, y2 = bbox[2:]
        if transform is not None:
            x1, y1, x2, y2 = transform[1]((x1, y1, x2, y2), self.image_size)
        x1, y1, x2, y2 = scale_bbox((x1, y1, x2, y2), self.image_size[:-1], original_height_width)
        
        return {'category_id':category_id, 'score': score, 'bbox':(x1, y1, x2, y2)}


if __name__ == '__main__':
    import time
    model = SSD('ssd_300')
    model.load_weights('trained_models/ssd300.h5')
    img_path = 'competition_data/val_images/test_05_1.jpg'
    s = time.time()
    predictions = model.predict_sw(img_path, (300, 300), 300)
    print(time.time()-s)