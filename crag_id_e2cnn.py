Running SLURM prolog script on alpha54.cluster.local
===============================================================================
Job started on Mon Dec 26 15:22:24 GMT 2022
Job ID          : 2349162
Job name        : run_test
WorkDir         : /mainfs/scratch/yy3u19/myN-JetNet
Command         : /mainfs/scratch/yy3u19/myN-JetNet/run_test
Partition       : ecsall
Num hosts       : 1
Num cores       : 4
Num of tasks    : 4
Hosts allocated : alpha54
Job Output Follows ...
===============================================================================
/scratch/yy3u19/anaconda3/lib/python3.9/site-packages/e2cnn/nn/modules/r2_conv/basisexpansion_singleblock.py:80: UserWarning: indexing with dtype torch.uint8 is now deprecated, please use a dtype torch.bool instead. (Triggered internally at  /opt/conda/conda-bld/pytorch_1639180549130/work/aten/src/ATen/native/IndexingUtils.h:30.)
  full_mask[mask] = norms.to(torch.uint8)
---------- kernel_size: 3 ---------- classes: 2 ---------- model: E2CNN ---------- rotations: 8 ---------- dataset: CRAG - test ----------
num of trainable parameters:7033922
Loading model checkpoints/CRAG/lr_0.002_bn_16_epoch_70_E2CNN_Ksize_3_rotation_8.pth num of rotations of filters: 8
Using device cuda
----------------------------------------------------------------------------------------------------------------------------------------------------------------
Num of images for evaulation: 160
img: 0 evaluate_data/CRAG/E2CNN/test/test_10_0_0_0.9419_[0.9814 0.9024].png
img: 1 evaluate_data/CRAG/E2CNN/test/test_10_0_1_0.8409_[0.7892 0.8926].png
img: 2 evaluate_data/CRAG/E2CNN/test/test_10_1_0_0.5_[1. 0.].png
img: 3 evaluate_data/CRAG/E2CNN/test/test_10_1_1_0.9258_[0.9785 0.8731].png
img: 4 evaluate_data/CRAG/E2CNN/test/test_11_0_0_0.9586_[0.9989 0.9184].png
img: 5 evaluate_data/CRAG/E2CNN/test/test_11_0_1_0.5_[1. 0.].png
img: 6 evaluate_data/CRAG/E2CNN/test/test_11_1_0_0.907_[0.898 0.916].png
img: 7 evaluate_data/CRAG/E2CNN/test/test_11_1_1_0.5_[1. 0.].png
img: 8 evaluate_data/CRAG/E2CNN/test/test_12_0_0_0.3174_[0.2406 0.3942].png
img: 9 evaluate_data/CRAG/E2CNN/test/test_12_0_1_0.9672_[0.9812 0.9531].png
img: 10 evaluate_data/CRAG/E2CNN/test/test_12_1_0_0.6403_[0.4859 0.7948].png
img: 11 evaluate_data/CRAG/E2CNN/test/test_12_1_1_0.8736_[0.81   0.9373].png
img: 12 evaluate_data/CRAG/E2CNN/test/test_13_0_0_0.8074_[0.9326 0.6822].png
img: 13 evaluate_data/CRAG/E2CNN/test/test_13_0_1_0.8653_[0.9549 0.7758].png
img: 14 evaluate_data/CRAG/E2CNN/test/test_13_1_0_0.8674_[0.9523 0.7825].png
img: 15 evaluate_data/CRAG/E2CNN/test/test_13_1_1_0.8982_[0.9923 0.8041].png
img: 16 evaluate_data/CRAG/E2CNN/test/test_14_0_0_0.9103_[0.8606 0.9601].png
img: 17 evaluate_data/CRAG/E2CNN/test/test_14_0_1_0.9593_[0.9831 0.9354].png
img: 18 evaluate_data/CRAG/E2CNN/test/test_14_1_0_0.8703_[0.8153 0.9253].png
img: 19 evaluate_data/CRAG/E2CNN/test/test_14_1_1_0.9285_[0.8955 0.9616].png
img: 20 evaluate_data/CRAG/E2CNN/test/test_15_0_0_0.7267_[0.8579 0.5955].png
img: 21 evaluate_data/CRAG/E2CNN/test/test_15_0_1_0.8647_[0.8557 0.8737].png
img: 22 evaluate_data/CRAG/E2CNN/test/test_15_1_0_0.7622_[0.9153 0.6091].png
img: 23 evaluate_data/CRAG/E2CNN/test/test_15_1_1_0.8908_[0.9485 0.833 ].png
img: 24 evaluate_data/CRAG/E2CNN/test/test_16_0_0_0.9508_[0.9182 0.9834].png
img: 25 evaluate_data/CRAG/E2CNN/test/test_16_0_1_0.9466_[0.9307 0.9625].png
img: 26 evaluate_data/CRAG/E2CNN/test/test_16_1_0_0.8902_[0.8039 0.9765].png
img: 27 evaluate_data/CRAG/E2CNN/test/test_16_1_1_0.7511_[0.5669 0.9353].png
img: 28 evaluate_data/CRAG/E2CNN/test/test_17_0_0_0.8795_[0.843  0.9159].png
img: 29 evaluate_data/CRAG/E2CNN/test/test_17_0_1_0.8364_[0.8202 0.8527].png
img: 30 evaluate_data/CRAG/E2CNN/test/test_17_1_0_0.9108_[0.9452 0.8765].png
img: 31 evaluate_data/CRAG/E2CNN/test/test_17_1_1_0.9104_[0.9628 0.858 ].png
img: 32 evaluate_data/CRAG/E2CNN/test/test_18_0_0_0.9391_[0.9663 0.9119].png
img: 33 evaluate_data/CRAG/E2CNN/test/test_18_0_1_0.9277_[0.9931 0.8623].png
img: 34 evaluate_data/CRAG/E2CNN/test/test_18_1_0_0.9011_[0.9494 0.8527].png
img: 35 evaluate_data/CRAG/E2CNN/test/test_18_1_1_0.8784_[0.9793 0.7774].png
img: 36 evaluate_data/CRAG/E2CNN/test/test_19_0_0_0.5_[1. 0.].png
img: 37 evaluate_data/CRAG/E2CNN/test/test_19_0_1_0.9498_[0.9436 0.956 ].png
img: 38 evaluate_data/CRAG/E2CNN/test/test_19_1_0_0.5_[1. 0.].png
img: 39 evaluate_data/CRAG/E2CNN/test/test_19_1_1_0.9346_[0.9454 0.9238].png
img: 40 evaluate_data/CRAG/E2CNN/test/test_1_0_0_0.9353_[0.9919 0.8786].png
img: 41 evaluate_data/CRAG/E2CNN/test/test_1_0_1_0.9115_[0.9554 0.8677].png
img: 42 evaluate_data/CRAG/E2CNN/test/test_1_1_0_0.7202_[0.8848 0.5557].png
img: 43 evaluate_data/CRAG/E2CNN/test/test_1_1_1_0.4999_[0.9998 0.    ].png
img: 44 evaluate_data/CRAG/E2CNN/test/test_20_0_0_0.9277_[0.9432 0.9122].png
img: 45 evaluate_data/CRAG/E2CNN/test/test_20_0_1_0.9419_[0.9618 0.9219].png
img: 46 evaluate_data/CRAG/E2CNN/test/test_20_1_0_0.9308_[0.9555 0.9061].png
img: 47 evaluate_data/CRAG/E2CNN/test/test_20_1_1_0.9424_[0.9628 0.922 ].png
img: 48 evaluate_data/CRAG/E2CNN/test/test_21_0_0_0.9642_[0.9854 0.9431].png
img: 49 evaluate_data/CRAG/E2CNN/test/test_21_0_1_0.8724_[0.8986 0.8463].png
img: 50 evaluate_data/CRAG/E2CNN/test/test_21_1_0_0.9154_[0.9196 0.9111].png
img: 51 evaluate_data/CRAG/E2CNN/test/test_21_1_1_0.8998_[0.9174 0.8821].png
img: 52 evaluate_data/CRAG/E2CNN/test/test_22_0_0_0.5_[1. 0.].png
img: 53 evaluate_data/CRAG/E2CNN/test/test_22_0_1_0.5_[1. 0.].png
img: 54 evaluate_data/CRAG/E2CNN/test/test_22_1_0_0.9515_[0.9984 0.9047].png
img: 55 evaluate_data/CRAG/E2CNN/test/test_22_1_1_0.9479_[0.9622 0.9337].png
img: 56 evaluate_data/CRAG/E2CNN/test/test_23_0_0_0.8441_[0.8973 0.791 ].png
img: 57 evaluate_data/CRAG/E2CNN/test/test_23_0_1_0.8113_[0.7663 0.8564].png
img: 58 evaluate_data/CRAG/E2CNN/test/test_23_1_0_0.7765_[0.8001 0.7529].png
img: 59 evaluate_data/CRAG/E2CNN/test/test_23_1_1_0.872_[0.8195 0.9245].png
img: 60 evaluate_data/CRAG/E2CNN/test/test_24_0_0_0.5_[1. 0.].png
img: 61 evaluate_data/CRAG/E2CNN/test/test_24_0_1_0.9585_[0.968  0.9489].png
img: 62 evaluate_data/CRAG/E2CNN/test/test_24_1_0_0.9564_[0.9852 0.9276].png
img: 63 evaluate_data/CRAG/E2CNN/test/test_24_1_1_0.933_[0.9062 0.9599].png
img: 64 evaluate_data/CRAG/E2CNN/test/test_25_0_0_0.9399_[0.9378 0.942 ].png
img: 65 evaluate_data/CRAG/E2CNN/test/test_25_0_1_0.9076_[0.8731 0.942 ].png
img: 66 evaluate_data/CRAG/E2CNN/test/test_25_1_0_0.8504_[0.7915 0.9094].png
img: 67 evaluate_data/CRAG/E2CNN/test/test_25_1_1_0.8507_[0.8516 0.8499].png
img: 68 evaluate_data/CRAG/E2CNN/test/test_26_0_0_0.8605_[0.8982 0.8228].png
img: 69 evaluate_data/CRAG/E2CNN/test/test_26_0_1_0.8906_[0.9443 0.8369].png
img: 70 evaluate_data/CRAG/E2CNN/test/test_26_1_0_0.8771_[0.9332 0.821 ].png
img: 71 evaluate_data/CRAG/E2CNN/test/test_26_1_1_0.8411_[0.9452 0.737 ].png
img: 72 evaluate_data/CRAG/E2CNN/test/test_27_0_0_0.9172_[0.8721 0.9624].png
img: 73 evaluate_data/CRAG/E2CNN/test/test_27_0_1_0.9162_[0.9803 0.8521].png
img: 74 evaluate_data/CRAG/E2CNN/test/test_27_1_0_0.8422_[0.7897 0.8948].png
img: 75 evaluate_data/CRAG/E2CNN/test/test_27_1_1_0.8629_[0.8835 0.8424].png
img: 76 evaluate_data/CRAG/E2CNN/test/test_28_0_0_0.9263_[0.9416 0.9109].png
img: 77 evaluate_data/CRAG/E2CNN/test/test_28_0_1_0.6498_[0.98   0.3196].png
img: 78 evaluate_data/CRAG/E2CNN/test/test_28_1_0_0.9298_[0.8914 0.9683].png
img: 79 evaluate_data/CRAG/E2CNN/test/test_28_1_1_0.9494_[0.971  0.9277].png
img: 80 evaluate_data/CRAG/E2CNN/test/test_29_0_0_0.8608_[0.813  0.9086].png
img: 81 evaluate_data/CRAG/E2CNN/test/test_29_0_1_0.865_[0.8422 0.8879].png
img: 82 evaluate_data/CRAG/E2CNN/test/test_29_1_0_0.8849_[0.8156 0.9542].png
img: 83 evaluate_data/CRAG/E2CNN/test/test_29_1_1_0.7068_[0.5301 0.8836].png
img: 84 evaluate_data/CRAG/E2CNN/test/test_2_0_0_0.9195_[0.9106 0.9284].png
img: 85 evaluate_data/CRAG/E2CNN/test/test_2_0_1_0.8584_[0.8314 0.8853].png
img: 86 evaluate_data/CRAG/E2CNN/test/test_2_1_0_0.8964_[0.8569 0.9359].png
img: 87 evaluate_data/CRAG/E2CNN/test/test_2_1_1_0.847_[0.824 0.87 ].png
img: 88 evaluate_data/CRAG/E2CNN/test/test_30_0_0_0.9442_[0.9661 0.9223].png
img: 89 evaluate_data/CRAG/E2CNN/test/test_30_0_1_0.9362_[0.9663 0.9061].png
img: 90 evaluate_data/CRAG/E2CNN/test/test_30_1_0_0.9169_[0.9146 0.9192].png
img: 91 evaluate_data/CRAG/E2CNN/test/test_30_1_1_0.8922_[0.8817 0.9028].png
img: 92 evaluate_data/CRAG/E2CNN/test/test_31_0_0_0.8995_[0.8765 0.9224].png
img: 93 evaluate_data/CRAG/E2CNN/test/test_31_0_1_0.8567_[0.8225 0.891 ].png
img: 94 evaluate_data/CRAG/E2CNN/test/test_31_1_0_0.9102_[0.8991 0.9213].png
img: 95 evaluate_data/CRAG/E2CNN/test/test_31_1_1_0.3559_[0.1454 0.5663].png
img: 96 evaluate_data/CRAG/E2CNN/test/test_32_0_0_0.8229_[0.8126 0.8333].png
img: 97 evaluate_data/CRAG/E2CNN/test/test_32_0_1_0.8151_[0.7795 0.8507].png
img: 98 evaluate_data/CRAG/E2CNN/test/test_32_1_0_0.7818_[0.754  0.8095].png
img: 99 evaluate_data/CRAG/E2CNN/test/test_32_1_1_0.7235_[0.632 0.815].png
img: 100 evaluate_data/CRAG/E2CNN/test/test_33_0_0_0.7218_[0.6077 0.8358].png
img: 101 evaluate_data/CRAG/E2CNN/test/test_33_0_1_0.8701_[0.8569 0.8833].png
img: 102 evaluate_data/CRAG/E2CNN/test/test_33_1_0_0.7876_[0.8309 0.7443].png
img: 103 evaluate_data/CRAG/E2CNN/test/test_33_1_1_0.6457_[0.709  0.5825].png
img: 104 evaluate_data/CRAG/E2CNN/test/test_34_0_0_0.9461_[0.9453 0.9469].png
img: 105 evaluate_data/CRAG/E2CNN/test/test_34_0_1_0.8916_[0.8671 0.9162].png
img: 106 evaluate_data/CRAG/E2CNN/test/test_34_1_0_0.9125_[0.91   0.9151].png
img: 107 evaluate_data/CRAG/E2CNN/test/test_34_1_1_0.9409_[0.9638 0.9181].png
img: 108 evaluate_data/CRAG/E2CNN/test/test_35_0_0_0.7505_[0.6669 0.8342].png
img: 109 evaluate_data/CRAG/E2CNN/test/test_35_0_1_0.8022_[0.6522 0.9522].png
img: 110 evaluate_data/CRAG/E2CNN/test/test_35_1_0_0.7208_[0.7237 0.718 ].png
img: 111 evaluate_data/CRAG/E2CNN/test/test_35_1_1_0.9393_[0.9153 0.9632].png
img: 112 evaluate_data/CRAG/E2CNN/test/test_36_0_0_0.9656_[0.9759 0.9553].png
img: 113 evaluate_data/CRAG/E2CNN/test/test_36_0_1_0.5_[1. 0.].png
img: 114 evaluate_data/CRAG/E2CNN/test/test_36_1_0_0.9349_[0.8986 0.9713].png
img: 115 evaluate_data/CRAG/E2CNN/test/test_36_1_1_0.9677_[0.9778 0.9576].png
img: 116 evaluate_data/CRAG/E2CNN/test/test_37_0_0_0.9664_[0.9875 0.9453].png
img: 117 evaluate_data/CRAG/E2CNN/test/test_37_0_1_0.9226_[0.9876 0.8576].png
img: 118 evaluate_data/CRAG/E2CNN/test/test_37_1_0_0.9717_[0.9862 0.9572].png
img: 119 evaluate_data/CRAG/E2CNN/test/test_37_1_1_0.9644_[0.9835 0.9453].png
img: 120 evaluate_data/CRAG/E2CNN/test/test_38_0_0_0.8411_[0.8944 0.7878].png
img: 121 evaluate_data/CRAG/E2CNN/test/test_38_0_1_0.8821_[0.927  0.8372].png
img: 122 evaluate_data/CRAG/E2CNN/test/test_38_1_0_0.8023_[0.7548 0.8498].png
img: 123 evaluate_data/CRAG/E2CNN/test/test_38_1_1_0.8827_[0.9412 0.8242].png
img: 124 evaluate_data/CRAG/E2CNN/test/test_39_0_0_0.494_[0.988 0.   ].png
img: 125 evaluate_data/CRAG/E2CNN/test/test_39_0_1_0.5_[1. 0.].png
img: 126 evaluate_data/CRAG/E2CNN/test/test_39_1_0_0.8862_[0.9289 0.8436].png
img: 127 evaluate_data/CRAG/E2CNN/test/test_39_1_1_0.8884_[0.9755 0.8012].png
img: 128 evaluate_data/CRAG/E2CNN/test/test_3_0_0_0.9275_[0.9763 0.8787].png
img: 129 evaluate_data/CRAG/E2CNN/test/test_3_0_1_0.9541_[0.9821 0.926 ].png
img: 130 evaluate_data/CRAG/E2CNN/test/test_3_1_0_0.9452_[0.984  0.9065].png
img: 131 evaluate_data/CRAG/E2CNN/test/test_3_1_1_0.5865_[0.2359 0.9371].png
img: 132 evaluate_data/CRAG/E2CNN/test/test_40_0_0_0.8186_[0.8413 0.796 ].png
img: 133 evaluate_data/CRAG/E2CNN/test/test_40_0_1_0.9085_[0.9362 0.8808].png
img: 134 evaluate_data/CRAG/E2CNN/test/test_40_1_0_0.7905_[0.8456 0.7355].png
img: 135 evaluate_data/CRAG/E2CNN/test/test_40_1_1_0.906_[0.9587 0.8534].png
img: 136 evaluate_data/CRAG/E2CNN/test/test_4_0_0_0.9109_[0.9132 0.9085].png
img: 137 evaluate_data/CRAG/E2CNN/test/test_4_0_1_0.8743_[0.8007 0.9479].png
img: 138 evaluate_data/CRAG/E2CNN/test/test_4_1_0_0.8453_[0.7653 0.9254].png
img: 139 evaluate_data/CRAG/E2CNN/test/test_4_1_1_0.8171_[0.7316 0.9026].png
img: 140 evaluate_data/CRAG/E2CNN/test/test_5_0_0_0.9592_[0.9607 0.9577].png
img: 141 evaluate_data/CRAG/E2CNN/test/test_5_0_1_0.8873_[0.8545 0.92  ].png
img: 142 evaluate_data/CRAG/E2CNN/test/test_5_1_0_0.9322_[0.9471 0.9174].png
img: 143 evaluate_data/CRAG/E2CNN/test/test_5_1_1_0.9335_[0.9357 0.9313].png
img: 144 evaluate_data/CRAG/E2CNN/test/test_6_0_0_0.8989_[0.8981 0.8997].png
img: 145 evaluate_data/CRAG/E2CNN/test/test_6_0_1_0.8778_[0.8589 0.8967].png
img: 146 evaluate_data/CRAG/E2CNN/test/test_6_1_0_0.7524_[0.671  0.8337].png
img: 147 evaluate_data/CRAG/E2CNN/test/test_6_1_1_0.8249_[0.7704 0.8794].png
img: 148 evaluate_data/CRAG/E2CNN/test/test_7_0_0_0.8534_[0.9934 0.7134].png
img: 149 evaluate_data/CRAG/E2CNN/test/test_7_0_1_0.8136_[0.8265 0.8008].png
img: 150 evaluate_data/CRAG/E2CNN/test/test_7_1_0_0.5364_[0.9932 0.0797].png
img: 151 evaluate_data/CRAG/E2CNN/test/test_7_1_1_0.7693_[0.8715 0.6672].png
img: 152 evaluate_data/CRAG/E2CNN/test/test_8_0_0_0.8568_[0.8567 0.8569].png
img: 153 evaluate_data/CRAG/E2CNN/test/test_8_0_1_0.6564_[0.4045 0.9084].png
img: 154 evaluate_data/CRAG/E2CNN/test/test_8_1_0_0.9028_[0.9871 0.8184].png
img: 155 evaluate_data/CRAG/E2CNN/test/test_8_1_1_0.5845_[0.2033 0.9658].png
img: 156 evaluate_data/CRAG/E2CNN/test/test_9_0_0_0.9593_[0.96   0.9586].png
img: 157 evaluate_data/CRAG/E2CNN/test/test_9_0_1_0.879_[0.8542 0.9039].png
img: 158 evaluate_data/CRAG/E2CNN/test/test_9_1_0_0.8742_[0.8351 0.9133].png
img: 159 evaluate_data/CRAG/E2CNN/test/test_9_1_1_0.927_[0.8922 0.9617].png
iou list:
[0.9419, 0.8409, 0.5, 0.9258, 0.9586, 0.5, 0.907, 0.5, 0.3174, 0.9672, 0.6403, 0.8736, 0.8074, 0.8653, 0.8674, 0.8982, 0.9103, 0.9593, 0.8703, 0.9285, 0.7267, 0.8647, 0.7622, 0.8908, 0.9508, 0.9466, 0.8902, 0.7511, 0.8795, 0.8364, 0.9108, 0.9104, 0.9391, 0.9277, 0.9011, 0.8784, 0.5, 0.9498, 0.5, 0.9346, 0.9353, 0.9115, 0.7202, 0.4999, 0.9277, 0.9419, 0.9308, 0.9424, 0.9642, 0.8724, 0.9154, 0.8998, 0.5, 0.5, 0.9515, 0.9479, 0.8441, 0.8113, 0.7765, 0.872, 0.5, 0.9585, 0.9564, 0.933, 0.9399, 0.9076, 0.8504, 0.8507, 0.8605, 0.8906, 0.8771, 0.8411, 0.9172, 0.9162, 0.8422, 0.8629, 0.9263, 0.6498, 0.9298, 0.9494, 0.8608, 0.865, 0.8849, 0.7068, 0.9195, 0.8584, 0.8964, 0.847, 0.9442, 0.9362, 0.9169, 0.8922, 0.8995, 0.8567, 0.9102, 0.3559, 0.8229, 0.8151, 0.7818, 0.7235, 0.7218, 0.8701, 0.7876, 0.6457, 0.9461, 0.8916, 0.9125, 0.9409, 0.7505, 0.8022, 0.7208, 0.9393, 0.9656, 0.5, 0.9349, 0.9677, 0.9664, 0.9226, 0.9717, 0.9644, 0.8411, 0.8821, 0.8023, 0.8827, 0.494, 0.5, 0.8862, 0.8884, 0.9275, 0.9541, 0.9452, 0.5865, 0.8186, 0.9085, 0.7905, 0.906, 0.9109, 0.8743, 0.8453, 0.8171, 0.9592, 0.8873, 0.9322, 0.9335, 0.8989, 0.8778, 0.7524, 0.8249, 0.8534, 0.8136, 0.5364, 0.7693, 0.8568, 0.6564, 0.9028, 0.5845, 0.9593, 0.879, 0.8742, 0.927]
2022-12-26 15:39:38.528596, iou: tensor([0.9130, 0.8816], device='cuda:0'), 0.8973
/scratch/yy3u19/anaconda3/lib/python3.9/site-packages/e2cnn/nn/modules/r2_conv/basisexpansion_singleblock.py:80: UserWarning: indexing with dtype torch.uint8 is now deprecated, please use a dtype torch.bool instead. (Triggered internally at  /opt/conda/conda-bld/pytorch_1639180549130/work/aten/src/ATen/native/IndexingUtils.h:30.)
  full_mask[mask] = norms.to(torch.uint8)
---------- kernel_size: 3 ---------- classes: 2 ---------- model: E2CNN ---------- rotations: -1 ---------- dataset: CRAG - test ----------
num of trainable parameters:13983490
Loading model checkpoints/CRAG/lr_0.002_bn_16_epoch_70_E2CNN_Ksize_3_rotation_-1.pth num of rotations of filters: -1
Using device cuda
----------------------------------------------------------------------------------------------------------------------------------------------------------------
Num of images for evaulation: 160
img: 0 evaluate_data/CRAG/E2CNN/test/test_10_0_0_0.9013_[0.965258   0.83730626].png
img: 1 evaluate_data/CRAG/E2CNN/test/test_10_0_1_0.7045_[0.59490764 0.81401616].png
img: 2 evaluate_data/CRAG/E2CNN/test/test_10_1_0_0.5_[1. 0.].png
img: 3 evaluate_data/CRAG/E2CNN/test/test_10_1_1_0.8872_[0.9640915 0.8103548].png
img: 4 evaluate_data/CRAG/E2CNN/test/test_11_0_0_0.8888_[0.99712515 0.7803945 ].png
img: 5 evaluate_data/CRAG/E2CNN/test/test_11_0_1_0.4999_[0.9997711 0.       ].png
img: 6 evaluate_data/CRAG/E2CNN/test/test_11_1_0_0.825_[0.8154421 0.8345802].png
img: 7 evaluate_data/CRAG/E2CNN/test/test_11_1_1_0.5_[1. 0.].png
img: 8 evaluate_data/CRAG/E2CNN/test/test_12_0_0_0.5613_[0.4143773  0.70823705].png
img: 9 evaluate_data/CRAG/E2CNN/test/test_12_0_1_0.9626_[0.97860384 0.9465782 ].png
img: 10 evaluate_data/CRAG/E2CNN/test/test_12_1_0_0.7779_[0.69758576 0.8582947 ].png
img: 11 evaluate_data/CRAG/E2CNN/test/test_12_1_1_0.8901_[0.8351602 0.9449802].png
img: 12 evaluate_data/CRAG/E2CNN/test/test_13_0_0_0.6657_[0.8410875  0.49031666].png
img: 13 evaluate_data/CRAG/E2CNN/test/test_13_0_1_0.7142_[0.8727066 0.5557099].png
img: 14 evaluate_data/CRAG/E2CNN/test/test_13_1_0_0.6551_[0.81490564 0.49528012].png
img: 15 evaluate_data/CRAG/E2CNN/test/test_13_1_1_0.8147_[0.9826344 0.6467574].png
img: 16 evaluate_data/CRAG/E2CNN/test/test_14_0_0_0.7918_[0.6713699 0.9121879].png
img: 17 evaluate_data/CRAG/E2CNN/test/test_14_0_1_0.9282_[0.9710281  0.88546586].png
img: 18 evaluate_data/CRAG/E2CNN/test/test_14_1_0_0.8254_[0.7492047  0.90153635].png
img: 19 evaluate_data/CRAG/E2CNN/test/test_14_1_1_0.8834_[0.8299082  0.93685067].png
img: 20 evaluate_data/CRAG/E2CNN/test/test_15_0_0_0.7004_[0.8311137 0.5697825].png
img: 21 evaluate_data/CRAG/E2CNN/test/test_15_0_1_0.748_[0.73267543 0.7633775 ].png
img: 22 evaluate_data/CRAG/E2CNN/test/test_15_1_0_0.733_[0.9054351  0.56057686].png
img: 23 evaluate_data/CRAG/E2CNN/test/test_15_1_1_0.7826_[0.89050645 0.6747003 ].png
img: 24 evaluate_data/CRAG/E2CNN/test/test_16_0_0_0.8255_[0.712474 0.938621].png
img: 25 evaluate_data/CRAG/E2CNN/test/test_16_0_1_0.8571_[0.81638026 0.8978075 ].png
img: 26 evaluate_data/CRAG/E2CNN/test/test_16_1_0_0.8848_[0.7963243 0.9733449].png
img: 27 evaluate_data/CRAG/E2CNN/test/test_16_1_1_0.5795_[0.29805967 0.86085975].png
img: 28 evaluate_data/CRAG/E2CNN/test/test_17_0_0_0.8018_[0.74764776 0.85590726].png
img: 29 evaluate_data/CRAG/E2CNN/test/test_17_0_1_0.7323_[0.69569623 0.76890695].png
img: 30 evaluate_data/CRAG/E2CNN/test/test_17_1_0_0.8921_[0.9316963 0.8525178].png
img: 31 evaluate_data/CRAG/E2CNN/test/test_17_1_1_0.692_[0.82414806 0.55989254].png
img: 32 evaluate_data/CRAG/E2CNN/test/test_18_0_0_0.9201_[0.9559737  0.88422716].png
img: 33 evaluate_data/CRAG/E2CNN/test/test_18_0_1_0.8692_[0.9853632 0.753059 ].png
img: 34 evaluate_data/CRAG/E2CNN/test/test_18_1_0_0.7575_[0.8866687 0.6282873].png
img: 35 evaluate_data/CRAG/E2CNN/test/test_18_1_1_0.6953_[0.9503595  0.44024312].png
img: 36 evaluate_data/CRAG/E2CNN/test/test_19_0_0_0.5_[1. 0.].png
img: 37 evaluate_data/CRAG/E2CNN/test/test_19_0_1_0.8939_[0.8807257 0.907106 ].png
img: 38 evaluate_data/CRAG/E2CNN/test/test_19_1_0_0.4989_[0.99770355 0.        ].png
img: 39 evaluate_data/CRAG/E2CNN/test/test_19_1_1_0.9098_[0.92438966 0.8952953 ].png
img: 40 evaluate_data/CRAG/E2CNN/test/test_1_0_0_0.909_[0.9882342  0.82980335].png
img: 41 evaluate_data/CRAG/E2CNN/test/test_1_0_1_0.8247_[0.9173606  0.73200506].png
img: 42 evaluate_data/CRAG/E2CNN/test/test_1_1_0_0.8411_[0.9277757 0.7544999].png
img: 43 evaluate_data/CRAG/E2CNN/test/test_1_1_1_0.4999_[0.9997597 0.       ].png
img: 44 evaluate_data/CRAG/E2CNN/test/test_20_0_0_0.8884_[0.9117937 0.8650937].png
img: 45 evaluate_data/CRAG/E2CNN/test/test_20_0_1_0.8044_[0.8733046 0.7355573].png
img: 46 evaluate_data/CRAG/E2CNN/test/test_20_1_0_0.7606_[0.84175164 0.6794519 ].png
img: 47 evaluate_data/CRAG/E2CNN/test/test_20_1_1_0.8189_[0.8831053 0.7546911].png
img: 48 evaluate_data/CRAG/E2CNN/test/test_21_0_0_0.924_[0.9686761  0.87927705].png
img: 49 evaluate_data/CRAG/E2CNN/test/test_21_0_1_0.8142_[0.85883826 0.76965004].png
img: 50 evaluate_data/CRAG/E2CNN/test/test_21_1_0_0.8464_[0.8491254  0.84360766].png
img: 51 evaluate_data/CRAG/E2CNN/test/test_21_1_1_0.746_[0.7705547 0.7214568].png
img: 52 evaluate_data/CRAG/E2CNN/test/test_22_0_0_0.5_[1. 0.].png
img: 53 evaluate_data/CRAG/E2CNN/test/test_22_0_1_0.5_[1. 0.].png
img: 54 evaluate_data/CRAG/E2CNN/test/test_22_1_0_0.951_[0.9984716 0.903588 ].png
img: 55 evaluate_data/CRAG/E2CNN/test/test_22_1_1_0.9323_[0.9511    0.9135651].png
img: 56 evaluate_data/CRAG/E2CNN/test/test_23_0_0_0.8304_[0.90051633 0.76021093].png
img: 57 evaluate_data/CRAG/E2CNN/test/test_23_0_1_0.7281_[0.663387  0.7928791].png
img: 58 evaluate_data/CRAG/E2CNN/test/test_23_1_0_0.724_[0.7499007  0.69800544].png
img: 59 evaluate_data/CRAG/E2CNN/test/test_23_1_1_0.7231_[0.60558695 0.84065163].png
img: 60 evaluate_data/CRAG/E2CNN/test/test_24_0_0_0.5_[1. 0.].png
img: 61 evaluate_data/CRAG/E2CNN/test/test_24_0_1_0.9146_[0.93245476 0.89667714].png
img: 62 evaluate_data/CRAG/E2CNN/test/test_24_1_0_0.953_[0.98393387 0.92205876].png
img: 63 evaluate_data/CRAG/E2CNN/test/test_24_1_1_0.8318_[0.7611388  0.90251637].png
img: 64 evaluate_data/CRAG/E2CNN/test/test_25_0_0_0.9303_[0.9287194  0.93184733].png
img: 65 evaluate_data/CRAG/E2CNN/test/test_25_0_1_0.8496_[0.79125905 0.90786356].png
img: 66 evaluate_data/CRAG/E2CNN/test/test_25_1_0_0.8232_[0.7582665 0.8882019].png
img: 67 evaluate_data/CRAG/E2CNN/test/test_25_1_1_0.8544_[0.8485829 0.8602785].png
img: 68 evaluate_data/CRAG/E2CNN/test/test_26_0_0_0.8423_[0.88675666 0.7978064 ].png
img: 69 evaluate_data/CRAG/E2CNN/test/test_26_0_1_0.813_[0.8982049 0.727793 ].png
img: 70 evaluate_data/CRAG/E2CNN/test/test_26_1_0_0.815_[0.89937216 0.73058075].png
img: 71 evaluate_data/CRAG/E2CNN/test/test_26_1_1_0.7739_[0.9218712 0.6259345].png
img: 72 evaluate_data/CRAG/E2CNN/test/test_27_0_0_0.8465_[0.76025623 0.93279743].png
img: 73 evaluate_data/CRAG/E2CNN/test/test_27_0_1_0.8704_[0.97041744 0.7703002 ].png
img: 74 evaluate_data/CRAG/E2CNN/test/test_27_1_0_0.6608_[0.5364236  0.78523564].png
img: 75 evaluate_data/CRAG/E2CNN/test/test_27_1_1_0.5437_[0.518567  0.5688613].png
img: 76 evaluate_data/CRAG/E2CNN/test/test_28_0_0_0.8684_[0.8940756  0.84273845].png
img: 77 evaluate_data/CRAG/E2CNN/test/test_28_0_1_0.583_[0.96243036 0.20354344].png
img: 78 evaluate_data/CRAG/E2CNN/test/test_28_1_0_0.8761_[0.81376696 0.938396  ].png
img: 79 evaluate_data/CRAG/E2CNN/test/test_28_1_1_0.9583_[0.976484  0.9400418].png
img: 80 evaluate_data/CRAG/E2CNN/test/test_29_0_0_0.86_[0.8124472  0.90746737].png
img: 81 evaluate_data/CRAG/E2CNN/test/test_29_0_1_0.894_[0.8717114 0.9162692].png
img: 82 evaluate_data/CRAG/E2CNN/test/test_29_1_0_0.6117_[0.37897563 0.8444748 ].png
img: 83 evaluate_data/CRAG/E2CNN/test/test_29_1_1_0.7224_[0.5415004  0.90331435].png
img: 84 evaluate_data/CRAG/E2CNN/test/test_2_0_0_0.8327_[0.8073596  0.85798436].png
img: 85 evaluate_data/CRAG/E2CNN/test/test_2_0_1_0.7799_[0.74286723 0.816922  ].png
img: 86 evaluate_data/CRAG/E2CNN/test/test_2_1_0_0.7225_[0.6203406 0.8245864].png
img: 87 evaluate_data/CRAG/E2CNN/test/test_2_1_1_0.7782_[0.74137706 0.81503016].png
img: 88 evaluate_data/CRAG/E2CNN/test/test_30_0_0_0.5418_[0.5938812  0.48969153].png
img: 89 evaluate_data/CRAG/E2CNN/test/test_30_0_1_0.7234_[0.8243503 0.6223813].png
img: 90 evaluate_data/CRAG/E2CNN/test/test_30_1_0_0.8507_[0.8440838 0.8572665].png
img: 91 evaluate_data/CRAG/E2CNN/test/test_30_1_1_0.6197_[0.59298265 0.64638084].png
img: 92 evaluate_data/CRAG/E2CNN/test/test_31_0_0_0.7581_[0.7119371 0.8043553].png
img: 93 evaluate_data/CRAG/E2CNN/test/test_31_0_1_0.8138_[0.77543503 0.8521628 ].png
img: 94 evaluate_data/CRAG/E2CNN/test/test_31_1_0_0.8437_[0.8266647  0.86082214].png
img: 95 evaluate_data/CRAG/E2CNN/test/test_31_1_1_0.4483_[0.19167915 0.704836  ].png
img: 96 evaluate_data/CRAG/E2CNN/test/test_32_0_0_0.7377_[0.733687 0.741703].png
img: 97 evaluate_data/CRAG/E2CNN/test/test_32_0_1_0.6918_[0.62547576 0.758086  ].png
img: 98 evaluate_data/CRAG/E2CNN/test/test_32_1_0_0.7381_[0.7104638  0.76565164].png
img: 99 evaluate_data/CRAG/E2CNN/test/test_32_1_1_0.6077_[0.5248159 0.6905276].png
img: 100 evaluate_data/CRAG/E2CNN/test/test_33_0_0_0.745_[0.6301819  0.85981977].png
img: 101 evaluate_data/CRAG/E2CNN/test/test_33_0_1_0.8585_[0.84863025 0.86845404].png
img: 102 evaluate_data/CRAG/E2CNN/test/test_33_1_0_0.7353_[0.79410815 0.6765351 ].png
img: 103 evaluate_data/CRAG/E2CNN/test/test_33_1_1_0.7316_[0.78785795 0.67528087].png
img: 104 evaluate_data/CRAG/E2CNN/test/test_34_0_0_0.8535_[0.8511241  0.85587454].png
img: 105 evaluate_data/CRAG/E2CNN/test/test_34_0_1_0.7024_[0.619595  0.7852994].png
img: 106 evaluate_data/CRAG/E2CNN/test/test_34_1_0_0.7788_[0.76419145 0.79340583].png
img: 107 evaluate_data/CRAG/E2CNN/test/test_34_1_1_0.7805_[0.8500321 0.710966 ].png
img: 108 evaluate_data/CRAG/E2CNN/test/test_35_0_0_0.7749_[0.7030416  0.84670293].png
img: 109 evaluate_data/CRAG/E2CNN/test/test_35_0_1_0.6819_[0.43625423 0.9275332 ].png
img: 110 evaluate_data/CRAG/E2CNN/test/test_35_1_0_0.7237_[0.7222604  0.72510564].png
img: 111 evaluate_data/CRAG/E2CNN/test/test_35_1_1_0.9223_[0.88995147 0.95455897].png
img: 112 evaluate_data/CRAG/E2CNN/test/test_36_0_0_0.9176_[0.94389105 0.89138854].png
img: 113 evaluate_data/CRAG/E2CNN/test/test_36_0_1_0.5_[1. 0.].png
img: 114 evaluate_data/CRAG/E2CNN/test/test_36_1_0_0.874_[0.8057784 0.9421606].png
img: 115 evaluate_data/CRAG/E2CNN/test/test_36_1_1_0.9611_[0.9733631 0.9487696].png
img: 116 evaluate_data/CRAG/E2CNN/test/test_37_0_0_0.9331_[0.97433907 0.89184976].png
img: 117 evaluate_data/CRAG/E2CNN/test/test_37_0_1_0.7657_[0.9474467  0.58399534].png
img: 118 evaluate_data/CRAG/E2CNN/test/test_37_1_0_0.9232_[0.9599862 0.8863265].png
img: 119 evaluate_data/CRAG/E2CNN/test/test_37_1_1_0.8945_[0.94637597 0.8425423 ].png
img: 120 evaluate_data/CRAG/E2CNN/test/test_38_0_0_0.8461_[0.89860505 0.79360884].png
img: 121 evaluate_data/CRAG/E2CNN/test/test_38_0_1_0.8089_[0.8730079 0.7448096].png
img: 122 evaluate_data/CRAG/E2CNN/test/test_38_1_0_0.7905_[0.73996246 0.84099156].png
img: 123 evaluate_data/CRAG/E2CNN/test/test_38_1_1_0.8094_[0.9030643 0.7157252].png
img: 124 evaluate_data/CRAG/E2CNN/test/test_39_0_0_0.395_[0.78993607 0.        ].png
img: 125 evaluate_data/CRAG/E2CNN/test/test_39_0_1_0.4977_[0.99544907 0.        ].png
img: 126 evaluate_data/CRAG/E2CNN/test/test_39_1_0_0.8143_[0.8767084 0.7519479].png
img: 127 evaluate_data/CRAG/E2CNN/test/test_39_1_1_0.7257_[0.9299718  0.52145004].png
img: 128 evaluate_data/CRAG/E2CNN/test/test_3_0_0_0.9082_[0.9692747 0.8472059].png
img: 129 evaluate_data/CRAG/E2CNN/test/test_3_0_1_0.9224_[0.96965617 0.8750833 ].png
img: 130 evaluate_data/CRAG/E2CNN/test/test_3_1_0_0.951_[0.9863733 0.9156205].png
img: 131 evaluate_data/CRAG/E2CNN/test/test_3_1_1_0.5907_[0.2393001  0.94207877].png
img: 132 evaluate_data/CRAG/E2CNN/test/test_40_0_0_0.7621_[0.796439   0.72770107].png
img: 133 evaluate_data/CRAG/E2CNN/test/test_40_0_1_0.896_[0.9273917  0.86461216].png
img: 134 evaluate_data/CRAG/E2CNN/test/test_40_1_0_0.8054_[0.8532864 0.7574646].png
img: 135 evaluate_data/CRAG/E2CNN/test/test_40_1_1_0.8788_[0.9459156 0.8115876].png
img: 136 evaluate_data/CRAG/E2CNN/test/test_4_0_0_0.8604_[0.8619346  0.85888034].png
img: 137 evaluate_data/CRAG/E2CNN/test/test_4_0_1_0.7495_[0.59629107 0.90274763].png
img: 138 evaluate_data/CRAG/E2CNN/test/test_4_1_0_0.7683_[0.6442553  0.89238703].png
img: 139 evaluate_data/CRAG/E2CNN/test/test_4_1_1_0.6892_[0.55467564 0.8236583 ].png
img: 140 evaluate_data/CRAG/E2CNN/test/test_5_0_0_0.647_[0.61930835 0.67468965].png
img: 141 evaluate_data/CRAG/E2CNN/test/test_5_0_1_0.5605_[0.3823058 0.7387027].png
img: 142 evaluate_data/CRAG/E2CNN/test/test_5_1_0_0.621_[0.62676203 0.61527354].png
img: 143 evaluate_data/CRAG/E2CNN/test/test_5_1_1_0.6242_[0.58930784 0.65914387].png
img: 144 evaluate_data/CRAG/E2CNN/test/test_6_0_0_0.8417_[0.8407955  0.84267247].png
img: 145 evaluate_data/CRAG/E2CNN/test/test_6_0_1_0.6943_[0.6571945 0.7314831].png
img: 146 evaluate_data/CRAG/E2CNN/test/test_6_1_0_0.68_[0.5664694  0.79354423].png
img: 147 evaluate_data/CRAG/E2CNN/test/test_6_1_1_0.7138_[0.61566    0.81185496].png
img: 148 evaluate_data/CRAG/E2CNN/test/test_7_0_0_0.6128_[0.94655997 0.2791113 ].png
img: 149 evaluate_data/CRAG/E2CNN/test/test_7_0_1_0.5581_[0.5128025 0.6033752].png
img: 150 evaluate_data/CRAG/E2CNN/test/test_7_1_0_0.4958_[0.92701375 0.06456685].png
img: 151 evaluate_data/CRAG/E2CNN/test/test_7_1_1_0.658_[0.74986464 0.5661743 ].png
img: 152 evaluate_data/CRAG/E2CNN/test/test_8_0_0_0.6968_[0.72279453 0.6707268 ].png
img: 153 evaluate_data/CRAG/E2CNN/test/test_8_0_1_0.5879_[0.28028458 0.89558595].png
img: 154 evaluate_data/CRAG/E2CNN/test/test_8_1_0_0.8982_[0.9856237 0.8107676].png
img: 155 evaluate_data/CRAG/E2CNN/test/test_8_1_1_0.6145_[0.27006397 0.958895  ].png
img: 156 evaluate_data/CRAG/E2CNN/test/test_9_0_0_0.8238_[0.831758   0.81575114].png
img: 157 evaluate_data/CRAG/E2CNN/test/test_9_0_1_0.7566_[0.7253459 0.7877998].png
img: 158 evaluate_data/CRAG/E2CNN/test/test_9_1_0_0.4661_[0.3787091  0.55352706].png
img: 159 evaluate_data/CRAG/E2CNN/test/test_9_1_1_0.7352_[0.6157051  0.85465294].png
iou list:
[0.9013, 0.7045, 0.5, 0.8872, 0.8888, 0.4999, 0.825, 0.5, 0.5613, 0.9626, 0.7779, 0.8901, 0.6657, 0.7142, 0.6551, 0.8147, 0.7918, 0.9282, 0.8254, 0.8834, 0.7004, 0.748, 0.733, 0.7826, 0.8255, 0.8571, 0.8848, 0.5795, 0.8018, 0.7323, 0.8921, 0.692, 0.9201, 0.8692, 0.7575, 0.6953, 0.5, 0.8939, 0.4989, 0.9098, 0.909, 0.8247, 0.8411, 0.4999, 0.8884, 0.8044, 0.7606, 0.8189, 0.924, 0.8142, 0.8464, 0.746, 0.5, 0.5, 0.951, 0.9323, 0.8304, 0.7281, 0.724, 0.7231, 0.5, 0.9146, 0.953, 0.8318, 0.9303, 0.8496, 0.8232, 0.8544, 0.8423, 0.813, 0.815, 0.7739, 0.8465, 0.8704, 0.6608, 0.5437, 0.8684, 0.583, 0.8761, 0.9583, 0.86, 0.894, 0.6117, 0.7224, 0.8327, 0.7799, 0.7225, 0.7782, 0.5418, 0.7234, 0.8507, 0.6197, 0.7581, 0.8138, 0.8437, 0.4483, 0.7377, 0.6918, 0.7381, 0.6077, 0.745, 0.8585, 0.7353, 0.7316, 0.8535, 0.7024, 0.7788, 0.7805, 0.7749, 0.6819, 0.7237, 0.9223, 0.9176, 0.5, 0.874, 0.9611, 0.9331, 0.7657, 0.9232, 0.8945, 0.8461, 0.8089, 0.7905, 0.8094, 0.395, 0.4977, 0.8143, 0.7257, 0.9082, 0.9224, 0.951, 0.5907, 0.7621, 0.896, 0.8054, 0.8788, 0.8604, 0.7495, 0.7683, 0.6892, 0.647, 0.5605, 0.621, 0.6242, 0.8417, 0.6943, 0.68, 0.7138, 0.6128, 0.5581, 0.4958, 0.658, 0.6968, 0.5879, 0.8982, 0.6145, 0.8238, 0.7566, 0.4661, 0.7352]
2022-12-26 15:58:18.029581, iou: tensor([0.8510, 0.8064], device='cuda:0'), 0.8287
==============================================================================
Running epilogue script on alpha54.

Submit time  : 2022-12-26T15:22:24
Start time   : 2022-12-26T15:22:24
End time     : 2022-12-26T15:58:21
Elapsed time : 00:35:57 (Timelimit=1-00:00:00)

Job ID: 2349162
Cluster: i5
User/Group: yy3u19/fp
State: COMPLETED (exit code 0)
Nodes: 1
Cores per node: 4
CPU Utilized: 00:36:13
CPU Efficiency: 25.19% of 02:23:48 core-walltime
Job Wall-clock time: 00:35:57
Memory Utilized: 15.82 GB
Memory Efficiency: 74.99% of 21.09 GB

