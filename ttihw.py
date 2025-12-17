import torch
from diffusers import StableDiffusionPipeline
from PIL import Image
pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5",torch_dtype=torch.float16).to("cpu")
prompt = "Astronaut riding a horse on Mars, ultra realistic"
result = pipe(prompt)
image: Image.Image = result.images[0]
image.show()
image.save("generated_image.png")
print("Image saved as generated_image.png")