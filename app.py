import streamlit as st
import openai
import os
import json
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="StreamBoost AI", page_icon="🎮")
st.title("🚀 StreamBoost AI")
st.markdown("Generá títulos, descripciones y tags virales para tus streams de Twitch o Kick en segundos.")

with st.expander("¿Cómo funciona esta app?"):
    st.write("""
    1. **Completá los datos:** Decime qué vas a jugar (ej. Valorant, FC 26, charlando) y qué onda va a tener el stream (tryhard, chill, etc.).
    2. **Generar:** Tocá el botón y la IA (usando GPT) procesa la info.
    3. **Resultado:** Te devuelve un título gancho, un texto para tu historia/tweet y los mejores tags, listo para copiar y pegar.
    """)

st.divider()

col1, col2 = st.columns(2)
with col1:
    juego = st.text_input("¿Qué vas a jugar/hacer hoy?", placeholder="Ej: Valorant, FC 26, Just Chatting...")
with col2:
    vibra = st.selectbox("¿Qué onda tiene el stream?", ["Competitivo / Tryhard", "Chill / Relajado", "Humor / Risas", "Enseñando / Tutorial"])

if st.button("🔥 Generar contenido para el stream"):
    if not juego:
        st.warning("Che, ponele a qué vas a jugar así la IA tiene contexto.")
    else:
        with st.spinner("Armando el contenido..."):
            try:

                prompt_sistema = """
                Sos un asistente experto en marketing para streamers de Twitch y Kick.
                Tu objetivo es ayudar al usuario a promocionar su directo de hoy.
                
                IMPORTANTE: Tu respuesta debe ser ÚNICAMENTE un JSON válido. Cero texto extra antes o después.
                El formato JSON debe ser exactamente este:
                {
                    "titulo": "un título muy llamativo para el stream (max 60 caracteres)",
                    "post_redes": "un texto corto y con emojis para avisar en Twitter/Instagram que prendió directo",
                    "tags": ["tag1", "tag2", "tag3", "tag4", "tag5"]
                }
                """
                
                prompt_usuario = f"Voy a streamear {juego} y la onda del directo va a ser {vibra}. Armame el contenido."

                respuesta = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": prompt_sistema},
                        {"role": "user", "content": prompt_usuario}
                    ],
                    temperature=0.7
                )

                resultado_texto = respuesta.choices[0].message.content
                resultado_json = json.loads(resultado_texto)

                st.success("¡Listo! Acá tenés el contenido:")
                
                st.subheader("📌 Título para el Stream")
                st.code(resultado_json["titulo"], language="text")
                
                st.subheader("📱 Post para Redes")
                st.info(resultado_json["post_redes"])
                
                st.subheader("🏷️ Tags")
                st.write(" ".join([f"#{tag}" for tag in resultado_json["tags"]]))

            except json.JSONDecodeError:
                st.error("Error: La IA no devolvió el formato JSON correctamente. Intentá de nuevo.")
            except Exception as e:
                # aca atajamos el error de falta de saldo (el famoso "You have no credits remaining")
                st.error(f"Hubo un error con la API de OpenAI (probablemente falta de saldo): {e}")