import streamlit as st
import os
import requests

st.set_page_config(
    page_title="AI Property Marketplace",
    layout="wide"
)

st.title("🏠 AI Real Estate Marketplace")

poster_folder = "posters"

if not os.path.exists(poster_folder):
    st.error("approved_posters folder not found")

else:

    files = os.listdir(poster_folder)

    if len(files) == 0:
        st.info("No approved properties available")

    else:

        cols = st.columns(2)

        for i, file in enumerate(files):

            with cols[i % 2]:

                st.image(
                    os.path.join(poster_folder, file),
                    use_container_width=True
                )

                st.markdown("### Interested in this property?")

                buyer_name = st.text_input(
                    "Name",
                    key=f"name_{file}"
                )

                phone = st.text_input(
                    "Phone",
                    key=f"phone_{file}"
                )

                purpose = st.selectbox(
                    "Purpose",
                    ["Buy", "Rent"],
                    key=f"purpose_{file}"
                )

                if st.button(
                        "Send Interest",
                        key=f"btn_{file}"
                ):

                    property_id = (
                        file
                        .replace("poster_", "")
                        .replace(".png", "")
                    )

                    response = requests.post(
                        "http://127.0.0.1:8000/interest",
                        json={
                            "property_id": property_id,
                            "buyer_name": buyer_name,
                            "phone": phone,
                            "purpose": purpose
                        }
                    )

                    if response.status_code == 200:
                        st.success(
                            "Interest sent successfully"
                        )
                    else:
                        st.error(
                            "Failed to send request"
                        )

                st.divider()