# Font2Font 

#### Yun-Chen Lo, Yi-Ren Chen, Jerry Zhang Jian (NTHU EE)

An enhanced zi2zi project [[1]](https://github.com/kaonashi-tyc/zi2zi) with word-oriented data augmentation, feature combination, and transfer learning. 

This repo is based on zi2zi project with incremental boost inspired on recent research and our observation on Chinese Characters.

## Folder Description

```
Font2Font
|	README.md
└──	src/
|	└── zi2zi/					# original zi2zi with data aug options
|	└── zi2zi_hir/					# + combine levels of features
|	└── zi2zi_hir_dis/				# + increase discriminator complexity
|	└── zi2zi_hir_morefilter/			# + alternative ways of complexity boost
|	PastDiscussion/
|	PriorWork/
|	Report/
|	└── Interim/
|	└── Final/
```

## Code Running Example
```
Train zi2zi 
change directory to src/zi2zi;
$ make all // prepare data, train, and evaluate on demo word
```

## Dependency
- tensorflow 0.8
- python 3.x

## Major contributions
![alt text](https://i.imgur.com/RqkXm2Y.png)
### Word-oriented data augmentation
![alt text](https://i.imgur.com/ysV0Yqc.png)
### Combine different level feature 
![alt text](https://i.imgur.com/jjym664.png)
### Transfer Learning
![alt text](https://i.imgur.com/9RCz2yg.png)
### Difficulty-aware adjustment
![alt text](https://i.imgur.com/tq1pbOu.png)

## Result
![alt text](https://i.imgur.com/2zaQnOI.png)

## Future Work
### Add code or tools to generate compatible Chinese font (.ttf)
### Add handwriting dataset and tools for further application exploration
