# mumheader
Add numbers to markdown headers.

## Install
The module works without install. Just call `numheader/numheader.py`.

## Usage


```bash
./numheader/numheader.py --file myfile.md --out out.md
```

When `myfile.md` is like following,

```markdown
# Title AAAA
## Title BBBB
## Title CCCC
# Title DDDD
```

`out.md` will be

```markdown
# 1. Title AAAA
## 1.1. Title BBBB
## 1.2. Title CCCC
# 2.1 Title DDDD
```

Broken numbers will be fixed.
