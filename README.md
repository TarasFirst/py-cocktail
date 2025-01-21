# Cocktail Advisor Chat

Cocktail Advisor Chat is a Python-based project designed to provide cocktail recommendations and advice using a Retrieval-Augmented Generation (RAG) system. It integrates vector databases and the latest OpenAI library for seamless interaction and robust performance.

## Features
- **Cocktail Recommendation**: Offers personalized cocktail suggestions.
- **FastAPI Framework**: Provides an intuitive API interface for interaction.
- **Modern Dependencies**: Uses the latest libraries such as LangChain and OpenAI.

## Project Structure
```
├── chain.py          # Core chain implementation for RAG
├── config.py         # Configuration file (paths, environment variables)
├── main.py           # Main FastAPI application
├── load_data.py      # Data loading utility
├── cocktails.csv     # Dataset of cocktail recipes and information
├── requirements.txt  # Project dependencies
```

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Set up a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   Create a `.env` file in the root directory and specify required variables:
   ```env
   OPENAI_API_KEY=your_openai_api_key
   ```

## Usage

1. **Run the application**:
   ```bash
   uvicorn main:app_tip_cocktail --reload
   ```

2. **Access the API**:
   Open your browser and navigate to:
   ```
   http://127.0.0.1:8000/docs
   ```
   Explore the available endpoints and test the application.

## Dataset
The `cocktails.csv` file contains columns such as:
- `name`: Name of the cocktail.
- `ingredients`: List of ingredients.
- `category`: Type or category of the cocktail.
- `glassType`: Suggested glass for serving.
- `alcoholic`: Indicates if the drink contains alcohol.

## Acknowledgments
- [OpenAI](https://openai.com) for their powerful APIs.
- [FastAPI](https://fastapi.tiangolo.com) for the elegant web framework.
- [LangChain](https://www.langchain.com) for robust tools in RAG workflows.
