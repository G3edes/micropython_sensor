from machine import Pin, time_pulse_us
import time

# --- Configuração dos Pinos ---
# Pinos do sensor ultrassônico HC-SR04
PINO_TRIG = 25
CONTADOR = 0
CAIXAS = 0
PINO_ECHO = 27

# Pino do LED vermelho
# Escolha um pino GPIO digital disponível, por exemplo, o 26.
# Verifique o diagrama de pinos do seu ESP32 no simulador ou datasheet.
PINO_LED_INTRUSO = 26

# Crie os objetos Pin com a configuração correta
trig = Pin(PINO_TRIG, Pin.OUT)
echo = Pin(PINO_ECHO, Pin.IN)
led_glass = Pin(PINO_LED_INTRUSO, Pin.OUT)

# --- Função de Medição de Distância (sem alterações) ---
def obter_distancia():
    """
    Mede a distância em centímetros usando o sensor HC-SR04.
    """
    trig.value(0)
    time.sleep_us(2)

    trig.value(1)
    time.sleep_us(10)
    trig.value(0)

    duracao = time_pulse_us(echo, 1, 10000)
    distancia = (duracao / 2) * 0.0343
    return distancia

# --- Loop Principal de Ação ---
while True:
    dist = obter_distancia()

    
    # --- Ação de Atuação: Controle do LED ---
    if dist <= 10:
        CONTADOR+=1
        print("FRASCO",CONTADOR)
        if CONTADOR % 10 == 0:
            CAIXAS+=1
            
        print("TOTAL DE CAIXAS:", CAIXAS) 
        
        
        
        led_glass.value(1)  # Acende o LED (sinal HIGH)
        time.sleep(1)
    else:
       
        print("Frasco Não Detectado")
        led_glass.value(0)  # Apaga o LED (sinal LOW)

    time.sleep(1)