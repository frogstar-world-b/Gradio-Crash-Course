import gradio as gr


def greet(name):
    return "Hello " + name + "!"


# Create interface: gets a function to excute, its input and output param types
# type could be text, number, image, audio, label
# demo = gr.Interface(fn=greet, inputs="text", outputs="text")

# or we could use gr types
# demo = gr.Interface(fn=greet, inputs=gr.Textbox(lines=2, placeholder="Name here"), outputs="text")


def greet2(name, is_morning, temperature):
    salutation = "Good morning!" if is_morning else "Good evening!"
    greeting = f"{salutation} {name}. Its {temperature} degrees today."
    celcius = (temperature - 32) * 5 / 9
    return greeting, round(celcius, 2)


# or have a list of inputs and outputs
demo = gr.Interface(fn=greet2,
                    inputs=["text", "checkbox", gr.Slider(1, 100)],
                    outputs=["text", "number"])

demo.launch()
