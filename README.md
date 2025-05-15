# tailor-price-predictor

🚀 **Status: Ready for Use** 🚀

## 📌 Description
**tailor-price-predictor** is a machine learning application that predicts tailoring service prices and turnaround times, built with a user-friendly interface using Streamlit. The model uses Multiple Linear Regression with a multi-output approach to simultaneously predict both price and production time.

## 📁 Project Structure
```
tailor-price-predictor/
├── app_modules/
│   ├── __init__.py            # Module initialization
│   ├── about.py               # About page module
│   ├── prediction.py          # Price prediction logic
│   ├── style.css              # CSS styles for the app
│   └── views/                 # Additional view components
├── data/                      # Directory for storing datasets
│   ├── processed/             # Processed data ready for modeling
│   └── raw/                   # Original data from tailors
├── models/                    # Directory for storing trained models
│   ├── model_akhir.pkl        # Trained prediction model
│   └── prediction_model.ipynb # Model training notebook
├── LICENSE                    # Project license file
├── README.md                  # Project documentation
├── requirements.txt           # Dependencies and libraries
└── streamlit_app.py           # Main Streamlit application
```

## 🚀 Installation & Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/adzkykhairany/tailor-price-predictor.git
   cd tailor-price-predictor
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