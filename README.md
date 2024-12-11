# Diabetic Retinopathy Detection using Deep Learning

## 🩺 **Why is Diabetic Retinopathy Detection Important?**
Diabetic Retinopathy (DR) is one of the leading causes of blindness in adults worldwide, caused by prolonged high blood sugar levels that damage the retina. Early detection and classification of DR stages are critical for preventing vision loss and ensuring timely treatment.

---

## 🚀 **Project Overview**
This project is an advanced AI-based system to detect and classify the stages of diabetic retinopathy from retinal images. Using a pretrained **ResNet-18** model, the system is fine-tuned for accurate classification and evaluation of DR stages.

---

## 🌟 **Key Features**
- **Non-Invasive Detection**: Uses retinal images to predict DR stages, reducing the need for invasive diagnostics.
- **ResNet-18 Backbone**: Fine-tuned for robust detection and classification.
- **Performance Monitoring**: Integrated **confusion matrix**, **ROC curve**, and **training vs. validation accuracy plots**.
- **Data Augmentation**: Addresses class imbalance and enhances feature extraction for better accuracy.

---

## 📊 **Dataset Summary**
- **Classes**:
  - `No DR`: Healthy retina
  - `Mild`: Early signs of DR
  - `Moderate`: Increased severity of DR
  - `Severe`: Pre-proliferative stage
  - `Proliferative DR`: Advanced stage of DR
- **Data Split**:
  - **Training Set**: 70%
  - **Validation Set**: 15%
  - **Test Set**: 15%

---

## ⚙️ **Technologies Used**

| **Technology**       | **Logo**                                                                                  |
|-----------------------|-------------------------------------------------------------------------------------------|
| **Python**           | ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) |
| **PyTorch**          | ![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white) |
| **Flask**            | ![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white) |
| **HTML**             | ![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white) |
| **CSS**              | ![CSS](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white) |
| **JavaScript**       | ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black) |
| **Matplotlib**       | ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=python&logoColor=white) |
| **GitHub**           | ![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white) |

---

## 📂 **Folder Structure**

.
├── app.py    <br>           
├── model.pth      <br>       
├── dataset/    <br>           
├── templates/index.html    <br>       
├── static/style.css      <br>         
├── images/      <br>          
└── README.md    <br>         

---

## 🚀 **How to Run This Project**
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/liver-fibrosis-detection.git
   cd liver-fibrosis-detection

2. Install Dependencies: 
Run the following command to install all required dependencies:
   ```bash 
   pip install -r requirements.txt

3. Run the Flask App
Start the Flask application by running:
   ```bash
   python app.py

4. Open Your Browser
Navigate to the following address in your web browser to access the application:
   ```bash
   http://127.0.0.1:5000

   
---
### 🔑 **Results**

Our model demonstrated exceptional accuracy and robust performance across all diabetic retinopathy stages, from No DR (healthy retina) to Proliferative DR (advanced stage). By effectively handling the challenges of differentiating between early stages such as Mild, Moderate, and Severe—which often exhibit subtle and overlapping characteristics—the model proves its reliability for clinical-grade diabetic retinopathy detection.

Leveraging the power of the pretrained ResNet-50 architecture, combined with advanced data augmentation techniques and extensive training, the model excels in identifying key patterns within retinal imaging data. The integration of a balanced dataset and careful preprocessing ensures its robustness and adaptability across various scenarios. Moreover, the use of metrics like the confusion matrix, ROC curves, and training-validation accuracy plots validates its high precision and recall across all classes, ensuring minimal misclassifications.

This achievement highlights the model's potential for real-world applications, such as:

Non-invasive diagnosis of diabetic retinopathy, reducing the need for invasive and costly diagnostic procedures.
Early-stage detection that enables healthcare professionals to intervene promptly, preventing vision loss or disease progression.
Monitoring disease progression and treatment efficacy in diabetic patients, ensuring better disease management and improved quality of life.


---

### 🙌 **Contributors**
#### Thilak R (https://github.com/thilak-r) <br>
#### under guidance of [Dr Agughasi Victor Ikechukwu](https://github.com/Victor-Ikechukwu) <br>
---

❤️ Thank You!
Thank you for checking out our project! We hope this inspires you to explore the intersection of AI and healthcare. Feel free to reach out for questions, suggestions, or collaborations.

<br><br>


📌 Keywords
#DiabeticRetinopathy #AIHealthcare #DeepLearning #MedicalAI #PyTorch #ResNet50 #ExplainableAI #HealthcareInnovation
