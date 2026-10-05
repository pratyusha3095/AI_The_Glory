import streamlit as st
import serpapi

# -----------------------------
# PAGE SETUP
# -----------------------------

st.set_page_config(
    page_title="AI The Glory",
    page_icon="🤖"
)

st.title("🤖 AI The Glory")
st.write("Search the web and get simple, useful results.")

# -----------------------------
# SERPAPI
# -----------------------------

serp = serpapi.Client(
    api_key=st.secrets["SERPAPI_KEY"]
)

# -----------------------------
# USER QUESTION
# -----------------------------

question = st.text_input(
    "🔎 What do you want to search?",
    placeholder="Example: What is Artificial Intelligence?"
)

# -----------------------------
# SEARCH
# -----------------------------

if st.button("🔍 Search"):

    if not question.strip():
        st.warning("Please enter a question.")

    else:

        with st.spinner("Searching the web..."):

            try:
                results = serp.search({
                    "engine": "google",
                    "q": question,
                    "num": 5
                })

                sources = results.get(
                    "organic_results",
                    []
                )

            except Exception as e:
                st.error(f"Something went wrong: {e}")
                st.stop()

        # -----------------------------
        # RESULTS
        # -----------------------------

        if not sources:
            st.warning("No results found.")
        else:

            st.subheader("📚 Search Results")

            for i, result in enumerate(sources, 1):

                title = result.get(
                    "title",
                    "Untitled"
                )

                snippet = result.get(
                    "snippet",
                    "No description available."
                )

                link = result.get(
                    "link",
                    ""
                )

                st.markdown(
                    f"### {i}. {title}"
                )

                st.write(snippet)

                if link:
                    st.link_button(
                        "🔗 Open Source",
                        link
                    )

                st.divider()