from PIL import Image
import io
import numpy as np

def load_img_fastai(img_bytes):
    img = Image.open(io.BytesIO(img_bytes.read()))
    img = img.convert('RGB')
    img.to_thumb(224,224)
    img = np.array(img)

    return img