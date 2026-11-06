<template>
  <footer class="footer">
    <div class="footer-container">
      <div class="footer-content">
        <div class="footer-brand">
          <div class="footer-logo">{{ siteTitle }}</div>
          <p class="footer-tagline">{{ footer?.message }}</p>
        </div>
        <div class="footer-links" v-if="footer?.items?.length">
          <div class="footer-column" v-for="col in footer.items" :key="col.text">
            <h4 class="footer-heading">{{ col.text }}</h4>
            <a
              v-for="item in col.items"
              :key="item.link"
              :href="item.link"
              class="footer-link"
            >{{ item.text }}</a>
          </div>
        </div>
      </div>
      <div class="footer-bottom" v-if="footer?.copyright">
        <p class="footer-copyright">{{ footer.copyright }}</p>
      </div>
    </div>
  </footer>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useData } from 'vitepress'

const { theme } = useData()
const siteTitle = computed(() => theme.value.siteTitle ?? 'qDiff')

interface FooterItem { text: string; link: string }
interface FooterGroup { text: string; items: FooterItem[] }
interface FooterConfig {
  message?: string
  copyright?: string
  items?: FooterGroup[]
}

const footer = computed<FooterConfig | undefined>(
  () => theme.value.footer as FooterConfig | undefined
)
</script>

<style scoped>
.footer {
  background: #142033;
  color: #ffffff;
  padding: 80px 0 40px;
}

.footer-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

.footer-content {
  display: grid;
  grid-template-columns: 1fr 3fr;
  gap: 80px;
  margin-bottom: 40px;
}

.footer-brand .footer-logo {
  font-size: 24px;
  font-weight: 700;
  margin-bottom: 12px;
  color: #ffffff;
}

.footer-tagline {
  color: #cccccc;
  margin: 0;
  font-size: 1rem;
}

.footer-links {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 40px;
}

.footer-heading {
  font-size: 1.1rem;
  font-weight: 600;
  margin: 0 0 20px;
  color: #ffffff;
}

.footer-link {
  display: block;
  color: #cccccc;
  text-decoration: none;
  margin-bottom: 12px;
  transition: color 0.2s;
}

.footer-link:hover {
  color: #ffffff;
}

.footer-bottom {
  border-top: 1px solid #333333;
  padding-top: 40px;
  text-align: center;
}

.footer-copyright {
  margin: 0;
  color: #999999;
  font-size: 0.9rem;
}

@media (max-width: 1024px) {
  .footer-content {
    grid-template-columns: 1fr;
    gap: 40px;
  }
}

@media (max-width: 768px) {
  .footer {
    padding: 60px 0 30px;
  }

  .footer-content {
    gap: 32px;
  }

  .footer-links {
    grid-template-columns: 1fr 1fr;
    gap: 28px;
  }
}

@media (max-width: 480px) {
  .footer-links {
    grid-template-columns: 1fr;
    gap: 24px;
  }
}
</style>
