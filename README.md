# ⚡ AeroVento — Presentación interactiva (versión web)

La presentación es una sola página web (`index.html` / `presentacion.html`) con 8 diapositivas:
portada, qué hace la app, franjas del día, código Python paso a paso, calculadora en vivo,
la factura por dentro, mapa del código y el código Python completo de `logica.py`.

## Archivos

```
aerovento-presentacion-web/
├── index.html           # La presentación (para GitHub Pages)
├── presentacion.html    # La misma presentación (la lee Streamlit)
├── streamlit_app.py     # La muestra a pantalla completa en Streamlit
├── requirements.txt
└── .streamlit/config.toml
```

## Opción A (la más sencilla): GitHub Pages

1. Crea un repositorio en https://github.com/new (por ejemplo `aerovento-presentacion`).
2. Sube estos archivos: **Add file → Upload files**, arrastra el contenido de la carpeta y **Commit changes**.
3. Entra a **Settings → Pages**. En **Build and deployment** elige **Deploy from a branch**,
   rama `main`, carpeta `/ (root)` y pulsa **Save**.
4. En uno o dos minutos tendrás el enlace: `https://TU_USUARIO.github.io/aerovento-presentacion/`

## Opción B: Streamlit Community Cloud

1. Sube los archivos a GitHub igual que en el paso 1 y 2 de la opción A.
2. Entra a https://share.streamlit.io con tu cuenta de GitHub y pulsa **Create app**.
3. Elige **Deploy a public app from GitHub**, tu repositorio, la rama `main` y escribe
   `streamlit_app.py` como archivo principal.
4. Pulsa **Deploy**.

## Cómo presentar

- Pasa las diapositivas con las flechas ← → del teclado, con los puntos de abajo o deslizando.
- **Haz clic dentro de la presentación una vez** para que el teclado funcione (en Streamlit queda dentro de un marco).
- Las demostraciones (franjas, código, calculadora, factura) responden al clic.
- Pantalla completa: usa el botón de abajo o la tecla F11 del navegador.
- Las apps de Streamlit Community Cloud se duermen cuando pasa tiempo sin visitas. Ábrela unos minutos
  antes de presentar. Si la usas en GitHub Pages no pasa.

## Cosas que debes saber

- Las letras vienen de Google Fonts y necesitan internet. Sin conexión se ven con otra tipografía, pero todo funciona.
- El código Python que se muestra en la diapositiva final es el de `logica.py`. La plantilla HTML de la factura
  aparece abreviada.
- Si cambias el contenido, edita `index.html` y copia el mismo cambio a `presentacion.html`.
