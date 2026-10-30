from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from configuracao import TOKEN
from respostas import criar_resposta_para_texto

async def lidar_com_mensagem(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto_recebido = update.message.text
    print(f"Mensagem recebida do usuário: {texto_recebido}")
    
    # Pega a resposta do arquivo respostas.py
    resposta = criar_resposta_para_texto(texto_recebido)
    
    # Envia a resposta de volta no Telegram
    await update.message.reply_text(resposta)

def main():
    print("🤖 Ligando o robô do Telegram...")
    
    # Constrói a aplicação com o token
    app = ApplicationBuilder().token(TOKEN).build()
    
    # Adiciona o ouvinte para qualquer mensagem de texto
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), lidar_com_mensagem))
    
    print("✅ Robô pronto e conectado com sucesso!")
    print("👉 Abra o seu aplicativo do Telegram e converse com o seu robô.")
    
    # Inicia o robô
    app.run_polling()

if __name__ == "__main__":
    main()
