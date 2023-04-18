import tkinter as tk
import customtkinter as ctk
from PIL import ImageTk

import torch
from torch import autocast
from diffusers import StableDiffusionPipeline
app = tk.Tk()
app.geometry("532x622")
app.title("Stabble diffusion")
ctk.set_appearance_mode("dark")
prompt = ctk.CTkEntry(height=40, width=512, text_font="Arial", text_color="black", fg_color="white")
prompt.place(x=10, y=10)
lmain = ctk.CTkLabel(height=512, width=512, text_font="Arial", text_color="white", fg_color="blue")
lmain.place(x=10, y=10)

modelid = "CompVis/stable-diffusion-v1-5"
pipe = StableDiffusionPipeline.from_pretrained(modelid, revision="fp16", torch_dtype=torch.float16, use_auth_token = "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" )
device = 'cuda'
pipe.to(device)
def generate():
    with autocast(device):
        image = pipe(prompt.get(), guidance_scale=8.5)['sample'][0]
    image.save("generatedimage.png")
    img = ImageTk.PhotoImage(image)
    lmain.configure(image = img)    
trigger = ctk.CTkButton(height=40, width=120, text_font="Arial", text_color="white", fg_color="blue", command=generate)
trigger.place(x=206, y=60)
trigger.configure(text="Generate")