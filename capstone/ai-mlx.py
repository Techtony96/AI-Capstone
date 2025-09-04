from mlx_lm import load, stream_generate
from mlx_lm.models.cache import make_prompt_cache
import gradio as gr

# Set the model ID for the Hugging Face model you want to use.
MODEL_ID = "mlx-community/Mistral-7B-Instruct-v0.3-4bit"


# Load a 4-bit quantized Mistral 7B model 
model, tokenizer = load(
    MODEL_ID,
    tokenizer_config={"trust_remote_code": True, "use_fast": True},
)

prompt_cache = make_prompt_cache(model)



def chat_with_model(prompt, history):
    messages = []
    for user_msg, assistant_msg in history:
        messages.append({"role": "user", "content": user_msg})
        messages.append({"role": "assistant", "content": assistant_msg})
    messages.append({"role": "user", "content": prompt})

    # Generate text from a prompt
    response = ""
    for token in stream_generate(
        model, 
        tokenizer, 
        tokenizer.apply_chat_template(messages, add_generation_prompt=True), 
        max_tokens=1024,
        prompt_cache=prompt_cache
    ):
        response += token.text;
        yield response


demo = gr.ChatInterface(
    fn=chat_with_model,
    title="Local LLM",
    description=f"This is a demo of the {MODEL_ID} model running locally. Enter your message and press Enter to chat."
)




# --- Launch the Application ---
if __name__ == "__main__":
    # The `share=True` argument would create a public link, but for local use, it's not needed.
    # `debug=True` provides more detailed error messages in the console.
    demo.launch(debug=False, share=False)