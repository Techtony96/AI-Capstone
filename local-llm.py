# Python Import Statements - these bring in the necessary libraries and modules.
from mlx_lm import load, stream_generate
from mlx_lm.models.cache import make_prompt_cache
import gradio as gr

# Set the model ID for the Hugging Face model you want to use.
MODEL_ID = "mlx-community/Mistral-7B-Instruct-v0.3-4bit"

# Max token length for responses.
MAX_TOKENS = 1024

# Load the model and tokenizer with custom configurations, and create a prompt cache for efficiency.
model, tokenizer = load(
    MODEL_ID,
    tokenizer_config={"trust_remote_code": True, "use_fast": True},
)
prompt_cache = make_prompt_cache(model)


# Function to handle chat interactions with the model.
def chat_with_model(prompt, history):
    messages = []
    
    # Add the chat history to the messages list.
    for user_msg, assistant_msg in history:
        messages.append({"role": "user", "content": user_msg})
        messages.append({"role": "assistant", "content": assistant_msg})
    
    # Finally, add the new user prompt.
    messages.append({"role": "user", "content": prompt})

    # Generate a response from the model.
    response = ""
    for token in stream_generate(
        model, 
        tokenizer, 
        tokenizer.apply_chat_template(messages, add_generation_prompt=True), 
        max_tokens=MAX_TOKENS,
        prompt_cache=prompt_cache
    ):
        response += token.text;
        yield response

# Set up the Gradio interface for the chat application.
demo = gr.ChatInterface(
    fn=chat_with_model,
    title="Local LLM Demo",
    description=f"This is a demo of the {MODEL_ID} model running locally."
)

# --- Launch the Application ---
if __name__ == "__main__":
    # share=True argument would create a public link, but for local use, it's not needed.
    # debug=True provides more detailed error messages in the console.
    demo.launch(debug=False, share=False)