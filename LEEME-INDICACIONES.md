# Playbooks ATV, versión nueva — qué hay en esta carpeta y qué cambiar en la página

## 1. Qué hay acá

Esta carpeta reemplaza entera a la que está publicada en recursos.atvos.io. Subila completa (o reemplazá archivo por
archivo, el nombre de cada uno es el mismo que usa el `index.html` nuevo).

- `index.html` — la página, ya parchada (ver punto 3). Es el mismo código de siempre con los JSON nuevos adentro.
- `pdf/` — los 19 PDF (18 playbooks + `ATV-S0-00-Playbook-main-El-sistema-completo.pdf`). Los nombres cambiaron:
  ahora son `ATV-S1-01-Contenido-que-se-crea-solo.pdf`, `ATV-S1-02-Metodo-de-las-semillas.pdf`, etc. Son vectoriales,
  con el texto seleccionable, y la portada original de cada uno está estirada a A4 (misma proporción que las hojas).
- `pdf/datos/` — los mismos PDF en base64 (`s1-1.js`, …). Solo los usa la página cuando se abre como archivo local
  (`file://`). En el servidor no hacen falta, pero no molestan.
- `img/paginas/` — cada página como imagen webp de 1600 px (`s1-1-p1.webp`, …). Es el respaldo del lector cuando
  PDF.js no carga, y lo que se muestra en los buscadores.
- `img/portadas/` — las 18 portadas originales (4:3, para la grilla) y la del main (`s0-1.webp`).
- `img/logo-*.png` y `vendor/` — iguales a los que ya están.

## 2. Qué cambió en el contenido

- Los 18 playbooks están reescritos en tu voz, con un dibujo grande por página, letra de 13 pt en el cuerpo y
  títulos en mayúsculas. Pasaron de 8–9 páginas a entre 14 y 19 cada uno. Todo el método original está, repartido
  en más páginas.
- Hay un playbook nuevo, el **main** (`s0-1`): por dónde empezar según la situación, las 18 instalaciones en siete
  días, una serie por mes, las seis series resumidas, las cadencias por etapa, cómo meter los 19 PDF en Claude o
  ChatGPT (con las instrucciones y diez prompts), la semana con el sistema andando, el equipo, el glosario y las
  dieciocho señales de que está instalado.
- Correcciones que ya están aplicadas: 3.200 chats en todo el ejemplo del playbook 1; la serie 2 ya no usa el caso
  del coach de seducción, usa una clienta nutricionista y ATV; "ocho reels en dos semanas"; la regla de diagnóstico de
  s2-3 coherente con los 50 DMs; "cliente ideal" en s4-1; "prepará" en s5-2; un solo ejemplo de prompts en s6-2;
  nada de "claudes"; los términos (setter, closer, show rate, TOFU…) explicados la primera vez; las cadencias siempre
  con su etapa; un solo nombre por playbook; sin dos puntos en medio de las frases.
- Las descripciones de las tarjetas (`desc`) y el título de la serie 6 también cambiaron (sin dos puntos).

## 3. Qué cambió en `index.html` (ya está hecho, es para que sepas)

1. La portada ya no es 4:3 en el lector: se borró la regla `.page[data-p="1"]{aspect-ratio:4/3}`. Todas las
   páginas son A4.
2. El color de fondo de las bandas del lector (`--pdf-paper`) se tomó de las páginas nuevas.
3. El lector mostraba "Serie 0N · Playbook 0N / 03" arriba; para el main dice "Playbook main · El sistema completo".
4. Hay un bloque nuevo arriba de las series, "Empezá por acá", con la tarjeta del main, un chip en el índice de series
   y un botón en el hero ("Empezá por el playbook main").
5. El contador dice "18 playbooks + el main".
6. `<title>`, `meta description` y etiquetas `og:` nuevas (antes no había descripción para Google ni para compartir).
7. Los JSON embebidos (`content`, `imgs`, `ft`) son nuevos: 19 playbooks, las secciones de cada uno (ahora una por
   página, así el índice del lector salta a la página justa), el texto completo de cada página para el buscador.

Una aclaración sobre algo que te dije en el análisis: el lector de la página no muestra las páginas como imagen,
usa PDF.js y el texto se puede seleccionar. Lo que sí es cierto es que en el celular la letra de los PDF viejos se
leía chica; con la letra nueva (13 pt) eso queda resuelto.

## 4. Qué conviene revisar después de subir

- Abrir un playbook desde el celular y comprobar que la portada ocupa el alto entero (A4) y que no queda una banda
  oscura vacía arriba o abajo.
- Buscar "por dónde empiezo" en el buscador: tiene que aparecer el main.
- Si el hosting cachea, forzar la recarga del `index.html` (o cambiar el nombre de la carpeta `pdf/` y de las
  imágenes no hace falta: los nombres ya son nuevos).

## 5. Si querés cambiar algo a mano

Los textos de las tarjetas (título, descripción, "lo que resolvés", "cómo sabés que funciona", "te sirve si…")
están en el JSON `content` dentro del `index.html`, y también sueltos en `content.json` por si preferís editarlos ahí
y pegarlos. El texto que usa el buscador está en el JSON `ft` (una entrada por página).
