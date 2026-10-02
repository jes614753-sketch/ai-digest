# AI 信息源日报（ai-digest）

每天一份《AI 信息源日报》，内容来自飞书群「RSS 推送」的全天信息（X 博主、aihot 精选、Follow Builders 等），由小蓝虾读取群聊后整合产出，自动发布为静态站点。

- **线上站点**：https://jes614753-sketch.github.io/ai-digest/
- **产出角色**：小蓝虾（整合者，读群 → 写日报 → 更新本仓库）
- **机器人A「RSS 信息源」**：只负责往群里推送原始信息卡片，不参与本项目

## 目录结构

```
data/YYYY-MM-DD.md    # 每天一份日报，小蓝虾唯一需要写的东西
data/index.json       # 自动生成的索引（GitHub Action 维护，不要手改）
index.html            # 站点（自动读取索引渲染，无需改动）
scripts/build_index.py
.github/workflows/sync-index.yml
```

## 小蓝虾每日更新协议

1. 文件名：`data/YYYY-MM-DD.md`，**日期 = 报告内容所属的那一天**（24 点跑的就是刚结束的这一天：10-03 00:00 跑 → 写 `2026-10-02.md`）。
2. 格式（markdown）：
   - 第一行一级标题：`# AI 信息源日报 · YYYY-MM-DD`
   - 第二行引用行写统计：`> 来源：8 位博主 · 共 N 条 ｜ 生成：小蓝虾`
   - 正文按 `##` 分节（建议：模型与产品 / 行业动态 / 论文与技术 / 观点与讨论）
   - 每条注明来源博主和原文链接：`- **博主名**：[标题](原文链接) 一句话要点`
3. 提交：

```bash
git add data/YYYY-MM-DD.md
git commit -m "digest: YYYY-MM-DD"
git push
```

推送后 Action 会自动重建 `data/index.json`，GitHub Pages 自动部署，约 1 分钟后站点更新。

## 给小蓝虾的定时指令（粘贴到小蓝虾的每日任务）

```
每天 24:00 执行「AI 信息源日报更新」：
1. 读取飞书群「RSS 推送」今天的全部推送卡片与讨论（以用户身份）。
2. 整理成日报 markdown：
   第一行 "# AI 信息源日报 · D"，D=刚结束的这一天（10-03 00:00 跑就是 2026-10-02），
   第二行 "> 来源：N 位博主 · 共 M 条 ｜ 生成：小蓝虾"，
   正文按 "##" 分节（模型与产品/行业动态/论文与技术/观点与讨论），
   每条格式 "- **博主名**：[标题](原文链接) 一句话要点"。
3. 保存为 C:\Users\17551\Documents\ai-digest\data\D.md
   （首次运行先确认该目录已是 ai-digest 仓库且 git pull 过；不要手改 index.json，Action 会自动重建）。
4. cd C:\Users\17551\Documents\ai-digest && git add data/今天日期.md
   && git commit -m "digest: 今天日期" && git push。
5. 推送成功后在群里发一行确认：✅ 今日 AI 信息源日报已发布到站点。
```

> 注意：小蓝虾所在机器需要对该仓库有 push 权限（本机 gh 已登录 jes614753-sketch；其他机器需配置 token）。git 代理需为 http://127.0.0.1:7891（7890 已失效）。

## 本地预览

GitHub Pages 不支持 file:// 直接打开，本地看效果：

```bash
cd ai-digest && python -m http.server 8089
# 打开 http://127.0.0.1:8089
```
