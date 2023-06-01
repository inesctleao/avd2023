import matplotlib.pyplot as plt

pontuacoes = [
    {'neg': 0.02, 'neu': 0.962, 'pos': 0.018, 'compound': 0.695},
    {'neg': 0.017, 'neu': 0.973, 'pos': 0.01, 'compound': -0.8758},
    {'neg': 0.011, 'neu': 0.986, 'pos': 0.003, 'compound': -0.9007},
    {'neg': 0.016, 'neu': 0.976, 'pos': 0.008, 'compound': -0.8238},
    {'neg': 0.011, 'neu': 0.976, 'pos': 0.013, 'compound': 0.8698},
    {'neg': 0.004, 'neu': 0.98, 'pos': 0.015, 'compound': 0.9841},
    {'neg': 0.018, 'neu': 0.962, 'pos': 0.02, 'compound': 0.9444},
    {'neg': 0.021, 'neu': 0.946, 'pos': 0.033, 'compound': 0.9869},
    {'neg': 0.007, 'neu': 0.97, 'pos': 0.023, 'compound': 0.9972},
    {'neg': 0.009, 'neu': 0.977, 'pos': 0.014, 'compound': 0.7121},
    {'neg': 0.013, 'neu': 0.951, 'pos': 0.036, 'compound': 0.9954},
    {'neg': 0.016, 'neu': 0.974, 'pos': 0.01, 'compound': -0.7527},
    {'neg': 0.012, 'neu': 0.973, 'pos': 0.015, 'compound': 0.9488},
    {'neg': 0.011, 'neu': 0.965, 'pos': 0.023, 'compound': 0.9764},
    {'neg': 0.022, 'neu': 0.958, 'pos': 0.02, 'compound': 0.8453},
    {'neg': 0.019, 'neu': 0.972, 'pos': 0.009, 'compound': -0.9174},
    {'neg': 0.021, 'neu': 0.966, 'pos': 0.013, 'compound': -0.7374},
    {'neg': 0.018, 'neu': 0.974, 'pos': 0.009, 'compound': -0.9123},
    {'neg': 0.015, 'neu': 0.977, 'pos': 0.008, 'compound': -0.8372},
    {'neg': 0.015, 'neu': 0.979, 'pos': 0.006, 'compound': -0.9554},
    {'neg': 0.009, 'neu': 0.972, 'pos': 0.019, 'compound': 0.9667},
    {'neg': 0.021, 'neu': 0.966, 'pos': 0.013, 'compound': -0.814},
    {'neg': 0.016, 'neu': 0.976, 'pos': 0.008, 'compound': -0.9291},
    {'neg': 0.013, 'neu': 0.964, 'pos': 0.023, 'compound': 0.9264},
    {'neg': 0.014, 'neu': 0.968, 'pos': 0.019, 'compound': 0.9608},
    {'neg': 0.014, 'neu': 0.974, 'pos': 0.012, 'compound': 0.7736},
    {'neg': 0.025, 'neu': 0.963, 'pos': 0.012, 'compound': -0.9067},
    {'neg': 0.005, 'neu': 0.971, 'pos': 0.024, 'compound': 0.989},
    {'neg': 0.018, 'neu': 0.969, 'pos': 0.013, 'compound': -0.5897},
    {'neg': 0.019, 'neu': 0.972, 'pos': 0.009, 'compound': -0.9839}
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
