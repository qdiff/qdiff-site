/**
 * Release links and the support address. Set a link to '' and every button
 * across the site falls back to the download guide / email, so no dead
 * store links ever ship.
 */
export const APP_STORE_ID = '6825630546'
export const APP_STORE_URL = `https://apps.apple.com/app/id${APP_STORE_ID}`
export const DMG_URL = ''
export const CONTACT_EMAIL = 'qdiff@w3cub.com'

export const DOWNLOAD_PATH = '/guide/download'
export const INTRO_PATH = '/guide/introduction'

export function mailto(subject: string): string {
  return `mailto:${CONTACT_EMAIL}?subject=${encodeURIComponent(subject)}`
}
