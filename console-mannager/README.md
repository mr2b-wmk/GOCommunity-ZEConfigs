# Gocommunity-ZEConfigs
Console message manager
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
| color  | 屌用没有 |
| coordinate  | 屌用没有 |
---

## 举例子说明:
```
"*** Leaf 1 leaving in 7 seconds ***" // 对应的地图消息
{
	"default"		"*** 叶子1还有7秒离开 ***" // 这里是翻译的译文
	"print"		"usermessage" // 消息输出的方式 （现在支持4种: 1. colorchat 2. hud 3. usermessage 4. html），我现在着重在更新usermessage/hud这两个方式, 反正记住如果要加倒计时这里填写usermessage就对了！
	"timer"		"7" // 倒计时时长 (0 -> 非倒计时消息 | >0 -> 即为>0秒的倒计时消息）
	"timercover"		"0" // 是否覆盖倒计时消息通道 (0 -> 不覆盖 | 1 -> 覆盖）, 如果设置为1则在触发这个倒计时消息的时候，会将当前存在的所有倒计时消息全部清空
	"timertip"		"叶子1 {time} 秒离开" // 屏幕中央倒计时的消息格式, {time} 会在代码中自动替换为倒计时剩余时间, 但绝对不能没有这个{time}
	"timerend"	"叶子1号小船, 已经起航, 不要在小船上乱跳哦!" // 倒计时结束后, 出现的蓝色提示文本
	"mulithud"		"1" // 是否加入滚动HUD信息队列 (就是绿色的那个滚动HUD)
	"taskhud"		"0" // 是否加入任务HUD信息队列 （就是屏幕左边的3个任务HUD通道）
	"color"		"0.000000 0.000000 0.000000" // 没用
	"coordinate"		"0.000000 0.000000 0.000000" // 没用
}
```

## NULL格式-Copy用
```
" "
{
	"default"		" "
	"print"		"hud"
	"timer"		"0"
	"timercover"		"0" 
	"timertip"		"倒计时 {time} 秒"
	"timerend"	" "
	"mulithud"		"1" 
	"taskhud"		"0"
	"color"		"0.000000 0.000000 0.000000"
	"coordinate"		"0.000000 0.000000 0.000000"
}
```
