# 5EPlay-ZEConfigs
Boss HUD Infomations
## BOSS分类
| 分类 | 说明            		|
|:----------:|:-------------------:|
| math_counter  | 计数器类BOSS  	|
| 非math_counter  | 计算伤害类BOSS 	|
---
## 字段解释
| 关键词 | 非math_counter类型实体 |
|:----------:|:-------------------:|
| 开头数字id  | 实体hammerid, 插件会自动填写, 如果是遗漏的实体需要添加则必须填上hammerid 	|
| classname  | 实体classname	|
| name  | 实体m_iName	|
| translate  | 实体名称的中文翻译	|
| status  | 消灭实体之后, 是否打印伤害排行榜	|
| created_tip | 实体激活的提示语	|
| damage_hud  | 伤害实体时的HUD信息显示	|
| health  | 实体血量记录	|
---

## 详细说明
```
<1> 非math_counter类型
"503736" // HammerId (所有配置文件关于实体的我都以hammerid为selection）
{
	"classname"		"func_physbox_multiplayer" // classname
	"name"		"Monstruo_Breakable" // m_iName
	"translate"	"中文名"	// 中文翻译
	"status"		"off" // 是否开启击杀统计即伤害结算排名面板 (on -> 开 | off -> 关) PS：慎用，请你在知道你真正需要的时候在开启on
	"created_tip"		"on"  // 是否在BOSS诞生的时候开启提示文本 (on -> 开| off -> 关) PS：这个功能正在（新建文件夹）还没弄
	"damage_hud"		"on" // 是否开启HUD攻击反馈 (on -> 开 | off -> 关)
	"health"		"1" // 记录BOSS在记录的时候血量 （这里的血量只是记录给我参考用的, 修改这里并不会直接修改BOSS血量, 后续我有可能会直接做成可修改BOSS血量）
}
```
```
<2> math_counter类型
"2710" // HammerId
{
	"classname"		"math_counter" // classname
	"name"		"bahamut_vida" // m_iName
	"translate"	"中文名"	// 中文翻译
	"status"		"off" // 是否开启击杀统计即伤害结算排名面板 (on -> 开 | off -> 关) PS：慎用，请你在知道你真正需要的时候在开启on
	"created_tip"		"on"// 是否在BOSS诞生的时候开启提示文本 (on -> 开| off -> 关) PS：这个功能正在（新建文件夹）还没弄
	"damage_hud"		"on" // 是否开启HUD攻击反馈 (on -> 开 | off -> 关)
	"change_mode"		"+" // math_counter的计数模式(+是递增,-是递减) PS：现在没啥屌用
	"change_tip"		"null" // 这个是准备用来计数一些BOSS核爆啊、技能释放的倒计时提示 PS：现在也没啥屌用，被我阉割掉了
	"health"		"20000" // 记录BOSS在记录的时候血量 （这里的血量只是记录给我参考用的, 修改这里并不会直接修改BOSS血量, 后续我有可能会直接做成可修改BOSS血量）
	"health_bar"		"5" // BOSS的血条数量（计算多管血条BOSS的时候记得一定要填写, 不然只会显示单条血量的数值）
}
```
