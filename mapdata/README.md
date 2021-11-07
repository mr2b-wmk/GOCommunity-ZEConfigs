# 5EPlay-ZEConfigs
Map data manager
## 文本使用逻辑
```flow
st=>start: 开始
op=>operation: 遍历maps.cfg中参数设置
cond=>condition: 改参数是否存在于default.ini中
e=>end
st->op->cond
cond(yes)->e
cond(no)->op
&```

```
举例子说明:

1. 需要修改的参数，必须录入default.ini，格式如下:
<格式> 你想好的命名 = cvar_name
<举例> 地图时长 = mp_timeleft

2. 在插件成功加载之后, 会自动在地图对应的cfg文件中加上default.ini中所有的参数,
然后, 修改对应的数值就行了!
"MapData"
{
  "地图时长" "60"
}
```
