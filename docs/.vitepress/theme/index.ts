import DefaultTheme from 'vitepress/theme'
import { h, defineComponent } from 'vue'
import { useRoute, useData } from 'vitepress'
import AdvancedHome from './AdvancedHome.vue'
import HomeActions from './HomeActions.vue'
import DownloadButtons from './DownloadButtons.vue'
import { SUPPORTED_LANGS } from './locale'
import './custom.css'

// Every non-English locale has a custom homepage at /<lang>/. Derive the
// matcher from SUPPORTED_LANGS so adding a language never needs a regex edit.
const HOME_PATH = new RegExp(
  `^\\/(${SUPPORTED_LANGS.filter((l) => l !== 'en').join('|')})\\/?$`
)

export default {
  extends: DefaultTheme,
  enhanceApp({ app }: { app: any }) {
    app.component('DownloadButtons', DownloadButtons)
  },
  // NOTE: Layout MUST be a stateful component (defineComponent), NOT a bare
  // function. A bare function is a *functional* component rendered inline inside
  // VitePressApp's render effect — and VitePressApp renders `() => h(Theme.Layout)`
  // exactly once (it has no reactive deps of its own), so a functional Layout
  // never re-runs on client-side navigation. That made the homepage
  // swap the URL but never re-render with the new locale's frontmatter.
  //
  // A stateful component has its OWN reactive render effect. Reading route.path
  // and frontmatter.value inside the returned render function makes it re-render
  // on every navigation (exactly like VitePress' default Layout.vue), so the
  // correct localized page data flows into AdvancedHome / MarketplaceView.
  Layout: defineComponent({
    name: 'QDiffLayout',
    setup() {
      const route = useRoute()
      const { frontmatter } = useData()

      // Reactive getters (called inside the render below so Vue tracks route.path).
      const isHomePage = () =>
        route.path === '/' || HOME_PATH.test(route.path)

      return () => {
        if (isHomePage()) {
          // `:key` forces a clean remount per URL, exactly like <Content>
          // swapping route.component — guarantees no stale locale state.
          return h(AdvancedHome, { data: frontmatter.value, key: route.path })
        }

        return h(
          DefaultTheme.Layout,
          {},
          { 'home-hero-info-after': () => h(HomeActions) }
        )
      }
    },
  }),
}
