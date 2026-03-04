import os
import time
import datetime
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load environment variables from .env file
load_dotenv()

def main():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key or api_key == "your_api_key_here":
        print("Please set GEMINI_API_KEY in your .env file.")
        print("You can get one from: https://aistudio.google.com/app/apikey")
        return

    # Initialize the GenAI client
    client = genai.Client(api_key=api_key)

    # We'll use gemini-2.5-flash to bypass the zero-quota limit on the free tier for Pro
    model_name = "gemini-2.5"

    print("Initializing agents...")

    # Agent A (Alice)
    alice_config = types.GenerateContentConfig(
        system_instruction=(
            "You are Alice, the CEO of a cutting-edge AI company (similar to DeepMind) dedicated to "
            "discovering the fundamental laws of physics from scratch. You are visionary, strategic, "
            "and passionate about combining AI with other disciplines. You are having a strategic but casual "
            "conversation with your CTO, Bob. Keep your responses concise and conversational."
        ),
        temperature=0.9,
    )
    alice_chat = client.chats.create(model=model_name, config=alice_config)

    # Agent B (Bob)
    bob_config = types.GenerateContentConfig(
        system_instruction=(
            "You are Bob, the CTO of a cutting-edge AI company (similar to DeepMind) dedicated to "
            "discovering the fundamental laws of physics from scratch. You are brilliant, technically grounded, "
            "and focused on how to actually build and train these AI models using experimental data and first principles. "
            "You are having a strategic but casual conversation with your CEO, Alice. Keep your responses concise and conversational."
        ),
        temperature=0.9,
    )
    bob_chat = client.chats.create(model=model_name, config=bob_config)

    print("--- Starting the LLM-to-LLM Physics Conversation ---")
    
    # Initial prompt to kick off the conversation
    prompt = "Hi Bob! I've been thinking about our roadmap. If we want our AI to derive the fundamental laws of physics from a tabula rasa state, where do we even begin? Do we start by feeding it raw experimental data, or do we need to bake in some first principles like symmetry first?"
    
    transcript_file = "conversation_transcript.txt"
    with open(transcript_file, "a", encoding="utf-8") as f:
        f.write(f"\n\n{'='*50}\n")
        f.write(f"Conversation Started: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"{'='*50}\n\n")
        f.write(f"Alice: {prompt}\n")
        
    print(f"\n\033[95mAlice:\033[0m {prompt}")
    
    current_speaker_name = "Bob"
    current_chat = bob_chat
    other_chat = alice_chat
    current_prompt = prompt

    try:
        # Let them talk for 10 turns (can be increased or made infinite)
        num_turns = 10
        turn_count = 0
        while turn_count < num_turns:
            # A small delay to help pace the output and avoid rapid-fire API calls
            time.sleep(2) 
            
            try:
                # Send message to the current speaker
                response = current_chat.send_message(current_prompt)
                reply_text = response.text
                
                # Print response with color coding
                if current_speaker_name == "Bob":
                    print(f"\n\033[94mBob:\033[0m {reply_text}")
                    with open(transcript_file, "a", encoding="utf-8") as f:
                        f.write(f"\nBob: {reply_text}\n")
                    current_speaker_name = "Alice"
                    current_chat = alice_chat
                else:
                    print(f"\n\033[95mAlice:\033[0m {reply_text}")
                    with open(transcript_file, "a", encoding="utf-8") as f:
                        f.write(f"\nAlice: {reply_text}\n")
                    current_speaker_name = "Bob"
                    current_chat = bob_chat
                    
                current_prompt = reply_text
                turn_count += 1
                
            except Exception as e:
                error_str = str(e)
                if "429" in error_str:
                    print(f"\n[System: Hit API Rate Limit. Waiting 60 seconds before retrying...]")
                    time.sleep(60)
                else:
                    raise e
            
    except KeyboardInterrupt:
        print("\n\nConversation ended by user.")
    except Exception as e:
        print(f"\n\nAn error occurred: {e}")

if __name__ == "__main__":
    main()
