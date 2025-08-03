# This is a project for creating a chatbot using LangChain and OpenAI's API.

## Description
In the `template_basic` directory, we are building a simple chatbot template. This chatbot uses a routing bot to handle different types of questions and send them to the right handler:
- FAQ Bot: Answers frequently asked questions.
- RAG Bot: Answers questions by retrieving information from a knowledge base.
- Default Bot: Handles all other questions.

The chatbot remembers the conversation history and logs everything to LangSmith.

There is also a feedback loop. Users can rate the chatbot's answers. The bot uses this feedback to improve its responses by rephrasing the question and generating a new answer. This helps the chatbot learn and get better over time.
This feedback loop happens internally. An agent evaluates the chatbot's answers, and if the answer is not good enough, it rephrases the question and tries again a few times before failing. This is especially useful for RAG.

See the workflow graph in the `chatbot_workflow_graph.png` file.

## How to run the chatbot
1. Install the required packages with `uv sync`.
2. Create a `.env` file in the `template_basic` directory with your OpenAI API key and other settings.
3. Build the vector storage by running `uv run template_basic/rag_input_documents/create_vector_storage.py`. This enables RAG for the chatbot.
4. Start the chatbot with `uv run template_basic/template_runner.py`.
5. Chat and enjoy!