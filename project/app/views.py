from django.shortcuts import render
import openai

# Create your views here.

"""
OPEN.AI
"""
# models
EMBEDDING_MODEL = "text-embedding-ada-002"
GPT_MODEL = "gpt-3.5-turbo"

openai.api_key = "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"

def api_openai(request):

    current = "En no más de 2 parrafos;" +  request.POST['q1']
    
    response = openai.ChatCompletion.create(
        messages=[
            {'role': 'system', 'content': 'You answer questions'},
            {'role': 'user', 'content': current},
        ],
        model=GPT_MODEL,
        temperature=0,
    )

    return render(request, 'story.html', {'result': response['choices'][0]['message']['content']})

def home(request):
    return render(request, 'home.html')