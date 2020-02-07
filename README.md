# 扇贝全库词频牌组
词组来源：[dennischancs/getWordsFromShanbay: 用 Python 写的爬虫，能批量爬取扇贝网单词书、单词列表和单词。](https://github.com/dennischancs/getWordsFromShanbay)

# 导入Anki
1. WordFrequencyPython处理词频；
2. 删除重复词义，只保留前3条词义（最终文件在`./WordLists/#2Anki`中）；
3. 导入anki，日学习数500，日复习数调成9999、复习间隔为36500；

---词汇量---
三个大类，每类之间会有重复词汇，每类之内词汇不重复（并统计了出现频次），建议从频次高往下学习。

| **医学词汇**   | **12258** |
|--------|-------|
| A-9876 | *68*    |
| B-5    | *121*   |
| C-4    | *285*   |
| D-3    | *688*   |
| E-2    | 1980  |
| F-1    | 9116  |

| **英文词汇大量** | **52350** |
|--------|-------|
| A-8    | *1685*  |
| B-7    | *3001*  |
| C-6    | *4120*  |
| D-5    | *4156*  |
| E-4    | 4060  |
| F-3    | 5582  |
| G-2    | 9112  |
| H-1    | 20634 |

| **计算机词汇**  | **8541**  |
|--------|-------|
| A-3    | *43*    |
| B-2    | *361*   |
| C-1    | 8137  |


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
