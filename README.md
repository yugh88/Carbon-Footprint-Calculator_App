Here's an updated version of your README with the integration of blockchain and details about running the app and the tech stack:

---

# 🌳Carbon Footprint Calculator with Blockchain Integration 🌳

The global annual carbon footprint has now surpassed an alarming 40 billion tons, underscoring the urgent need for collective action to mitigate climate change. There exists a direct and undeniable correlation between the daily habits of individuals and the surge in CO2 emissions. Everyday practices, ranging from energy consumption and transportation to residential heating-cooling systems and food production-consumption, significantly contribute to this escalating environmental challenge. Recognizing the pivotal role individuals play in this scenario, it becomes imperative to foster awareness regarding their impact on the global increase in CO2 levels.

### New Feature: Blockchain Integration
This project now integrates blockchain technology to record and retrieve the user's carbon footprint data. The blockchain ensures a secure, transparent, and immutable record of all user inputs and their corresponding carbon footprint. By leveraging blockchain, the application provides a permanent, verifiable ledger that tracks individual carbon footprint calculations and their reduction efforts.

## 🛠️ Project Steps

### 🧩 Backend Development:
1. **Data Handling with Pandas**:
   - Used Pandas for data manipulation and analysis.

2. **NumPy for Numeric Operations**:
   - Leveraged NumPy for numerical operations and array manipulation.

3. **Machine Learning with scikit-learn**:
   - Implemented machine learning algorithms to predict carbon footprints based on user input.

4. **Blockchain Integration**:
   - Integrated blockchain to record and retrieve carbon footprint data.
   - Smart contracts are used to store footprint data on a blockchain, making it immutable and publicly verifiable.
   - The blockchain system enables secure data storage and retrieval based on user interactions with the calculator.

5. **Data Visualization**:
   - Used Matplotlib to create visualizations of the carbon footprint data.

6. **Image Processing with Pillow**:
   - Implemented image processing to visualize footprint data.

7. **Base64 Encoding/Decoding**:
   - Utilized Base64 encoding and decoding for handling image data within the blockchain.

### 🖥️ Frontend Development:
1. **Streamlit Setup**:
   - Streamlit was used for the frontend to build a user-friendly web application.

2. **User Interface Design**:
   - Designed an intuitive UI using Streamlit components, CSS, and JavaScript for seamless interaction.

3. **Blockchain Interaction UI**:
   - Added buttons for interacting with the blockchain, including recording carbon footprint data and retrieving it.

4. **Testing**:
   - Ensured the application functions correctly by testing the backend and frontend components.

## 👩‍🏫 How to Use

1. Visit [Carbon Footprint Calculator App](https://carbonfootprintcalculator.streamlit.app/).
2. If the app is inactive, please wait a few moments for it to wake up.
3. Fill out the form on the homepage, which includes personal habits and activities.
4. Navigate to the "Consumption" tab to calculate your carbon footprint.
5. Once your carbon footprint is calculated, you can:
   - View the results as a visual representation.
   - Record your footprint in the blockchain by clicking the "Save to Blockchain" button.
   - Retrieve your previous footprints from the blockchain using the "Retrieve from Blockchain" button.
6. Optionally, you can offset your carbon footprint by donating trees to a reforestation charity.

### Blockchain Interaction:
- The **Save to Blockchain** button stores the calculated carbon footprint data on a blockchain, ensuring it is securely recorded and can be accessed later.
- The **Retrieve from Blockchain** button allows users to view their previously stored footprint data from the blockchain.

## 🧑‍💻 Tech Stack:
- **Frontend**: Streamlit, HTML, CSS, JavaScript
- **Backend**: Python (with Pandas, NumPy, Matplotlib, Pillow)
- **Machine Learning**: Scikit-learn (for carbon footprint prediction)
- **Blockchain**: Ethereum, Solidity (for smart contracts), Web3.js (to interact with Ethereum)
- **Database**: Blockchain for immutable data storage
- **Other Libraries**: 
  - **Base64** (for encoding image data)
  - **Io** (for handling input/output operations)

## 💻 How to Run the App Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Carbon-Footprint-Calculator-App.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Carbon-Footprint-Calculator-App
   ```

3. Install the necessary dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Start the Streamlit app:
   ```bash
   streamlit run app.py
   ```

5. Open the app in your browser at `http://localhost:8501`.

## 👨‍👩‍👧‍👦 Team Members:

-Yugh Juneja 
-Shubhdeep Singh
-Aditya Singh
-Aryan Pandey
-Mansi Kapse

## 📺 Project Presentation

[Watch the Project Demo](https://github.com/mesutdmn/Carbon-Footprint-Calculator-App/assets/72805471/657285e0-eded-4296-8937-fd2d22f7aeef)

---

This updated README reflects the integration of blockchain and includes the necessary setup commands, as well as the tech stack used in the project.
