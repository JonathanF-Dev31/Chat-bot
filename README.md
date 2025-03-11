# Motorcycle Chatbot

## Project Overview
Motorcycle Chatbot is a web-based application designed to provide users with information about specific motorcycle models from the **Pulsar** brand. Users can select a model and ask questions, receiving AI-generated responses.

## Features
- Interactive chatbot for answering questions about motorcycles.
- Supports **four specific Pulsar models**:
  - **Pulsar N160**
  - **Pulsar NS200**
  - **Pulsar 220F**
  - **Pulsar RS200**
- Simple and responsive user interface.
- Feedback system to evaluate the chatbot's responses.

## Technologies Used
- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Flask (Python)
- **AI Model:** `g4f` API for generating chatbot responses

## Installation & Setup
### Prerequisites
- Python 3.x installed
- Flask installed (`pip install flask`)
- `g4f` module installed (`pip install g4f`)


## API Endpoints
### `GET /`
- Renders the **index.html** page with the chatbot interface.

### `POST /api/chat`
- **Request:**
  ```json
  {
    "model": "Pulsar N160",
    "question": "What is the fuel efficiency?"
  }
  ```
- **Response:**
  ```json
  {
    "response": "The Pulsar N160 has a fuel efficiency of approximately 45 km/l."
  }
  ```
- **Validation:** Only allows queries about the four predefined Pulsar models.

## AI Model Used
The chatbot uses the `g4f` API to generate responses. The AI model interacts with the user by processing the provided motorcycle model and question, ensuring accurate and relevant answers.

## License
This project is open-source and free to use.

## Author
Developed by [Your Name].

## Acknowledgments
Special thanks to the `g4f` API contributors for providing a free AI-based solution.

