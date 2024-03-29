# Gradio-Crash-Course

- [`gradio`](https://www.gradio.app/) is a great app for demoing and deploying ML models and chatbots.
- `gradio` provides a local URL (e.g., http://127.0.0.1:7860) for interacting with your model directly on your machine. Additionally, it offers the option to share a public URL (e.g., by setting `demo.launch(share=True)`) to make your model accessible over the internet.
- `app_transformers.py` in this repo builds an app that translates text from English to German using Hugging Face's Transformers liberay, and `gradio` will provided a public link (e.g., https://ddee556273263c7c3c.gradio.live)
- Make sure you install `gradio` and other packages in the scripts, then you can run an app like this:

   ```bash
   python app.py
   ``` 
- For a great tutorial, I highly recommend this [youtube video](https://youtu.be/eE7CamOE-PA?si=bR3rz-e8Lim63Tc1).

