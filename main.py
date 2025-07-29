from flask import Flask, render_template, request, url_for, redirect
import google.generativeai as genai
import get_api_key
import random

app = Flask(__name__)

# Configure Gemini API
genai.configure(api_key=get_api_key.api)

def call_gemini_api(prompt):
    """Call Gemini API and return the generated content"""
    try:
        # Create the model
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Generate content
        response = model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(
                temperature=0.8,
                top_p=0.95,
                top_k=40,
                max_output_tokens=250,
            )
        )
        
        # Return the generated text
        return response.text.strip()
        
    except Exception as e:
        print(f"Error calling Gemini API: {str(e)}")
        return f"Yaar, kuch gadbad ho gayi! Error: {str(e)}"
    

# @app.route('/', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         name = request.form.get('name', '').strip().lower()
#         if name == 'gilhari':
#             return redirect(url_for('/bora'))
#     return render_template('login.html')



# @app.route('/bora')
# def home():
#     return render_template("index.html")


@app.route('/', methods=['GET'])
def login():
    name = request.args.get('name', '').strip().lower()
    if name == 'gilhari':
        return redirect(url_for('bora', name=name))  # Redirect with query param
    return render_template('login.html')

@app.route('/bora')
def bora():
    name = request.args.get('name', 'User').title()
    # return f"Welcome to Gilhari's Vibe Box, {name}!"
    return render_template("index.html")


@app.route('/poem')
def get_poem():
    """Generate varied poems with informal multilingual vibes"""
    
    poem_prompts = [
         "Write a very short and rhyming 3 to 5 line poem in English with a friendly or light-hearted tone. "
    "It should feel warm, playful, or caring — like something you'd send to a best friend. "
    "Some poems can be slightly flirty or silly, but most should feel like genuine appreciation for friendship. "
    "Keep the language natural and easy to read. Don't make it too dramatic or romantic.\n\n"
    "Here are a few sample styles:\n"
    "— You’re the reason memes make sense,\n"
    "And why my chaos feels less intense.\n"
    "Through every rant, every cry,\n"
    "You’re my person — no need to ask why.\n\n"
    "— You're my WiFi in this offline mess,\n"
    "Bestie vibes, no need to impress.\n"
    "We roast, we vibe, we spill the tea,\n"
    "A friendship built on OTP.\n\n"
    "— If I had a dollar for every time we laughed,\n"
    "We'd own an island and a yacht, draft aft.\n"
    "You make weird feel cool,\n"
    "That’s our golden rule.\n\n"
    "Now write a new original poem like that."
    ]
    
    selected_prompt = random.choice(poem_prompts)
    response = call_gemini_api(selected_prompt)
    return response

@app.route('/quote')
def get_quote():
    
    quote_prompts = [
    "Give me only one short motivational quote (1 or 2 lines only). "
    "It should inspire someone working hard toward goals like joining the defence forces or clearing UPSC. "
    "Don't mention defence or UPSC directly — just reflect values like discipline, courage, or focus. "
    "Return only one quote. Do not include multiple quotes, bullet points, or examples."
    ]
    
    selected_prompt = random.choice(quote_prompts)
    response = call_gemini_api(selected_prompt)
    return response

@app.route('/pickup')
def get_pickup_line():
    
    pickup_prompts = [
    "Are you Google? Because you’ve got everything I’ve been searching for.",
    "Do you have a name, or can I call you mine?",
    "You're the reason even bad days feel okay.",
    "Are you WiFi? Because I'm feeling a strong connection.",
    "If I were a cat, I’d spend all 9 lives with you.",
    "Do you have a map? I just got lost in your smile.",
    "You must be tired — you’ve been running through my mind all day.",
    "Your vibe is my favorite notification.",
    "Even autocorrect knows you’re perfect.",
    "Are you made of sugar? Because you just sweetened my day.",
    "You're like a bug — because you crash my heart every time.",
    "If being cute was a crime, you'd be serving life.",
    "Are you light mode? Because you brighten my screen.",
    "I’m not a photographer, but I can picture us together.",
    "You're not an option, you’re a priority.",
    "You bring more sparkle than my phone screen.",
    "Even my code runs smoother when I think of you.",
    "No need for chatbots, you're the only reply I want.",
    "You’ve got the kind of smile that could fix memory leaks."
    "If confidence was a crime, you'd be serving a life sentence.",
    "Are you a goal? Because my focus shifts every time you walk in.",
    "You’re like chai on a winter morning — warm, comforting, and impossible to resist.",
    "Are you preparing for UPSC? Because you’ve got every quality they’re looking for.",
    "You're the reason my heart skips revision sessions.",
    "Even the army would salute that smile of yours.",
    "You must be a challenge — because I can’t stop chasing you.",
    "You walk in like motivation — unexpected, but much needed.",
    "You make even the toughest syllabus feel light.",
    "If I had a rank list, you'd be AIR 1 in my heart."
    ]
    
    selected_prompt = random.choice(pickup_prompts)
    return selected_prompt

    

@app.route('/compliments')
def get_compliment():
        
    compliment_prompts = [
    "You’ve got the kind of energy that could lead an army — or a group project!",
    "Brains, calmness, and a killer smile — you’re the full package!",
    "If confidence were a uniform, you’d wear it like a medal.",
    "Your focus could cut through chaos like a commando mission!",
    "You're the kind of person who makes tough look easy.",
    "Even Google would need help understanding how amazing you are!",
    "Every goal you aim for is probably scared of how close you're getting.",
    "Your calm vibe could probably de-escalate world wars.",
    "If determination had a brand ambassador, it’d be you!",
    "You light up a room like it’s your exam hall victory dance!",
    "The way you stay focused is more epic than any Netflix plot.",
    "You’re like a one-person motivation playlist!",
    "Even Monday looks less scary when you’re around.",
    "You’ve got that quiet strength that speaks louder than words.",
    "CDS or UPSC — they don’t know what's coming!",
    "You’re not just preparing, you’re leveling up life!",
    "Even coffee feels energized by your vibe!",
    "If goals had eyes, they’d be blushing at how you stare them down.",
    "You’re a walking reminder that cool and capable go hand in hand.",
    "Success is basically waiting for your green signal!"
    
    "You make ambition look effortless!",
    "Even a checklist would be impressed by how much you get done.",
    "You're not just chasing dreams — you’re catching them.",
    "If calm had a face, it’d probably be yours.",
    "Your confidence could pass every exam without studying.",
    "You’ve got the discipline of a soldier and the smile of sunshine.",
    "You make being focused look so cool.",
    "If there was a parade for dedication, you'd be leading it!",
    "Your prep game is stronger than most people’s Wi-Fi.",
    "You’re proof that determination can look good too!",
    "Even setbacks think twice before messing with you.",
    "You're like a cup of chai — strong, warm, and absolutely needed.",
    "You could motivate a rock to start preparing.",
    "No map needed — you’re clearly on the path to something big.",
    "Your vibe says 'calm now, conquer later.'",
    "Some people wait for inspiration, you just become it.",
    "If exams had emotions, they’d be nervous seeing your name.",
    "You’re not made for comfort zones — you're built for milestones.",
    "Just existing, and still managing to raise the bar.",
    "You make resilience look like an art form."
    ]
    
    selected_prompt = random.choice(compliment_prompts)
    return selected_prompt

if __name__ == '__main__':
    print("🚀 Gilhari's multilingual Flask server starting...")
    print("📍 Visit: http://localhost:5000")
    print("🤖 Desi vibes with Hindi/Haryanvi/Pahadi touch!")
    print("🌟 All responses will be varied and informal")
    app.run(debug=True)