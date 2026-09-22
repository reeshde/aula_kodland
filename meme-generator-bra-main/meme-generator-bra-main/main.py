# Importação
from flask import Flask, render_template, request, send_from_directory


app = Flask(__name__)

# Resultados do formulário
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        # obtendo a imagem selecionada
        selected_image = request.form.get('image-selector')
        text_top = request.form.get("textTop")
        text_bottom = request.form.get("textBottom")
        text_top_y = request.form.get("textTop_y")
        text_bottom_y = request.form.get("textBottom_y")
        selected_color = request.form.get('color-selector')
        # Tarefa #2. Recebendo o texto
        

        # Tarefa #3. Recebendo o posicionamento do texto
       

        # Tarefa #3. Recebendo a cor do texto
        

        return render_template('index.html', 
                               # exibindo a imagem selecionada
                               selected_image=selected_image, 
                               text_top = text_top,
                               text_bottom = text_bottom,
                               selected_color = selected_color,
                               text_top_y = text_top_y,
                               text_bottom_y = text_bottom_y
                               # Tarefa #2. exibindo o texto
                               

                               # Tarefa #3. exibindo a cor 
                               
                               
                               # Tarefa #3. exibindo o posicionamento do texto

                               )
    else:
        # exibindo a primeira imagem por padrão
        return render_template('index.html', selected_image='logo.svg')


@app.route('/static/img/<path:path>')
def serve_images(path):
    return send_from_directory('static/img', path)

app.run(debug=True)