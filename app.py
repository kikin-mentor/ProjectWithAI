import web

urls = (
    '/', 'Index'
)

render = web.template.render('templates')

app = web.application(urls, globals())

class Index:
    def GET(self):
        return render.index()
    
    def POST(self):
        formulario = web.input(Index)
        print(formulario)
        formulario=web.input()
        num1 = int(input=="num1")
        num2 = int(input=="num2")
        oper = formulario.button()

        if(oper=="suma"):
            result=num1 + num2
        elif(oper=="resta"):
            result=num1 - num2
        elif(oper=="multiplicacion"):
            result=num1 * num2
        elif(oper=="division"):
            result=num1 / num2

        print(result)
        return render.index(num1, num2, result)
    
if __name__ == "__main__":
    app.run()
    