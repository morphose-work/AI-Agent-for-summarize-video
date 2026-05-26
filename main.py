import streamlit as st

from src.crew import YoutubeSummaryCrew
from src.schema import OutputSummarySchema
from src.utils import load_css

load_css()

st.set_page_config(
    page_title='Yotube Summary Agent',
    page_icon='📽',
    layout='wide'
)

st.title('Yotube Summary Agent')

url = st.text_input('Введите ссылку на видео с Youtube')

col1, col2, col3 = st.columns([2,2,1])

with col2:
    start_btn = st.button('🚀Начать сумаризацию')

if start_btn and url:
    with st.status('Подождите...', expanded=True) as status:
        progress_bar = st.progress(0)

        status.text('🤖Агенты работают...')
        progress_bar.progress(50)

        crew = YoutubeSummaryCrew().crew().kickoff(inputs={'url': url})

        status.success('✅Готово')
        progress_bar.progress(100)

        result: OutputSummarySchema = crew.pydantic

        tab_1, tab_2, tab_3 = st.tabs(['📃Краткое содержание', '🔑Ключевые тезисы', '💡 Советы'])

        with tab_1:
            st.markdown(f'## **{result.title}**')
            st.write(result.brief_summary)

        with tab_2:
            st.markdown(f'## **{result.title}**')

            for key in result.key_points:
                st.markdown(f'- {key}')

        with tab_3:
            st.markdown(f'## **{result.title}**')
            
            for item in result.action_items:
                st.markdown(f'💡 {item}')