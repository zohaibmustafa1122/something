import json
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="For My Guddi 💗",
    page_icon="💗",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Hide Streamlit's default chrome so it feels like a real app, not a Streamlit page
st.markdown(
    """
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .block-container {padding: 0 !important; margin: 0 !important; max-width: 100% !important;}
    iframe {border: none;}
    </style>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# ✏️ EDIT EVERYTHING BELOW THIS LINE TO PERSONALIZE THE PAGE
# ============================================================

HER_NAME = "Meri Guddi"
YOUR_NAME = "Zohaib"

# Optional: your WhatsApp number with country code, digits only, no + or spaces.
# Example for Pakistan: "923001234567". Leave as "" to skip the WhatsApp button.
WHATSAPP_NUMBER = "923097889488"

OPENING_LINE = "menu pta ay main tuhada dil dukhaya ay lkn yaqeen kro ,main har roz pachtandan."
MEMORY = "Yaad kro apan kinny thek c apas vich bas lokan di waja tun dooriyan aa gyan"
APOLOGY = "Main buht ghalat kitta buht dil dukhaya tuhada lkn yaqeen kro main buht yaad kitta tuhanon inna dinnan vich , plzz hunr maaaf kr dyo na , hor guzara nai honda tuhady beghair"
PROMISE = "main waada krdan main sb kujh thek kr dyan ga, bas akhri chance dy dy."
CLOSING_LINE = "You are still, and always will be, the best part of my life. I'm not asking you to forget — just to give us one more chance to talk."

# Add / edit as many memories as you like — each becomes a swipeable card
MEMORIES = [
    {"emoji": "🌅", "date": "The beginning", "text": "Write about how you two met or your first real conversation."},
    {"emoji": "😂", "date": "A silly memory", "text": "Write about a moment that always makes you both laugh."},
    {"emoji": "🌧️", "date": "A hard day", "text": "Write about a time she supported you or you supported her."},
    {"emoji": "🏡", "date": "A quiet moment", "text": "Write about a small everyday memory you miss the most."},
]

# 6 short reasons — each becomes a tap-to-flip card
REASONS = [
    "Tussi jidan meri care krdy c.",
    "tuhada msg vekh k meri saari preshanian door ho jandian sanr.",
    "tuhadi sohnrian akkhan.",
    "tussi jehry menu nickname dendy c.",
    "Simply , because you're you.",
    "I love you so much meri guddi.",
]

# A short, honest section about what these two months have been like for you.
# Keep it real, not dramatic — a few sentences is enough.
PAIN_LINES = [
    "inna dinnan vich roz tuhadi id khol k dkhdan.",
    "roz purani chats parhdan roz tuhady voice not sunrdan.",
    "tuhadi ik ik video ha mere kol o daily dkhdan",
]

# The date (YYYY-MM-DD) you two last really talked — used to show a live day counter
LAST_TALKED_DATE = "2026-05-13"

# Path to a photo to show in this section (any image in the same folder as app.py)
PHOTO_PATH = "photo.png"
PHOTO_CAPTION = "a memory I still smile at"

# The 4-digit PIN she needs to unlock the page — you said her birthday, so DDMM format
PIN_CODE = "0602"
PIN_HINT = "hint: pincode of my phone"

# ============================================================
# Do not edit below this line
# ============================================================

with open("experience_template.html", "r", encoding="utf-8") as f:
    html_code = f.read()

import base64
import mimetypes

def photo_data_url(path: str) -> str:
    mime, _ = mimetypes.guess_type(path)
    mime = mime or "image/png"
    with open(path, "rb") as img_f:
        b64 = base64.b64encode(img_f.read()).decode("ascii")
    return f"data:{mime};base64,{b64}"

def js_str(value: str) -> str:
    """Safely encode a Python string as a JS string literal (handles quotes, apostrophes, etc.)"""
    return json.dumps(value, ensure_ascii=False)

replacements = {
    "__HER_NAME__": js_str(HER_NAME),
    "__YOUR_NAME__": js_str(YOUR_NAME),
    "__WHATSAPP_NUMBER__": js_str(WHATSAPP_NUMBER),
    "__OPENING_LINE__": js_str(OPENING_LINE),
    "__MEMORY__": js_str(MEMORY),
    "__APOLOGY__": js_str(APOLOGY),
    "__PROMISE__": js_str(PROMISE),
    "__CLOSING_LINE__": js_str(CLOSING_LINE),
    "__MEMORIES_JSON__": json.dumps(MEMORIES, ensure_ascii=False),
    "__REASONS_JSON__": json.dumps(REASONS, ensure_ascii=False),
    "__PAIN_LINES_JSON__": json.dumps(PAIN_LINES, ensure_ascii=False),
    "__LAST_TALKED_DATE__": js_str(LAST_TALKED_DATE),
    "__PIN_CODE__": js_str(PIN_CODE),
    "__PIN_HINT__": js_str(PIN_HINT),
    # These two are inserted directly into HTML attributes/text, not JS, so no JSON quoting
    "__PHOTO_DATA_URL__": photo_data_url(PHOTO_PATH),
    "__PHOTO_CAPTION__": PHOTO_CAPTION,
}

for token, value in replacements.items():
    html_code = html_code.replace(token, value)

components.html(html_code, height=1900, scrolling=True)
