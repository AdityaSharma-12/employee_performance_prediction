👕 Garment Worker Productivity Prediction

This project focuses on building and deploying a machine learning model to predict the productivity of garment workers based on various operational metrics. The model is served via a lightweight Python Flask web application.

🔗 Project Links                                              
Status            Live Demo
Complete          https://employee-performance-prediction-qgt9.onrender.com/ 


🌟 Project Goal and Features

The objective is to provide an analytical tool that uses historical data to forecast worker efficiency.

    Prediction Target: Garment Worker Productivity Classification (e.g., Target Met/Not Met).
    
    Modeling: Uses a classification algorithm (e.g., Logistic Regression, Random Forest) trained on features like work-in-progress, idle time, and actual vs. required effort.                                                                                                                                                
    
    Deployment: The trained model is saved using pickle and loaded into a Flask server for real-time inference.

🛠️ Technical Stack

Category	      Technology	                      Role 
Core Language	  Python 3.x	                    Backend logic and machine learning tasks.
Web Framework	   Flask	                        Serves the web interface and handles API requests.
Machine Learning  Scikit-learn, Pandas, NumPy	Model training, data handling, and preparation.
Model Persistence	Pickle	                    Serializes the trained model for loading in the production environment.
Interface	         HTML	                        Creates the user-friendly data input form and displays results.
Hosting	           Render 	                     Platform hosting the live web application.