from flask import Flask, jsonify, request, abort

from escpos import printer

app = Flask(__name__)

dummy_list = [
    {
        'id': 1,
        'description': 'Buy bin bags',
        'done': True
    },
    {
        'id': 2,
        'description': 'Buy toilet paper',
        'done': False
    }
]

@app.route('/printbot/list/all', methods=['GET'])
def get_all_items():
    return jsonify({'list': dummy_list})


@app.route('/printbot/list/todo', methods=['GET'])
def get_incomplete_items():
    return jsonify({'list': [i for i in dummy_list if i['done'] == False]})


@app.route('/printbot/list/add', methods=['POST'])
def add_to_list():
    if not request.json or not 'description' in request.json:
        abort(400)
    item = {
        'id': dummy_list[-1]['id'] + 1,
        'description': request.json['description'],
        'done': False
    }
    dummy_list.append(item)
    return jsonify({'list': dummy_list}), 201


@app.route('/printbot/list/toggle_done', methods=['POST'])
def toggle_item():
    if not request.json or not 'id' in request.json:
        abort(400)
    
    for item in dummy_list:
        if item['id'] == request.json['id']:
            if item['done']:
                item['done'] = False
            else:
                item['done'] = True
            
    return jsonify({'list': dummy_list}), 201


@app.route('/printbot/list/print', methods=['POST'])
def print_list():
    printstring = ''
    for item in dummy_list:
        if not item['done']:
            printstring += '{}\n'.format(item['description'], item['done'])

    printbot = printer.Usb(0x0416, 0x5011)
    printbot.text(printstring if printstring else "I'm sorry human, there's nothing in the list")
    printbot.cut()

    return printstring if printstring else "List empty"


@app.route('/printbot/print', methods=['POST'])
def print_custom():
    if not request.json or not 'message' in request.json:
        abort(400, 'Shit - no message in the request payload: {}'.format(request.json))

    message = request.json['message']

    printbot = printer.Usb(0x0416, 0x5011)
    printbot.text(message if message else "I'm sorry human. I cannot understand that message.")
    printbot.cut()

    return message


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

