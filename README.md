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
- but the issue with this pipeline was the data set is not balanced audio duration wise, i.e. real training data is of `4 second mean` duration and fake is of `1.5 seconds` duration
- i have applied preprocessing steps like tranculation, padding, weight bias for fake class, changed the loss function but the model is learning only real data set and ignoring fake data and hence predicting almost everything as real.

## Method 2 
> Fine tunning wav2vec2 pretrained model
Wav2vec2 directly operates on raw audio waveforms
# Preprocessing  audio
- audio loaded using librosa
