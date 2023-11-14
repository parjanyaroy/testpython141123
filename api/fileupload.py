import streamlit as st
import os

def upload_pdf(name):
    st.title('PDF Upload App')
    
    uploaded_file = st.file_uploader(f"Hello {name}, please upload a PDF", type=['pdf'])
    
    if uploaded_file is not None:
        with open(os.path.join('tempDir',uploaded_file.name),"wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success("File uploaded successfully!")
        
        # Display the variables in the log
        st.text('Uploaded File Name: ' + str(uploaded_file.name))
        st.text('Uploaded File Size: ' + str(uploaded_file.size))
        st.text('Uploaded File Type: ' + str(uploaded_file.type))

# Call the function
upload_pdf('SampleFile')
