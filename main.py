import pyautogui
import time

pyautogui.PAUSE = 0.5
pyautogui.FAILSAFE = True

def esperar(img, timeout=15, conf=0.9):
    inicio = time.time()
    while time.time() - inicio < timeout:
        pos = pyautogui.locateCenterOnScreen(img, confidence=conf)
        if pos:
            return pos
        time.sleep(0.4)
    raise Exception(f"Não achei {img}")

def procurar_com_scroll(img, timeout=20, conf=0.8, scroll_step=-300):
    inicio = time.time()
    while time.time() - inicio < timeout:
        pos = pyautogui.locateCenterOnScreen(img, confidence=conf)
        if pos:
            return pos
        pyautogui.scroll(scroll_step)
        time.sleep(0.6)
    raise Exception(f"Não achei {img} mesmo com scroll")

def clicar_campo_por_label(img_label, dx, dy):
    pos = esperar(img_label)
    pyautogui.click(pos.x + dx, pos.y + dy)

def clicar(img):
    pos = esperar(img)
    pyautogui.click(pos)

meses = [
    ("01", "2025", "imgs/jan_2025.png"),
    ("02", "2025", "imgs/fev_2025.png"),
    ("03", "2025", "imgs/mar_2025.png"),
    ("04", "2025", "imgs/abr_2025.png"),
    ("05", "2025", "imgs/mai_2025.png"),
    ("06", "2025", "imgs/jun_2025.png"),
    ("07", "2025", "imgs/jul_2025.png"),
    ("08", "2025", "imgs/ago_2025.png"),
    ("09", "2025", "imgs/set_2025.png"),
    ("10", "2025", "imgs/out_2025.png"),
    ("11", "2025", "imgs/nov_2025.png"),
    ("12", "2025", "imgs/dez_2025.png")
]

conta = input("Conta: ")
tipo = int(input("TIPO (1-EXTRATO/2-INVESTIMENTO): "))

print("Começando em 5s...")
time.sleep(5)

for mes, ano, img_mes in meses:
    print(f"\nProcessando {tipo} - {ano}/{mes}...")

    if tipo == 1:
        nome = f"Conta {conta} - EXTRATO - {ano}-{mes}.pdf"
        clicar(img_mes)          # seleciona mês
        time.sleep(2)            # BB carrega extrato

    if tipo == 2:
        nome = f"Conta {conta} - INVESTIMENTO - {ano}-{mes}.pdf"
        inv_ext = mes + ano
        clicar_campo_por_label("imgs/mes_ano_label_invest.png", 120, 0)
        pyautogui.write(inv_ext, interval=0.12)
        time.sleep(1)
        clicar("imgs/ok.png")
        time.sleep(1)
        pyautogui.hotkey("ctrl", "home")
        time.sleep(1)

    clicar("imgs/imprimir.png")
    clicar("imgs/salvar_pdf.png")
    clicar("imgs/nome_campo.png")

    pyautogui.hotkey("ctrl", "a")
    pyautogui.write(nome)

    clicar("imgs/salvar.png")
    
    print(f'"{nome}" salvo com sucesso!')

    if tipo == 2:
        pyautogui.hotkey("ctrl", "end")
        time.sleep(1)
        pos = procurar_com_scroll("imgs/nova.png")
        pyautogui.click(pos)

    time.sleep(2)  # evita stress no site
