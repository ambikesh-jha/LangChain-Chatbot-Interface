from langchain import PromptTemplate

# Define a basic prompt template
basic_template = """Question: {question}
Answer: Let's think step by step."""

# Function to retrieve a prompt template
def get_prompt_template(template_type="basic"):
    if template_type == "basic":
        return PromptTemplate(template=basic_template, input_variables=["question"])
    # Add other template types if needed
