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
# 地圖修復展示
找個地方列一下社區哪些地圖修復過，順便學習一下如何寫README文件。
這個文件的作用是給TOP遊廊社區僵尸逃跑管理員展示地圖修復的哪些地方，以便其與玩家進行溝通。內容可能有點長，故放在最下面，不定時更新。可能有遺漏。

##### Bilibili ZE-Tastysaw 以上
#####  [Stripper入門教程](https://www.bilibili.com/read/cv17496906)

## ze_ancient_wrath_v2_test27_g6t 古代遺跡:金字塔
 1. 修復熱身關卡炸服
 2. 修復第六關的空速不夠無法跳火車
 3. 和諧部分宗教元素
 >Tips:空速插件應該是已經修復，由於某些原因這裡並未刪除
>由 幽々子等 修復
##  ze_ashen_keep_v0_3_csgo4 黑暗之魂:亞諾爾隆德
1. 修復神器陷地
>由 健忘症晚期 修復
##  ze_atos_v2_3 夢幻阿托斯
1. 防止滑翔超車
2. 神器關聯修正
3. 部分雜項修復
>由 健忘症晚期 修復
##  ze_biohazard3_nemesis_b5_2 生化危機:復仇女神
1. 雜項修復
>由 未知作者 修復
##  ze_bioshock_v6_2_csgo6 生化奇兵v6
1. 黑洞神器修復
2. 提高玩家對Boss傷害
3. 神器升級修復
>由 多人 修復
##  ze_blood_castle_b7 血色城堡
1. 還原CSOL的雜項機制
2. 玩家出生地點修復
##  ze_boatescape_ultimate_t2f3 坐船跑:終極大亂鬥
1. 全面漢化
>由 白雲我真的白 修復
##  ze_border_b2_fix 邊境
1. 雜項及部分神器修復
>由 未知作者 修復
##  ze_crashbandicoot_p3 古惑狼
1. 修復特效不顯示
>由 未知作者 修復
##  ze_deadcore_s7f2 死亡核心(s7f2)
1. 一些關卡減速與傳送修復
2. 額外關卡
>由 健忘症晚期 和 未知作者 修復
>Tips:這裡由於社區在去年存檔丟失過一次 故修復並不完整
## ze_destruction_of_exorath_v4_lite 死亡空間
1. 一些亂七八糟的雜項修復
>由 未知作者 修復
##  ze_diddle_v3 欺騙(地豆)(維他檸檬茶)(譯名不唯一)
1. Luffaren官方的#11修復
2. 社區生態修復的墻反傷
3. 無下限的重口味和諧
>除官方外由 健忘症晚期等 修復
##  ze_djinn_go1 法老王墓
1. 雜項修復
>由 移植者 和 健忘症晚期 修復
##  ze_dystopia_a4 反烏托邦
1. 和諧黃色元素
>由 幽々子 修復
##  ze_eternal_journey_go_v1_4t8 永恒旅途
1. 修復冰神器卡頓
2. 跳過第四關
>由 健忘症晚期等 修復
## 最終幻想7與最終幻想12
1. 過於冗長，在此不列出
##  ze_frostdrake_tower_v1 寒霜高塔(冰龍)
1. 禁止刷屍籠
##  ze_jungle_escape_v1_2_d 叢林逃亡
1. 神器修復
2. 雜項修復
>由 健忘症晚期 修復
##  ze_lotr_minas_tirith_p5 魔戒:米那斯提力斯
1.雜項修復
>由 Koyomaple等 修復
##  ze_minecraft_adventure_v1_3d 我的世界:大冒險
1. 各種神器修復
>由 健忘症晚期等 修復
##  ze_mist_q2 迷霧
1. 防止滑翔超車
2. 王座推力調整
>由 幽々子等 修復
##  ze_necromanteion_v3_1 瞬獄影殺陣
1. 防止刷Boss血量
2. 修正血量显示
>由 健忘症晚期 修復
##  ze_obj_npst_v2 半條命:黑山基地v2
1. 移植者提供的修復相關材料於去年社區存檔丟失事件中丟失 是否存在修復處於未知狀態
2. 叠伤没修，不过第二个狙击手已经say byebye了
3. 增加部分gametext汉化
## ze_obj_rampage_v1_2 半條命:橫空出世
1. 移除母體時間限製 請TOP遊廊社區僵屍逃跑管理員進行具體時間修改。
2. 由於推力矢量計算插件早在去年就已修復 故已於年初移除上升氣流的額外推力加成。
3. 長管道由於TOP遊廊社區的僵屍疑似是hitbox(不確定，繼續以hitbox代指僵屍模型)與prop_dynamic在某些時刻無法發生物理交互，社區插件問題並非地圖原有問題，已於去年與移植者進行溝通，故此處給出修復指導，詳見3.1 3.2。
- 3.1 對社區插件進行修復(社區生態與技術性分析結果為 困難與不建議)。
- 3.2 加一個func_breakble或者func_brush等固實體配合IO邏輯模擬空氣墻(社區生態與技術性分析結果為 簡單與建議)。
4. 中文歌詞文本由 **茉莉かわいい** 提供相關文本，已於年初進行格式優化，社區也已經對text通道進行處理，如出現hud閃爍等請自行retry。
5. 以上僅為個人建議，需要相關材料請聯系我，這裏僅做通知，請由TOP遊廊社區僵屍逃跑管理員進行後續調整與修復。
6. 由於本系列地圖的不可描述原因，故只在github進行通知。
##  ze_obj_void_b3_t 半條命:至死不渝b3
1. 移植者提供的修復相關材料於去年社區存檔丟失事件中丟失 是否存在修復處於未知狀態
##  ze_offliner_v2_csgo1 單機者
1. 雜項修復
>由 未知作者 修復
## ze_otakuroom_v3_4_ps5 御宅房v3
1. 和諧黃色元素
>由 c1m等 修復
##  ze_otakuroom_v5_r 御宅房v5
1. 和諧黃色元素
2. 雜項修復
>由 c1m等 修復 
##  ze_paper_escaper_p7 紙質大逃亡
1. 修改核爆傷害
>由 健忘症晚期 修復
##  ze_project_codex_v1_2 彩虹聖典
1. 全面漢化
2. 關卡標題小雜項
>由 椀 修復
##  ze_parking_p4 最終疏散:停車場
1. 修改核爆傷害
>由 健忘症晚期 修復
##  ze_rizomata_a46(b45) 精靈塔
1. 神器拾取修復
2. 雜項修復
>由 健忘症晚期等 修復
##  ze_santassination_v3 獅子王(聖誕老人)
1. Luffaren官方的#9修復
2. 連關製
3. 去除裡世界黑幕
4. 和諧
5. 蘇格拉底的血量顯示以補償推力玩家和僵屍調整終局戰術
>除官方外由 血色的龍琉璃等 修復
##  ze_serpentis_temple_csgo5 美杜莎神廟v1(csgo5)
1. 難度增加
2. 偷雞卡Bug過關修復
3. 雜項及全面漢化
##  ze_shroomforest3_p 蘑菇森林3
1. 和諧納粹元素
>由 幽々子等 修復
##  ze_surf_dark_fantasy_v2go2 滑翔:黑暗幻想
1. 自動設置語言
2. 核爆處理
>由 健忘症晚期 修復
##  ze_tesv_skyrim_v5_6 上古卷軸5:天際
1. 神器拾取及雜項
2. 宗教元素和諧
3. 添加二周目額外全員500關卡
##  ze_tyranny_v5_go3 暴君魔典紀元:第一部分
1. 神器拾取修復
2. 全面漢化
##  ze_tyranny2_v1_csgo2.cfg 暴君魔典紀元:第二部分
1. 開局護甲發放
2. 聖經次數限制
3. 全面漢化
##  ze_uchiha_legacy_cm2_fix 宇智波:遺響
1. 跳刀吞血量修复
2. 花树界降临增强
##  
