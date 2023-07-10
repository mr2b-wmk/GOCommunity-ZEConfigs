## Test
## TOP游廊 Community-ZEConfigs
TOP游廊 Community ZombieEscape Configs Settings
## 使用说明
| 对应目录             | 说明                                     |
|------------------|----------------------------------------|
| bosshud          | [地图BOSS详情](./bosshud/README.md)        |
| console-mannager | [地图剧情消息](./console-mannager/README.md) |
| entwatch         | [地图神器配置](./entwatch/README.md)         |
| mapdata          | [地图参数详情](./mapdata/README.md)          |
| stripper         | [地图实体修改](./stripper/README.md)         |


## mapchinese
## 使用说明
| 关键词 | 说明                                                                       |
|----------|:----------------------------------------------------------------------------:|
| chinese  | 对应的中文翻译  |
| level  | 地图难度 |
| tag  | 地图tag |
| win  | 获胜回合数  |
| lost  | 失败回合数  |
| cd  | 当前地图CD  |
| cooldown  | 订图后固定生效CD时长 不填默认24H  |
---

## 举例子说明:
```
	"ze_undertale_g_v1_3_fix1"   // 地图名
	{
		"chinese"		"传说之下:屠杀线"   //中文译名
		"level"		"普通"  //难度
		"tag"		"闯关"  //tag
		"win"		"0" // 获胜|通关需要的人类胜利回合数
		"lost"		"0" //
		"cd"		"0" //立刻生效的CD
		"cooldown"		"25000"  //订图后固定生效CD时长 单位秒(S)
	}
```

## NULL格式-Copy用
```
	""
	{
		"chinese"		""
		"level"		""
		"tag"		""
		"win"		"0"
		"lost"		"0"
		"cd"		"0"
		"cooldown"		""
	}
```


