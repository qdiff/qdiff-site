/**
 * Locale helpers for the custom theme.
 *
 * All *translatable content* lives in each page's markdown frontmatter
 * (see docs/<lang>/index.md). This file
 * only holds the small bits of logic that must stay in code: the list of
 * supported locales and the helpers that compute locale-prefixed links.
 */

export type Lang = 'en' | 'zh-CN' | 'zh-TW' | 'ja' | 'de' | 'es' | 'fr'

export const SUPPORTED_LANGS: Lang[] = [
  'en', 'zh-CN', 'zh-TW', 'ja', 'de', 'es', 'fr',
]

/** Resolve the current lang, falling back to 'en' for unknown values. */
export function resolveLang(lang: string): Lang {
  return (SUPPORTED_LANGS as string[]).includes(lang) ? (lang as Lang) : 'en'
}

/** Prefix a path with the locale segment, or return as-is for English (root). */
export function localeLink(path: string, lang: string): string {
  if (!lang || lang === 'en') return path
  return `/${lang}${path}`
}
