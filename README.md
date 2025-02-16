# tailor-price-predictor

🚧 **Status: In Development** 🚧

## 📌 Description
**tailor-price-predictor** is a machine learning model development project for predicting tailoring service prices, equipped with a GUI interface using Streamlit. This project is still in its early stages and will be continuously updated.

## 📁 Project Structure
```
tailor-price-predictor/
├── src/                 # Main code for database, preprocessing, and model
│   ├── database/        # Database-related files
│   │   ├── connection.py # PostgreSQL connection
│   │   ├── query.py      # Query handling
│   ├── predict.py       # Prediction function
│   ├── preprocessing.py # Preprocessing stage
│   ├── train.py         # Model training
├── streamlit_app/       # Streamlit application
│   ├── app.py           # GUI for users
├── test/                # Unit testing
│   ├── test_database.py # Database connection testing
│   ├── test_model.py    # Model testing
│   ├── test_preprocessing.py # Preprocessing testing
├── LICENSE              # Project license
├── README.md            # Main project documentation
├── requirements.txt     # List of dependencies
```

## 🚀 Installation & Usage (Under Development)

1. Clone the repository:
   ```bash
   git clone https://github.com/adzkykhairany/tailor-price-predictor.git
   cd tailor-price-predictor
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit application (currently in development):
   ```bash
   streamlit run streamlit_app/app.py
   ```

## 🛠 Planned Features
🚧 Connect to PostgreSQL to retrieve data 📊  
🚧 Data preprocessing (normalization, encoding) 🔄  
🚧 Train a machine learning model for price prediction 📈  
🚧 Interactive GUI using Streamlit 🖥  
🚧 Unit testing for database, preprocessing, and model 🔬  
🚧 Complete documentation for project setup and usage 📄  

## 📜 License
This project is licensed under the LICENSE file. Please check the license file for details.