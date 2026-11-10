---
title: "Comparer des dossiers"
description: "Visualisez les fichiers nouveaux, modifiés et manquants entre deux dossiers, filtrez l'arborescence et resynchronisez les deux côtés."
---

# Comparer des dossiers

Quand deux dossiers devraient correspondre — une copie de travail et sa
sauvegarde, un ancien export et un nouveau — les comparer fichier par fichier
est fastidieux. qDiff affiche toute l'arborescence d'un seul coup.

<img src="/screenshots/folders.svg" alt="Deux arborescences de dossiers avec des états de fichiers en couleur" class="guide-shot" />

## Ouvrir deux dossiers

Déposez deux dossiers sur la fenêtre, ou choisissez-les depuis
**Fichier → Ouvrir**. Les dossiers contenus dans les dossiers sont comparés
eux aussi, pour vous donner une vue complète.

## Lire l'arborescence d'un coup d'œil

- **Vert** — un fichier qui n'existe que d'un seul côté.
- **Orange** — le nom correspond mais le contenu diffère.
- **Rouge** — un fichier absent de l'autre côté.
- **Gris** — les deux côtés correspondent.

## N'afficher que l'essentiel

Utilisez les filtres par état pour masquer tout ce qui correspond déjà, ou
saisissez une partie d'un nom pour réduire la liste. Vous pouvez choisir une
vérification rapide sur les noms seuls ou demander à qDiff de lire aussi le
contenu — pratique lorsqu'une sauvegarde semble correcte mais pourrait être
périmée à l'intérieur.

Même les grands dossiers s'ouvrent vite : nul besoin de rester devant une
barre de progression.

## Remettre les choses en ordre depuis la liste

Copiez un fichier de l'autre côté, supprimez un reliquat ou synchronisez tout
un groupe — le tout depuis la même arborescence. Inutile de revenir au Finder.

::: tip Explorez sans risque
Rien n'est modifié sur le disque tant que vous ne lancez pas une action.
Parcourir et filtrer une comparaison est totalement sans danger.
:::

Ensuite : [relisez un projet avant de valider](./projects.md).
