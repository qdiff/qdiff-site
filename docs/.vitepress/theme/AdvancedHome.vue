<template>
  <div class="advanced-home">
    <!-- Shared navigation (brand + menu + i18n switcher + appearance) -->
    <SiteNav :id="lang"/>

    <!-- Hero Section -->
    <section class="hero-section">
      <div class="hero-container">
        <div class="hero-content">
          <div class="hero-text">
            <h1 class="hero-title">{{ data.hero.name }}</h1>
            <p class="hero-subtitle">{{ data.hero.text }}</p>
            <p class="hero-description">{{ data.hero.tagline }}</p>
            <div class="hero-actions">
              <HomeActions />
            </div>
          </div>
          <div class="hero-visual">
            <!-- <div class="floating-elements">
              <div v-for="(card, i) in content.floatingCards" :key="i"
                   class="floating-card" :class="`card-${i + 1}`">
                <div class="card-icon">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <component :is="floatingIcons[i]" />
                  </svg>
                </div>
                <div class="card-text">{{ card }}</div>
              </div>
            </div> -->
            <div class="hero-image">
              <img :src="withBase(data.hero.image.src)" :alt="data.hero.image.alt" />
            </div>
          </div>
        </div>
      </div>
      <div class="hero-bg-pattern"></div>
    </section>

    <!-- Features Section -->
    <section class="features-section" id="features">
      <div class="features-container">
        <div class="section-header">
          <h2 class="section-title">{{ content.sections.featuresTitle }}</h2>
          <p class="section-subtitle">{{ content.sections.featuresSubtitle }}</p>
        </div>
        <div class="features-grid">
          <div v-for="(feature, index) in data.features" :key="feature.title"
               class="feature-card"
               :style="{ animationDelay: `${index * 0.1}s` }">
            <div class="feature-icon" :style="{ backgroundColor: featureColors[index % featureColors.length] }">
              <img :src="withBase(feature.icon.light)" :alt="feature.icon.alt"
                   :width="feature.icon.width" :height="feature.icon.height" />
            </div>
            <h3 class="feature-title">{{ feature.title }}</h3>
            <p class="feature-description">{{ feature.details }}</p>
            <a v-if="feature.link" :href="link(feature.link)" class="feature-link">{{ feature.linkText }}</a>
          </div>
        </div>
      </div>
    </section>

    <!-- Action Categories Section -->
    <section class="formats-section">
      <div class="formats-container">
        <div class="section-header">
          <h2 class="section-title">{{ content.sections.categoriesTitle }}</h2>
          <p class="section-subtitle">{{ content.sections.categoriesSubtitle }}</p>
        </div>
        <div class="formats-grid">
          <a class="format-card" v-for="cat in categories" :key="cat.name" :href="cat.link">
            <div class="format-icon" :style="{ backgroundColor: cat.color }">
              <span class="format-ext">{{ cat.badge }}</span>
            </div>
            <div class="format-info">
              <h3 class="format-name">{{ cat.name }}</h3>
              <p class="format-desc">{{ cat.desc }}</p>
            </div>
          </a>
        </div>
        <div class="formats-cta">
          <a :href="link('/guide/download')" class="btn btn-primary">{{ content.categoriesCta }}</a>
        </div>
      </div>
    </section>

    <!-- How It Works Section -->
    <section class="how-section">
      <div class="how-container">
        <div class="section-header">
          <h2 class="section-title">{{ content.sections.howTitle }}</h2>
          <p class="section-subtitle">{{ content.sections.howSubtitle }}</p>
        </div>
        <div class="steps-grid">
          <div class="step-card" v-for="(step, index) in content.steps" :key="index">
            <div class="step-number">{{ step.num }}</div>
            <h3 class="step-title">{{ step.title }}</h3>
            <p class="step-desc">{{ step.desc }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- FAQ Section -->
    <section class="faq-section">
      <div class="faq-container">
        <div class="section-header">
          <h2 class="section-title">{{ content.sections.faqTitle }}</h2>
          <p class="section-subtitle">{{ content.sections.faqSubtitle }}</p>
        </div>
        <div class="faq-grid">
          <div v-for="faq in content.faqs" :key="faq.question" class="faq-item">
            <details class="faq-details">
              <summary class="faq-question">{{ faq.question }}</summary>
              <div class="faq-answer">{{ faq.answer }}</div>
            </details>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA Section -->
    <section class="cta-section">
      <div class="cta-container">
        <div class="cta-content">
          <h2 class="cta-title">{{ content.cta.title }}</h2>
          <p class="cta-description">{{ content.cta.description }}</p>
          <div class="cta-actions">
            <a :href="localeLink(content.cta.primaryLink, lang)" class="btn btn-primary">{{ content.cta.primary }}</a>
            <a :href="localeLink(content.cta.secondaryLink, lang)" class="btn btn-secondary">{{ content.cta.secondary }}</a>
          </div>
        </div>
      </div>
    </section>

    <!-- Footer -->
    <SiteFooter />
  </div>
</template>

<script setup lang="ts">
import { computed, h } from 'vue'
import { withBase, useData } from 'vitepress'
import HomeActions from './HomeActions.vue'
import SiteNav from './SiteNav.vue'
import SiteFooter from './SiteFooter.vue'
import { localeLink } from './locale'

interface Props {
  data: any
}

const props = defineProps<Props>()

const { lang } = useData()
// All page content now comes from the markdown frontmatter (`data`).
const content = computed(() => props.data || {})

// SVG icon render functions for floating cards
const floatingIcons = [
  () => h('path', { d: 'M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z' }),
  () => h('g', {}, [
    h('polyline', { points: '23 6 13.5 15.5 8.5 10.5 1 18' }),
    h('polyline', { points: '17 6 23 6 23 12' }),
  ]),
  () => h('g', {}, [
    h('rect', { x: '3', y: '11', width: '18', height: '11', rx: '2', ry: '2' }),
    h('path', { d: 'M7 11V7a5 5 0 0 1 10 0v4' }),
  ]),
]

const featureColors = [
  '#3b82f6', // blue — files
  '#20a877', // green — folders
  '#6366f1', // indigo — projects
  '#0ea5e9', // sky — images & archives
  '#f59e0b', // amber — reading changes
  '#14b8a6', // teal — privacy
]

/** Prefix an internal link with the current locale segment. */
function link(path: string): string {
  if (!path) return path
  if (/^https?:\/\//.test(path) || path.startsWith('mailto:') || path.startsWith('#')) return path
  return localeLink(path, lang.value)
}

const categories = computed(() =>
  (content.value.categories || []).map((c: any) => ({
    ...c,
    link: link(c.link || '/guide/introduction'),
  }))
)
</script>

<style scoped>
.advanced-home {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  line-height: 1.6;
  color: var(--vp-c-text-1);
}

/* Navigation styles live in SiteNav.vue */

/* Hero Section */
.hero-section {
  padding: 120px 0 100px;
  background: var(--ah-hero-bg);
  position: relative;
  overflow: hidden;
}

.hero-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

.hero-content {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 80px;
  align-items: center;
}

.hero-text {
  position: relative;
  z-index: 2;
}

.hero-title {
  font-size: 4rem;
  font-weight: 800;
  margin: 0 0 20px;
  line-height: 1.1;
  color: var(--vp-c-text-1);
  background: linear-gradient(135deg, var(--ah-hero-title-from) 0%, var(--ah-hero-title-to) 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.hero-subtitle {
  font-size: 2rem;
  font-weight: 600;
  margin: 0 0 20px;
  color: var(--vp-c-text-1);
  opacity: 0.9;
}

.hero-description {
  font-size: 1.25rem;
  margin: 0 0 40px;
  color: var(--vp-c-text-2);
  line-height: 1.6;
  max-width: 500px;
}

.hero-actions {
  margin-top: 40px;
}

.btn {
  display: inline-flex;
  align-items: center;
  padding: 16px 32px;
  border-radius: 12px;
  text-decoration: none;
  font-weight: 600;
  font-size: 1rem;
  transition: all 0.3s ease;
  cursor: pointer;
  position: relative;
  overflow: hidden;
}

.btn-primary {
  background: linear-gradient(135deg, #4b8dff 0%, #2f6fe4 100%);
  color: #ffffff;
  border: none;
  box-shadow: 0 10px 24px rgba(47, 111, 228, 0.24);
}

.btn-primary:hover {
  background: linear-gradient(135deg, #5a97ff 0%, #2563d9 100%);
  transform: translateY(-2px);
}

.btn-secondary {
  background: rgba(255, 255, 255, 0.15);
  color: #ffffff;
  border: 2px solid rgba(255, 255, 255, 0.7);
}

.btn-secondary:hover {
  background: rgba(255, 255, 255, 0.25);
  border-color: #ffffff;
  transform: translateY(-1px);
}

.hero-visual {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
}

.floating-elements {
  position: absolute;
  width: 100%;
  height: 100%;
}

.floating-card {
  position: absolute;
  background: var(--ah-card-bg);
  padding: 16px 20px;
  border-radius: 12px;
  box-shadow: var(--ah-card-shadow);
  display: flex;
  align-items: center;
  gap: 12px;
  font-size: 14px;
  font-weight: 500;
  animation: float 6s ease-in-out infinite;
}

.card-1 { top: 20%; left: 10%; animation-delay: 0s; }
.card-2 { top: 60%; right: 15%; animation-delay: 2s; }
.card-3 { bottom: 20%; left: 20%; animation-delay: 4s; }

.card-icon {
  font-size: 18px;
  color: var(--vp-c-brand-1);
  display: flex;
  align-items: center;
}

.hero-image {
  position: relative;
  z-index: 1;
}

.hero-image img {
  width: 100%;
  max-width: 700px;
  height: auto;
}

.hero-bg-pattern {
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  background-image:
    radial-gradient(circle at 20% 80%, rgba(59, 130, 246, 0.1) 0%, transparent 50%),
    radial-gradient(circle at 80% 20%, rgba(16, 185, 129, 0.1) 0%, transparent 50%);
  pointer-events: none;
}

/* Features Section */
.features-section {
  padding: 120px 0;
  background: var(--vp-c-bg);
}

.features-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

.section-header {
  text-align: center;
  margin-bottom: 80px;
}

.section-title {
  font-size: 3rem;
  font-weight: 700;
  margin: 0 0 16px;
  color: var(--vp-c-text-1);
}

.section-subtitle {
  font-size: 1.25rem;
  color: var(--vp-c-text-2);
  margin: 0 auto;
  max-width: 600px;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
  gap: 40px;
}

.feature-card {
  background: var(--ah-card-bg);
  padding: 40px 30px;
  border-radius: 20px;
  box-shadow: var(--ah-card-shadow);
  text-align: center;
  transition: all 0.3s ease;
  border: 1px solid var(--vp-c-divider);
  animation: fadeInUp 0.6s ease-out forwards;
  opacity: 0;
  transform: translateY(30px);
}

.feature-card:hover {
  transform: translateY(-8px);
  box-shadow: var(--ah-card-shadow-hover);
  border-color: var(--vp-c-brand-1);
}

.feature-icon {
  width: 72px;
  height: 72px;
  border-radius: 18px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 24px;
  color: white;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
}

.feature-icon img {
  filter: brightness(0) invert(1);
}

.feature-title {
  font-size: 1.5rem;
  font-weight: 600;
  margin: 0 0 16px;
  color: var(--vp-c-text-1);
  line-height: 1.3;
}

.feature-description {
  color: var(--vp-c-text-2);
  line-height: 1.6;
  margin: 0 0 24px;
  font-size: 1rem;
}

.feature-link {
  color: var(--vp-c-text-1);
  text-decoration: none;
  font-weight: 600;
  font-size: 0.95rem;
  transition: color 0.2s;
}

.feature-link:hover {
  color: var(--vp-c-brand-1);
}

/* Formats Preview Section */
.formats-section {
  padding: 120px 0;
  background: var(--vp-c-bg-soft);
}

.formats-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

.formats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 24px;
  margin-bottom: 48px;
}

.format-card {
  background: var(--ah-card-bg);
  border-radius: 20px;
  padding: 32px 24px;
  display: flex;
  align-items: center;
  gap: 20px;
  box-shadow: var(--ah-card-shadow);
  border: 1px solid var(--vp-c-divider);
  transition: all 0.3s ease;
}

.format-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--ah-card-shadow);
  border-color: var(--vp-c-brand-1);
}

.format-icon {
  width: 64px;
  height: 64px;
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  color: white;
  font-weight: 700;
  font-size: 1.1rem;
}

.format-ext {
  font-family: 'SF Mono', 'Fira Code', monospace;
  font-size: 1rem;
  font-weight: 700;
  color: white;
}

.format-info { flex: 1; }

.format-name {
  font-size: 1.2rem;
  font-weight: 600;
  color: var(--vp-c-text-1);
  margin: 0 0 4px;
}

.format-desc {
  font-size: 0.9rem;
  color: var(--vp-c-text-2);
  margin: 0;
  line-height: 1.5;
}

.formats-cta { text-align: center; }

/* How It Works Section */
.how-section {
  padding: 120px 0;
  background: var(--vp-c-bg);
}

.how-container {
  max-width: 1000px;
  margin: 0 auto;
  padding: 0 20px;
}

.steps-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 32px;
}

.step-card {
  text-align: center;
  padding: 40px 24px;
  background: var(--vp-c-bg-soft);
  border-radius: 20px;
  border: 1px solid var(--vp-c-divider);
  transition: all 0.3s ease;
}

.step-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--ah-card-shadow);
}

.step-number {
  font-size: 3rem;
  font-weight: 800;
  color: var(--vp-c-brand-1);
  margin-bottom: 16px;
  line-height: 1;
}

.step-title {
  font-size: 1.3rem;
  font-weight: 600;
  color: var(--vp-c-text-1);
  margin: 0 0 12px;
}

.step-desc {
  font-size: 1rem;
  color: var(--vp-c-text-2);
  margin: 0 auto;
  line-height: 1.6;
  max-width: 280px;
}

/* FAQ Section */
.faq-section {
  padding: 120px 0;
  background: var(--vp-c-bg);
}

.faq-container {
  max-width: 800px;
  margin: 0 auto;
  padding: 0 20px;
}

.faq-grid {
  display: grid;
  gap: 16px;
}

.faq-item {
  background: var(--ah-card-bg);
  border-radius: 12px;
  border: 1px solid var(--vp-c-divider);
  overflow: hidden;
  transition: all 0.2s ease;
}

.faq-item:hover {
  box-shadow: var(--ah-card-shadow);
}

.faq-details { width: 100%; }

.faq-question {
  padding: 24px 30px;
  background: var(--vp-c-bg-soft);
  cursor: pointer;
  font-weight: 600;
  font-size: 1.1rem;
  color: var(--vp-c-text-1);
  border: none;
  outline: none;
  transition: background-color 0.2s;
  text-align: left;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.faq-question:hover { background: var(--ah-faq-hover-bg); }

.faq-question::after {
  content: '+';
  font-size: 18px;
  font-weight: bold;
  transition: transform 0.2s;
}

.faq-details[open] .faq-question::after { transform: rotate(45deg); }

.faq-answer {
  padding: 0 30px 24px;
  color: var(--vp-c-text-2);
  line-height: 1.6;
}

/* CTA Section */
.cta-section {
  padding: 120px 0;
  background: linear-gradient(135deg, rgb(0, 0, 0), rgb(26, 26, 26));
  color: #ffffff;
}

.cta-section .btn-primary {
  background: #ffffff;
  color: #1d4ed8;
  box-shadow: 0 10px 26px rgba(0, 0, 0, 0.18);
}

.cta-section .btn-primary:hover {
  background: #eef4ff;
}

.cta-container {
  max-width: 800px;
  margin: 0 auto;
  padding: 0 20px;
  text-align: center;
}

.cta-title {
  font-size: 3rem;
  font-weight: 700;
  margin: 0 0 20px;
  line-height: 1.2;
}

.cta-description {
  font-size: 1.25rem;
  margin: 0 0 40px;
  opacity: 0.9;
  line-height: 1.6;
}

.cta-actions {
  display: flex;
  justify-content: center;
  gap: 20px;
  flex-wrap: wrap;
}

/* Animations */
@keyframes float {
  0%, 100% { transform: translateY(0px) rotate(0deg); }
  33% { transform: translateY(-10px) rotate(2deg); }
  66% { transform: translateY(5px) rotate(-2deg); }
}

@keyframes fadeInUp {
  to { opacity: 1; transform: translateY(0); }
}

/* Responsive — tablet */
@media (max-width: 1024px) {
  .hero-content {
    grid-template-columns: 1fr;
    gap: 60px;
    text-align: center;
  }

  .hero-title { font-size: 3rem; }
  .hero-subtitle { font-size: 2rem; }
  .features-grid { grid-template-columns: 1fr; }
}

/* Responsive — mobile */
@media (max-width: 768px) {
  .hero-section { padding: 90px 0 60px; }
  .hero-title { font-size: 2.2rem; }
  .hero-subtitle { font-size: 1.6rem; }
  .hero-description { font-size: 1.05rem; }

  .section-title { font-size: 2rem; }
  .section-subtitle { font-size: 1.05rem; }
  .section-header { margin-bottom: 48px; }

  .features-section,
  .formats-section,
  .how-section,
  .faq-section,
  .cta-section {
    padding: 64px 0;
  }

  .feature-card { padding: 32px 20px; }

  .steps-grid { grid-template-columns: 1fr; }

  .cta-title { font-size: 2rem; }
  .cta-description { font-size: 1.05rem; }

  .hero-actions,
  .cta-actions {
    flex-direction: column;
    align-items: center;
  }

  .btn {
    width: 100%;
    max-width: 300px;
    justify-content: center;
  }

  .floating-elements { display: none; }
}

@media (max-width: 480px) {
  .hero-title { font-size: 1.8rem; }
  .hero-subtitle { font-size: 1.3rem; }
  .section-title { font-size: 1.6rem; }
  .cta-title { font-size: 1.6rem; }
  .format-card { padding: 24px 16px; }
  .faq-question { padding: 18px 20px; font-size: 1rem; }
  .faq-answer { padding: 0 20px 20px; }
}
</style>
