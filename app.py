import streamlit as st
from datetime import datetime, timedelta
import time
import random
import base64
import os

def main():
    st.set_page_config(
        page_title="nosso contador",
        page_icon="💕",
        layout="wide"
    )
    
    # CSS personalizado com fundo mais claro e romântico
    st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    .counter-header {
        text-align: center;
        color: #ff6b95;
        font-family: 'Georgia', serif;
        margin-bottom: 30px;
        text-shadow: 0px 0px 10px rgba(255, 107, 149, 0.5);
    }
    .counter-card {
        background: rgba(255, 255, 255, 0.60);
        padding: 30px;
        border-radius: 20px;
        margin: 20px 0;
        box-shadow: 0 8px 25px rgba(255, 107, 149, 0.3);
        text-align: center;
    }
    .big-number {
        font-size: 48px;
        font-weight: bold;
        color: #ff6b95;
        margin: 10px 0;
    }
    .love-message {
        background: linear-gradient(135deg, #ff6b95 0%, #ff8e8e 100%);
        padding: 20px;
        border-radius: 15px;
        margin: 20px 0;
        text-align: center;
        color: white;
        font-style: italic;
    }
    .memory-box {
        background: linear-gradient(135deg, #ff6b95 0%, #ff8e8e 100%);
        width: 100px;
        height: 100px;
        border-radius: 15px;
        margin: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    .memory-box:hover {
        transform: scale(1.05);
        box-shadow: 0 8px 25px rgba(255, 107, 149, 0.5);
    }
    .memory-emoji {
        font-size: 36px;
    }
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    .css-18e3th9 {
        padding-top: 0;
    }
    .css-1d391kg {
        padding-top: 3.5rem;
    }
    h1, h2, h3, p, label {
        color: white !important;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 2px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: rgba(255, 107, 149, 0.2);
        border-radius: 4px 4px 0 0;
        color: white;
        padding: 10px 20px;
    }
    .stTabs [aria-selected="true"] {
        background-color: rgba(255, 107, 149, 0.8) !important;
    }
    .memory-card {
        background: rgba(255, 255, 255, 0.60);
        padding: 20px;
        border-radius: 15px;
        margin: 10px 0;
        box-shadow: 0 4px 15px rgba(255, 107, 149, 0.3);
        border: 2px solid rgba(255, 107, 149, 0.3);
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<h1 class="counter-header">💕 nosso contador, alright!! 💕</h1>', unsafe_allow_html=True)
    
    # Data que se conheceram
    data_conheceram = datetime(2025, 5, 9)  # 9 de maio de 2025
    
    # Data de início do relacionamento
    inicio_relacionamento = datetime(2025, 5, 16)  # 16 de maio de 2025
    
    # Calcular tempo juntos
    agora = datetime.now()
    tempo_juntos = agora - inicio_relacionamento
    dias_desde_conheceram = (agora - data_conheceram).days
    
    st.markdown(f"""
    <div style="text-align: center; background: linear-gradient(135deg, #ff6b95 0%, #ff8e8e 100%); 
                padding: 20px; border-radius: 15px; margin: 20px 0; color: white;">
        <h3>✨ Nossa História Começou em 9 de Maio ✨</h3>
        <p style="font-size: 18px;">Há <strong>{dias_desde_conheceram} dias</strong> nossos caminhos se cruzaram</p>
        <p style="font-size: 16px;">E há <strong>{tempo_juntos.days} dias</strong> decidimos caminhar juntos! 💕</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Extrair componentes
    anos = tempo_juntos.days // 365
    meses = (tempo_juntos.days % 365) // 30
    dias = tempo_juntos.days
    horas = tempo_juntos.total_seconds() // 3600
    minutos = tempo_juntos.total_seconds() // 60
    segundos = tempo_juntos.total_seconds()
    
    # Layout em colunas
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
        <div class="counter-card">
            <h3 style="color: #333 !important;">📅 Dias Juntos</h3>
            <div class="big-number">{dias}</div>
            <p style="color: #333 !important;">Dias de puro amor!</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="counter-card">
            <h3 style="color: #333 !important;">⏰ Horas Juntos</h3>
            <div class="big-number">{int(horas):,}</div>
            <p style="color: #333 !important;">Horas de felicidade!</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="counter-card">
            <h3 style="color: #333 !important;">📆 Meses de Amor</h3>
            <div class="big-number">{meses}</div>
            <p style="color: #333 !important;">Meses inesquecíveis!</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="counter-card">
            <h3 style="color: #333 !important;">⚡ Minutos Juntos</h3>
            <div class="big-number">{int(minutos):,}</div>
            <p style="color: #333 !important;">Minutos preciosos!</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Mensagens especiais baseadas no tempo
    mensagens_especiais = [
        "9 de maio: o dia que o destino nos apresentou! 💫",
        "16 de maio: o dia que decidimos ser felizes juntos! 💕",
        "Cada segundo ao seu lado é um presente! 💝",
        "Nosso amor cresce desde aquele 16 de maio! 🌱💕",
        "Você é a razão do meu sorriso diário! 😊❤️",
        "Desde maio, minha vida tem mais cor! 🌈💖",
        "Cada momento com você é mágico! ✨💕",
        "Nosso amor nasceu em maio e floresce a cada dia! 🌸💫"
    ]
    
    # Selecionar mensagem baseada no dia
    mensagem_do_dia = mensagens_especiais[dias % len(mensagens_especiais)]
    
    st.markdown(f"""
    <div class="love-message">
        <h3 style="color: white !important;">💌 Mensagem Especial de Hoje</h3>
        <p style="font-size: 18px; color: white !important;">{mensagem_do_dia}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Quadradinhos de memórias espalhados pela tela
    st.markdown("### 💖 Nossas Memórias Especiais")
    st.markdown("Clique nos quadradinhos para revelar memórias especiais!")
    
    # Verificar se precisa reinicializar as memórias (compatibilidade)
    if 'memorias' not in st.session_state or 'tipo' not in st.session_state.memorias.get('memoria1', {}):
        st.session_state.memorias = {
            'memoria1': {
                'revelada': False,
                'mensagem': 'primeira vez em que eu te vi!!! 💫',
                'emoji': '😍',
                'tipo': 'video',
                'arquivo': 'media/video.mp4'
            },
            'memoria2': {
                'revelada': False,
                'mensagem': 'lembra do nosso primeiro beijo? 💋',
                'emoji': '💋',
                'tipo': 'foto',
                'arquivo': 'media/foto2.jpeg'
            },
            'memoria3': {
                'revelada': False,
                'mensagem': 'primeiro role ref junto 💯',
                'emoji': '💯',
                'tipo': 'foto',
                'arquivo': 'media/foto3.jpeg'
            },
            'memoria4': {
                'revelada': False,
                'mensagem': 'primeira sonequinha juntos na minha casa 🏠',
                'emoji': '🏠',
                'tipo': 'foto',
                'arquivo': 'media/foto4.jpeg'
            },
            'memoria5': {
                'revelada': False,
                'mensagem': 'nosso primeiro jantar rsrs (hoje!)🌹',
                'emoji': '🌹',
                'tipo': 'vazio',
                'arquivo': None
            },
            'memoria6': {
                'revelada': False,
                'mensagem': 'THESE BITCHES LOVE SOSA!!!!',
                'emoji': '✏️',
                'tipo': 'foto',
                'arquivo': 'media/foto6.jpeg'
            }
        }
    
    # Criar grid de quadradinhos (2 linhas x 3 colunas = 6 memórias)
    num_rows = 2
    num_cols = 3
    
    for row in range(num_rows):
        cols = st.columns(num_cols)
        for col in range(num_cols):
            memoria_id = f'memoria{row * num_cols + col + 1}'
            memoria = st.session_state.memorias[memoria_id]
            
            with cols[col]:
                # Quadradinho clicável
                if not memoria['revelada']:
                    if st.button(f"{memoria['emoji']}", key=f"btn_{memoria_id}", 
                                help="Clique para revelar uma memória especial!",
                                use_container_width=True):
                        st.session_state.memorias[memoria_id]['revelada'] = True
                        st.rerun()
                else:
                    # Exibir memória revelada
                    st.markdown(f"""
                    <div class="memory-card">
                        <h4 style="color: #333 !important; text-align: center;">{memoria['emoji']} Memória Especial</h4>
                        <p style="color: #333 !important; text-align: center; font-style: italic;">{memoria['mensagem']}</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Exibir mídia baseada no tipo
                    if memoria.get('tipo') == 'video' and memoria.get('arquivo'):
                        try:
                            st.video(memoria['arquivo'])
                        except Exception as e:
                            st.error(f"Erro ao carregar vídeo: {e}")
                            st.info("Certifique-se de que o arquivo video.mp4 está na pasta media/")
                    elif memoria.get('tipo') == 'foto' and memoria.get('arquivo'):
                        try:
                            st.image(memoria['arquivo'], caption="Nossa foto especial ❤️", use_column_width=True)
                        except Exception as e:
                            st.error(f"Erro ao carregar foto: {e}")
                            st.info("Certifique-se de que a foto está na pasta media/")
                    elif memoria.get('tipo') == 'vazio':
                        st.info("📷 Foto será adicionada em breve...")
                        # Opção para upload manual
                        uploaded_file = st.file_uploader("Ou adicione uma foto agora:", 
                                                       type=["jpg", "jpeg", "png"], 
                                                       key=f"upload_{memoria_id}")
                        if uploaded_file is not None:
                            st.image(uploaded_file, caption="Nossa foto especial ❤️", use_column_width=True)
                    
                    # Campo editável para a mensagem
                    nova_mensagem = st.text_area("Editar mensagem:", 
                                               value=memoria['mensagem'], 
                                               key=f"msg_{memoria_id}",
                                               height=80)
                    st.session_state.memorias[memoria_id]['mensagem'] = nova_mensagem
                    
                    # Botão para esconder a memória
                    if st.button("Esconder", key=f"hide_{memoria_id}"):
                        st.session_state.memorias[memoria_id]['revelada'] = False
                        st.rerun()
    
    st.markdown("---")
    
    # Marcos futuros
    st.markdown("### 🎯 Próximos Marcos Especiais")
    
    # Calcular próximos marcos
    proximo_mes = inicio_relacionamento + timedelta(days=(meses + 1) * 30)
    proximo_ano = inicio_relacionamento + timedelta(days=(anos + 1) * 365)
    mil_dias = inicio_relacionamento + timedelta(days=1000)
    
    marcos = []
    if proximo_mes > agora:
        dias_para_mes = (proximo_mes - agora).days
        marcos.append(f"🗓️ Próximo mês de relacionamento: em {dias_para_mes} dias")
    
    if proximo_ano > agora:
        dias_para_ano = (proximo_ano - agora).days
        marcos.append(f"🎂 Próximo ano juntos: em {dias_para_ano} dias")
    
    if mil_dias > agora:
        dias_para_mil = (mil_dias - agora).days
        marcos.append(f"🎉 1000 dias juntos: em {dias_para_mil} dias")
    
    for marco in marcos:
        st.info(marco)
    
    # Contador em tempo real
    if st.checkbox("⏱️ Contador em Tempo Real"):
        placeholder = st.empty()
        
        for i in range(10):  # Atualiza por 10 segundos
            agora_real = datetime.now()
            segundos_reais = (agora_real - inicio_relacionamento).total_seconds()
            
            placeholder.markdown(f"""
            <div class="counter-card">
                <h3 style="color: #333 !important;">⚡ Segundos de Amor em Tempo Real</h3>
                <div class="big-number">{int(segundos_reais):,}</div>
                <p style="color: #333 !important;">E contando...</p>
            </div>
            """, unsafe_allow_html=True)
            
            time.sleep(1)
    
    # Botão especial
    if st.button("💕 Enviar Amor", type="primary"):
        st.balloons()
        st.success("Amor enviado com sucesso! 💕✨")
        st.markdown("### 💖 Te amo mais a cada segundo que passa!")

    if st.button("us?", type="primary"):
        st.snow()
        st.success("damn!!")
        st.markdown("### A HUUUUG!!!!!!")

if __name__ == "__main__":
    main()