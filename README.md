# **Car Price Prediction App – README**

## **Overview**

This project is a **Machine Learning–based Car Price Prediction System** that estimates the market price of a used car based on key vehicle features such as brand, model, mileage, engine capacity, fuel type, and more.
The system uses multiple regression models, evaluates their performance, and automatically selects and saves the best model for future predictions.

---

## **Features**

* ✔️ Data preprocessing and cleaning
* ✔️ Label encoding and scaling
* ✔️ Multiple ML models tested and evaluated
* ✔️ Automatic selection of the best model
* ✔️ Saved model (`best_model.pkl`) for real-time predictions
* ✔️ Prediction function to estimate car prices from user input
* ✔️ Visualization of model performance (R² comparison chart)

---

## **Technologies Used**

* **Python**
* **Pandas**, **NumPy**
* **Scikit-Learn**
* **Matplotlib** / **Seaborn**
* **Joblib** for saving models

---

## **Project Structure**

**```
├── carprice_dataset.csv        # Training dataset
├── steamlit_app.py               # streamlit app for the user interface
├── car_price_model.pkl            # Saved best-performing model
├── scaler.pkl                  # Saved scaler for transformations
├── README.md                   # Project documentation
|--carprice.ipynb               #Main notebook containing model training code
```**

---

## **How the Model Works**

1. **Load and preprocess the dataset**
   Missing values are handled, categorical columns are label-encoded, and numerical columns are scaled.

2. **Train multiple machine-learning models**
   Examples include:

   * Linear Regression
   * Ridge Regression
   * Lasso Regression
   * Decision Tree
   * Gradient Boosting
   * Random Forest
   * KNN

3. **Evaluate Models**
   Each model generates:

   * MAE
   * MSE
   * RMSE
   * R² score

4. **Select Best Model**
   The model with the highest R² score is saved as:

   ```
   car_price_model.pkl
   ```

5. **Predict Car Price Using User Input**
   Using the `predict_price()` function, users can input car details and get an estimated price.

---

## **How to Run the Project**

### **1. Install Required Libraries**

```bash
pip install pandas numpy scikit-learn matplotlib seaborn joblib xgboost
```

### **2. Launch Jupyter Notebook**

```bash
jupyter notebook
```

### **3. Open the project notebook**

Run each cell in order to:

* Preprocess data
* Train models
* Save the best model
* Generate predictions

---

## **Model Prediction Example**

```python
sample_input = {
    'Company Name': 'Toyota',
    'Model Name': 'Corolla',
    'Model Year': 2020,
    'Location': 'Punjab',
    'Mileage': 30000,
    'Engine Type': 'Petrol',
    'Engine Capacity': 1300,
    'Color': 'White',
    'Assembly': 'Local',
    'Body Type': 'Sedan',
    'Transmission Type': 'Automatic',
    'Registration Status': 'Registered'
}

predicted_price = predict_price(sample_input)
print(predicted_price)
```

---

## **Outputs**

* A printed model comparison table
* A bar chart showing R² scores
* Saved `car_price_model.pkl` for deployment
* Price predictions for any user input
