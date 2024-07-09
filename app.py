import chainlit as cl
from chainlit.input_widget import Slider

@cl.on_chat_start
async def start():
    image = cl.Image(path="./download.jpeg", name="cat",display="page")

    # Attach the image to the message
    await cl.Message(
        content="This message has an image!",
        elements=[image],
    ).send()
    text_content = "print('hello')"
    elements = [
        cl.Text(name="simple_text", content=text_content, language="python", display="inline")
    ]

    await cl.Message(
        content="Check out this text element!",
        elements=elements,
    ).send()

    elements = [
      cl.Pdf(name="pdf1", display="inline", path="./tech3355.pdf")
    ]

    cl.Message(content="Look at this local pdf!", elements=elements).send()
    settings = await cl.ChatSettings(
        [
            Slider(
                id="Temperature",
                label="OpenAI - Temperature",
                initial=1,
                min=0,
                max=2,
                step=0.1,
            ),
        ]
    ).send()
    value = settings["Temperature"]

@cl.on_message
async def main(message: cl.message):
    await cl.Message(
        content=f"Recived: {message.content}"
    ).send()

@cl.on_stop
def on_stop():
    print("the user stoped the session")

