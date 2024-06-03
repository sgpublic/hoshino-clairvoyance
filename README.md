# Hoshino 千里眼

数据源：[Columba-丘比@bilibili](https://www.bilibili.com/read/cv15264705/)

## 食用方法

注释掉 Hoshino 中 `hoshino/modules/priconne/query/query.py` 文件的所有内容，并将本仓库克隆到 `hoshino/modules/priconne`，即（目录结构）：

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
    ├── query.py # 注释掉这个文件的所有内容
    └── whois.py
```

（可选）修改 `hoshino/config/priconne.py`，追加以下内容：

```python
class clairvoyance:
    CLAIRVOYANCE_GIT_URL = "https://github.com/sgpublic/hoshino-clairvoyance"
    CLAIRVOYANCE_GIT_BRANCH = "resource"
```

若网络环境不通畅，`CLAIRVOYANCE_GIT_URL` 可使用 `https://gitee.com/sgpublic/hoshino-clairvoyance`
