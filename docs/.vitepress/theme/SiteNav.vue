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
        <!-- Desktop: inline nav menu + language switcher -->
        <div class="nav-inline">
          <VPNavBarMenu />
          <VPNavBarTranslations class="nav-lang" />
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

        <!-- Theme toggle is always visible -->
        <VPSwitchAppearance class="nav-appearance" />
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
import VPSwitchAppearance from 'vitepress/dist/client/theme-default/components/VPSwitchAppearance.vue'
// localeLink no longer needed — nav links are already prefixed in config.ts

const { lang, theme, site } = useData()
const route = useRoute()

const menuOpen = ref(false)
const navEl = ref<HTMLElement | null>(null)

// Locale-aware home link for the brand logo
const homeLink = computed(() =>
  !lang.value || lang.value === 'en' ? '/' : `/${lang.value}/`
)

// Current locale's nav items (each has text + link).
// Links in theme.nav are already locale-prefixed by config.ts (tc()),
// so we use them as-is — no extra localeLink() wrapping.
const navItems = computed(() =>
  (theme.value.nav || []).map((item: any) => ({
    text: item.text,
    link: item.link,
  }))
)

const langMenuLabel = computed(() => theme.value.langMenuLabel || 'Language')

const currentLang = computed(() => {
  const l = site.value.locales[lang.value]
  return { label: (l && l.label) || 'English' }
})

// Build the language list from the configured locales, keeping the user on the
// same relative path when they switch language.
function stripLangPrefix(p: string): string {
  const m = p.match(/^\/(zh-CN|zh-TW)(\/.*)?$/)
  return m ? (m[2] || '/') : p
}
const localeLinks = computed(() => {
  const locales = site.value.locales || {}
  const base = stripLangPrefix(route.path)
  return Object.entries(locales)
    .filter(([key]) => key !== lang.value)
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
.nav-inline { display: flex; align-items: center; gap: 20px; }
.nav-appearance { display: flex; align-items: center; }

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

.panel-enter-active, .panel-leave-active { transition: opacity 0.18s ease, transform 0.18s ease; }
.panel-enter-from, .panel-leave-to { opacity: 0; transform: translateY(-8px); }

/* ── Breakpoints ────────────────────────────────────────────── */
@media (max-width: 767px) {
  .nav-inline { display: none; }
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
