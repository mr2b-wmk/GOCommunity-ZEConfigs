# Go community-ZEConfigs
Map data manager
## 文本使用逻辑

>在default.ini中注册好需要修改的参数
>>格式: 中文名 = cvar_name
>>>然后插件在加载之后, 会向对应的map.cfg中添加字段
>>>>然后修改map.cfg对应字段的值即可

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
## 各参数说明
```
投票延长次数 = ext_limit  //玩家手动输入的ext可用次数
投票延长时间 = ext_time   //ext延长时间
地图延长次数 = rtv_ext_limit  //rtv投票中9延长的次数
地图延长时间 = rtv_ext_time   //rtv投票9延 延长时间
地图冷却时间 = mp_freezetime  //回合开局无法移动时间 建议0或1 单位秒
每回合的回合时间 = mp_roundtime     //回合时间 建议根据关卡需要的时间填,一般设置60
地图时间 = mp_timelimit     //地图时间,时间到5分钟时触发rtv投票 单位分钟
跌落伤害 = sv_falldamage_scale      // 1开启摔伤 0关闭摔伤
服务器重力 = sv_gravity      //默认800 一般建议750左右 可不填
出生金钱 = zr_account_cashfill_value
人类血量 = zr_class_modify "humans" "health" //仅为开局人类血量,并非更改人类血量上限.
母体僵尸血量 = zr_class_modify "motherzombies" "health"
普通僵尸血量 = zr_class_modify "zombies" "health"
僵尸死亡重生时间 = zr_respawn_delay
僵尸回血速度 = zr_class_modify "zombies" "health_regen_amount"        //回血血量
僵尸回血间隔 = zr_class_modify "zombies" "health_regen_interval"      //回血间隔
僵尸击退系数 = zr_class_modify "zombies" "knockback"
设置开局尸变比例 = zr_infect_mzombie_ratio      //人类僵尸比值 例:比例为9时 人类僵尸9:1 ?不确定
母体是否传送回出生点 = zr_infect_mzombie_respawn  //一定要为1 不为1就是ZM
僵尸母体出现倒计时 = zr_infect_spawntime_max     //僵尸出现倒计时
高爆手雷价格 = zr_item_modify "高爆手雷" "cost"
燃烧手雷价格 = zr_item_modify "燃烧手雷" "cost"
冰冻手雷价格 = zr_item_modify "冰冻手雷" "cost"
照明弹价格 = zr_item_modify "照明弹" "cost"
血针购买价格 = zr_item_modify "治疗针" "cost"
防弹衣价格 = zr_item_modify "购买护甲" "cost"
高爆手雷可购买次数 = zr_item_modify "高爆手雷" "limit"       //0为无限 -1为禁止
燃烧手雷可购买次数 = zr_item_modify "燃烧手雷" "limit"
冰冻手雷可购买次数 = zr_item_modify "冰冻手雷" "limit"
照明弹可购买次数 = zr_item_modify "照明弹" "limit"
规定每回合血针购买次数 = zr_item_modify "治疗针" "limit"
规定每回合防弹衣购买次数 = zr_item_modify "购买护甲" "limit"
人类空中最大速度 = zr_human_air_maxspeed        //最大空速 不低于250即可
僵尸空中最大速度 = zr_zombie_air_maxspeed
人类最大传送次数 = zr_ztele_max_human       //ztele次数
僵尸最大传送次数 = zr_ztele_max_zombie
AUG可购买次数 = zr_item_modify "AUG 自动步枪" "limit"        //0为无限制 -1为禁止 默认无限制
SG556可购买次数 = zr_item_modify "SG556 自动步枪" "limit"
SCAR可购买次数 = zr_item_modify "SCAR-20 自动狙击步枪" "limit"
G3SG1可购买次数 = zr_item_modify "G3SG1 自动狙击步枪" "limit"
SSG08可购买次数 = zr_item_modify "SSG08狙击枪" "limit"
NEGEV可购买次数 = zr_item_modify "NEGEV 轻机枪" "limit"
M249可购买次数 = zr_item_modify "M249 轻机枪" "limit"
高爆手雷击退系数 = zr_item_modify "高爆手雷" "knockback"        //默认值2.25
高爆手雷燃烧时间 = zr_grenade_ignite_time       //默认2s
可携带高爆手雷数量 = ammo_grenade_limit_hegrenade
可携带燃烧弹数量 = ammo_grenade_limit_incgrenade
可携带冰冻手雷数量 = ammo_grenade_limit_smokegrenade
可携带照明弹数量 = ammo_grenade_limit_flashbang

```
## 默认参数 复制用
```
"MapDataMannager"
{
	//关于地图时间
    "投票延长次数"		"1"
	"投票延长时间"		"1800"
	"地图延长次数"		"2"
	"地图延长时间"		"1200"
	"地图冷却时间"		"1"
	"每回合的回合时间"		"60"
	"地图时间"		"45"

    //重力
	"跌落伤害"		"0"
	"服务器重力"		"750"
	"人类空中最大速度"		"270"
	"僵尸空中最大速度"		"330"
	"人类最大传送次数"		"3"
	"僵尸最大传送次数"		"3"

    //关于开局
	"出生金钱"		"9000"
	"人类血量"		"100"
	"母体僵尸血量"		"30000"
	"普通僵尸血量"		"30000"
	"僵尸死亡重生时间"		"2"
	"僵尸回血速度"		"500"
	"僵尸回血间隔"		"2"

    //ZR类
	"僵尸击退系数"		"1.8"
	"设置开局尸变比例"		"8"
	"母体是否传送回出生点"		"1"
	"僵尸母体出现倒计时"		"25"

    //投掷物
	"高爆手雷击退系数"		"2.25"
	"高爆手雷燃烧时间"		"2"
	"可携带照明弹数量"		"10"
	"可携带高爆手雷数量"		"10"
	"可携带燃烧弹数量"		"10"
	"可携带冰冻手雷数量"		"10"
    "高爆手雷价格"		"3500"
	"燃烧手雷价格"		"4500"
	"冰冻手雷价格"		"6000"
    "照明弹价格"		"1"
    "血针购买价格"		"2000"
    "高爆手雷可购买次数"		"20"
    "燃烧手雷可购买次数"		"5"
	"冰冻手雷可购买次数"		"3"
	"照明弹可购买次数"		"1"
	"规定每回合血针购买次数"		"2"
	"防弹衣价格"		"2000"
	"规定每回合防弹衣购买次数"		"0"

    //武器类限制
    "AWP可购买次数"		"0"
	"AUG可购买次数"		"0"
	"SG556可购买次数"		"1"
	"SCAR可购买次数"		"-1"
	"G3SG1可购买次数"		"-1"
	"SSG08可购买次数"		"-1"
	"NEGEV可购买次数"		"5"
	"M249可购买次数"		"5"
}

```
