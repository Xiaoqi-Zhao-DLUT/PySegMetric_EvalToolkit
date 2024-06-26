# PySegMetric_EvalToolkit
<p align="center">
  <img src="./image/logo_pyseg.png" alt="Logo" width="300" height="auto">
 
<p align="center">
 基于python的图像分割测评工具箱（PSM）
</p>
  
## 已集成的评估指标
- **Pixel Accuracy (PA)** is calculated based on
the binarized prediction mask and ground-truth:
<p align="center">
    <img src="image/PA_metric.png" width=40%/> <br />
</p>

- **F-measure** is a metric that comprehensively considers both precision and recall:
<p align="center">
    <img src="image/Fm_metric.png" width=40%/> <br />
</p>

- **weighted F-measure** is proposed to improve the metric F-measure. It assigns different weights (ω) to precision and recall across different errors at different locations, considering the neighborhood information:
<p align="center">
    <img src="image/Fm_metric.png" width=40%/> <br />
</p>

- **S-measure** evaluates the spatial structure similarity by combining the region-aware
structural similarity Sr and the object-aware structural similarity So:
<p align="center">
    <img src="image/Sm_metric.png" width=40%/> <br />
</p>

- **E-measure**  can jointly capture image level statistics and local pixel matching information:
<p align="center">
    <img src="image/Em_metric.png" width=40%/> <br />
</p>

- **IOU** is the most common metric for evaluating classification accuracy:
<p align="center">
    <img src="image/IOU_metric.png" width=40%/> <br />
</p>

- **Dice** is a statistic used to gauge the similarity of two samples and become the most used metric in validating medical image segmentation:
<p align="center">
    <img src="image/DICE_metric.png" width=40%/> <br />
</p>

- **Balanced error rate (BER)** is a common metric to evaluate shadow detection performance, where shadow and non-shadow regions contribute equally to the overall performance without considering their relative areas:
<p align="center">
    <img src="image/BER_metric.png" width=40%/> <br />
</p>


- **MAE** measures the average absolute difference between the prediction and the ground truth pixel by pixel:
<p align="center">
    <img src="image/MAE_metric.png" width=40%/> <br />
</p>

## 分割任务中使用各类评估指标的代表性顶会论文工作
### 显著性目标检测（Salient Object Detection）
  
<table><tr>
<td><img src="./image/sod.jpg" width="300" border=0></td>
<td><img src="./image/sod.png" width="300" border=0></td>
</tr></table>  

  - <a href="https://arxiv.org/abs/2101.12482"><strong>Self-Supervised Pretraining for RGB-D Salient Object Detection, AAAI 2022.[Fmax, Fw, Sm, Em, MAE]</strong></a>
  - <a href="https://arxiv.org/pdf/2007.08074.pdf"><strong>Suppress and Balance: A Simple Gated Network for Salient Object Detection, ECCV 2020.[Fmax, Sm, MAE]</strong></a>
  - <a href="https://arxiv.org/pdf/2007.06811.pdf"><strong>A Single Stream Network for Robust and Real-time RGB-D Salient Object Detection, ECCV 2020.[Fmax, Fmean, Fw, Sm, Em, MAE]</strong></a>
   - <a href="https://arxiv.org/pdf/2007.09062.pdf"><strong>Multi-scale Interactive Network for Salient Object Detection, CVPR 2020.[Fmax, Fmean, Fw, Sm, Em, MAE]</strong></a>
   - <a href="https://arxiv.org/pdf/2007.06227.pdf"><strong>Hierarchical Dynamic Filtering Network for RGB-D Salient Object Detection, ECCV 2020.[Fmax, Fmean, Fw, Sm, Em, MAE]</strong></a>
### 伪装目标检测 （Camouflaged Object Detection）

<table><tr>
<td><img src="./image/cod.jpg" width="300" border=0></td>
<td><img src="./image/cod.png" width="300" border=0></td>
</tr></table>  


- <a href="https://arxiv.org/pdf/2203.02688.pdf"><strong>Zoom In and Out: A Mixed-scale Triplet Network for Camouflaged Object Detection, CVPR 2022.[Fmax, Fw, Sm, Em, MAE]</strong></a>
- <a href="https://openaccess.thecvf.com/content/ICCV2021/papers/Yang_Uncertainty-Guided_Transformer_Reasoning_for_Camouflaged_Object_Detection_ICCV_2021_paper.pdf"><strong>Uncertainty-Guided Transformer Reasoning for Camouflaged Object Detection, ICCV 2021.[Fw, Sm, Em, MAE]</strong></a>
- <a href="https://arxiv.org/pdf/2105.12555.pdf"><strong>Context-aware Cross-level Fusion Network for Camouflaged Object Detection, IJCAI 2021.[Fw, Sm, Em, MAE]</strong></a>
- <a href="https://arxiv.org/pdf/2104.02628.pdf"><strong>Uncertainty-aware Joint Salient Object and Camouflaged Object Detection, CVPR 2021.[Fmean, Sm, Em, MAE]</strong></a>
- <a href="https://openaccess.thecvf.com/content/CVPR2021/papers/Mei_Camouflaged_Object_Segmentation_With_Distraction_Mining_CVPR_2021_paper.pdf"><strong>Camouflaged Object Segmentation with Distraction Mining, CVPR 2021.[Fw, Sm, Em, MAE]</strong></a>
### 散焦模糊检测 （Defocus Blur Detection）

<table><tr>
<td><img src="./image/DBD.bmp" width="300" border=0></td>
<td><img src="./image/DBD_GT.bmp" width="300" border=0></td>
</tr></table>  


- <a href="https://openaccess.thecvf.com/content/CVPR2021/papers/Zhao_Self-Generated_Defocus_Blur_Detection_via_Dual_Adversarial_Discriminators_CVPR_2021_paper.pdf"><strong>Self-generated Defocus Blur Detection via Dual Adversarial Discriminators, CVPR 2021.[Fmean, MAE]</strong></a>
- <a href="https://arxiv.org/pdf/2007.08113.pdf"><strong>Self-generated Defocus Blur Detection via Dual Adversarial Discriminators, ECCV 2020.[Fmean, MAE]</strong></a>
- <a href="https://ojs.aaai.org/index.php/AAAI/article/view/6884"><strong>R2MRF: Defocus Blur Detection viaRecurrently Refining Multi-Scale Residual Features, AAAI 2020.[Fmean, MAE]</strong></a>
- <a href="https://openaccess.thecvf.com/content_CVPR_2019/papers/Zhao_Enhancing_Diversity_of_Defocus_Blur_Detectors_via_Cross-Ensemble_Network_CVPR_2019_paper.pdf"><strong>Enhancing Diversity of Defocus Blur Detectors via Cross-Ensemble Network, CVPR 2019.[Fmean, MAE]</strong></a>
- <a href="https://openaccess.thecvf.com/content_cvpr_2018/papers/Zhao_Defocus_Blur_Detection_CVPR_2018_paper.pdf"><strong>Defocus Blur Detection via Multi-Stream Bottom-Top-Bottom Fully Convolutional Network, CVPR 2018.[Fmean, MAE]</strong></a>
### 阴影检测 （Shadow Detection）

<table><tr>
<td><img src="./image/shadow.jpg" width="300" border=0></td>
<td><img src="./image/shadow.png" width="300" border=0></td>
</tr></table>  

- <a href="https://dl.acm.org/doi/pdf/10.1145/3474085.3475199"><strong>Robust Shadow Detection by Exploring Effective Shadow Contexts, ACM MM 2021.[Ber]</strong></a>
- <a href="https://openaccess.thecvf.com/content/ICCV2021/papers/Zhu_Mitigating_Intensity_Bias_in_Shadow_Detection_via_Feature_Decomposition_and_ICCV_2021_paper.pdf"><strong>Mitigating Intensity Bias in Shadow Detection via Feature Decomposition and Reweighting, ICCV 2021.[Ber]</strong></a>
- <a href="https://openaccess.thecvf.com/content_CVPR_2019/papers/Zheng_Distraction-Aware_Shadow_Detection_CVPR_2019_paper.pdf"><strong>Distraction-aware Shadow Detection, CVPR 2019.[Ber]</strong></a>
- <a href="https://openaccess.thecvf.com/content_ICCV_2019/papers/Ding_ARGAN_Attentive_Recurrent_Generative_Adversarial_Network_for_Shadow_Detection_and_ICCV_2019_paper.pdf"><strong>ARGAN: Attentive Recurrent Generative Adversarial Network for Shadow Detection and Removal, ICCV 2019.[Ber]</strong></a>
- <a href="https://openaccess.thecvf.com/content_ECCV_2018/papers/Lei_Zhu_Bi-directional_Feature_Pyramid_ECCV_2018_paper.pdf"><strong>Bidirectional Feature Pyramid Network with Recurrent Attention Residual Modules for Shadow Detection, ECCV 2018.[Ber]</strong></a>
### 透明目标检测 （Transparent Object Dectection）

<table><tr>
<td><img src="./image/transparent.jpg" width="300" border=0></td>
<td><img src="./image/transparent.png" width="300" border=0></td>
</tr></table>  

- <a href="https://openaccess.thecvf.com/content/ICCV2021/papers/Zhu_Transfusion_A_Novel_SLAM_Method_Focused_on_Transparent_Objects_ICCV_2021_paper.pdf"><strong>Transfusion: A Novel SLAM Method Focused on Transparent Objects, ICCV 2021.[mIoU, Acc, Ber, MAE]</strong></a>
- <a href="https://arxiv.org/pdf/2101.08461.pdf"><strong>Segmenting Transparent Object in the Wild with Transformer, IJCAI 2021.[mIoU, Acc]</strong></a>
- <a href="https://arxiv.org/pdf/2003.13948.pdf"><strong>Segmenting Transparent Objects in the Wild, ECCV 2020.[mIoU, Acc, Ber]</strong></a>
### 玻璃目标检测 （Glass Object Detection）

<table><tr>
<td><img src="./image/Glass.jpg" width="300" border=0></td>
<td><img src="./image/Glass.png" width="300" border=0></td>
</tr></table>  

- <a href="https://openaccess.thecvf.com/content/ICCV2021/papers/He_Enhanced_Boundary_Learning_for_Glass-Like_Object_Segmentation_ICCV_2021_paper.pdf"><strong>Enhanced Boundary Learning for Glass-like Object Segmentation, ICCV 2021.[mIoU, Acc, Fmean, Ber, MAE]</strong></a>
- <a href="https://openaccess.thecvf.com/content/CVPR2021/papers/Lin_Rich_Context_Aggregation_With_Reflection_Prior_for_Glass_Surface_Detection_CVPR_2021_paper.pdf"><strong>Rich Context Aggregation with Reflection Prior for Glass Surface Detection, CVPR 2021.[mIoU, Fmean, Ber, MAE]</strong></a>
- <a href="https://openaccess.thecvf.com/content_CVPR_2020/papers/Mei_Dont_Hit_Me_Glass_Detection_in_Real-World_Scenes_CVPR_2020_paper.pdf"><strong>Don’t Hit Me! Glass Detection in Real-world Scenes, CVPR 2020.[mIoU, Acc, Fmean, Ber, MAE]</strong></a>
### 镜子检测 （Mirror Detection）
<table><tr>
<td><img src="./image/Mirror.jpg" width="300" border=0></td>
<td><img src="./image/Mirror.png" width="300" border=0></td>
</tr></table>  

- <a href="https://openaccess.thecvf.com/content/CVPR2021/papers/Mei_Depth-Aware_Mirror_Segmentation_CVPR_2021_paper.pdf"><strong>Depth-Aware Mirror Segmentation, CVPR 2021.[mIoU, Fw, Ber, MAE]</strong></a>
- <a href="https://openaccess.thecvf.com/content_CVPR_2020/papers/Lin_Progressive_Mirror_Detection_CVPR_2020_paper.pdf"><strong>Progressive Mirror Detection, CVPR 2020.[Fmean, MAE]</strong></a>
- <a href="https://openaccess.thecvf.com/content_ICCV_2019/papers/Yang_Where_Is_My_Mirror_ICCV_2019_paper.pdf"><strong>Where Is My Mirror?, ICCV 2019.[mIoU, Acc, Fmean, Ber, MAE]</strong></a>

### 息肉分割 （Polyp Segmentation） 

<table><tr>
<td><img src="./image/Polyp.png" width="300" border=0></td>
<td><img src="./image/Polyp_gt.png" width="300" border=0></td>
</tr></table> 


- <a href="https://arxiv.org/pdf/2108.05082.pdf"><strong>Automatic Polyp Segmentation via Multi-scale Subtraction Network, MICCAI 2021.[mIoU, mDice, Fw, Sm, Em, MAE]</strong></a>
- <a href="https://arxiv.org/pdf/2102.08005.pdf"><strong>TransFuse: Fusing Transformers and CNNs for Medical Image Segmentation, MICCAI 2021.[mIoU, mDice]</strong></a>
- <a href="https://arxiv.org/pdf/2108.00882.pdf?ref=https://githubhelp.com"><strong>Shallow Attention Network for Polyp Segmentation, MICCAI 2021.[mIoU, mDice]</strong></a>
- <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-030-87193-2_68.pdf"><strong>Learnable Oriented-Derivative Network for Polyp Segmentation, MICCAI 2021.[mIoU, mDice]</strong></a>
- <a href="https://arxiv.org/pdf/2006.11392.pdf?ref=https://githubhelp.com"><strong>PraNet: Parallel Reverse Attention Network
for Polyp Segmentation, MICCAI 2020.[mIoU, mDice, Fw, Sm, Em, MAE]</strong></a>
### 其他类型分割任务 （人像分割、缺陷检测、表面检测、物体内部探伤检测等）
<table><tr>
<td><img src="./image/human.jpg" width="300" border=0></td>
<td><img src="./image/human.png" width="300" border=0></td>
</tr></table> 
<table><tr>
<td><img src="./image/Magnetic-tile-defect-datasets.-master.jpg" width="300" border=0></td>
<td><img src="./image/Magnetic-tile-defect-datasets.-master.png" width="300" border=0></td>
</tr></table> 
<table><tr>
<td><img src="./image/CrackForest.jpg" width="300" border=0></td>
<td><img src="./image/CrackForest.png" width="300" border=0></td>
</tr></table> 

## 超快捷使用方法  
- 安装./requirements.txt中的依赖
- 对utils/config.py中的Models = {'Model1':Model1,'Model2':Model2}及test_datasets = {'dataset1':dataset1,'dataset2':dataset2}完成对应的路径设置。注意字典中的'dataset'及待测方法中的数据集文件夹名字应与真实的数据集名称保持一致。
- 运行./test_score.py 数值预测结果日志将保留在当前目录中。
## 评测指标参考文献
```text
@inproceedings{Fmax_mean,
  title={Frequency-tuned salient region detection},
  author={Achanta, Radhakrishna and Hemami, Sheila and Estrada, Francisco and S{\"u}sstrunk, Sabine},
  booktitle= CVPR,
  pages={1597--1604},
  year={2009}
}  

@inproceedings{Fwb,
  title={How to evaluate foreground maps?},
  author={Margolin, Ran and Zelnik-Manor, Lihi and Tal, Ayellet},
  booktitle=CVPR,
  pages={248--255},
  year={2014}
}

@inproceedings{Sm,
  title={Structure-measure: A new way to evaluate foreground maps},
  author={Fan, Deng-Ping and Cheng, Ming-Ming and Liu, Yun and Li, Tao and Borji, Ali},
  booktitle= ICCV,
  pages={4548--4557},
  year={2017}
}  
@inproceedings{Em,
    title="Enhanced-alignment Measure for Binary Foreground Map Evaluation",
    author="Deng-Ping {Fan} and Cheng {Gong} and Yang {Cao} and Bo {Ren} and Ming-Ming {Cheng} and Ali {Borji}",
    booktitle=IJCAI,
    pages="698--704",
    year={2018}
}  
```
