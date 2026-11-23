"""
streamlit_app.py — Muestra la presentación interactiva de AeroVento como una página web.

La presentación es el archivo presentacion.html (HTML, CSS y JavaScript en un solo archivo).
Streamlit solo la incrusta a pantalla completa.
"""

from pathlib import Path

import streamlit as st

st.set_page_config(page_title="AeroVento · Presentación", page_icon="⚡",
                   layout="wide", initial_sidebar_state="collapsed")

# Quita el encabezado y los márgenes para que la presentación ocupe toda la pantalla.
st.html("""
<style>
header, [data-testid="stHeader"], footer { display: none !important; }
.block-container { padding: 0 !important; max-width: 100% !important; }
iframe { height: 100vh !important; border: 0; }
</style>
""")

HTML = (Path(__file__).parent / "presentacion.html").read_text(encoding="utf-8")


def mostrar(html: str, alto: int = 800):
    """Incrusta el HTML. Usa st.iframe (versiones nuevas) o components.html (versiones viejas)."""
    if hasattr(st, "iframe"):
        st.iframe(html, height=alto)
    else:
        import streamlit.components.v1 as components
        components.html(html, height=alto, scrolling=False)


mostrar(HTML)
