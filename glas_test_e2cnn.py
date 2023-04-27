Running SLURM prolog script on alpha51.cluster.local
===============================================================================
Job started on Mon Dec 26 18:05:36 GMT 2022
Job ID          : 2349362
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
---------- kernel_size: 3 ---------- classes: 2 ---------- model: E2CNN ---------- rotations: 8 ---------- dataset: GlaS - test ----------
num of trainable parameters:7033922
Loading model checkpoints/GlaS/lr_0.002_bn_16_epoch_70_E2CNN_Ksize_3_rotation_8.pth num of rotations of filters: 8
Using device cuda
----------------------------------------------------------------------------------------------------------------------------------------------------------------
Num of images for evaulation: 320
img: 0 evaluate_data/GlaS/E2CNN/test/testA_10_0_0_0.8384_[0.8258 0.8509].png
img: 1 evaluate_data/GlaS/E2CNN/test/testA_10_0_405_0.8094_[0.8283 0.7906].png
img: 2 evaluate_data/GlaS/E2CNN/test/testA_10_126_0_0.771_[0.7633 0.7787].png
img: 3 evaluate_data/GlaS/E2CNN/test/testA_10_126_405_0.8043_[0.8315 0.7771].png
img: 4 evaluate_data/GlaS/E2CNN/test/testA_11_0_0_0.5817_[0.8599 0.3036].png
img: 5 evaluate_data/GlaS/E2CNN/test/testA_11_0_405_0.7271_[0.8992 0.5549].png
img: 6 evaluate_data/GlaS/E2CNN/test/testA_11_126_0_0.4858_[0.9716 0.    ].png
img: 7 evaluate_data/GlaS/E2CNN/test/testA_11_126_405_0.8262_[0.9654 0.6871].png
img: 8 evaluate_data/GlaS/E2CNN/test/testA_12_0_0_0.4781_[0.4614 0.4949].png
img: 9 evaluate_data/GlaS/E2CNN/test/testA_12_0_405_0.7963_[0.8157 0.7769].png
img: 10 evaluate_data/GlaS/E2CNN/test/testA_12_126_0_0.512_[0.5169 0.5071].png
img: 11 evaluate_data/GlaS/E2CNN/test/testA_12_126_405_0.749_[0.7662 0.7317].png
img: 12 evaluate_data/GlaS/E2CNN/test/testA_13_0_0_0.8404_[0.927  0.7538].png
img: 13 evaluate_data/GlaS/E2CNN/test/testA_13_0_405_0.782_[0.7785 0.7854].png
img: 14 evaluate_data/GlaS/E2CNN/test/testA_13_126_0_0.8665_[0.9412 0.7917].png
img: 15 evaluate_data/GlaS/E2CNN/test/testA_13_126_405_0.8488_[0.8522 0.8455].png
img: 16 evaluate_data/GlaS/E2CNN/test/testA_14_0_0_0.5434_[0.7386 0.3482].png
img: 17 evaluate_data/GlaS/E2CNN/test/testA_14_0_405_0.9239_[0.9713 0.8765].png
img: 18 evaluate_data/GlaS/E2CNN/test/testA_14_126_0_0.5358_[0.7232 0.3485].png
img: 19 evaluate_data/GlaS/E2CNN/test/testA_14_126_405_0.9222_[0.9708 0.8736].png
img: 20 evaluate_data/GlaS/E2CNN/test/testA_15_0_0_0.5682_[0.8466 0.2898].png
img: 21 evaluate_data/GlaS/E2CNN/test/testA_15_0_405_0.883_[0.8531 0.9129].png
img: 22 evaluate_data/GlaS/E2CNN/test/testA_15_126_0_0.524_[0.841 0.207].png
img: 23 evaluate_data/GlaS/E2CNN/test/testA_15_126_405_0.9163_[0.9045 0.9281].png
img: 24 evaluate_data/GlaS/E2CNN/test/testA_16_0_0_0.8034_[0.7894 0.8175].png
img: 25 evaluate_data/GlaS/E2CNN/test/testA_16_0_191_0.8684_[0.862  0.8748].png
img: 26 evaluate_data/GlaS/E2CNN/test/testA_16_38_0_0.7892_[0.7778 0.8005].png
img: 27 evaluate_data/GlaS/E2CNN/test/testA_16_38_191_0.8266_[0.8402 0.8129].png
img: 28 evaluate_data/GlaS/E2CNN/test/testA_17_0_0_0.2967_[0.5934 0.    ].png
img: 29 evaluate_data/GlaS/E2CNN/test/testA_17_0_405_0.8156_[0.8344 0.7969].png
img: 30 evaluate_data/GlaS/E2CNN/test/testA_17_126_0_0.3761_[0.7521 0.    ].png
img: 31 evaluate_data/GlaS/E2CNN/test/testA_17_126_405_0.8205_[0.8206 0.8204].png
img: 32 evaluate_data/GlaS/E2CNN/test/testA_18_0_0_0.7396_[0.8647 0.6145].png
img: 33 evaluate_data/GlaS/E2CNN/test/testA_18_0_405_0.8541_[0.873  0.8353].png
img: 34 evaluate_data/GlaS/E2CNN/test/testA_18_126_0_0.6876_[0.7796 0.5957].png
img: 35 evaluate_data/GlaS/E2CNN/test/testA_18_126_405_0.8727_[0.855  0.8904].png
img: 36 evaluate_data/GlaS/E2CNN/test/testA_19_0_0_0.8285_[0.822  0.8349].png
img: 37 evaluate_data/GlaS/E2CNN/test/testA_19_0_405_0.8185_[0.8173 0.8198].png
img: 38 evaluate_data/GlaS/E2CNN/test/testA_19_126_0_0.8634_[0.8642 0.8626].png
img: 39 evaluate_data/GlaS/E2CNN/test/testA_19_126_405_0.8099_[0.7918 0.8281].png
img: 40 evaluate_data/GlaS/E2CNN/test/testA_1_0_0_0.6206_[0.4457 0.7955].png
img: 41 evaluate_data/GlaS/E2CNN/test/testA_1_0_405_0.3943_[0.1824 0.6062].png
img: 42 evaluate_data/GlaS/E2CNN/test/testA_1_126_0_0.7895_[0.688  0.8911].png
img: 43 evaluate_data/GlaS/E2CNN/test/testA_1_126_405_0.3209_[0.1296 0.5122].png
img: 44 evaluate_data/GlaS/E2CNN/test/testA_20_0_0_0.4256_[0.5987 0.2525].png
img: 45 evaluate_data/GlaS/E2CNN/test/testA_20_0_405_0.5827_[0.5293 0.636 ].png
img: 46 evaluate_data/GlaS/E2CNN/test/testA_20_126_0_0.3744_[0.5909 0.1579].png
img: 47 evaluate_data/GlaS/E2CNN/test/testA_20_126_405_0.5481_[0.6454 0.4508].png
img: 48 evaluate_data/GlaS/E2CNN/test/testA_21_0_0_0.7424_[0.7803 0.7044].png
img: 49 evaluate_data/GlaS/E2CNN/test/testA_21_0_405_0.8137_[0.8558 0.7716].png
img: 50 evaluate_data/GlaS/E2CNN/test/testA_21_126_0_0.8765_[0.8709 0.8821].png
img: 51 evaluate_data/GlaS/E2CNN/test/testA_21_126_405_0.8932_[0.8944 0.8921].png
img: 52 evaluate_data/GlaS/E2CNN/test/testA_22_0_0_0.65_[0.6919 0.608 ].png
img: 53 evaluate_data/GlaS/E2CNN/test/testA_22_0_405_0.588_[0.585 0.591].png
img: 54 evaluate_data/GlaS/E2CNN/test/testA_22_126_0_0.6395_[0.7317 0.5472].png
img: 55 evaluate_data/GlaS/E2CNN/test/testA_22_126_405_0.5333_[0.5744 0.4923].png
img: 56 evaluate_data/GlaS/E2CNN/test/testA_23_0_0_0.3105_[0.6209 0.    ].png
img: 57 evaluate_data/GlaS/E2CNN/test/testA_23_0_405_0.6664_[0.6942 0.6386].png
img: 58 evaluate_data/GlaS/E2CNN/test/testA_23_126_0_0.2666_[0.495  0.0381].png
img: 59 evaluate_data/GlaS/E2CNN/test/testA_23_126_405_0.8688_[0.863  0.8746].png
img: 60 evaluate_data/GlaS/E2CNN/test/testA_24_0_0_0.6972_[0.8108 0.5836].png
img: 61 evaluate_data/GlaS/E2CNN/test/testA_24_0_405_0.7239_[0.7131 0.7348].png
img: 62 evaluate_data/GlaS/E2CNN/test/testA_24_126_0_0.8268_[0.8833 0.7703].png
img: 63 evaluate_data/GlaS/E2CNN/test/testA_24_126_405_0.7291_[0.6976 0.7607].png
img: 64 evaluate_data/GlaS/E2CNN/test/testA_25_0_0_0.6228_[0.546  0.6996].png
img: 65 evaluate_data/GlaS/E2CNN/test/testA_25_0_405_0.8129_[0.8114 0.8144].png
img: 66 evaluate_data/GlaS/E2CNN/test/testA_25_126_0_0.7136_[0.6177 0.8095].png
img: 67 evaluate_data/GlaS/E2CNN/test/testA_25_126_405_0.8683_[0.8526 0.884 ].png
img: 68 evaluate_data/GlaS/E2CNN/test/testA_26_0_0_0.4531_[0.9012 0.0049].png
img: 69 evaluate_data/GlaS/E2CNN/test/testA_26_0_405_0.8801_[0.9086 0.8515].png
img: 70 evaluate_data/GlaS/E2CNN/test/testA_26_126_0_0.4736_[0.9471 0.    ].png
img: 71 evaluate_data/GlaS/E2CNN/test/testA_26_126_405_0.8747_[0.9126 0.8369].png
img: 72 evaluate_data/GlaS/E2CNN/test/testA_27_0_0_0.8678_[0.8455 0.89  ].png
img: 73 evaluate_data/GlaS/E2CNN/test/testA_27_0_405_0.8414_[0.8386 0.8441].png
img: 74 evaluate_data/GlaS/E2CNN/test/testA_27_126_0_0.7946_[0.7824 0.8068].png
img: 75 evaluate_data/GlaS/E2CNN/test/testA_27_126_405_0.8417_[0.8443 0.8391].png
img: 76 evaluate_data/GlaS/E2CNN/test/testA_28_0_0_0.4535_[0.4737 0.4333].png
img: 77 evaluate_data/GlaS/E2CNN/test/testA_28_0_405_0.85_[0.8447 0.8553].png
img: 78 evaluate_data/GlaS/E2CNN/test/testA_28_126_0_0.6282_[0.6323 0.6242].png
img: 79 evaluate_data/GlaS/E2CNN/test/testA_28_126_405_0.859_[0.8564 0.8616].png
img: 80 evaluate_data/GlaS/E2CNN/test/testA_29_0_0_0.6193_[0.7128 0.5258].png
img: 81 evaluate_data/GlaS/E2CNN/test/testA_29_0_405_0.9135_[0.9281 0.8989].png
img: 82 evaluate_data/GlaS/E2CNN/test/testA_29_126_0_0.833_[0.8951 0.771 ].png
img: 83 evaluate_data/GlaS/E2CNN/test/testA_29_126_405_0.9342_[0.946  0.9224].png
img: 84 evaluate_data/GlaS/E2CNN/test/testA_2_0_0_0.5063_[0.7052 0.3073].png
img: 85 evaluate_data/GlaS/E2CNN/test/testA_2_0_200_0.6846_[0.8345 0.5346].png
img: 86 evaluate_data/GlaS/E2CNN/test/testA_2_50_0_0.4814_[0.6761 0.2868].png
img: 87 evaluate_data/GlaS/E2CNN/test/testA_2_50_200_0.714_[0.864 0.564].png
img: 88 evaluate_data/GlaS/E2CNN/test/testA_30_0_0_0.873_[0.8362 0.9098].png
img: 89 evaluate_data/GlaS/E2CNN/test/testA_30_0_405_0.924_[0.9305 0.9176].png
img: 90 evaluate_data/GlaS/E2CNN/test/testA_30_126_0_0.874_[0.8415 0.9065].png
img: 91 evaluate_data/GlaS/E2CNN/test/testA_30_126_405_0.8821_[0.9016 0.8625].png
img: 92 evaluate_data/GlaS/E2CNN/test/testA_31_0_0_0.71_[0.9191 0.5008].png
img: 93 evaluate_data/GlaS/E2CNN/test/testA_31_0_405_0.9446_[0.9628 0.9263].png
img: 94 evaluate_data/GlaS/E2CNN/test/testA_31_126_0_0.6209_[0.7818 0.4601].png
img: 95 evaluate_data/GlaS/E2CNN/test/testA_31_126_405_0.9411_[0.9352 0.947 ].png
img: 96 evaluate_data/GlaS/E2CNN/test/testA_32_0_0_0.7273_[0.8044 0.6502].png
img: 97 evaluate_data/GlaS/E2CNN/test/testA_32_0_405_0.6293_[0.78   0.4785].png
img: 98 evaluate_data/GlaS/E2CNN/test/testA_32_126_0_0.7696_[0.8312 0.7081].png
img: 99 evaluate_data/GlaS/E2CNN/test/testA_32_126_405_0.7234_[0.8771 0.5697].png
img: 100 evaluate_data/GlaS/E2CNN/test/testA_33_0_0_0.7528_[0.6991 0.8065].png
img: 101 evaluate_data/GlaS/E2CNN/test/testA_33_0_405_0.9019_[0.8766 0.9271].png
img: 102 evaluate_data/GlaS/E2CNN/test/testA_33_126_0_0.7974_[0.7541 0.8407].png
img: 103 evaluate_data/GlaS/E2CNN/test/testA_33_126_405_0.903_[0.9023 0.9037].png
img: 104 evaluate_data/GlaS/E2CNN/test/testA_34_0_0_0.7758_[0.8416 0.7099].png
img: 105 evaluate_data/GlaS/E2CNN/test/testA_34_0_405_0.3616_[0.4547 0.2686].png
img: 106 evaluate_data/GlaS/E2CNN/test/testA_34_126_0_0.8025_[0.8126 0.7923].png
img: 107 evaluate_data/GlaS/E2CNN/test/testA_34_126_405_0.586_[0.6448 0.5273].png
img: 108 evaluate_data/GlaS/E2CNN/test/testA_35_0_0_0.8614_[0.8047 0.9181].png
img: 109 evaluate_data/GlaS/E2CNN/test/testA_35_0_200_0.8975_[0.8615 0.9335].png
img: 110 evaluate_data/GlaS/E2CNN/test/testA_35_50_0_0.8846_[0.8356 0.9336].png
img: 111 evaluate_data/GlaS/E2CNN/test/testA_35_50_200_0.8973_[0.862  0.9326].png
img: 112 evaluate_data/GlaS/E2CNN/test/testA_36_0_0_0.561_[0.512 0.61 ].png
img: 113 evaluate_data/GlaS/E2CNN/test/testA_36_0_405_0.8889_[0.8663 0.9116].png
img: 114 evaluate_data/GlaS/E2CNN/test/testA_36_126_0_0.7459_[0.6852 0.8066].png
img: 115 evaluate_data/GlaS/E2CNN/test/testA_36_126_405_0.8996_[0.896  0.9032].png
img: 116 evaluate_data/GlaS/E2CNN/test/testA_37_0_0_0.8149_[0.8083 0.8216].png
img: 117 evaluate_data/GlaS/E2CNN/test/testA_37_0_405_0.3212_[0.2773 0.365 ].png
img: 118 evaluate_data/GlaS/E2CNN/test/testA_37_126_0_0.802_[0.7774 0.8266].png
img: 119 evaluate_data/GlaS/E2CNN/test/testA_37_126_405_0.1593_[0.1461 0.1724].png
img: 120 evaluate_data/GlaS/E2CNN/test/testA_38_0_0_0.3572_[0.7144 0.    ].png
img: 121 evaluate_data/GlaS/E2CNN/test/testA_38_0_405_0.4912_[0.9824 0.    ].png
img: 122 evaluate_data/GlaS/E2CNN/test/testA_38_126_0_0.468_[0.936 0.   ].png
img: 123 evaluate_data/GlaS/E2CNN/test/testA_38_126_405_0.4922_[0.9844 0.    ].png
img: 124 evaluate_data/GlaS/E2CNN/test/testA_39_0_0_0.4905_[0.9811 0.    ].png
img: 125 evaluate_data/GlaS/E2CNN/test/testA_39_0_405_0.7194_[0.8192 0.6197].png
img: 126 evaluate_data/GlaS/E2CNN/test/testA_39_126_0_0.4944_[0.9888 0.    ].png
img: 127 evaluate_data/GlaS/E2CNN/test/testA_39_126_405_0.8659_[0.9391 0.7928].png
img: 128 evaluate_data/GlaS/E2CNN/test/testA_3_0_0_0.7357_[0.6737 0.7978].png
img: 129 evaluate_data/GlaS/E2CNN/test/testA_3_0_191_0.8784_[0.9088 0.848 ].png
img: 130 evaluate_data/GlaS/E2CNN/test/testA_3_38_0_0.7637_[0.6852 0.8423].png
img: 131 evaluate_data/GlaS/E2CNN/test/testA_3_38_191_0.893_[0.9125 0.8735].png
img: 132 evaluate_data/GlaS/E2CNN/test/testA_40_0_0_0.7415_[0.7728 0.7101].png
img: 133 evaluate_data/GlaS/E2CNN/test/testA_40_0_405_0.8665_[0.8493 0.8838].png
img: 134 evaluate_data/GlaS/E2CNN/test/testA_40_126_0_0.7246_[0.7562 0.693 ].png
img: 135 evaluate_data/GlaS/E2CNN/test/testA_40_126_405_0.8453_[0.8246 0.866 ].png
img: 136 evaluate_data/GlaS/E2CNN/test/testA_41_0_0_0.6944_[0.8666 0.5222].png
img: 137 evaluate_data/GlaS/E2CNN/test/testA_41_0_405_0.6306_[0.8454 0.4157].png
img: 138 evaluate_data/GlaS/E2CNN/test/testA_41_126_0_0.6298_[0.9131 0.3465].png
img: 139 evaluate_data/GlaS/E2CNN/test/testA_41_126_405_0.7573_[0.9203 0.5942].png
img: 140 evaluate_data/GlaS/E2CNN/test/testA_42_0_0_0.5266_[0.6492 0.404 ].png
img: 141 evaluate_data/GlaS/E2CNN/test/testA_42_0_405_0.8151_[0.8565 0.7737].png
img: 142 evaluate_data/GlaS/E2CNN/test/testA_42_126_0_0.451_[0.5547 0.3473].png
img: 143 evaluate_data/GlaS/E2CNN/test/testA_42_126_405_0.8327_[0.8769 0.7885].png
img: 144 evaluate_data/GlaS/E2CNN/test/testA_43_0_0_0.8636_[0.8352 0.8921].png
img: 145 evaluate_data/GlaS/E2CNN/test/testA_43_0_200_0.8835_[0.8494 0.9176].png
img: 146 evaluate_data/GlaS/E2CNN/test/testA_43_50_0_0.8782_[0.861  0.8954].png
img: 147 evaluate_data/GlaS/E2CNN/test/testA_43_50_200_0.871_[0.841  0.9011].png
img: 148 evaluate_data/GlaS/E2CNN/test/testA_44_0_0_0.6486_[0.6324 0.6647].png
img: 149 evaluate_data/GlaS/E2CNN/test/testA_44_0_200_0.8139_[0.7826 0.8451].png
img: 150 evaluate_data/GlaS/E2CNN/test/testA_44_50_0_0.582_[0.5319 0.6322].png
img: 151 evaluate_data/GlaS/E2CNN/test/testA_44_50_200_0.7904_[0.738  0.8429].png
img: 152 evaluate_data/GlaS/E2CNN/test/testA_45_0_0_0.8575_[0.8513 0.8637].png
img: 153 evaluate_data/GlaS/E2CNN/test/testA_45_0_188_0.8744_[0.8425 0.9064].png
img: 154 evaluate_data/GlaS/E2CNN/test/testA_45_28_0_0.9068_[0.8985 0.9151].png
img: 155 evaluate_data/GlaS/E2CNN/test/testA_45_28_188_0.8902_[0.8631 0.9174].png
img: 156 evaluate_data/GlaS/E2CNN/test/testA_46_0_0_0.6623_[0.5586 0.7659].png
img: 157 evaluate_data/GlaS/E2CNN/test/testA_46_0_405_0.9023_[0.8781 0.9265].png
img: 158 evaluate_data/GlaS/E2CNN/test/testA_46_126_0_0.8054_[0.7098 0.9011].png
img: 159 evaluate_data/GlaS/E2CNN/test/testA_46_126_405_0.9021_[0.8795 0.9246].png
img: 160 evaluate_data/GlaS/E2CNN/test/testA_47_0_0_0.723_[0.8307 0.6153].png
img: 161 evaluate_data/GlaS/E2CNN/test/testA_47_0_405_0.9394_[0.9485 0.9302].png
img: 162 evaluate_data/GlaS/E2CNN/test/testA_47_126_0_0.7961_[0.8303 0.7619].png
img: 163 evaluate_data/GlaS/E2CNN/test/testA_47_126_405_0.8989_[0.9277 0.8701].png
img: 164 evaluate_data/GlaS/E2CNN/test/testA_48_0_0_0.7777_[0.6886 0.8668].png
img: 165 evaluate_data/GlaS/E2CNN/test/testA_48_0_405_0.7909_[0.7147 0.8671].png
img: 166 evaluate_data/GlaS/E2CNN/test/testA_48_126_0_0.7807_[0.6872 0.8742].png
img: 167 evaluate_data/GlaS/E2CNN/test/testA_48_126_405_0.7952_[0.7521 0.8382].png
img: 168 evaluate_data/GlaS/E2CNN/test/testA_49_0_0_0.4527_[0.9054 0.    ].png
img: 169 evaluate_data/GlaS/E2CNN/test/testA_49_0_405_0.608_[0.5969 0.6191].png
img: 170 evaluate_data/GlaS/E2CNN/test/testA_49_126_0_0.5534_[0.9295 0.1774].png
img: 171 evaluate_data/GlaS/E2CNN/test/testA_49_126_405_0.6959_[0.7033 0.6886].png
img: 172 evaluate_data/GlaS/E2CNN/test/testA_4_0_0_0.5917_[0.7152 0.4681].png
img: 173 evaluate_data/GlaS/E2CNN/test/testA_4_0_405_0.8522_[0.9635 0.741 ].png
img: 174 evaluate_data/GlaS/E2CNN/test/testA_4_126_0_0.5176_[0.8253 0.2099].png
img: 175 evaluate_data/GlaS/E2CNN/test/testA_4_126_405_0.7277_[0.9783 0.4771].png
img: 176 evaluate_data/GlaS/E2CNN/test/testA_50_0_0_0.8352_[0.801  0.8694].png
img: 177 evaluate_data/GlaS/E2CNN/test/testA_50_0_183_0.9125_[0.8934 0.9315].png
img: 178 evaluate_data/GlaS/E2CNN/test/testA_50_28_0_0.8521_[0.8149 0.8893].png
img: 179 evaluate_data/GlaS/E2CNN/test/testA_50_28_183_0.9062_[0.8861 0.9263].png
img: 180 evaluate_data/GlaS/E2CNN/test/testA_51_0_0_0.4206_[0.6906 0.1506].png
img: 181 evaluate_data/GlaS/E2CNN/test/testA_51_0_405_0.8543_[0.9171 0.7915].png
img: 182 evaluate_data/GlaS/E2CNN/test/testA_51_126_0_0.5407_[0.6376 0.4438].png
img: 183 evaluate_data/GlaS/E2CNN/test/testA_51_126_405_0.9247_[0.9326 0.9168].png
img: 184 evaluate_data/GlaS/E2CNN/test/testA_52_0_0_0.8787_[0.8585 0.8989].png
img: 185 evaluate_data/GlaS/E2CNN/test/testA_52_0_405_0.9626_[0.9708 0.9545].png
img: 186 evaluate_data/GlaS/E2CNN/test/testA_52_126_0_0.8575_[0.8263 0.8886].png
img: 187 evaluate_data/GlaS/E2CNN/test/testA_52_126_405_0.9584_[0.9665 0.9504].png
img: 188 evaluate_data/GlaS/E2CNN/test/testA_53_0_0_0.4536_[0.9071 0.    ].png
img: 189 evaluate_data/GlaS/E2CNN/test/testA_53_0_405_0.5284_[0.7444 0.3125].png
img: 190 evaluate_data/GlaS/E2CNN/test/testA_53_126_0_0.4397_[0.8793 0.    ].png
img: 191 evaluate_data/GlaS/E2CNN/test/testA_53_126_405_0.5541_[0.765  0.3432].png
img: 192 evaluate_data/GlaS/E2CNN/test/testA_54_0_0_0.8212_[0.7954 0.847 ].png
img: 193 evaluate_data/GlaS/E2CNN/test/testA_54_0_405_0.8407_[0.8465 0.8349].png
img: 194 evaluate_data/GlaS/E2CNN/test/testA_54_126_0_0.8933_[0.8615 0.9251].png
img: 195 evaluate_data/GlaS/E2CNN/test/testA_54_126_405_0.8248_[0.8114 0.8382].png
img: 196 evaluate_data/GlaS/E2CNN/test/testA_55_0_0_0.8142_[0.7959 0.8324].png
img: 197 evaluate_data/GlaS/E2CNN/test/testA_55_0_405_0.6407_[0.5133 0.7681].png
img: 198 evaluate_data/GlaS/E2CNN/test/testA_55_126_0_0.873_[0.8499 0.896 ].png
img: 199 evaluate_data/GlaS/E2CNN/test/testA_55_126_405_0.5317_[0.3982 0.6653].png
img: 200 evaluate_data/GlaS/E2CNN/test/testA_56_0_0_0.4885_[0.4194 0.5576].png
img: 201 evaluate_data/GlaS/E2CNN/test/testA_56_0_405_0.6361_[0.7132 0.559 ].png
img: 202 evaluate_data/GlaS/E2CNN/test/testA_56_126_0_0.8021_[0.7916 0.8127].png
img: 203 evaluate_data/GlaS/E2CNN/test/testA_56_126_405_0.7376_[0.8059 0.6694].png
img: 204 evaluate_data/GlaS/E2CNN/test/testA_57_0_0_0.4657_[0.3188 0.6126].png
img: 205 evaluate_data/GlaS/E2CNN/test/testA_57_0_405_0.7157_[0.6511 0.7803].png
img: 206 evaluate_data/GlaS/E2CNN/test/testA_57_126_0_0.5972_[0.451  0.7435].png
img: 207 evaluate_data/GlaS/E2CNN/test/testA_57_126_405_0.6618_[0.6065 0.7172].png
img: 208 evaluate_data/GlaS/E2CNN/test/testA_58_0_0_0.3975_[0.4276 0.3674].png
img: 209 evaluate_data/GlaS/E2CNN/test/testA_58_0_405_0.8923_[0.8782 0.9064].png
img: 210 evaluate_data/GlaS/E2CNN/test/testA_58_126_0_0.3585_[0.3893 0.3277].png
img: 211 evaluate_data/GlaS/E2CNN/test/testA_58_126_405_0.9015_[0.8793 0.9236].png
img: 212 evaluate_data/GlaS/E2CNN/test/testA_59_0_0_0.5832_[0.5667 0.5997].png
img: 213 evaluate_data/GlaS/E2CNN/test/testA_59_0_405_0.8147_[0.7932 0.8363].png
img: 214 evaluate_data/GlaS/E2CNN/test/testA_59_126_0_0.6326_[0.5568 0.7083].png
img: 215 evaluate_data/GlaS/E2CNN/test/testA_59_126_405_0.8327_[0.8053 0.8601].png
img: 216 evaluate_data/GlaS/E2CNN/test/testA_5_0_0_0.8149_[0.784  0.8458].png
img: 217 evaluate_data/GlaS/E2CNN/test/testA_5_0_405_0.7995_[0.7633 0.8357].png
img: 218 evaluate_data/GlaS/E2CNN/test/testA_5_126_0_0.724_[0.6811 0.767 ].png
img: 219 evaluate_data/GlaS/E2CNN/test/testA_5_126_405_0.8244_[0.8248 0.8239].png
img: 220 evaluate_data/GlaS/E2CNN/test/testA_60_0_0_0.816_[0.817  0.8149].png
img: 221 evaluate_data/GlaS/E2CNN/test/testA_60_0_405_0.9506_[0.983  0.9182].png
img: 222 evaluate_data/GlaS/E2CNN/test/testA_60_126_0_0.902_[0.874 0.93 ].png
img: 223 evaluate_data/GlaS/E2CNN/test/testA_60_126_405_0.9327_[0.9617 0.9037].png
img: 224 evaluate_data/GlaS/E2CNN/test/testA_6_0_0_0.4906_[0.4426 0.5385].png
img: 225 evaluate_data/GlaS/E2CNN/test/testA_6_0_405_0.6322_[0.7123 0.5522].png
img: 226 evaluate_data/GlaS/E2CNN/test/testA_6_126_0_0.618_[0.5654 0.6706].png
img: 227 evaluate_data/GlaS/E2CNN/test/testA_6_126_405_0.6738_[0.7312 0.6164].png
img: 228 evaluate_data/GlaS/E2CNN/test/testA_7_0_0_0.4448_[0.8329 0.0568].png
img: 229 evaluate_data/GlaS/E2CNN/test/testA_7_0_405_0.3604_[0.3865 0.3344].png
img: 230 evaluate_data/GlaS/E2CNN/test/testA_7_126_0_0.4239_[0.7684 0.0794].png
img: 231 evaluate_data/GlaS/E2CNN/test/testA_7_126_405_0.5172_[0.5418 0.4926].png
img: 232 evaluate_data/GlaS/E2CNN/test/testA_8_0_0_0.7839_[0.7848 0.783 ].png
img: 233 evaluate_data/GlaS/E2CNN/test/testA_8_0_405_0.887_[0.9113 0.8627].png
img: 234 evaluate_data/GlaS/E2CNN/test/testA_8_126_0_0.8136_[0.7898 0.8374].png
img: 235 evaluate_data/GlaS/E2CNN/test/testA_8_126_405_0.9135_[0.9137 0.9132].png
img: 236 evaluate_data/GlaS/E2CNN/test/testA_9_0_0_0.666_[0.5447 0.7872].png
img: 237 evaluate_data/GlaS/E2CNN/test/testA_9_0_405_0.8431_[0.767  0.9192].png
img: 238 evaluate_data/GlaS/E2CNN/test/testA_9_126_0_0.7271_[0.6024 0.8518].png
img: 239 evaluate_data/GlaS/E2CNN/test/testA_9_126_405_0.7319_[0.5997 0.8641].png
img: 240 evaluate_data/GlaS/E2CNN/test/testB_10_0_0_0.4668_[0.5647 0.3689].png
img: 241 evaluate_data/GlaS/E2CNN/test/testB_10_0_405_0.5747_[0.5358 0.6136].png
img: 242 evaluate_data/GlaS/E2CNN/test/testB_10_126_0_0.5762_[0.596  0.5565].png
img: 243 evaluate_data/GlaS/E2CNN/test/testB_10_126_405_0.5477_[0.4749 0.6205].png
img: 244 evaluate_data/GlaS/E2CNN/test/testB_11_0_0_0.1978_[0.3955 0.    ].png
img: 245 evaluate_data/GlaS/E2CNN/test/testB_11_0_405_0.217_[0.434 0.   ].png
img: 246 evaluate_data/GlaS/E2CNN/test/testB_11_126_0_0.1366_[0.2732 0.    ].png
img: 247 evaluate_data/GlaS/E2CNN/test/testB_11_126_405_0.2257_[0.4513 0.    ].png
img: 248 evaluate_data/GlaS/E2CNN/test/testB_12_0_0_0.627_[0.574  0.6799].png
img: 249 evaluate_data/GlaS/E2CNN/test/testB_12_0_405_0.6378_[0.4848 0.7907].png
img: 250 evaluate_data/GlaS/E2CNN/test/testB_12_126_0_0.6686_[0.7063 0.6308].png
img: 251 evaluate_data/GlaS/E2CNN/test/testB_12_126_405_0.7577_[0.7078 0.8075].png
img: 252 evaluate_data/GlaS/E2CNN/test/testB_13_0_0_0.5874_[0.6157 0.5591].png
img: 253 evaluate_data/GlaS/E2CNN/test/testB_13_0_405_0.6167_[0.6089 0.6244].png
img: 254 evaluate_data/GlaS/E2CNN/test/testB_13_126_0_0.4442_[0.5023 0.3862].png
img: 255 evaluate_data/GlaS/E2CNN/test/testB_13_126_405_0.5806_[0.6468 0.5145].png
img: 256 evaluate_data/GlaS/E2CNN/test/testB_14_0_0_0.4283_[0.8565 0.    ].png
img: 257 evaluate_data/GlaS/E2CNN/test/testB_14_0_405_0.4548_[0.6228 0.2868].png
img: 258 evaluate_data/GlaS/E2CNN/test/testB_14_126_0_0.4808_[0.9616 0.    ].png
img: 259 evaluate_data/GlaS/E2CNN/test/testB_14_126_405_0.5399_[0.7742 0.3055].png
img: 260 evaluate_data/GlaS/E2CNN/test/testB_15_0_0_0.4197_[0.5264 0.3129].png
img: 261 evaluate_data/GlaS/E2CNN/test/testB_15_0_405_0.7157_[0.7627 0.6688].png
img: 262 evaluate_data/GlaS/E2CNN/test/testB_15_126_0_0.4655_[0.4448 0.4863].png
img: 263 evaluate_data/GlaS/E2CNN/test/testB_15_126_405_0.7205_[0.8106 0.6305].png
img: 264 evaluate_data/GlaS/E2CNN/test/testB_16_0_0_0.5198_[0.4698 0.5698].png
img: 265 evaluate_data/GlaS/E2CNN/test/testB_16_0_405_0.5221_[0.4091 0.635 ].png
img: 266 evaluate_data/GlaS/E2CNN/test/testB_16_126_0_0.628_[0.5389 0.717 ].png
img: 267 evaluate_data/GlaS/E2CNN/test/testB_16_126_405_0.3856_[0.2492 0.5221].png
img: 268 evaluate_data/GlaS/E2CNN/test/testB_17_0_0_0.3522_[0.5439 0.1606].png
img: 269 evaluate_data/GlaS/E2CNN/test/testB_17_0_405_0.3726_[0.2466 0.4986].png
img: 270 evaluate_data/GlaS/E2CNN/test/testB_17_126_0_0.4125_[0.5499 0.2751].png
img: 271 evaluate_data/GlaS/E2CNN/test/testB_17_126_405_0.1683_[0.1062 0.2305].png
img: 272 evaluate_data/GlaS/E2CNN/test/testB_18_0_0_0.2403_[0.4806 0.    ].png
img: 273 evaluate_data/GlaS/E2CNN/test/testB_18_0_405_0.2205_[0.4411 0.    ].png
img: 274 evaluate_data/GlaS/E2CNN/test/testB_18_126_0_0.285_[0.5701 0.    ].png
img: 275 evaluate_data/GlaS/E2CNN/test/testB_18_126_405_0.2014_[0.4028 0.    ].png
img: 276 evaluate_data/GlaS/E2CNN/test/testB_19_0_0_0.2343_[0.4686 0.    ].png
img: 277 evaluate_data/GlaS/E2CNN/test/testB_19_0_405_0.2905_[0.5809 0.    ].png
img: 278 evaluate_data/GlaS/E2CNN/test/testB_19_126_0_0.2162_[0.4324 0.    ].png
img: 279 evaluate_data/GlaS/E2CNN/test/testB_19_126_405_0.3323_[0.6647 0.    ].png
img: 280 evaluate_data/GlaS/E2CNN/test/testB_1_0_0_0.6354_[0.6459 0.625 ].png
img: 281 evaluate_data/GlaS/E2CNN/test/testB_1_0_405_0.9622_[0.9898 0.9346].png
img: 282 evaluate_data/GlaS/E2CNN/test/testB_1_126_0_0.6742_[0.7843 0.5642].png
img: 283 evaluate_data/GlaS/E2CNN/test/testB_1_126_405_0.9358_[0.9874 0.8842].png
img: 284 evaluate_data/GlaS/E2CNN/test/testB_20_0_0_0.1574_[0.3148 0.    ].png
img: 285 evaluate_data/GlaS/E2CNN/test/testB_20_0_405_0.2571_[0.3392 0.175 ].png
img: 286 evaluate_data/GlaS/E2CNN/test/testB_20_126_0_0.2102_[0.4203 0.    ].png
img: 287 evaluate_data/GlaS/E2CNN/test/testB_20_126_405_0.2151_[0.3021 0.1282].png
img: 288 evaluate_data/GlaS/E2CNN/test/testB_2_0_0_0.6271_[0.7324 0.5218].png
img: 289 evaluate_data/GlaS/E2CNN/test/testB_2_0_405_0.7663_[0.7411 0.7915].png
img: 290 evaluate_data/GlaS/E2CNN/test/testB_2_126_0_0.7094_[0.7134 0.7053].png
img: 291 evaluate_data/GlaS/E2CNN/test/testB_2_126_405_0.8581_[0.8467 0.8696].png
img: 292 evaluate_data/GlaS/E2CNN/test/testB_3_0_0_0.1328_[0.2657 0.    ].png
img: 293 evaluate_data/GlaS/E2CNN/test/testB_3_0_405_0.3225_[0.645 0.   ].png
img: 294 evaluate_data/GlaS/E2CNN/test/testB_3_126_0_0.1469_[0.2938 0.    ].png
img: 295 evaluate_data/GlaS/E2CNN/test/testB_3_126_405_0.2759_[0.5517 0.    ].png
img: 296 evaluate_data/GlaS/E2CNN/test/testB_4_0_0_0.8141_[0.8252 0.803 ].png
img: 297 evaluate_data/GlaS/E2CNN/test/testB_4_0_405_0.3384_[0.2981 0.3787].png
img: 298 evaluate_data/GlaS/E2CNN/test/testB_4_126_0_0.8043_[0.7778 0.8308].png
img: 299 evaluate_data/GlaS/E2CNN/test/testB_4_126_405_0.3079_[0.2407 0.3751].png
img: 300 evaluate_data/GlaS/E2CNN/test/testB_5_0_0_0.5283_[0.7222 0.3343].png
img: 301 evaluate_data/GlaS/E2CNN/test/testB_5_0_405_0.4996_[0.5289 0.4702].png
img: 302 evaluate_data/GlaS/E2CNN/test/testB_5_126_0_0.4664_[0.7267 0.2061].png
img: 303 evaluate_data/GlaS/E2CNN/test/testB_5_126_405_0.7926_[0.7802 0.8051].png
img: 304 evaluate_data/GlaS/E2CNN/test/testB_6_0_0_0.3888_[0.5273 0.2502].png
img: 305 evaluate_data/GlaS/E2CNN/test/testB_6_0_405_0.4737_[0.9473 0.    ].png
img: 306 evaluate_data/GlaS/E2CNN/test/testB_6_126_0_0.4707_[0.5243 0.4172].png
img: 307 evaluate_data/GlaS/E2CNN/test/testB_6_126_405_0.5706_[0.8925 0.2487].png
img: 308 evaluate_data/GlaS/E2CNN/test/testB_7_0_0_0.6162_[0.6014 0.631 ].png
img: 309 evaluate_data/GlaS/E2CNN/test/testB_7_0_405_0.9175_[0.901  0.9341].png
img: 310 evaluate_data/GlaS/E2CNN/test/testB_7_126_0_0.576_[0.6154 0.5366].png
img: 311 evaluate_data/GlaS/E2CNN/test/testB_7_126_405_0.7251_[0.7011 0.7492].png
img: 312 evaluate_data/GlaS/E2CNN/test/testB_8_0_0_0.6052_[0.6153 0.5951].png
img: 313 evaluate_data/GlaS/E2CNN/test/testB_8_0_405_0.697_[0.7659 0.6281].png
img: 314 evaluate_data/GlaS/E2CNN/test/testB_8_126_0_0.5456_[0.3957 0.6955].png
img: 315 evaluate_data/GlaS/E2CNN/test/testB_8_126_405_0.8194_[0.8495 0.7893].png
img: 316 evaluate_data/GlaS/E2CNN/test/testB_9_0_0_0.442_[0.2754 0.6085].png
img: 317 evaluate_data/GlaS/E2CNN/test/testB_9_0_405_0.4862_[0.4417 0.5308].png
img: 318 evaluate_data/GlaS/E2CNN/test/testB_9_126_0_0.4892_[0.3436 0.6348].png
img: 319 evaluate_data/GlaS/E2CNN/test/testB_9_126_405_0.6864_[0.7503 0.6225].png
iou list:
[0.8384, 0.8094, 0.771, 0.8043, 0.5817, 0.7271, 0.4858, 0.8262, 0.4781, 0.7963, 0.512, 0.749, 0.8404, 0.782, 0.8665, 0.8488, 0.5434, 0.9239, 0.5358, 0.9222, 0.5682, 0.883, 0.524, 0.9163, 0.8034, 0.8684, 0.7892, 0.8266, 0.2967, 0.8156, 0.3761, 0.8205, 0.7396, 0.8541, 0.6876, 0.8727, 0.8285, 0.8185, 0.8634, 0.8099, 0.6206, 0.3943, 0.7895, 0.3209, 0.4256, 0.5827, 0.3744, 0.5481, 0.7424, 0.8137, 0.8765, 0.8932, 0.65, 0.588, 0.6395, 0.5333, 0.3105, 0.6664, 0.2666, 0.8688, 0.6972, 0.7239, 0.8268, 0.7291, 0.6228, 0.8129, 0.7136, 0.8683, 0.4531, 0.8801, 0.4736, 0.8747, 0.8678, 0.8414, 0.7946, 0.8417, 0.4535, 0.85, 0.6282, 0.859, 0.6193, 0.9135, 0.833, 0.9342, 0.5063, 0.6846, 0.4814, 0.714, 0.873, 0.924, 0.874, 0.8821, 0.71, 0.9446, 0.6209, 0.9411, 0.7273, 0.6293, 0.7696, 0.7234, 0.7528, 0.9019, 0.7974, 0.903, 0.7758, 0.3616, 0.8025, 0.586, 0.8614, 0.8975, 0.8846, 0.8973, 0.561, 0.8889, 0.7459, 0.8996, 0.8149, 0.3212, 0.802, 0.1593, 0.3572, 0.4912, 0.468, 0.4922, 0.4905, 0.7194, 0.4944, 0.8659, 0.7357, 0.8784, 0.7637, 0.893, 0.7415, 0.8665, 0.7246, 0.8453, 0.6944, 0.6306, 0.6298, 0.7573, 0.5266, 0.8151, 0.451, 0.8327, 0.8636, 0.8835, 0.8782, 0.871, 0.6486, 0.8139, 0.582, 0.7904, 0.8575, 0.8744, 0.9068, 0.8902, 0.6623, 0.9023, 0.8054, 0.9021, 0.723, 0.9394, 0.7961, 0.8989, 0.7777, 0.7909, 0.7807, 0.7952, 0.4527, 0.608, 0.5534, 0.6959, 0.5917, 0.8522, 0.5176, 0.7277, 0.8352, 0.9125, 0.8521, 0.9062, 0.4206, 0.8543, 0.5407, 0.9247, 0.8787, 0.9626, 0.8575, 0.9584, 0.4536, 0.5284, 0.4397, 0.5541, 0.8212, 0.8407, 0.8933, 0.8248, 0.8142, 0.6407, 0.873, 0.5317, 0.4885, 0.6361, 0.8021, 0.7376, 0.4657, 0.7157, 0.5972, 0.6618, 0.3975, 0.8923, 0.3585, 0.9015, 0.5832, 0.8147, 0.6326, 0.8327, 0.8149, 0.7995, 0.724, 0.8244, 0.816, 0.9506, 0.902, 0.9327, 0.4906, 0.6322, 0.618, 0.6738, 0.4448, 0.3604, 0.4239, 0.5172, 0.7839, 0.887, 0.8136, 0.9135, 0.666, 0.8431, 0.7271, 0.7319, 0.4668, 0.5747, 0.5762, 0.5477, 0.1978, 0.217, 0.1366, 0.2257, 0.627, 0.6378, 0.6686, 0.7577, 0.5874, 0.6167, 0.4442, 0.5806, 0.4283, 0.4548, 0.4808, 0.5399, 0.4197, 0.7157, 0.4655, 0.7205, 0.5198, 0.5221, 0.628, 0.3856, 0.3522, 0.3726, 0.4125, 0.1683, 0.2403, 0.2205, 0.285, 0.2014, 0.2343, 0.2905, 0.2162, 0.3323, 0.6354, 0.9622, 0.6742, 0.9358, 0.1574, 0.2571, 0.2102, 0.2151, 0.6271, 0.7663, 0.7094, 0.8581, 0.1328, 0.3225, 0.1469, 0.2759, 0.8141, 0.3384, 0.8043, 0.3079, 0.5283, 0.4996, 0.4664, 0.7926, 0.3888, 0.4737, 0.4707, 0.5706, 0.6162, 0.9175, 0.576, 0.7251, 0.6052, 0.697, 0.5456, 0.8194, 0.442, 0.4862, 0.4892, 0.6864]
2022-12-26 18:26:40.116751, iou: tensor([0.7191, 0.6470], device='cuda:0'), 0.6831
==============================================================================
Running epilogue script on alpha51.

Submit time  : 2022-12-26T18:05:35
Start time   : 2022-12-26T18:05:35
End time     : 2022-12-26T18:26:42
Elapsed time : 00:21:07 (Timelimit=1-00:00:00)

Job ID: 2349362
Cluster: i5
User/Group: yy3u19/fp
State: COMPLETED (exit code 0)
Nodes: 1
Cores per node: 4
CPU Utilized: 00:21:26
CPU Efficiency: 25.37% of 01:24:28 core-walltime
Job Wall-clock time: 00:21:07
Memory Utilized: 12.07 GB
Memory Efficiency: 57.21% of 21.09 GB

