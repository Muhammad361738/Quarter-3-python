# # import streamlit as st
# # import pandas as pd
# # import os 
# # from io import BytesIO


# # # Set up our Streamlit app
# # st.set_page_config(page_title="Data Sweeper", layout="wide")
# # st.title("Data Sweeper")
# # st.write("Transform Your Files Between CSV and Excel formats with built-in data cleaning and visualization.")

# # # File uploader for multiple files
# # uploaded_files = st.file_uploader("Upload your files (CSV or Excel):", 
# #                                   type=["csv", "xlsx"], 
# #                                   accept_multiple_files=True)

# # # Helper function to read CSV with fallback encodings
# # def read_csv_with_fallback(file):
# #     encodings = ['utf-8', 'ISO-8859-1', 'cp1252']
# #     for encoding in encodings:
# #         try:
# #             return pd.read_csv(file, encoding=encoding)
# #         except Exception as e:
# #             continue
# #     st.error(f"Failed to read the CSV file. Try re-saving it in UTF-8 format.")
# #     return None

# # # Process each uploaded file
# # if uploaded_files:
# #     for file in uploaded_files:
# #         file_ext = os.path.splitext(file.name)[-1].lower()

# #         # Read CSV or Excel file with encoding fallback
# #         try:
# #             if file_ext == ".csv":
# #                 df = read_csv_with_fallback(file)
# #             elif file_ext == ".xlsx":
# #                 df = pd.read_excel(file)
# #             else:
# #                 st.error(f"Unsupported file type: {file_ext}")
# #                 continue

# #             if df is None:
# #                 continue
# #         except Exception as e:
# #             st.error(f"Error loading file {file.name}: {str(e)}")
# #             continue

# #         # Display file details
# #         st.write(f'**File Name:** {file.name}')
# #         st.write(f'**File Size:** {file.size / 1024:.2f} KB')

# #         # Show first 5 rows of the dataframe
# #         st.write("Preview of the Data:")
# #         st.dataframe(df.head())

# #         # Data Cleaning Options
# #         st.subheader("Data Cleaning Options")
# #         if st.checkbox(f"Clean Data for {file.name}"):
# #             col1, col2 = st.columns(2)

# #             with col1:
# #                 if st.button(f"Remove Duplicates from {file.name}"):
# #                     df.drop_duplicates(inplace=True)
# #                     st.write("✅ Duplicates Removed!")

# #             with col2:
# #                 if st.button(f"Fill Missing Values for {file.name}"):
# #                     numeric_cols = df.select_dtypes(include=['number']).columns
# #                     df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
# #                     st.write("✅ Missing Values Filled!")

# #             # Column Selection
# #             st.subheader("Select Columns to Keep")
# #             selected_columns = st.multiselect(f"Choose Columns for {file.name}", df.columns, default=df.columns)
# #             df = df[selected_columns]

# #         #  create some visualiation 
# #         st.subheader(" Data Visualization ")

# #         if st.checkbox(f"Show Visualization for {file.name}"):
# #             st.bar_chart(df.select_dtypes(include="number").iloc[:,:2])

# #         #  Convert the file --> CSV to Excel
# #         st.subheader("Conversion Option ")
# #         conversion_type = st.radio(f'Convert {file.name} to: ',["CSV","Excel"], key=file.name)
# #         if st.button(f"Convert {file.name}"):
# #             buffer = BytesIO()
# #             if conversion_type == "CSV":
# #                 df.to_csv(buffer, index=False)
# #                 file_name = file.name.replace(file_ext, ".csv")
# #                 mime_type = "text/csv"


# #             elif conversion_type == "Excel":
# #                 df.to_excel(buffer, index=False)
# #                 file_name = file.name.replace(file_ext, ".xlsx")
# #                 mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
# #             buffer.seek(0)


# #             #  Dowmload button 
# #             # st.download_button(
# #             #     label=f"Downloads {file.name} as {conversion_type}",
# #             #     data= buffer,
# #             #     file = file_name ,
# #             #     mime = mime_type

# #             # )
# #             st.download_button(
# #             label=f"Download {file.name} as {conversion_type}",
# #             data=buffer,
# #             file_name=file_name,
# #             mime=mime_type
# #             )
# # st.success(" All filles processed !")


# import streamlit as st
# import pandas as pd
# import os 
# from io import BytesIO


# # Set up our Streamlit app
# st.set_page_config(page_title="Data Sweeper", layout="wide")
# st.title("Data Sweeper")
# st.write("Transform Your Files Between CSV and Excel formats with built-in data cleaning and visualization.")

# # File uploader for multiple files
# uploaded_files = st.file_uploader("Upload your files (CSV or Excel):", 
#                                   type=["csv", "xlsx"], 
#                                   accept_multiple_files=True)

# # Helper function to read CSV with fallback encodings
# def read_csv_with_fallback(file):
#     encodings = ['utf-8', 'ISO-8859-1', 'cp1252']
#     for encoding in encodings:
#         try:
#             return pd.read_csv(file, encoding=encoding)
#         except Exception as e:
#             continue
#     st.error(f"Failed to read the CSV file. Try re-saving it in UTF-8 format.")
#     return None

# # Process each uploaded file
# if uploaded_files:
#     for file in uploaded_files:
#         file_ext = os.path.splitext(file.name)[-1].lower()

#         # Read CSV or Excel file with encoding fallback
#         try:
#             if file_ext == ".csv":
#                 df = read_csv_with_fallback(file)
#             elif file_ext == ".xlsx":
#                 df = pd.read_excel(file)
#             else:
#                 st.error(f"Unsupported file type: {file_ext}")
#                 continue

#             if df is None:
#                 continue
#         except Exception as e:
#             st.error(f"Error loading file {file.name}: {str(e)}")
#             continue

#         # Display file details
#         st.write(f'**File Name:** {file.name}')
#         st.write(f'**File Size:** {file.size / 1024:.2f} KB')

#         # Show first 5 rows of the dataframe
#         st.write("Preview of the Data:")
#         st.dataframe(df.head())

#         # Data Cleaning Options
#         st.subheader("Data Cleaning Options")
#         if st.checkbox(f"Clean Data for {file.name}"):
#             col1, col2 = st.columns(2)

#             with col1:
#                 if st.button(f"Remove Duplicates from {file.name}"):
#                     df.drop_duplicates(inplace=True)
#                     st.write("✅ Duplicates Removed!")

#             with col2:
#                 if st.button(f"Fill Missing Values for {file.name}"):
#                     numeric_cols = df.select_dtypes(include=['number']).columns
#                     df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
#                     st.write("✅ Missing Values Filled!")

#             # Column Selection
#             st.subheader("Select Columns to Keep")
#             selected_columns = st.multiselect(f"Choose Columns for {file.name}", df.columns, default=df.columns)
#             df = df[selected_columns]

#         #  create some visualiation 
#         st.subheader(" Data Visualization ")

#         if st.checkbox(f"Show Visualization for {file.name}"):
#             st.bar_chart(df.select_dtypes(include="number").iloc[:,:2])

#         #  Convert the file --> CSV to Excel
#         st.subheader("Conversion Option ")
#         conversion_type = st.radio(f'Convert {file.name} to: ',["CSV","Excel"], key=file.name)
#         if st.button(f"Convert {file.name}"):
#             buffer = BytesIO()
#             if conversion_type == "CSV":
#                 df.to_csv(buffer, index=False)
#                 file_name = file.name.replace(file_ext, ".csv")
#                 mime_type = "text/csv"


#             elif conversion_type == "Excel":
#                 df.to_excel(buffer, index=False)
#                 file_name = file.name.replace(file_ext, ".xlsx")
#                 mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
#             buffer.seek(0)


#             #  Dowmload button 
#             # st.download_button(
#             #     label=f"Downloads {file.name} as {conversion_type}",
#             #     data= buffer,
#             #     file = file_name ,
#             #     mime = mime_type

#             # )
#             st.download_button(
#             label=f"Download {file.name} as {conversion_type}",
#             data=buffer,
#             file_name=file_name,
#             mime=mime_type
#             )
# st.success(" All filles processed !")


import streamlit as st
import pandas as pd
import os
import subprocess
import sys
from io import BytesIO

# Ensure 'openpyxl' is installed for handling Excel files
try:
    import openpyxl
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "openpyxl"])
    import openpyxl

# Set up our Streamlit app
st.set_page_config(page_title="Data Sweeper", layout="wide")
st.title("Data Sweeper")
st.write("Transform Your Files Between CSV and Excel formats with built-in data cleaning and visualization.")

# File uploader for multiple files
uploaded_files = st.file_uploader("Upload your files (CSV or Excel):", 
                                  type=["csv", "xlsx"], 
                                  accept_multiple_files=True)

# Helper function to read CSV with fallback encodings
def read_csv_with_fallback(file):
    encodings = ['utf-8', 'ISO-8859-1', 'cp1252']
    for encoding in encodings:
        try:
            return pd.read_csv(file, encoding=encoding)
        except Exception as e:
            continue
    st.error("Failed to read the CSV file. Try re-saving it in UTF-8 format.")
    return None

# Process each uploaded file
if uploaded_files:
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[-1].lower()

        # Read CSV or Excel file with encoding fallback
        try:
            if file_ext == ".csv":
                df = read_csv_with_fallback(file)
            elif file_ext == ".xlsx":
                df = pd.read_excel(file, engine='openpyxl')
            else:
                st.error(f"Unsupported file type: {file_ext}")
                continue

            if df is None:
                continue
        except Exception as e:
            st.error(f"Error loading file {file.name}: {str(e)}")
            continue

        # Display file details
        st.write(f'**File Name:** {file.name}')
        st.write(f'**File Size:** {file.size / 1024:.2f} KB')

        # Show first 5 rows of the dataframe
        st.write("Preview of the Data:")
        st.dataframe(df.head())

        # Data Cleaning Options
        st.subheader("Data Cleaning Options")
        if st.checkbox(f"Clean Data for {file.name}"):
            col1, col2 = st.columns(2)

            with col1:
                if st.button(f"Remove Duplicates from {file.name}"):
                    df.drop_duplicates(inplace=True)
                    st.write("✅ Duplicates Removed!")

            with col2:
                if st.button(f"Fill Missing Values for {file.name}"):
                    numeric_cols = df.select_dtypes(include=['number']).columns
                    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                    st.write("✅ Missing Values Filled!")

            # Column Selection
            st.subheader("Select Columns to Keep")
            selected_columns = st.multiselect(f"Choose Columns for {file.name}", df.columns, default=df.columns)
            df = df[selected_columns]

        # Data Visualization
        st.subheader("Data Visualization")

        if st.checkbox(f"Show Visualization for {file.name}"):
            st.bar_chart(df.select_dtypes(include="number").iloc[:, :2])

        # Conversion Options
        st.subheader("Conversion Options")
        conversion_type = st.radio(f'Convert {file.name} to:', ["CSV", "Excel"], key=file.name)

        if st.button(f"Convert {file.name}"):
            buffer = BytesIO()
            if conversion_type == "CSV":
                df.to_csv(buffer, index=False)
                file_name = file.name.replace(file_ext, ".csv")
                mime_type = "text/csv"

            elif conversion_type == "Excel":
                df.to_excel(buffer, index=False, engine='openpyxl')
                file_name = file.name.replace(file_ext, ".xlsx")
                mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

            buffer.seek(0)

            # Download button
            st.download_button(
                label=f"Download {file.name} as {conversion_type}",
                data=buffer,
                file_name=file_name,
                mime=mime_type
            )

st.success("All files processed successfully!")
