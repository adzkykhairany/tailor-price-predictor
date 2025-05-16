# tailoring-predictor

🚀 **Status: Ready for Use** 🚀

## 📌 Description
**tailoring-predictor** is a machine learning application that predicts tailoring service prices and turnaround times, built with a user-friendly interface using Streamlit.The model uses Multiple Linear Regression with a multi-output approach to simultaneously predict both price and production time. The data is based on a survey of 10 tailoring businesses operating in Pasar Sunan Giri, Rawamangun, Jakarta Timur.

## 📁 Project Structure
```
tailoring-predictor/
├── views/                     # View components for the application
│   ├── __init__.py            # Module initialization
│   ├── about.py               # About page component
│   ├── prediction.py          # Price prediction logic and UI
│   ├── catalog.py             # Clothing model catalog component
│   ├── style.css              # CSS styles for the app
├── data/                      # Directory for storing datasets
├── images/                    # Images of clothing models
├── models/                    # Directory for storing trained models
│   ├── model_akhir.pkl        # Trained prediction model
│   └── prediction_model.ipynb # Model training notebook
├── LICENSE                    # Project license file
├── README.md                  # Project documentation
├── requirements.txt           # Dependencies and libraries
└── streamlit_app.py           # Main Streamlit application
```

## 🚀 Live Demo & Installation

### 💻 Live Demo
Try the live application here: <a href="https://tailor-predictor.streamlit.app" target="_blank">tailor-predictor</a>

### 🛠️ Local Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/adzkykhairany/tailoring-predictor.git
   cd tailoring-predictor
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit application:
   ```bash
   streamlit run streamlit_app.py
   ```

## ✅ Implemented Features
1. Data collection from 10 tailoring businesses in Pasar Sunan Giri, Rawamangun, Jakarta Timur
2. Data preprocessing and encoding
3. Multiple Linear Regression model trained for price and time prediction
4. Interactive GUI using Streamlit with:
   - Navigation menu with 3 pages (Prediction, Clothing Models, About)
   - Clothing model selection (Kebaya Traditional, Kebaya Modern, Blus, Midi Dress, Maxi Dress)
   - Material type selection (Katun, Sutra, Brokat, Sifon, Satin)
   - Ornament/embellishment options (13 different options including embroidery and sequins)
   - Input validation and error handling
   - Real-time price and time estimates with clear display
5. Visual clothing model catalog with images and descriptions
6. Detailed "About" page explaining the methodology and data sources
7. Responsive design with custom styling

## 💻 Technical Details
- Built with Streamlit v1.45.0
- Prediction model developed using scikit-learn v1.6.1
- Uses joblib v1.4.2 for model serialization and loading
- Data visualization capabilities with matplotlib v3.10.0 and seaborn v0.13.2
- Image handling with pillow v11.1.0
- Data manipulation with pandas v2.2.3 and numpy v2.0.2

## 🛠 Future Improvements
- Add more fabric types and clothing model options
- Enhance prediction accuracy with additional training data
- Implement user accounts for saving previous estimates
- Add comparison feature between different model/material combinations
- Develop a responsive mobile interface
- Integrate with local tailor service booking systems

## 📜 License
This project is licensed under the LICENSE file. Please check the license file for details.

## 👩‍💻 Author
© 2025 Athiyya Adzky Khairany