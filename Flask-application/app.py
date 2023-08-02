from flask import Flask, render_template, request
import os
import openai
import time
# OpenAI API key
openai.api_key = os.getenv("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")
openai.api_key = "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"

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/main',methods=["POST","GET"])
def main_():
    query = request.form.get('query')
    if request.method == "POST":
        def get_completion(query, model="gpt-3.5-turbo"):
            messages=[
                {"role": "system", "content": f"""You are an Question and Answer bot who has to answer User query
                and understand the query in detail.If you are not sure about answer just say "Unsure about response".
                Avoid any further generation of text.Provide answer very short and precise."""},
                {"role": "user", "content": f"{query}"}
            ]

            response = openai.ChatCompletion.create(
                model=model,
                messages=messages,
                temperature=0,# this is the degree of randomness of the model's output
            )
            return response
        response = get_completion(query)
        return render_template("login.html",response=response, query = query)
        
    else:
        return render_template("main.html")

if __name__ == '__main__':
    app.run(debug=True)