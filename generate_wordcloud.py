#!/usr/bin/env python3
"""
Script para gerar Word Cloud das tecnologias e projetos do portfólio
"""

import os
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Palavras-chave dos projetos e tecnologias
keywords = """
Python LLM RAG Machine Learning Deep Learning DevOps CI CD
Kubernetes Docker AWS Azure Terraform Infrastructure Code
AI Artificial Intelligence Multiagentes Agents LangChain LangGraph
FastAPI PostgreSQL Redis MongoDB Data Science
Scikit-learn Pandas NumPy PyTorch TensorFlow Transformers
Prometheus Grafana Monitoring Observability
MLOps AIOps DevSecOps Security Automation
CNN YOLO Computer Vision Natural Language Processing
N8N Workflow Automation Vibecoding AI Product Builder
GitHub Actions Testing Deployment Scalability
Insights Estratégicos Find People HELPME
Innovation Technology Solutions Cloud Computing
Blockchain Smart Contracts Web Development
Analytics Intelligence Transformation Strategy
Excellence Performance Optimization Best Practices
Open Source Collaboration Community Driven
Future Ready Cutting Edge Modern Architecture
"""

# Gerar word cloud
wordcloud = WordCloud(
    width=1200,
    height=600,
    background_color='white',
    colormap='viridis',
    relative_scaling=0.5,
    min_font_size=10
).generate(keywords)

# Configurar figura
plt.figure(figsize=(16, 8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.tight_layout(pad=0)

# Salvar a imagem
output_path = 'wordcloud/wordcloud.png'
os.makedirs('wordcloud', exist_ok=True)
plt.savefig(output_path, dpi=150, bbox_inches='tight')
print(f"✅ Word Cloud gerada com sucesso em: {output_path}")

# Contar palavras únicas
word_count = len(keywords.split())
print(f"📊 Total de palavras-chave: {word_count}")

plt.close()
