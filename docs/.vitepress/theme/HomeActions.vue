<script setup lang="ts">
import { computed } from 'vue'
import { useData, withBase } from 'vitepress'
import { APP_STORE_URL, DOWNLOAD_PATH, INTRO_PATH } from './site'
import { localeLink, resolveLang } from './locale'

const { lang } = useData()
const L = computed(() => resolveLang(lang.value))

const COPY = {
  en: {
    primary: 'Get qDiff',
    primaryStore: 'Download on the Mac App Store',
    secondary: 'See how it works',
    note: 'macOS 12 or later · Free to use · No account needed',
  },
  'zh-CN': {
    primary: '获取 qDiff',
    primaryStore: '从 Mac App Store 下载',
    secondary: '看看怎么用',
    note: 'macOS 12 或更新 · 免费使用 · 无需账号',
  },
  'zh-TW': {
    primary: '取得 qDiff',
    primaryStore: '從 Mac App Store 下載',
    secondary: '看看怎麼用',
    note: 'macOS 12 或更新 · 免費使用 · 不需要帳號',
  },
}

const copy = computed(() => COPY[L.value])
const primaryHref = computed(() => APP_STORE_URL || localeLink(DOWNLOAD_PATH, L.value))
const secondaryHref = computed(() => localeLink(INTRO_PATH, L.value))
const external = computed(() => Boolean(APP_STORE_URL))
</script>

<template>
  <div class="home-actions">
    <div class="home-action-row">
      <a
        v-if="external"
        :href="primaryHref"
        class="action-store"
        target="_blank"
        rel="noopener noreferrer"
      >
        <img
          :src="withBase('/badges/Mac-App-Store.png')"
          :alt="copy.primaryStore"
          class="store-badge"
          width="195"
          height="46"
        />
      </a>
      <a v-else :href="primaryHref" class="action-primary">{{ copy.primary }}</a>
      <a :href="secondaryHref" class="action-secondary">{{ copy.secondary }}</a>
    </div>
    <p class="action-note">{{ copy.note }}</p>
  </div>
</template>

<style scoped>
.home-actions {
  margin-top: 8px;
}

.home-action-row {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 14px;
}

.action-primary,
.action-secondary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  height: 52px;
  padding: 0 28px;
  border-radius: 12px;
  font-size: 1rem;
  font-weight: 650;
  text-decoration: none;
  transition: transform 0.2s ease, box-shadow 0.2s ease, background 0.2s ease;
}

.action-store {
  display: inline-flex;
  border-radius: 10px;
  transition: opacity 0.2s ease, transform 0.2s ease;
}

.action-store:hover {
  opacity: 0.82;
  transform: translateY(-2px);
}

.action-store img {
  display: block;
  height: 50px;
  width: auto;
  border-radius: 8px;
}

.action-primary {
  background: linear-gradient(135deg, #4b8dff 0%, #2f6fe4 100%);
  color: #ffffff;
  box-shadow: 0 10px 24px rgba(47, 111, 228, 0.28);
}

.action-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 14px 30px rgba(47, 111, 228, 0.34);
}

.action-secondary {
  background: transparent;
  color: var(--vp-c-text-1);
  border: 1.5px solid var(--vp-c-divider);
}

.action-secondary:hover {
  transform: translateY(-2px);
  border-color: var(--vp-c-brand-1);
  color: var(--vp-c-brand-1);
}

.action-note {
  margin: 16px 0 0;
  font-size: 0.9rem;
  color: var(--vp-c-text-2);
}

@media (max-width: 768px) {
  .home-action-row { flex-direction: column; align-items: flex-start; }
  .action-primary, .action-secondary { width: 100%; max-width: 320px; }
}
</style>
