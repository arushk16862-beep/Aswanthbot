import os
import asyncio
from openai import AsyncOpenAI

# Initialize the async OpenAI client using environment variables
# Set OPENAI_API_KEY in your Render Environment Variables dashboard
ai_client = AsyncOpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

async def ai(query):
    # Uses the modern gpt-3.5-turbo / gpt-4o-mini chat completion API asynchronously
    response = await ai_client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful Telegram bot assistant."},
            {"role": "user", "content": query}
        ],
        max_tokens=150,
        temperature=0.7
    )
    return response.choices[0].message.content.strip()

async def ask_ai(client, m, message):
    try:
        # Check if user provided a prompt
        args = message.text.split(" ", 1)
        if len(args) < 2:
            return await m.edit("<b>Please provide a prompt!</b>\nExample: <code>/ai What is quantum physics?</code>")

        question = args[1]
        
        # Generate async response
        response = await ai(question)
        
        # Send response back
        await m.edit(f"<b>Query:</b> {question}\n\n<b>Response:</b>\n{response}")
        
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        await m.edit(error_message)
