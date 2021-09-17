import streamlit as st
import docx2txt
from web.utils import read_pdf


def sidebox():

    # TODO: Retrain your model with pipeline...Fit & return the pipeline

    return None


def main():

    with st.container():

        st.markdown("Upload a File")

        st.write("File can be in the format of '.docx,pdf,txt' ")

        file = st.file_uploader(label="File Upload", type=["txt", "docx", "pdf"])

        if file is not None:
            if st.button("Process", key="process"):
                file_details = dict(
                    filename=file.name, file_type=file.type, file_size=file.size
                )
                st.write(file_details)
                if file.type == "application/pdf":
                    st.write(read_pdf(file))
                    return read_pdf(file)
                elif file.type == "text/plain":
                    raw_text = str(file.read(), "utf-8")
                    st.write(raw_text)
                    return raw_text
                else:
                    raw_text = docx2txt.process(file)
                    st.write(raw_text)
                    return raw_text


if __name__ == "__main__":
    st.header("Document Tagger")

    st.sidebar.markdown("## Model Options ")

    model = st.sidebar.selectbox(
        label="Select A Model", options=["LDAModel", "HeiracialModel"]
    )

    main()
