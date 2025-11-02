### Getting Started with Openai Models and APIs

1. **Create an API key** from your dashboard.
2. **Export the openai api key** using an environment variable

```
export OPENAI_API_KEY="your_api_key"

```

3. **Setup you python virtual Environment**

```
python -m pip install --upgrade pip

```

4. **Create a virtual Environment:**

```
Create a folder for your project

mkdir YourFolderName

cd YourFolderName

python -m venv venv
```

5. **Run the requirements.txt file** (If you are downloading the code from this repo to test run.)

```
requirements.txt

pip install -r requirements.txt

OR run the following commands if you are setting up the environment manually.

pip install openai
pip install chainlit
pip install --upgrade pip

```

6. **App.py file**

```
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
```

7. **Run the application**

```
chainlit run app.py
```

8. Enter your prompt and press enter, your response should appear within 5-10 seconds depending on your internet speed.

#### Important notes

1. gpt-5 model is expensive, therefore if you are creating projects to learn, then i would recommend you use the cheapest and the fastest model for text generations, which is ***gpt-4o-mini***
2. This application is simply using the model only, therefore it can response to simple prompts and queries only. If you try to ask for complex information or updated data, then it would require ***web search***, which means that you have to write your code that includes the use of ***tools.***

```
tools=[{"type": "web_search"}]

This enables live web-search.
```