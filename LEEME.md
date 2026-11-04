# Playbooks ATV

Plataforma de los 18 playbooks de ATV: buscador por problema, lector de páginas
dentro de la web y panel de resumen al costado de cada playbook.

## Qué hay en esta carpeta

- `index.html`: la página completa. Abrila directo en el navegador o subila a cualquier hosting.
- `pdf/`: los 18 PDF originales. El visor del lector los muestra con PDF.js: texto seleccionable, zoom, pantalla completa y descarga.
- `pdf/datos/`: los mismos PDF como `.js`. Solo se usan al abrir `index.html` con doble clic, porque el navegador no deja leer archivos desde `file://`. Si cambiás un PDF, hay que regenerar su `.js`.
- `vendor/`: PDF.js 3.11.174.
- `img/paginas/`: las 161 páginas en WebP (1600 px de ancho), nombradas `s<serie>-<playbook>-p<página>.webp`. Quedan como respaldo: el lector las usa si un PDF no carga.
- `img/portadas/`: las 18 portadas.
- `img/logo-oscuro.png` y `img/logo-claro.png`: el logo para fondo claro y para fondo oscuro.
- `contenido.json`: todos los textos editables (título, descripción, cifras, series, títulos y descripciones de cada playbook, bullets del resumen, "Cómo sabés que funciona" y las frases-problema del buscador). Es una copia de lo que ya está dentro de `index.html`, en el bloque `<script type="application/json" id="content">`.
- `texto-completo-pdfs.json`: el texto de cada página de cada PDF. El buscador lo usa para encontrar la página exacta. También está dentro de `index.html`, en el bloque `id="ft"`.

## Notas para seguir trabajando

- Los textos se leen del bloque JSON `id="content"` de `index.html`. Para cambiar un texto, editá ese bloque (o regeneralo desde `contenido.json`).
- El botón "Editar textos" y el guardado solo funcionaban dentro de Claude (usaban las funciones de los artifacts de claude.ai). Fuera de Claude el botón no aparece.
- El visor no tiene bordes porque cada página va sobre una franja de su mismo color: crema (`--pdf-paper`) y oscuro (`--pdf-dark`) en la primera y la última. Si un PDF nuevo cambia esos colores, hay que ajustar `bandsHtml` en `index.html`.
- Las tipografías son las del sistema (Helvetica en Mac/iPhone). Si querés volver a usar Helvetica Now Display y Hoosegow, agregá los `@font-face` en el `<style>` y las variables `--font-display` y `--font-slab`.
