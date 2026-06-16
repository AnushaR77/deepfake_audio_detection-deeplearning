# Deepfake audio detection 
```
https://deepfakeaudiodetection-deeplearning.streamlit.app/
```
The project explores the use of audio signal processing techniques combined with deep learning-based transfer learning for deepfake audio detection.

## Dataset
```
/kaggle/input/datasets/mohammedabdeldayem/the-fake-or-real-dataset
```
The project uses the Fake-or-Real (FoR) dataset containing recordings from:
- Real human speakers
- Synthetic speech generated using modern TTS systems
Contains four category of data: `Normal` `Original` `2-sec` `Rerec`

## Method 1
> Fine Tunning ResNet34
# Preprocessing audio
- audio preprocessing is done using `librosa` python library
- Mel spectogram was generated which is used as image representation of audio signal.

# Transfer learning using ResNet34
- Pretrained ResNet 34 is used and fine tunned, ResNet 34 is used because it solves the problem of vanishing gradiesnt which happens in CNN build from scratch
- but the issue with this pipeline was the data set was not
