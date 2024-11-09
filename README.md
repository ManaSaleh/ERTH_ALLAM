# ERTH - إرث

---

## Project Overview

**إرث** (Erth) is a multi-character simulation project designed to bring Saudi Arabian history to life by embodying a knowledgeable narrator. The narrator specializes in the history of Imam Muhammad bin Saud, the founder of the First Saudi State. This project offers an interactive experience, allowing users to engage with a character that shares authentic, well-researched stories of Saudi heritage, with a focus on cultural, political, and societal contributions.

## Features

- **Historical Character Simulation**: The narrator character has a detailed persona crafted to deliver insights on the history and cultural heritage of Najd and the early Saudi state.
- **Interactive Dialogue**: Users engage with the narrator through natural conversations, receiving contextual and accurate responses to their inquiries.
- **Comprehensive Historical Coverage**: The character shares detailed knowledge of Imam Muhammad bin Saud, his alliances, and his role in establishing the first Saudi state.
- **Educational and Cultural Platform**: This project serves as an educational resource, offering historical context and enriching users' understanding of Saudi Arabia's legacy.

## Project Structure

This project is organized into several directories for ease of use and modularity:

- **Data/**: Contains essential data files required for the character simulation, including historical texts, annotations, and processed datasets.
- **Notebooks/**: Jupyter notebooks for data exploration, analysis, and experimentation. These notebooks document the development and training of the model, as well as data insights.
- **Documents/**: Supplemental documentation, including research materials, historical references, and background information used to construct character knowledge.
- **Evaluation/**: Scripts and resources for evaluating the quality of interactions, character responsiveness, and overall performance metrics.
- **Scripts/**: Contains Python scripts that handle various functions, such as data preprocessing, model training, embedding generation, and deployment utilities.
- **UI/**: User interface assets, including design elements, configuration files, and images related to the user interface.

## Key Topics

1. **Imam Muhammad bin Saud**: Detailed accounts of his life, vision, and leadership.
2. **Unification of Najd**: Exploration of Imam Muhammad bin Saud's efforts to unify Najd and foster regional stability.
3. **Founding the First Saudi State**: Insights into the foundational principles, alliances, and governance established by Imam Muhammad bin Saud.
4. **Major Achievements**: Overview of his contributions to security, trade, education, culture, and international relations.
5. **Enduring Legacy**: Analysis of his impact on Saudi Arabian history and culture, and the significance of his contributions in shaping the region.

## User Interface

The user interface is designed to enhance interaction by providing an intuitive, engaging environment. Below is a preview of the UI:

![ERTH UI](Imges/ERTH_UI.jpeg)

## Technical Specifications

### Technology Stack

- **Language**: Python
- **Libraries**: LlamaIndex, Qdrant for embedding and storage, IBM Watsonx for natural language processing
- **Deployment**: Docker containerization for a consistent environment across platforms

### Deployment Overview

The project is containerized with Docker and uses Docker Compose for orchestrating multiple services. The architecture includes the LLM, database, and front-end interface as separate services, enabling streamlined deployment and management.

### System Requirements

- **Docker** and **Docker Compose** for containerized deployment
- **Python 3.8** or higher for local development
- API keys for **IBM Watsonx** and **Qdrant**
- **FastAPI** and **Streamlit** for the web interface (optional)

### Installation and Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/username/erth-multi-character-simulation.git
   cd erth-multi-character-simulation
   ```

2. **Configure Environment Variables**:
   Set up a `.env` file with API keys and other configurations:
   ```plaintext
   IBM_API_KEY=<your_ibm_key>
   QDRANT_API_KEY=<your_qdrant_key>
   ```

3. **Build and Launch with Docker Compose**:
   ```bash
   docker-compose up --build
   ```

4. **Access the Application**:
   Navigate to `http://localhost:8000` in a web browser to start interacting with the character.

## Usage Guide

- **Initiate a Conversation**: Users can pose questions related to Imam Muhammad bin Saud, historical events, or cultural heritage, and receive detailed, contextually accurate answers.
- **Explore Historical Insights**: Discover major historical events, alliances, and cultural insights through a conversational interface designed for educational engagement.

## Roadmap for Future Enhancements

- **Additional Historical Figures**: Expand the character lineup with additional figures from Saudi Arabian history.
- **Enhanced Response Mechanisms**: Improve dialogue interactions by implementing sophisticated response refinement modes for more nuanced answers.
- **Mobile Accessibility**: Develop a mobile-friendly version to increase accessibility.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

Special thanks to:

- **IBM Watsonx** for providing advanced NLP capabilities.
- **Qdrant** for efficient vector-based data storage and retrieval.

---
