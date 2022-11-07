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
| default  | 对应的中文翻译 [string] |
| print | 消息输出方式 [string] |
| timer  | 消息倒计时时长 [int] |
| timercover  | 覆盖倒计时消息 [1/0] |
| timertip  | 倒计时消息格式 [string] |
| timerend  | 倒计时结束后的提示语 [string] |
| mulithud  | 是否加入滚动HUD消息队列 [1/0] |
| taskhud  | 是否加入任务HUD消息队列 [1/0] |
| taskmessage  | 任务HUD的显示内容, 若不填则默认显示中文翻译 [string] |
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
		"cooldown"		"25000"  //固定生效CD时长 单位秒(S)
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



## 注意事项

请各位参加编辑的OP们, 在测试服跑图完毕之后，找bb索要entwatch、consolemannager文本，
Thanks~
