# transeval

## 一、基本介绍

transeval是基于GPT-4模型的中英人工翻译可解释性质量评估模型。借鉴MQM等传统笔译评估框架，国内外高校、翻译协会认证考试评分细则，设计了一套基于并适用于大语言模型的人工翻译可解释性自动评估流程，模拟了人工翻译质量评估并输出类似人工翻译质量评估的结果，包括译文的错误位置、错误类型、错误严重程度和错误解释。



## 二、评估流程

（1）切分文本：将输入的原文本按照段落切分为若干字数相近的段落，切分过程由GPT实现；

（2）对齐文本：将原文、参考译文、待评估译文对齐，对齐由GPT实现；

（3）评估文本：将原文、参考译文、待评估译文以及评估标准，按照一定的prompt框架（LangGPT）组织为自然语言指令，让GPT-4模型进行评估，并输出JSON结构的评估结果。

<img src="https://picbed-1324358826.cos.ap-beijing.myqcloud.com/typechoimage-20240413155721877.png" alt="image-20240413155721877" style="zoom: 80%;" />

## 三、测试集

对评估模型从如下五个维度进行评估：错误类型、错误数量、错误共现（不同类型错误同时出现）、是否有参考译文、GPT输出结果是否稳定等方面进行测试。

测试集来自于中英CATTI三级笔译试题，参考译文来自于XXLIN1987公众号和某网校提供的译文。

XXLIN1987译文：https://mp.weixin.qq.com/s/y8gvX5qDY8LPMTiKIAOCYw

某网校译文：https://www.examw.com/catti/bycj/test/

测试结果如下：

![image-20240413160728234](https://picbed-1324358826.cos.ap-beijing.myqcloud.com/typechoconclusion.png)

test_code文件夹下提供了测试使用的Python代码；

test_set文件夹下是所有的测试集文件，文件夹命方式为：编号-评估维度-（错误类型）。

测试集下载后建议用Excel打开查看，步骤如下：

（1）下载测试集；

（2）打开一个新的Excel工作簿；

（3）从“数据-获取和转换数据-从文本/CSV”打开.csv文件。

![image-20240413162242582](https://picbed-1324358826.cos.ap-beijing.myqcloud.com/typechoimage-20240413162242582.png)
