# **Restaurant Name and Menu Generator**
Welcome to the Restaurant Name and Menu Generator! This application leverages the power of the mistralai/Mixtral-8x7B-Instruct-v0.1 model and LangChain to generate unique restaurant names and curated menus based on the selected cuisine. The app is deployed using Streamlit, providing a seamless and interactive user experience.

**Features**
Cuisine Selection: Choose from a variety of cuisines to generate a relevant restaurant name and menu.
AI-Generated Content: Utilizes the advanced mistralai/Mixtral-8x7B-Instruct-v0.1 model for generating creative and contextually appropriate names and menus.
Interactive Interface: Built with Streamlit for a user-friendly and interactive experience.
Dynamic Output: Generates a new restaurant name and menu each time you select or change the cuisine.

**Installation**
To run this application locally, follow these steps:

Clone the repository:

git clone https://github.com/yourusername/restaurant-name-menu-generator.git
cd restaurant-name-menu-generator


Create a virtual environment:

python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`


Install the required packages:

pip install -r requirements.txt


Usage
To start the Streamlit app, run the following command:

streamlit run app.py


How to Use
Select Cuisine: Choose a cuisine from the dropdown menu.
Generate: Click on the 'Generate' button to produce a restaurant name and menu based on the selected cuisine.
View Results: The generated restaurant name and menu will be displayed on the screen.

Components
mistralai/Mixtral-8x7B-Instruct-v0.1 Model: This model is used for generating the names and menus. It is a sophisticated language model capable of understanding and creating relevant text based on input prompts.
LangChain: This library is used to handle the interaction between the input prompts and the AI model, ensuring coherent and contextually appropriate outputs.
Streamlit: A framework used to create the web interface, making the app interactive and easy to use.

Customization
You can customize the list of available cuisines or the format of the generated menus by modifying the cuisines.json and menu_format.json files respectively.

Contributing
We welcome contributions to enhance the functionality and features of this app. To contribute:

Fork the repository.
Create a new branch (git checkout -b feature/YourFeature).
Commit your changes (git commit -m 'Add YourFeature').
Push to the branch (git push origin feature/YourFeature).
Open a Pull Request.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
For any questions or issues, please open an issue in the repository or contact the project maintainer at chpraneethvardhanreddy143@gmail.com
