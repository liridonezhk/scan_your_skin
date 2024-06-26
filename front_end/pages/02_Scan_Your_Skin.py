import streamlit as st
import requests
from PIL import Image

# Title
highlighted_text_title = (
    "<span style='font-size: 30px; color: gray; text-decoration: underline overline;font-family: Calibri; '>"
    "**SCAN YOUR SKIN**"
    "</span>"
)
st.markdown(highlighted_text_title, unsafe_allow_html=True)

# Sidebar
st.sidebar.markdown('''
## <span style="font-size: 14px;">Jihyeong LEE</span><br><span style="font-size: 14px;">Julijana STEIMLE</span><br><span style="font-size: 14px;">Liridone ZHUGOLLI</span><br><span style="font-size: 14px;">Loredana HOREZEANU</span>
''', unsafe_allow_html=True)



predict_url = 'https://melcont-frvnbh56ia-ew.a.run.app/predict'
two_mode = st.selectbox('Choose How', ['Upload Image File', 'Live Capture'])

def send_prediction_request(image_bytes):
    files = {'img': image_bytes}
    response = requests.post(predict_url, files=files).json()
    return response

if two_mode == "Upload Image File":
    st.markdown('<h4 style="color:gray;">Upload the Image</h4>', unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        if st.button('Prediction'):
            response = send_prediction_request(uploaded_file.getvalue())
            st.write("The mole is ", response["Mole_prediction"], "with probability", response["with probability of"])

elif two_mode == 'Live Capture':
    st.markdown('<h4 style="color:gray;">Live Capture</h4>', unsafe_allow_html=True)
    captured_picture = st.camera_input("Take a picture")
    if captured_picture:
        st.image(captured_picture, caption="Captured Image", use_column_width=True)
        if st.button('Prediction'):
            # Convert the BytesIO directly to bytes for the request
            image_bytes = captured_picture.getvalue()
            response = send_prediction_request(image_bytes)
            st.write("The mole is ", response["Mole_prediction"], "with probability", response["with probability of"])


#old code just in case


# import streamlit as st
# import requests
# from PIL import Image

# # Title
# highlighted_text_title = (
#     "<span style='font-size: 30px; color: gray; text-decoration: underline overline;font-family: Calibri; '>"
#     "**SCAN YOUR SKIN**"
#     "</span>"
# )
# st.markdown(highlighted_text_title, unsafe_allow_html=True)

# predict_url = 'https://melcont-frvnbh56ia-ew.a.run.app/predict'
# two_mode = st.selectbox('Choose How', ['Upload Image File', 'Live Capture'])

# if two_mode == "Upload Image File":
#     # File uploader
#     st.markdown('<h4 style="color:gray;">Upload the Image</h2>', unsafe_allow_html=True)
#     uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
#     print(type(uploaded_file), "this is the type")
#     # Check the uploaded Image
#     if uploaded_file is not None:
#         # Read Image file
#         image = Image.open(uploaded_file)
#         print(image)
#         # Display the uploaded image
#         st.image(image, caption="Uploaded Image", use_column_width=True)
#         #Predict Button
#         predict_button = st.button('Prediction')
#         # When the Button "Prediction" is pushed >> Link it to Model
#         if predict_button:
#             files = {'img': uploaded_file.getvalue()}
#             response = requests.post(predict_url, files=files).json()
#             print(f"THIS IS THE RESPONCE{response}")
#             print(response["Mole_prediction"])
#             #result = response.json()
#             st.write("The mole is ", response["Mole_prediction"], "with probability", response["with probability of"])


# elif two_mode =='Live Capture':
#     st.markdown('<h4 style="color:gray;">Live Capture</h4>', unsafe_allow_html=True)
#     captured_picture = st.camera_input("Take a picture")
#     if captured_picture:
#         st.image(captured_picture, caption="Captured Image", use_column_width=True)
#         #Predict Button
#         predict_button = st.button('Prediction')
#         # When the Button "Prediction" is pushed >> Link it to Model
#         if predict_button:
#             files = {'img': captured_picture.getvalue()}
#             response = requests.post(predict_url, files=files).json()
#             print(f"THIS IS THE RESPONCE{response}")
#             print(response["Mole_prediction"])
#             #result = response.json()
#             st.write("The mole is ", response["Mole_prediction"], "with probability", response["with probability of"])
