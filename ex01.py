while True:
    valor_brl = float(input("Digite o valor em reais (BRL): "))
    taxa_cambio = float(input("Digite a taxa de câmbio para USD: "))
    valor_usd = valor_brl * taxa_cambio
    print(f"Valor em dólares (USD): {valor_usd:.2f}")
    
    continuar = input("Deseja realizar outra conversão? (s/n): ")
    if continuar.lower() != 's':
        break