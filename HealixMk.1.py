import os
import time
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("Healix_Mk1_API_KEY")

if API_KEY is None:
    raise ValueError("API Key not found. Ensure it's set in the .env file.")

def setup_gemini():
    genai.configure(api_key=API_KEY)

def clear_screen():
    print("\033c", end="")  

def loading_animation():
    print("\nPlease wait, loading...")
    time.sleep(1)
    clear_screen()

def service_menu_return():
    Service_menu_return_question = input("\nWould you like to return to the service menu? (yes/no) ").casefold().strip()
    loading_animation()
    if Service_menu_return_question == "yes":
        Service_type_menu()
    elif Service_menu_return_question == "no":
        print("Ok, take care.")
    else:
        sarcastic_retry_for_service_menu_RETURN()
        

def BayBot_greeting():
    baymax_face = """
    ██        ██  
  ████████████████  
 ██████████████████ 
 ███  ●      ●   ██    B  A  Y   -   B  O  T
 ███    ▬▬▬▬     ██            Mk. 1
 ██████████████████  
  ████████████████ 
    ██        ██  
"""
    print(baymax_face)
    time.sleep(0.75)
    print("Hello!")
    time.sleep(0.5)
    print("I am Healix Mk.1, your personal healthcare assistant.")
    time.sleep(0.5)
    print("Always here to keep you safe, healthy, and informed. 🚑💡\n")
    first_question = input("Would you like to try out my services? (yes/no)  ").casefold().strip()
    loading_animation()
    
    if first_question == "yes":
        Service_type_menu()
    elif first_question == "no":
        No_service()
    else:
        sarcastic_retry_for_BAYBOT_greeting()

def No_service():
    print("If you ever need assistance, I'm always here to help! 😊 Stay healthy! 💙\n")
    time.sleep(0.5)
    first_question_again = input("Would you like to restart Healix Mk.1? (yes/no) ").casefold().strip()
    if first_question_again == "yes":
        loading_animation()
        BayBot_greeting()
    elif first_question_again == "no":
        print("Ok, take care!")
    else:
        print("Invalid prompt, please restart Healix Mk.1")

sarcastic_responses = [
    "Wow. That was… impressively wrong.",
    "If common sense was a sport, you'd be in last place.",
    "Your reading skills just declared bankruptcy.",
    "Are you trying to communicate with another species?",
    "NASA just called. They want to study how you missed the point this badly.",
    "I’d explain again, but I feel like you’d still mess it up.",
    "You must be a magician, because you made the right answer disappear.",
    "This is an AI program, not a wishing well. Try again.",
    "Your ability to ignore instructions is almost impressive.",
    "I’d be mad, but honestly, this is just entertaining now.",
    "My disappointment is immeasurable, and my day is ruined.",
    "This isn’t a quiz show where you get points for originality.",
    "If you’re speedrunning failure, congrats! New world record.",
    "Your logic has left the chat.",
    "Did you trip and fall on the keyboard, or was that intentional?",
    "Are you having a staring contest with the correct answer and losing?",
    "Try again, but this time with actual effort.",
    "I’ll call a doctor because I think you might be allergic to reading.",
    "Even a broken clock is right twice a day. What’s your excuse?",
    "This isn’t Minesweeper. You don’t just click randomly and hope for the best.",
    "Are you playing on extra hard mode where you ignore all instructions?",
    "Oh, look, another attempt at defying logic itself.",
    "Your keyboard deserves an apology.",
    "Your answer was so bad, my circuits felt physical pain.",
    "Ever thought about a career in cryptography? Because your thought process is impossible to decode.",
    "Let’s try a revolutionary new technique: reading the instructions.",
    "Your brain must be on airplane mode.",
    "Fun fact: guessing isn't a valid life strategy.",
    "If you keep this up, I’ll start charging you per mistake.",
    "Somewhere, a dictionary is crying.",
    "I hope this is performance art, because it’s quite the show.",
    "At this point, I’m just here for the entertainment.",
    "You do realize words have meaning, right?",
    "Are you legally blind, or just rebelliously incorrect?",
    "If I had a dollar for every mistake you made, I’d retire.",
    "It’s okay, not everyone was meant to understand basic instructions.",
    "You’re either testing me or yourself. Either way, it's painful to watch.",
    "This was a creative way to be wrong, I’ll give you that.",
    "Oh wow, that’s a new level of incorrect.",
    "That answer was so wrong, I think I lost a few brain cells.",
    "You’re making me question my existence as an AI.",
    "Is this a prank? Blink twice if you need help.",
    "That was such a bad answer, I’m considering self-destructing.",
    "The answer is in front of you, but you still dodged it like Neo in The Matrix.",
    "Your ability to be wrong in unique ways is truly inspiring.",
    "If being wrong was a superpower, you’d be the main character.",
    "Every time you get it wrong, I get a little closer to giving up on humanity.",
    "I would say ‘close, but no cigar,’ but you weren’t even close.",
    "You could have picked any number of right answers, and yet you chose that.",
    "Your logic is so wild, I’m considering adding a ‘just give up’ button.",
    "You must have a PhD in misunderstanding instructions.",
]

wrong_attempts = 0

def sarcastic_retry_for_NO_service():
    global wrong_attempts
    print("\n" + sarcastic_responses[wrong_attempts % len(sarcastic_responses)] + "\n")
    wrong_attempts += 1  
    No_service()

def sarcastic_retry_for_service_menu_RETURN():
    global wrong_attempts
    print("\n" + sarcastic_responses[wrong_attempts % len(sarcastic_responses)] + "\n")
    wrong_attempts += 1  
    service_menu_return()

def sarcastic_retry_for_BAYBOT_greeting():
    global wrong_attempts
    print("\n" + sarcastic_responses[wrong_attempts % len(sarcastic_responses)] + "\n")
    wrong_attempts += 1  
    BayBot_greeting()

def sarcastic_retry_for_service_type_menu():
    global wrong_attempts
    print("\n" + sarcastic_responses[wrong_attempts % len(sarcastic_responses)] + "\n")
    wrong_attempts += 1  
    Service_type_menu()

def Service_type_menu():
    print("\nYour health, my priority! Pick a service and let’s get started!")
    print("1️⃣  Symptom Checker")
    print("2️⃣  First Aid Assistance")
    print("3️⃣  Medication Guide")
    print("4️⃣  Emergency Contacts")
    print("5️⃣  Mental Health Support")
    print("6️⃣  Diet & Nutrition Advice")
    print("7️⃣  Any other queries\n")
    first_service_question = input("Enter the number corresponding to your desired service to proceed:  ").strip()
    loading_animation()
    match first_service_question:
        case "1":
            symptom_checker()
        case "2":
            First_aid_assistance()
        case "3":
            medication_guide()
        case "4":
            emergency_contacts()
        case "5":
            mental_health_support()
        case "6":
            diet_and_nutrition_advice()
        case "7":
            any_other_queries()
        case _:
            sarcastic_retry_for_service_type_menu()


def First_aid_assistance():
    setup_gemini()
    model = genai.GenerativeModel("gemini-2.0-flash-exp")
    user_input = input("Describe your condition (separated by commas): ")
    print("This may take a few seconds...")
    prompt = f"Give a brief, to-the-point answer (max 60 words) for the following prompt. I have the following conditions: {user_input}. What could be the first aid treatments?"

    response = model.generate_content(prompt)
    response_text = response.text if response else "Sorry, I couldn't fetch a response."

    loading_animation()
    print(response_text)

    time.sleep(2)
    service_menu_return()
def symptom_checker():
    setup_gemini()
    model = genai.GenerativeModel("gemini-2.0-flash-exp")
    user_input = input("Describe your symptoms: ")
    print("This may take a few seconds...")
    prompt = f"Give a brief, to-the-point answer (max 100 words) for the following prompt. I have the following symptoms: {user_input}. What could be the possible causes and first aid treatments?"

    response = model.generate_content(prompt)
    response_text = response.text if response else "Sorry, I couldn't fetch a response."

    loading_animation()
    print("\nPossible diseases: ")
    print(response_text)
    time.sleep(2)
    service_menu_return()
    

def medication_guide():
    setup_gemini()
    model = genai.GenerativeModel("gemini-2.0-flash-exp")
    user_input = input("Describe your condition or the context in which you need medication: ")
    print("This may take a few seconds...")
    prompt = f"Give a brief, to-the-point answer (max 80 words) for the following prompt. This is the context from a user: {user_input}. What could be the medication guide for the same?"

    response = model.generate_content(prompt)
    response_text = response.text if response else "Sorry, I couldn't fetch a response."

    loading_animation()
    print(response_text)
    time.sleep(2)
    service_menu_return()

def emergency_contacts():
    setup_gemini()
    model = genai.GenerativeModel("gemini-2.0-flash-exp")
    user_input = input("Which country are you in, and what type of emergency contact are you looking for (e.g., ambulance, poison control, mental health support)?")
    print("This may take a few seconds...")
    prompt = f"Give a brief, to-the-point answer (max 10 words) for the following prompt. This is the country user lives in, along with the emergency contact they require: {user_input}. What is the telephone number of the emergency contact(along with country code)?"

    response = model.generate_content(prompt)
    response_text = response.text if response else "Sorry, I couldn't fetch a response."

    loading_animation()
    print(response_text)
    time.sleep(2)
    service_menu_return()

def mental_health_support():
    setup_gemini()
    model = genai.GenerativeModel("gemini-2.0-flash-exp")
    user_input = input("How are you feeling today? Describe your emotions or any concerns you have: ")
    print("This may take a few seconds...")
    prompt = f"Give a brief, to-the-point answer (max 150 words) for the following prompt. This is the context from a user: {user_input}. What could be the mental health support guide for the same?"

    response = model.generate_content(prompt)
    response_text = response.text if response else "Sorry, I couldn't fetch a response."

    loading_animation()
    print(response_text)
    time.sleep(2)
    service_menu_return()

def diet_and_nutrition_advice():
    setup_gemini()
    model = genai.GenerativeModel("gemini-2.0-flash-exp")
    user_input = input("What are your dietary preferences or nutrition concerns?: ")
    print("This may take a few seconds...")
    prompt = f"Give a brief, to-the-point answer (max 150 words) for the following prompt. This is the context from a user: {user_input}. What could be the diet and nutrition advice and support for the same?"

    response = model.generate_content(prompt)
    response_text = response.text if response else "Sorry, I couldn't fetch a response."

    loading_animation()
    print(response_text)
    time.sleep(2)
    service_menu_return()

def any_other_queries():
    setup_gemini()
    model = genai.GenerativeModel("gemini-2.0-flash-exp")
    user_input = input("What is your query? ")
    print("This may take a few seconds...")
    prompt = f"Give a brief, to-the-point answer (max 150 words) for the following prompt. This is the query from a user: {user_input}. What could be the answer to the query user just asked?"

    response = model.generate_content(prompt)
    response_text = response.text if response else "Sorry, I couldn't fetch a response."

    loading_animation()
    print(response_text)
    time.sleep(2)
    service_menu_return()


    

BayBot_greeting()

