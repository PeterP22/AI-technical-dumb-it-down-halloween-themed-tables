import pandas as pd

# Convert the table content into structured data
data = {
    'Instead of Saying...': [
        "We're implementing Autogen",
        "Foundation Models are our base",
        "We're integrating YOLO Models",
        "Let's set up an Auto Labelling Pipeline",
        "Multimodal AI systems are key",
        "We'll deploy AI Copilot for assistance",
        "Adapters will fine-tune our AI",
        "Agentic AI for independent operations",
        "Knowledge Graph for data connection",
        "Large Language Models (LLM) for tasks",
        "AutoML for model optimization",
        "Hallucinations need to be addressed",
        "Generative AI for content creation",
        "Open Models vs Proprietary Models",
        "Cloud Native for AI deployment",
        # Additional relevant examples
        "We're implementing RAG architecture",
        "Vector DB integration required",
        "Implementing few-shot learning",
        "Deploying model quantization",
        "Implementing semantic search"
    ],
    'Say...': [
        "We're using a system to automatically generate code or content based on predefined rules or AI-driven insights",
        "We're starting with large-scale models pre-trained on vast datasets to adapt to a wide array of tasks quickly",
        "We're using real-time object detection models like YOLO for high-speed, high-accuracy image analysis",
        "We're creating an automated process to label data, reducing manual labor and enhancing model training efficiency",
        "We're employing AI models that can understand and generate content across different data types like text, images, and audio for richer interactions",
        "We're deploying a conversational AI interface to assist users in real-time with various tasks using natural language processing",
        "We're using small modules to adapt pre-trained models for new tasks without extensive retraining, saving time and resources",
        "We're developing AI systems that can pursue complex goals autonomously with minimal human supervision",
        "We'll use a structured representation to show relationships between entities, enhancing AI understanding and context in applications",
        "We're leveraging models like BERT, GPT-4 for various language-related tasks due to their deep understanding of language context",
        "We're automating the machine learning workflow to select, preprocess data, and tune models for optimal performance with minimal human input",
        "We need to mitigate instances where the AI generates incorrect or fabricated information, ensuring model reliability",
        "We'll use AI to generate new content, whether it's text, images, or other data types, based on learned patterns",
        "We're considering using models that are openly available with comparable performance to proprietary ones for flexibility in deployment",
        "We're deploying our AI solutions on cloud-native platforms like Kubernetes for scalability and efficiency in managing AI model lifecycle",
        # Additional explanations
        "We're enhancing our AI's responses by combining them with relevant information from our knowledge base",
        "We're setting up a specialized database to efficiently store and search through AI-processed information",
        "We're teaching our AI to learn new tasks with just a few examples instead of massive datasets",
        "We're optimizing our AI models to run faster and use less memory while maintaining accuracy",
        "We're implementing advanced search that understands meaning rather than just matching keywords"
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Style the table with hacker theme
def style_df(df):
    return df.style.set_properties(**{
        'white-space': 'wrap',
        'text-align': 'left',
        'padding': '12px',
        'border': '1px solid #00ff00',
        'color': '#ffffff',
        'background-color': '#000000'
    }).set_table_styles([
        {'selector': '',
         'props': [('background-color', '#000000')]},
        {'selector': 'th',
         'props': [('background-color', '#1a1a1a'),
                  ('color', '#00ff00'),
                  ('font-weight', 'bold'),
                  ('text-align', 'left'),
                  ('padding', '15px'),
                  ('border', '2px solid #00ff00'),
                  ('text-shadow', '0 0 5px #00ff00')]},
        {'selector': 'tr:nth-of-type(odd)',
         'props': [('background-color', '#0a0a0a')]},
        {'selector': 'tr:nth-of-type(even)',
         'props': [('background-color', '#000000')]},
        {'selector': 'tr:hover',
         'props': [('background-color', '#1a1a1a')]},
    ])

# Apply styling
styled_df = style_df(df)

# Save to HTML with additional CSS
html = styled_df.to_html(index=False)
with open('ai_translation_matrix.html', 'w', encoding='utf-8') as f:
    css = """
    <style>
    body {
        background-color: #000000;
        padding: 20px;
    }
    table {
        border-collapse: separate;
        border-spacing: 0;
        width: 100%;
        background-color: #000000;
        box-shadow: 0 0 20px rgba(0, 255, 0, 0.3);
        font-family: 'Courier New', monospace;
        border-radius: 10px;
        overflow: hidden;
        margin: 20px 0;
    }
    th {
        position: relative;
        overflow: hidden;
    }
    th::after {
        content: '';
        position: absolute;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 2px;
        background: linear-gradient(90deg, transparent, #00ff00, transparent);
        animation: scan-line 2s linear infinite;
    }
    td, th {
        transition: all 0.3s ease;
        border: 1px solid rgba(0, 255, 0, 0.2);
    }
    tr:hover {
        transform: scale(1.01);
        box-shadow: 0 0 15px rgba(0, 255, 0, 0.2);
    }
    tr:hover td {
        color: #00ff00;
        text-shadow: 0 0 5px rgba(0, 255, 0, 0.5);
    }
    @keyframes scan-line {
        0% { transform: translateX(-100%); }
        100% { transform: translateX(100%); }
    }
    .title {
        color: #00ff00;
        text-align: center;
        font-family: 'Courier New', monospace;
        text-shadow: 0 0 10px rgba(0, 255, 0, 0.5);
        margin-bottom: 20px;
        font-size: 24px;
    }
    </style>
    <div class="title">AI Technical Language Translation Matrix</div>
    """
    f.write(css + html)
