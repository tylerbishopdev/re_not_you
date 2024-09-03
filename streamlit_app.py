import os, replicate, streamlit as st
from dotenv import load_dotenv

load_dotenv()

replicate_api_token = os.getenv("REPLICATE_API_TOKEN")


# Streamlit app
st.title("YE-I")
st.subheader("Geniusly Created As A Kanye-Themed AI Model Playground By $hibaKing")
with st.sidebar:
  if not replicate_api_token:
    replicate_api_token = st.text_input("Replicate API Token", type="password")
  option = st.selectbox("Select Model", [
    "Image: Re_Adam/Machine",
    "Image: Re_Tyler/Machine",
    "Image: Re_Angie/Machine",
    "Image: Re_Jena/Machine",
    "Image: Stable Diffusion 3", 
    "Image: Black Forest Labs Flux Schnell", 
    "Audio: Suno AI Bark",
    "Music: Meta MusicGen"]
    )

os.environ["REPLICATE_API_TOKEN"] = replicate_api_token
prompt = st.text_input("Prompt", label_visibility="collapsed")

# If Generate button is clicked
if st.button("Generate"):
  if not replicate_api_token.strip() or not prompt.strip():
    st.error("Please provide the missing fields.")
  else:
    try:
      with st.spinner("Please wait..."):
        if option == "Image: Re_Adam/Machine":
          output = replicate.run(
            "tylerbishopdev/adammachine:7f2777e9f593b60851b8a23dada634d9324fb7d256819d20e16ae90e4be510ff",
            input={
                "width": 1024,
                "height": 1024,
                "prompt": "a photo of ADAM storming the United States capital wearing a red hat",
                "refine": "no_refiner",
                "scheduler": "K_EULER",
                "lora_scale": 0.6,
                "num_outputs": 1,
                "guidance_scale": 7.5,
                "apply_watermark": True,
                "high_noise_frac": 0.8,
                "negative_prompt": "",
                "prompt_strength": 0.8,
                "num_inference_steps": 50
            }
          )
          st.success(''.join(output))
        elif option == "Image: Re_Tyler/Machine":
          output = replicate.run(
            "tylerbishopdev/retylerv2:04de895d7e4756f867247b907a4aa66df16ba9cc00c95cca7602f85c6ff88702",
            input={
                "width": 1024,
                "height": 1024,
                "prompt": "A comic-style image of TYLER riding a sloth",
                "refine": "no_refiner",
                "scheduler": "K_EULER",
                "lora_scale": 0.6,
                "num_outputs": 1,
                "guidance_scale": 7.5,
                "apply_watermark": True,
                "high_noise_frac": 0.8,
                "negative_prompt": "",
                "prompt_strength": 0.8,
                "num_inference_steps": 50
            }
          )
          st.success(''.join(output))
        elif option == "Image: Re_Angie/Machine":
          output = replicate.run(
            "tylerbishopdev/angelamachine:1e73e53b1b80c1944327a284635f65815061f1d51f7214396896673a890c905b",
            input={
                "width": 1024,
                "height": 1024,
                "prompt": "An astronaut riding a rainbow unicorn",
                "refine": "no_refiner",
                "scheduler": "K_EULER",
                "lora_scale": 0.6,
                "num_outputs": 1,
                "guidance_scale": 7.5,
                "apply_watermark": True,
                "high_noise_frac": 0.8,
                "negative_prompt": "",
                "prompt_strength": 0.8,
                "num_inference_steps": 50
            }
          )
          st.success(''.join(output))
        elif option == "Re_Jena/Machine":
          output = replicate.run(
            "tylerbishopdev/jenamachine:ed8865f5e68274ec3667e97d9a6bae1812fa8d77386a4a6a8513c0ce6f19301a",
            input={
                "width": 1024,
                "height": 1024,
                "prompt": "JENA in a X-men’s juggernaut costume from the neck down",
                "refine": "no_refiner",
                "scheduler": "K_EULER",
                "lora_scale": 0.6,
                "num_outputs": 1,
                "guidance_scale": 7.5,
                "apply_watermark": True,
                "high_noise_frac": 0.8,
                "negative_prompt": "",
                "prompt_strength": 0.8,
                "num_inference_steps": 50
            }
          )
          st.success(''.join(output))
        elif option == "Image: Stable Diffusion 3":
          output = replicate.run(
            "stability-ai/stable-diffusion-3", 
            input={
              "prompt": prompt,
              "aspect_ratio": "3:2"
            }
          )
          st.image(output)
        elif option == "Image: Black Forest Labs Flux Schnell":
          output = replicate.run(
            "black-forest-labs/flux-schnell", 
            input={
              "prompt": prompt,
              "aspect_ratio": "3:2"
            }
          )
          st.image(output)
        elif option == "Code: Meta Code Llama 70B Instruct":
          output = replicate.run(
            "meta/codellama-70b-instruct:a279116fe47a0f65701a8817188601e2fe8f4b9e04a518789655ea7b995851bf",
            input={
                "top_k": 10,
                "top_p": 0.95,
                "prompt": prompt,
                "max_tokens": 500,
                "temperature": 0.8,
                "system_prompt": "",
                "repeat_penalty": 1.1,
                "presence_penalty": 0,
                "frequency_penalty": 0
            }
          )
          st.success(''.join(output))
        elif option == "Audio: Suno AI Bark":
          output = replicate.run(
            "suno-ai/bark:b76242b40d67c76ab6742e987628a2a9ac019e11d56ab96c4e91ce03b79b2787",
            input={
                "prompt": prompt,
                "text_temp": 0.7,
                "output_full": False,
                "waveform_temp": 0.7,
                "history_prompt": "announcer"
            }
          )
          st.audio(output.get('audio_out'), format="audio/wav")
        elif option == "Music: Meta MusicGen":
          output = replicate.run(
            "meta/musicgen:671ac645ce5e552cc63a54a2bbff63fcf798043055d2dac5fc9e36a837eedcfb",
            input={
                "top_k": 250,
                "top_p": 0,
                "prompt": prompt,
                "duration": 33,
                "temperature": 1,
                "continuation": False,
                "model_version": "stereo-large",
                "output_format": "mp3",
                "continuation_start": 0,
                "multi_band_diffusion": False,
                "normalization_strategy": "peak",
                "classifier_free_guidance": 3
            }
          )
          st.audio(output, format="audio/mp3")
    except Exception as e:
      st.exception(f"Exception: {e}")