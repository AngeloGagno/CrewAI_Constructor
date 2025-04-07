import streamlit as st
from create_crew_project.backend import run
import os
import zipfile

class Webapp:
    def __init__(self):
        self._configure_page()
        self._header()
        self._description()
        self.text = self._textbox()
        self._sidebar()
        self.button = self._execute_button()

    def _configure_page(self):
        st.set_page_config(
            page_title="Gerador de Conteúdo",
            page_icon="📝",
            layout="wide",
            initial_sidebar_state="expanded"
        )
        
        # CSS personalizado
        st.markdown("""
        <style>
        .main {
            padding: 2rem;
            background-color: #f8f9fa;
        }
        .stButton button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 24px;
            border-radius: 8px;
            font-weight: bold;
            border: none;
            transition: all 0.3s;
        }
        .stButton button:hover {
            background-color: #45a049;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }
        .stTextArea textarea {
            border-radius: 8px;
            border: 1px solid #ddd;
            padding: 10px;
        }
        .download-btn {
            background-color: #2196F3 !important;
        }
        .download-btn:hover {
            background-color: #0b7dda !important;
        }
        h1 {
            color: #333;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            padding-bottom: 20px;
            border-bottom: 2px solid #f0f0f0;
        }
        .success-message {
            background-color: #d4edda;
            color: #155724;
            padding: 15px;
            border-radius: 5px;
            margin: 20px 0;
        }
        </style>
        """, unsafe_allow_html=True)

    def _header(self):
        st.title("Gerador de Conteúdo para sua CrewAI")
        st.markdown("---")

    def _description(self):
        st.markdown("""
        ### Como funciona?
        1. Digite seu prompt detalhado na caixa de texto abaixo
        2. Clique em 'Gerar Arquivos'
        3. Aguarde o processamento
        4. Faça o download dos arquivos gerados
        """)

    def _sidebar(self):
        with st.sidebar:
            st.header("Sobre")
            st.info("""
            Esta ferramenta utiliza inteligência artificial para gerar arquivos de configuração para seu CrewAI.
            Sendo agents.yml, task.yml e o crew.py para facilitar o uso dessa ferramenta. 
            """)
            
            st.header("Exemplos")
            with st.expander("Ver exemplos de prompts"):
                st.markdown("""
                - Crie um relatório detalhado sobre os impactos ambientais do uso de plástico.
                - Desenvolva uma análise de mercado para uma startup de tecnologia educacional.
                - Elabore uma estratégia de marketing para um produto de beleza natural.
                """)
            st.header("Documentação")
            st.markdown("[Docs](https://google.com)")
            st.header("Contato")
            st.markdown("[GitHub](https://github.com/AngeloGagno)")
            st.markdown("[Linkedin](https://www.linkedin.com/in/angelogagno)")

    def _textbox(self):
        st.subheader("💬 Digite seu prompt")
        text = st.text_area(
            label="",
            placeholder="Descreva detalhadamente o que você deseja gerar (mínimo de 50 caracteres)...",
            height=200
        )
        st.caption(f"Caracteres: {len(text)}/50 mínimo")
        return text

    def _execute_button(self):
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            return st.button("Gerar Arquivos", use_container_width=True)

    def verify_len_text(self):
        if len(self.text) >= 50:
            return self.text
        else: 
            st.error('⚠️ Insira um prompt com pelo menos 50 caracteres para melhor entendimento do modelo.') 
            return None

    def verify_folder_output(self):
        output_path = 'output'
        if os.path.exists(output_path):
            files = [os.path.join(output_path, f) for f in os.listdir(output_path) if os.path.isfile(os.path.join(output_path, f))]
            if len(files) == 3:
                return files
        return None

    def create_zip(self, files, zip_path='output/output_files.zip'):
        with zipfile.ZipFile(zip_path, 'w') as zipf:
            for file in files:
                zipf.write(file, arcname=os.path.basename(file))
        return zip_path

    def cleanup_output(self):
        folder = 'output'
        for f in os.listdir(folder):
            file_path = os.path.join(folder, f)
            if os.path.isfile(file_path):
                os.remove(file_path)

    def show_zip_download_button(self, zip_file_path):
        with open(zip_file_path, 'rb') as f:
            st.markdown("""
            <div class="success-message">
                <h3>✅ Arquivos gerados com sucesso!</h3>
                <p>Seus arquivos estão prontos para download.</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.download_button(
                label="📦 Baixar Arquivos (.zip)",
                data=f,
                file_name=os.path.basename(zip_file_path),
                mime='application/zip',
                on_click=self.cleanup_output,
                key="download-button"
            )

    def execute(self):
        if self.button:
            validated_text = self.verify_len_text()
            if validated_text: 
                with st.spinner("🔄 Gerando seu conteúdo... Por favor, aguarde."):   
                    run(validated_text) 
                    
                    # Verifica os arquivos gerados
                    files = self.verify_folder_output()
                if files:
                    zip_path = self.create_zip(files)
                        
                    self.show_zip_download_button(zip_path)
                else:
                    st.warning("⚠️ Ainda não há 3 arquivos na pasta de output. Tente novamente mais tarde.")
