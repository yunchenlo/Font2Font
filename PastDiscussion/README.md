## 6/18 Final round
1. Report (5 pages)
   - survey 
   - encountered problem
   - contribution
      - data augmentation (unlike generated sample and some noise)
      - hierarchical (unlike generated sample and some noise)
      - transfer learning (mode collapse)
      - enhance discriminator (mode collapse)
   - experiment (batch size: 16, epoch:100, lr:0.001, L1: 100, Lconst:15)
      - XXM_STZMF : raw zi2zi -> hierarchical -> data aug. -> transfer learning -> enhance discriminator
      - BIAUKAI_STZMF : raw zi2zi -> hierarchical -> data aug.
     
   - extra detail results in cloud
2. slides
3. source code
4. hand-writing word

## How to solve Generator Failure from XXM to target font
1. Increase dataset picture number (3000 -> 6000)
2. Increase complexity of discriminator or encoder and generator (Yi-Ren, Jerry)
3. Pretrain from (input:target font, output:target font) to ensure the generator initial state is correct (Jerry) 
4. Apply pretrained model to new dataset(Yi-Ren)
5. Create new loss term (yclo)
6. Find who cause the failure(encoder or generator) (yclo)


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