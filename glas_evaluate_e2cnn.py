Running SLURM prolog script on alpha51.cluster.local
===============================================================================
Job started on Mon Dec 26 18:05:55 GMT 2022
Job ID          : 2349363
Job name        : run_test
WorkDir         : /mainfs/scratch/yy3u19/myN-JetNet
Command         : /mainfs/scratch/yy3u19/myN-JetNet/run_test
Partition       : ecsall
Num hosts       : 1
Num cores       : 4
Num of tasks    : 4
Hosts allocated : alpha51
Job Output Follows ...
===============================================================================
/scratch/yy3u19/anaconda3/lib/python3.9/site-packages/e2cnn/nn/modules/r2_conv/basisexpansion_singleblock.py:80: UserWarning: indexing with dtype torch.uint8 is now deprecated, please use a dtype torch.bool instead. (Triggered internally at  /opt/conda/conda-bld/pytorch_1639180549130/work/aten/src/ATen/native/IndexingUtils.h:30.)
  full_mask[mask] = norms.to(torch.uint8)
---------- kernel_size: 3 ---------- classes: 2 ---------- model: E2CNN ---------- rotations: 8 ---------- dataset: GlaS - evaluate ----------
num of trainable parameters:7033922
Loading model checkpoints/GlaS/lr_0.002_bn_16_epoch_70_E2CNN_Ksize_3_rotation_8.pth num of rotations of filters: 8
Using device cuda
----------------------------------------------------------------------------------------------------------------------------------------------------------------
Num of images for evaulation: 1280
img: 0 evaluate_data/GlaS/E2CNN/evaluate/testA_10_0_0.pn_0_0.6315_[0.505  0.7579].png
img: 1 evaluate_data/GlaS/E2CNN/evaluate/testA_10_0_0.pn_1_0.5774_[0.481  0.6737].png
img: 2 evaluate_data/GlaS/E2CNN/evaluate/testA_10_0_0.pn_2_0.5002_[0.3741 0.6263].png
img: 3 evaluate_data/GlaS/E2CNN/evaluate/testA_10_0_0.pn_3_0.4784_[0.3687 0.5881].png
img: 4 evaluate_data/GlaS/E2CNN/evaluate/testA_10_0_405.pn_0_0.5694_[0.5419 0.5968].png
img: 5 evaluate_data/GlaS/E2CNN/evaluate/testA_10_0_405.pn_1_0.4772_[0.4229 0.5315].png
img: 6 evaluate_data/GlaS/E2CNN/evaluate/testA_10_0_405.pn_2_0.5132_[0.4914 0.5351].png
img: 7 evaluate_data/GlaS/E2CNN/evaluate/testA_10_0_405.pn_3_0.3056_[0.4696 0.1416].png
img: 8 evaluate_data/GlaS/E2CNN/evaluate/testA_10_126_0.pn_0_0.6553_[0.4948 0.8158].png
img: 9 evaluate_data/GlaS/E2CNN/evaluate/testA_10_126_0.pn_1_0.3715_[0.1987 0.5443].png
img: 10 evaluate_data/GlaS/E2CNN/evaluate/testA_10_126_0.pn_2_0.6211_[0.4725 0.7697].png
img: 11 evaluate_data/GlaS/E2CNN/evaluate/testA_10_126_0.pn_3_0.4757_[0.3141 0.6373].png
img: 12 evaluate_data/GlaS/E2CNN/evaluate/testA_10_126_405.pn_0_0.4802_[0.543  0.4174].png
img: 13 evaluate_data/GlaS/E2CNN/evaluate/testA_10_126_405.pn_1_0.5819_[0.5465 0.6173].png
img: 14 evaluate_data/GlaS/E2CNN/evaluate/testA_10_126_405.pn_2_0.4167_[0.3455 0.488 ].png
img: 15 evaluate_data/GlaS/E2CNN/evaluate/testA_10_126_405.pn_3_0.5337_[0.5363 0.531 ].png
img: 16 evaluate_data/GlaS/E2CNN/evaluate/testA_11_0_0.pn_0_0.5981_[0.6853 0.5109].png
img: 17 evaluate_data/GlaS/E2CNN/evaluate/testA_11_0_0.pn_1_0.5415_[0.6533 0.4298].png
img: 18 evaluate_data/GlaS/E2CNN/evaluate/testA_11_0_0.pn_2_0.6624_[0.7664 0.5583].png
img: 19 evaluate_data/GlaS/E2CNN/evaluate/testA_11_0_0.pn_3_0.3796_[0.5069 0.2522].png
img: 20 evaluate_data/GlaS/E2CNN/evaluate/testA_11_0_405.pn_0_0.3355_[0.6622 0.0088].png
img: 21 evaluate_data/GlaS/E2CNN/evaluate/testA_11_0_405.pn_1_0.7829_[0.7383 0.8276].png
img: 22 evaluate_data/GlaS/E2CNN/evaluate/testA_11_0_405.pn_2_0.5541_[0.6892 0.419 ].png
img: 23 evaluate_data/GlaS/E2CNN/evaluate/testA_11_0_405.pn_3_0.4657_[0.6546 0.2768].png
img: 24 evaluate_data/GlaS/E2CNN/evaluate/testA_11_126_0.pn_0_0.3096_[0.6192 0.    ].png
img: 25 evaluate_data/GlaS/E2CNN/evaluate/testA_11_126_0.pn_1_0.382_[0.764 0.   ].png
img: 26 evaluate_data/GlaS/E2CNN/evaluate/testA_11_126_0.pn_2_0.3061_[0.6123 0.    ].png
img: 27 evaluate_data/GlaS/E2CNN/evaluate/testA_11_126_0.pn_3_0.3819_[0.7638 0.    ].png
img: 28 evaluate_data/GlaS/E2CNN/evaluate/testA_11_126_405.pn_0_0.3816_[0.7331 0.0301].png
img: 29 evaluate_data/GlaS/E2CNN/evaluate/testA_11_126_405.pn_1_0.4734_[0.7083 0.2385].png
img: 30 evaluate_data/GlaS/E2CNN/evaluate/testA_11_126_405.pn_2_0.5256_[0.7078 0.3434].png
img: 31 evaluate_data/GlaS/E2CNN/evaluate/testA_11_126_405.pn_3_0.3663_[0.7325 0.    ].png
img: 32 evaluate_data/GlaS/E2CNN/evaluate/testA_12_0_0.pn_0_0.6592_[0.4629 0.8555].png
img: 33 evaluate_data/GlaS/E2CNN/evaluate/testA_12_0_0.pn_1_0.5957_[0.4258 0.7656].png
img: 34 evaluate_data/GlaS/E2CNN/evaluate/testA_12_0_0.pn_2_0.5045_[0.3723 0.6367].png
img: 35 evaluate_data/GlaS/E2CNN/evaluate/testA_12_0_0.pn_3_0.6214_[0.4408 0.802 ].png
img: 36 evaluate_data/GlaS/E2CNN/evaluate/testA_12_0_405.pn_0_0.5491_[0.5118 0.5864].png
img: 37 evaluate_data/GlaS/E2CNN/evaluate/testA_12_0_405.pn_1_0.6152_[0.5425 0.6879].png
img: 38 evaluate_data/GlaS/E2CNN/evaluate/testA_12_0_405.pn_2_0.5738_[0.4699 0.6777].png
img: 39 evaluate_data/GlaS/E2CNN/evaluate/testA_12_0_405.pn_3_0.6224_[0.5212 0.7236].png
img: 40 evaluate_data/GlaS/E2CNN/evaluate/testA_12_126_0.pn_0_0.6043_[0.4683 0.7403].png
img: 41 evaluate_data/GlaS/E2CNN/evaluate/testA_12_126_0.pn_1_0.6244_[0.4786 0.7701].png
img: 42 evaluate_data/GlaS/E2CNN/evaluate/testA_12_126_0.pn_2_0.663_[0.5028 0.8232].png
img: 43 evaluate_data/GlaS/E2CNN/evaluate/testA_12_126_0.pn_3_0.5956_[0.4645 0.7267].png
img: 44 evaluate_data/GlaS/E2CNN/evaluate/testA_12_126_405.pn_0_0.6446_[0.5094 0.7798].png
img: 45 evaluate_data/GlaS/E2CNN/evaluate/testA_12_126_405.pn_1_0.6147_[0.4889 0.7405].png
img: 46 evaluate_data/GlaS/E2CNN/evaluate/testA_12_126_405.pn_2_0.6242_[0.5032 0.7451].png
img: 47 evaluate_data/GlaS/E2CNN/evaluate/testA_12_126_405.pn_3_0.6286_[0.4945 0.7628].png
img: 48 evaluate_data/GlaS/E2CNN/evaluate/testA_13_0_0.pn_0_0.5204_[0.5698 0.4709].png
img: 49 evaluate_data/GlaS/E2CNN/evaluate/testA_13_0_0.pn_1_0.6371_[0.6547 0.6195].png
img: 50 evaluate_data/GlaS/E2CNN/evaluate/testA_13_0_0.pn_2_0.6828_[0.6975 0.6682].png
img: 51 evaluate_data/GlaS/E2CNN/evaluate/testA_13_0_0.pn_3_0.6796_[0.6922 0.667 ].png
img: 52 evaluate_data/GlaS/E2CNN/evaluate/testA_13_0_405.pn_0_0.5868_[0.4823 0.6914].png
img: 53 evaluate_data/GlaS/E2CNN/evaluate/testA_13_0_405.pn_1_0.527_[0.4547 0.5993].png
img: 54 evaluate_data/GlaS/E2CNN/evaluate/testA_13_0_405.pn_2_0.5485_[0.405 0.692].png
img: 55 evaluate_data/GlaS/E2CNN/evaluate/testA_13_0_405.pn_3_0.5986_[0.4714 0.7257].png
img: 56 evaluate_data/GlaS/E2CNN/evaluate/testA_13_126_0.pn_0_0.5403_[0.6198 0.4607].png
img: 57 evaluate_data/GlaS/E2CNN/evaluate/testA_13_126_0.pn_1_0.6294_[0.6768 0.5819].png
img: 58 evaluate_data/GlaS/E2CNN/evaluate/testA_13_126_0.pn_2_0.4691_[0.5587 0.3794].png
img: 59 evaluate_data/GlaS/E2CNN/evaluate/testA_13_126_0.pn_3_0.5707_[0.6449 0.4965].png
img: 60 evaluate_data/GlaS/E2CNN/evaluate/testA_13_126_405.pn_0_0.5148_[0.4616 0.568 ].png
img: 61 evaluate_data/GlaS/E2CNN/evaluate/testA_13_126_405.pn_1_0.6326_[0.5057 0.7595].png
img: 62 evaluate_data/GlaS/E2CNN/evaluate/testA_13_126_405.pn_2_0.5389_[0.4757 0.602 ].png
img: 63 evaluate_data/GlaS/E2CNN/evaluate/testA_13_126_405.pn_3_0.5782_[0.4647 0.6916].png
img: 64 evaluate_data/GlaS/E2CNN/evaluate/testA_14_0_0.pn_0_0.6252_[0.6733 0.5771].png
img: 65 evaluate_data/GlaS/E2CNN/evaluate/testA_14_0_0.pn_1_0.5058_[0.5632 0.4484].png
img: 66 evaluate_data/GlaS/E2CNN/evaluate/testA_14_0_0.pn_2_0.5693_[0.5829 0.5556].png
img: 67 evaluate_data/GlaS/E2CNN/evaluate/testA_14_0_0.pn_3_0.6367_[0.6363 0.6371].png
img: 68 evaluate_data/GlaS/E2CNN/evaluate/testA_14_0_405.pn_0_0.7975_[0.7358 0.8591].png
img: 69 evaluate_data/GlaS/E2CNN/evaluate/testA_14_0_405.pn_1_0.5049_[0.578  0.4317].png
img: 70 evaluate_data/GlaS/E2CNN/evaluate/testA_14_0_405.pn_2_0.4721_[0.5498 0.3943].png
img: 71 evaluate_data/GlaS/E2CNN/evaluate/testA_14_0_405.pn_3_0.747_[0.7204 0.7736].png
img: 72 evaluate_data/GlaS/E2CNN/evaluate/testA_14_126_0.pn_0_0.5432_[0.6223 0.464 ].png
img: 73 evaluate_data/GlaS/E2CNN/evaluate/testA_14_126_0.pn_1_0.4852_[0.5605 0.41  ].png
img: 74 evaluate_data/GlaS/E2CNN/evaluate/testA_14_126_0.pn_2_0.4522_[0.5381 0.3662].png
img: 75 evaluate_data/GlaS/E2CNN/evaluate/testA_14_126_0.pn_3_0.6393_[0.6841 0.5946].png
img: 76 evaluate_data/GlaS/E2CNN/evaluate/testA_14_126_405.pn_0_0.6608_[0.6544 0.6672].png
img: 77 evaluate_data/GlaS/E2CNN/evaluate/testA_14_126_405.pn_1_0.7533_[0.734  0.7726].png
img: 78 evaluate_data/GlaS/E2CNN/evaluate/testA_14_126_405.pn_2_0.7877_[0.7174 0.858 ].png
img: 79 evaluate_data/GlaS/E2CNN/evaluate/testA_14_126_405.pn_3_0.5679_[0.5866 0.5491].png
img: 80 evaluate_data/GlaS/E2CNN/evaluate/testA_15_0_0.pn_0_0.229_[0.2603 0.1977].png
img: 81 evaluate_data/GlaS/E2CNN/evaluate/testA_15_0_0.pn_1_0.2119_[0.2728 0.151 ].png
img: 82 evaluate_data/GlaS/E2CNN/evaluate/testA_15_0_0.pn_2_0.6215_[0.4689 0.774 ].png
img: 83 evaluate_data/GlaS/E2CNN/evaluate/testA_15_0_0.pn_3_0.281_[0.292  0.2699].png
img: 84 evaluate_data/GlaS/E2CNN/evaluate/testA_15_0_405.pn_0_0.4417_[0.3925 0.491 ].png
img: 85 evaluate_data/GlaS/E2CNN/evaluate/testA_15_0_405.pn_1_0.6306_[0.5502 0.7111].png
img: 86 evaluate_data/GlaS/E2CNN/evaluate/testA_15_0_405.pn_2_0.4158_[0.3875 0.4441].png
img: 87 evaluate_data/GlaS/E2CNN/evaluate/testA_15_0_405.pn_3_0.5065_[0.3749 0.6381].png
img: 88 evaluate_data/GlaS/E2CNN/evaluate/testA_15_126_0.pn_0_0.2088_[0.2751 0.1425].png
img: 89 evaluate_data/GlaS/E2CNN/evaluate/testA_15_126_0.pn_1_0.2466_[0.287  0.2062].png
img: 90 evaluate_data/GlaS/E2CNN/evaluate/testA_15_126_0.pn_2_0.2174_[0.2831 0.1518].png
img: 91 evaluate_data/GlaS/E2CNN/evaluate/testA_15_126_0.pn_3_0.2846_[0.3056 0.2636].png
img: 92 evaluate_data/GlaS/E2CNN/evaluate/testA_15_126_405.pn_0_0.7138_[0.5385 0.889 ].png
img: 93 evaluate_data/GlaS/E2CNN/evaluate/testA_15_126_405.pn_1_0.484_[0.3263 0.6416].png
img: 94 evaluate_data/GlaS/E2CNN/evaluate/testA_15_126_405.pn_2_0.5574_[0.4557 0.6591].png
img: 95 evaluate_data/GlaS/E2CNN/evaluate/testA_15_126_405.pn_3_0.4833_[0.3221 0.6445].png
img: 96 evaluate_data/GlaS/E2CNN/evaluate/testA_16_0_0.pn_0_0.5512_[0.4731 0.6293].png
img: 97 evaluate_data/GlaS/E2CNN/evaluate/testA_16_0_0.pn_1_0.5349_[0.4678 0.602 ].png
img: 98 evaluate_data/GlaS/E2CNN/evaluate/testA_16_0_0.pn_2_0.5689_[0.4822 0.6555].png
img: 99 evaluate_data/GlaS/E2CNN/evaluate/testA_16_0_0.pn_3_0.5665_[0.4829 0.6502].png
img: 100 evaluate_data/GlaS/E2CNN/evaluate/testA_16_0_191.pn_0_0.2433_[0.3627 0.1238].png
img: 101 evaluate_data/GlaS/E2CNN/evaluate/testA_16_0_191.pn_1_0.2439_[0.3982 0.0896].png
img: 102 evaluate_data/GlaS/E2CNN/evaluate/testA_16_0_191.pn_2_0.4158_[0.4356 0.396 ].png
img: 103 evaluate_data/GlaS/E2CNN/evaluate/testA_16_0_191.pn_3_0.2393_[0.315  0.1636].png
img: 104 evaluate_data/GlaS/E2CNN/evaluate/testA_16_38_0.pn_0_0.5596_[0.4313 0.6878].png
img: 105 evaluate_data/GlaS/E2CNN/evaluate/testA_16_38_0.pn_1_0.3225_[0.3085 0.3365].png
img: 106 evaluate_data/GlaS/E2CNN/evaluate/testA_16_38_0.pn_2_0.4222_[0.3377 0.5066].png
img: 107 evaluate_data/GlaS/E2CNN/evaluate/testA_16_38_0.pn_3_0.5273_[0.4502 0.6044].png
img: 108 evaluate_data/GlaS/E2CNN/evaluate/testA_16_38_191.pn_0_0.2276_[0.2442 0.211 ].png
img: 109 evaluate_data/GlaS/E2CNN/evaluate/testA_16_38_191.pn_1_0.2445_[0.3625 0.1265].png
img: 110 evaluate_data/GlaS/E2CNN/evaluate/testA_16_38_191.pn_2_0.387_[0.4975 0.2765].png
img: 111 evaluate_data/GlaS/E2CNN/evaluate/testA_16_38_191.pn_3_0.2855_[0.3657 0.2052].png
img: 112 evaluate_data/GlaS/E2CNN/evaluate/testA_17_0_0.pn_0_0.4058_[0.2847 0.5268].png
img: 113 evaluate_data/GlaS/E2CNN/evaluate/testA_17_0_0.pn_1_0.3194_[0.219  0.4198].png
img: 114 evaluate_data/GlaS/E2CNN/evaluate/testA_17_0_0.pn_2_0.3518_[0.2499 0.4536].png
img: 115 evaluate_data/GlaS/E2CNN/evaluate/testA_17_0_0.pn_3_0.3591_[0.2594 0.4589].png
img: 116 evaluate_data/GlaS/E2CNN/evaluate/testA_17_0_405.pn_0_0.554_[0.527 0.581].png
img: 117 evaluate_data/GlaS/E2CNN/evaluate/testA_17_0_405.pn_1_0.6108_[0.5516 0.6699].png
img: 118 evaluate_data/GlaS/E2CNN/evaluate/testA_17_0_405.pn_2_0.6218_[0.5418 0.7019].png
img: 119 evaluate_data/GlaS/E2CNN/evaluate/testA_17_0_405.pn_3_0.5494_[0.4727 0.6262].png
img: 120 evaluate_data/GlaS/E2CNN/evaluate/testA_17_126_0.pn_0_0.3333_[0.2654 0.4011].png
img: 121 evaluate_data/GlaS/E2CNN/evaluate/testA_17_126_0.pn_1_0.241_[0.2063 0.2757].png
img: 122 evaluate_data/GlaS/E2CNN/evaluate/testA_17_126_0.pn_2_0.0977_[0.1872 0.0083].png
img: 123 evaluate_data/GlaS/E2CNN/evaluate/testA_17_126_0.pn_3_0.2434_[0.2047 0.2822].png
img: 124 evaluate_data/GlaS/E2CNN/evaluate/testA_17_126_405.pn_0_0.4802_[0.4723 0.4881].png
img: 125 evaluate_data/GlaS/E2CNN/evaluate/testA_17_126_405.pn_1_0.643_[0.5384 0.7476].png
img: 126 evaluate_data/GlaS/E2CNN/evaluate/testA_17_126_405.pn_2_0.6109_[0.5143 0.7074].png
img: 127 evaluate_data/GlaS/E2CNN/evaluate/testA_17_126_405.pn_3_0.5537_[0.4607 0.6467].png
img: 128 evaluate_data/GlaS/E2CNN/evaluate/testA_18_0_0.pn_0_0.5277_[0.6037 0.4517].png
img: 129 evaluate_data/GlaS/E2CNN/evaluate/testA_18_0_0.pn_1_0.6874_[0.6757 0.6991].png
img: 130 evaluate_data/GlaS/E2CNN/evaluate/testA_18_0_0.pn_2_0.4325_[0.5024 0.3626].png
img: 131 evaluate_data/GlaS/E2CNN/evaluate/testA_18_0_0.pn_3_0.4162_[0.4617 0.3708].png
img: 132 evaluate_data/GlaS/E2CNN/evaluate/testA_18_0_405.pn_0_0.4855_[0.4128 0.5582].png
img: 133 evaluate_data/GlaS/E2CNN/evaluate/testA_18_0_405.pn_1_0.5269_[0.4538 0.6   ].png
img: 134 evaluate_data/GlaS/E2CNN/evaluate/testA_18_0_405.pn_2_0.5916_[0.564  0.6193].png
img: 135 evaluate_data/GlaS/E2CNN/evaluate/testA_18_0_405.pn_3_0.5395_[0.5153 0.5636].png
img: 136 evaluate_data/GlaS/E2CNN/evaluate/testA_18_126_0.pn_0_0.6054_[0.6085 0.6023].png
img: 137 evaluate_data/GlaS/E2CNN/evaluate/testA_18_126_0.pn_1_0.4235_[0.3934 0.4537].png
img: 138 evaluate_data/GlaS/E2CNN/evaluate/testA_18_126_0.pn_2_0.4853_[0.4671 0.5036].png
img: 139 evaluate_data/GlaS/E2CNN/evaluate/testA_18_126_0.pn_3_0.4435_[0.4678 0.4193].png
img: 140 evaluate_data/GlaS/E2CNN/evaluate/testA_18_126_405.pn_0_0.4298_[0.3259 0.5337].png
img: 141 evaluate_data/GlaS/E2CNN/evaluate/testA_18_126_405.pn_1_0.6386_[0.576  0.7013].png
img: 142 evaluate_data/GlaS/E2CNN/evaluate/testA_18_126_405.pn_2_0.4649_[0.3626 0.5672].png
img: 143 evaluate_data/GlaS/E2CNN/evaluate/testA_18_126_405.pn_3_0.4196_[0.2815 0.5576].png
img: 144 evaluate_data/GlaS/E2CNN/evaluate/testA_19_0_0.pn_0_0.5759_[0.4793 0.6726].png
img: 145 evaluate_data/GlaS/E2CNN/evaluate/testA_19_0_0.pn_1_0.2565_[0.4155 0.0976].png
img: 146 evaluate_data/GlaS/E2CNN/evaluate/testA_19_0_0.pn_2_0.6118_[0.5021 0.7216].png
img: 147 evaluate_data/GlaS/E2CNN/evaluate/testA_19_0_0.pn_3_0.6377_[0.5258 0.7495].png
img: 148 evaluate_data/GlaS/E2CNN/evaluate/testA_19_0_405.pn_0_0.6195_[0.5259 0.7132].png
img: 149 evaluate_data/GlaS/E2CNN/evaluate/testA_19_0_405.pn_1_0.6068_[0.5231 0.6904].png
img: 150 evaluate_data/GlaS/E2CNN/evaluate/testA_19_0_405.pn_2_0.6641_[0.5511 0.7771].png
img: 151 evaluate_data/GlaS/E2CNN/evaluate/testA_19_0_405.pn_3_0.4596_[0.4667 0.4525].png
img: 152 evaluate_data/GlaS/E2CNN/evaluate/testA_19_126_0.pn_0_0.4881_[0.386  0.5902].png
img: 153 evaluate_data/GlaS/E2CNN/evaluate/testA_19_126_0.pn_1_0.646_[0.5349 0.757 ].png
img: 154 evaluate_data/GlaS/E2CNN/evaluate/testA_19_126_0.pn_2_0.6456_[0.527  0.7642].png
img: 155 evaluate_data/GlaS/E2CNN/evaluate/testA_19_126_0.pn_3_0.7033_[0.575  0.8317].png
img: 156 evaluate_data/GlaS/E2CNN/evaluate/testA_19_126_405.pn_0_0.7038_[0.5663 0.8413].png
img: 157 evaluate_data/GlaS/E2CNN/evaluate/testA_19_126_405.pn_1_0.7106_[0.5447 0.8765].png
img: 158 evaluate_data/GlaS/E2CNN/evaluate/testA_19_126_405.pn_2_0.7026_[0.5456 0.8596].png
img: 159 evaluate_data/GlaS/E2CNN/evaluate/testA_19_126_405.pn_3_0.6907_[0.5351 0.8463].png
img: 160 evaluate_data/GlaS/E2CNN/evaluate/testA_1_0_0.pn_0_0.3069_[0.1167 0.4971].png
img: 161 evaluate_data/GlaS/E2CNN/evaluate/testA_1_0_0.pn_1_0.4055_[0.1722 0.6388].png
img: 162 evaluate_data/GlaS/E2CNN/evaluate/testA_1_0_0.pn_2_0.2974_[0.0606 0.5341].png
img: 163 evaluate_data/GlaS/E2CNN/evaluate/testA_1_0_0.pn_3_0.3176_[0.0892 0.5461].png
img: 164 evaluate_data/GlaS/E2CNN/evaluate/testA_1_0_405.pn_0_0.2321_[0.0532 0.4109].png
img: 165 evaluate_data/GlaS/E2CNN/evaluate/testA_1_0_405.pn_1_0.3318_[0.1356 0.528 ].png
img: 166 evaluate_data/GlaS/E2CNN/evaluate/testA_1_0_405.pn_2_0.2057_[0.0633 0.348 ].png
img: 167 evaluate_data/GlaS/E2CNN/evaluate/testA_1_0_405.pn_3_0.3302_[0.1353 0.5251].png
img: 168 evaluate_data/GlaS/E2CNN/evaluate/testA_1_126_0.pn_0_0.2756_[0.1964 0.3548].png
img: 169 evaluate_data/GlaS/E2CNN/evaluate/testA_1_126_0.pn_1_0.3976_[0.2295 0.5656].png
img: 170 evaluate_data/GlaS/E2CNN/evaluate/testA_1_126_0.pn_2_0.3575_[0.2106 0.5044].png
img: 171 evaluate_data/GlaS/E2CNN/evaluate/testA_1_126_0.pn_3_0.3997_[0.2296 0.5698].png
img: 172 evaluate_data/GlaS/E2CNN/evaluate/testA_1_126_405.pn_0_0.1618_[0.0622 0.2613].png
img: 173 evaluate_data/GlaS/E2CNN/evaluate/testA_1_126_405.pn_1_0.2165_[0.0682 0.3647].png
img: 174 evaluate_data/GlaS/E2CNN/evaluate/testA_1_126_405.pn_2_0.112_[0.053 0.171].png
img: 175 evaluate_data/GlaS/E2CNN/evaluate/testA_1_126_405.pn_3_0.1682_[0.0526 0.2838].png
img: 176 evaluate_data/GlaS/E2CNN/evaluate/testA_20_0_0.pn_0_0.3808_[0.3152 0.4465].png
img: 177 evaluate_data/GlaS/E2CNN/evaluate/testA_20_0_0.pn_1_0.722_[0.6942 0.7499].png
img: 178 evaluate_data/GlaS/E2CNN/evaluate/testA_20_0_0.pn_2_0.4758_[0.3804 0.5711].png
img: 179 evaluate_data/GlaS/E2CNN/evaluate/testA_20_0_0.pn_3_0.4316_[0.3345 0.5287].png
img: 180 evaluate_data/GlaS/E2CNN/evaluate/testA_20_0_405.pn_0_0.6027_[0.4367 0.7688].png
img: 181 evaluate_data/GlaS/E2CNN/evaluate/testA_20_0_405.pn_1_0.3637_[0.3098 0.4176].png
img: 182 evaluate_data/GlaS/E2CNN/evaluate/testA_20_0_405.pn_2_0.3373_[0.1816 0.493 ].png
img: 183 evaluate_data/GlaS/E2CNN/evaluate/testA_20_0_405.pn_3_0.3614_[0.3092 0.4136].png
img: 184 evaluate_data/GlaS/E2CNN/evaluate/testA_20_126_0.pn_0_0.4282_[0.3765 0.4799].png
img: 185 evaluate_data/GlaS/E2CNN/evaluate/testA_20_126_0.pn_1_0.3838_[0.3563 0.4113].png
img: 186 evaluate_data/GlaS/E2CNN/evaluate/testA_20_126_0.pn_2_0.4111_[0.4191 0.4031].png
img: 187 evaluate_data/GlaS/E2CNN/evaluate/testA_20_126_0.pn_3_0.4386_[0.4651 0.4121].png
img: 188 evaluate_data/GlaS/E2CNN/evaluate/testA_20_126_405.pn_0_0.4918_[0.51   0.4737].png
img: 189 evaluate_data/GlaS/E2CNN/evaluate/testA_20_126_405.pn_1_0.3456_[0.3583 0.333 ].png
img: 190 evaluate_data/GlaS/E2CNN/evaluate/testA_20_126_405.pn_2_0.4628_[0.4648 0.4608].png
img: 191 evaluate_data/GlaS/E2CNN/evaluate/testA_20_126_405.pn_3_0.3837_[0.4739 0.2934].png
img: 192 evaluate_data/GlaS/E2CNN/evaluate/testA_21_0_0.pn_0_0.4224_[0.4459 0.3989].png
img: 193 evaluate_data/GlaS/E2CNN/evaluate/testA_21_0_0.pn_1_0.6145_[0.5853 0.6437].png
img: 194 evaluate_data/GlaS/E2CNN/evaluate/testA_21_0_0.pn_2_0.5617_[0.5692 0.5542].png
img: 195 evaluate_data/GlaS/E2CNN/evaluate/testA_21_0_0.pn_3_0.5618_[0.5713 0.5523].png
img: 196 evaluate_data/GlaS/E2CNN/evaluate/testA_21_0_405.pn_0_0.635_[0.6047 0.6653].png
img: 197 evaluate_data/GlaS/E2CNN/evaluate/testA_21_0_405.pn_1_0.6307_[0.6025 0.6589].png
img: 198 evaluate_data/GlaS/E2CNN/evaluate/testA_21_0_405.pn_2_0.3745_[0.3467 0.4024].png
img: 199 evaluate_data/GlaS/E2CNN/evaluate/testA_21_0_405.pn_3_0.6534_[0.6189 0.6879].png
img: 200 evaluate_data/GlaS/E2CNN/evaluate/testA_21_126_0.pn_0_0.5894_[0.471  0.7079].png
img: 201 evaluate_data/GlaS/E2CNN/evaluate/testA_21_126_0.pn_1_0.4137_[0.2643 0.5632].png
img: 202 evaluate_data/GlaS/E2CNN/evaluate/testA_21_126_0.pn_2_0.3853_[0.2808 0.4898].png
img: 203 evaluate_data/GlaS/E2CNN/evaluate/testA_21_126_0.pn_3_0.6508_[0.5216 0.7799].png
img: 204 evaluate_data/GlaS/E2CNN/evaluate/testA_21_126_405.pn_0_0.4464_[0.3611 0.5317].png
img: 205 evaluate_data/GlaS/E2CNN/evaluate/testA_21_126_405.pn_1_0.3404_[0.2728 0.4081].png
img: 206 evaluate_data/GlaS/E2CNN/evaluate/testA_21_126_405.pn_2_0.6721_[0.605  0.7391].png
img: 207 evaluate_data/GlaS/E2CNN/evaluate/testA_21_126_405.pn_3_0.3172_[0.2522 0.3821].png
img: 208 evaluate_data/GlaS/E2CNN/evaluate/testA_22_0_0.pn_0_0.6119_[0.4978 0.7261].png
img: 209 evaluate_data/GlaS/E2CNN/evaluate/testA_22_0_0.pn_1_0.4015_[0.3882 0.4149].png
img: 210 evaluate_data/GlaS/E2CNN/evaluate/testA_22_0_0.pn_2_0.4906_[0.3996 0.5817].png
img: 211 evaluate_data/GlaS/E2CNN/evaluate/testA_22_0_0.pn_3_0.4107_[0.3662 0.4552].png
img: 212 evaluate_data/GlaS/E2CNN/evaluate/testA_22_0_405.pn_0_0.4413_[0.3503 0.5322].png
img: 213 evaluate_data/GlaS/E2CNN/evaluate/testA_22_0_405.pn_1_0.6127_[0.4438 0.7817].png
img: 214 evaluate_data/GlaS/E2CNN/evaluate/testA_22_0_405.pn_2_0.3541_[0.327  0.3811].png
img: 215 evaluate_data/GlaS/E2CNN/evaluate/testA_22_0_405.pn_3_0.464_[0.3687 0.5592].png
img: 216 evaluate_data/GlaS/E2CNN/evaluate/testA_22_126_0.pn_0_0.4345_[0.4737 0.3954].png
img: 217 evaluate_data/GlaS/E2CNN/evaluate/testA_22_126_0.pn_1_0.2246_[0.4205 0.0288].png
img: 218 evaluate_data/GlaS/E2CNN/evaluate/testA_22_126_0.pn_2_0.5607_[0.5257 0.5958].png
img: 219 evaluate_data/GlaS/E2CNN/evaluate/testA_22_126_0.pn_3_0.4502_[0.463  0.4374].png
img: 220 evaluate_data/GlaS/E2CNN/evaluate/testA_22_126_405.pn_0_0.4413_[0.3795 0.503 ].png
img: 221 evaluate_data/GlaS/E2CNN/evaluate/testA_22_126_405.pn_1_0.2972_[0.3578 0.2367].png
img: 222 evaluate_data/GlaS/E2CNN/evaluate/testA_22_126_405.pn_2_0.3143_[0.3446 0.2841].png
img: 223 evaluate_data/GlaS/E2CNN/evaluate/testA_22_126_405.pn_3_0.3943_[0.3546 0.4341].png
img: 224 evaluate_data/GlaS/E2CNN/evaluate/testA_23_0_0.pn_0_0.4426_[0.3485 0.5366].png
img: 225 evaluate_data/GlaS/E2CNN/evaluate/testA_23_0_0.pn_1_0.3701_[0.3211 0.4191].png
img: 226 evaluate_data/GlaS/E2CNN/evaluate/testA_23_0_0.pn_2_0.6486_[0.5033 0.7938].png
img: 227 evaluate_data/GlaS/E2CNN/evaluate/testA_23_0_0.pn_3_0.6624_[0.5345 0.7903].png
img: 228 evaluate_data/GlaS/E2CNN/evaluate/testA_23_0_405.pn_0_0.4867_[0.4106 0.5629].png
img: 229 evaluate_data/GlaS/E2CNN/evaluate/testA_23_0_405.pn_1_0.4511_[0.3546 0.5476].png
img: 230 evaluate_data/GlaS/E2CNN/evaluate/testA_23_0_405.pn_2_0.4546_[0.3626 0.5467].png
img: 231 evaluate_data/GlaS/E2CNN/evaluate/testA_23_0_405.pn_3_0.5007_[0.4198 0.5815].png
img: 232 evaluate_data/GlaS/E2CNN/evaluate/testA_23_126_0.pn_0_0.6046_[0.5081 0.701 ].png
img: 233 evaluate_data/GlaS/E2CNN/evaluate/testA_23_126_0.pn_1_0.6819_[0.5576 0.8061].png
img: 234 evaluate_data/GlaS/E2CNN/evaluate/testA_23_126_0.pn_2_0.5711_[0.4925 0.6497].png
img: 235 evaluate_data/GlaS/E2CNN/evaluate/testA_23_126_0.pn_3_0.5024_[0.4706 0.5341].png
img: 236 evaluate_data/GlaS/E2CNN/evaluate/testA_23_126_405.pn_0_0.5204_[0.3682 0.6725].png
img: 237 evaluate_data/GlaS/E2CNN/evaluate/testA_23_126_405.pn_1_0.4152_[0.4165 0.4139].png
img: 238 evaluate_data/GlaS/E2CNN/evaluate/testA_23_126_405.pn_2_0.6956_[0.5417 0.8495].png
img: 239 evaluate_data/GlaS/E2CNN/evaluate/testA_23_126_405.pn_3_0.4414_[0.2797 0.603 ].png
img: 240 evaluate_data/GlaS/E2CNN/evaluate/testA_24_0_0.pn_0_0.4128_[0.4209 0.4047].png
img: 241 evaluate_data/GlaS/E2CNN/evaluate/testA_24_0_0.pn_1_0.4887_[0.561  0.4164].png
img: 242 evaluate_data/GlaS/E2CNN/evaluate/testA_24_0_0.pn_2_0.4449_[0.5051 0.3847].png
img: 243 evaluate_data/GlaS/E2CNN/evaluate/testA_24_0_0.pn_3_0.6272_[0.6428 0.6116].png
img: 244 evaluate_data/GlaS/E2CNN/evaluate/testA_24_0_405.pn_0_0.4232_[0.3113 0.5351].png
img: 245 evaluate_data/GlaS/E2CNN/evaluate/testA_24_0_405.pn_1_0.1353_[0.2707 0.    ].png
img: 246 evaluate_data/GlaS/E2CNN/evaluate/testA_24_0_405.pn_2_0.3961_[0.3368 0.4553].png
img: 247 evaluate_data/GlaS/E2CNN/evaluate/testA_24_0_405.pn_3_0.4332_[0.327  0.5393].png
img: 248 evaluate_data/GlaS/E2CNN/evaluate/testA_24_126_0.pn_0_0.4842_[0.4343 0.5341].png
img: 249 evaluate_data/GlaS/E2CNN/evaluate/testA_24_126_0.pn_1_0.5776_[0.5351 0.6201].png
img: 250 evaluate_data/GlaS/E2CNN/evaluate/testA_24_126_0.pn_2_0.6269_[0.5844 0.6695].png
img: 251 evaluate_data/GlaS/E2CNN/evaluate/testA_24_126_0.pn_3_0.4636_[0.4135 0.5137].png
img: 252 evaluate_data/GlaS/E2CNN/evaluate/testA_24_126_405.pn_0_0.1288_[0.2566 0.0009].png
img: 253 evaluate_data/GlaS/E2CNN/evaluate/testA_24_126_405.pn_1_0.223_[0.2802 0.1658].png
img: 254 evaluate_data/GlaS/E2CNN/evaluate/testA_24_126_405.pn_2_0.2897_[0.2972 0.2822].png
img: 255 evaluate_data/GlaS/E2CNN/evaluate/testA_24_126_405.pn_3_0.3624_[0.3228 0.402 ].png
img: 256 evaluate_data/GlaS/E2CNN/evaluate/testA_25_0_0.pn_0_0.3325_[0.1594 0.5055].png
img: 257 evaluate_data/GlaS/E2CNN/evaluate/testA_25_0_0.pn_1_0.3377_[0.2239 0.4515].png
img: 258 evaluate_data/GlaS/E2CNN/evaluate/testA_25_0_0.pn_2_0.3433_[0.2179 0.4688].png
img: 259 evaluate_data/GlaS/E2CNN/evaluate/testA_25_0_0.pn_3_0.3951_[0.2792 0.5109].png
img: 260 evaluate_data/GlaS/E2CNN/evaluate/testA_25_0_405.pn_0_0.6223_[0.518  0.7266].png
img: 261 evaluate_data/GlaS/E2CNN/evaluate/testA_25_0_405.pn_1_0.479_[0.4583 0.4998].png
img: 262 evaluate_data/GlaS/E2CNN/evaluate/testA_25_0_405.pn_2_0.5316_[0.4367 0.6266].png
img: 263 evaluate_data/GlaS/E2CNN/evaluate/testA_25_0_405.pn_3_0.5823_[0.4997 0.665 ].png
img: 264 evaluate_data/GlaS/E2CNN/evaluate/testA_25_126_0.pn_0_0.4476_[0.2886 0.6066].png
img: 265 evaluate_data/GlaS/E2CNN/evaluate/testA_25_126_0.pn_1_0.228_[0.2568 0.1993].png
img: 266 evaluate_data/GlaS/E2CNN/evaluate/testA_25_126_0.pn_2_0.4348_[0.3238 0.5458].png
img: 267 evaluate_data/GlaS/E2CNN/evaluate/testA_25_126_0.pn_3_0.4994_[0.3221 0.6767].png
img: 268 evaluate_data/GlaS/E2CNN/evaluate/testA_25_126_405.pn_0_0.4349_[0.3418 0.5281].png
img: 269 evaluate_data/GlaS/E2CNN/evaluate/testA_25_126_405.pn_1_0.6105_[0.5015 0.7195].png
img: 270 evaluate_data/GlaS/E2CNN/evaluate/testA_25_126_405.pn_2_0.6455_[0.5318 0.7593].png
img: 271 evaluate_data/GlaS/E2CNN/evaluate/testA_25_126_405.pn_3_0.3849_[0.2537 0.5162].png
img: 272 evaluate_data/GlaS/E2CNN/evaluate/testA_26_0_0.pn_0_0.4898_[0.7481 0.2315].png
img: 273 evaluate_data/GlaS/E2CNN/evaluate/testA_26_0_0.pn_1_0.3636_[0.7273 0.    ].png
img: 274 evaluate_data/GlaS/E2CNN/evaluate/testA_26_0_0.pn_2_0.3509_[0.6321 0.0698].png
img: 275 evaluate_data/GlaS/E2CNN/evaluate/testA_26_0_0.pn_3_0.6308_[0.7701 0.4914].png
img: 276 evaluate_data/GlaS/E2CNN/evaluate/testA_26_0_405.pn_0_0.4816_[0.5292 0.434 ].png
img: 277 evaluate_data/GlaS/E2CNN/evaluate/testA_26_0_405.pn_1_0.5837_[0.6044 0.563 ].png
img: 278 evaluate_data/GlaS/E2CNN/evaluate/testA_26_0_405.pn_2_0.4351_[0.4407 0.4295].png
img: 279 evaluate_data/GlaS/E2CNN/evaluate/testA_26_0_405.pn_3_0.3605_[0.4017 0.3194].png
img: 280 evaluate_data/GlaS/E2CNN/evaluate/testA_26_126_0.pn_0_0.3846_[0.7692 0.    ].png
img: 281 evaluate_data/GlaS/E2CNN/evaluate/testA_26_126_0.pn_1_0.3976_[0.7952 0.    ].png
img: 282 evaluate_data/GlaS/E2CNN/evaluate/testA_26_126_0.pn_2_0.3405_[0.6809 0.    ].png
img: 283 evaluate_data/GlaS/E2CNN/evaluate/testA_26_126_0.pn_3_0.3751_[0.7502 0.    ].png
img: 284 evaluate_data/GlaS/E2CNN/evaluate/testA_26_126_405.pn_0_0.4656_[0.443  0.4881].png
img: 285 evaluate_data/GlaS/E2CNN/evaluate/testA_26_126_405.pn_1_0.6865_[0.6274 0.7456].png
img: 286 evaluate_data/GlaS/E2CNN/evaluate/testA_26_126_405.pn_2_0.6064_[0.5831 0.6297].png
img: 287 evaluate_data/GlaS/E2CNN/evaluate/testA_26_126_405.pn_3_0.3755_[0.3773 0.3738].png
img: 288 evaluate_data/GlaS/E2CNN/evaluate/testA_27_0_0.pn_0_0.6764_[0.5144 0.8383].png
img: 289 evaluate_data/GlaS/E2CNN/evaluate/testA_27_0_0.pn_1_0.4989_[0.4018 0.5959].png
img: 290 evaluate_data/GlaS/E2CNN/evaluate/testA_27_0_0.pn_2_0.6075_[0.4857 0.7293].png
img: 291 evaluate_data/GlaS/E2CNN/evaluate/testA_27_0_0.pn_3_0.6769_[0.5541 0.7997].png
img: 292 evaluate_data/GlaS/E2CNN/evaluate/testA_27_0_405.pn_0_0.4951_[0.4354 0.5548].png
img: 293 evaluate_data/GlaS/E2CNN/evaluate/testA_27_0_405.pn_1_0.6888_[0.5306 0.8471].png
img: 294 evaluate_data/GlaS/E2CNN/evaluate/testA_27_0_405.pn_2_0.6435_[0.5022 0.7849].png
img: 295 evaluate_data/GlaS/E2CNN/evaluate/testA_27_0_405.pn_3_0.7107_[0.5463 0.875 ].png
img: 296 evaluate_data/GlaS/E2CNN/evaluate/testA_27_126_0.pn_0_0.6017_[0.5017 0.7016].png
img: 297 evaluate_data/GlaS/E2CNN/evaluate/testA_27_126_0.pn_1_0.627_[0.5097 0.7443].png
img: 298 evaluate_data/GlaS/E2CNN/evaluate/testA_27_126_0.pn_2_0.492_[0.452  0.5319].png
img: 299 evaluate_data/GlaS/E2CNN/evaluate/testA_27_126_0.pn_3_0.6467_[0.5375 0.756 ].png
img: 300 evaluate_data/GlaS/E2CNN/evaluate/testA_27_126_405.pn_0_0.6507_[0.5341 0.7673].png
img: 301 evaluate_data/GlaS/E2CNN/evaluate/testA_27_126_405.pn_1_0.5729_[0.4787 0.6671].png
img: 302 evaluate_data/GlaS/E2CNN/evaluate/testA_27_126_405.pn_2_0.6964_[0.5771 0.8158].png
img: 303 evaluate_data/GlaS/E2CNN/evaluate/testA_27_126_405.pn_3_0.7097_[0.5717 0.8478].png
img: 304 evaluate_data/GlaS/E2CNN/evaluate/testA_28_0_0.pn_0_0.4347_[0.2906 0.5788].png
img: 305 evaluate_data/GlaS/E2CNN/evaluate/testA_28_0_0.pn_1_0.3966_[0.3204 0.4727].png
img: 306 evaluate_data/GlaS/E2CNN/evaluate/testA_28_0_0.pn_2_0.4025_[0.3244 0.4805].png
img: 307 evaluate_data/GlaS/E2CNN/evaluate/testA_28_0_0.pn_3_0.371_[0.1641 0.5778].png
img: 308 evaluate_data/GlaS/E2CNN/evaluate/testA_28_0_405.pn_0_0.6301_[0.506  0.7543].png
img: 309 evaluate_data/GlaS/E2CNN/evaluate/testA_28_0_405.pn_1_0.433_[0.3282 0.5378].png
img: 310 evaluate_data/GlaS/E2CNN/evaluate/testA_28_0_405.pn_2_0.583_[0.493 0.673].png
img: 311 evaluate_data/GlaS/E2CNN/evaluate/testA_28_0_405.pn_3_0.6917_[0.557  0.8263].png
img: 312 evaluate_data/GlaS/E2CNN/evaluate/testA_28_126_0.pn_0_0.6006_[0.4509 0.7504].png
img: 313 evaluate_data/GlaS/E2CNN/evaluate/testA_28_126_0.pn_1_0.4242_[0.3617 0.4867].png
img: 314 evaluate_data/GlaS/E2CNN/evaluate/testA_28_126_0.pn_2_0.5043_[0.4044 0.6042].png
img: 315 evaluate_data/GlaS/E2CNN/evaluate/testA_28_126_0.pn_3_0.5815_[0.4408 0.7223].png
img: 316 evaluate_data/GlaS/E2CNN/evaluate/testA_28_126_405.pn_0_0.6386_[0.5549 0.7223].png
img: 317 evaluate_data/GlaS/E2CNN/evaluate/testA_28_126_405.pn_1_0.6038_[0.5393 0.6683].png
img: 318 evaluate_data/GlaS/E2CNN/evaluate/testA_28_126_405.pn_2_0.4489_[0.3147 0.5831].png
img: 319 evaluate_data/GlaS/E2CNN/evaluate/testA_28_126_405.pn_3_0.6408_[0.5475 0.7342].png
img: 320 evaluate_data/GlaS/E2CNN/evaluate/testA_29_0_0.pn_0_0.4555_[0.4984 0.4127].png
img: 321 evaluate_data/GlaS/E2CNN/evaluate/testA_29_0_0.pn_1_0.594_[0.5638 0.6241].png
img: 322 evaluate_data/GlaS/E2CNN/evaluate/testA_29_0_0.pn_2_0.4827_[0.5081 0.4572].png
img: 323 evaluate_data/GlaS/E2CNN/evaluate/testA_29_0_0.pn_3_0.5466_[0.5448 0.5484].png
img: 324 evaluate_data/GlaS/E2CNN/evaluate/testA_29_0_405.pn_0_0.671_[0.5963 0.7458].png
img: 325 evaluate_data/GlaS/E2CNN/evaluate/testA_29_0_405.pn_1_0.7405_[0.6264 0.8546].png
img: 326 evaluate_data/GlaS/E2CNN/evaluate/testA_29_0_405.pn_2_0.7323_[0.6251 0.8394].png
img: 327 evaluate_data/GlaS/E2CNN/evaluate/testA_29_0_405.pn_3_0.3361_[0.44   0.2322].png
img: 328 evaluate_data/GlaS/E2CNN/evaluate/testA_29_126_0.pn_0_0.5272_[0.5649 0.4896].png
img: 329 evaluate_data/GlaS/E2CNN/evaluate/testA_29_126_0.pn_1_0.5847_[0.5622 0.6073].png
img: 330 evaluate_data/GlaS/E2CNN/evaluate/testA_29_126_0.pn_2_0.4848_[0.4707 0.499 ].png
img: 331 evaluate_data/GlaS/E2CNN/evaluate/testA_29_126_0.pn_3_0.5816_[0.5918 0.5714].png
img: 332 evaluate_data/GlaS/E2CNN/evaluate/testA_29_126_405.pn_0_0.6012_[0.5968 0.6056].png
img: 333 evaluate_data/GlaS/E2CNN/evaluate/testA_29_126_405.pn_1_0.3158_[0.4193 0.2122].png
img: 334 evaluate_data/GlaS/E2CNN/evaluate/testA_29_126_405.pn_2_0.7008_[0.6369 0.7646].png
img: 335 evaluate_data/GlaS/E2CNN/evaluate/testA_29_126_405.pn_3_0.4869_[0.5416 0.4321].png
img: 336 evaluate_data/GlaS/E2CNN/evaluate/testA_2_0_0.pn_0_0.6187_[0.5838 0.6537].png
img: 337 evaluate_data/GlaS/E2CNN/evaluate/testA_2_0_0.pn_1_0.5406_[0.5292 0.5521].png
img: 338 evaluate_data/GlaS/E2CNN/evaluate/testA_2_0_0.pn_2_0.7798_[0.6558 0.9039].png
img: 339 evaluate_data/GlaS/E2CNN/evaluate/testA_2_0_0.pn_3_0.5372_[0.5795 0.4948].png
img: 340 evaluate_data/GlaS/E2CNN/evaluate/testA_2_0_200.pn_0_0.6702_[0.6557 0.6848].png
img: 341 evaluate_data/GlaS/E2CNN/evaluate/testA_2_0_200.pn_1_0.4234_[0.5878 0.2591].png
img: 342 evaluate_data/GlaS/E2CNN/evaluate/testA_2_0_200.pn_2_0.5475_[0.614  0.4811].png
img: 343 evaluate_data/GlaS/E2CNN/evaluate/testA_2_0_200.pn_3_0.671_[0.6532 0.6888].png
img: 344 evaluate_data/GlaS/E2CNN/evaluate/testA_2_50_0.pn_0_0.7623_[0.6416 0.8829].png
img: 345 evaluate_data/GlaS/E2CNN/evaluate/testA_2_50_0.pn_1_0.5404_[0.4883 0.5925].png
img: 346 evaluate_data/GlaS/E2CNN/evaluate/testA_2_50_0.pn_2_0.7382_[0.6287 0.8477].png
img: 347 evaluate_data/GlaS/E2CNN/evaluate/testA_2_50_0.pn_3_0.7468_[0.6321 0.8615].png
img: 348 evaluate_data/GlaS/E2CNN/evaluate/testA_2_50_200.pn_0_0.4935_[0.5775 0.4094].png
img: 349 evaluate_data/GlaS/E2CNN/evaluate/testA_2_50_200.pn_1_0.6668_[0.6718 0.6618].png
img: 350 evaluate_data/GlaS/E2CNN/evaluate/testA_2_50_200.pn_2_0.4616_[0.5204 0.4029].png
img: 351 evaluate_data/GlaS/E2CNN/evaluate/testA_2_50_200.pn_3_0.6057_[0.6421 0.5694].png
img: 352 evaluate_data/GlaS/E2CNN/evaluate/testA_30_0_0.pn_0_0.5743_[0.4093 0.7393].png
img: 353 evaluate_data/GlaS/E2CNN/evaluate/testA_30_0_0.pn_1_0.7076_[0.5423 0.8728].png
img: 354 evaluate_data/GlaS/E2CNN/evaluate/testA_30_0_0.pn_2_0.5959_[0.4447 0.7471].png
img: 355 evaluate_data/GlaS/E2CNN/evaluate/testA_30_0_0.pn_3_0.6337_[0.4644 0.803 ].png
img: 356 evaluate_data/GlaS/E2CNN/evaluate/testA_30_0_405.pn_0_0.6642_[0.5671 0.7614].png
img: 357 evaluate_data/GlaS/E2CNN/evaluate/testA_30_0_405.pn_1_0.6609_[0.5586 0.7632].png
img: 358 evaluate_data/GlaS/E2CNN/evaluate/testA_30_0_405.pn_2_0.7396_[0.6049 0.8743].png
img: 359 evaluate_data/GlaS/E2CNN/evaluate/testA_30_0_405.pn_3_0.6572_[0.5587 0.7557].png
img: 360 evaluate_data/GlaS/E2CNN/evaluate/testA_30_126_0.pn_0_0.6505_[0.582 0.719].png
img: 361 evaluate_data/GlaS/E2CNN/evaluate/testA_30_126_0.pn_1_0.6619_[0.5141 0.8097].png
img: 362 evaluate_data/GlaS/E2CNN/evaluate/testA_30_126_0.pn_2_0.6136_[0.4927 0.7346].png
img: 363 evaluate_data/GlaS/E2CNN/evaluate/testA_30_126_0.pn_3_0.6126_[0.4602 0.7649].png
img: 364 evaluate_data/GlaS/E2CNN/evaluate/testA_30_126_405.pn_0_0.7467_[0.6211 0.8724].png
img: 365 evaluate_data/GlaS/E2CNN/evaluate/testA_30_126_405.pn_1_0.7613_[0.6315 0.8911].png
img: 366 evaluate_data/GlaS/E2CNN/evaluate/testA_30_126_405.pn_2_0.6171_[0.5434 0.6908].png
img: 367 evaluate_data/GlaS/E2CNN/evaluate/testA_30_126_405.pn_3_0.7479_[0.6218 0.8741].png
img: 368 evaluate_data/GlaS/E2CNN/evaluate/testA_31_0_0.pn_0_0.7263_[0.7325 0.72  ].png
img: 369 evaluate_data/GlaS/E2CNN/evaluate/testA_31_0_0.pn_1_0.6643_[0.7223 0.6063].png
img: 370 evaluate_data/GlaS/E2CNN/evaluate/testA_31_0_0.pn_2_0.6074_[0.6761 0.5386].png
img: 371 evaluate_data/GlaS/E2CNN/evaluate/testA_31_0_0.pn_3_0.7128_[0.7876 0.638 ].png
img: 372 evaluate_data/GlaS/E2CNN/evaluate/testA_31_0_405.pn_0_0.5323_[0.5859 0.4786].png
img: 373 evaluate_data/GlaS/E2CNN/evaluate/testA_31_0_405.pn_1_0.7783_[0.7061 0.8504].png
img: 374 evaluate_data/GlaS/E2CNN/evaluate/testA_31_0_405.pn_2_0.5893_[0.5778 0.6009].png
img: 375 evaluate_data/GlaS/E2CNN/evaluate/testA_31_0_405.pn_3_0.5077_[0.5901 0.4254].png
img: 376 evaluate_data/GlaS/E2CNN/evaluate/testA_31_126_0.pn_0_0.4898_[0.5213 0.4583].png
img: 377 evaluate_data/GlaS/E2CNN/evaluate/testA_31_126_0.pn_1_0.3691_[0.4178 0.3203].png
img: 378 evaluate_data/GlaS/E2CNN/evaluate/testA_31_126_0.pn_2_0.7535_[0.7063 0.8007].png
img: 379 evaluate_data/GlaS/E2CNN/evaluate/testA_31_126_0.pn_3_0.7784_[0.6753 0.8815].png
img: 380 evaluate_data/GlaS/E2CNN/evaluate/testA_31_126_405.pn_0_0.6954_[0.5486 0.8421].png
img: 381 evaluate_data/GlaS/E2CNN/evaluate/testA_31_126_405.pn_1_0.5929_[0.4921 0.6938].png
img: 382 evaluate_data/GlaS/E2CNN/evaluate/testA_31_126_405.pn_2_0.7407_[0.5719 0.9095].png
img: 383 evaluate_data/GlaS/E2CNN/evaluate/testA_31_126_405.pn_3_0.3889_[0.4057 0.3721].png
img: 384 evaluate_data/GlaS/E2CNN/evaluate/testA_32_0_0.pn_0_0.4543_[0.517  0.3917].png
img: 385 evaluate_data/GlaS/E2CNN/evaluate/testA_32_0_0.pn_1_0.3676_[0.4005 0.3346].png
img: 386 evaluate_data/GlaS/E2CNN/evaluate/testA_32_0_0.pn_2_0.4603_[0.476  0.4447].png
img: 387 evaluate_data/GlaS/E2CNN/evaluate/testA_32_0_0.pn_3_0.3602_[0.3915 0.3289].png
img: 388 evaluate_data/GlaS/E2CNN/evaluate/testA_32_0_405.pn_0_0.4397_[0.6334 0.2461].png
img: 389 evaluate_data/GlaS/E2CNN/evaluate/testA_32_0_405.pn_1_0.3041_[0.6082 0.    ].png
img: 390 evaluate_data/GlaS/E2CNN/evaluate/testA_32_0_405.pn_2_0.5345_[0.6762 0.3929].png
img: 391 evaluate_data/GlaS/E2CNN/evaluate/testA_32_0_405.pn_3_0.4109_[0.5676 0.2543].png
img: 392 evaluate_data/GlaS/E2CNN/evaluate/testA_32_126_0.pn_0_0.5646_[0.5669 0.5623].png
img: 393 evaluate_data/GlaS/E2CNN/evaluate/testA_32_126_0.pn_1_0.5353_[0.5626 0.5081].png
img: 394 evaluate_data/GlaS/E2CNN/evaluate/testA_32_126_0.pn_2_0.4057_[0.5206 0.2907].png
img: 395 evaluate_data/GlaS/E2CNN/evaluate/testA_32_126_0.pn_3_0.4818_[0.4633 0.5003].png
img: 396 evaluate_data/GlaS/E2CNN/evaluate/testA_32_126_405.pn_0_0.4891_[0.6431 0.3351].png
img: 397 evaluate_data/GlaS/E2CNN/evaluate/testA_32_126_405.pn_1_0.3656_[0.4723 0.2589].png
img: 398 evaluate_data/GlaS/E2CNN/evaluate/testA_32_126_405.pn_2_0.4789_[0.6048 0.3531].png
img: 399 evaluate_data/GlaS/E2CNN/evaluate/testA_32_126_405.pn_3_0.3923_[0.4989 0.2857].png
img: 400 evaluate_data/GlaS/E2CNN/evaluate/testA_33_0_0.pn_0_0.4297_[0.2453 0.6141].png
img: 401 evaluate_data/GlaS/E2CNN/evaluate/testA_33_0_0.pn_1_0.4215_[0.2186 0.6245].png
img: 402 evaluate_data/GlaS/E2CNN/evaluate/testA_33_0_0.pn_2_0.3554_[0.2018 0.509 ].png
img: 403 evaluate_data/GlaS/E2CNN/evaluate/testA_33_0_0.pn_3_0.5569_[0.4381 0.6758].png
img: 404 evaluate_data/GlaS/E2CNN/evaluate/testA_33_0_405.pn_0_0.6621_[0.4783 0.8459].png
img: 405 evaluate_data/GlaS/E2CNN/evaluate/testA_33_0_405.pn_1_0.5222_[0.3562 0.6882].png
img: 406 evaluate_data/GlaS/E2CNN/evaluate/testA_33_0_405.pn_2_0.5758_[0.3918 0.7599].png
img: 407 evaluate_data/GlaS/E2CNN/evaluate/testA_33_0_405.pn_3_0.4785_[0.2978 0.6592].png
img: 408 evaluate_data/GlaS/E2CNN/evaluate/testA_33_126_0.pn_0_0.56_[0.4019 0.7181].png
img: 409 evaluate_data/GlaS/E2CNN/evaluate/testA_33_126_0.pn_1_0.5147_[0.3591 0.6704].png
img: 410 evaluate_data/GlaS/E2CNN/evaluate/testA_33_126_0.pn_2_0.6242_[0.4509 0.7976].png
img: 411 evaluate_data/GlaS/E2CNN/evaluate/testA_33_126_0.pn_3_0.6261_[0.4524 0.7999].png
img: 412 evaluate_data/GlaS/E2CNN/evaluate/testA_33_126_405.pn_0_0.5292_[0.4145 0.644 ].png
img: 413 evaluate_data/GlaS/E2CNN/evaluate/testA_33_126_405.pn_1_0.6931_[0.5484 0.8378].png
img: 414 evaluate_data/GlaS/E2CNN/evaluate/testA_33_126_405.pn_2_0.6104_[0.501  0.7198].png
img: 415 evaluate_data/GlaS/E2CNN/evaluate/testA_33_126_405.pn_3_0.4475_[0.31   0.5851].png
img: 416 evaluate_data/GlaS/E2CNN/evaluate/testA_34_0_0.pn_0_0.3979_[0.4863 0.3095].png
img: 417 evaluate_data/GlaS/E2CNN/evaluate/testA_34_0_0.pn_1_0.3358_[0.4086 0.263 ].png
img: 418 evaluate_data/GlaS/E2CNN/evaluate/testA_34_0_0.pn_2_0.4233_[0.6014 0.2453].png
img: 419 evaluate_data/GlaS/E2CNN/evaluate/testA_34_0_0.pn_3_0.4727_[0.5436 0.4018].png
img: 420 evaluate_data/GlaS/E2CNN/evaluate/testA_34_0_405.pn_0_0.3898_[0.2726 0.5071].png
img: 421 evaluate_data/GlaS/E2CNN/evaluate/testA_34_0_405.pn_1_0.6452_[0.4816 0.8089].png
img: 422 evaluate_data/GlaS/E2CNN/evaluate/testA_34_0_405.pn_2_0.3427_[0.1879 0.4975].png
img: 423 evaluate_data/GlaS/E2CNN/evaluate/testA_34_0_405.pn_3_0.541_[0.4228 0.6593].png
img: 424 evaluate_data/GlaS/E2CNN/evaluate/testA_34_126_0.pn_0_0.4117_[0.3393 0.4842].png
img: 425 evaluate_data/GlaS/E2CNN/evaluate/testA_34_126_0.pn_1_0.3667_[0.3123 0.4212].png
img: 426 evaluate_data/GlaS/E2CNN/evaluate/testA_34_126_0.pn_2_0.5907_[0.534  0.6473].png
img: 427 evaluate_data/GlaS/E2CNN/evaluate/testA_34_126_0.pn_3_0.631_[0.5549 0.7071].png
img: 428 evaluate_data/GlaS/E2CNN/evaluate/testA_34_126_405.pn_0_0.3552_[0.2954 0.415 ].png
img: 429 evaluate_data/GlaS/E2CNN/evaluate/testA_34_126_405.pn_1_0.2094_[0.3716 0.0471].png
img: 430 evaluate_data/GlaS/E2CNN/evaluate/testA_34_126_405.pn_2_0.3646_[0.2889 0.4402].png
img: 431 evaluate_data/GlaS/E2CNN/evaluate/testA_34_126_405.pn_3_0.3608_[0.3232 0.3983].png
img: 432 evaluate_data/GlaS/E2CNN/evaluate/testA_35_0_0.pn_0_0.6027_[0.4625 0.7429].png
img: 433 evaluate_data/GlaS/E2CNN/evaluate/testA_35_0_0.pn_1_0.5074_[0.3292 0.6855].png
img: 434 evaluate_data/GlaS/E2CNN/evaluate/testA_35_0_0.pn_2_0.5279_[0.3425 0.7132].png
img: 435 evaluate_data/GlaS/E2CNN/evaluate/testA_35_0_0.pn_3_0.4697_[0.2855 0.654 ].png
img: 436 evaluate_data/GlaS/E2CNN/evaluate/testA_35_0_200.pn_0_0.6074_[0.4396 0.7753].png
img: 437 evaluate_data/GlaS/E2CNN/evaluate/testA_35_0_200.pn_1_0.6728_[0.4726 0.873 ].png
img: 438 evaluate_data/GlaS/E2CNN/evaluate/testA_35_0_200.pn_2_0.5621_[0.4115 0.7127].png
img: 439 evaluate_data/GlaS/E2CNN/evaluate/testA_35_0_200.pn_3_0.4711_[0.3469 0.5953].png
img: 440 evaluate_data/GlaS/E2CNN/evaluate/testA_35_50_0.pn_0_0.662_[0.4466 0.8775].png
img: 441 evaluate_data/GlaS/E2CNN/evaluate/testA_35_50_0.pn_1_0.4478_[0.3143 0.5814].png
img: 442 evaluate_data/GlaS/E2CNN/evaluate/testA_35_50_0.pn_2_0.4732_[0.324  0.6224].png
img: 443 evaluate_data/GlaS/E2CNN/evaluate/testA_35_50_0.pn_3_0.6389_[0.4276 0.8502].png
img: 444 evaluate_data/GlaS/E2CNN/evaluate/testA_35_50_200.pn_0_0.6744_[0.6172 0.7316].png
img: 445 evaluate_data/GlaS/E2CNN/evaluate/testA_35_50_200.pn_1_0.5753_[0.4142 0.7363].png
img: 446 evaluate_data/GlaS/E2CNN/evaluate/testA_35_50_200.pn_2_0.4508_[0.3243 0.5773].png
img: 447 evaluate_data/GlaS/E2CNN/evaluate/testA_35_50_200.pn_3_0.6201_[0.4906 0.7495].png
img: 448 evaluate_data/GlaS/E2CNN/evaluate/testA_36_0_0.pn_0_0.678_[0.5729 0.7831].png
img: 449 evaluate_data/GlaS/E2CNN/evaluate/testA_36_0_0.pn_1_0.7158_[0.6795 0.752 ].png
img: 450 evaluate_data/GlaS/E2CNN/evaluate/testA_36_0_0.pn_2_0.4424_[0.2774 0.6075].png
img: 451 evaluate_data/GlaS/E2CNN/evaluate/testA_36_0_0.pn_3_0.5559_[0.3828 0.729 ].png
img: 452 evaluate_data/GlaS/E2CNN/evaluate/testA_36_0_405.pn_0_0.6867_[0.5245 0.849 ].png
img: 453 evaluate_data/GlaS/E2CNN/evaluate/testA_36_0_405.pn_1_0.6702_[0.515  0.8255].png
img: 454 evaluate_data/GlaS/E2CNN/evaluate/testA_36_0_405.pn_2_0.5895_[0.4602 0.7187].png
img: 455 evaluate_data/GlaS/E2CNN/evaluate/testA_36_0_405.pn_3_0.6838_[0.5653 0.8022].png
img: 456 evaluate_data/GlaS/E2CNN/evaluate/testA_36_126_0.pn_0_0.4937_[0.3542 0.6332].png
img: 457 evaluate_data/GlaS/E2CNN/evaluate/testA_36_126_0.pn_1_0.5097_[0.3657 0.6537].png
img: 458 evaluate_data/GlaS/E2CNN/evaluate/testA_36_126_0.pn_2_0.6712_[0.4988 0.8436].png
img: 459 evaluate_data/GlaS/E2CNN/evaluate/testA_36_126_0.pn_3_0.6555_[0.4656 0.8455].png
img: 460 evaluate_data/GlaS/E2CNN/evaluate/testA_36_126_405.pn_0_0.7212_[0.5951 0.8473].png
img: 461 evaluate_data/GlaS/E2CNN/evaluate/testA_36_126_405.pn_1_0.6532_[0.5262 0.7803].png
img: 462 evaluate_data/GlaS/E2CNN/evaluate/testA_36_126_405.pn_2_0.5793_[0.4567 0.702 ].png
img: 463 evaluate_data/GlaS/E2CNN/evaluate/testA_36_126_405.pn_3_0.673_[0.5561 0.7899].png
img: 464 evaluate_data/GlaS/E2CNN/evaluate/testA_37_0_0.pn_0_0.6849_[0.5565 0.8133].png
img: 465 evaluate_data/GlaS/E2CNN/evaluate/testA_37_0_0.pn_1_0.6273_[0.5335 0.721 ].png
img: 466 evaluate_data/GlaS/E2CNN/evaluate/testA_37_0_0.pn_2_0.3706_[0.3448 0.3964].png
img: 467 evaluate_data/GlaS/E2CNN/evaluate/testA_37_0_0.pn_3_0.5669_[0.4977 0.6361].png
img: 468 evaluate_data/GlaS/E2CNN/evaluate/testA_37_0_405.pn_0_0.1988_[0.1163 0.2812].png
img: 469 evaluate_data/GlaS/E2CNN/evaluate/testA_37_0_405.pn_1_0.1987_[0.1583 0.2391].png
img: 470 evaluate_data/GlaS/E2CNN/evaluate/testA_37_0_405.pn_2_0.3261_[0.2076 0.4446].png
img: 471 evaluate_data/GlaS/E2CNN/evaluate/testA_37_0_405.pn_3_0.1791_[0.1674 0.1908].png
img: 472 evaluate_data/GlaS/E2CNN/evaluate/testA_37_126_0.pn_0_0.6976_[0.5972 0.798 ].png
img: 473 evaluate_data/GlaS/E2CNN/evaluate/testA_37_126_0.pn_1_0.7044_[0.5657 0.843 ].png
img: 474 evaluate_data/GlaS/E2CNN/evaluate/testA_37_126_0.pn_2_0.4249_[0.3774 0.4724].png
img: 475 evaluate_data/GlaS/E2CNN/evaluate/testA_37_126_0.pn_3_0.6992_[0.5509 0.8476].png
img: 476 evaluate_data/GlaS/E2CNN/evaluate/testA_37_126_405.pn_0_0.2112_[0.0902 0.3321].png
img: 477 evaluate_data/GlaS/E2CNN/evaluate/testA_37_126_405.pn_1_0.1649_[0.053  0.2769].png
img: 478 evaluate_data/GlaS/E2CNN/evaluate/testA_37_126_405.pn_2_0.1924_[0.0589 0.3258].png
img: 479 evaluate_data/GlaS/E2CNN/evaluate/testA_37_126_405.pn_3_0.2172_[0.0916 0.3428].png
img: 480 evaluate_data/GlaS/E2CNN/evaluate/testA_38_0_0.pn_0_0.7825_[0.7682 0.7968].png
img: 481 evaluate_data/GlaS/E2CNN/evaluate/testA_38_0_0.pn_1_0.753_[0.7854 0.7206].png
img: 482 evaluate_data/GlaS/E2CNN/evaluate/testA_38_0_0.pn_2_0.6595_[0.6625 0.6564].png
img: 483 evaluate_data/GlaS/E2CNN/evaluate/testA_38_0_0.pn_3_0.7974_[0.7307 0.8642].png
img: 484 evaluate_data/GlaS/E2CNN/evaluate/testA_38_0_405.pn_0_0.3944_[0.7888 0.    ].png
img: 485 evaluate_data/GlaS/E2CNN/evaluate/testA_38_0_405.pn_1_0.3578_[0.7157 0.    ].png
img: 486 evaluate_data/GlaS/E2CNN/evaluate/testA_38_0_405.pn_2_0.3311_[0.6623 0.    ].png
img: 487 evaluate_data/GlaS/E2CNN/evaluate/testA_38_0_405.pn_3_0.4061_[0.8121 0.    ].png
img: 488 evaluate_data/GlaS/E2CNN/evaluate/testA_38_126_0.pn_0_0.4731_[0.6919 0.2543].png
img: 489 evaluate_data/GlaS/E2CNN/evaluate/testA_38_126_0.pn_1_0.6307_[0.8139 0.4476].png
img: 490 evaluate_data/GlaS/E2CNN/evaluate/testA_38_126_0.pn_2_0.6416_[0.8085 0.4747].png
img: 491 evaluate_data/GlaS/E2CNN/evaluate/testA_38_126_0.pn_3_0.5549_[0.7352 0.3747].png
img: 492 evaluate_data/GlaS/E2CNN/evaluate/testA_38_126_405.pn_0_0.3682_[0.7364 0.    ].png
img: 493 evaluate_data/GlaS/E2CNN/evaluate/testA_38_126_405.pn_1_0.3591_[0.7182 0.    ].png
img: 494 evaluate_data/GlaS/E2CNN/evaluate/testA_38_126_405.pn_2_0.324_[0.6479 0.    ].png
img: 495 evaluate_data/GlaS/E2CNN/evaluate/testA_38_126_405.pn_3_0.4221_[0.8443 0.    ].png
img: 496 evaluate_data/GlaS/E2CNN/evaluate/testA_39_0_0.pn_0_0.2536_[0.5071 0.    ].png
img: 497 evaluate_data/GlaS/E2CNN/evaluate/testA_39_0_0.pn_1_0.3569_[0.7137 0.    ].png
img: 498 evaluate_data/GlaS/E2CNN/evaluate/testA_39_0_0.pn_2_0.3134_[0.6269 0.    ].png
img: 499 evaluate_data/GlaS/E2CNN/evaluate/testA_39_0_0.pn_3_0.3489_[0.6978 0.    ].png
img: 500 evaluate_data/GlaS/E2CNN/evaluate/testA_39_0_405.pn_0_0.6444_[0.6701 0.6187].png
img: 501 evaluate_data/GlaS/E2CNN/evaluate/testA_39_0_405.pn_1_0.5506_[0.6206 0.4807].png
img: 502 evaluate_data/GlaS/E2CNN/evaluate/testA_39_0_405.pn_2_0.6327_[0.6386 0.6267].png
img: 503 evaluate_data/GlaS/E2CNN/evaluate/testA_39_0_405.pn_3_0.2993_[0.3182 0.2804].png
img: 504 evaluate_data/GlaS/E2CNN/evaluate/testA_39_126_0.pn_0_0.3219_[0.6438 0.    ].png
img: 505 evaluate_data/GlaS/E2CNN/evaluate/testA_39_126_0.pn_1_0.3783_[0.7567 0.    ].png
img: 506 evaluate_data/GlaS/E2CNN/evaluate/testA_39_126_0.pn_2_0.3291_[0.6582 0.    ].png
img: 507 evaluate_data/GlaS/E2CNN/evaluate/testA_39_126_0.pn_3_0.3805_[0.7611 0.    ].png
img: 508 evaluate_data/GlaS/E2CNN/evaluate/testA_39_126_405.pn_0_0.7161_[0.7074 0.7248].png
img: 509 evaluate_data/GlaS/E2CNN/evaluate/testA_39_126_405.pn_1_0.7475_[0.6934 0.8017].png
img: 510 evaluate_data/GlaS/E2CNN/evaluate/testA_39_126_405.pn_2_0.728_[0.6893 0.7668].png
img: 511 evaluate_data/GlaS/E2CNN/evaluate/testA_39_126_405.pn_3_0.7051_[0.6744 0.7358].png
img: 512 evaluate_data/GlaS/E2CNN/evaluate/testA_3_0_0.pn_0_0.4063_[0.2781 0.5345].png
img: 513 evaluate_data/GlaS/E2CNN/evaluate/testA_3_0_0.pn_1_0.3905_[0.261 0.52 ].png
img: 514 evaluate_data/GlaS/E2CNN/evaluate/testA_3_0_0.pn_2_0.3488_[0.2441 0.4535].png
img: 515 evaluate_data/GlaS/E2CNN/evaluate/testA_3_0_0.pn_3_0.3297_[0.1918 0.4675].png
img: 516 evaluate_data/GlaS/E2CNN/evaluate/testA_3_0_191.pn_0_0.4318_[0.4628 0.4008].png
img: 517 evaluate_data/GlaS/E2CNN/evaluate/testA_3_0_191.pn_1_0.4585_[0.4822 0.4349].png
img: 518 evaluate_data/GlaS/E2CNN/evaluate/testA_3_0_191.pn_2_0.7611_[0.7516 0.7707].png
img: 519 evaluate_data/GlaS/E2CNN/evaluate/testA_3_0_191.pn_3_0.4191_[0.5219 0.3163].png
img: 520 evaluate_data/GlaS/E2CNN/evaluate/testA_3_38_0.pn_0_0.3742_[0.1977 0.5507].png
img: 521 evaluate_data/GlaS/E2CNN/evaluate/testA_3_38_0.pn_1_0.3672_[0.206  0.5283].png
img: 522 evaluate_data/GlaS/E2CNN/evaluate/testA_3_38_0.pn_2_0.3717_[0.1997 0.5438].png
img: 523 evaluate_data/GlaS/E2CNN/evaluate/testA_3_38_0.pn_3_0.2945_[0.1165 0.4724].png
img: 524 evaluate_data/GlaS/E2CNN/evaluate/testA_3_38_191.pn_0_0.8001_[0.6957 0.9045].png
img: 525 evaluate_data/GlaS/E2CNN/evaluate/testA_3_38_191.pn_1_0.768_[0.6478 0.8882].png
img: 526 evaluate_data/GlaS/E2CNN/evaluate/testA_3_38_191.pn_2_0.7074_[0.6206 0.7943].png
img: 527 evaluate_data/GlaS/E2CNN/evaluate/testA_3_38_191.pn_3_0.7812_[0.6534 0.909 ].png
img: 528 evaluate_data/GlaS/E2CNN/evaluate/testA_40_0_0.pn_0_0.5813_[0.5315 0.631 ].png
img: 529 evaluate_data/GlaS/E2CNN/evaluate/testA_40_0_0.pn_1_0.537_[0.505  0.5689].png
img: 530 evaluate_data/GlaS/E2CNN/evaluate/testA_40_0_0.pn_2_0.6267_[0.5564 0.6971].png
img: 531 evaluate_data/GlaS/E2CNN/evaluate/testA_40_0_0.pn_3_0.7045_[0.599 0.81 ].png
img: 532 evaluate_data/GlaS/E2CNN/evaluate/testA_40_0_405.pn_0_0.3931_[0.2854 0.5007].png
img: 533 evaluate_data/GlaS/E2CNN/evaluate/testA_40_0_405.pn_1_0.6282_[0.5548 0.7016].png
img: 534 evaluate_data/GlaS/E2CNN/evaluate/testA_40_0_405.pn_2_0.6641_[0.5489 0.7794].png
img: 535 evaluate_data/GlaS/E2CNN/evaluate/testA_40_0_405.pn_3_0.3552_[0.2449 0.4655].png
img: 536 evaluate_data/GlaS/E2CNN/evaluate/testA_40_126_0.pn_0_0.6229_[0.5403 0.7054].png
img: 537 evaluate_data/GlaS/E2CNN/evaluate/testA_40_126_0.pn_1_0.614_[0.5359 0.6921].png
img: 538 evaluate_data/GlaS/E2CNN/evaluate/testA_40_126_0.pn_2_0.5853_[0.5223 0.6482].png
img: 539 evaluate_data/GlaS/E2CNN/evaluate/testA_40_126_0.pn_3_0.6369_[0.5468 0.7269].png
img: 540 evaluate_data/GlaS/E2CNN/evaluate/testA_40_126_405.pn_0_0.6447_[0.5115 0.7778].png
img: 541 evaluate_data/GlaS/E2CNN/evaluate/testA_40_126_405.pn_1_0.3666_[0.3906 0.3427].png
img: 542 evaluate_data/GlaS/E2CNN/evaluate/testA_40_126_405.pn_2_0.5801_[0.4756 0.6845].png
img: 543 evaluate_data/GlaS/E2CNN/evaluate/testA_40_126_405.pn_3_0.6748_[0.5318 0.8179].png
img: 544 evaluate_data/GlaS/E2CNN/evaluate/testA_41_0_0.pn_0_0.7233_[0.7215 0.7252].png
img: 545 evaluate_data/GlaS/E2CNN/evaluate/testA_41_0_0.pn_1_0.6408_[0.6992 0.5825].png
img: 546 evaluate_data/GlaS/E2CNN/evaluate/testA_41_0_0.pn_2_0.6822_[0.7682 0.5962].png
img: 547 evaluate_data/GlaS/E2CNN/evaluate/testA_41_0_0.pn_3_0.6517_[0.7039 0.5994].png
img: 548 evaluate_data/GlaS/E2CNN/evaluate/testA_41_0_405.pn_0_0.3634_[0.5491 0.1777].png
img: 549 evaluate_data/GlaS/E2CNN/evaluate/testA_41_0_405.pn_1_0.4413_[0.6203 0.2623].png
img: 550 evaluate_data/GlaS/E2CNN/evaluate/testA_41_0_405.pn_2_0.5839_[0.7275 0.4402].png
img: 551 evaluate_data/GlaS/E2CNN/evaluate/testA_41_0_405.pn_3_0.3041_[0.48   0.1282].png
img: 552 evaluate_data/GlaS/E2CNN/evaluate/testA_41_126_0.pn_0_0.7257_[0.739  0.7124].png
img: 553 evaluate_data/GlaS/E2CNN/evaluate/testA_41_126_0.pn_1_0.5043_[0.635  0.3737].png
img: 554 evaluate_data/GlaS/E2CNN/evaluate/testA_41_126_0.pn_2_0.7858_[0.7636 0.808 ].png
img: 555 evaluate_data/GlaS/E2CNN/evaluate/testA_41_126_0.pn_3_0.6846_[0.7413 0.6279].png
img: 556 evaluate_data/GlaS/E2CNN/evaluate/testA_41_126_405.pn_0_0.7705_[0.7516 0.7894].png
img: 557 evaluate_data/GlaS/E2CNN/evaluate/testA_41_126_405.pn_1_0.6406_[0.7111 0.5701].png
img: 558 evaluate_data/GlaS/E2CNN/evaluate/testA_41_126_405.pn_2_0.4908_[0.6218 0.3598].png
img: 559 evaluate_data/GlaS/E2CNN/evaluate/testA_41_126_405.pn_3_0.7173_[0.7414 0.6932].png
img: 560 evaluate_data/GlaS/E2CNN/evaluate/testA_42_0_0.pn_0_0.4838_[0.5104 0.4572].png
img: 561 evaluate_data/GlaS/E2CNN/evaluate/testA_42_0_0.pn_1_0.5816_[0.5264 0.6368].png
img: 562 evaluate_data/GlaS/E2CNN/evaluate/testA_42_0_0.pn_2_0.418_[0.3542 0.4819].png
img: 563 evaluate_data/GlaS/E2CNN/evaluate/testA_42_0_0.pn_3_0.4794_[0.3946 0.5643].png
img: 564 evaluate_data/GlaS/E2CNN/evaluate/testA_42_0_405.pn_0_0.7793_[0.6753 0.8833].png
img: 565 evaluate_data/GlaS/E2CNN/evaluate/testA_42_0_405.pn_1_0.778_[0.6963 0.8596].png
img: 566 evaluate_data/GlaS/E2CNN/evaluate/testA_42_0_405.pn_2_0.62_[0.5761 0.6638].png
img: 567 evaluate_data/GlaS/E2CNN/evaluate/testA_42_0_405.pn_3_0.6084_[0.5132 0.7036].png
img: 568 evaluate_data/GlaS/E2CNN/evaluate/testA_42_126_0.pn_0_0.5356_[0.3697 0.7016].png
img: 569 evaluate_data/GlaS/E2CNN/evaluate/testA_42_126_0.pn_1_0.4288_[0.2932 0.5645].png
img: 570 evaluate_data/GlaS/E2CNN/evaluate/testA_42_126_0.pn_2_0.3422_[0.223  0.4613].png
img: 571 evaluate_data/GlaS/E2CNN/evaluate/testA_42_126_0.pn_3_0.3907_[0.2252 0.5562].png
img: 572 evaluate_data/GlaS/E2CNN/evaluate/testA_42_126_405.pn_0_0.4771_[0.5444 0.4097].png
img: 573 evaluate_data/GlaS/E2CNN/evaluate/testA_42_126_405.pn_1_0.5845_[0.6188 0.5502].png
img: 574 evaluate_data/GlaS/E2CNN/evaluate/testA_42_126_405.pn_2_0.4447_[0.418  0.4714].png
img: 575 evaluate_data/GlaS/E2CNN/evaluate/testA_42_126_405.pn_3_0.4446_[0.4397 0.4495].png
img: 576 evaluate_data/GlaS/E2CNN/evaluate/testA_43_0_0.pn_0_0.6436_[0.4455 0.8417].png
img: 577 evaluate_data/GlaS/E2CNN/evaluate/testA_43_0_0.pn_1_0.6659_[0.5035 0.8284].png
img: 578 evaluate_data/GlaS/E2CNN/evaluate/testA_43_0_0.pn_2_0.6153_[0.4612 0.7693].png
img: 579 evaluate_data/GlaS/E2CNN/evaluate/testA_43_0_0.pn_3_0.5808_[0.4314 0.7302].png
img: 580 evaluate_data/GlaS/E2CNN/evaluate/testA_43_0_200.pn_0_0.6724_[0.4896 0.8552].png
img: 581 evaluate_data/GlaS/E2CNN/evaluate/testA_43_0_200.pn_1_0.6265_[0.4434 0.8096].png
img: 582 evaluate_data/GlaS/E2CNN/evaluate/testA_43_0_200.pn_2_0.5767_[0.4229 0.7306].png
img: 583 evaluate_data/GlaS/E2CNN/evaluate/testA_43_0_200.pn_3_0.6224_[0.4619 0.783 ].png
img: 584 evaluate_data/GlaS/E2CNN/evaluate/testA_43_50_0.pn_0_0.6872_[0.5446 0.8299].png
img: 585 evaluate_data/GlaS/E2CNN/evaluate/testA_43_50_0.pn_1_0.6571_[0.5141 0.8002].png
img: 586 evaluate_data/GlaS/E2CNN/evaluate/testA_43_50_0.pn_2_0.6808_[0.5624 0.7993].png
img: 587 evaluate_data/GlaS/E2CNN/evaluate/testA_43_50_0.pn_3_0.6728_[0.5575 0.7881].png
img: 588 evaluate_data/GlaS/E2CNN/evaluate/testA_43_50_200.pn_0_0.7048_[0.5232 0.8865].png
img: 589 evaluate_data/GlaS/E2CNN/evaluate/testA_43_50_200.pn_1_0.6628_[0.4977 0.8279].png
img: 590 evaluate_data/GlaS/E2CNN/evaluate/testA_43_50_200.pn_2_0.5828_[0.4359 0.7297].png
img: 591 evaluate_data/GlaS/E2CNN/evaluate/testA_43_50_200.pn_3_0.6399_[0.4641 0.8156].png
img: 592 evaluate_data/GlaS/E2CNN/evaluate/testA_44_0_0.pn_0_0.4309_[0.2719 0.5899].png
img: 593 evaluate_data/GlaS/E2CNN/evaluate/testA_44_0_0.pn_1_0.4975_[0.2989 0.6962].png
img: 594 evaluate_data/GlaS/E2CNN/evaluate/testA_44_0_0.pn_2_0.4569_[0.2849 0.6288].png
img: 595 evaluate_data/GlaS/E2CNN/evaluate/testA_44_0_0.pn_3_0.3427_[0.2352 0.4503].png
img: 596 evaluate_data/GlaS/E2CNN/evaluate/testA_44_0_200.pn_0_0.577_[0.41   0.7439].png
img: 597 evaluate_data/GlaS/E2CNN/evaluate/testA_44_0_200.pn_1_0.5476_[0.417  0.6783].png
img: 598 evaluate_data/GlaS/E2CNN/evaluate/testA_44_0_200.pn_2_0.5999_[0.4258 0.7741].png
img: 599 evaluate_data/GlaS/E2CNN/evaluate/testA_44_0_200.pn_3_0.5501_[0.4012 0.699 ].png
img: 600 evaluate_data/GlaS/E2CNN/evaluate/testA_44_50_0.pn_0_0.4673_[0.3145 0.6202].png
img: 601 evaluate_data/GlaS/E2CNN/evaluate/testA_44_50_0.pn_1_0.3952_[0.2864 0.5039].png
img: 602 evaluate_data/GlaS/E2CNN/evaluate/testA_44_50_0.pn_2_0.4448_[0.3111 0.5785].png
img: 603 evaluate_data/GlaS/E2CNN/evaluate/testA_44_50_0.pn_3_0.4294_[0.2981 0.5607].png
img: 604 evaluate_data/GlaS/E2CNN/evaluate/testA_44_50_200.pn_0_0.5439_[0.3763 0.7116].png
img: 605 evaluate_data/GlaS/E2CNN/evaluate/testA_44_50_200.pn_1_0.6572_[0.518  0.7964].png
img: 606 evaluate_data/GlaS/E2CNN/evaluate/testA_44_50_200.pn_2_0.629_[0.4442 0.8138].png
img: 607 evaluate_data/GlaS/E2CNN/evaluate/testA_44_50_200.pn_3_0.5138_[0.353  0.6745].png
img: 608 evaluate_data/GlaS/E2CNN/evaluate/testA_45_0_0.pn_0_0.5907_[0.4696 0.7117].png
img: 609 evaluate_data/GlaS/E2CNN/evaluate/testA_45_0_0.pn_1_0.5136_[0.4004 0.6268].png
img: 610 evaluate_data/GlaS/E2CNN/evaluate/testA_45_0_0.pn_2_0.3694_[0.3901 0.3487].png
img: 611 evaluate_data/GlaS/E2CNN/evaluate/testA_45_0_0.pn_3_0.56_[0.4571 0.6628].png
img: 612 evaluate_data/GlaS/E2CNN/evaluate/testA_45_0_188.pn_0_0.4535_[0.3168 0.5901].png
img: 613 evaluate_data/GlaS/E2CNN/evaluate/testA_45_0_188.pn_1_0.58_[0.3844 0.7756].png
img: 614 evaluate_data/GlaS/E2CNN/evaluate/testA_45_0_188.pn_2_0.5446_[0.354  0.7353].png
img: 615 evaluate_data/GlaS/E2CNN/evaluate/testA_45_0_188.pn_3_0.5884_[0.3926 0.7842].png
img: 616 evaluate_data/GlaS/E2CNN/evaluate/testA_45_28_0.pn_0_0.2934_[0.3617 0.2251].png
img: 617 evaluate_data/GlaS/E2CNN/evaluate/testA_45_28_0.pn_1_0.5462_[0.4414 0.651 ].png
img: 618 evaluate_data/GlaS/E2CNN/evaluate/testA_45_28_0.pn_2_0.6127_[0.4861 0.7394].png
img: 619 evaluate_data/GlaS/E2CNN/evaluate/testA_45_28_0.pn_3_0.5043_[0.4117 0.5968].png
img: 620 evaluate_data/GlaS/E2CNN/evaluate/testA_45_28_188.pn_0_0.5379_[0.3648 0.711 ].png
img: 621 evaluate_data/GlaS/E2CNN/evaluate/testA_45_28_188.pn_1_0.559_[0.3789 0.7391].png
img: 622 evaluate_data/GlaS/E2CNN/evaluate/testA_45_28_188.pn_2_0.5589_[0.3764 0.7414].png
img: 623 evaluate_data/GlaS/E2CNN/evaluate/testA_45_28_188.pn_3_0.5036_[0.3469 0.6604].png
img: 624 evaluate_data/GlaS/E2CNN/evaluate/testA_46_0_0.pn_0_0.3606_[0.2246 0.4965].png
img: 625 evaluate_data/GlaS/E2CNN/evaluate/testA_46_0_0.pn_1_0.4309_[0.2874 0.5744].png
img: 626 evaluate_data/GlaS/E2CNN/evaluate/testA_46_0_0.pn_2_0.4007_[0.2685 0.5329].png
img: 627 evaluate_data/GlaS/E2CNN/evaluate/testA_46_0_0.pn_3_0.3626_[0.2018 0.5233].png
img: 628 evaluate_data/GlaS/E2CNN/evaluate/testA_46_0_405.pn_0_0.664_[0.4931 0.8348].png
img: 629 evaluate_data/GlaS/E2CNN/evaluate/testA_46_0_405.pn_1_0.5697_[0.4272 0.7122].png
img: 630 evaluate_data/GlaS/E2CNN/evaluate/testA_46_0_405.pn_2_0.6755_[0.5736 0.7774].png
img: 631 evaluate_data/GlaS/E2CNN/evaluate/testA_46_0_405.pn_3_0.5897_[0.4769 0.7025].png
img: 632 evaluate_data/GlaS/E2CNN/evaluate/testA_46_126_0.pn_0_0.5048_[0.2928 0.7169].png
img: 633 evaluate_data/GlaS/E2CNN/evaluate/testA_46_126_0.pn_1_0.3767_[0.2169 0.5366].png
img: 634 evaluate_data/GlaS/E2CNN/evaluate/testA_46_126_0.pn_2_0.5863_[0.3649 0.8077].png
img: 635 evaluate_data/GlaS/E2CNN/evaluate/testA_46_126_0.pn_3_0.3593_[0.1807 0.5379].png
img: 636 evaluate_data/GlaS/E2CNN/evaluate/testA_46_126_405.pn_0_0.6303_[0.4747 0.786 ].png
img: 637 evaluate_data/GlaS/E2CNN/evaluate/testA_46_126_405.pn_1_0.6968_[0.4975 0.8961].png
img: 638 evaluate_data/GlaS/E2CNN/evaluate/testA_46_126_405.pn_2_0.6661_[0.4767 0.8554].png
img: 639 evaluate_data/GlaS/E2CNN/evaluate/testA_46_126_405.pn_3_0.6548_[0.504  0.8056].png
img: 640 evaluate_data/GlaS/E2CNN/evaluate/testA_47_0_0.pn_0_0.5859_[0.5968 0.5749].png
img: 641 evaluate_data/GlaS/E2CNN/evaluate/testA_47_0_0.pn_1_0.5826_[0.5878 0.5775].png
img: 642 evaluate_data/GlaS/E2CNN/evaluate/testA_47_0_0.pn_2_0.3169_[0.4747 0.1591].png
img: 643 evaluate_data/GlaS/E2CNN/evaluate/testA_47_0_0.pn_3_0.6344_[0.6137 0.6551].png
img: 644 evaluate_data/GlaS/E2CNN/evaluate/testA_47_0_405.pn_0_0.5386_[0.5476 0.5295].png
img: 645 evaluate_data/GlaS/E2CNN/evaluate/testA_47_0_405.pn_1_0.555_[0.574  0.5361].png
img: 646 evaluate_data/GlaS/E2CNN/evaluate/testA_47_0_405.pn_2_0.5198_[0.5546 0.485 ].png
img: 647 evaluate_data/GlaS/E2CNN/evaluate/testA_47_0_405.pn_3_0.5969_[0.5834 0.6104].png
img: 648 evaluate_data/GlaS/E2CNN/evaluate/testA_47_126_0.pn_0_0.4115_[0.368  0.4551].png
img: 649 evaluate_data/GlaS/E2CNN/evaluate/testA_47_126_0.pn_1_0.5075_[0.5072 0.5078].png
img: 650 evaluate_data/GlaS/E2CNN/evaluate/testA_47_126_0.pn_2_0.6305_[0.5609 0.7001].png
img: 651 evaluate_data/GlaS/E2CNN/evaluate/testA_47_126_0.pn_3_0.6346_[0.5568 0.7124].png
img: 652 evaluate_data/GlaS/E2CNN/evaluate/testA_47_126_405.pn_0_0.3715_[0.517 0.226].png
img: 653 evaluate_data/GlaS/E2CNN/evaluate/testA_47_126_405.pn_1_0.6551_[0.6112 0.699 ].png
img: 654 evaluate_data/GlaS/E2CNN/evaluate/testA_47_126_405.pn_2_0.3568_[0.4688 0.2448].png
img: 655 evaluate_data/GlaS/E2CNN/evaluate/testA_47_126_405.pn_3_0.5341_[0.5678 0.5004].png
img: 656 evaluate_data/GlaS/E2CNN/evaluate/testA_48_0_0.pn_0_0.4272_[0.2429 0.6116].png
img: 657 evaluate_data/GlaS/E2CNN/evaluate/testA_48_0_0.pn_1_0.4757_[0.2883 0.6631].png
img: 658 evaluate_data/GlaS/E2CNN/evaluate/testA_48_0_0.pn_2_0.5025_[0.2968 0.7082].png
img: 659 evaluate_data/GlaS/E2CNN/evaluate/testA_48_0_0.pn_3_0.4471_[0.2548 0.6395].png
img: 660 evaluate_data/GlaS/E2CNN/evaluate/testA_48_0_405.pn_0_0.3111_[0.2295 0.3927].png
img: 661 evaluate_data/GlaS/E2CNN/evaluate/testA_48_0_405.pn_1_0.3106_[0.2605 0.3607].png
img: 662 evaluate_data/GlaS/E2CNN/evaluate/testA_48_0_405.pn_2_0.4407_[0.3265 0.555 ].png
img: 663 evaluate_data/GlaS/E2CNN/evaluate/testA_48_0_405.pn_3_0.2833_[0.2277 0.3389].png
img: 664 evaluate_data/GlaS/E2CNN/evaluate/testA_48_126_0.pn_0_0.2702_[0.1371 0.4033].png
img: 665 evaluate_data/GlaS/E2CNN/evaluate/testA_48_126_0.pn_1_0.2353_[0.1451 0.3255].png
img: 666 evaluate_data/GlaS/E2CNN/evaluate/testA_48_126_0.pn_2_0.2909_[0.1525 0.4293].png
img: 667 evaluate_data/GlaS/E2CNN/evaluate/testA_48_126_0.pn_3_0.3294_[0.1539 0.505 ].png
img: 668 evaluate_data/GlaS/E2CNN/evaluate/testA_48_126_405.pn_0_0.528_[0.38   0.6761].png
img: 669 evaluate_data/GlaS/E2CNN/evaluate/testA_48_126_405.pn_1_0.3768_[0.3233 0.4304].png
img: 670 evaluate_data/GlaS/E2CNN/evaluate/testA_48_126_405.pn_2_0.3909_[0.3242 0.4575].png
img: 671 evaluate_data/GlaS/E2CNN/evaluate/testA_48_126_405.pn_3_0.4264_[0.3375 0.5152].png
img: 672 evaluate_data/GlaS/E2CNN/evaluate/testA_49_0_0.pn_0_0.5974_[0.7486 0.4461].png
img: 673 evaluate_data/GlaS/E2CNN/evaluate/testA_49_0_0.pn_1_0.3564_[0.6416 0.0711].png
img: 674 evaluate_data/GlaS/E2CNN/evaluate/testA_49_0_0.pn_2_0.4627_[0.6698 0.2557].png
img: 675 evaluate_data/GlaS/E2CNN/evaluate/testA_49_0_0.pn_3_0.3694_[0.7361 0.0026].png
img: 676 evaluate_data/GlaS/E2CNN/evaluate/testA_49_0_405.pn_0_0.6971_[0.5478 0.8464].png
img: 677 evaluate_data/GlaS/E2CNN/evaluate/testA_49_0_405.pn_1_0.6855_[0.5837 0.7873].png
img: 678 evaluate_data/GlaS/E2CNN/evaluate/testA_49_0_405.pn_2_0.4876_[0.4002 0.575 ].png
img: 679 evaluate_data/GlaS/E2CNN/evaluate/testA_49_0_405.pn_3_0.6812_[0.5806 0.7818].png
img: 680 evaluate_data/GlaS/E2CNN/evaluate/testA_49_126_0.pn_0_0.3314_[0.66   0.0027].png
img: 681 evaluate_data/GlaS/E2CNN/evaluate/testA_49_126_0.pn_1_0.3288_[0.653  0.0046].png
img: 682 evaluate_data/GlaS/E2CNN/evaluate/testA_49_126_0.pn_2_0.3241_[0.6462 0.002 ].png
img: 683 evaluate_data/GlaS/E2CNN/evaluate/testA_49_126_0.pn_3_0.372_[0.7439 0.    ].png
img: 684 evaluate_data/GlaS/E2CNN/evaluate/testA_49_126_405.pn_0_0.5944_[0.5087 0.6802].png
img: 685 evaluate_data/GlaS/E2CNN/evaluate/testA_49_126_405.pn_1_0.6589_[0.5641 0.7536].png
img: 686 evaluate_data/GlaS/E2CNN/evaluate/testA_49_126_405.pn_2_0.5876_[0.5095 0.6657].png
img: 687 evaluate_data/GlaS/E2CNN/evaluate/testA_49_126_405.pn_3_0.6057_[0.5203 0.6912].png
img: 688 evaluate_data/GlaS/E2CNN/evaluate/testA_4_0_0.pn_0_0.7643_[0.689  0.8397].png
img: 689 evaluate_data/GlaS/E2CNN/evaluate/testA_4_0_0.pn_1_0.5269_[0.4739 0.5799].png
img: 690 evaluate_data/GlaS/E2CNN/evaluate/testA_4_0_0.pn_2_0.546_[0.5625 0.5296].png
img: 691 evaluate_data/GlaS/E2CNN/evaluate/testA_4_0_0.pn_3_0.5726_[0.4857 0.6596].png
img: 692 evaluate_data/GlaS/E2CNN/evaluate/testA_4_0_405.pn_0_0.4877_[0.7036 0.2719].png
img: 693 evaluate_data/GlaS/E2CNN/evaluate/testA_4_0_405.pn_1_0.3658_[0.5966 0.135 ].png
img: 694 evaluate_data/GlaS/E2CNN/evaluate/testA_4_0_405.pn_2_0.392_[0.6398 0.1441].png
img: 695 evaluate_data/GlaS/E2CNN/evaluate/testA_4_0_405.pn_3_0.289_[0.5616 0.0165].png
img: 696 evaluate_data/GlaS/E2CNN/evaluate/testA_4_126_0.pn_0_0.8158_[0.7495 0.882 ].png
img: 697 evaluate_data/GlaS/E2CNN/evaluate/testA_4_126_0.pn_1_0.5602_[0.6726 0.4477].png
img: 698 evaluate_data/GlaS/E2CNN/evaluate/testA_4_126_0.pn_2_0.5093_[0.6303 0.3882].png
img: 699 evaluate_data/GlaS/E2CNN/evaluate/testA_4_126_0.pn_3_0.6141_[0.6674 0.5608].png
img: 700 evaluate_data/GlaS/E2CNN/evaluate/testA_4_126_405.pn_0_0.3921_[0.7842 0.    ].png
img: 701 evaluate_data/GlaS/E2CNN/evaluate/testA_4_126_405.pn_1_0.2933_[0.5866 0.    ].png
img: 702 evaluate_data/GlaS/E2CNN/evaluate/testA_4_126_405.pn_2_0.3941_[0.7882 0.    ].png
img: 703 evaluate_data/GlaS/E2CNN/evaluate/testA_4_126_405.pn_3_0.3927_[0.7855 0.    ].png
img: 704 evaluate_data/GlaS/E2CNN/evaluate/testA_50_0_0.pn_0_0.6387_[0.4645 0.8129].png
img: 705 evaluate_data/GlaS/E2CNN/evaluate/testA_50_0_0.pn_1_0.5535_[0.4219 0.6852].png
img: 706 evaluate_data/GlaS/E2CNN/evaluate/testA_50_0_0.pn_2_0.6216_[0.4574 0.7857].png
img: 707 evaluate_data/GlaS/E2CNN/evaluate/testA_50_0_0.pn_3_0.5023_[0.4002 0.6043].png
img: 708 evaluate_data/GlaS/E2CNN/evaluate/testA_50_0_183.pn_0_0.6357_[0.4849 0.7866].png
img: 709 evaluate_data/GlaS/E2CNN/evaluate/testA_50_0_183.pn_1_0.5528_[0.4486 0.657 ].png
img: 710 evaluate_data/GlaS/E2CNN/evaluate/testA_50_0_183.pn_2_0.6804_[0.5177 0.8431].png
img: 711 evaluate_data/GlaS/E2CNN/evaluate/testA_50_0_183.pn_3_0.4864_[0.3467 0.626 ].png
img: 712 evaluate_data/GlaS/E2CNN/evaluate/testA_50_28_0.pn_0_0.634_[0.4896 0.7783].png
img: 713 evaluate_data/GlaS/E2CNN/evaluate/testA_50_28_0.pn_1_0.5348_[0.4154 0.6543].png
img: 714 evaluate_data/GlaS/E2CNN/evaluate/testA_50_28_0.pn_2_0.5319_[0.4214 0.6424].png
img: 715 evaluate_data/GlaS/E2CNN/evaluate/testA_50_28_0.pn_3_0.6434_[0.5492 0.7377].png
img: 716 evaluate_data/GlaS/E2CNN/evaluate/testA_50_28_183.pn_0_0.5968_[0.4781 0.7155].png
img: 717 evaluate_data/GlaS/E2CNN/evaluate/testA_50_28_183.pn_1_0.6196_[0.4831 0.7561].png
img: 718 evaluate_data/GlaS/E2CNN/evaluate/testA_50_28_183.pn_2_0.658_[0.5108 0.8051].png
img: 719 evaluate_data/GlaS/E2CNN/evaluate/testA_50_28_183.pn_3_0.574_[0.4317 0.7163].png
img: 720 evaluate_data/GlaS/E2CNN/evaluate/testA_51_0_0.pn_0_0.4623_[0.5284 0.3962].png
img: 721 evaluate_data/GlaS/E2CNN/evaluate/testA_51_0_0.pn_1_0.5739_[0.7186 0.4292].png
img: 722 evaluate_data/GlaS/E2CNN/evaluate/testA_51_0_0.pn_2_0.4136_[0.4808 0.3465].png
img: 723 evaluate_data/GlaS/E2CNN/evaluate/testA_51_0_0.pn_3_0.5419_[0.5898 0.4941].png
img: 724 evaluate_data/GlaS/E2CNN/evaluate/testA_51_0_405.pn_0_0.4475_[0.6156 0.2794].png
img: 725 evaluate_data/GlaS/E2CNN/evaluate/testA_51_0_405.pn_1_0.7533_[0.7166 0.7901].png
img: 726 evaluate_data/GlaS/E2CNN/evaluate/testA_51_0_405.pn_2_0.6659_[0.6799 0.6518].png
img: 727 evaluate_data/GlaS/E2CNN/evaluate/testA_51_0_405.pn_3_0.7743_[0.7199 0.8286].png
img: 728 evaluate_data/GlaS/E2CNN/evaluate/testA_51_126_0.pn_0_0.6005_[0.5556 0.6453].png
img: 729 evaluate_data/GlaS/E2CNN/evaluate/testA_51_126_0.pn_1_0.6238_[0.5987 0.6488].png
img: 730 evaluate_data/GlaS/E2CNN/evaluate/testA_51_126_0.pn_2_0.5477_[0.5436 0.5517].png
img: 731 evaluate_data/GlaS/E2CNN/evaluate/testA_51_126_0.pn_3_0.6872_[0.6252 0.7493].png
img: 732 evaluate_data/GlaS/E2CNN/evaluate/testA_51_126_405.pn_0_0.7112_[0.6647 0.7576].png
img: 733 evaluate_data/GlaS/E2CNN/evaluate/testA_51_126_405.pn_1_0.4673_[0.4675 0.4671].png
img: 734 evaluate_data/GlaS/E2CNN/evaluate/testA_51_126_405.pn_2_0.4364_[0.3898 0.483 ].png
img: 735 evaluate_data/GlaS/E2CNN/evaluate/testA_51_126_405.pn_3_0.45_[0.3958 0.5043].png
img: 736 evaluate_data/GlaS/E2CNN/evaluate/testA_52_0_0.pn_0_0.6731_[0.5122 0.834 ].png
img: 737 evaluate_data/GlaS/E2CNN/evaluate/testA_52_0_0.pn_1_0.6706_[0.5824 0.7588].png
img: 738 evaluate_data/GlaS/E2CNN/evaluate/testA_52_0_0.pn_2_0.5923_[0.4415 0.7432].png
img: 739 evaluate_data/GlaS/E2CNN/evaluate/testA_52_0_0.pn_3_0.6887_[0.6129 0.7644].png
img: 740 evaluate_data/GlaS/E2CNN/evaluate/testA_52_0_405.pn_0_0.7632_[0.7343 0.792 ].png
img: 741 evaluate_data/GlaS/E2CNN/evaluate/testA_52_0_405.pn_1_0.6314_[0.6029 0.6599].png
img: 742 evaluate_data/GlaS/E2CNN/evaluate/testA_52_0_405.pn_2_0.7504_[0.6724 0.8284].png
img: 743 evaluate_data/GlaS/E2CNN/evaluate/testA_52_0_405.pn_3_0.6439_[0.5995 0.6884].png
img: 744 evaluate_data/GlaS/E2CNN/evaluate/testA_52_126_0.pn_0_0.6559_[0.5713 0.7405].png
img: 745 evaluate_data/GlaS/E2CNN/evaluate/testA_52_126_0.pn_1_0.674_[0.5145 0.8335].png
img: 746 evaluate_data/GlaS/E2CNN/evaluate/testA_52_126_0.pn_2_0.7061_[0.5338 0.8784].png
img: 747 evaluate_data/GlaS/E2CNN/evaluate/testA_52_126_0.pn_3_0.5511_[0.4148 0.6875].png
img: 748 evaluate_data/GlaS/E2CNN/evaluate/testA_52_126_405.pn_0_0.4289_[0.5479 0.3099].png
img: 749 evaluate_data/GlaS/E2CNN/evaluate/testA_52_126_405.pn_1_0.7437_[0.6484 0.8389].png
img: 750 evaluate_data/GlaS/E2CNN/evaluate/testA_52_126_405.pn_2_0.7551_[0.6716 0.8385].png
img: 751 evaluate_data/GlaS/E2CNN/evaluate/testA_52_126_405.pn_3_0.7461_[0.6444 0.8478].png
img: 752 evaluate_data/GlaS/E2CNN/evaluate/testA_53_0_0.pn_0_0.5743_[0.6394 0.5092].png
img: 753 evaluate_data/GlaS/E2CNN/evaluate/testA_53_0_0.pn_1_0.3755_[0.4966 0.2543].png
img: 754 evaluate_data/GlaS/E2CNN/evaluate/testA_53_0_0.pn_2_0.7797_[0.7483 0.8112].png
img: 755 evaluate_data/GlaS/E2CNN/evaluate/testA_53_0_0.pn_3_0.2414_[0.2865 0.1962].png
img: 756 evaluate_data/GlaS/E2CNN/evaluate/testA_53_0_405.pn_0_0.466_[0.5474 0.3846].png
img: 757 evaluate_data/GlaS/E2CNN/evaluate/testA_53_0_405.pn_1_0.3796_[0.4188 0.3405].png
img: 758 evaluate_data/GlaS/E2CNN/evaluate/testA_53_0_405.pn_2_0.6475_[0.6359 0.659 ].png
img: 759 evaluate_data/GlaS/E2CNN/evaluate/testA_53_0_405.pn_3_0.3782_[0.4411 0.3154].png
img: 760 evaluate_data/GlaS/E2CNN/evaluate/testA_53_126_0.pn_0_0.234_[0.2874 0.1805].png
img: 761 evaluate_data/GlaS/E2CNN/evaluate/testA_53_126_0.pn_1_0.319_[0.3813 0.2567].png
img: 762 evaluate_data/GlaS/E2CNN/evaluate/testA_53_126_0.pn_2_0.2515_[0.3123 0.1908].png
img: 763 evaluate_data/GlaS/E2CNN/evaluate/testA_53_126_0.pn_3_0.431_[0.6634 0.1987].png
img: 764 evaluate_data/GlaS/E2CNN/evaluate/testA_53_126_405.pn_0_0.508_[0.6197 0.3962].png
img: 765 evaluate_data/GlaS/E2CNN/evaluate/testA_53_126_405.pn_1_0.3867_[0.5852 0.1883].png
img: 766 evaluate_data/GlaS/E2CNN/evaluate/testA_53_126_405.pn_2_0.4966_[0.6696 0.3236].png
img: 767 evaluate_data/GlaS/E2CNN/evaluate/testA_53_126_405.pn_3_0.4853_[0.6332 0.3374].png
img: 768 evaluate_data/GlaS/E2CNN/evaluate/testA_54_0_0.pn_0_0.4454_[0.3141 0.5767].png
img: 769 evaluate_data/GlaS/E2CNN/evaluate/testA_54_0_0.pn_1_0.4979_[0.3476 0.6482].png
img: 770 evaluate_data/GlaS/E2CNN/evaluate/testA_54_0_0.pn_2_0.4966_[0.363  0.6302].png
img: 771 evaluate_data/GlaS/E2CNN/evaluate/testA_54_0_0.pn_3_0.4278_[0.304  0.5517].png
img: 772 evaluate_data/GlaS/E2CNN/evaluate/testA_54_0_405.pn_0_0.6774_[0.5391 0.8157].png
img: 773 evaluate_data/GlaS/E2CNN/evaluate/testA_54_0_405.pn_1_0.6954_[0.5487 0.8421].png
img: 774 evaluate_data/GlaS/E2CNN/evaluate/testA_54_0_405.pn_2_0.646_[0.5192 0.7728].png
img: 775 evaluate_data/GlaS/E2CNN/evaluate/testA_54_0_405.pn_3_0.6666_[0.5182 0.815 ].png
img: 776 evaluate_data/GlaS/E2CNN/evaluate/testA_54_126_0.pn_0_0.6259_[0.4196 0.8321].png
img: 777 evaluate_data/GlaS/E2CNN/evaluate/testA_54_126_0.pn_1_0.542_[0.3848 0.6991].png
img: 778 evaluate_data/GlaS/E2CNN/evaluate/testA_54_126_0.pn_2_0.629_[0.4672 0.7908].png
img: 779 evaluate_data/GlaS/E2CNN/evaluate/testA_54_126_0.pn_3_0.6171_[0.4227 0.8115].png
img: 780 evaluate_data/GlaS/E2CNN/evaluate/testA_54_126_405.pn_0_0.4572_[0.4246 0.4898].png
img: 781 evaluate_data/GlaS/E2CNN/evaluate/testA_54_126_405.pn_1_0.5604_[0.4905 0.6304].png
img: 782 evaluate_data/GlaS/E2CNN/evaluate/testA_54_126_405.pn_2_0.5281_[0.4422 0.6139].png
img: 783 evaluate_data/GlaS/E2CNN/evaluate/testA_54_126_405.pn_3_0.534_[0.464 0.604].png
img: 784 evaluate_data/GlaS/E2CNN/evaluate/testA_55_0_0.pn_0_0.4747_[0.4091 0.5404].png
img: 785 evaluate_data/GlaS/E2CNN/evaluate/testA_55_0_0.pn_1_0.5662_[0.4625 0.67  ].png
img: 786 evaluate_data/GlaS/E2CNN/evaluate/testA_55_0_0.pn_2_0.4287_[0.3821 0.4753].png
img: 787 evaluate_data/GlaS/E2CNN/evaluate/testA_55_0_0.pn_3_0.4596_[0.3363 0.583 ].png
img: 788 evaluate_data/GlaS/E2CNN/evaluate/testA_55_0_405.pn_0_0.316_[0.1304 0.5016].png
img: 789 evaluate_data/GlaS/E2CNN/evaluate/testA_55_0_405.pn_1_0.3617_[0.1449 0.5786].png
img: 790 evaluate_data/GlaS/E2CNN/evaluate/testA_55_0_405.pn_2_0.3186_[0.1342 0.5029].png
img: 791 evaluate_data/GlaS/E2CNN/evaluate/testA_55_0_405.pn_3_0.1366_[0.1011 0.1721].png
img: 792 evaluate_data/GlaS/E2CNN/evaluate/testA_55_126_0.pn_0_0.6915_[0.5267 0.8563].png
img: 793 evaluate_data/GlaS/E2CNN/evaluate/testA_55_126_0.pn_1_0.722_[0.5569 0.8872].png
img: 794 evaluate_data/GlaS/E2CNN/evaluate/testA_55_126_0.pn_2_0.6185_[0.4915 0.7455].png
img: 795 evaluate_data/GlaS/E2CNN/evaluate/testA_55_126_0.pn_3_0.69_[0.5412 0.8388].png
img: 796 evaluate_data/GlaS/E2CNN/evaluate/testA_55_126_405.pn_0_0.3379_[0.1567 0.5191].png
img: 797 evaluate_data/GlaS/E2CNN/evaluate/testA_55_126_405.pn_1_0.2885_[0.1435 0.4335].png
img: 798 evaluate_data/GlaS/E2CNN/evaluate/testA_55_126_405.pn_2_0.4013_[0.1783 0.6243].png
img: 799 evaluate_data/GlaS/E2CNN/evaluate/testA_55_126_405.pn_3_0.3343_[0.1558 0.5128].png
img: 800 evaluate_data/GlaS/E2CNN/evaluate/testA_56_0_0.pn_0_0.3844_[0.2458 0.523 ].png
img: 801 evaluate_data/GlaS/E2CNN/evaluate/testA_56_0_0.pn_1_0.4004_[0.2514 0.5494].png
img: 802 evaluate_data/GlaS/E2CNN/evaluate/testA_56_0_0.pn_2_0.6068_[0.3615 0.8521].png
img: 803 evaluate_data/GlaS/E2CNN/evaluate/testA_56_0_0.pn_3_0.4691_[0.2815 0.6567].png
img: 804 evaluate_data/GlaS/E2CNN/evaluate/testA_56_0_405.pn_0_0.3121_[0.4327 0.1915].png
img: 805 evaluate_data/GlaS/E2CNN/evaluate/testA_56_0_405.pn_1_0.3254_[0.3929 0.258 ].png
img: 806 evaluate_data/GlaS/E2CNN/evaluate/testA_56_0_405.pn_2_0.4018_[0.3869 0.4167].png
img: 807 evaluate_data/GlaS/E2CNN/evaluate/testA_56_0_405.pn_3_0.3436_[0.4389 0.2482].png
img: 808 evaluate_data/GlaS/E2CNN/evaluate/testA_56_126_0.pn_0_0.4096_[0.3646 0.4545].png
img: 809 evaluate_data/GlaS/E2CNN/evaluate/testA_56_126_0.pn_1_0.734_[0.5806 0.8874].png
img: 810 evaluate_data/GlaS/E2CNN/evaluate/testA_56_126_0.pn_2_0.6009_[0.5028 0.699 ].png
img: 811 evaluate_data/GlaS/E2CNN/evaluate/testA_56_126_0.pn_3_0.6966_[0.549  0.8442].png
img: 812 evaluate_data/GlaS/E2CNN/evaluate/testA_56_126_405.pn_0_0.4751_[0.5468 0.4035].png
img: 813 evaluate_data/GlaS/E2CNN/evaluate/testA_56_126_405.pn_1_0.5472_[0.568  0.5265].png
img: 814 evaluate_data/GlaS/E2CNN/evaluate/testA_56_126_405.pn_2_0.4137_[0.486  0.3413].png
img: 815 evaluate_data/GlaS/E2CNN/evaluate/testA_56_126_405.pn_3_0.4069_[0.4454 0.3685].png
img: 816 evaluate_data/GlaS/E2CNN/evaluate/testA_57_0_0.pn_0_0.3017_[0.144  0.4593].png
img: 817 evaluate_data/GlaS/E2CNN/evaluate/testA_57_0_0.pn_1_0.3569_[0.1239 0.59  ].png
img: 818 evaluate_data/GlaS/E2CNN/evaluate/testA_57_0_0.pn_2_0.3615_[0.1522 0.5708].png
img: 819 evaluate_data/GlaS/E2CNN/evaluate/testA_57_0_0.pn_3_0.3412_[0.1554 0.527 ].png
img: 820 evaluate_data/GlaS/E2CNN/evaluate/testA_57_0_405.pn_0_0.3365_[0.2663 0.4068].png
img: 821 evaluate_data/GlaS/E2CNN/evaluate/testA_57_0_405.pn_1_0.3757_[0.2701 0.4814].png
img: 822 evaluate_data/GlaS/E2CNN/evaluate/testA_57_0_405.pn_2_0.3559_[0.3089 0.4029].png
img: 823 evaluate_data/GlaS/E2CNN/evaluate/testA_57_0_405.pn_3_0.3076_[0.1996 0.4155].png
img: 824 evaluate_data/GlaS/E2CNN/evaluate/testA_57_126_0.pn_0_0.2569_[0.1528 0.361 ].png
img: 825 evaluate_data/GlaS/E2CNN/evaluate/testA_57_126_0.pn_1_0.289_[0.1623 0.4157].png
img: 826 evaluate_data/GlaS/E2CNN/evaluate/testA_57_126_0.pn_2_0.26_[0.1538 0.3662].png
img: 827 evaluate_data/GlaS/E2CNN/evaluate/testA_57_126_0.pn_3_0.2781_[0.1608 0.3954].png
img: 828 evaluate_data/GlaS/E2CNN/evaluate/testA_57_126_405.pn_0_0.3935_[0.3106 0.4763].png
img: 829 evaluate_data/GlaS/E2CNN/evaluate/testA_57_126_405.pn_1_0.4356_[0.3284 0.5428].png
img: 830 evaluate_data/GlaS/E2CNN/evaluate/testA_57_126_405.pn_2_0.2484_[0.2278 0.2689].png
img: 831 evaluate_data/GlaS/E2CNN/evaluate/testA_57_126_405.pn_3_0.4632_[0.34   0.5864].png
img: 832 evaluate_data/GlaS/E2CNN/evaluate/testA_58_0_0.pn_0_0.3834_[0.2609 0.506 ].png
img: 833 evaluate_data/GlaS/E2CNN/evaluate/testA_58_0_0.pn_1_0.3005_[0.1838 0.4172].png
img: 834 evaluate_data/GlaS/E2CNN/evaluate/testA_58_0_0.pn_2_0.3387_[0.2043 0.473 ].png
img: 835 evaluate_data/GlaS/E2CNN/evaluate/testA_58_0_0.pn_3_0.3428_[0.2714 0.4141].png
img: 836 evaluate_data/GlaS/E2CNN/evaluate/testA_58_0_405.pn_0_0.6536_[0.5179 0.7892].png
img: 837 evaluate_data/GlaS/E2CNN/evaluate/testA_58_0_405.pn_1_0.7032_[0.5796 0.8269].png
img: 838 evaluate_data/GlaS/E2CNN/evaluate/testA_58_0_405.pn_2_0.6119_[0.4936 0.7302].png
img: 839 evaluate_data/GlaS/E2CNN/evaluate/testA_58_0_405.pn_3_0.4214_[0.3493 0.4935].png
img: 840 evaluate_data/GlaS/E2CNN/evaluate/testA_58_126_0.pn_0_0.4757_[0.2987 0.6526].png
img: 841 evaluate_data/GlaS/E2CNN/evaluate/testA_58_126_0.pn_1_0.5806_[0.3654 0.7959].png
img: 842 evaluate_data/GlaS/E2CNN/evaluate/testA_58_126_0.pn_2_0.2936_[0.1818 0.4054].png
img: 843 evaluate_data/GlaS/E2CNN/evaluate/testA_58_126_0.pn_3_0.2812_[0.1895 0.373 ].png
img: 844 evaluate_data/GlaS/E2CNN/evaluate/testA_58_126_405.pn_0_0.7145_[0.5572 0.8719].png
img: 845 evaluate_data/GlaS/E2CNN/evaluate/testA_58_126_405.pn_1_0.7094_[0.5487 0.8702].png
img: 846 evaluate_data/GlaS/E2CNN/evaluate/testA_58_126_405.pn_2_0.6723_[0.5084 0.8362].png
img: 847 evaluate_data/GlaS/E2CNN/evaluate/testA_58_126_405.pn_3_0.7044_[0.572  0.8367].png
img: 848 evaluate_data/GlaS/E2CNN/evaluate/testA_59_0_0.pn_0_0.4451_[0.3404 0.5497].png
img: 849 evaluate_data/GlaS/E2CNN/evaluate/testA_59_0_0.pn_1_0.4129_[0.3412 0.4846].png
img: 850 evaluate_data/GlaS/E2CNN/evaluate/testA_59_0_0.pn_2_0.5039_[0.3654 0.6424].png
img: 851 evaluate_data/GlaS/E2CNN/evaluate/testA_59_0_0.pn_3_0.3766_[0.3029 0.4502].png
img: 852 evaluate_data/GlaS/E2CNN/evaluate/testA_59_0_405.pn_0_0.4269_[0.3623 0.4915].png
img: 853 evaluate_data/GlaS/E2CNN/evaluate/testA_59_0_405.pn_1_0.4615_[0.3794 0.5435].png
img: 854 evaluate_data/GlaS/E2CNN/evaluate/testA_59_0_405.pn_2_0.5035_[0.3952 0.6117].png
img: 855 evaluate_data/GlaS/E2CNN/evaluate/testA_59_0_405.pn_3_0.494_[0.3953 0.5927].png
img: 856 evaluate_data/GlaS/E2CNN/evaluate/testA_59_126_0.pn_0_0.4437_[0.2998 0.5876].png
img: 857 evaluate_data/GlaS/E2CNN/evaluate/testA_59_126_0.pn_1_0.4475_[0.3017 0.5934].png
img: 858 evaluate_data/GlaS/E2CNN/evaluate/testA_59_126_0.pn_2_0.3011_[0.2486 0.3535].png
img: 859 evaluate_data/GlaS/E2CNN/evaluate/testA_59_126_0.pn_3_0.4089_[0.2833 0.5345].png
img: 860 evaluate_data/GlaS/E2CNN/evaluate/testA_59_126_405.pn_0_0.5807_[0.4397 0.7216].png
img: 861 evaluate_data/GlaS/E2CNN/evaluate/testA_59_126_405.pn_1_0.457_[0.3824 0.5317].png
img: 862 evaluate_data/GlaS/E2CNN/evaluate/testA_59_126_405.pn_2_0.3241_[0.3333 0.3149].png
img: 863 evaluate_data/GlaS/E2CNN/evaluate/testA_59_126_405.pn_3_0.6038_[0.4578 0.7497].png
img: 864 evaluate_data/GlaS/E2CNN/evaluate/testA_5_0_0.pn_0_0.5695_[0.4249 0.7141].png
img: 865 evaluate_data/GlaS/E2CNN/evaluate/testA_5_0_0.pn_1_0.3028_[0.3368 0.2688].png
img: 866 evaluate_data/GlaS/E2CNN/evaluate/testA_5_0_0.pn_2_0.4679_[0.3928 0.5431].png
img: 867 evaluate_data/GlaS/E2CNN/evaluate/testA_5_0_0.pn_3_0.6743_[0.5017 0.8468].png
img: 868 evaluate_data/GlaS/E2CNN/evaluate/testA_5_0_405.pn_0_0.6504_[0.5055 0.7952].png
img: 869 evaluate_data/GlaS/E2CNN/evaluate/testA_5_0_405.pn_1_0.4522_[0.3502 0.5541].png
img: 870 evaluate_data/GlaS/E2CNN/evaluate/testA_5_0_405.pn_2_0.463_[0.3615 0.5644].png
img: 871 evaluate_data/GlaS/E2CNN/evaluate/testA_5_0_405.pn_3_0.4205_[0.3479 0.4931].png
img: 872 evaluate_data/GlaS/E2CNN/evaluate/testA_5_126_0.pn_0_0.5955_[0.4691 0.7219].png
img: 873 evaluate_data/GlaS/E2CNN/evaluate/testA_5_126_0.pn_1_0.4661_[0.3611 0.5712].png
img: 874 evaluate_data/GlaS/E2CNN/evaluate/testA_5_126_0.pn_2_0.5571_[0.4396 0.6747].png
img: 875 evaluate_data/GlaS/E2CNN/evaluate/testA_5_126_0.pn_3_0.4042_[0.2911 0.5173].png
img: 876 evaluate_data/GlaS/E2CNN/evaluate/testA_5_126_405.pn_0_0.6542_[0.5504 0.7581].png
img: 877 evaluate_data/GlaS/E2CNN/evaluate/testA_5_126_405.pn_1_0.6073_[0.5033 0.7113].png
img: 878 evaluate_data/GlaS/E2CNN/evaluate/testA_5_126_405.pn_2_0.3058_[0.401  0.2105].png
img: 879 evaluate_data/GlaS/E2CNN/evaluate/testA_5_126_405.pn_3_0.6398_[0.5145 0.7652].png
img: 880 evaluate_data/GlaS/E2CNN/evaluate/testA_60_0_0.pn_0_0.6782_[0.5797 0.7767].png
img: 881 evaluate_data/GlaS/E2CNN/evaluate/testA_60_0_0.pn_1_0.6917_[0.6408 0.7426].png
img: 882 evaluate_data/GlaS/E2CNN/evaluate/testA_60_0_0.pn_2_0.7277_[0.6089 0.8464].png
img: 883 evaluate_data/GlaS/E2CNN/evaluate/testA_60_0_0.pn_3_0.5546_[0.4747 0.6345].png
img: 884 evaluate_data/GlaS/E2CNN/evaluate/testA_60_0_405.pn_0_0.6086_[0.6724 0.5448].png
img: 885 evaluate_data/GlaS/E2CNN/evaluate/testA_60_0_405.pn_1_0.5779_[0.6919 0.4639].png
img: 886 evaluate_data/GlaS/E2CNN/evaluate/testA_60_0_405.pn_2_0.6771_[0.7689 0.5853].png
img: 887 evaluate_data/GlaS/E2CNN/evaluate/testA_60_0_405.pn_3_0.726_[0.7485 0.7035].png
img: 888 evaluate_data/GlaS/E2CNN/evaluate/testA_60_126_0.pn_0_0.6322_[0.4665 0.7979].png
img: 889 evaluate_data/GlaS/E2CNN/evaluate/testA_60_126_0.pn_1_0.6609_[0.5026 0.8193].png
img: 890 evaluate_data/GlaS/E2CNN/evaluate/testA_60_126_0.pn_2_0.6222_[0.4623 0.7821].png
img: 891 evaluate_data/GlaS/E2CNN/evaluate/testA_60_126_0.pn_3_0.6518_[0.4848 0.8189].png
img: 892 evaluate_data/GlaS/E2CNN/evaluate/testA_60_126_405.pn_0_0.633_[0.6096 0.6563].png
img: 893 evaluate_data/GlaS/E2CNN/evaluate/testA_60_126_405.pn_1_0.6036_[0.6214 0.5858].png
img: 894 evaluate_data/GlaS/E2CNN/evaluate/testA_60_126_405.pn_2_0.768_[0.7009 0.8351].png
img: 895 evaluate_data/GlaS/E2CNN/evaluate/testA_60_126_405.pn_3_0.5504_[0.5467 0.554 ].png
img: 896 evaluate_data/GlaS/E2CNN/evaluate/testA_6_0_0.pn_0_0.4411_[0.3111 0.5711].png
img: 897 evaluate_data/GlaS/E2CNN/evaluate/testA_6_0_0.pn_1_0.3246_[0.241  0.4083].png
img: 898 evaluate_data/GlaS/E2CNN/evaluate/testA_6_0_0.pn_2_0.2277_[0.2172 0.2382].png
img: 899 evaluate_data/GlaS/E2CNN/evaluate/testA_6_0_0.pn_3_0.4998_[0.3147 0.685 ].png
img: 900 evaluate_data/GlaS/E2CNN/evaluate/testA_6_0_405.pn_0_0.4713_[0.5068 0.4359].png
img: 901 evaluate_data/GlaS/E2CNN/evaluate/testA_6_0_405.pn_1_0.4969_[0.5108 0.483 ].png
img: 902 evaluate_data/GlaS/E2CNN/evaluate/testA_6_0_405.pn_2_0.6189_[0.5647 0.6731].png
img: 903 evaluate_data/GlaS/E2CNN/evaluate/testA_6_0_405.pn_3_0.4762_[0.4096 0.5429].png
img: 904 evaluate_data/GlaS/E2CNN/evaluate/testA_6_126_0.pn_0_0.2251_[0.1685 0.2818].png
img: 905 evaluate_data/GlaS/E2CNN/evaluate/testA_6_126_0.pn_1_0.3662_[0.2096 0.5227].png
img: 906 evaluate_data/GlaS/E2CNN/evaluate/testA_6_126_0.pn_2_0.4079_[0.2256 0.5901].png
img: 907 evaluate_data/GlaS/E2CNN/evaluate/testA_6_126_0.pn_3_0.2364_[0.1764 0.2964].png
img: 908 evaluate_data/GlaS/E2CNN/evaluate/testA_6_126_405.pn_0_0.4522_[0.4929 0.4116].png
img: 909 evaluate_data/GlaS/E2CNN/evaluate/testA_6_126_405.pn_1_0.6094_[0.552  0.6668].png
img: 910 evaluate_data/GlaS/E2CNN/evaluate/testA_6_126_405.pn_2_0.4634_[0.4965 0.4304].png
img: 911 evaluate_data/GlaS/E2CNN/evaluate/testA_6_126_405.pn_3_0.7495_[0.6228 0.8761].png
img: 912 evaluate_data/GlaS/E2CNN/evaluate/testA_7_0_0.pn_0_0.428_[0.6925 0.1634].png
img: 913 evaluate_data/GlaS/E2CNN/evaluate/testA_7_0_0.pn_1_0.3386_[0.6773 0.    ].png
img: 914 evaluate_data/GlaS/E2CNN/evaluate/testA_7_0_0.pn_2_0.4444_[0.706  0.1827].png
img: 915 evaluate_data/GlaS/E2CNN/evaluate/testA_7_0_0.pn_3_0.4168_[0.6833 0.1502].png
img: 916 evaluate_data/GlaS/E2CNN/evaluate/testA_7_0_405.pn_0_0.2615_[0.1769 0.3462].png
img: 917 evaluate_data/GlaS/E2CNN/evaluate/testA_7_0_405.pn_1_0.5223_[0.397  0.6475].png
img: 918 evaluate_data/GlaS/E2CNN/evaluate/testA_7_0_405.pn_2_0.3852_[0.2154 0.5551].png
img: 919 evaluate_data/GlaS/E2CNN/evaluate/testA_7_0_405.pn_3_0.3991_[0.2286 0.5697].png
img: 920 evaluate_data/GlaS/E2CNN/evaluate/testA_7_126_0.pn_0_0.3158_[0.6283 0.0032].png
img: 921 evaluate_data/GlaS/E2CNN/evaluate/testA_7_126_0.pn_1_0.3594_[0.6842 0.0346].png
img: 922 evaluate_data/GlaS/E2CNN/evaluate/testA_7_126_0.pn_2_0.2991_[0.5734 0.0248].png
img: 923 evaluate_data/GlaS/E2CNN/evaluate/testA_7_126_0.pn_3_0.315_[0.6271 0.003 ].png
img: 924 evaluate_data/GlaS/E2CNN/evaluate/testA_7_126_405.pn_0_0.5002_[0.3906 0.6098].png
img: 925 evaluate_data/GlaS/E2CNN/evaluate/testA_7_126_405.pn_1_0.6598_[0.5105 0.809 ].png
img: 926 evaluate_data/GlaS/E2CNN/evaluate/testA_7_126_405.pn_2_0.6593_[0.5152 0.8033].png
img: 927 evaluate_data/GlaS/E2CNN/evaluate/testA_7_126_405.pn_3_0.4954_[0.3921 0.5988].png
img: 928 evaluate_data/GlaS/E2CNN/evaluate/testA_8_0_0.pn_0_0.6685_[0.5372 0.7998].png
img: 929 evaluate_data/GlaS/E2CNN/evaluate/testA_8_0_0.pn_1_0.5198_[0.4014 0.6382].png
img: 930 evaluate_data/GlaS/E2CNN/evaluate/testA_8_0_0.pn_2_0.5914_[0.4785 0.7042].png
img: 931 evaluate_data/GlaS/E2CNN/evaluate/testA_8_0_0.pn_3_0.6669_[0.5353 0.7985].png
img: 932 evaluate_data/GlaS/E2CNN/evaluate/testA_8_0_405.pn_0_0.6151_[0.5954 0.6348].png
img: 933 evaluate_data/GlaS/E2CNN/evaluate/testA_8_0_405.pn_1_0.5188_[0.5759 0.4616].png
img: 934 evaluate_data/GlaS/E2CNN/evaluate/testA_8_0_405.pn_2_0.6744_[0.6247 0.7242].png
img: 935 evaluate_data/GlaS/E2CNN/evaluate/testA_8_0_405.pn_3_0.5021_[0.4679 0.5363].png
img: 936 evaluate_data/GlaS/E2CNN/evaluate/testA_8_126_0.pn_0_0.5182_[0.4348 0.6017].png
img: 937 evaluate_data/GlaS/E2CNN/evaluate/testA_8_126_0.pn_1_0.5859_[0.4982 0.6735].png
img: 938 evaluate_data/GlaS/E2CNN/evaluate/testA_8_126_0.pn_2_0.5317_[0.432  0.6315].png
img: 939 evaluate_data/GlaS/E2CNN/evaluate/testA_8_126_0.pn_3_0.3189_[0.3562 0.2816].png
img: 940 evaluate_data/GlaS/E2CNN/evaluate/testA_8_126_405.pn_0_0.3406_[0.4408 0.2404].png
img: 941 evaluate_data/GlaS/E2CNN/evaluate/testA_8_126_405.pn_1_0.5252_[0.4421 0.6084].png
img: 942 evaluate_data/GlaS/E2CNN/evaluate/testA_8_126_405.pn_2_0.548_[0.515 0.581].png
img: 943 evaluate_data/GlaS/E2CNN/evaluate/testA_8_126_405.pn_3_0.6491_[0.5374 0.7608].png
img: 944 evaluate_data/GlaS/E2CNN/evaluate/testA_9_0_0.pn_0_0.3206_[0.1691 0.4721].png
img: 945 evaluate_data/GlaS/E2CNN/evaluate/testA_9_0_0.pn_1_0.6415_[0.3875 0.8955].png
img: 946 evaluate_data/GlaS/E2CNN/evaluate/testA_9_0_0.pn_2_0.3049_[0.1812 0.4286].png
img: 947 evaluate_data/GlaS/E2CNN/evaluate/testA_9_0_0.pn_3_0.581_[0.3514 0.8107].png
img: 948 evaluate_data/GlaS/E2CNN/evaluate/testA_9_0_405.pn_0_0.4812_[0.2444 0.7179].png
img: 949 evaluate_data/GlaS/E2CNN/evaluate/testA_9_0_405.pn_1_0.4631_[0.2658 0.6604].png
img: 950 evaluate_data/GlaS/E2CNN/evaluate/testA_9_0_405.pn_2_0.332_[0.1651 0.499 ].png
img: 951 evaluate_data/GlaS/E2CNN/evaluate/testA_9_0_405.pn_3_0.3946_[0.1944 0.5949].png
img: 952 evaluate_data/GlaS/E2CNN/evaluate/testA_9_126_0.pn_0_0.4959_[0.2774 0.7145].png
img: 953 evaluate_data/GlaS/E2CNN/evaluate/testA_9_126_0.pn_1_0.4151_[0.2533 0.577 ].png
img: 954 evaluate_data/GlaS/E2CNN/evaluate/testA_9_126_0.pn_2_0.5086_[0.3123 0.705 ].png
img: 955 evaluate_data/GlaS/E2CNN/evaluate/testA_9_126_0.pn_3_0.2931_[0.2258 0.3605].png
img: 956 evaluate_data/GlaS/E2CNN/evaluate/testA_9_126_405.pn_0_0.4829_[0.2455 0.7204].png
img: 957 evaluate_data/GlaS/E2CNN/evaluate/testA_9_126_405.pn_1_0.4957_[0.2575 0.7338].png
img: 958 evaluate_data/GlaS/E2CNN/evaluate/testA_9_126_405.pn_2_0.3871_[0.185  0.5893].png
img: 959 evaluate_data/GlaS/E2CNN/evaluate/testA_9_126_405.pn_3_0.4577_[0.2543 0.6611].png
img: 960 evaluate_data/GlaS/E2CNN/evaluate/testB_10_0_0.pn_0_0.3062_[0.2565 0.3559].png
img: 961 evaluate_data/GlaS/E2CNN/evaluate/testB_10_0_0.pn_1_0.3485_[0.2679 0.4291].png
img: 962 evaluate_data/GlaS/E2CNN/evaluate/testB_10_0_0.pn_2_0.3485_[0.3047 0.3924].png
img: 963 evaluate_data/GlaS/E2CNN/evaluate/testB_10_0_0.pn_3_0.3611_[0.326  0.3961].png
img: 964 evaluate_data/GlaS/E2CNN/evaluate/testB_10_0_405.pn_0_0.3157_[0.3581 0.2733].png
img: 965 evaluate_data/GlaS/E2CNN/evaluate/testB_10_0_405.pn_1_0.2753_[0.2407 0.3099].png
img: 966 evaluate_data/GlaS/E2CNN/evaluate/testB_10_0_405.pn_2_0.3304_[0.3215 0.3393].png
img: 967 evaluate_data/GlaS/E2CNN/evaluate/testB_10_0_405.pn_3_0.2959_[0.3132 0.2787].png
img: 968 evaluate_data/GlaS/E2CNN/evaluate/testB_10_126_0.pn_0_0.3957_[0.3084 0.483 ].png
img: 969 evaluate_data/GlaS/E2CNN/evaluate/testB_10_126_0.pn_1_0.4057_[0.2571 0.5543].png
img: 970 evaluate_data/GlaS/E2CNN/evaluate/testB_10_126_0.pn_2_0.2978_[0.2793 0.3162].png
img: 971 evaluate_data/GlaS/E2CNN/evaluate/testB_10_126_0.pn_3_0.3636_[0.2447 0.4825].png
img: 972 evaluate_data/GlaS/E2CNN/evaluate/testB_10_126_405.pn_0_0.3758_[0.2638 0.4878].png
img: 973 evaluate_data/GlaS/E2CNN/evaluate/testB_10_126_405.pn_1_0.4415_[0.388  0.4951].png
img: 974 evaluate_data/GlaS/E2CNN/evaluate/testB_10_126_405.pn_2_0.382_[0.2546 0.5095].png
img: 975 evaluate_data/GlaS/E2CNN/evaluate/testB_10_126_405.pn_3_0.5704_[0.4805 0.6602].png
img: 976 evaluate_data/GlaS/E2CNN/evaluate/testB_11_0_0.pn_0_0.6586_[0.4788 0.8384].png
img: 977 evaluate_data/GlaS/E2CNN/evaluate/testB_11_0_0.pn_1_0.7057_[0.5707 0.8406].png
img: 978 evaluate_data/GlaS/E2CNN/evaluate/testB_11_0_0.pn_2_0.7266_[0.5265 0.9267].png
img: 979 evaluate_data/GlaS/E2CNN/evaluate/testB_11_0_0.pn_3_0.6017_[0.4112 0.7923].png
img: 980 evaluate_data/GlaS/E2CNN/evaluate/testB_11_0_405.pn_0_0.6381_[0.5162 0.76  ].png
img: 981 evaluate_data/GlaS/E2CNN/evaluate/testB_11_0_405.pn_1_0.7064_[0.5161 0.8968].png
img: 982 evaluate_data/GlaS/E2CNN/evaluate/testB_11_0_405.pn_2_0.7285_[0.5928 0.8641].png
img: 983 evaluate_data/GlaS/E2CNN/evaluate/testB_11_0_405.pn_3_0.6832_[0.5141 0.8524].png
img: 984 evaluate_data/GlaS/E2CNN/evaluate/testB_11_126_0.pn_0_0.3006_[0.2328 0.3685].png
img: 985 evaluate_data/GlaS/E2CNN/evaluate/testB_11_126_0.pn_1_0.5121_[0.32   0.7042].png
img: 986 evaluate_data/GlaS/E2CNN/evaluate/testB_11_126_0.pn_2_0.4294_[0.2245 0.6343].png
img: 987 evaluate_data/GlaS/E2CNN/evaluate/testB_11_126_0.pn_3_0.4176_[0.244  0.5912].png
img: 988 evaluate_data/GlaS/E2CNN/evaluate/testB_11_126_405.pn_0_0.6222_[0.4386 0.8058].png
img: 989 evaluate_data/GlaS/E2CNN/evaluate/testB_11_126_405.pn_1_0.6347_[0.4696 0.7998].png
img: 990 evaluate_data/GlaS/E2CNN/evaluate/testB_11_126_405.pn_2_0.73_[0.5348 0.9252].png
img: 991 evaluate_data/GlaS/E2CNN/evaluate/testB_11_126_405.pn_3_0.7199_[0.5243 0.9156].png
img: 992 evaluate_data/GlaS/E2CNN/evaluate/testB_12_0_0.pn_0_0.4731_[0.2732 0.673 ].png
img: 993 evaluate_data/GlaS/E2CNN/evaluate/testB_12_0_0.pn_1_0.4694_[0.3141 0.6247].png
img: 994 evaluate_data/GlaS/E2CNN/evaluate/testB_12_0_0.pn_2_0.4684_[0.3459 0.591 ].png
img: 995 evaluate_data/GlaS/E2CNN/evaluate/testB_12_0_0.pn_3_0.4248_[0.3239 0.5258].png
img: 996 evaluate_data/GlaS/E2CNN/evaluate/testB_12_0_405.pn_0_0.5207_[0.2863 0.755 ].png
img: 997 evaluate_data/GlaS/E2CNN/evaluate/testB_12_0_405.pn_1_0.1595_[0.2019 0.1172].png
img: 998 evaluate_data/GlaS/E2CNN/evaluate/testB_12_0_405.pn_2_0.3561_[0.1929 0.5192].png
img: 999 evaluate_data/GlaS/E2CNN/evaluate/testB_12_0_405.pn_3_0.4332_[0.2188 0.6476].png
img: 1000 evaluate_data/GlaS/E2CNN/evaluate/testB_12_126_0.pn_0_0.5552_[0.5074 0.6029].png
img: 1001 evaluate_data/GlaS/E2CNN/evaluate/testB_12_126_0.pn_1_0.3832_[0.4727 0.2937].png
img: 1002 evaluate_data/GlaS/E2CNN/evaluate/testB_12_126_0.pn_2_0.4387_[0.3692 0.5082].png
img: 1003 evaluate_data/GlaS/E2CNN/evaluate/testB_12_126_0.pn_3_0.498_[0.4652 0.5309].png
img: 1004 evaluate_data/GlaS/E2CNN/evaluate/testB_12_126_405.pn_0_0.4748_[0.325  0.6246].png
img: 1005 evaluate_data/GlaS/E2CNN/evaluate/testB_12_126_405.pn_1_0.4807_[0.3489 0.6125].png
img: 1006 evaluate_data/GlaS/E2CNN/evaluate/testB_12_126_405.pn_2_0.473_[0.3799 0.566 ].png
img: 1007 evaluate_data/GlaS/E2CNN/evaluate/testB_12_126_405.pn_3_0.4732_[0.3587 0.5877].png
img: 1008 evaluate_data/GlaS/E2CNN/evaluate/testB_13_0_0.pn_0_0.6566_[0.624  0.6893].png
img: 1009 evaluate_data/GlaS/E2CNN/evaluate/testB_13_0_0.pn_1_0.4187_[0.3686 0.4689].png
img: 1010 evaluate_data/GlaS/E2CNN/evaluate/testB_13_0_0.pn_2_0.4693_[0.4457 0.4928].png
img: 1011 evaluate_data/GlaS/E2CNN/evaluate/testB_13_0_0.pn_3_0.4109_[0.4299 0.3918].png
img: 1012 evaluate_data/GlaS/E2CNN/evaluate/testB_13_0_405.pn_0_0.4912_[0.4218 0.5605].png
img: 1013 evaluate_data/GlaS/E2CNN/evaluate/testB_13_0_405.pn_1_0.4873_[0.3904 0.5842].png
img: 1014 evaluate_data/GlaS/E2CNN/evaluate/testB_13_0_405.pn_2_0.3875_[0.3107 0.4643].png
img: 1015 evaluate_data/GlaS/E2CNN/evaluate/testB_13_0_405.pn_3_0.4962_[0.4309 0.5614].png
img: 1016 evaluate_data/GlaS/E2CNN/evaluate/testB_13_126_0.pn_0_0.676_[0.4939 0.8581].png
img: 1017 evaluate_data/GlaS/E2CNN/evaluate/testB_13_126_0.pn_1_0.4136_[0.3432 0.484 ].png
img: 1018 evaluate_data/GlaS/E2CNN/evaluate/testB_13_126_0.pn_2_0.3828_[0.3274 0.4383].png
img: 1019 evaluate_data/GlaS/E2CNN/evaluate/testB_13_126_0.pn_3_0.2892_[0.2231 0.3553].png
img: 1020 evaluate_data/GlaS/E2CNN/evaluate/testB_13_126_405.pn_0_0.5281_[0.4845 0.5718].png
img: 1021 evaluate_data/GlaS/E2CNN/evaluate/testB_13_126_405.pn_1_0.3766_[0.3249 0.4284].png
img: 1022 evaluate_data/GlaS/E2CNN/evaluate/testB_13_126_405.pn_2_0.6759_[0.5768 0.775 ].png
img: 1023 evaluate_data/GlaS/E2CNN/evaluate/testB_13_126_405.pn_3_0.6018_[0.5557 0.6479].png
img: 1024 evaluate_data/GlaS/E2CNN/evaluate/testB_14_0_0.pn_0_0.4474_[0.4913 0.4034].png
img: 1025 evaluate_data/GlaS/E2CNN/evaluate/testB_14_0_0.pn_1_0.3771_[0.5018 0.2523].png
img: 1026 evaluate_data/GlaS/E2CNN/evaluate/testB_14_0_0.pn_2_0.4677_[0.5105 0.425 ].png
img: 1027 evaluate_data/GlaS/E2CNN/evaluate/testB_14_0_0.pn_3_0.3274_[0.498  0.1569].png
img: 1028 evaluate_data/GlaS/E2CNN/evaluate/testB_14_0_405.pn_0_0.22_[0.1742 0.2657].png
img: 1029 evaluate_data/GlaS/E2CNN/evaluate/testB_14_0_405.pn_1_0.2247_[0.1366 0.3128].png
img: 1030 evaluate_data/GlaS/E2CNN/evaluate/testB_14_0_405.pn_2_0.1579_[0.1631 0.1528].png
img: 1031 evaluate_data/GlaS/E2CNN/evaluate/testB_14_0_405.pn_3_0.1941_[0.169  0.2191].png
img: 1032 evaluate_data/GlaS/E2CNN/evaluate/testB_14_126_0.pn_0_0.3015_[0.5973 0.0057].png
img: 1033 evaluate_data/GlaS/E2CNN/evaluate/testB_14_126_0.pn_1_0.3298_[0.5997 0.0599].png
img: 1034 evaluate_data/GlaS/E2CNN/evaluate/testB_14_126_0.pn_2_0.5961_[0.6486 0.5435].png
img: 1035 evaluate_data/GlaS/E2CNN/evaluate/testB_14_126_0.pn_3_0.464_[0.6276 0.3003].png
img: 1036 evaluate_data/GlaS/E2CNN/evaluate/testB_14_126_405.pn_0_0.3035_[0.3352 0.2717].png
img: 1037 evaluate_data/GlaS/E2CNN/evaluate/testB_14_126_405.pn_1_0.2375_[0.334  0.1409].png
img: 1038 evaluate_data/GlaS/E2CNN/evaluate/testB_14_126_405.pn_2_0.2184_[0.328  0.1089].png
img: 1039 evaluate_data/GlaS/E2CNN/evaluate/testB_14_126_405.pn_3_0.1699_[0.3063 0.0336].png
img: 1040 evaluate_data/GlaS/E2CNN/evaluate/testB_15_0_0.pn_0_0.5648_[0.4951 0.6344].png
img: 1041 evaluate_data/GlaS/E2CNN/evaluate/testB_15_0_0.pn_1_0.4262_[0.4382 0.4143].png
img: 1042 evaluate_data/GlaS/E2CNN/evaluate/testB_15_0_0.pn_2_0.3677_[0.3846 0.3507].png
img: 1043 evaluate_data/GlaS/E2CNN/evaluate/testB_15_0_0.pn_3_0.5638_[0.508  0.6197].png
img: 1044 evaluate_data/GlaS/E2CNN/evaluate/testB_15_0_405.pn_0_0.557_[0.5105 0.6035].png
img: 1045 evaluate_data/GlaS/E2CNN/evaluate/testB_15_0_405.pn_1_0.4675_[0.4769 0.4581].png
img: 1046 evaluate_data/GlaS/E2CNN/evaluate/testB_15_0_405.pn_2_0.5239_[0.5041 0.5437].png
img: 1047 evaluate_data/GlaS/E2CNN/evaluate/testB_15_0_405.pn_3_0.4382_[0.4802 0.3963].png
img: 1048 evaluate_data/GlaS/E2CNN/evaluate/testB_15_126_0.pn_0_0.3729_[0.2911 0.4547].png
img: 1049 evaluate_data/GlaS/E2CNN/evaluate/testB_15_126_0.pn_1_0.4095_[0.3357 0.4832].png
img: 1050 evaluate_data/GlaS/E2CNN/evaluate/testB_15_126_0.pn_2_0.3558_[0.3033 0.4083].png
img: 1051 evaluate_data/GlaS/E2CNN/evaluate/testB_15_126_0.pn_3_0.4295_[0.3951 0.4639].png
img: 1052 evaluate_data/GlaS/E2CNN/evaluate/testB_15_126_405.pn_0_0.5184_[0.5397 0.497 ].png
img: 1053 evaluate_data/GlaS/E2CNN/evaluate/testB_15_126_405.pn_1_0.5442_[0.5382 0.5503].png
img: 1054 evaluate_data/GlaS/E2CNN/evaluate/testB_15_126_405.pn_2_0.4343_[0.5234 0.3452].png
img: 1055 evaluate_data/GlaS/E2CNN/evaluate/testB_15_126_405.pn_3_0.4788_[0.5313 0.4264].png
img: 1056 evaluate_data/GlaS/E2CNN/evaluate/testB_16_0_0.pn_0_0.4384_[0.3337 0.5431].png
img: 1057 evaluate_data/GlaS/E2CNN/evaluate/testB_16_0_0.pn_1_0.5109_[0.3867 0.6351].png
img: 1058 evaluate_data/GlaS/E2CNN/evaluate/testB_16_0_0.pn_2_0.1665_[0.3331 0.    ].png
img: 1059 evaluate_data/GlaS/E2CNN/evaluate/testB_16_0_0.pn_3_0.4133_[0.3267 0.5   ].png
img: 1060 evaluate_data/GlaS/E2CNN/evaluate/testB_16_0_405.pn_0_0.2423_[0.2315 0.2532].png
img: 1061 evaluate_data/GlaS/E2CNN/evaluate/testB_16_0_405.pn_1_0.492_[0.3266 0.6574].png
img: 1062 evaluate_data/GlaS/E2CNN/evaluate/testB_16_0_405.pn_2_0.1768_[0.2172 0.1364].png
img: 1063 evaluate_data/GlaS/E2CNN/evaluate/testB_16_0_405.pn_3_0.3308_[0.2509 0.4108].png
img: 1064 evaluate_data/GlaS/E2CNN/evaluate/testB_16_126_0.pn_0_0.4097_[0.3526 0.4668].png
img: 1065 evaluate_data/GlaS/E2CNN/evaluate/testB_16_126_0.pn_1_0.4424_[0.3953 0.4895].png
img: 1066 evaluate_data/GlaS/E2CNN/evaluate/testB_16_126_0.pn_2_0.258_[0.2851 0.231 ].png
img: 1067 evaluate_data/GlaS/E2CNN/evaluate/testB_16_126_0.pn_3_0.4191_[0.3377 0.5006].png
img: 1068 evaluate_data/GlaS/E2CNN/evaluate/testB_16_126_405.pn_0_0.3285_[0.2186 0.4384].png
img: 1069 evaluate_data/GlaS/E2CNN/evaluate/testB_16_126_405.pn_1_0.3846_[0.2446 0.5246].png
img: 1070 evaluate_data/GlaS/E2CNN/evaluate/testB_16_126_405.pn_2_0.4279_[0.2391 0.6166].png
img: 1071 evaluate_data/GlaS/E2CNN/evaluate/testB_16_126_405.pn_3_0.3026_[0.2064 0.3988].png
img: 1072 evaluate_data/GlaS/E2CNN/evaluate/testB_17_0_0.pn_0_0.37_[0.3071 0.433 ].png
img: 1073 evaluate_data/GlaS/E2CNN/evaluate/testB_17_0_0.pn_1_0.2662_[0.2634 0.2691].png
img: 1074 evaluate_data/GlaS/E2CNN/evaluate/testB_17_0_0.pn_2_0.2358_[0.2555 0.2161].png
img: 1075 evaluate_data/GlaS/E2CNN/evaluate/testB_17_0_0.pn_3_0.2827_[0.2453 0.3202].png
img: 1076 evaluate_data/GlaS/E2CNN/evaluate/testB_17_0_405.pn_0_0.2109_[0.0972 0.3247].png
img: 1077 evaluate_data/GlaS/E2CNN/evaluate/testB_17_0_405.pn_1_0.1645_[0.1148 0.2141].png
img: 1078 evaluate_data/GlaS/E2CNN/evaluate/testB_17_0_405.pn_2_0.1238_[0.1265 0.1212].png
img: 1079 evaluate_data/GlaS/E2CNN/evaluate/testB_17_0_405.pn_3_0.196_[0.1112 0.2808].png
img: 1080 evaluate_data/GlaS/E2CNN/evaluate/testB_17_126_0.pn_0_0.4095_[0.3335 0.4856].png
img: 1081 evaluate_data/GlaS/E2CNN/evaluate/testB_17_126_0.pn_1_0.444_[0.3252 0.5627].png
img: 1082 evaluate_data/GlaS/E2CNN/evaluate/testB_17_126_0.pn_2_0.2749_[0.3136 0.2363].png
img: 1083 evaluate_data/GlaS/E2CNN/evaluate/testB_17_126_0.pn_3_0.489_[0.3846 0.5934].png
img: 1084 evaluate_data/GlaS/E2CNN/evaluate/testB_17_126_405.pn_0_0.0117_[0.0234 0.    ].png
img: 1085 evaluate_data/GlaS/E2CNN/evaluate/testB_17_126_405.pn_1_0.1943_[0.0295 0.3592].png
img: 1086 evaluate_data/GlaS/E2CNN/evaluate/testB_17_126_405.pn_2_0.0863_[0.0258 0.1469].png
img: 1087 evaluate_data/GlaS/E2CNN/evaluate/testB_17_126_405.pn_3_0.0801_[0.0251 0.1351].png
img: 1088 evaluate_data/GlaS/E2CNN/evaluate/testB_18_0_0.pn_0_0.5796_[0.5131 0.6461].png
img: 1089 evaluate_data/GlaS/E2CNN/evaluate/testB_18_0_0.pn_1_0.5104_[0.4307 0.59  ].png
img: 1090 evaluate_data/GlaS/E2CNN/evaluate/testB_18_0_0.pn_2_0.6222_[0.5557 0.6888].png
img: 1091 evaluate_data/GlaS/E2CNN/evaluate/testB_18_0_0.pn_3_0.5744_[0.5084 0.6403].png
img: 1092 evaluate_data/GlaS/E2CNN/evaluate/testB_18_0_405.pn_0_0.5502_[0.3473 0.7531].png
img: 1093 evaluate_data/GlaS/E2CNN/evaluate/testB_18_0_405.pn_1_0.4074_[0.2781 0.5367].png
img: 1094 evaluate_data/GlaS/E2CNN/evaluate/testB_18_0_405.pn_2_0.3732_[0.1906 0.5558].png
img: 1095 evaluate_data/GlaS/E2CNN/evaluate/testB_18_0_405.pn_3_0.6032_[0.3897 0.8166].png
img: 1096 evaluate_data/GlaS/E2CNN/evaluate/testB_18_126_0.pn_0_0.739_[0.79   0.6879].png
img: 1097 evaluate_data/GlaS/E2CNN/evaluate/testB_18_126_0.pn_1_0.5117_[0.4737 0.5496].png
img: 1098 evaluate_data/GlaS/E2CNN/evaluate/testB_18_126_0.pn_2_0.6537_[0.6132 0.6941].png
img: 1099 evaluate_data/GlaS/E2CNN/evaluate/testB_18_126_0.pn_3_0.735_[0.7605 0.7096].png
img: 1100 evaluate_data/GlaS/E2CNN/evaluate/testB_18_126_405.pn_0_0.6734_[0.5188 0.828 ].png
img: 1101 evaluate_data/GlaS/E2CNN/evaluate/testB_18_126_405.pn_1_0.6122_[0.4483 0.776 ].png
img: 1102 evaluate_data/GlaS/E2CNN/evaluate/testB_18_126_405.pn_2_0.5784_[0.4346 0.7222].png
img: 1103 evaluate_data/GlaS/E2CNN/evaluate/testB_18_126_405.pn_3_0.6093_[0.4392 0.7794].png
img: 1104 evaluate_data/GlaS/E2CNN/evaluate/testB_19_0_0.pn_0_0.6036_[0.4341 0.773 ].png
img: 1105 evaluate_data/GlaS/E2CNN/evaluate/testB_19_0_0.pn_1_0.635_[0.4945 0.7755].png
img: 1106 evaluate_data/GlaS/E2CNN/evaluate/testB_19_0_0.pn_2_0.6374_[0.478  0.7968].png
img: 1107 evaluate_data/GlaS/E2CNN/evaluate/testB_19_0_0.pn_3_0.5877_[0.4096 0.7659].png
img: 1108 evaluate_data/GlaS/E2CNN/evaluate/testB_19_0_405.pn_0_0.3781_[0.4472 0.3091].png
img: 1109 evaluate_data/GlaS/E2CNN/evaluate/testB_19_0_405.pn_1_0.3608_[0.5082 0.2134].png
img: 1110 evaluate_data/GlaS/E2CNN/evaluate/testB_19_0_405.pn_2_0.4816_[0.4919 0.4712].png
img: 1111 evaluate_data/GlaS/E2CNN/evaluate/testB_19_0_405.pn_3_0.5588_[0.6055 0.5121].png
img: 1112 evaluate_data/GlaS/E2CNN/evaluate/testB_19_126_0.pn_0_0.6027_[0.4961 0.7092].png
img: 1113 evaluate_data/GlaS/E2CNN/evaluate/testB_19_126_0.pn_1_0.5733_[0.4827 0.664 ].png
img: 1114 evaluate_data/GlaS/E2CNN/evaluate/testB_19_126_0.pn_2_0.6681_[0.5294 0.8068].png
img: 1115 evaluate_data/GlaS/E2CNN/evaluate/testB_19_126_0.pn_3_0.6498_[0.5258 0.7738].png
img: 1116 evaluate_data/GlaS/E2CNN/evaluate/testB_19_126_405.pn_0_0.4996_[0.5961 0.4032].png
img: 1117 evaluate_data/GlaS/E2CNN/evaluate/testB_19_126_405.pn_1_0.6347_[0.6592 0.6102].png
img: 1118 evaluate_data/GlaS/E2CNN/evaluate/testB_19_126_405.pn_2_0.5308_[0.6037 0.4579].png
img: 1119 evaluate_data/GlaS/E2CNN/evaluate/testB_19_126_405.pn_3_0.6349_[0.6568 0.613 ].png
img: 1120 evaluate_data/GlaS/E2CNN/evaluate/testB_1_0_0.pn_0_0.3135_[0.1935 0.4335].png
img: 1121 evaluate_data/GlaS/E2CNN/evaluate/testB_1_0_0.pn_1_0.2665_[0.1791 0.3539].png
img: 1122 evaluate_data/GlaS/E2CNN/evaluate/testB_1_0_0.pn_2_0.2713_[0.1782 0.3644].png
img: 1123 evaluate_data/GlaS/E2CNN/evaluate/testB_1_0_0.pn_3_0.203_[0.1636 0.2423].png
img: 1124 evaluate_data/GlaS/E2CNN/evaluate/testB_1_0_405.pn_0_0.6197_[0.733  0.5064].png
img: 1125 evaluate_data/GlaS/E2CNN/evaluate/testB_1_0_405.pn_1_0.547_[0.7063 0.3877].png
img: 1126 evaluate_data/GlaS/E2CNN/evaluate/testB_1_0_405.pn_2_0.6641_[0.7957 0.5325].png
img: 1127 evaluate_data/GlaS/E2CNN/evaluate/testB_1_0_405.pn_3_0.5196_[0.6615 0.3776].png
img: 1128 evaluate_data/GlaS/E2CNN/evaluate/testB_1_126_0.pn_0_0.2253_[0.2997 0.1508].png
img: 1129 evaluate_data/GlaS/E2CNN/evaluate/testB_1_126_0.pn_1_0.2616_[0.2986 0.2246].png
img: 1130 evaluate_data/GlaS/E2CNN/evaluate/testB_1_126_0.pn_2_0.385_[0.2948 0.4753].png
img: 1131 evaluate_data/GlaS/E2CNN/evaluate/testB_1_126_0.pn_3_0.2733_[0.2922 0.2543].png
img: 1132 evaluate_data/GlaS/E2CNN/evaluate/testB_1_126_405.pn_0_0.6748_[0.7668 0.5828].png
img: 1133 evaluate_data/GlaS/E2CNN/evaluate/testB_1_126_405.pn_1_0.693_[0.7525 0.6335].png
img: 1134 evaluate_data/GlaS/E2CNN/evaluate/testB_1_126_405.pn_2_0.3704_[0.6465 0.0944].png
img: 1135 evaluate_data/GlaS/E2CNN/evaluate/testB_1_126_405.pn_3_0.5404_[0.6978 0.383 ].png
img: 1136 evaluate_data/GlaS/E2CNN/evaluate/testB_20_0_0.pn_0_0.5048_[0.23   0.7797].png
img: 1137 evaluate_data/GlaS/E2CNN/evaluate/testB_20_0_0.pn_1_0.6019_[0.3282 0.8756].png
img: 1138 evaluate_data/GlaS/E2CNN/evaluate/testB_20_0_0.pn_2_0.2283_[0.1277 0.3289].png
img: 1139 evaluate_data/GlaS/E2CNN/evaluate/testB_20_0_0.pn_3_0.2429_[0.1494 0.3363].png
img: 1140 evaluate_data/GlaS/E2CNN/evaluate/testB_20_0_405.pn_0_0.5588_[0.4129 0.7048].png
img: 1141 evaluate_data/GlaS/E2CNN/evaluate/testB_20_0_405.pn_1_0.3655_[0.2991 0.4319].png
img: 1142 evaluate_data/GlaS/E2CNN/evaluate/testB_20_0_405.pn_2_0.3018_[0.2151 0.3885].png
img: 1143 evaluate_data/GlaS/E2CNN/evaluate/testB_20_0_405.pn_3_0.2793_[0.257  0.3016].png
img: 1144 evaluate_data/GlaS/E2CNN/evaluate/testB_20_126_0.pn_0_0.3948_[0.2276 0.562 ].png
img: 1145 evaluate_data/GlaS/E2CNN/evaluate/testB_20_126_0.pn_1_0.3276_[0.1774 0.4778].png
img: 1146 evaluate_data/GlaS/E2CNN/evaluate/testB_20_126_0.pn_2_0.2547_[0.145  0.3643].png
img: 1147 evaluate_data/GlaS/E2CNN/evaluate/testB_20_126_0.pn_3_0.2664_[0.1684 0.3644].png
img: 1148 evaluate_data/GlaS/E2CNN/evaluate/testB_20_126_405.pn_0_0.3068_[0.2113 0.4023].png
img: 1149 evaluate_data/GlaS/E2CNN/evaluate/testB_20_126_405.pn_1_0.5252_[0.349  0.7014].png
img: 1150 evaluate_data/GlaS/E2CNN/evaluate/testB_20_126_405.pn_2_0.3523_[0.2313 0.4733].png
img: 1151 evaluate_data/GlaS/E2CNN/evaluate/testB_20_126_405.pn_3_0.4798_[0.3275 0.6321].png
img: 1152 evaluate_data/GlaS/E2CNN/evaluate/testB_2_0_0.pn_0_0.6878_[0.5831 0.7925].png
img: 1153 evaluate_data/GlaS/E2CNN/evaluate/testB_2_0_0.pn_1_0.451_[0.366  0.5359].png
img: 1154 evaluate_data/GlaS/E2CNN/evaluate/testB_2_0_0.pn_2_0.6128_[0.5465 0.6791].png
img: 1155 evaluate_data/GlaS/E2CNN/evaluate/testB_2_0_0.pn_3_0.4786_[0.4053 0.5519].png
img: 1156 evaluate_data/GlaS/E2CNN/evaluate/testB_2_0_405.pn_0_0.4022_[0.2941 0.5103].png
img: 1157 evaluate_data/GlaS/E2CNN/evaluate/testB_2_0_405.pn_1_0.5947_[0.463  0.7265].png
img: 1158 evaluate_data/GlaS/E2CNN/evaluate/testB_2_0_405.pn_2_0.5263_[0.4546 0.598 ].png
img: 1159 evaluate_data/GlaS/E2CNN/evaluate/testB_2_0_405.pn_3_0.392_[0.3537 0.4304].png
img: 1160 evaluate_data/GlaS/E2CNN/evaluate/testB_2_126_0.pn_0_0.611_[0.5098 0.7121].png
img: 1161 evaluate_data/GlaS/E2CNN/evaluate/testB_2_126_0.pn_1_0.5812_[0.5042 0.6581].png
img: 1162 evaluate_data/GlaS/E2CNN/evaluate/testB_2_126_0.pn_2_0.5073_[0.4208 0.5938].png
img: 1163 evaluate_data/GlaS/E2CNN/evaluate/testB_2_126_0.pn_3_0.534_[0.4639 0.6041].png
img: 1164 evaluate_data/GlaS/E2CNN/evaluate/testB_2_126_405.pn_0_0.5273_[0.4501 0.6045].png
img: 1165 evaluate_data/GlaS/E2CNN/evaluate/testB_2_126_405.pn_1_0.5884_[0.4478 0.7291].png
img: 1166 evaluate_data/GlaS/E2CNN/evaluate/testB_2_126_405.pn_2_0.6741_[0.522  0.8261].png
img: 1167 evaluate_data/GlaS/E2CNN/evaluate/testB_2_126_405.pn_3_0.5667_[0.3993 0.7342].png
img: 1168 evaluate_data/GlaS/E2CNN/evaluate/testB_3_0_0.pn_0_0.4995_[0.3583 0.6407].png
img: 1169 evaluate_data/GlaS/E2CNN/evaluate/testB_3_0_0.pn_1_0.3972_[0.2951 0.4994].png
img: 1170 evaluate_data/GlaS/E2CNN/evaluate/testB_3_0_0.pn_2_0.6989_[0.503  0.8949].png
img: 1171 evaluate_data/GlaS/E2CNN/evaluate/testB_3_0_0.pn_3_0.5084_[0.3603 0.6564].png
img: 1172 evaluate_data/GlaS/E2CNN/evaluate/testB_3_0_405.pn_0_0.5801_[0.6375 0.5227].png
img: 1173 evaluate_data/GlaS/E2CNN/evaluate/testB_3_0_405.pn_1_0.4212_[0.4857 0.3566].png
img: 1174 evaluate_data/GlaS/E2CNN/evaluate/testB_3_0_405.pn_2_0.4165_[0.4922 0.3409].png
img: 1175 evaluate_data/GlaS/E2CNN/evaluate/testB_3_0_405.pn_3_0.552_[0.5824 0.5216].png
img: 1176 evaluate_data/GlaS/E2CNN/evaluate/testB_3_126_0.pn_0_0.6119_[0.4695 0.7543].png
img: 1177 evaluate_data/GlaS/E2CNN/evaluate/testB_3_126_0.pn_1_0.3513_[0.233  0.4696].png
img: 1178 evaluate_data/GlaS/E2CNN/evaluate/testB_3_126_0.pn_2_0.5681_[0.4409 0.6954].png
img: 1179 evaluate_data/GlaS/E2CNN/evaluate/testB_3_126_0.pn_3_0.4176_[0.2022 0.633 ].png
img: 1180 evaluate_data/GlaS/E2CNN/evaluate/testB_3_126_405.pn_0_0.6991_[0.6595 0.7387].png
img: 1181 evaluate_data/GlaS/E2CNN/evaluate/testB_3_126_405.pn_1_0.4818_[0.5424 0.4212].png
img: 1182 evaluate_data/GlaS/E2CNN/evaluate/testB_3_126_405.pn_2_0.4834_[0.4651 0.5017].png
img: 1183 evaluate_data/GlaS/E2CNN/evaluate/testB_3_126_405.pn_3_0.6286_[0.6023 0.6548].png
img: 1184 evaluate_data/GlaS/E2CNN/evaluate/testB_4_0_0.pn_0_0.5461_[0.4915 0.6007].png
img: 1185 evaluate_data/GlaS/E2CNN/evaluate/testB_4_0_0.pn_1_0.388_[0.431  0.3451].png
img: 1186 evaluate_data/GlaS/E2CNN/evaluate/testB_4_0_0.pn_2_0.3535_[0.384 0.323].png
img: 1187 evaluate_data/GlaS/E2CNN/evaluate/testB_4_0_0.pn_3_0.3687_[0.3725 0.3649].png
img: 1188 evaluate_data/GlaS/E2CNN/evaluate/testB_4_0_405.pn_0_0.2019_[0.1937 0.2101].png
img: 1189 evaluate_data/GlaS/E2CNN/evaluate/testB_4_0_405.pn_1_0.1131_[0.1944 0.0318].png
img: 1190 evaluate_data/GlaS/E2CNN/evaluate/testB_4_0_405.pn_2_0.2648_[0.1835 0.346 ].png
img: 1191 evaluate_data/GlaS/E2CNN/evaluate/testB_4_0_405.pn_3_0.2763_[0.1902 0.3625].png
img: 1192 evaluate_data/GlaS/E2CNN/evaluate/testB_4_126_0.pn_0_0.3228_[0.2944 0.3512].png
img: 1193 evaluate_data/GlaS/E2CNN/evaluate/testB_4_126_0.pn_1_0.4896_[0.4088 0.5705].png
img: 1194 evaluate_data/GlaS/E2CNN/evaluate/testB_4_126_0.pn_2_0.2372_[0.3337 0.1406].png
img: 1195 evaluate_data/GlaS/E2CNN/evaluate/testB_4_126_0.pn_3_0.2621_[0.2587 0.2655].png
img: 1196 evaluate_data/GlaS/E2CNN/evaluate/testB_4_126_405.pn_0_0.0603_[0.1201 0.0006].png
img: 1197 evaluate_data/GlaS/E2CNN/evaluate/testB_4_126_405.pn_1_0.2698_[0.1418 0.3978].png
img: 1198 evaluate_data/GlaS/E2CNN/evaluate/testB_4_126_405.pn_2_0.2265_[0.1246 0.3284].png
img: 1199 evaluate_data/GlaS/E2CNN/evaluate/testB_4_126_405.pn_3_0.1727_[0.1154 0.2301].png
img: 1200 evaluate_data/GlaS/E2CNN/evaluate/testB_5_0_0.pn_0_0.7415_[0.6577 0.8253].png
img: 1201 evaluate_data/GlaS/E2CNN/evaluate/testB_5_0_0.pn_1_0.6606_[0.6262 0.695 ].png
img: 1202 evaluate_data/GlaS/E2CNN/evaluate/testB_5_0_0.pn_2_0.3751_[0.5352 0.2149].png
img: 1203 evaluate_data/GlaS/E2CNN/evaluate/testB_5_0_0.pn_3_0.7873_[0.6917 0.8829].png
img: 1204 evaluate_data/GlaS/E2CNN/evaluate/testB_5_0_405.pn_0_0.3995_[0.3379 0.4611].png
img: 1205 evaluate_data/GlaS/E2CNN/evaluate/testB_5_0_405.pn_1_0.4966_[0.3949 0.5984].png
img: 1206 evaluate_data/GlaS/E2CNN/evaluate/testB_5_0_405.pn_2_0.4111_[0.3376 0.4846].png
img: 1207 evaluate_data/GlaS/E2CNN/evaluate/testB_5_0_405.pn_3_0.3695_[0.332  0.4071].png
img: 1208 evaluate_data/GlaS/E2CNN/evaluate/testB_5_126_0.pn_0_0.4123_[0.5052 0.3195].png
img: 1209 evaluate_data/GlaS/E2CNN/evaluate/testB_5_126_0.pn_1_0.7513_[0.6935 0.8092].png
img: 1210 evaluate_data/GlaS/E2CNN/evaluate/testB_5_126_0.pn_2_0.5998_[0.6047 0.5949].png
img: 1211 evaluate_data/GlaS/E2CNN/evaluate/testB_5_126_0.pn_3_0.701_[0.6811 0.721 ].png
img: 1212 evaluate_data/GlaS/E2CNN/evaluate/testB_5_126_405.pn_0_0.3086_[0.3923 0.225 ].png
img: 1213 evaluate_data/GlaS/E2CNN/evaluate/testB_5_126_405.pn_1_0.421_[0.4579 0.3841].png
img: 1214 evaluate_data/GlaS/E2CNN/evaluate/testB_5_126_405.pn_2_0.3259_[0.3975 0.2543].png
img: 1215 evaluate_data/GlaS/E2CNN/evaluate/testB_5_126_405.pn_3_0.632_[0.5414 0.7225].png
img: 1216 evaluate_data/GlaS/E2CNN/evaluate/testB_6_0_0.pn_0_0.4646_[0.3457 0.5835].png
img: 1217 evaluate_data/GlaS/E2CNN/evaluate/testB_6_0_0.pn_1_0.4073_[0.3262 0.4883].png
img: 1218 evaluate_data/GlaS/E2CNN/evaluate/testB_6_0_0.pn_2_0.2484_[0.278  0.2188].png
img: 1219 evaluate_data/GlaS/E2CNN/evaluate/testB_6_0_0.pn_3_0.418_[0.3279 0.5081].png
img: 1220 evaluate_data/GlaS/E2CNN/evaluate/testB_6_0_405.pn_0_0.4229_[0.7667 0.0792].png
img: 1221 evaluate_data/GlaS/E2CNN/evaluate/testB_6_0_405.pn_1_0.3853_[0.7706 0.    ].png
img: 1222 evaluate_data/GlaS/E2CNN/evaluate/testB_6_0_405.pn_2_0.3823_[0.7647 0.    ].png
img: 1223 evaluate_data/GlaS/E2CNN/evaluate/testB_6_0_405.pn_3_0.3822_[0.7645 0.    ].png
img: 1224 evaluate_data/GlaS/E2CNN/evaluate/testB_6_126_0.pn_0_0.3819_[0.2303 0.5334].png
img: 1225 evaluate_data/GlaS/E2CNN/evaluate/testB_6_126_0.pn_1_0.3719_[0.2323 0.5115].png
img: 1226 evaluate_data/GlaS/E2CNN/evaluate/testB_6_126_0.pn_2_0.5698_[0.3173 0.8224].png
img: 1227 evaluate_data/GlaS/E2CNN/evaluate/testB_6_126_0.pn_3_0.563_[0.338  0.7879].png
img: 1228 evaluate_data/GlaS/E2CNN/evaluate/testB_6_126_405.pn_0_0.3706_[0.7411 0.    ].png
img: 1229 evaluate_data/GlaS/E2CNN/evaluate/testB_6_126_405.pn_1_0.3808_[0.6942 0.0674].png
img: 1230 evaluate_data/GlaS/E2CNN/evaluate/testB_6_126_405.pn_2_0.3375_[0.6751 0.    ].png
img: 1231 evaluate_data/GlaS/E2CNN/evaluate/testB_6_126_405.pn_3_0.3371_[0.601  0.0732].png
img: 1232 evaluate_data/GlaS/E2CNN/evaluate/testB_7_0_0.pn_0_0.2277_[0.2558 0.1995].png
img: 1233 evaluate_data/GlaS/E2CNN/evaluate/testB_7_0_0.pn_1_0.6905_[0.5444 0.8366].png
img: 1234 evaluate_data/GlaS/E2CNN/evaluate/testB_7_0_0.pn_2_0.2807_[0.2837 0.2778].png
img: 1235 evaluate_data/GlaS/E2CNN/evaluate/testB_7_0_0.pn_3_0.2335_[0.2592 0.2078].png
img: 1236 evaluate_data/GlaS/E2CNN/evaluate/testB_7_0_405.pn_0_0.2763_[0.3248 0.2277].png
img: 1237 evaluate_data/GlaS/E2CNN/evaluate/testB_7_0_405.pn_1_0.2682_[0.2487 0.2877].png
img: 1238 evaluate_data/GlaS/E2CNN/evaluate/testB_7_0_405.pn_2_0.3527_[0.2969 0.4086].png
img: 1239 evaluate_data/GlaS/E2CNN/evaluate/testB_7_0_405.pn_3_0.258_[0.3371 0.179 ].png
img: 1240 evaluate_data/GlaS/E2CNN/evaluate/testB_7_126_0.pn_0_0.6789_[0.5015 0.8562].png
img: 1241 evaluate_data/GlaS/E2CNN/evaluate/testB_7_126_0.pn_1_0.23_[0.306 0.154].png
img: 1242 evaluate_data/GlaS/E2CNN/evaluate/testB_7_126_0.pn_2_0.2165_[0.2985 0.1345].png
img: 1243 evaluate_data/GlaS/E2CNN/evaluate/testB_7_126_0.pn_3_0.2244_[0.2938 0.155 ].png
img: 1244 evaluate_data/GlaS/E2CNN/evaluate/testB_7_126_405.pn_0_0.3689_[0.3397 0.398 ].png
img: 1245 evaluate_data/GlaS/E2CNN/evaluate/testB_7_126_405.pn_1_0.2664_[0.2858 0.2471].png
img: 1246 evaluate_data/GlaS/E2CNN/evaluate/testB_7_126_405.pn_2_0.6267_[0.4597 0.7937].png
img: 1247 evaluate_data/GlaS/E2CNN/evaluate/testB_7_126_405.pn_3_0.1824_[0.2516 0.1132].png
img: 1248 evaluate_data/GlaS/E2CNN/evaluate/testB_8_0_0.pn_0_0.2413_[0.0472 0.4353].png
img: 1249 evaluate_data/GlaS/E2CNN/evaluate/testB_8_0_0.pn_1_0.3247_[0.1746 0.4747].png
img: 1250 evaluate_data/GlaS/E2CNN/evaluate/testB_8_0_0.pn_2_0.2858_[0.2567 0.315 ].png
img: 1251 evaluate_data/GlaS/E2CNN/evaluate/testB_8_0_0.pn_3_0.2828_[0.0949 0.4706].png
img: 1252 evaluate_data/GlaS/E2CNN/evaluate/testB_8_0_405.pn_0_0.6213_[0.6104 0.6322].png
img: 1253 evaluate_data/GlaS/E2CNN/evaluate/testB_8_0_405.pn_1_0.4593_[0.4706 0.4481].png
img: 1254 evaluate_data/GlaS/E2CNN/evaluate/testB_8_0_405.pn_2_0.5237_[0.5686 0.4787].png
img: 1255 evaluate_data/GlaS/E2CNN/evaluate/testB_8_0_405.pn_3_0.4052_[0.4461 0.3644].png
img: 1256 evaluate_data/GlaS/E2CNN/evaluate/testB_8_126_0.pn_0_0.2787_[0.2259 0.3316].png
img: 1257 evaluate_data/GlaS/E2CNN/evaluate/testB_8_126_0.pn_1_0.2341_[0.1624 0.3059].png
img: 1258 evaluate_data/GlaS/E2CNN/evaluate/testB_8_126_0.pn_2_0.2172_[0.1192 0.3151].png
img: 1259 evaluate_data/GlaS/E2CNN/evaluate/testB_8_126_0.pn_3_0.2459_[0.19   0.3018].png
img: 1260 evaluate_data/GlaS/E2CNN/evaluate/testB_8_126_405.pn_0_0.6101_[0.5335 0.6868].png
img: 1261 evaluate_data/GlaS/E2CNN/evaluate/testB_8_126_405.pn_1_0.6458_[0.5864 0.7051].png
img: 1262 evaluate_data/GlaS/E2CNN/evaluate/testB_8_126_405.pn_2_0.7059_[0.6304 0.7814].png
img: 1263 evaluate_data/GlaS/E2CNN/evaluate/testB_8_126_405.pn_3_0.5117_[0.455  0.5684].png
img: 1264 evaluate_data/GlaS/E2CNN/evaluate/testB_9_0_0.pn_0_0.2804_[0.2349 0.3258].png
img: 1265 evaluate_data/GlaS/E2CNN/evaluate/testB_9_0_0.pn_1_0.3337_[0.1639 0.5035].png
img: 1266 evaluate_data/GlaS/E2CNN/evaluate/testB_9_0_0.pn_2_0.1774_[0.2308 0.1241].png
img: 1267 evaluate_data/GlaS/E2CNN/evaluate/testB_9_0_0.pn_3_0.1412_[0.2275 0.0549].png
img: 1268 evaluate_data/GlaS/E2CNN/evaluate/testB_9_0_405.pn_0_0.5965_[0.4997 0.6934].png
img: 1269 evaluate_data/GlaS/E2CNN/evaluate/testB_9_0_405.pn_1_0.6111_[0.4911 0.7312].png
img: 1270 evaluate_data/GlaS/E2CNN/evaluate/testB_9_0_405.pn_2_0.5665_[0.4885 0.6445].png
img: 1271 evaluate_data/GlaS/E2CNN/evaluate/testB_9_0_405.pn_3_0.5169_[0.4606 0.5733].png
img: 1272 evaluate_data/GlaS/E2CNN/evaluate/testB_9_126_0.pn_0_0.168_[0.2556 0.0804].png
img: 1273 evaluate_data/GlaS/E2CNN/evaluate/testB_9_126_0.pn_1_0.4571_[0.2378 0.6764].png
img: 1274 evaluate_data/GlaS/E2CNN/evaluate/testB_9_126_0.pn_2_0.4731_[0.2909 0.6553].png
img: 1275 evaluate_data/GlaS/E2CNN/evaluate/testB_9_126_0.pn_3_0.3885_[0.2425 0.5345].png
img: 1276 evaluate_data/GlaS/E2CNN/evaluate/testB_9_126_405.pn_0_0.6987_[0.5818 0.8156].png
img: 1277 evaluate_data/GlaS/E2CNN/evaluate/testB_9_126_405.pn_1_0.672_[0.5655 0.7784].png
img: 1278 evaluate_data/GlaS/E2CNN/evaluate/testB_9_126_405.pn_2_0.6891_[0.5704 0.8077].png
img: 1279 evaluate_data/GlaS/E2CNN/evaluate/testB_9_126_405.pn_3_0.6439_[0.5436 0.7443].png
iou list:
[0.6315, 0.5774, 0.5002, 0.4784, 0.5694, 0.4772, 0.5132, 0.3056, 0.6553, 0.3715, 0.6211, 0.4757, 0.4802, 0.5819, 0.4167, 0.5337, 0.5981, 0.5415, 0.6624, 0.3796, 0.3355, 0.7829, 0.5541, 0.4657, 0.3096, 0.382, 0.3061, 0.3819, 0.3816, 0.4734, 0.5256, 0.3663, 0.6592, 0.5957, 0.5045, 0.6214, 0.5491, 0.6152, 0.5738, 0.6224, 0.6043, 0.6244, 0.663, 0.5956, 0.6446, 0.6147, 0.6242, 0.6286, 0.5204, 0.6371, 0.6828, 0.6796, 0.5868, 0.527, 0.5485, 0.5986, 0.5403, 0.6294, 0.4691, 0.5707, 0.5148, 0.6326, 0.5389, 0.5782, 0.6252, 0.5058, 0.5693, 0.6367, 0.7975, 0.5049, 0.4721, 0.747, 0.5432, 0.4852, 0.4522, 0.6393, 0.6608, 0.7533, 0.7877, 0.5679, 0.229, 0.2119, 0.6215, 0.281, 0.4417, 0.6306, 0.4158, 0.5065, 0.2088, 0.2466, 0.2174, 0.2846, 0.7138, 0.484, 0.5574, 0.4833, 0.5512, 0.5349, 0.5689, 0.5665, 0.2433, 0.2439, 0.4158, 0.2393, 0.5596, 0.3225, 0.4222, 0.5273, 0.2276, 0.2445, 0.387, 0.2855, 0.4058, 0.3194, 0.3518, 0.3591, 0.554, 0.6108, 0.6218, 0.5494, 0.3333, 0.241, 0.0977, 0.2434, 0.4802, 0.643, 0.6109, 0.5537, 0.5277, 0.6874, 0.4325, 0.4162, 0.4855, 0.5269, 0.5916, 0.5395, 0.6054, 0.4235, 0.4853, 0.4435, 0.4298, 0.6386, 0.4649, 0.4196, 0.5759, 0.2565, 0.6118, 0.6377, 0.6195, 0.6068, 0.6641, 0.4596, 0.4881, 0.646, 0.6456, 0.7033, 0.7038, 0.7106, 0.7026, 0.6907, 0.3069, 0.4055, 0.2974, 0.3176, 0.2321, 0.3318, 0.2057, 0.3302, 0.2756, 0.3976, 0.3575, 0.3997, 0.1618, 0.2165, 0.112, 0.1682, 0.3808, 0.722, 0.4758, 0.4316, 0.6027, 0.3637, 0.3373, 0.3614, 0.4282, 0.3838, 0.4111, 0.4386, 0.4918, 0.3456, 0.4628, 0.3837, 0.4224, 0.6145, 0.5617, 0.5618, 0.635, 0.6307, 0.3745, 0.6534, 0.5894, 0.4137, 0.3853, 0.6508, 0.4464, 0.3404, 0.6721, 0.3172, 0.6119, 0.4015, 0.4906, 0.4107, 0.4413, 0.6127, 0.3541, 0.464, 0.4345, 0.2246, 0.5607, 0.4502, 0.4413, 0.2972, 0.3143, 0.3943, 0.4426, 0.3701, 0.6486, 0.6624, 0.4867, 0.4511, 0.4546, 0.5007, 0.6046, 0.6819, 0.5711, 0.5024, 0.5204, 0.4152, 0.6956, 0.4414, 0.4128, 0.4887, 0.4449, 0.6272, 0.4232, 0.1353, 0.3961, 0.4332, 0.4842, 0.5776, 0.6269, 0.4636, 0.1288, 0.223, 0.2897, 0.3624, 0.3325, 0.3377, 0.3433, 0.3951, 0.6223, 0.479, 0.5316, 0.5823, 0.4476, 0.228, 0.4348, 0.4994, 0.4349, 0.6105, 0.6455, 0.3849, 0.4898, 0.3636, 0.3509, 0.6308, 0.4816, 0.5837, 0.4351, 0.3605, 0.3846, 0.3976, 0.3405, 0.3751, 0.4656, 0.6865, 0.6064, 0.3755, 0.6764, 0.4989, 0.6075, 0.6769, 0.4951, 0.6888, 0.6435, 0.7107, 0.6017, 0.627, 0.492, 0.6467, 0.6507, 0.5729, 0.6964, 0.7097, 0.4347, 0.3966, 0.4025, 0.371, 0.6301, 0.433, 0.583, 0.6917, 0.6006, 0.4242, 0.5043, 0.5815, 0.6386, 0.6038, 0.4489, 0.6408, 0.4555, 0.594, 0.4827, 0.5466, 0.671, 0.7405, 0.7323, 0.3361, 0.5272, 0.5847, 0.4848, 0.5816, 0.6012, 0.3158, 0.7008, 0.4869, 0.6187, 0.5406, 0.7798, 0.5372, 0.6702, 0.4234, 0.5475, 0.671, 0.7623, 0.5404, 0.7382, 0.7468, 0.4935, 0.6668, 0.4616, 0.6057, 0.5743, 0.7076, 0.5959, 0.6337, 0.6642, 0.6609, 0.7396, 0.6572, 0.6505, 0.6619, 0.6136, 0.6126, 0.7467, 0.7613, 0.6171, 0.7479, 0.7263, 0.6643, 0.6074, 0.7128, 0.5323, 0.7783, 0.5893, 0.5077, 0.4898, 0.3691, 0.7535, 0.7784, 0.6954, 0.5929, 0.7407, 0.3889, 0.4543, 0.3676, 0.4603, 0.3602, 0.4397, 0.3041, 0.5345, 0.4109, 0.5646, 0.5353, 0.4057, 0.4818, 0.4891, 0.3656, 0.4789, 0.3923, 0.4297, 0.4215, 0.3554, 0.5569, 0.6621, 0.5222, 0.5758, 0.4785, 0.56, 0.5147, 0.6242, 0.6261, 0.5292, 0.6931, 0.6104, 0.4475, 0.3979, 0.3358, 0.4233, 0.4727, 0.3898, 0.6452, 0.3427, 0.541, 0.4117, 0.3667, 0.5907, 0.631, 0.3552, 0.2094, 0.3646, 0.3608, 0.6027, 0.5074, 0.5279, 0.4697, 0.6074, 0.6728, 0.5621, 0.4711, 0.662, 0.4478, 0.4732, 0.6389, 0.6744, 0.5753, 0.4508, 0.6201, 0.678, 0.7158, 0.4424, 0.5559, 0.6867, 0.6702, 0.5895, 0.6838, 0.4937, 0.5097, 0.6712, 0.6555, 0.7212, 0.6532, 0.5793, 0.673, 0.6849, 0.6273, 0.3706, 0.5669, 0.1988, 0.1987, 0.3261, 0.1791, 0.6976, 0.7044, 0.4249, 0.6992, 0.2112, 0.1649, 0.1924, 0.2172, 0.7825, 0.753, 0.6595, 0.7974, 0.3944, 0.3578, 0.3311, 0.4061, 0.4731, 0.6307, 0.6416, 0.5549, 0.3682, 0.3591, 0.324, 0.4221, 0.2536, 0.3569, 0.3134, 0.3489, 0.6444, 0.5506, 0.6327, 0.2993, 0.3219, 0.3783, 0.3291, 0.3805, 0.7161, 0.7475, 0.728, 0.7051, 0.4063, 0.3905, 0.3488, 0.3297, 0.4318, 0.4585, 0.7611, 0.4191, 0.3742, 0.3672, 0.3717, 0.2945, 0.8001, 0.768, 0.7074, 0.7812, 0.5813, 0.537, 0.6267, 0.7045, 0.3931, 0.6282, 0.6641, 0.3552, 0.6229, 0.614, 0.5853, 0.6369, 0.6447, 0.3666, 0.5801, 0.6748, 0.7233, 0.6408, 0.6822, 0.6517, 0.3634, 0.4413, 0.5839, 0.3041, 0.7257, 0.5043, 0.7858, 0.6846, 0.7705, 0.6406, 0.4908, 0.7173, 0.4838, 0.5816, 0.418, 0.4794, 0.7793, 0.778, 0.62, 0.6084, 0.5356, 0.4288, 0.3422, 0.3907, 0.4771, 0.5845, 0.4447, 0.4446, 0.6436, 0.6659, 0.6153, 0.5808, 0.6724, 0.6265, 0.5767, 0.6224, 0.6872, 0.6571, 0.6808, 0.6728, 0.7048, 0.6628, 0.5828, 0.6399, 0.4309, 0.4975, 0.4569, 0.3427, 0.577, 0.5476, 0.5999, 0.5501, 0.4673, 0.3952, 0.4448, 0.4294, 0.5439, 0.6572, 0.629, 0.5138, 0.5907, 0.5136, 0.3694, 0.56, 0.4535, 0.58, 0.5446, 0.5884, 0.2934, 0.5462, 0.6127, 0.5043, 0.5379, 0.559, 0.5589, 0.5036, 0.3606, 0.4309, 0.4007, 0.3626, 0.664, 0.5697, 0.6755, 0.5897, 0.5048, 0.3767, 0.5863, 0.3593, 0.6303, 0.6968, 0.6661, 0.6548, 0.5859, 0.5826, 0.3169, 0.6344, 0.5386, 0.555, 0.5198, 0.5969, 0.4115, 0.5075, 0.6305, 0.6346, 0.3715, 0.6551, 0.3568, 0.5341, 0.4272, 0.4757, 0.5025, 0.4471, 0.3111, 0.3106, 0.4407, 0.2833, 0.2702, 0.2353, 0.2909, 0.3294, 0.528, 0.3768, 0.3909, 0.4264, 0.5974, 0.3564, 0.4627, 0.3694, 0.6971, 0.6855, 0.4876, 0.6812, 0.3314, 0.3288, 0.3241, 0.372, 0.5944, 0.6589, 0.5876, 0.6057, 0.7643, 0.5269, 0.546, 0.5726, 0.4877, 0.3658, 0.392, 0.289, 0.8158, 0.5602, 0.5093, 0.6141, 0.3921, 0.2933, 0.3941, 0.3927, 0.6387, 0.5535, 0.6216, 0.5023, 0.6357, 0.5528, 0.6804, 0.4864, 0.634, 0.5348, 0.5319, 0.6434, 0.5968, 0.6196, 0.658, 0.574, 0.4623, 0.5739, 0.4136, 0.5419, 0.4475, 0.7533, 0.6659, 0.7743, 0.6005, 0.6238, 0.5477, 0.6872, 0.7112, 0.4673, 0.4364, 0.45, 0.6731, 0.6706, 0.5923, 0.6887, 0.7632, 0.6314, 0.7504, 0.6439, 0.6559, 0.674, 0.7061, 0.5511, 0.4289, 0.7437, 0.7551, 0.7461, 0.5743, 0.3755, 0.7797, 0.2414, 0.466, 0.3796, 0.6475, 0.3782, 0.234, 0.319, 0.2515, 0.431, 0.508, 0.3867, 0.4966, 0.4853, 0.4454, 0.4979, 0.4966, 0.4278, 0.6774, 0.6954, 0.646, 0.6666, 0.6259, 0.542, 0.629, 0.6171, 0.4572, 0.5604, 0.5281, 0.534, 0.4747, 0.5662, 0.4287, 0.4596, 0.316, 0.3617, 0.3186, 0.1366, 0.6915, 0.722, 0.6185, 0.69, 0.3379, 0.2885, 0.4013, 0.3343, 0.3844, 0.4004, 0.6068, 0.4691, 0.3121, 0.3254, 0.4018, 0.3436, 0.4096, 0.734, 0.6009, 0.6966, 0.4751, 0.5472, 0.4137, 0.4069, 0.3017, 0.3569, 0.3615, 0.3412, 0.3365, 0.3757, 0.3559, 0.3076, 0.2569, 0.289, 0.26, 0.2781, 0.3935, 0.4356, 0.2484, 0.4632, 0.3834, 0.3005, 0.3387, 0.3428, 0.6536, 0.7032, 0.6119, 0.4214, 0.4757, 0.5806, 0.2936, 0.2812, 0.7145, 0.7094, 0.6723, 0.7044, 0.4451, 0.4129, 0.5039, 0.3766, 0.4269, 0.4615, 0.5035, 0.494, 0.4437, 0.4475, 0.3011, 0.4089, 0.5807, 0.457, 0.3241, 0.6038, 0.5695, 0.3028, 0.4679, 0.6743, 0.6504, 0.4522, 0.463, 0.4205, 0.5955, 0.4661, 0.5571, 0.4042, 0.6542, 0.6073, 0.3058, 0.6398, 0.6782, 0.6917, 0.7277, 0.5546, 0.6086, 0.5779, 0.6771, 0.726, 0.6322, 0.6609, 0.6222, 0.6518, 0.633, 0.6036, 0.768, 0.5504, 0.4411, 0.3246, 0.2277, 0.4998, 0.4713, 0.4969, 0.6189, 0.4762, 0.2251, 0.3662, 0.4079, 0.2364, 0.4522, 0.6094, 0.4634, 0.7495, 0.428, 0.3386, 0.4444, 0.4168, 0.2615, 0.5223, 0.3852, 0.3991, 0.3158, 0.3594, 0.2991, 0.315, 0.5002, 0.6598, 0.6593, 0.4954, 0.6685, 0.5198, 0.5914, 0.6669, 0.6151, 0.5188, 0.6744, 0.5021, 0.5182, 0.5859, 0.5317, 0.3189, 0.3406, 0.5252, 0.548, 0.6491, 0.3206, 0.6415, 0.3049, 0.581, 0.4812, 0.4631, 0.332, 0.3946, 0.4959, 0.4151, 0.5086, 0.2931, 0.4829, 0.4957, 0.3871, 0.4577, 0.3062, 0.3485, 0.3485, 0.3611, 0.3157, 0.2753, 0.3304, 0.2959, 0.3957, 0.4057, 0.2978, 0.3636, 0.3758, 0.4415, 0.382, 0.5704, 0.6586, 0.7057, 0.7266, 0.6017, 0.6381, 0.7064, 0.7285, 0.6832, 0.3006, 0.5121, 0.4294, 0.4176, 0.6222, 0.6347, 0.73, 0.7199, 0.4731, 0.4694, 0.4684, 0.4248, 0.5207, 0.1595, 0.3561, 0.4332, 0.5552, 0.3832, 0.4387, 0.498, 0.4748, 0.4807, 0.473, 0.4732, 0.6566, 0.4187, 0.4693, 0.4109, 0.4912, 0.4873, 0.3875, 0.4962, 0.676, 0.4136, 0.3828, 0.2892, 0.5281, 0.3766, 0.6759, 0.6018, 0.4474, 0.3771, 0.4677, 0.3274, 0.22, 0.2247, 0.1579, 0.1941, 0.3015, 0.3298, 0.5961, 0.464, 0.3035, 0.2375, 0.2184, 0.1699, 0.5648, 0.4262, 0.3677, 0.5638, 0.557, 0.4675, 0.5239, 0.4382, 0.3729, 0.4095, 0.3558, 0.4295, 0.5184, 0.5442, 0.4343, 0.4788, 0.4384, 0.5109, 0.1665, 0.4133, 0.2423, 0.492, 0.1768, 0.3308, 0.4097, 0.4424, 0.258, 0.4191, 0.3285, 0.3846, 0.4279, 0.3026, 0.37, 0.2662, 0.2358, 0.2827, 0.2109, 0.1645, 0.1238, 0.196, 0.4095, 0.444, 0.2749, 0.489, 0.0117, 0.1943, 0.0863, 0.0801, 0.5796, 0.5104, 0.6222, 0.5744, 0.5502, 0.4074, 0.3732, 0.6032, 0.739, 0.5117, 0.6537, 0.735, 0.6734, 0.6122, 0.5784, 0.6093, 0.6036, 0.635, 0.6374, 0.5877, 0.3781, 0.3608, 0.4816, 0.5588, 0.6027, 0.5733, 0.6681, 0.6498, 0.4996, 0.6347, 0.5308, 0.6349, 0.3135, 0.2665, 0.2713, 0.203, 0.6197, 0.547, 0.6641, 0.5196, 0.2253, 0.2616, 0.385, 0.2733, 0.6748, 0.693, 0.3704, 0.5404, 0.5048, 0.6019, 0.2283, 0.2429, 0.5588, 0.3655, 0.3018, 0.2793, 0.3948, 0.3276, 0.2547, 0.2664, 0.3068, 0.5252, 0.3523, 0.4798, 0.6878, 0.451, 0.6128, 0.4786, 0.4022, 0.5947, 0.5263, 0.392, 0.611, 0.5812, 0.5073, 0.534, 0.5273, 0.5884, 0.6741, 0.5667, 0.4995, 0.3972, 0.6989, 0.5084, 0.5801, 0.4212, 0.4165, 0.552, 0.6119, 0.3513, 0.5681, 0.4176, 0.6991, 0.4818, 0.4834, 0.6286, 0.5461, 0.388, 0.3535, 0.3687, 0.2019, 0.1131, 0.2648, 0.2763, 0.3228, 0.4896, 0.2372, 0.2621, 0.0603, 0.2698, 0.2265, 0.1727, 0.7415, 0.6606, 0.3751, 0.7873, 0.3995, 0.4966, 0.4111, 0.3695, 0.4123, 0.7513, 0.5998, 0.701, 0.3086, 0.421, 0.3259, 0.632, 0.4646, 0.4073, 0.2484, 0.418, 0.4229, 0.3853, 0.3823, 0.3822, 0.3819, 0.3719, 0.5698, 0.563, 0.3706, 0.3808, 0.3375, 0.3371, 0.2277, 0.6905, 0.2807, 0.2335, 0.2763, 0.2682, 0.3527, 0.258, 0.6789, 0.23, 0.2165, 0.2244, 0.3689, 0.2664, 0.6267, 0.1824, 0.2413, 0.3247, 0.2858, 0.2828, 0.6213, 0.4593, 0.5237, 0.4052, 0.2787, 0.2341, 0.2172, 0.2459, 0.6101, 0.6458, 0.7059, 0.5117, 0.2804, 0.3337, 0.1774, 0.1412, 0.5965, 0.6111, 0.5665, 0.5169, 0.168, 0.4571, 0.4731, 0.3885, 0.6987, 0.672, 0.6891, 0.6439]
2022-12-26 21:07:24.143298, iou: tensor([0.4221, 0.5360], device='cuda:0'), 0.4791
==============================================================================
Running epilogue script on alpha51.

Submit time  : 2022-12-26T18:05:54
Start time   : 2022-12-26T18:05:54
End time     : 2022-12-26T21:07:27
Elapsed time : 03:01:33 (Timelimit=1-00:00:00)

Job ID: 2349363
Cluster: i5
User/Group: yy3u19/fp
State: COMPLETED (exit code 0)
Nodes: 1
Cores per node: 4
CPU Utilized: 03:02:52
CPU Efficiency: 25.18% of 12:06:12 core-walltime
Job Wall-clock time: 03:01:33
Memory Utilized: 12.31 GB
Memory Efficiency: 58.36% of 21.09 GB

