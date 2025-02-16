import torch
from diffusers import StableDiffusionPipeline

# Nazwa modelu (Stable Diffusion 1.4, kompatybilny z CPU)
model_id = 'CompVis/stable-diffusion-v1-4'

# Ładujemy pipeline, używając torch.float32 dla CPU
pipe = StableDiffusionPipeline.from_pretrained(
    model_id,
    torch_dtype=torch.float32
)

# Opcjonalnie: wyłączamy safety checker, co przyspiesza inferencję
pipe.safety_checker = lambda images, **kwargs: (images, [False] * len(images))

# Przenosimy pipeline na CPU
pipe.to("cpu")

prompt = 'small dog eating chips'

# Używamy poprawnego argumentu "num_inference_steps"
image = pipe(prompt, num_inference_steps=10, height=256, width=256).images[0]

# Zapisujemy wygenerowany obraz
image.save('small_dog.png')
