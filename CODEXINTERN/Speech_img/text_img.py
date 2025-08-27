import customtkinter as ctk
from PIL import Image, ImageTk
from authtoken import auth_token

import torch
from diffusers import StableDiffusionPipeline

app = ctk.CTk()
app.geometry("532x632")
app.title("Stable Bud")
ctk.set_appearance_mode("dark")


prompt = ctk.CTkEntry(
    app,
    height=40, 
    width=512, 
    font=("Arial", 20), 
    text_color="black",
    fg_color="white"
)
prompt.place(x=10, y=10)


lmain = ctk.CTkLabel(app, height=512, width=512, text="")
lmain.place(x=10, y=110)

modelid = "CompVis/stable-diffusion-v1-4"
device = "cpu"

pipe = StableDiffusionPipeline.from_pretrained(
    modelid,
    use_auth_token=auth_token
)
pipe.to(device)

generated_img_ref = None

def generate():
    global generated_img_ref

    image = pipe(prompt.get(), guidance_scale=8.5).images[0]

    image.save("generatedimage.png")

    generated_img_ref = ImageTk.PhotoImage(image)
    lmain.configure(image=generated_img_ref)

trigger = ctk.CTkButton(
    app,
    height=40, 
    width=100,
    font=("Arial", 20), 
    text_color="white",
    fg_color="blue",
    text="Generate",
    command=generate
)
trigger.place(x=206, y=60)

app.mainloop()
