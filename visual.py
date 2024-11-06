import pandas as pd
from groq import Groq
import os
from datetime import datetime

def generate_ai_translations(num_entries=5):
    client = Groq(
        api_key=os.environ.get("GROQ_API_KEY")
    )
    
    prompt = """Generate a list of {num_entries} pairs of technical AI terms and their simplified explanations. 
    Each pair should include a complex technical AI term or phrase and its clear, simple explanation for non-technical stakeholders.
    
    Format each pair as:
    Technical: [complex AI term or phrase]
    Simple: [clear, simple explanation]
    
    Make sure each term is:
    1. A real AI/ML concept or technology
    2. Something commonly used in technical discussions
    3. Explained in plain language without jargon
    4. Different from previous entries
    """

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt.format(num_entries=num_entries),
            }
        ],
        model="llama3-8b-8192",  # Updated to use the latest Llama 3 model
        stream=False,
    )

    # Parse response
    content = chat_completion.choices[0].message.content
    lines = content.split('\n')
    
    technical_terms = []
    simple_explanations = []
    
    current_term = None
    for line in lines:
        if line.strip():
            if line.startswith('Technical:'):
                current_term = line.replace('Technical:', '').strip()
            elif line.startswith('Simple:') and current_term:
                explanation = line.replace('Simple:', '').strip()
                technical_terms.append(current_term)
                simple_explanations.append(explanation)
                current_term = None

    # Create DataFrame
    data = {
        'Instead of Saying...': technical_terms,
        'Say...': simple_explanations
    }
    
    return pd.DataFrame(data)

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
styled_df = style_df(generate_ai_translations())

# Save to HTML with additional CSS
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
filename = f'ai_translation_matrix_{timestamp}.html'

html = styled_df.to_html(index=False)
with open(filename, 'w', encoding='utf-8') as f:
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

print(f"File saved as: {filename}")
