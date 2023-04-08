from flask import Flask, render_template, request
import chess
import chess.svg

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    board = chess.Board()
    if request.method == 'POST':
        # print(request.form)
        move = request.form['moves']
        try:
            board.push_san(move)
        except ValueError as ve:
            print(ve)
            pass
    svg = chess.svg.board(board=board)
    return render_template('index.html', svg=svg)

if __name__ == '__main__':
    app.run(host='0.0.0.0')