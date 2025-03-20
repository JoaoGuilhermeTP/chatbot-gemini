import os, google.generativeai as genai

# Armazenar me uma variável global o modelo utilizado
MODEL = genai.GenerativeModel("gemini-2.0-flash")
# Armazenar em uma variável global a chave da API, objtida de uma variável global
API_KEY = os.getenv('GEMINI_API_KEY')
# Quantidade de perguntas que o usuário poderá fazer
QTDE_PERGUNTAS = 3


def obter_resposta(pergunta, contexto, modelo):
    """Função que consulta a API do Google Gemini para responder perguntas sobre um contexto específico."""
    model = modelo
    resposta = model.generate_content(f"Você é um professor muito bem humorado e engraçado, especialista em {contexto}. Responda a seguinte pergunta de forma clara, concisa, didática e com senso de humor: {pergunta}")
    return resposta.text

def main():
    """Fluxo principal do chatbot."""
    genai.configure(api_key=API_KEY)  
    
    print("Bem-vindo ao Chatbot Inteligente!")
    contexto = input("Sobre qual área de negócio você deseja perguntar? ")
    print(f"Ótimo! Você pode fazer três perguntas sobre {contexto}.")
    
    # Listas para armazenar as perguntas e respostas
    perguntas = []
    respostas = []
    
    for i in range(QTDE_PERGUNTAS):
        pergunta = input(f"Pergunta {i+1}: ")
        perguntas.append(pergunta)
        resposta = obter_resposta(pergunta, contexto, MODEL)
        respostas.append(resposta)
        print(f"Resposta: {resposta}\n")
    
    # Gerando um resumo
    resumo = MODEL.generate_content("Resuma as seguintes perguntas e respostas de forma clara, objetiva e bem humorada:\n" + "\n".join([f"Pergunta: {p}\nResposta: {r}" for p, r in zip(perguntas, respostas)]))
    
    print("\nResumo final das respostas:")
    print(resumo.text)

if __name__ == "__main__":
    main()