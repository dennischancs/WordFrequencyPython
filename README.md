# 扇贝全库词频牌组
词组来源：[dennischancs/getWordsFromShanbay: 用 Python 写的爬虫，能批量爬取扇贝网单词书、单词列表和单词。](https://github.com/dennischancs/getWordsFromShanbay)
> 含单词、词组

# 导入Anki
1. WordFrequencyPython处理词频；
2. 删除重复词义，只保留前3条词义（最终文件在`./WordLists/#2Anki/#v4可导入anki.7z`中）；
3. 导入anki，日学习数500，日复习数调成9999、复习间隔为36500；
4. 用anki插件去重[Merge Duplicate Cards(合并重复卡片) - AnkiWeb](https://ankiweb.net/shared/info/608625159)
5. 导出卡牌备份

---词汇量---
三个大类（按统计频次排序），建议从频次高往下学习。

| **医学词汇**   | **6694** |
|--------|-------|
| A-9876 | *27*  |
| B-5    | *61*  |
| C-4    | *157* |
| D-3    | *417* |
| E-2    | 1235  |
| F-1    | 4797  |

| **英文词汇大量** | **50227** |
|--------|---------|
| A-8    | *1684*  |
| B-7    | *3001*  |
| C-6    | *4120*  |
| D-5    | *4156*  |
| E-4    | *4060*  |
| F-3    | 5068    |
| G-2    | 8506    |
| H-1    | 19632   |

| **计算机词汇**  | **647**  |
|--------|-------|
| A-3    | *2*   |
| B-2    | *11*  |
| C-1    | *634*   |

> *斜体*常用词汇量为`18330`；总词汇量为`57568`。

---anki卡牌格式---

1. 单词+词性
2. 主要汉语意思（只看前3个意义）
3. 保留点击跳转到安卓欧路词典APP的功能。

---AnkiDroid+的效果图---

<img alt="ankidroid" src="./WordLists/%232Anki/ankidroid.jpg?raw=true" width="200px" height="auto">

注：使用[Antimoon模板](https://www.laohuang.net/20180108/antimoon-template-3/)。

# 学习方法
1. 以上就是anki要用的背词牌组；
2. 先花3~5个月学习（参考[快，学会学习（十二）-我的故事 - BonXG · 学习型博客 | For you and me](https://bonxg.com/p/60.html)的方法，用Anki背的时候并抄写单词，抄在ipad pro的goodnotes上）习得到大量的被动词汇；
3. 强化被动词汇：然后就是做阅读，训练对背了的词汇的阅读运用能力：如六级阅读、考研阅读、托福阅读、GRE等题目。
4. 转化部分被动词汇为主动词汇：指定要用什么单词写作/造句；
5. 听力的练习；

# WordFrequencyPython
一个统计重复词条 并 合并词条意思的python脚本。
[ostwalprasad/WordFrequencyPython: Python code to find out most frequent words from different word lists](https://github.com/ostwalprasad/WordFrequencyPython)
