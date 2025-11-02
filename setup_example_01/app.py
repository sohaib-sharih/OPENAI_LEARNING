from openai import OpenAI
import chainlit as cl

client = OpenAI()

@cl.on_message
async def main(message: cl.Message):
    response = client.responses.create(
        model="gpt-4o-mini",
        input=message.content,
        timeout=25
    )
    await cl.Message(content=response.output_text).send()