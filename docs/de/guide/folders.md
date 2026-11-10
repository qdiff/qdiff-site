---
title: "Ordner vergleichen"
description: "Sehen Sie neue, geänderte und fehlende Dateien in zwei Ordnern, filtern Sie den Baum und bringen Sie beide Seiten in Einklang."
---

# Ordner vergleichen

Wenn zwei Ordner übereinstimmen sollen — eine Arbeitskopie und ihre Sicherung,
ein alter Export und ein neuer —, ist der Vergleich Datei für Datei mühsam.
qDiff zeigt den gesamten Baum auf einmal.

<img src="/screenshots/folders.svg" alt="Zwei Ordnerbäume mit farbigen Dateizuständen" class="guide-shot" />

## Zwei Ordner öffnen

Ziehen Sie zwei Ordner ins Fenster oder wählen Sie sie über **Ablage → Öffnen**
aus. Auch Ordner innerhalb von Ordnern werden verglichen, sodass Sie das
vollständige Bild sehen.

## Den Baum auf einen Blick lesen

- **Grün** — eine Datei, die nur auf einer Seite existiert.
- **Orange** — der Name stimmt überein, der Inhalt weicht ab.
- **Rot** — eine Datei, die auf der anderen Seite fehlt.
- **Grau** — beide Seiten stimmen überein.

## Nur zeigen, was zählt

Nutzen Sie die Statusfilter, um alles auszublenden, was bereits übereinstimmt,
oder tippen Sie einen Teil eines Namens ein, um die Liste einzugrenzen. Sie
können eine schnelle Prüfung nur nach Namen wählen oder qDiff auch die Inhalte
lesen lassen — nützlich, wenn eine Sicherung richtig aussieht, aber innen
vielleicht veraltet ist.

Auch große Ordner öffnen sich schnell, sodass Sie nicht auf eine
Fortschrittsanzeige starren müssen.

## Direkt aus der Liste korrigieren

Kopieren Sie eine Datei auf die andere Seite, entfernen Sie einen Überrest oder
synchronisieren Sie eine ganze Gruppe — alles im selben Baum. Sie müssen nicht
zum Finder zurückwechseln.

::: tip Bedenkenlos stöbern
Auf der Festplatte wird nichts verändert, bis Sie eine Aktion wählen. Das
Durchsehen und Filtern eines Vergleichs ist völlig gefahrlos.
:::

Weiter: [ein Projekt vor dem Commit prüfen](./projects.md).
