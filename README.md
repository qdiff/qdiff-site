# qDiff 官网

qDiff 的官方站点，面向普通用户介绍「把两份文件、两个文件夹或项目里的改动并排看清」这一件事。域名 `qdiff.w3cub.com`，用 VitePress 构建，英文为默认语言，另提供简体中文与繁體中文。

站点内容刻意不谈实现细节：不讲框架、不讲编译、不讲版本库底层，只讲用户会遇到什么问题、怎么点、能得到什么。

## 目录

```
docs/
  index.md                 英文首页（自定义 AdvancedHome 布局）
  zh-CN/  zh-TW/           中文首页 + 各自的使用指南
  guide/                   使用指南（英文）
  privacy/index.md         隐私政策（App Store Connect 必填）
  terms/index.md           使用条款
  .vitepress/config.ts     三语导航、侧栏、页脚、SEO
  .vitepress/theme/        自定义首页、导航、页脚、按钮、品牌样式
  public/                  logo、首页插图、OG 分享图、指南插图、功能图标
scripts/build-assets.py    重新生成全部图片素材
```

## 本地开发

```bash
pnpm install
pnpm docs:dev       # http://localhost:5173
pnpm docs:build     # 产物 docs/.vitepress/dist
pnpm docs:preview   # 预览构建结果
pnpm assets         # 重画 public/ 里的图片（需要 Python + Pillow + rsvg-convert）
```

`docs/.vitepress/theme/site.ts` 是唯一需要按发布状态修改的地方：

| 常量 | 说明 |
| --- | --- |
| `APP_STORE_ID` | Mac App Store 应用 ID，当前 `6825630546` |
| `APP_STORE_URL` | 由 ID 拼出，留空则全站按钮回退到下载指南 |
| `DMG_URL` | 若日后提供官网安装包，填直链即可多出一个下载按钮 |
| `CONTACT_EMAIL` | 支持邮箱，当前 `qdiff@w3cub.com` |

导航、页脚和社交图标里的邮箱在 `docs/.vitepress/config.ts` 里另有一份，改动时两处一起更新。

## 上线

推送到 `main` 会由 `.github/workflows/deploy.yml` 构建并发布到 `gh-pages`，同时写入 `CNAME`（`qdiff.w3cub.com`）。也可以本地跑 `./deploy.sh`。

DNS 需要给 `qdiff.w3cub.com` 加一条指向 GitHub Pages 的 CNAME 记录。

App Store Connect 需要能打开的三个地址，站点里都已备好：

| 用途 | 地址 | 对应文件 |
| --- | --- | --- |
| Marketing URL | `https://qdiff.w3cub.com` | `docs/index.md` |
| Support URL | `https://qdiff.w3cub.com/guide/introduction` | `docs/guide/introduction.md` |
| Privacy Policy URL | `https://qdiff.w3cub.com/privacy` | `docs/privacy/index.md` |

## 内容与素材

- 文案取自产品本身的能力清单：文件/文件夹/项目比较、图片与压缩包比较、按词高亮、同步滚动、分享成图、纯本地、免费可用。
- 图片全部由 `scripts/build-assets.py` 从 SVG 绘制，`logo.png` 来自 qDiff 应用图标；没有引用任何第三方产品的截图或名称。
- 全站不出现其他比较工具的名称，也不出现开发框架、依赖库等技术名词。
