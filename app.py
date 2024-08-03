from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/scrape', methods=['GET'])
def scrape():
    try:
        url = 'https://zelenkevich-swimming.ru/'  # URL сайта для скрапинга
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        response.raise_for_status()  # Проверка наличия ошибок HTTP

        soup = BeautifulSoup(response.text, 'html.parser')

        # Извлечение всех блоков
        blocks = []
        for element in soup.find_all(True):  # True находит все теги
            blocks.append({
                'tag': element.name,
                'attributes': dict(element.attrs),
                'content': element.decode_contents()
            })

        return jsonify({'status': 'success', 'blocks': blocks})
    except requests.exceptions.RequestException as e:
        # Обработка ошибок запроса HTTP
        return jsonify({'error': 'HTTP error', 'details': str(e)}), 500
    except Exception as e:
        # Обработка других ошибок
        return jsonify({'error': 'Internal server error', 'details': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
