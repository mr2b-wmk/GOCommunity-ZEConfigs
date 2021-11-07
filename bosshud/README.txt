只会记录两种情况的BOSS信息, 分别为1. math_counter类型和 2. 非math_counter类型,
现在对这两个类型的数据进行举例子说明:
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
