import streamlit as st
import llm_service

def main():
    st.set_page_config(
        page_title="Book Recommendation Engine", 
        page_icon="📚", 
        layout="centered"
    )

    # App Header Styling
    st.title("📚 Book Recommendation Engine")
    st.markdown("### *Your Personal AI-Powered Librarian*")
    st.write("Answer the 5 rapid questions below to discover books tailored to your exact emotional state.")
    st.write("---")
    
    # --- FORM INPUTS ---
    st.subheader("🔮 Define Your Current Vibe")
    
    mood = st.selectbox(
        "1. What is your current emotional state?", 
        [
            "Stressed and need an escape", 
            "Adventurous and energetic", 
            "Melancholic and reflective", 
            "Curious and intellectual", 
            "Cozy and nostalgic"
        ]
    )

    pacing = st.radio(
        "2. What kind of pacing are you looking for?", 
        ["A fast-paced page-turner", "A steady, character-driven journey", "A slow-burn that builds tension"]
    )

    setting = st.text_input(
        "3. What type of environment do you want to be transported to?",
        placeholder="e.g., A sprawling cyberpunk city, a quiet countryside, deep space..."
    )

    with st.expander("Advanced Narrative Preferences"):
        familiarity = st.select_slider(
            "4. Do you want genre-typical comfort or something wildly unique?",
            options=["Give me all the tropes", "A healthy mix", "Completely unconventional"],
            value="A healthy mix"
        )

    recent_favorite = st.text_area(
        "5. What was the last book or movie you thoroughly enjoyed, and why?",
        placeholder="e.g., Interstellar because of the mind-bending sci-fi elements and emotional core."
    )

    # --- RECOMMENDATION ENGINE LOGIC ---
    st.write("---")
    if st.button("✨ Generate My Custom Reading List", use_container_width=True):
        if not setting or not recent_favorite:
            st.error("⚠️ Please fill out all text options (Questions 3 and 5) so the AI can build an accurate profile!")
        else:
            with st.spinner("🕵️‍♂️ Scanning the literary universe to match your mood..."):
                try:
                    # Fetch structured results and fallback status from Phase 4 llm_service
                    result, is_fallback = llm_service.get_book_recommendations(
                        mood, pacing, setting, familiarity, recent_favorite
                    )
                    
                    # Alert the user if we are offline / hitting API errors
                    if is_fallback:
                        st.warning("📡 **Network Interruption:** The AI Librarian is currently unreachable. Displaying our offline, universally loved classics instead!")
                    else:
                        st.balloons()
                        st.success("🎯 Your Curated Matches Are Ready!")
                    
                    st.write(" ")
                    
                    # Render the beautiful UI cards
                    for idx, book in enumerate(result.books):
                        with st.container(border=True):
                            st.markdown(f"### 📖 {idx + 1}. {book.title}")
                            st.markdown(f"**By:** *{book.author}* | **Genre:** `{book.genre}`")
                            st.markdown("**Plot Overview:**")
                            st.write(book.synopsis)
                            st.info(f"💡 **Why this fits:** {book.why_it_fits}")
                            st.write(" ")
                            
                except Exception as e:
                    st.error(f"A critical error occurred: {e}")

if __name__ == "__main__":
    main()