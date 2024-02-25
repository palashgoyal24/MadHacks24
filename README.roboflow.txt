
Severstal-steel-defects - v1 2024-02-24 2:14pm
==============================

This dataset was exported via roboflow.com on Feb 24 2024 

Roboflow is an end-to-end computer vision platform that helps you
* collaborate with your team on computer vision projects
* collect & organize images
* understand and search unstructured image data
* annotate, and create datasets
* export, train, and deploy computer vision models
* use active learning to improve your dataset over time

For state of the art Computer Vision training notebooks you can use with this dataset,
visit https://github.com/roboflow/notebooks

To find over 100k other datasets and pre-trained models, visit https://universe.roboflow.com

The dataset includes 11998 images.
Steel-Defects are annotated in YOLOv8 format.

The following pre-processing was applied to each image:
* Auto-orientation of pixel data (with EXIF-orientation stripping)
* Resize to 512x256 (Stretch)

The following augmentation was applied to create 2 versions of each source image:
* 50% probability of horizontal flip
* 50% probability of vertical flip
* Random brigthness adjustment of between -20 and +20 percent
* Salt and pepper noise was applied to 5 percent of pixels


