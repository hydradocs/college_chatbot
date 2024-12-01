# SARA - College Chatbot for RVS College of Engineering and Technology  

SARA is an AI-powered chatbot designed to assist visitors and prospective students of **RVS College of Engineering and Technology**. Built using Python, NLTK, and machine learning, SARA provides information about college courses, eligibility criteria, fee structures, and much more.

## Features  

- **Course Information**: Provides details about courses offered.  
- **Eligibility Criteria**: Answers queries about course eligibility.  
- **Fee Structure**: Shares details about the tuition and other fees.  
- **Course Recommendation**: Suggests courses based on user preferences.  
- **Placement Data**: Displays college placement statistics and achievements.  
- **Event Updates**: Shares details about past and upcoming college events.  
- **Sports Facilities**: Offers information about sports and extracurricular activities.  
- **User Interaction Storage**: Saves data of new visitors into a MySQL database for follow-up or administrative purposes.  

## Tech Stack  

- **Frontend**: HTML, CSS, JavaScript  
- **Backend**: Python (Flask/Django)  
- **AI & NLP**: Python, NLTK, Machine Learning  
- **Database**: MySQL  
- **Cloud**: Hosting for chatbot and database  

## Setup and Installation  

### Prerequisites  

- Python 3.8 or higher  
- MySQL Server  
- pip (Python package installer)  

### Installation Steps  

1. Clone the repository:  
   ```bash  
   git clone https://github.com/your-repository/sara-college-chatbot.git  
   cd sara-college-chatbot  
   ```  

2. Create and activate a virtual environment:  
   ```bash  
   python -m venv env  
   source env/bin/activate  # For Linux/macOS  
   env\Scripts\activate     # For Windows  
   ```  

3. Install required dependencies:  
   ```bash  
   pip install -r requirements.txt  
   ```  

4. Set up the MySQL database:  
   - Create a database named `sara_db`.  
   - Import the provided schema using:  
     ```sql  
     mysql -u root -p sara_db < schema.sql  
     ```  
   - Update `config.py` with your database credentials.  

5. Run the application:  
   ```bash  
   python app.py  
   ```  

6. Access the chatbot at `http://localhost:5000`.  

## Project Structure  

```plaintext  
sara-college-chatbot/  
├── app.py                  # Main application file  
├── config.py               # Configuration file for database and settings  
├── static/                 # Frontend assets (CSS, JS, Images)  
├── templates/              # HTML templates  
├── chatbot/                # Core chatbot logic  
│   ├── intents/            # Predefined intents for conversations  
│   ├── models/             # ML models and training scripts  
│   ├── utils/              # Helper functions  
├── database/               # MySQL schema and queries  
├── requirements.txt        # Python dependencies  
└── README.md               # Project documentation  
```  

## Contributors  

- **Hydra Team**  
  - Sourav Singh  
  - Vikash Mandal  

## Future Enhancements  

- Add voice support for interactions.  
- Implement real-time notifications for events.  
- Integrate with the college website for seamless functionality.  

## License  

This project is licensed under the [MIT License](LICENSE).  
