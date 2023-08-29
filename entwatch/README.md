# Go community-ZEConfigs
entWatch informations
## 字段解释
| 关键词 | 说明            		|
|:----------:|:-------------------:|
| name  | 实体m_iName  	|
| translate  | 神器中文名翻译 	|
| classname  | 实体classname 	|
| team  | 实体可用队伍	|
| button  | m_hParent按钮实体hammerid 	|
| red | 发光颜色（红）1~255	|
| green  | 发光颜色（绿）1~255 	|
| blue  | 发光颜色（蓝）1~255 	|
| cooldown  | 冷却时间	|
| usemax  | 最大使用次数 	|
| ban  | 是否禁用该神器	|
| epick  | 是否允许按E拾取该神器	|
---

## 举例说明
```
"515770" // HammerId
{
	"name"		"Kohh_Elite" // m_iName
	"translate"		"Kohh_Elite" // 中文名
	"classname"		"weapon_elite" // classname
	"team"		"all" // 使用的队伍 (zombie | human)
	"button"		"515700" // 对应button的hammerid (插件自动填写）
	"red"		"255" // glow - red
	"green"		"255" // glow - green
	"blue"		"255" // glow - blue
	"cooldown"		"60" // cd
	"usemax"		"0" // 最大使用次数 (0为不限制）
	"epick"		"0" // 禁止epick拾取
}
```

## NULL例子 - Copy用
```
""
{
	"name"		""
	"translate"		""
	"classname"		""
	"team"		"all"
	"button"		""
	"red"		"255"
	"green"		"255"
	"blue"		"255"
	"cooldown"		"60"
	"usemax"		"0"
	"ban"		"0"
    "epick"		"0"
}
```
