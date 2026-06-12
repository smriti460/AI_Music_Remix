import streamlit as st
from remix import remix_song

# ---------------- CSS ---------------- #

st.markdown("""
<style>

.main-title{
    text-align:center;
    color:#ff4b4b;
    font-size:45px;
    font-weight:bold;
}

.subtitle{
    text-align:center;
    font-size:20px;
    color:gray;
}

.mood-box{
    background-color:#f5f5f5;
    padding:15px;
    border-radius:10px;
    margin-top:10px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ---------------- #

st.markdown("""
<div style='text-align:center;padding:20px;'>
    <h1>🎵 AI Music Remix & Mood Generator</h1>
    <p>Create mood-based remixes of your favorite songs instantly!</p>
</div>
""", unsafe_allow_html=True)

# ---------------- FILE UPLOAD ---------------- #

uploaded_file = st.file_uploader(
    "📁 Upload a Song",
    type=["mp3", "wav"]
)

if uploaded_file is not None:

    st.success("✅ Song Uploaded Successfully!")

    st.write("🎵 Song Name:", uploaded_file.name)

    # Original Audio
    st.subheader("Original Song")
    st.audio(uploaded_file)

    # Mood Selection
    mood = st.selectbox(
        "🎭 Select Mood",
        [
            "Happy 😊",
            "Sad 😔",
            "Energetic 🔥",
            "Relaxing 🌙"
        ]
    )

    st.info(f"Selected Mood: {mood}")

    # Remix Button
    if st.button("🎵 Generate Remix"):

        output = remix_song(uploaded_file, mood)

        st.success("🎉 Remix Generated Successfully!")

        st.subheader("Remixed Song")

        st.audio(output)

        # Download Button
        with open(output, "rb") as file:

            st.download_button(
                label="⬇ Download Remix",
                data=file,
                file_name="remix.wav",
                mime="audio/wav"
            )

# ---------------- FOOTER ---------------- #

st.markdown("---")

st.markdown(
    "<center>Developed using Python, Streamlit and Pydub</center>",
    unsafe_allow_html=True
)