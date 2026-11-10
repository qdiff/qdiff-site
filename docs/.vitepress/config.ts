import { defineConfig } from 'vitepress'

// ── Per-locale UI strings (nav / sidebar / footer) ────────────────
// Page copy itself lives in each locale's markdown files.
const STR = {
  en: {
    home: 'Home', features: 'Features', guide: 'Guide', download: 'Download',
    faq: 'FAQ', support: 'Support',
    startGroup: 'Getting started',
    intro: 'Meet qDiff', install: 'Get & install',
    useGroup: 'Using qDiff',
    files: 'Compare files', folders: 'Compare folders',
    projects: 'Before you commit', more: 'More ways to compare',
    helpGroup: 'Help',
    contact: 'Contact us',
    aboutGroup: 'About',
    privacy: 'Privacy Policy', terms: 'Terms of Use', sysreq: 'System requirements',
    footerMessage: 'qDiff — see exactly what changed between files, folders and projects. Everything stays on your Mac.',
    footerCopyright: '© 2026 w3cub.com. All rights reserved.',
    product: 'Product', supportCol: 'Support', aboutCol: 'About',
    language: 'Language', email: 'Email us',
  },
  'zh-CN': {
    home: '首页', features: '功能', guide: '使用指南', download: '下载',
    faq: '常见问题', support: '联系我们',
    startGroup: '开始使用',
    intro: '认识 qDiff', install: '获取与安装',
    useGroup: '怎么用',
    files: '比较文件', folders: '比较文件夹',
    projects: '提交前看一遍', more: '更多比较方式',
    helpGroup: '帮助',
    contact: '联系我们',
    aboutGroup: '关于',
    privacy: '隐私政策', terms: '使用条款', sysreq: '系统要求',
    footerMessage: 'qDiff —— 把文件、文件夹与项目里的改动并排看清，所有内容只留在你的 Mac 上。',
    footerCopyright: '© 2026 w3cub.com 保留所有权利。',
    product: '产品', supportCol: '支持', aboutCol: '关于',
    language: '语言', email: '邮件联系',
  },
  'zh-TW': {
    home: '首頁', features: '功能', guide: '使用指南', download: '下載',
    faq: '常見問題', support: '聯絡我們',
    startGroup: '開始使用',
    intro: '認識 qDiff', install: '取得與安裝',
    useGroup: '怎麼用',
    files: '比較檔案', folders: '比較資料夾',
    projects: '提交前看一遍', more: '更多比較方式',
    helpGroup: '幫助',
    contact: '聯絡我們',
    aboutGroup: '關於',
    privacy: '隱私政策', terms: '使用條款', sysreq: '系統需求',
    footerMessage: 'qDiff —— 把檔案、資料夾與專案裡的改動並排看清，所有內容只留在你的 Mac 上。',
    footerCopyright: '© 2026 w3cub.com 保留所有權利。',
    product: '產品', supportCol: '支援', aboutCol: '關於',
    language: '語言', email: '郵件聯絡',
  },
  ja: {
    home: 'ホーム', features: '機能', guide: 'ガイド', download: 'ダウンロード',
    faq: 'よくある質問', support: 'お問い合わせ',
    startGroup: 'はじめに',
    intro: 'qDiff を知る', install: '入手とインストール',
    useGroup: '使い方',
    files: 'ファイルを比較', folders: 'フォルダーを比較',
    projects: 'コミット前の確認', more: 'その他の比較方法',
    helpGroup: 'ヘルプ',
    contact: 'お問い合わせ',
    aboutGroup: 'qDiff について',
    privacy: 'プライバシーポリシー', terms: '利用規約', sysreq: 'システム要件',
    footerMessage: 'qDiff —— ファイル、フォルダー、プロジェクトの変更点を並べて正確に確認できます。すべてのデータはお使いの Mac 内だけに留まります。',
    footerCopyright: '© 2026 w3cub.com. すべての権利を留保します。',
    product: '製品', supportCol: 'サポート', aboutCol: 'qDiff について',
    language: '言語', email: 'メールでお問い合わせ',
  },
  de: {
    home: 'Start', features: 'Funktionen', guide: 'Anleitung', download: 'Download',
    faq: 'FAQ', support: 'Kontakt',
    startGroup: 'Erste Schritte',
    intro: 'qDiff kennenlernen', install: 'Herunterladen & installieren',
    useGroup: 'qDiff nutzen',
    files: 'Dateien vergleichen', folders: 'Ordner vergleichen',
    projects: 'Vor dem Commit prüfen', more: 'Weitere Vergleichsarten',
    helpGroup: 'Hilfe',
    contact: 'Kontakt',
    aboutGroup: 'Über qDiff',
    privacy: 'Datenschutz', terms: 'Nutzungsbedingungen', sysreq: 'Systemvoraussetzungen',
    footerMessage: 'qDiff — sehen Sie genau, was sich in Dateien, Ordnern und Projekten geändert hat. Alle Daten bleiben auf Ihrem Mac.',
    footerCopyright: '© 2026 w3cub.com. Alle Rechte vorbehalten.',
    product: 'Produkt', supportCol: 'Support', aboutCol: 'Über qDiff',
    language: 'Sprache', email: 'E-Mail schreiben',
  },
  es: {
    home: 'Inicio', features: 'Funciones', guide: 'Guía', download: 'Descarga',
    faq: 'Preguntas frecuentes', support: 'Contacto',
    startGroup: 'Primeros pasos',
    intro: 'Conoce qDiff', install: 'Descargar e instalar',
    useGroup: 'Cómo usarlo',
    files: 'Comparar archivos', folders: 'Comparar carpetas',
    projects: 'Antes de confirmar', more: 'Más formas de comparar',
    helpGroup: 'Ayuda',
    contact: 'Contacto',
    aboutGroup: 'Acerca de',
    privacy: 'Política de privacidad', terms: 'Términos de uso', sysreq: 'Requisitos del sistema',
    footerMessage: 'qDiff — descubre exactamente qué cambió entre archivos, carpetas y proyectos. Todo permanece en tu Mac.',
    footerCopyright: '© 2026 w3cub.com. Todos los derechos reservados.',
    product: 'Producto', supportCol: 'Soporte', aboutCol: 'Acerca de',
    language: 'Idioma', email: 'Escríbenos',
  },
  fr: {
    home: 'Accueil', features: 'Fonctionnalités', guide: 'Guide', download: 'Télécharger',
    faq: 'FAQ', support: 'Contact',
    startGroup: 'Bien démarrer',
    intro: 'Découvrir qDiff', install: 'Obtenir et installer',
    useGroup: 'Utiliser qDiff',
    files: 'Comparer des fichiers', folders: 'Comparer des dossiers',
    projects: 'Avant de valider', more: 'Autres comparaisons',
    helpGroup: 'Aide',
    contact: 'Nous contacter',
    aboutGroup: 'À propos',
    privacy: 'Confidentialité', terms: "Conditions d'utilisation", sysreq: 'Configuration requise',
    footerMessage: 'qDiff — voyez exactement ce qui a changé entre vos fichiers, dossiers et projets. Tout reste sur votre Mac.',
    footerCopyright: '© 2026 w3cub.com. Tous droits réservés.',
    product: 'Produit', supportCol: 'Assistance', aboutCol: 'À propos',
    language: 'Langue', email: 'Nous écrire',
  },
}

// All internal links get the locale segment so nav / sidebar / footer
// resolve to the localized page in every language.
function tc(S: typeof STR.en, lang: string) {
  const base = !lang || lang === 'en' ? '' : `/${lang}`
  const L = (p: string) =>
    /^https?:\/\//.test(p) || p.startsWith('mailto:') || p.startsWith(base)
      ? p
      : `${base}${p}`
  return {
    nav: [
      { text: S.home, link: L('/') },
      { text: S.features, link: L('/#features') },
      { text: S.guide, link: L('/guide/introduction') },
      { text: S.download, link: L('/guide/download') },
      { text: S.faq, link: L('/guide/faq') },
    ],
    sidebar: [
      {
        text: S.startGroup,
        items: [
          { text: S.intro, link: L('/guide/introduction') },
          { text: S.install, link: L('/guide/download') },
        ],
      },
      {
        text: S.useGroup,
        items: [
          { text: S.files, link: L('/guide/files') },
          { text: S.folders, link: L('/guide/folders') },
          { text: S.projects, link: L('/guide/projects') },
          { text: S.more, link: L('/guide/more') },
        ],
      },
      {
        text: S.helpGroup,
        items: [
          { text: S.faq, link: L('/guide/faq') },
          { text: S.support, link: L('/guide/support') },
        ],
      },
      {
        text: S.aboutGroup,
        items: [
          { text: S.privacy, link: L('/privacy/') },
          { text: S.terms, link: L('/terms/') },
          { text: S.sysreq, link: L('/guide/download#system-requirements') },
        ],
      },
    ],
    footer: {
      message: S.footerMessage,
      copyright: S.footerCopyright,
      items: [
        {
          text: S.product,
          items: [
            { text: S.features, link: L('/#features') },
            { text: S.download, link: L('/guide/download') },
            { text: S.intro, link: L('/guide/introduction') },
            { text: S.more, link: L('/guide/more') },
          ],
        },
        {
          text: S.supportCol,
          items: [
            { text: S.guide, link: L('/guide/introduction') },
            { text: S.faq, link: L('/guide/faq') },
            { text: S.contact, link: L('/guide/support') },
            { text: S.email, link: 'mailto:qdiff@w3cub.com' },
          ],
        },
        {
          text: S.aboutCol,
          items: [
            { text: S.privacy, link: L('/privacy/') },
            { text: S.terms, link: L('/terms/') },
            { text: S.sysreq, link: L('/guide/download#system-requirements') },
          ],
        },
      ],
    },
    langMenuLabel: S.language,
  }
}

const MD = {
  'zh-CN': {
    container: { tipLabel: '提示', warningLabel: '注意', dangerLabel: '重要', infoLabel: '说明', detailsLabel: '详情' },
    codeCopyButton: { tooltipText: '复制', copiedText: '已复制' },
  },
  'zh-TW': {
    container: { tipLabel: '提示', warningLabel: '注意', dangerLabel: '重要', infoLabel: '說明', detailsLabel: '詳情' },
    codeCopyButton: { tooltipText: '複製', copiedText: '已複製' },
  },
  ja: {
    container: { tipLabel: 'ヒント', warningLabel: '警告', dangerLabel: '危険', infoLabel: '情報', detailsLabel: '詳細' },
    codeCopyButton: { tooltipText: 'コードをコピー', copiedText: 'コピーしました' },
  },
  de: {
    container: { tipLabel: 'Tipp', warningLabel: 'Warnung', dangerLabel: 'Gefahr', infoLabel: 'Info', detailsLabel: 'Details' },
    codeCopyButton: { tooltipText: 'Code kopieren', copiedText: 'Kopiert' },
  },
  es: {
    container: { tipLabel: 'Consejo', warningLabel: 'Advertencia', dangerLabel: 'Peligro', infoLabel: 'Info', detailsLabel: 'Detalles' },
    codeCopyButton: { tooltipText: 'Copiar código', copiedText: 'Copiado' },
  },
  fr: {
    container: { tipLabel: 'Astuce', warningLabel: 'Avertissement', dangerLabel: 'Danger', infoLabel: 'Info', detailsLabel: 'Détails' },
    codeCopyButton: { tooltipText: 'Copier le code', copiedText: 'Copié' },
  },
}

// ── Local search UI strings, keyed by VitePress' localeIndex ──────
// ('root' is the English default). Without these the search box and its
// modal stay in English on every translated page.
function searchLocale(t: {
  search: string; details: string; reset: string; back: string; none: string;
  select: string; navigate: string; close: string;
}) {
  return {
    translations: {
      button: { buttonText: t.search, buttonAriaLabel: t.search },
      modal: {
        displayDetails: t.details,
        resetButtonTitle: t.reset,
        backButtonTitle: t.back,
        noResultsText: t.none,
        footer: {
          selectText: t.select,
          selectKeyAriaLabel: 'enter',
          navigateText: t.navigate,
          navigateUpKeyAriaLabel: 'up arrow',
          navigateDownKeyAriaLabel: 'down arrow',
          closeText: t.close,
          closeKeyAriaLabel: 'escape',
        },
      },
    },
  }
}

const SEARCH_LOCALES = {
  root: searchLocale({
    search: 'Search', details: 'Display detailed list', reset: 'Reset query',
    back: 'Back to search', none: 'No results for',
    select: 'to select', navigate: 'to navigate', close: 'to close',
  }),
  'zh-CN': searchLocale({
    search: '搜索', details: '显示详细列表', reset: '清除搜索',
    back: '返回搜索', none: '没有找到',
    select: '选择', navigate: '切换', close: '关闭',
  }),
  'zh-TW': searchLocale({
    search: '搜尋', details: '顯示詳細列表', reset: '清除搜尋',
    back: '返回搜尋', none: '找不到結果',
    select: '選擇', navigate: '切換', close: '關閉',
  }),
  ja: searchLocale({
    search: '検索', details: '詳細リストを表示', reset: '検索をクリア',
    back: '検索に戻る', none: '該当する結果はありません',
    select: '選択', navigate: '移動', close: '閉じる',
  }),
  de: searchLocale({
    search: 'Suchen', details: 'Detaillierte Liste anzeigen', reset: 'Suche zurücksetzen',
    back: 'Zurück zur Suche', none: 'Keine Ergebnisse für',
    select: 'auswählen', navigate: 'navigieren', close: 'schließen',
  }),
  es: searchLocale({
    search: 'Buscar', details: 'Mostrar lista detallada', reset: 'Borrar búsqueda',
    back: 'Volver a la búsqueda', none: 'Sin resultados para',
    select: 'seleccionar', navigate: 'desplazarse', close: 'cerrar',
  }),
  fr: searchLocale({
    search: 'Rechercher', details: 'Afficher la liste détaillée', reset: 'Effacer la recherche',
    back: 'Retour à la recherche', none: 'Aucun résultat pour',
    select: 'sélectionner', navigate: 'naviguer', close: 'fermer',
  }),
}

const SITE = 'https://qdiff.w3cub.com'

export default defineConfig({
  base: '/',
  title: 'qDiff',
  titleTemplate: 'qDiff — :title',
  description: 'qDiff compares files, folders and projects side by side on your Mac, so you can see exactly what changed. Private by design — your files never leave your computer.',
  lastUpdated: true,
  head: [
    ['link', { rel: 'icon', type: 'image/png', href: '/favicon.png' }],
    ['link', { rel: 'apple-touch-icon', href: '/logo.png' }],
    ['meta', { name: 'theme-color', content: '#3b82f6' }],
    ['meta', { name: 'viewport', content: 'width=device-width, initial-scale=1.0' }],
    ['meta', { name: 'keywords', content: 'qDiff, diff, compare files, compare folders, file comparison, visual diff, merge, macOS, code review, find differences' }],
    ['meta', { name: 'author', content: 'w3cub.com' }],
    ['meta', { property: 'og:type', content: 'website' }],
    ['meta', { property: 'og:site_name', content: 'qDiff' }],
    ['meta', { property: 'og:url', content: `${SITE}/` }],
    ['meta', { property: 'og:title', content: 'qDiff — See exactly what changed' }],
    ['meta', { property: 'og:description', content: 'Compare files, folders and projects side by side. Colour-coded changes, every file staying on your Mac.' }],
    ['meta', { property: 'og:image', content: `${SITE}/preview.png` }],
    ['meta', { property: 'og:image:width', content: '1200' }],
    ['meta', { property: 'og:image:height', content: '630' }],
    ['meta', { property: 'og:image:alt', content: 'qDiff — See exactly what changed' }],
    ['meta', { name: 'twitter:card', content: 'summary_large_image' }],
    ['meta', { name: 'twitter:url', content: `${SITE}/` }],
    ['meta', { name: 'twitter:title', content: 'qDiff — See exactly what changed' }],
    ['meta', { name: 'twitter:description', content: 'Compare files, folders and projects side by side. Colour-coded changes, every file staying on your Mac.' }],
    ['meta', { name: 'twitter:image', content: `${SITE}/preview.png` }],
    ['meta', { name: 'twitter:image:alt', content: 'qDiff — See exactly what changed' }],
  ],
  themeConfig: {
    siteTitle: 'qDiff',
    logo: '/logo.png',
    search: { provider: 'local', options: { locales: SEARCH_LOCALES } },
    socialLinks: [
      { icon: 'github', link: 'https://github.com/qdiff' },
    ],
  },
  locales: {
    root: {
      label: 'English',
      lang: 'en',
      themeConfig: tc(STR.en, 'en'),
    },
    'zh-CN': {
      label: '简体中文',
      lang: 'zh-CN',
      link: '/zh-CN/',
      themeConfig: tc(STR['zh-CN'], 'zh-CN'),
      markdown: MD['zh-CN'],
    },
    'zh-TW': {
      label: '繁體中文',
      lang: 'zh-TW',
      link: '/zh-TW/',
      themeConfig: tc(STR['zh-TW'], 'zh-TW'),
      markdown: MD['zh-TW'],
    },
    ja: {
      label: '日本語',
      lang: 'ja',
      link: '/ja/',
      themeConfig: tc(STR.ja, 'ja'),
      markdown: MD.ja,
    },
    de: {
      label: 'Deutsch',
      lang: 'de',
      link: '/de/',
      themeConfig: tc(STR.de, 'de'),
      markdown: MD.de,
    },
    es: {
      label: 'Español',
      lang: 'es',
      link: '/es/',
      themeConfig: tc(STR.es, 'es'),
      markdown: MD.es,
    },
    fr: {
      label: 'Français',
      lang: 'fr',
      link: '/fr/',
      themeConfig: tc(STR.fr, 'fr'),
      markdown: MD.fr,
    },
  },
})
