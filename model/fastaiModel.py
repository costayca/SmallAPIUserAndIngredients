import torch
import fastai 
fastai.device = torch.device('cpu')
from fastai.vision.all import *

# import pathlib
# temp = pathlib.PosixPath
# pathlib.PosixPath = pathlib.WindowsPath

learn = load_learner("./model/resnet_34_8_mult_2_70_test.pkl")

# dest = "./model/62787.jpg"
# im = Image.open(dest)
# im.to_thumb(224,224)
# im = np.array(im)
# print(learn.predict(im)[0])

# dest = "./model/62832.jpg"
# im = Image.open(dest)
# im.to_thumb(224,224)
# im = np.array(im)
# print(learn.predict(im)[0])

# dest = "./model/110043.jpg"
# im = Image.open(dest)
# im.to_thumb(224,224)
# im = np.array(im)
# print(learn.predict(im)[0])

# dest = "./model/136256.jpg"
# im = Image.open(dest)
# im.to_thumb(224,224)
# im = np.array(im)
# print(learn.predict(im)[0])