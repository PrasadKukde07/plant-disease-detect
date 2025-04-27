import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import base64
import io  # Import the io module

# Load the image
try:
    bg_image = Image.open("image.jpeg")
except FileNotFoundError:
    bg_image = None
    st.warning("Background image 'image.jpeg' not found.")

# Function to encode the background image to base64
def bg_image_base64():
    if bg_image:
        buffered = io.BytesIO()
        bg_image.save(buffered, format=bg_image.format)
        img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')
        return img_str
    return None

# Function for Tensorflow Model Prediction
def model_prediction(test_image):
    model = tf.keras.models.load_model("trained_model.keras")
    image = tf.keras.preprocessing.image.load_img(test_image, target_size=(128, 128))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr])  # Convert single image to batch
    predictions = model.predict(input_arr)
    return np.argmax(predictions)  # Return index of max element

# Function for disease prevention (Improved with more comprehensive advice)
def disease_prevention(disease_name):
    prevention_methods = {
        "Apple___Apple_scab": [
            "Apply fungicides preventatively, starting in early spring.",
            "Choose scab-resistant apple varieties.",
            "Rake and destroy fallen leaves to reduce overwintering inoculum.",
            "Prune trees to improve air circulation and reduce humidity."
        ],
        "Apple___Black_rot": [
            "Remove and destroy mummified fruits and cankered branches.",
            "Apply fungicides at pink bud and petal fall.",
            "Maintain tree vigor through proper fertilization and watering.",
            "Practice good sanitation in the orchard."
        ],
        "Apple___Cedar_apple_rust": [
            "Remove cedar trees within a few miles of apple orchards.",  # miles instead of meters
            "Apply fungicides during pink bud and bloom stages.",
            "Choose resistant apple varieties.",
            "Destroy galls on cedar trees before they release spores."
        ],
        "Apple___healthy": ["Regularly monitor trees for any signs of disease.", "Maintain good orchard hygiene."],
        "Blueberry___healthy": ["Ensure proper soil drainage.", "Use disease-free planting material."],
        "Cherry_(including_sour)___Powdery_mildew": [
            "Apply fungicides at bloom and after harvest.",
            "Prune trees to improve air circulation.",
            "Use resistant varieties if available."
        ],
        "Cherry_(including_sour)___healthy": ["Monitor trees and maintain plant vigor."],
        "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": [
            "Use resistant corn hybrids.",
            "Practice crop rotation with non-host crops.",
            "Apply fungicides if disease pressure is high.",
            "Manage residue to reduce overwintering inoculum."
        ],
        "Corn_(maize)___Common_rust_": [
            "Plant resistant corn hybrids.",
            "Apply fungicides preventively in susceptible hybrids.",
            "Monitor fields regularly for rust development."
        ],
        "Corn_(maize)___Northern_Leaf_Blight": [
            "Select resistant hybrids.",
            "Practice crop rotation and residue management.",
            "Apply fungicides at tasseling or silking if needed."
        ],
        "Corn_(maize)___healthy": ["Use good farming practices."],
        "Grape___Black_rot": [
            "Apply fungicides protectively, especially before bloom and after fruit set.",
            "Remove mummified berries and prune out infected canes.",
            "Ensure good air circulation within the canopy."
        ],
        "Grape___Esca_(Black_Measles)": [
            "Practice careful pruning to minimize wounds.",
            "Apply wound protectants after pruning.",
            "Remove and destroy infected wood.",
            "Maintain healthy vines through balanced nutrition and watering."
        ],
        "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": [
            "Apply fungicides during wet periods.",
            "Practice good sanitation.",
            "Improve air circulation."
        ],
        "Grape___healthy": ["Regular monitoring."],
        "Orange___Haunglongbing_(Citrus_greening)": [
            "Control Asian citrus psyllid vectors with insecticides.",
            "Remove and destroy infected trees.",
            "Use disease-free budwood for propagation.",
            "Apply nutritional sprays to improve tree health."
        ],
        "Peach___Bacterial_spot": [
            "Apply bactericides preventively.",
            "Use resistant peach varieties.",
            "Practice good orchard sanitation.",
            "Prune to improve air circulation."
        ],
        "Peach___healthy": ["Regular monitoring."],
        "Pepper,_bell___Bacterial_spot": [
            "Use disease-free seeds and transplants.",
            "Apply copper-based bactericides.",
            "Practice crop rotation.",
            "Avoid overhead irrigation."
        ],
        "Pepper,_bell___healthy": ["Regular monitoring."],
        "Potato___Early_blight": [
            "Apply fungicides protectively, especially during wet weather.",
            "Use resistant varieties.",
            "Practice crop rotation.",
            "Maintain plant vigor."
        ],
        "Potato___Late_blight": [
            "Use resistant varieties.",
            "Apply fungicides preventively, especially during cool, wet weather.",
            "Destroy infected plants promptly.",
            "Improve field drainage."
        ],
        "Potato___healthy": ["Regularly monitor."],
        "Raspberry___healthy": ["Regular monitoring."],
        "Soybean___healthy": ["Regular monitoring."],
        "Squash___Powdery_mildew": [
            "Use resistant varieties.",
            "Apply fungicides, including systemic types.",
            "Ensure good air circulation.",
            "Water at the base of plants to avoid wetting foliage."
        ],
        "Strawberry___Leaf_scorch": [
            "Use resistant strawberry varieties.",
            "Apply fungicides.",
            "Remove and destroy infected leaves.",
            "Ensure adequate spacing for air circulation."
        ],
        "Strawberry___healthy": ["Regularly monitor."],
        "Tomato___Bacterial_spot": [
            "Use disease-free transplants.",
            "Apply copper-based bactericides and mancozeb.",
            "Practice crop rotation.",
            "Avoid overhead watering."
        ],
        "Tomato___Early_blight": [
            "Apply fungicides preventively.",
            "Use resistant varieties.",
            "Remove and destroy infected leaves.",
            "Provide adequate plant spacing."
        ],
        "Tomato___Late_blight": [
            "Use resistant varieties.",
            "Apply fungicides, especially during cool, wet weather.",
            "Destroy infected plants promptly.",
        ],
        "Tomato___Leaf_Mold": [
            "Use resistant varieties.",
            "Apply fungicides.",
            "Improve ventilation in greenhouses.",
            "Avoid overhead watering."
        ],
        "Tomato___Septoria_leaf_spot": [
            "Apply fungicides.",
            "Remove and destroy infected leaves.",
            "Practice crop rotation.",
            "Provide adequate plant spacing."
        ],
        "Tomato___Spider_mites Two-spotted_spider_mite": [
            "Use miticides.",
            "Encourage natural predators.",
            "Maintain plant vigor.",
            "Use insecticidal soap or horticultural oil."
        ],
        "Tomato___Target_Spot": [
            "Apply fungicides.",
            "Practice crop rotation.",
            "Remove infected leaves and fruit."
        ],
        "Tomato___Tomato_Yellow_Leaf_Curl_Virus": [
            "Control whitefly vectors with insecticides.",
            "Remove and destroy infected plants.",
            "Use resistant varieties if available."
        ],
        "Tomato___Tomato_mosaic_virus": [
            "Use resistant varieties.",
            "Practice good sanitation (wash hands, disinfect tools).",
            "Control aphid vectors.",
            "Remove infected plants."
        ],
        "Tomato___healthy": ["Regularly monitor."],
    }

    if disease_name in prevention_methods:
        st.subheader("Prevention Methods:")
        for method in prevention_methods[disease_name]:
            st.markdown(f"- {method}")
    else:
        st.write("No specific prevention methods found for this disease.")

# Streamlit App
def main():
    # Apply background image
    bg_str = bg_image_base64()
    if bg_str:
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("data:image/{bg_image.format.lower()};base64,{bg_str}");
                background-size: cover;
                background-repeat: no-repeat;
                background-attachment: fixed;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )

    st.title("Plant Disease Recognition") # Using st.title for the main heading

    # Prediction Page (No sidebar in this version)
    test_image = st.file_uploader("Choose an Image:", type=["jpg", "jpeg", "png"]) #accept image
    if test_image is not None: # check if image is uploaded
        if st.button("Show Image"):
            st.image(test_image, width=400, use_column_width=True)
        # Predict button
        if st.button("Predict"):
            st.write("Our Prediction:")
            try:
                result_index = model_prediction(test_image)
                class_name = ['Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy',
                              'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew',
                              'Cherry_(including_sour)___healthy', 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
                              'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy',
                              'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
                              'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot',
                              'Peach___healthy', 'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy',
                              'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy',
                              'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew',
                              'Strawberry___Leaf_scorch', 'Strawberry___healthy', 'Tomato___Bacterial_spot',
                              'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold',
                              'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite',
                              'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus',
                              'Tomato___healthy']
                # Display the prediction
                st.success(f"The model predicts it's a: {class_name[result_index]}")
                # Call the prevention function
                disease_prevention(class_name[result_index])
            except Exception as e:
                st.error(f"Error during prediction: {e}")

if __name__ == "__main__":
    import io
    main()
