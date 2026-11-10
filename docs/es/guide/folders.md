---
title: "Comparar carpetas"
description: "Vea los archivos nuevos, modificados y ausentes en dos carpetas, filtre el árbol y sincronice ambos lados."
---

# Comparar carpetas

Cuando dos carpetas deberían coincidir —una copia de trabajo y su copia de
seguridad, una exportación antigua y otra nueva— compararlas archivo por
archivo es un engorro. qDiff muestra todo el árbol de una vez.

<img src="/screenshots/folders.svg" alt="Dos árboles de carpetas con estados de archivo coloreados" class="guide-shot" />

## Abra dos carpetas

Arrastre dos carpetas a la ventana o elíjalas desde **Archivo → Abrir**. Las
carpetas dentro de carpetas también se comparan, para que vea el panorama
completo.

## Lea el árbol de un vistazo

- **Verde** — un archivo que solo existe en un lado.
- **Naranja** — el nombre coincide pero el contenido difiere.
- **Rojo** — un archivo que falta en el otro lado.
- **Gris** — los dos lados coinciden.

## Muestre solo lo que importa

Use los filtros por estado para ocultar todo lo que ya coincide, o escriba parte
de un nombre para reducir la lista. Puede elegir una comprobación rápida solo
por nombre o pedir a qDiff que lea también el contenido, algo útil cuando una
copia de seguridad parece correcta pero podría estar desactualizada por dentro.

Incluso las carpetas grandes se abren rápido, así que no se quedará mirando una
barra de progreso.

## Ponga todo en orden desde la lista

Copie un archivo al otro lado, elimine un sobrante o sincronice todo un grupo,
siempre desde el mismo árbol. No hace falta volver al Finder.

::: tip Puede explorar sin miedo
No se cambia nada en el disco hasta que usted elige una acción. Examinar y
filtrar una comparación es completamente seguro.
:::

A continuación: [revise un proyecto antes de confirmar los cambios](./projects.md).
