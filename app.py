import os

from flask import Flask, render_template, request


app = Flask(__name__)

QUESTIONS = [
    {
        "id": "q1",
        "title": "Q1 When you have a day off, you prefer to?",
        "options": [
            ("A", "Plan out the whole day in advance"),
            ("B", "Go with the flow without any plans"),
        ],
    },
    {
        "id": "q2",
        "title": "Q2 A friend invites you to a gathering with many strangers. You will?",
        "options": [
            ("A", "Look forward to it and feel excited to meet new people"),
            ("B", "Prefer to hang out only with close friends"),
        ],
    },
    {
        "id": "q3",
        "title": "Q3 How do you feel when plans suddenly change?",
        "options": [
            ("A", "A little uneasy; I hate my schedule being disrupted"),
            ("B", "It might be fun; I am open to unexpected surprises"),
        ],
    },
]

RESULTS = {'AAA': {'color_name': 'Brown锝淐ocoa Brownie',
         'color_hex': '#8B4513',
         'img_src': 'https://images.unsplash.com/photo-1583230791811-8585c13db083?q=80&w=1470&auto=format&fit=crop',
         'spot': 'Ruins of St. Paul',
         'description': 'You are steady and prudent. You love a predictable routine and are someone others can rely '
                        'on.',
         'speech': 'This iconic heritage landmark carries centuries of history. Slow down and appreciate every carved '
                   'detail.',
         'encouragement': 'Stay grounded. Your thoughtfulness will always lead you forward.'},
 'AAB': {'color_name': 'Red锝淩ed Velvet',
         'color_hex': '#c93838',
         'img_src': 'https://images.unsplash.com/photo-1598517511295-c216a164a3b1?q=80&w=1470&auto=format&fit=crop',
         'spot': 'Rua do Cunha',
         'description': 'You usually stick to plans but welcome surprises. Passionate and bold, you are willing to try '
                        'new things.',
         'speech': 'Filled with local snacks and cozy shops, perfect for food lovers who enjoy wandering.',
         'encouragement': 'Stay bold! Every new adventure creates amazing stories.'},
 'ABA': {'color_name': 'Purple锝淧urple Sweet Potato',
         'color_hex': '#9F69B3',
         'img_src': 'https://s41.ax1x.com/2026/09/05/pnAuUJg.jpg',
         'spot': 'Avenue of Stars, Hong Kong',
         'description': 'You follow principles on the surface yet have unique inner thoughts. You value spiritual '
                        'connection and hate following the crowd.',
         'speech': 'Walk along the waterfront with stunning skyline views, ideal for quiet contemplation.',
         'encouragement': 'Embrace your uniqueness. Your creative mind is your superpower.'},
 'BAA': {'color_name': 'Yellow锝淐heese',
         'color_hex': '#FFB354',
         'img_src': 'https://images.unsplash.com/photo-1569336415962-a4bd9f69c8bf?q=80&w=1470&auto=format&fit=crop',
         'spot': 'Senado Square',
         'description': 'You are outgoing and optimistic. You enjoy socializing and spread positive energy to people '
                        'around you.',
         'speech': 'The vibrant heart of Macau, full of vitality and classic Portuguese architecture.',
         'encouragement': 'Keep shining! Your positivity brightens everyone around you.'},
 'BBA': {'color_name': 'Green锝淢atcha',
         'color_hex': '#70B888',
         'img_src': 'https://images.unsplash.com/photo-1596464145217-12be129a722f?q=80&w=1470&auto=format&fit=crop',
         'spot': 'Taipa Houses',
         'description': 'You love a quiet, relaxed life and cherish alone time. You only seek stability when dealing '
                        'with important matters.',
         'speech': 'Charming colonial houses surrounded by greenery, perfect for a slow peaceful stroll.',
         'encouragement': 'Cherish your peace. Calm minds see the clearest paths.'},
 'BAB': {'color_name': 'Pink锝淪akura Pink',
         'color_hex': '#F4A8B8',
         'img_src': 'https://images.unsplash.com/photo-1602442784108-82254d45e930?q=80&w=1470&auto=format&fit=crop',
         'spot': 'Travessa da Paix茫o',
         'description': 'You are gentle and romantic. You easily spot small beauties in life and are empathetic '
                        'towards others.',
         'speech': 'Famous pastel鈥憄ink alley, full of romantic atmosphere for lovely snapshots.',
         'encouragement': 'Keep your soft heart. You deserve all life鈥檚 little joys.'},
 'ABB': {'color_name': 'White',
         'color_hex': '#F8F6F9',
         'img_src': 'https://media.cntraveler.com/photos/5a908567723a834885e15329/16:9/w_2560,c_limit/Ma-Temple_Courtesy-Macao-Government-Tourism-Office_2018__O4I9797.jpg',
         'spot': 'A鈥慚a Temple',
         'description': 'You are well鈥慴alanced. You can enjoy parties as well as quiet moments and adapt smoothly to '
                        'changes.',
         'speech': 'Macau鈥檚 oldest temple, blending traditional culture with peaceful surroundings.',
         'encouragement': 'Keep balancing well. You are ready for anything life brings.'},
 'BBB': {'color_name': 'Golden锝淐aramel Gold',
         'color_hex': '#D4A017',
         'img_src': 'https://s41.ax1x.com/2026/09/05/pnAuaWQ.jpg',
         'spot': 'Hong Kong Disneyland',
         'description': 'You live freely without being restricted by schedules. Flexible and easy鈥慻oing, you can find '
                        'joy from unexpected situations.',
         'speech': 'Where magic comes alive, perfect for embracing surprises and childlike joy.',
         'encouragement': 'Go with the flow! Wonderful surprises are ahead of you.'}}


@app.route("/", methods=["GET", "POST"])
def quiz():
    result = None
    error = None

    if request.method == "POST":
        answers = [request.form.get(question["id"]) for question in QUESTIONS]
        if any(answer not in {"A", "B"} for answer in answers):
            error = "Please answer all three questions."
        else:
            result = RESULTS["".join(answers)]

    return render_template(
        "index.html",
        questions=QUESTIONS,
        result=result,
        error=error,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "5000")), debug=False)
