# 系统开发工具基础 - 执行表

## 远程服务器信息

- **Host:** 192.168.79.130
- **Username:** joe
- **Password:** Zyj@070505

## 目录结构

```
G:\CSProjects\SystemToolBaiscLesson\
├── ReportSource\          # 实验报告源文件（.md）
├── Report\                # 渲染后的PDF报告
├── Scripts\               # 脚本文件
│   ├── q01\              # 第1题脚本
│   ├── q02\              # 第2题脚本
│   └── ...
└── 执行表.md             # 本文档
```

## 实验报告书写流程

1. 请先阅读 `ReportTemplate.md` ，这是实验报告模板，再去以此书写实验报告
2. 写完md版实验报告后请阅读 `md-to-pdf-guide.md` ，里面记录了md转pdf文件的方法，将其转为pdf并放入Report文件夹中
3. **必须将md文件转换为PDF**：每完成一道题目或课后练习后，必须使用 `md2pdf` 命令将实验报告转换为PDF格式，并保存到 `Report/` 目录下

## 执行流程

### 第1周（2026年8月24日）

#### 第1题：含空格文件名的批量整理

**任务：** Shell基础与文件系统

**执行步骤：**
1. 连接远程服务器：`ssh joe@192.168.79.130`
2. 创建目录结构和文件
3. 执行文件操作命令
4. 记录命令和输出
5. 提交git：`git add . && git commit -m "完成第1题"`

**需要创建的文件：**
- `Scripts/q01/batch_organize.sh` - 批量整理脚本
- `ReportSource/实验报告_第1题.md` - 实验报告

---

#### 第2题：随机访问日志统计

**任务：** Shell管道与文本处理

**执行步骤：**
1. 创建access.csv文件
2. 编写analyze.sh脚本
3. 测试脚本功能
4. 记录命令和输出
5. 提交git：`git add . && git commit -m "完成第2题"`

**需要创建的文件：**
- `Scripts/q02/analyze.sh` - 分析脚本
- `ReportSource/实验报告_第2题.md` - 实验报告

---

#### 第3题：制造、解决并解释一次合并冲突

**任务：** Version Control and Git

**执行步骤：**
1. 初始化Git仓库
2. 创建分支和文件
3. 制造合并冲突
4. 解决冲突并提交
5. 记录命令和输出
6. 提交git：`git add . && git commit -m "完成第3题"`

**需要创建的文件：**
- `Scripts/q03/git_workflow.sh` - Git工作流脚本
- `ReportSource/实验报告_第3题.md` - 实验报告

---

#### 第4题：修复并构建一页技术说明

**任务：** LaTeX文档编辑

**执行步骤：**
1. 创建report.tex文件
2. 添加公式、表格和引用
3. 使用latexmk构建PDF
4. 验证PDF输出
5. 记录命令和输出
6. 提交git：`git add . && git commit -m "完成第4题"`

**需要创建的文件：**
- `Scripts/q04/report.tex` - LaTeX源文件
- `ReportSource/实验报告_第4题.md` - 实验报告

---

### 课后练习1（完成第1-4题后）

**要求：** 完成practice.md中"课程概览 + Shell 入门"章节的10个练习（不可与其他课后练习重复）

**选择的练习题：**
1. 练习1 - 确认当前Shell环境
2. 练习2 - ls -l命令详解
3. 练习3 - Glob模式匹配
4. 练习4 - 引号类型与特殊字符
5. 练习5 - 标准流与重定向
6. 练习6 - 退出状态与条件执行
7. 练习7 - cd内建命令原理
8. 练习8 - 条件表达式脚本
9. 练习9 - 文件权限与执行
10. 练习10 - set -x调试

**执行步骤：**
1. 阅读practice.md中第1章节的练习题
2. 选择10个练习完成
3. 记录执行的命令和输出结果
4. 编写实验报告
5. 提交git：`git add . && git commit -m "完成课后练习1"`

**需要创建的文件：**
- `ReportSource/实验报告_课后练习1.md` - 实验报告

---

### 第2周（2026年8月31日）

#### 第5题：控制一个可清理的后台任务

**任务：** 命令行环境：进程、信号与任务控制

**执行步骤：**
1. 创建worker.sh脚本
2. 前台启动任务
3. 使用Ctrl-Z挂起任务
4. 使用bg后台运行
5. 发送SIGTERM信号
6. 验证cleanup.log
7. 记录命令和输出
8. 提交git：`git add . && git commit -m "完成第5题"`

**需要创建的文件：**
- `Scripts/q05/worker.sh` - 工作进程脚本
- `ReportSource/实验报告_第5题.md` - 实验报告

---

#### 第6题：语义重构与本地开发反馈

**任务：** 开发环境与工具

**执行步骤：**
1. 创建三个Python文件
2. 配置Python语言服务器
3. 演示跳转到定义和查找引用
4. 使用重命名符号功能
5. 使用ruff检查代码
6. 运行pytest测试
7. 记录命令和输出
8. 提交git：`git add . && git commit -m "完成第6题"`

**需要创建的文件：**
- `Scripts/q06/math_utils.py` - 数学工具模块
- `Scripts/q06/app.py` - 应用程序
- `Scripts/q06/test_math_utils.py` - 测试文件
- `ReportSource/实验报告_第6题.md` - 实验报告

---

#### 第7题：用调试器定位归并排序缺陷

**任务：** Debugging

**执行步骤：**
1. 创建merge_sort.py文件
2. 运行程序确认错误
3. 使用调试器设置断点
4. 观察变量值
5. 修复缺陷
6. 添加测试用例
7. 记录命令和输出
8. 提交git：`git add . && git commit -m "完成第7题"`

**需要创建的文件：**
- `Scripts/q07/merge_sort.py` - 归并排序脚本
- `Scripts/q07/test_merge_sort.py` - 测试文件
- `ReportSource/实验报告_第7题.md` - 实验报告

---

#### 第8题：先测量，再优化慢速词频程序

**任务：** Profiling

**执行步骤：**
1. 创建generate_words.py和wordfreq.py
2. 生成words.txt
3. 运行原程序记录耗时
4. 使用cProfile分析性能
5. 优化程序
6. 比较优化前后性能
7. 记录命令和输出
8. 提交git：`git add . && git commit -m "完成第8题"`

**需要创建的文件：**
- `Scripts/q08/generate_words.py` - 生成词表脚本
- `Scripts/q08/wordfreq.py` - 词频统计脚本
- `ReportSource/实验报告_第8题.md` - 实验报告

---

### 课后练习2（完成第5-8题后）

**要求：** 完成practice.md中"命令行环境"章节的10个练习（不可与其他课后练习重复）

**选择的练习题：**
1. 参数与Globs - 练习1（--参数）
2. 参数与Globs - 练习2（ls高级选项）
3. 参数与Globs - 练习3（进程替换）
4. 环境变量 - 练习1（marco/polo函数）
5. 返回码 - 练习1（失败重试脚本）
6. 信号与任务控制 - 练习1（sleep/pgrep/pkill）
7. 信号与任务控制 - 练习2（wait/pidwait函数）
8. 文件与权限 - 练习1（递归查找最近修改文件）
9. 终端复用器 - 练习1（tmux基础）
10. Aliases与Dotfiles - 练习1（dc别名）

**执行步骤：**
1. 阅读practice.md中第2章节的练习题
2. 选择10个练习完成
3. 记录执行的命令和输出结果
4. 编写实验报告
5. 提交git：`git add . && git commit -m "完成课后练习2"`

**需要创建的文件：**
- `ReportSource/实验报告_课后练习2.md` - 实验报告

---

### 第3周（2026年9月7日）

#### 第9题：从源码构建并在干净环境安装Wheel

**任务：** Packaging and Shipping Code

**执行步骤：**
1. 创建Python包结构
2. 编写pyproject.toml
3. 构建wheel包
4. 创建虚拟环境
5. 安装wheel包
6. 测试命令行工具
7. 记录命令和输出
8. 提交git：`git add . && git commit -m "完成第9题"`

**需要创建的文件：**
- `Scripts/q09/src/greetlab/__init__.py` - 包初始化
- `Scripts/q09/src/greetlab/cli.py` - 命令行接口
- `Scripts/q09/pyproject.toml` - 项目配置
- `ReportSource/实验报告_第9题.md` - 实验报告

---

#### 第10题：让编程智能体进入可验证的修复循环

**任务：** 智能体编程

**执行步骤：**
1. 复制q09为q10
2. 添加失败测试
3. 运行测试确认失败
4. 使用编程智能体修复
5. 人工检查diff
6. 运行测试验证
7. 记录ai_log.md
8. 记录命令和输出
9. 提交git：`git add . && git commit -m "完成第10题"`

**需要创建的文件：**
- `Scripts/q10/ai_log.md` - 智能体日志
- `ReportSource/实验报告_第10题.md` - 实验报告

---

#### 第11题：把"无法处理"的协作材料改成可执行信息

**任务：** 不止于代码

**执行步骤：**
1. 分析给定的协作材料
2. 重写Issue描述
3. 重写提交信息
4. 重写评审意见
5. 编写communication.md
6. 记录命令和输出
7. 提交git：`git add . && git commit -m "完成第11题"`

**需要创建的文件：**
- `Scripts/q11/communication.md` - 协作文档
- `ReportSource/实验报告_第11题.md` - 实验报告

---

#### 第12题：修复一个可复现的线性回归训练循环

**任务：** Python与PyTorch

**执行步骤：**
1. 创建train.py文件
2. 补全训练循环
3. 运行训练程序
4. 验证损失值
5. 记录命令和输出
6. 提交git：`git add . && git commit -m "完成第12题"`

**需要创建的文件：**
- `Scripts/q12/train.py` - 训练脚本
- `ReportSource/实验报告_第12题.md` - 实验报告

---

### 课后练习3（完成第9-12题后）

**要求：** 完成practice.md中"开发环境与工具"和"Debugging and Profiling"章节的10个练习（不可与其他课后练习重复）

**选择的练习题：**
1. 开发环境与工具 - 练习1（Vim模式）
2. 开发环境与工具 - 练习2（VimGolf）
3. 开发环境与工具 - 练习3（IDE语言服务器配置）
4. 开发环境与工具 - 练习4（IDE扩展安装）
5. 调试 - 练习1（归并排序调试）
6. 调试 - 练习4（strace系统调用跟踪）
7. 调试 - 练习5（LLM辅助调试）
8. 性能分析 - 练习1（perf stat）
9. 性能分析 - 练习3（hyperfine基准测试）
10. 性能分析 - 练习5（端口占用排查）

**执行步骤：**
1. 阅读practice.md中第3-4章节的练习题
2. 选择10个练习完成
3. 记录执行的命令和输出结果
4. 编写实验报告
5. 提交git：`git add . && git commit -m "完成课后练习3"`

**需要创建的文件：**
- `ReportSource/实验报告_课后练习3.md` - 实验报告

---

### 第4周（2026年9月14日）

#### 第13题：建立可执行的本地质量门禁

**任务：** 代码质量

**执行步骤：**
1. 复制q10为q13
2. 配置ruff和pytest
3. 添加测试用例
4. 运行代码质量检查
5. 编写check.sh脚本
6. 验证所有检查通过
7. 记录命令和输出
8. 提交git：`git add . && git commit -m "完成第13题"`

**需要创建的文件：**
- `Scripts/q13/check.sh` - 质量检查脚本
- `ReportSource/实验报告_第13题.md` - 实验报告

---

#### 第14题：让Make只重建真正受影响的产物

**任务：** 元编程：构建系统

**执行步骤：**
1. 创建源文件
2. 编写Makefile
3. 测试首次构建
4. 测试增量构建
5. 测试clean目标
6. 记录命令和输出
7. 提交git：`git add . && git commit -m "完成第14题"`

**需要创建的文件：**
- `Scripts/q14/Makefile` - 构建脚本
- `Scripts/q14/data.csv` - 数据文件
- `Scripts/q14/stats.py` - 统计脚本
- `Scripts/q14/build_report.py` - 报告构建脚本
- `Scripts/q14/report.md` - 报告模板
- `ReportSource/实验报告_第14题.md` - 实验报告

---

#### 第15题：把本地API数据转换为可读报告

**任务：** 大杂烩：API、jq、CLI约定与Markdown

**执行步骤：**
1. 创建packages.json
2. 启动本地HTTP服务
3. 使用curl获取数据
4. 使用jq筛选数据
5. 编写api_report.sh脚本
6. 生成summary.md报告
7. 记录命令和输出
8. 提交git：`git add . && git commit -m "完成第15题"`

**需要创建的文件：**
- `Scripts/q15/packages.json` - JSON数据
- `Scripts/q15/api_report.sh` - API报告脚本
- `ReportSource/实验报告_第15题.md` - 实验报告

---

#### 第16题：修复并交付一个陌生的小型工具仓库

**任务：** 课堂综合测试

**执行步骤：**
1. 复制q13为q16
2. 初始化Git仓库
3. 修改问候语实现
4. 运行测试确认失败
5. 定位并修复问题
6. 编写Makefile
7. 构建wheel包
8. 计算SHA-256
9. 提交Git变更
10. 记录命令和输出
11. 提交git：`git add . && git commit -m "完成第16题"`

**需要创建的文件：**
- `Scripts/q16/Makefile` - 构建脚本
- `ReportSource/实验报告_第16题.md` - 实验报告

---

### 课后练习4（完成第13-16题后）

**要求：** 完成practice.md中"Version Control and Git"、"Packaging and Shipping Code"、"智能体编程"、"不止于代码"和"代码质量"章节的10个练习（不可与其他课后练习重复）

**选择的练习题：**
1. Version Control and Git - 练习2（克隆仓库探索历史）
2. Version Control and Git - 练习5（Git别名配置）
3. Version Control and Git - 练习8（合并冲突模拟）
4. Packaging and Shipping Code - 练习1（venv环境对比）
5. Packaging and Shipping Code - 练习2（Python包创建）
6. 智能体编程 - 练习1（不同编程方式对比）
7. 智能体编程 - 练习4（AGENTS.md创建测试）
8. 不止于代码 - 练习2（提交信息质量分析）
9. 代码质量 - 练习1（格式化器+linter配置）
10. 代码质量 - 练习4（正则表达式代码搜索）

**执行步骤：**
1. 阅读practice.md中第5-9章节的练习题
2. 选择10个练习完成
3. 记录执行的命令和输出结果
4. 编写实验报告
5. 提交git：`git add . && git commit -m "完成课后练习4"`

**需要创建的文件：**
- `ReportSource/实验报告_课后练习4.md` - 实验报告

---

## 通用执行命令

### 连接远程服务器
```bash
ssh joe@192.168.79.130
```

### 创建目录结构
```bash
mkdir -p ReportSource Scripts/q01 Scripts/q02 ... Scripts/q16
```

---

## 注意事项

1. 所有操作在远程Ubuntu服务器上执行
2. 每完成一题立即编写实验报告
3. 实验报告只需记录执行的命令和输出结果
4. 脚本文件保存在Scripts/对应题号/目录下
5. PDF报告保存在Report/目录下
6. 保持报告格式一致
7. 记录所有错误和解决方案
8. **每完成一个题目或一次课后练习后提交一次git**

---

## 进度跟踪

| 题号 | 状态 | 完成时间 | 备注 |
|------|------|----------|------|
| 1 | ✅ 已完成 | 2026-08-31 | 含空格文件名的批量整理 |
| 2 | ⏳ 待完成 | | |
| 3 | ⏳ 待完成 | | |
| 4 | ⏳ 待完成 | | |
| 课后练习1 | ⏳ 待完成 | | |
| 5 | ⏳ 待完成 | | |
| 6 | ⏳ 待完成 | | |
| 7 | ⏳ 待完成 | | |
| 8 | ⏳ 待完成 | | |
| 课后练习2 | ⏳ 待完成 | | |
| 9 | ⏳ 待完成 | | |
| 10 | ⏳ 待完成 | | |
| 11 | ⏳ 待完成 | | |
| 12 | ⏳ 待完成 | | |
| 课后练习3 | ⏳ 待完成 | | |
| 13 | ⏳ 待完成 | | |
| 14 | ⏳ 待完成 | | |
| 15 | ⏳ 待完成 | | |
| 16 | ⏳ 待完成 | | |
| 课后练习4 | ⏳ 待完成 | | |
