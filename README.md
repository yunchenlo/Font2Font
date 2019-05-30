# Font.py

## 0530 TODO (Deadline: 6/2)
- Generate Handwriting dataset (Find Resources)
- Enlarge gap between source & target (新細明體 -> others) (Jerry 新細明體 master)
  - Fix target & inference on new font (新細明體)
  - Train on new source target fonts
- Modify Cheat Loss (Chen Yi-Ren)
- Find ways to augment few training data (Yun-Chen Lo) 
  - Bold Font
  - Break 部首
- Transfer Learning (all)

## 0525 TODO
- Find ways to augment few training data (Yun-Chen Lo) 
  - Bold Font
  - Scale & Crop (done)
  - Break 部首
- Replace Generator & Descriminator part architecture (Jerry) (don't do)
- Hierarchical GAN implementation (Chen Yi-Ren)
  - Hierarchical Discriminator (done)
  - Generator t1,t2,t3 (Hierarchical Generator) (done)

## 0524 Conclusion
- Train FontMissing and analyze the results using pix2pix.
- Train FontMissing and analyze results using Cycle-GAN.
- Use other architecture to see the result differences. 

## Table of Contents
- Task A : Font missing word learning
- Task B : Write to Font Transfer
- (Optional) : Font Minecraft

## Task A : Font missing word learning
### Prior Works
* [Chinese Handwriting Imitation with HGAN](http://bmvc2018.org/contents/papers/1141.pdf) 


  - Most important idea:
    - Propose to use global features and detail features to generate the targeted transform
  - Method:
    - Feed Embedding feature to Generator
    - Feed generator's feature to Descriminator

## Task B : Write to Font Transfer


## Other Prior Works
* 建中生運用GAN實現字體風格轉換[(slideshare)](https://www.slideshare.net/cnanews/gan-137298578)
* 以類神經網路對手寫漢字與書法字體作風格遷移[.(website)](http://ludwig.willyoudo.com/?p=1219)
* Rewrite: Neural Style Transfer For Chinese Fonts[.(website)](https://github.com/kaonashi-tyc/Rewrite)
* zi2zi: Master Chinese Calligraphy with Conditional Adversarial Networks[.(website)](https://github.com/kaonashi-tyc/zi2zi)
* [Generating Handwritten Chinese Characters using CycleGAN](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=8354132)
* [Handwritten Chinese Font Generation with Collaborative Stroke Refinement](https://arxiv.org/pdf/1904.13268.pdf)
* [Separating Style and Content for Generalized Style Transfer](https://arxiv.org/pdf/1711.06454.pdf)
* [Chinese Handwriting Imitation with Hierarchical Generative Adversarial Network](http://bmvc2018.org/contents/papers/1141.pdf)
* [Auto-Encoder Guided GAN for Chinese Calligraphy Synthesis](https://arxiv.org/pdf/1706.08789.pdf)
* [Chinese Typeface Transformation with Hierarchical Adversarial Network](https://arxiv.org/pdf/1711.06448.pdf)
* [SCFont: Structure-guided Chinese Font Generation via Deep Stacked Networks](http://www.icst.pku.edu.cn/zlian/docs/2019-01/20190122112100781376.pdf)

## Background Knowledge
* Neural Style Transfer [medium](https://towardsdatascience.com/neural-style-transfer-tutorial-part-1-f5cd3315fa7f)

### Project Members
- Yun-Chen Lo, Yi-Ren Chen, Jerry Zhang Jiang (NTHU EE)
