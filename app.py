import requests
import os
import web

urls = (
    '/', 'Index'
)

render = web.template.render('templates/')
app = web.application(urls, globals())

class Index:
    def GET(self):
        return render.index("")

    def POST(self):
        print("Recibiendo los datos del formulario")

        formulario = web.input()
        print(formulario)

        prompt = formulario.prompt

        url = "https://api.groq.com/openai/v1/chat/completions"
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer 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"
        }
        data = {
            "model": "meta-llama/llama-4-scout-17b-16e-instruct",
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "temperature": 1,
            "max_completion_tokens": 1024,
            "top_p": 1,
            "stream": False,
            "stop": None
        }

        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        response_data = response.json()

        result = response_data['choices'][0]['message']['content']

        return render.index(result, prompt)

if __name__ == "__main__":
    app.run()

