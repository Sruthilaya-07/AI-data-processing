import ollama

res = ollama.chat(
    model='llava',
    messages=[
        {
            'role': 'user',
            'content': 'Describe this  image',
             'images': [r"C:\Users\sruth\OneDrive\Desktop\tower2.jpeg" ]
        }
    ]
)
description = res.get('message', {}).get('content', 'No content found')
print(description)
