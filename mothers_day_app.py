import streamlit as st
import time
from PIL import Image
import base64

# Set page config
st.set_page_config(page_title="Mother's Day Love", page_icon="🌸", layout="centered")

# Function to encode image to base64
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
    return f"data:image/jpeg;base64,{encoded}"

# Function to autoplay audio
def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio autoplay loop>
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
        """
        st.markdown(md, unsafe_allow_html=True)

# Load base64 image once
base64_img = get_base64_image("mama.jpg")

# Custom CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Montserrat:wght@400;600&display=swap');

    body {
        background: linear-gradient(135deg, #fff0f5 0%, #fce4ec 100%);
        font-family: 'Montserrat', sans-serif;
    }
    .container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        min-height: 60vh;
    }
    .envelope {
        width: 320px;
        height: 220px;
        background: linear-gradient(135deg, #ff9a9e 0%, #fad0c4 100%);
        position: relative;
        margin: 40px auto;
        cursor: pointer;
        border-radius: 15px;
        box-shadow: 0 15px 35px rgba(233, 30, 99, 0.2);
        transition: all 0.5s ease;
        z-index: 10;
    }
    .envelope:hover {
        transform: translateY(-10px) scale(1.03);
        box-shadow: 0 20px 40px rgba(233, 30, 99, 0.3);
    }
    .flap {
        width: 0;
        height: 0;
        border-left: 160px solid transparent;
        border-right: 160px solid transparent;
        border-bottom: 110px solid #ff6f91;
        position: absolute;
        top: -110px;
        left: 0;
        border-radius: 15px 15px 0 0;
        transform-origin: top;
        transition: transform 0.8s ease;
        z-index: 15;
    }
    .open .flap {
        transform: rotateX(180deg);
    }
    .message-container {
        display: none;
        text-align: center;
        margin: 30px auto;
        max-width: 600px;
        padding: 30px;
        background: white;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        position: relative;
        overflow: hidden;
    }
    .message-container::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 10px;
        background: linear-gradient(90deg, #ff6b81, #ff8e53);
    }
    .show {
        display: block !important;
        animation: fadeInUp 1.5s forwards;
    }
    @keyframes fadeInUp {
        from {opacity: 0; transform: translateY(30px);}
        to {opacity: 1; transform: translateY(0);}
    }
    @keyframes float {
        0%, 100% {transform: translateY(0);}
        50% {transform: translateY(-20px);}
    }
    .heart {
        position: fixed;
        width: 20px;
        height: 20px;
        background-color: #ff6f91;
        transform: rotate(45deg);
        animation: floatUp 5s linear infinite;
        opacity: 0.7;
        z-index: 1;
    }
    .heart::before,
    .heart::after {
        content: "";
        position: absolute;
        width: 20px;
        height: 20px;
        background-color: #ff6f91;
        border-radius: 50%;
    }
    .heart::before {
        top: -10px;
        left: 0;
    }
    .heart::after {
        left: -10px;
        top: 0;
    }
    @keyframes floatUp {
        0% {transform: rotate(45deg) translateY(0) scale(0.8); opacity: 0.7;}
        100% {transform: rotate(45deg) translateY(-100vh) scale(1.2); opacity: 0;}
    }
    .photo-frame {
        width: 150px;
        height: 150px;
        border-radius: 50%;
        border: 5px solid white;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        margin: 20px auto;
        overflow: hidden;
        animation: float 3s ease-in-out infinite;
    }
    .photo-frame img {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }
    .signature {
        font-family: 'Dancing Script', cursive;
        font-size: 28px;
        color: #d63384;
        margin-top: 15px;
    }
    .btn-primary {
        background: linear-gradient(135deg, #ff6b81 0%, #ff8e53 100%);
        color: white !important;
        border: none;
        padding: 12px 30px;
        font-size: 18px;
        border-radius: 50px;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 5px 15px rgba(255, 107, 129, 0.4);
        margin: 20px auto;
        display: block;
    }
    .btn-primary:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 20px rgba(255, 107, 129, 0.6);
    }
    .music-note {
        position: fixed;
        bottom: 20px;
        right: 20px;
        font-size: 24px;
        color: #ff6b81;
        animation: bounce 2s infinite;
    }
    @keyframes bounce {
        0%, 100% {transform: translateY(0);}
        50% {transform: translateY(-10px);}
    }
    </style>
""", unsafe_allow_html=True)

# Main heading
st.markdown("""
    <h1 style='text-align: center; color: #d63384; font-family: "Dancing Script", cursive;
    animation: fadeIn 2s forwards; margin-bottom: 10px;'>
    🌸 A Special Mother's Day Gift 🌸
    </h1>
    <p style='text-align: center; color: #666; font-size: 18px; margin-bottom: 30px;'>
    Click on the envelope to reveal your surprise</p>
""", unsafe_allow_html=True)

# Envelope
st.markdown("""
    <div class="container">
        <div class="envelope" id="envelope">
            <div class="flap"></div>
        </div>
    </div>
""", unsafe_allow_html=True)

# Open button
clicked = st.button("💖 Open Your Gift 💖", key="open_btn", help="Click to reveal your special message")

if clicked:
    # Background music
    try:
        autoplay_audio("audio.mp3")
        st.markdown('<div class="music-note">🎵</div>', unsafe_allow_html=True)
    except:
        pass

    # JS to open envelope flap
    st.markdown("""
        <script>
        document.getElementById('envelope').classList.add('open');
        </script>
    """, unsafe_allow_html=True)

    time.sleep(1)

    # Message box with image and message
    st.markdown(f"""
        <div class="message-container show">
            <div class="photo-frame">
                <img src="{base64_img}" alt="Mother">
            </div>
            <h2 style="color: #d63384; font-family: 'Dancing Script', cursive; font-size: 32px;">
                To The World's Best Mom
            </h2>
            <p style="font-size: 18px; line-height: 1.6; color: #555;">
                No matter how old I get, I'll always need my mom.<br>
                Your love is the light that guides me through life.<br>
                Thank you for your endless patience, unconditional love,<br>
                and for always believing in me.
            </p>
            <p style="font-size: 20px; color: #ff6b81; margin: 20px 0;">
                🌷 You are loved more than you'll ever know 🌷
            </p>
            <div class="signature">With all my love</div>
        </div>
    """, unsafe_allow_html=True)

    # Floating hearts
    for i in range(15):
        st.markdown(
            f'<div class="heart" style="left: {10 + (i * 6)}%; bottom: -20px; animation-duration: {5 + (i % 3)}s; animation-delay: {i * 0.2}s;"></div>',
            unsafe_allow_html=True
        )

    # Flower animation
    st.markdown("""
        <div style="text-align: center; margin-top: 20px; animation: fadeIn 2s forwards;">
            <span style="font-size: 30px; margin: 0 5px; animation: float 3s ease-in-out infinite;">🌼</span>
            <span style="font-size: 40px; margin: 0 5px; animation: float 4s ease-in-out infinite 0.5s;">🌹</span>
            <span style="font-size: 35px; margin: 0 5px; animation: float 3.5s ease-in-out infinite 1s;">🌸</span>
            <span style="font-size: 30px; margin: 0 5px; animation: float 3s ease-in-out infinite 1.5s;">🌺</span>
            <span style="font-size: 40px; margin: 0 5px; animation: float 4s ease-in-out infinite 2s;">🌻</span>
        </div>
    """, unsafe_allow_html=True)
