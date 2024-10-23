# 图片描述生成（诗歌）

## 目录
1. [项目简介](#项目简介)
2. [难点分析](#难点分析)
3. [模型结构](#模型结构)
4. [所用数据集](#所用数据集)
5. [实验结果](#实验结果)
6. [参考文献](#参考文献)
7. [使用说明](#使用说明)

## 项目简介
&emsp;&emsp;从图像中自动生成自然语言已经引起广泛关注，本项目更进一步来研究由**图像自动生成诗歌**（多行）创作。不同于普通的图片描述，诗歌描述可能不那么注重于描述图片所代表的事实本身，而是倾向于从图像中的物体、场景和情感中捕捉更深层次的意义和诗意符号（如从猎鹰中捕捉骑士，从进食中捕捉狩猎和战斗，从站立中捕捉等待）。本项目通过使用策略梯度进行对抗训练将任务进一步拆解，最终虽然再韵律等传统的诗歌技巧等方面仍不成熟，但仍然具有一定的是个结构和风格。   

## 难点分析
1. **多模态处理**：与由主题生成诗歌相比，该任务是一个跨模态任务。一个直观的想法是由图像提取主题再生成诗歌，但是这样会造成信息丢失。
2. **任务主观性**：与caption相比，该任务是一个更加主观的任务，因为一张图像可能对应多种诗歌，而caption更侧重描述image中的客观事实。
3. **格式要求**：诗歌的格式和风格与自然语言不同。本文生成的是自由诗（English free verse），对韵律等无要求。
   
## 模型结构

![1](https://github.com/user-attachments/assets/c25f6cec-5f9a-48d3-ace0-766fce09da18)

 **（1)深度耦合视觉-诗歌嵌入模型**：用于从图像中学习诗歌表征。
 
 **（2)策略梯度优化的多对抗训练过程**：基于RNN的生成器作为代理，两个判别网络为策略梯度提供奖励。



## 所用数据集
1. **Multi-Modal Poem dataset (MultiM-Poem)**：由图像和人工标注的诗句组成
![2(1)](https://github.com/user-attachments/assets/0976ab2f-1079-4d2e-83ea-0d099e4884f1)

2. **Uni-Modal Poem dataset (UniM-Poem)**:最大的诗句语料库
![2(2)](https://github.com/user-attachments/assets/b6530648-0490-4e58-9818-a367dd729912)

3. **MultiM-Poem (Ex)**：通过训练好的嵌入模型，对MultiM-Poem通过相似度扩展并去除冗余而来
- 各数据集详细情况如下：

 ![3](https://github.com/user-attachments/assets/54f92bca-13e2-49f4-8328-b96177475ec3)

## 实验结果
性能对比，其中Show and Tell和SeqGAN都曾是Image Caption相关性能最优模型
- BLEU：评价模型生成内容于人工标注答案的相似度
- Novelty:评价模型生成内容的新颖性（从其他地方引用程度）
- Overall：计算平均分
  
| Method | Relevance | Novelty-2 | Novelty-3 |BLEU-1 |BLEU-2 |BLEU-3 |Overall |
| :------:| :------: | :------: | :-----: |:-----: |:-----: |:-----: |:-----: |
| Show and Tell | 1.91 | 48.09 | 81.37|12.64|3.34|0.8|34.34|
| SeqGAN | 2.03 | 47.52 | 82.32 |13.40 |3.72|0.76|44.95|
| I2pGAN | 2.25 | 54.32 | 85.37 |14.25|3.84|0.94|77.23|


## 参考文献
- 参考文献：[Bei Liu, Jianlong Fu, Makoto P. Kato, and Masatoshi Yoshikawa. 2018. Beyond Narrative Description: Generating Poetry from Images by Multi-Adversarial Training. ](https://arxiv.org/pdf/1804.08473)   


## 使用说明
1. [点此下载模型](https://huggingface.co/ZicXu/img2poem)，并放到code/model/目录下（测试可用code/src/test.py）：
   
2. 本项目仅支持Linux系统,Windows可通过Docker进行测试：
- 执行：
  
```bash
docker pull zichangxu/img2poem 
```
运行容器后，切换到app/src/下，执行以下命令，将默认对images/test.jpg进行预测
```bash
python test.py
```
