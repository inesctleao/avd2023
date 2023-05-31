import matplotlib.pyplot as plt

pontuacoes = [
    {'neg': 0.016, 'neu': 0.972, 'pos': 0.012, 'compound': -0.5897},
    {'neg': 0.016, 'neu': 0.97, 'pos': 0.013, 'compound': -0.4035},
    {'neg': 0.02, 'neu': 0.98, 'pos': 0.0, 'compound': -0.9157},
    {'neg': 0.02, 'neu': 0.957, 'pos': 0.023, 'compound': 0.8377},
    {'neg': 0.018, 'neu': 0.972, 'pos': 0.01, 'compound': -0.86},
    {'neg': 0.017, 'neu': 0.972, 'pos': 0.011, 'compound': -0.7067},
    {'neg': 0.023, 'neu': 0.961, 'pos': 0.016, 'compound': -0.8035},
    {'neg': 0.006, 'neu': 0.987, 'pos': 0.007, 'compound': 0.7374},
    {'neg': 0.015, 'neu': 0.976, 'pos': 0.009, 'compound': -0.6935},
    {'neg': 0.014, 'neu': 0.973, 'pos': 0.012, 'compound': 0.814},
    {'neg': 0.015, 'neu': 0.972, 'pos': 0.013, 'compound': 0.8492},
    {'neg': 0.038, 'neu': 0.957, 'pos': 0.005, 'compound': -0.9686},
    {'neg': 0.012, 'neu': 0.984, 'pos': 0.004, 'compound': -0.9453},
    {'neg': 0.014, 'neu': 0.982, 'pos': 0.004, 'compound': -0.9547},
    {'neg': 0.022, 'neu': 0.971, 'pos': 0.006, 'compound': -0.9839},
    {'neg': 0.027, 'neu': 0.965, 'pos': 0.009, 'compound': -0.9796},
    {'neg': 0.017, 'neu': 0.98, 'pos': 0.004, 'compound': -0.9706},
    {'neg': 0.025, 'neu': 0.975, 'pos': 0.0, 'compound': -0.982},
    {'neg': 0.011, 'neu': 0.972, 'pos': 0.017, 'compound': 0.9533},
    {'neg': 0.022, 'neu': 0.971, 'pos': 0.006, 'compound': -0.972},
    {'neg': 0.02, 'neu': 0.972, 'pos': 0.008, 'compound': -0.78},
    {'neg': 0.022, 'neu': 0.972, 'pos': 0.006, 'compound': -0.954},
    {'neg': 0.012, 'neu': 0.971, 'pos': 0.017, 'compound': 0.9655}
]

valores_compound = [sentimento['compound'] for sentimento in pontuacoes]

rotulos = [f"Capítulo {i+1}" for i in range(len(pontuacoes))]

plt.figure(figsize=(10, 6))
plt.bar(rotulos, valores_compound)
plt.xlabel('Capítulo')
plt.ylabel('Sentimento (compound)')
plt.title('Análise de Sentimento por Capítulo')
plt.xticks(rotation=45)
plt.show()
