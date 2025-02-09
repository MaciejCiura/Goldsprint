# web.py
from flask import Flask, request, jsonify
import threading
from core import race_controller  # przykładowy moduł sterujący aplikacją

app = Flask(__name__)

@app.route('/start_race', methods=['POST'])
def start_race():
    # Wywołanie funkcji z modułu core, która np. uruchamia wyścig
    result = controller.start_race()  # zakładamy, że taka funkcja istnieje
    return jsonify({'status': 'ok', 'result': result})

@app.route('/status', methods=['GET'])
def status():
    # Pobranie aktualnego stanu aplikacji
    current_status = controller.get_status()  # przykładowa funkcja zwracająca stan
    return jsonify(current_status)

def run_web_server():
    # Uruchamiamy serwer na porcie 5000, dostępny dla wszystkich interfejsów sieciowych
    app.run(host='0.0.0.0', port=5000)

if __name__ == '__main__':
    # Uruchomienie serwera web w osobnym wątku
    server_thread = threading.Thread(target=run_web_server)
    server_thread.daemon = True  # dzięki temu wątek zakończy się przy zamknięciu głównego programu
    server_thread.start()

    # Uruchomienie głównej logiki aplikacji
    controller.main_loop()  # lub inna funkcja, która odpowiada za działanie aplikacji
