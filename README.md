# Hoshino 千里眼

数据源：[Columba-丘比@bilibili](https://www.bilibili.com/read/cv15264705/)

## 食用方法

删除 Hoshino 中 `hoshino/modules/priconne/query/query.py` 文件，并将本仓库克隆到 `hoshino/modules/priconne`，即（目录结构）：

```shell
(venv) madray@nas:./Hoshino/hoshino/modules$ tree -a ./priconne/
./priconne/
├── ...
├── clairvoyance
│   ├── clairvoyance.py
│   ├── .git/
│   ├── .gitignore
│   ├── __init__.py
│   ├── README.md
│   └── _test.py
└── query
    ├── __init__.py
    ├── miner.py
    └── whois.py
```
