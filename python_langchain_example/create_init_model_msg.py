import os
from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv

# ✅ Load environment variables
load_dotenv()

# ✅ Get API key
OPENROUTER_KEY = os.getenv("OPENROUTER_API_KEY")
if not OPENROUTER_KEY:
    raise ValueError("Missing OPENROUTER_API_KEY in environment")

# ✅ Set OpenAI-compatible variables for OpenRouter
os.environ["OPENAI_API_KEY"] = OPENROUTER_KEY
os.environ["OPENAI_BASE_URL"] = "https://openrouter.ai/api/v1"

# ✅ Create Chat Model
model = init_chat_model(
    model="x-ai/grok-4.1-fast:free",
    model_provider="openai",
    api_key=OPENROUTER_KEY,
    temperature=0.7
)

# ✅ Define system behavior
system_msg = SystemMessage(
    content="You are a friendly AI assistant that explains things in simple words."
)

# ✅ First user message (better learning prompt)
human_msg_1 = HumanMessage(
    content="Explain what Artificial Intelligence is in very simple terms."
)

# ✅ First conversation turn
messages = [system_msg, human_msg_1]
response_1 = model.invoke(messages)

print("AI:", response_1.content)

# ✅ Store AI reply as context
ai_msg = AIMessage(content=response_1.content)

# ✅ Second user message using previous context
human_msg_2 = HumanMessage(
    content="Give me a real-life example of it."
)

# ✅ Continue the conversation with memory
messages = [system_msg, human_msg_1, ai_msg, human_msg_2]
response_2 = model.invoke(messages)

print("\nAI:", response_2.content)
