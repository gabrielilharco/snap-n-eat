# Snap & Eat (formerly deep139)
Deep Learning Hackathon 48h - Cotidiano (**First place Project =D** )

We believe nutrition tracking should be as simple as taking a picture.

Snap & Eat is a web application that tracks the user's food intake by pictures. We use state-of-the-art deep learning techniques to recognize dishes, making instant nutrition estimates from the user's meals.

## Demo

![test](data/results/app_homescreen.jpg) 
![test](data/results/food_prediction.jpg)  

## Our model

We use an [Aggregated Residual Convolutional Neural Network](https://arxiv.org/abs/1611.05431) - ResNeXt-101 with 101 layers, pretrained on [ImageNet](http://www.image-net.org/) dataset. We finetune the model on [Food-101 dataset](https://www.vision.ee.ethz.ch/datasets_extra/food-101/), and achieve a significant improvement on accuracy (71% in our work compared to [Bossard et al., 2014](http://www.vision.ee.ethz.ch/~lbossard/bossard_eccv14_food-101.pdf)).

For recomending new dishes, we use minimum ditance in an n-dimensional space of nutritional information that describe each dish.

## Instalation and usage

Dependencies:

- [fastai lib](https://github.com/fastai/fastai)
- Flask
- Node.js

# About the idea

To be written.