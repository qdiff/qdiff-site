<template>
  <nav class="navbar" ref="navEl">
    <div class="nav-container">
      <div class="nav-brand">
        <VPLink :href="homeLink" class="brand-link">
          <img src="/logo.png" alt="qDiff" class="brand-logo" />
          <span class="brand-text">qDiff</span>
        </VPLink>
      </div>

      <div class="nav-right">
        <!-- Desktop: same order, groups and dividers as VitePress' inner-page
             navbar (menu | translations | appearance | social links). -->
        <div class="nav-inline">
          <VPNavBarMenu class="nav-menu" />
          <span class="nav-divider" aria-hidden="true" />
          <VPNavBarTranslations class="nav-lang" />
          <span class="nav-divider nav-divider-appearance" aria-hidden="true" />
          <VPSwitchAppearance class="nav-appearance" />
          <span class="nav-divider nav-divider-social" aria-hidden="true" />
          <VPNavBarSocialLinks class="nav-social" />
        </div>

        <!-- Mobile: a "more" button that opens the menu panel -->
        <button
          class="nav-more"
          type="button"
          :aria-expanded="menuOpen"
          aria-label="Open menu"
          @click="menuOpen = !menuOpen"
        >
          <svg viewBox="0 0 24 24" width="22" height="22" fill="currentColor" aria-hidden="true">
            <circle cx="5" cy="12" r="2" />
            <circle cx="12" cy="12" r="2" />
            <circle cx="19" cy="12" r="2" />
          </svg>
        </button>

        <!-- Theme toggle stays visible on every breakpoint -->
      </div>
    </div>

    <!-- Mobile dropdown panel -->
    <transition name="panel">
      <div v-if="menuOpen" class="nav-panel">
        <div class="nav-panel-inner">
          <ul class="panel-nav">
            <li v-for="item in navItems" :key="item.text">
              <a
                :href="item.link"
                class="panel-link"
                target="_blank"
                rel="noopener noreferrer"
                v-if="isExternal(item.link)"
                @click="close"
              >{{ item.text }}</a>
              <a v-else :href="item.link" class="panel-link" @click="close">{{ item.text }}</a>
            </li>
          </ul>

          <div class="panel-langs">
            <span class="panel-langs-title">{{ langMenuLabel }}</span>
            <a
              v-for="l in localeLinks"
              :key="l.link"
              :href="l.link"
              class="panel-lang"
              :class="{ active: l.text === currentLang.label }"
              @click="close"
            >{{ l.text }}</a>
          </div>

          <!-- Mirrors the social link inside VitePress' mobile screen menu -->
          <a
            href="https://github.com/qdiff"
            target="_blank"
            rel="noopener noreferrer"
            class="panel-social-link"
            @click="close"
          >
            <svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor" aria-hidden="true">
              <path d="M12 .5C5.73.5.5 5.73.5 12c0 5.08 3.29 9.39 7.86 10.91.58.11.79-.25.79-.56 0-.28-.01-1.02-.02-2-3.2.7-3.88-1.54-3.88-1.54-.52-1.33-1.28-1.69-1.28-1.69-1.05-.72.08-.7.08-.7 1.16.08 1.77 1.19 1.77 1.19 1.03 1.77 2.7 1.26 3.36.96.1-.75.4-1.26.73-1.55-2.55-.29-5.24-1.28-5.24-5.69 0-1.26.45-2.29 1.19-3.1-.12-.29-.52-1.46.11-3.05 0 0 .97-.31 3.18 1.18a11 11 0 0 1 5.8 0c2.2-1.49 3.17-1.18 3.17-1.18.63 1.59.23 2.76.11 3.05.74.81 1.19 1.84 1.19 3.1 0 4.42-2.7 5.39-5.26 5.68.41.36.78 1.06.78 2.14 0 1.55-.01 2.8-.01 3.18 0 .31.21.68.8.56A11.51 11.51 0 0 0 23.5 12C23.5 5.73 18.27.5 12 .5z" />
            </svg>
            <span>GitHub</span>
          </a>
        </div>
      </div>
    </transition>
  </nav>
</template>

<script setup lang="ts">
import { ref, computed, onMounted, onUnmounted, watch } from 'vue'
import { useData, useRoute } from 'vitepress'
import { VPLink } from 'vitepress/theme'
import VPNavBarMenu from 'vitepress/dist/client/theme-default/components/VPNavBarMenu.vue'
import VPNavBarTranslations from 'vitepress/dist/client/theme-default/components/VPNavBarTranslations.vue'
import VPNavBarSocialLinks from 'vitepress/dist/client/theme-default/components/VPNavBarSocialLinks.vue'
import VPSwitchAppearance from 'vitepress/dist/client/theme-default/components/VPSwitchAppearance.vue'
import { SUPPORTED_LANGS } from './locale'

// Derived from the single source of truth in locale.ts (English is the root).
const LOCALE_PREFIX = new RegExp(
  `^\\/(${SUPPORTED_LANGS.filter((l) => l !== 'en').join('|')})(\\/.*)?$`
)

const { lang, theme, site } = useData()
const route = useRoute()

const menuOpen = ref(false)
const navEl = ref<HTMLElement | null>(null)

// Locale-aware home link for the brand logo
const homeLink = computed(() =>
  !lang.value || lang.value === 'en' ? '/' : `/${lang.value}/`
)

// Current locale's nav items (each has text + link).
// localeLink is not needed here: links in theme.nav are already
// locale-prefixed by config.ts (tc()),
// so we use them as-is — no extra localeLink() wrapping.
const navItems = computed(() =>
  (theme.value.nav || []).map((item: any) => ({
    text: item.text,
    link: item.link,
  }))
)

const langMenuLabel = computed(() => theme.value.langMenuLabel || 'Language')

// The English locale is keyed as 'root', not 'en' — resolve by the locale's
// `lang` field so the mobile switcher marks the right entry as active.
const currentLang = computed(() => {
  const locales = site.value.locales || {}
  const key = Object.keys(locales).find(
    (k) => (locales[k]?.lang || (k === 'root' ? 'en' : k)) === lang.value
  ) || 'root'
  return { key, label: locales[key]?.label || 'English' }
})

// Build the language list from the configured locales, keeping the user on the
// same relative path when they switch language.
function stripLangPrefix(p: string): string {
  const m = p.match(LOCALE_PREFIX)
  return m ? (m[2] || '/') : p
}
const localeLinks = computed(() => {
  const locales = site.value.locales || {}
  const base = stripLangPrefix(route.path)
  return Object.entries(locales)
    .filter(([key]) => key !== currentLang.value.key)
    .map(([key, val]: [string, any]) => {
      const prefix = key === 'root' ? '' : `/${key}`
      return { text: val.label, link: prefix + base, lang: key }
    })
})

function isExternal(link: string): boolean {
  return /^https?:\/\//.test(link) || link.startsWith('mailto:')
}

function close() {
  menuOpen.value = false
}

function onDocClick(e: MouseEvent) {
  if (!menuOpen.value) return
  if (navEl.value && !navEl.value.contains(e.target as Node)) {
    menuOpen.value = false
  }
}

function onKey(e: KeyboardEvent) {
  if (e.key === 'Escape') menuOpen.value = false
}

// Close the panel whenever the route changes
watch(
  () => useRoute().path,
  () => { menuOpen.value = false }
)

onMounted(() => {
  document.addEventListener('click', onDocClick)
  document.addEventListener('keydown', onKey)
})
onUnmounted(() => {
  document.removeEventListener('click', onDocClick)
  document.removeEventListener('keydown', onKey)
})
</script>

<style scoped>
.navbar {
  position: fixed;
  top: 0; left: 0; right: 0;
  background: var(--ah-navbar-bg);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  border-bottom: 1px solid var(--ah-navbar-border);
  z-index: 1000;
}
.nav-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 70px;
}
.nav-brand .brand-link { display: flex; align-items: center; gap: 12px; text-decoration: none; }
.brand-logo { height: 32px; width: auto; }
.brand-text { font-size: 20px; font-weight: 700; color: var(--vp-c-text-1); }

.nav-right { display: flex; align-items: center; gap: 20px; }
.nav-inline { display: flex; align-items: center; gap: 0; }
.nav-appearance { display: flex; align-items: center; }

/* VitePress draws a 1px divider between each of the four navbar groups on
   inner pages (menu | translations | appearance | social links). Reproduce
   the same rules and the same 1280px breakpoint here so both headers match. */
.nav-divider {
  display: none;
  width: 1px;
  height: 24px;
  flex: 0 0 1px;
  background-color: var(--vp-c-divider);
  margin: 0 8px;
}

@media (min-width: 1280px) {
  .nav-divider { display: block; }
  .nav-divider-appearance { margin-right: 16px; }
  .nav-divider-social { margin-left: 16px; }
  .nav-social { margin-right: -8px; }
}

/* The "more" button is hidden on desktop, shown on mobile */
.nav-more {
  display: none;
  align-items: center;
  justify-content: center;
  width: 40px; height: 40px;
  border: none;
  background: transparent;
  color: var(--vp-c-text-1);
  cursor: pointer;
  border-radius: 8px;
}
.nav-more:hover { background: var(--vp-c-bg-soft); }

/* VPNavBarTranslations is hidden below 1280px by its own scoped style.
   On desktop we force it visible alongside the menu. */
.nav-lang :deep(.VPNavBarTranslations) { display: flex !important; align-items: center; }
.nav-lang :deep(.VPNavBarTranslations .text) { color: var(--vp-c-text-2); }
.nav-lang :deep(.VPNavBarTranslations:hover .text) { color: var(--vp-c-text-1); }

/* ── Mobile panel ───────────────────────────────────────────── */
.nav-panel {
  position: absolute;
  top: 100%; left: 0; right: 0;
  background: var(--ah-navbar-bg);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  border-bottom: 1px solid var(--vp-c-divider);
  box-shadow: 0 12px 24px rgba(0, 0, 0, 0.08);
}
.nav-panel-inner {
  max-width: 1200px;
  margin: 0 auto;
  padding: 12px 20px 20px;
}
.panel-nav {
  list-style: none;
  margin: 0 0 12px;
  padding: 0;
  display: flex;
  flex-direction: column;
}
.panel-nav .panel-link {
  display: block;
  padding: 12px 4px;
  font-size: 16px;
  font-weight: 600;
  color: var(--vp-c-text-1);
  text-decoration: none;
  border-bottom: 1px solid var(--vp-c-divider);
}
.panel-nav .panel-link:hover { color: var(--vp-c-brand-1); }

.panel-langs {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 8px;
  padding-top: 8px;
}
.panel-langs-title {
  width: 100%;
  font-size: 12px;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--vp-c-text-3);
  margin-bottom: 4px;
}
.panel-lang {
  padding: 6px 14px;
  border: 1px solid var(--vp-c-divider);
  border-radius: 999px;
  font-size: 14px;
  color: var(--vp-c-text-2);
  text-decoration: none;
  transition: 0.15s;
}
.panel-lang:hover { color: var(--vp-c-text-1); border-color: var(--vp-c-brand-1); }
.panel-lang.active {
  background: var(--vp-c-brand-1);
  color: #fff;
  border-color: var(--vp-c-brand-1);
}

.panel-social-link {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  margin-top: 14px;
  padding: 6px 4px;
  font-size: 15px;
  font-weight: 600;
  color: var(--vp-c-text-2);
  text-decoration: none;
}
.panel-social-link:hover { color: var(--vp-c-text-1); }

.panel-enter-active, .panel-leave-active { transition: opacity 0.18s ease, transform 0.18s ease; }
.panel-enter-from, .panel-leave-to { opacity: 0; transform: translateY(-8px); }

/* ── Breakpoints ────────────────────────────────────────────── */
@media (max-width: 767px) {
  /* The theme switch lives inside .nav-inline now — keep it visible on
     mobile, hide every other desktop-only group. */
  .nav-inline .nav-menu,
  .nav-inline .nav-lang,
  .nav-inline .nav-social,
  .nav-inline .nav-divider { display: none !important; }
  .nav-more { display: inline-flex; }
}
@media (min-width: 768px) {
  /* Never show the mobile panel on desktop */
  .nav-panel { display: none !important; }
}

/* Hide brand text on very small screens — only show the logo image */
@media (max-width: 480px) {
  .nav-container { padding: 0 12px; height: 56px; }
  .brand-text { display: none; }
  .brand-logo { height: 28px; }
  .nav-right { gap: 4px; }
}
</style>
