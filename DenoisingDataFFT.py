import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk

def gerar_sinal():
    try:
        freq1 = float(entry_freq1.get())
        freq2 = float(entry_freq2.get())
    except ValueError:
        print("Por favor, insira valores numéricos.")
        return

    dt = 0.001
    t = np.arange(0, 1, dt)
    f_clean = np.sin(2 * np.pi * freq1 * t) + np.sin(2 * np.pi * freq2 * t)
    f_noisy = f_clean + 2.5 * np.random.randn(len(t))

    n = len(t)
    fhat = np.fft.fft(f_noisy, n)
    PSD = fhat * np.conj(fhat) / n
    freq = (1 / (dt * n)) * np.arange(n)
    L = np.arange(1, int(np.floor(n / 2)))

    indices = PSD > 100
    PSDclean = PSD * indices
    fhat = indices * fhat
    ffilt = np.fft.ifft(fhat)

    # Plotagem dos gráficos
    fig = plt.figure(figsize=(16, 10))
    fig.canvas.manager.set_window_title('Remoção de ruídos FFT')

    plt.subplot(2, 2, 1)
    plt.plot(t, f_clean, color='k', label='Clean')
    plt.title("Sinal Original")
    plt.legend()

    plt.subplot(2, 2, 2)
    plt.plot(t, f_noisy, color='r', label='Noisy')
    plt.plot(t, f_clean, color='k', label='Clean')
    plt.title("Sinal com Ruído")
    plt.legend()

    plt.subplot(2, 2, 3)
    plt.plot(freq[L], PSD[L], color='c', label='Noisy')
    plt.plot(freq[L], PSDclean[L], color='k', label='Filtered')
    plt.title("Espectro de Frequências (PSD)")
    plt.legend()

    plt.subplot(2, 2, 4)
    plt.plot(t, ffilt, color='k', label='Filtrado')
    plt.title("Sinal Após Filtragem")
    plt.legend()

    plt.tight_layout()
    plt.show()


# Interface Gráfica
window = tk.Tk()
window.title("Remoção de Ruídos com FFT - Configurações")
window.geometry("600x200")

# Widgets

ttk.Label(window, text="Frequência 1 (Hz):").grid(row=0, column=0, padx=100, pady=20, sticky="e")
entry_freq1 = ttk.Entry(window)
entry_freq1.insert(0, "")
entry_freq1.grid(row=0, column=1)

ttk.Label(window, text="Frequência 2 (Hz):").grid(row=1, column=0, padx=100, pady=10)
entry_freq2 = ttk.Entry(window)
entry_freq2.insert(0, "")
entry_freq2.grid(row=1, column=1)
'''
ttk.Label(window, text="Nível de Ruído:").grid(row=2, column=0, padx=100, pady=20, sticky="e")
entry_ruido = ttk.Entry(window)
entry_ruido.insert(0, "")
entry_ruido.grid(row=2, column=1)
'''
ttk.Button(window, text="Gerar e Limpar Sinal", command=gerar_sinal).grid(row=3, column=1, columnspan=2, padx=0, pady=20)
window.mainloop()