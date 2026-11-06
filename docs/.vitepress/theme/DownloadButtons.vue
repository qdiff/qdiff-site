<script setup lang="ts">
import { computed } from 'vue'
import { useData, withBase } from 'vitepress'
import { APP_STORE_URL, DMG_URL, mailto } from './site'
import { resolveLang } from './locale'

const { lang } = useData()
const L = computed(() => resolveLang(lang.value))

const COPY = {
  en: {
    store: 'Download on the Mac App Store',
    dmg: 'Download the macOS installer',
    pendingTitle: 'The Mac App Store release is on its way',
    pendingBody: 'Want to try it earlier? Send us a note and we will let you know as soon as a build is available.',
    email: 'Ask for a preview',
    hint: 'Free to use, with an optional one-time purchase. No account, no subscription.',
    subject: 'qDiff preview build',
  },
  'zh-CN': {
    store: '从 Mac App Store 下载',
    dmg: '下载 macOS 安装包',
    pendingTitle: 'Mac App Store 版本正在准备中',
    pendingBody: '想提前体验？给我们写封邮件，可用时我们会第一时间告诉你。',
    email: '联系我们获取测试版',
    hint: '免费使用全部功能，另有一次性的可选购买。不需要账号，也没有订阅。',
    subject: 'qDiff 测试版',
  },
  'zh-TW': {
    store: '從 Mac App Store 下載',
    dmg: '下載 macOS 安裝包',
    pendingTitle: 'Mac App Store 版本正在準備中',
    pendingBody: '想提前體驗？寫封信給我們，可用時我們會第一時間通知你。',
    email: '聯絡我們取得測試版',
    hint: '免費使用全部功能，另有一次性的選購項目。不需要帳號，也沒有訂閱。',
    subject: 'qDiff 測試版',
  },
}

const copy = computed(() => COPY[L.value])
const ready = computed(() => Boolean(APP_STORE_URL || DMG_URL))
</script>

<template>
  <div class="download-box">
    <div v-if="ready" class="download-ready">
      <a v-if="APP_STORE_URL" :href="APP_STORE_URL" target="_blank" rel="noopener noreferrer" class="dl-store">
        <img :src="withBase('/badges/Mac-App-Store.png')" :alt="copy.store" class="store-badge" width="195" height="46" />
      </a>
      <a v-if="DMG_URL" :href="DMG_URL" class="dl-btn" :class="{ 'dl-primary': !APP_STORE_URL, 'dl-secondary': APP_STORE_URL }">{{ copy.dmg }}</a>
    </div>
    <div v-else class="download-pending">
      <div class="pending-mark" aria-hidden="true">
        <svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
          <rect x="3" y="4" width="18" height="16" rx="3" />
          <path d="M8 9h8M8 13h5" />
          <circle cx="17" cy="16" r="2.4" />
        </svg>
      </div>
      <div class="pending-copy">
        <strong>{{ copy.pendingTitle }}</strong>
        <p>{{ copy.pendingBody }}</p>
      </div>
      <a :href="mailto(copy.subject)" class="dl-btn dl-primary">{{ copy.email }}</a>
    </div>
    <p class="dl-hint">{{ copy.hint }}</p>
  </div>
</template>

<style scoped>
.download-box {
  margin: 28px 0 32px;
  padding: 28px;
  border: 1px solid var(--vp-c-divider);
  border-radius: 18px;
  background: var(--vp-c-bg-soft);
}

.download-ready,
.download-pending {
  display: flex;
  align-items: center;
  gap: 20px;
  flex-wrap: wrap;
}

.pending-mark {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 52px;
  height: 52px;
  flex-shrink: 0;
  border-radius: 14px;
  color: #ffffff;
  background: linear-gradient(135deg, #4b8dff, #2f6fe4);
}

.pending-copy { flex: 1; min-width: 220px; }
.pending-copy strong { font-size: 1.05rem; color: var(--vp-c-text-1); }
.pending-copy p { margin: 6px 0 0; font-size: 0.93rem; color: var(--vp-c-text-2); line-height: 1.6; }

.dl-store {
  display: inline-flex;
  border-radius: 10px;
  transition: opacity 0.2s ease, transform 0.2s ease;
}

.dl-store:hover {
  opacity: 0.82;
  transform: translateY(-2px);
}

.dl-store img {
  display: block;
  height: 50px;
  width: auto;
  border-radius: 8px;
}

.dl-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 46px;
  padding: 0 22px;
  border-radius: 11px;
  font-weight: 650;
  font-size: 0.95rem;
  text-decoration: none;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.dl-btn:hover { transform: translateY(-2px); }

.dl-primary {
  color: #ffffff;
  background: linear-gradient(135deg, #4b8dff, #2f6fe4);
  box-shadow: 0 8px 20px rgba(47, 111, 228, 0.24);
}

.dl-secondary {
  color: var(--vp-c-text-1);
  border: 1.5px solid var(--vp-c-divider);
}

.dl-hint {
  margin: 18px 0 0;
  font-size: 0.87rem;
  color: var(--vp-c-text-2);
}
</style>
