import gradio as gr
import numpy as np


def sepia(input_img):
    """Apply a sapia filter to a numpy image"""
    sepia_filter = np.array(
        [0.393, 0.769, 0.189,
         0.349, 0.686, 0.168,
         0.272, 0.534, 0.131]
    )

    sepia_img = input_img.dot(sepia_filter.T)
    sepia_img /= sepia_img.max()
    print(input_img.shape, sepia_img.shape)
    return sepia_img


demo = gr.Interface(sepia, gr.Image(), "image")
demo.launch()
