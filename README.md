Here’s the complete `README.md` with the UI image added:

---

# إرث - Multi-Character Simulation

## Project Overview

**إرث** is an interactive simulation that brings historical narratives to life through the character of a narrator who specializes in the history of Imam Muhammad bin Saud, the founder of the first Saudi state. This project aims to provide users with engaging, conversational insights into the life, achievements, and legacy of Imam Muhammad bin Saud, while also incorporating elements of Saudi Arabian heritage and history.

## Features

- **Character Simulation**: The simulated narrator character has a distinct personality, with knowledge and storytelling abilities focused on the history and culture of Najd and the early Saudi state.
- **Dynamic Interaction**: Users can ask questions and engage in conversation with the narrator, who responds with historical insights and well-structured answers.
- **Historical Content**: Includes detailed information about Imam Muhammad bin Saud, his alliance with Sheikh Muhammad ibn Abdul-Wahhab, and his efforts in unifying Najd and establishing the first Saudi state.
- **Educational and Cultural Resource**: Offers a platform to learn about Saudi history, culture, and the legacy of its founding figures.

## Key Topics Covered

1. **Biography of Imam Muhammad bin Saud**: Insights into his early life, role as a leader, and achievements.
2. **Unification of Najd**: How Imam Muhammad bin Saud led the unification efforts in Najd and established stability and peace.
3. **Foundation of the First Saudi State**: The founding principles and alliances that helped establish the state.
4. **Achievements**: Notable contributions in various fields, including security, trade, education, culture, and international relations.
5. **Legacy**: Lasting impacts on Saudi Arabian history and the symbolic importance of his efforts.

## User Interface

Here’s a preview of the user interface:

![ERTH UI](Image/ERTH_UI.jpeg)

## Technical Details

### Tech Stack

- **Programming Language**: Python
- **Frameworks/Libraries**: LlamaIndex, Qdrant (for data handling and embedding), IBM Watsonx (for language processing)
- **Containerization**: Docker (for deployment and environment setup)

### Deployment

The application is containerized with Docker, ensuring a consistent environment across different systems. The multi-character simulation is deployed via Docker Compose, with separate services handling different components such as the LLM (Large Language Model), database, and front-end interface.

### Requirements

- Docker and Docker Compose installed on the host machine.
- Python 3.8 or higher.
- API keys for IBM Watsonx and Qdrant (if applicable).
- For a web interface, FastAPI and Streamlit can be used.

### Setup and Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/username/erth-multi-character-simulation.git
   cd erth-multi-character-simulation
   ```

2. **Configure Environment Variables**:
   Create a `.env` file to store your API keys and other configurations.
   ```plaintext
   IBM_API_KEY=<your_ibm_key>
   QDRANT_API_KEY=<your_qdrant_key>
   ```

3. **Build and Run with Docker Compose**:
   ```bash
   docker-compose up --build
   ```

4. **Access the Application**:
   Open `http://localhost:8000` in your browser to interact with the simulated character.

### Usage

- **Start a Conversation**: Ask questions about Imam Muhammad bin Saud's life, achievements, or Saudi history, and receive informative responses.
- **Learn about Key Events**: Understand significant historical events, the formation of alliances, and cultural developments.

## Future Enhancements

- **Additional Characters**: Introduce other historical figures for a broader simulation.
- **Enhanced Interaction**: Implement response modes to refine answers and simulate more nuanced dialogue.
- **Mobile Application**: Develop a mobile version for accessibility.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- **IBM Watsonx** for advanced language processing capabilities.
- **Qdrant** for efficient vector-based data handling.

---

This README provides a full overview of the project, instructions for setup and usage, as well as future enhancement plans. Let me know if you'd like any further customization!
