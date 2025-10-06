import streamlit as st
import random as rm

st.markdown(
    """
    <style>
    .big-heading {
        font-family: 'Consolas', 'Courier New', monospace;
        font-size: 40px;
        font-weight;
        text-align: left;
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<div class='big-heading'>⛩️ Random JJK Character Generator</div>", unsafe_allow_html=True)

st.caption("This WebApp Gives you a random Jujutsu Kaisen Character to sketch or whatever your purpose is!!!\nGive It A Try!:")

st.set_page_config(page_title="JJK Character Generator", page_icon="⛩️", layout="centered")

characters = [
    "Masamichi Yaga🧸", "Satoru Gojo🤞", "Atsuya Kusakabe🗡️", "Kiyotaka Ijichi", "Shoko Ieiri",
    "Yuji Itadori👊", "Megumi Fushiguro🐺", "Nobara Kugisaki", "Maki Zenin🗡️",
    "Panda🐼", "Toge Inumaki📢", "Yuta Okkotsu🗡️", "Kinji Hakari👌",
    "Yoshinobu Gakuganji", "Utahime Iori", "Mai Zenin🔫", "Mechamaru🤖",
    "Kokichi Muta", "Kasumi Miwa🗑️", "Noritoshi Kamo (Kyoto)🩸🏹", "Aoi Todo👏", "Nishimiya Momo",
    "Kento Nanami🔪", "Takuma Ino", "Mei Mei💸", "Yuki Tsukumo", "Master Tengen",
    "Naobito Zen'in", "Naoya Zen'in", "Hajime Kashimo⚡️", "Hana Kurusu😇", "Hiromi Higuruma⚖️",
    "Fumihiko Takaba", "Rin Amai", "Iori Hazenoki💥", "Dhruv Lakdawala", "Ryu Ishiguro💥",
    "Takako Uro", "Charles Bernard🖋️", "Riko Amanai", "Misato Kuroi🧹", "Ui Ui🪓", "Mahito",
    "Jogo🔥", "Hanami🌸", "Dagon (final form)🐙", "Dagon (womb)🐙", "Rika (Cursed)", "Rika",
    "Kuchisake-Onna", "Cursed Naoya", "Kurouroshi🐞", "Choso🩸", "Eso🖼️", "Kechizu🖼️",
    "Finger bearer curse", "Rainbow Dragon🐉", "Ko-Guy🦗", "Suguru Geto🔮", "Mimiko Hasaba",
    "Nanako Hasaba", "Miguel", "Larue👊", "Sukuna⛩️", "Kenjaku (Geto)🔮", "Uraume❄️",
    "Juzo Kumiya", "Haruta Shigemo🗡️", "Noritoshi Kamo (Kenjaku)☂️",
    "Toji Fushiguro🔪", "Shiu Kong", "Tsumiki Fushiguro🛌", "Takada-chan", "Mahoraga☸",
    "Divine Dogs🐺", "Nue🐦", "Fleeing Rabbits🐇", "Gama Toad🐸", "Orachi Great Serpent🐍",
    "Max Elephant🐘", "Round Deer🦌", "Peircing Ox🐂"
]

if "char" not in st.session_state:
    st.session_state.char = None

if st.button("🎲 Proceed"):
    st.session_state.char = rm.choice(characters)

if st.session_state.char:
    st.success(f"**Your Character is:** {st.session_state.char}")

st.caption("-Aaradhya Rampuriya")
st.caption("  Developer")
