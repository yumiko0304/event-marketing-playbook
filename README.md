# 线下活动实操手册

一个面向 Codex 的 skill，用来帮助策划、执行、传播与复盘法律行业的线下或混合活动。

这个 skill 基于《“独一无二”的活动：法律行业市场品牌实战手册》的方法论整理而成，但仓库中存放的是结构化提炼后的 skill 资料，不是书稿原文全文转存。

## 适用场景

- 把一个模糊的活动想法梳理成清晰的活动 brief
- 设计活动主题、议程、嘉宾结构与互动形式
- 拆解活动执行节点、里程碑、风险与分工
- 规划会前、会中、会后的传播节奏
- 设计活动后的关系沉淀、转化与复盘路径
- 用 AI 搭建活动母文档、提示词链路与知识沉淀方式

## Skill 信息

- 内部调用名：`event-ops-playbook`
- 界面显示名：`线下活动实操手册`

示例调用：

```text
使用 $event-ops-playbook 帮我设计、执行并复盘一场法律行业线下活动。
```

## 仓库结构

```text
.
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── manuscript-map.md
│   ├── phase-playbook.md
│   ├── interaction-patterns.md
│   └── ai-growth-ops.md
└── scripts/
    └── search_refs.py
```

## 参考资料说明

- `manuscript-map.md`：书稿章节地图和检索入口
- `phase-playbook.md`：活动全流程策划与执行打法
- `interaction-patterns.md`：适合制造记忆点的互动形式
- `ai-growth-ops.md`：AI 工作流、传播、转化和效果衡量
- `search_refs.py`：关键词检索脚本

## 发布建议

- 如果公开发布，建议在仓库说明中注明：这是基于书稿方法论提炼的 skill，而非书稿原文公开发布。
- 如果书稿尚未正式授权公开传播，优先考虑先发私有仓库。
