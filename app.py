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

RESULTS = {
    "AAA": {
        "color_name": "Cocoa Brown | Cocoa Brownie",
        "color_hex": "#8B4513",
        "img_src": "https://www.geodata.cn/ManagerDev/comprehensive/api/files/downloadStream?objectName=res/images/baike/pic/dsbpf2.jpg",
        "spot": "Ruins of St. Paul's",
        "description": "You are steady and prudent. You love a predictable routine and are someone others can always rely on.",
        "speech": "This iconic heritage landmark carries centuries of history. Slow down and appreciate every carved detail.",
        "encouragement": "Stay grounded. Your thoughtfulness will always lead you forward.",
    },
    "AAB": {
        "color_name": "Velvet Red | Strawberry Rouge",
        "color_hex": "#c93838",
        "img_src": "https://gips2.baidu.com/it/u=1696535491,3019352511&fm=3074&app=3074&f=JPEG?w=1080&h=1409&type=normal&func=",
        "spot": "Rua do Cunha",
        "description": "You usually stick to plans but welcome small surprises. Passionate and bold, you are willing to try new delicacies.",
        "speech": "Filled with local snacks and cozy shops, perfect for food lovers who enjoy wandering.",
        "encouragement": "Stay bold! Every new adventure creates amazing stories.",
    },
    "ABA": {
        "color_name": "Lavender Purple | Grape Mousse",
        "color_hex": "#9F69B3",
        "img_src": "https://miaobi-lite.bj.bcebos.com/miaobi/5mao/b%27LV8xNzMzNDcwOTgwLjU3NDc3MTQ%3D%27/0.png?authorization=bce-auth-v1%2FALTAKmda7zOvhZVbRzBLewvCMU%2F2024-12-06T07%3A43%3A01Z%2F-1%2F%2F16ebd8c6553e120b9380c05fb32bb7b0ce22fc5f1c70390fbab286017e11598e",
        "spot": "Our Lady of Penha Church",
        "description": "You follow principles yet have unique inner thoughts. You value quiet moments and hate following the crowd blindly.",
        "speech": "Overlooking the whole city, it offers peaceful scenery ideal for relaxing and clearing your mind.",
        "encouragement": "Embrace your uniqueness. Your creative mind is your superpower.",
    },
    "BAA": {
        "color_name": "Sunshine Orange | Mango Cheese",
        "color_hex": "#FFB354",
        "img_src": "https://b0.bdstatic.com/ugc/_QWuzoFPHbqmx-VathgWSQ0a8ecd6780da3904c00671defec7ced9.jpg",
        "spot": "Senado Square",
        "description": "You are outgoing and optimistic. You enjoy socializing and spread positive energy to people around you.",
        "speech": "The vibrant heart of Macau, full of vitality and classic Portuguese architecture.",
        "encouragement": "Keep shining! Your positivity brightens everyone around you.",
    },
    "BBA": {
        "color_name": "Green | Matcha Latte",
        "color_hex": "#70B888",
        "img_src": "https://img0.baidu.com/it/u=558524,841929187&fm=253&app=138&f=JPEG?w=500&h=653",
        "spot": "Taipa Village",
        "description": "You love a quiet, relaxed life and cherish alone time. You only seek stability when dealing with important matters.",
        "speech": "Warm old streets with pastel buildings, ideal for slow travel and casual photography.",
        "encouragement": "Cherish your peace. Calm minds see the clearest paths.",
    },
    "BAB": {
        "color_name": "Pink | Sakura Cream",
        "color_hex": "#F4A8B8",
        "img_src": "https://b0.bdstatic.com/ugc/personal_page_creator/LCEC4XbQIMbX9OHFt-mYig5fd7d6dcf2ae1e19928092488e843626.jpg",
        "spot": "Travessa da Paixão",
        "description": "You are gentle and romantic. You easily spot small beauties in life and are empathetic towards others.",
        "speech": "Famous pastel-pink alley, full of romantic atmosphere for lovely snapshots.",
        "encouragement": "Keep your soft heart. You deserve all life's little joys.",
    },
    "ABB": {
        "color_name": "Vanilla Off-white | Vanilla Cream",
        "color_hex": "#F8F6F9",
        "img_src": "https://miaobi-lite.bj.bcebos.com/miaobi/5mao/b%27MDE0OTMzN%2BWmiOellumYgV8xNzM1NDIxNTEzLjM5MTY5MTc%3D%27/0.png",
        "spot": "A-Ma Temple",
        "description": "You are well-balanced. You can enjoy lively crowds as well as quiet moments and adapt smoothly to changes.",
        "speech": "Macau's oldest temple, blending traditional culture with peaceful surroundings.",
        "encouragement": "Keep balancing well. You are ready for anything life brings.",
    },
    "BBB": {
        "color_name": "Ocean Blue | Sky Blue",
        "color_hex": "#87CEEB",
        "img_src": "https://miaobi-lite.bj.bcebos.com/miaobi/5mao/b%27MDE0OTMzN%2BWmiOellumYgV8xNzM1NDIxNTEzLjM5MTY5MTc%3D%27/0.png",
        "spot": "A-Ma Temple",
        "description": "You live freely without being restricted by schedules. Flexible and easy-going, you find joy from unexpected situations.",
        "speech": "Macau's oldest temple, blending traditional culture with peaceful surroundings.",
        "encouragement": "Go with the flow! Wonderful surprises are ahead of you.",
    },
}


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
