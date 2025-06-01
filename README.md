# tailoring-predictor

🚀 **Status: Ready for Use** 🚀

## 📌 Description
**Tailoring Predictor** is a machine learning application that predicts tailoring service prices and turnaround times, built with a user-friendly interface using Streamlit. The model uses Multiple Linear Regression with a multi-output approach to simultaneously predict both price and production time.

## 📁 Project Structure
```
tailor-predictor/
├── views/                     # View components
│   ├── __init__.py            # Module initialization
│   ├── about.py               # About page module
│   ├── catalog.py             # Clothing reference catalog
│   ├── prediction.py          # Price prediction logic
│   └── style.css              # CSS styles for the app
├── data/                      # Directory for storing dataset
│   └── data.csv               # Processed data used for modeling
├── images/                    # Directory for reference images
│   ├── blus.png               # Blouse reference image
│   ├── kebaya_modern.png      # Modern kebaya reference image
│   ├── kebaya_tradisional.png # Traditional kebaya reference image
│   ├── maxi.jpg               # Maxi dress reference image
│   └── midi_dress.png         # Midi dress reference image
├── models/                    # Directory for storing trained models
│   ├── model_akhir.pkl        # Trained prediction model
│   └── prediction_model.ipynb # Model training notebook
├── LICENSE                    # Project license file
├── README.md                  # Project documentation
├── requirements.txt           # Dependencies and libraries
└── streamlit_app.py           # Main Streamlit application
```

## 🚀 Installation & Usage

1. **Option 1: Access online**
   
   Visit the deployed application at: [https://tailor-predictor.streamlit.app](https://tailor-predictor.streamlit.app)

2. **Option 2: Run locally**

   a. Clone the repository:
   ```bash
   git clone https://github.com/adzkykhairany/tailoring-predictor.git
   cd tailoring-predictor
   ```
   b. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   c. Run the Streamlit application:
   ```bash
   streamlit run streamlit_app.py
   ```

## ✅ Implemented Features
1. Data collection from 10 tailoring businesses in Pasar Sunan Giri, Rawamangun  
2. Data preprocessing and encoding  
3. Multiple Linear Regression model trained for price and time prediction  
4. Interactive GUI using Streamlit with:
   - Model selection interface
   - Material type selection
   - Ornament/embellishment options
   - Error validation
   - Real-time predictions  
5. Detailed "About" page explaining the methodology  

## 🛠 Future Improvements
- Add more fabric and model options
- Enhance prediction accuracy with more training data
- Add user accounts for saving previous estimates
- Create a responsive mobile interface

## 📜 License
This project is licensed under the LICENSE file. Please check the license file for details.