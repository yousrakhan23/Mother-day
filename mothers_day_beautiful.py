import streamlit as st
import time

st.set_page_config(page_title="Mother's Day Envelope", page_icon="💌", layout="centered")

# Custom CSS for gorgeous UI
st.markdown("""
    <style>
    body {
        background-color: #fff0f5;
    }
    .container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }
    .envelope {
        width: 300px;
        height: 200px;
        background: linear-gradient(135deg, #ff9a9e 0%, #fad0c4 100%);
        position: relative;
        margin-top: 50px;
        cursor: pointer;
        border-radius: 20px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.2);
        transition: transform 0.5s ease;
    }
    .envelope:hover {
        transform: scale(1.05);
    }
    .flap {
        width: 0;
        height: 0;
        border-left: 150px solid transparent;
        border-right: 150px solid transparent;
        border-bottom: 100px solid #ff6f91;
        position: absolute;
        top: -100px;
        left: 0;
        border-radius: 20px 20px 0 0;
    }
    .message {
        display: none;
        text-align: center;
        margin-top: 30px;
        font-size: 22px;
        color: #d63384;
        font-weight: bold;
        animation: fadeIn 2s forwards;
    }
    .show {
        display: block !important;
    }
    @keyframes fadeIn {
        from {opacity: 0;}
        to {opacity: 1;}
    }

    /* Heart floating animation */
    .heart {
        position: fixed;
        top: 50%;
        left: 50%;
        width: 20px;
        height: 20px;
        background-color: #ff6f91;
        transform: translate(-50%, -50%) rotate(45deg);
        animation: floatUp 5s infinite ease-in;
        opacity: 0.6;
        border-radius: 50%;
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
        0% {transform: translate(-50%, -50%) rotate(45deg) translateY(0);}
        100% {transform: translate(-50%, -50%) rotate(45deg) translateY(-600px);}
    }
    </style>
""", unsafe_allow_html=True)

# Envelope title
st.markdown("<h1 style='text-align: center; color: #d63384;'>💖 Special Mother's Day 💖</h1>", unsafe_allow_html=True)

# Button
clicked = st.button("💌 Open Your Surprise 💌")

# Envelope display
st.markdown("""
    <div class="container">
        <div class="envelope">
            <div class="flap"></div>
        </div>
    </div>
""", unsafe_allow_html=True)

# When clicked show message + hearts
if clicked:
    time.sleep(0.5)
    st.markdown("""
        <p class="message show">
            🌸 Happy Mother's Day! 🌸<br>
            You are my sunshine, my heart, my everything. 💕<br>
            Thank you for your endless love. 🌷
        </p>
    """, unsafe_allow_html=True)

    # Show floating hearts (5 hearts)
    for i in range(5):
        st.markdown('<div class="heart" style="left: {}%; animation-delay: {}s;"></div>'.format(20*i + 10, i), unsafe_allow_html=True)
