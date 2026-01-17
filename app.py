import streamlit as st
import tempfile
import os

from trip_sheet_generator import generate_trip_sheets

st.set_page_config(page_title="Trip Sheet Generator")

st.title("🚕 Trip Sheet PDF Generator")
st.write("Upload Excel file and click Generate")

excel_file = st.file_uploader(
    "Upload Excel File",
    type=["xlsx"]
)

if excel_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".xlsx") as tmp:
        tmp.write(excel_file.read())
        excel_path = tmp.name

    watermark_image = "hanuman.png"
    output_pdf = "Trip_Sheets_Output.pdf"

    if st.button("Generate Trip Sheets PDF"):
        generate_trip_sheets(
            excel_path,
            output_pdf,
            watermark_image
        )

        with open(output_pdf, "rb") as f:
            st.download_button(
                "⬇️ Download PDF",
                f,
                file_name="Trip_Sheets.pdf",
                mime="application/pdf"
            )
