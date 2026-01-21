#!/usr/bin/env python3
"""
Gera uma word cloud com palavras-chave dos repositórios públicos do GitHub do usuário BettoEsteves.
Busca nome, descrição, tópicos e linguagem de cada repositório.
Salva a imagem em wordcloud/wordcloud.png no estilo do exemplo fornecido.
"""
import requests
import os
from wordcloud import WordCloud
import matplotlib.pyplot as plt

GITHUB_USER = "BettoEsteves"
API_URL = f"https://api.github.com/users/{GITHUB_USER}/repos?per_page=100"

# Buscar repositórios
resp = requests.get(API_URL)
repos = resp.json()

keywords = []
for repo in repos:
    # Nome e descrição
    if repo.get('name'): keywords.extend(repo['name'].split('-'))
    if repo.get('description'): keywords.extend(repo['description'].split())
    # Linguagem
    if repo.get('language'): keywords.append(repo['language'])
    # Tópicos (precisa de API extra, mas tentamos)
    topics_url = repo.get('topics_url') or f"https://api.github.com/repos/{GITHUB_USER}/{repo['name']}/topics"
    topics_resp = requests.get(topics_url, headers={"Accept": "application/vnd.github.mercy-preview+json"})
    if topics_resp.status_code == 200:
        topics = topics_resp.json().get('names', [])
        keywords.extend(topics)

# Palavras-chave extras para garantir destaque
keywords.extend([
    "AI", "GenAI", "LLM", "FASTAPI", "LangChain", "LangGraph", "CNN", "YOLO", "N8N", "Vibecoding", "AI Product Builder",
    "Python", "Machine Learning", "Deep Learning", "DevOps", "MLOps", "AIOps", "DevSecOps", "RAG", "Multiagentes"
])

# Limpar e normalizar
keywords = [k.strip().replace('_', ' ').replace('-', ' ') for k in keywords if k and len(k) > 1]
text = ' '.join(keywords)

# Gerar word cloud
os.makedirs('wordcloud', exist_ok=True)
wordcloud = WordCloud(
    width=1200,
    height=600,
    background_color='white',
    colormap='viridis',
    relative_scaling=0.5,
    min_font_size=10
).generate(text)

plt.figure(figsize=(16, 8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.tight_layout(pad=0)
plt.savefig('wordcloud/wordcloud.png', dpi=150, bbox_inches='tight')
print("✅ Word Cloud gerada com sucesso em: wordcloud/wordcloud.png")
