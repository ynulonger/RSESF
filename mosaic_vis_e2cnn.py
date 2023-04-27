Running SLURM prolog script on alpha51.cluster.local
===============================================================================
Job started on Mon Dec 26 18:04:01 GMT 2022
Job ID          : 2349360
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
---------- kernel_size: 3 ---------- classes: 5 ---------- model: E2CNN ---------- rotations: -1 ---------- dataset: Mosaics - vis ----------
num of trainable parameters:13983429
Loading model checkpoints/Mosaics/lr_0.002_bn_16_epoch_70_E2CNN_Ksize_3_rotation_-1.pth num of rotations of filters: -1
Using device cuda
----------------------------------------------------------------------------------------------------------------------------------------------------------------
Num of images for evaulation: 2000
img: 0 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_0_s_0.73_r_107_0.7202_[0.42880037 0.6567733  0.94868505 0.65287864 0.9139431 ].png
img: 1 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1000_s_1.54_r_90_0.4826_[2.0752285e-01 7.4786389e-01 4.7476047e-01 9.8255199e-01 3.7452622e-04].png
img: 2 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1001_s_1.45_r_212_0.7019_[0.35087833 0.8831878  0.69268805 0.9869462  0.59579533].png
img: 3 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1002_s_1.37_r_96_0.5875_[0.389321   0.9207083  0.5085458  0.9874029  0.13176729].png
img: 4 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1003_s_1.17_r_216_0.844_[0.3958224  0.93585503 0.95256555 0.98766994 0.947948  ].png
img: 5 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1004_s_1.49_r_288_0.5858_[0.31499448 0.84220594 0.54239637 0.9836387  0.24570134].png
img: 6 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1005_s_0.73_r_14_0.737_[0.4255063  0.68208194 0.9482612  0.7079417  0.92107904].png
img: 7 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1006_s_1.3_r_301_0.8114_[0.38386974 0.92768097 0.8819295  0.98848814 0.87523836].png
img: 8 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1007_s_1.7_r_205_0.4951_[0.16689411 0.72627604 0.50659925 0.96108115 0.1145261 ].png
img: 9 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1008_s_1.84_r_262_0.4304_[6.8265520e-02 6.5398335e-01 4.7048548e-01 9.5932621e-01 5.2366988e-05].png
img: 10 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1009_s_1.27_r_161_0.7368_[0.39949766 0.92292535 0.7214082  0.9901144  0.6500261 ].png
img: 11 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_100_s_1.08_r_257_0.8334_[0.40491676 0.92290187 0.9282423  0.98702544 0.9238638 ].png
img: 12 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1010_s_0.68_r_61_0.5978_[0.4408004  0.50300014 0.9324622  0.23287141 0.879911  ].png
img: 13 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1011_s_1.32_r_135_0.7659_[0.3837527  0.927278   0.7851205  0.98956007 0.7435965 ].png
img: 14 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1012_s_1.49_r_68_0.5787_[0.3187417  0.85312533 0.53062266 0.98892033 0.20214461].png
img: 15 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1013_s_1.49_r_46_0.6237_[0.30023506 0.8350809  0.6016091  0.9881475  0.3934617 ].png
img: 16 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1014_s_1.61_r_134_0.5407_[0.20385325 0.7441892  0.5410312  0.98105925 0.23360845].png
img: 17 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1015_s_1.73_r_287_0.462_[0.13487826 0.7091285  0.48041102 0.9533901  0.03232546].png
img: 18 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1016_s_1.97_r_184_0.411_[0.03437207 0.61941624 0.4624736  0.93848896 0.        ].png
img: 19 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1017_s_1.86_r_298_0.4499_[0.10157204 0.68419045 0.4806648  0.9372659  0.04574815].png
img: 20 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1018_s_0.64_r_139_0.5579_[0.42321894 0.48321044 0.86381465 0.21455167 0.80460924].png
img: 21 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1019_s_0.8_r_15_0.823_[0.4107329  0.85897577 0.9525279  0.9551826  0.9376652 ].png
img: 22 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_101_s_1.39_r_325_0.7391_[0.37463775 0.9186989  0.73647386 0.9896814  0.6758087 ].png
img: 23 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1020_s_1.88_r_62_0.4427_[0.09433071 0.6774614  0.4734766  0.9425146  0.025485  ].png
img: 24 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1021_s_0.53_r_313_0.3642_[0.36672777 0.37659794 0.26078108 0.3070242  0.5099142 ].png
img: 25 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1022_s_1.47_r_175_0.5237_[0.30239603 0.82313824 0.48165286 0.9883287  0.02317009].png
img: 26 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1023_s_1.5_r_57_0.6044_[0.30085486 0.8368918  0.5723963  0.9892093  0.3227131 ].png
img: 27 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1024_s_1.41_r_162_0.6107_[0.38241097 0.9114611  0.53845507 0.989812   0.23113628].png
img: 28 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1025_s_1.63_r_315_0.5278_[0.18311861 0.7365982  0.52826595 0.9702298  0.22091426].png
img: 29 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1026_s_1.38_r_108_0.6819_[0.38658738 0.92154086 0.6346569  0.98974353 0.47680846].png
img: 30 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1027_s_1.0_r_253_0.8356_[0.40778843 0.8795263  0.9768391  0.951213   0.962865  ].png
img: 31 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1028_s_1.61_r_212_0.5595_[0.2205137  0.75966996 0.55843127 0.9785054  0.28045338].png
img: 32 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1029_s_1.53_r_354_0.4985_[0.24400187 0.78367025 0.4733506  0.98641014 0.00499105].png
img: 33 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_102_s_1.42_r_38_0.7314_[0.36624157 0.919411   0.7275991  0.98844975 0.6550763 ].png
img: 34 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1030_s_0.59_r_44_0.4221_[0.41202223 0.43568686 0.427877   0.24931788 0.5857493 ].png
img: 35 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1031_s_0.88_r_240_0.8274_[0.40807548 0.8907415  0.94240195 0.9643812  0.93139553].png
img: 36 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1032_s_0.58_r_211_0.4454_[0.4143017  0.42055723 0.53531355 0.24428944 0.6125403 ].png
img: 37 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1033_s_0.86_r_347_0.8407_[0.41569772 0.88231945 0.959953   0.99017626 0.95534503].png
img: 38 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1034_s_1.11_r_19_0.8432_[0.40165374 0.9248138  0.95493937 0.9895257  0.9452603 ].png
img: 39 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1035_s_1.45_r_230_0.6805_[0.35054448 0.8829105  0.6581185  0.9875679  0.52330756].png
img: 40 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1036_s_1.28_r_147_0.8147_[0.39265388 0.9287153  0.8867463  0.990979   0.8741841 ].png
img: 41 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1037_s_1.18_r_100_0.7807_[0.40454856 0.92780006 0.80718696 0.98970556 0.7742944 ].png
img: 42 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1038_s_0.59_r_188_0.5633_[0.4165625  0.45776352 0.8472446  0.3120629  0.7828312 ].png
img: 43 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1039_s_0.68_r_157_0.6204_[0.4472201  0.5195476  0.9398122  0.31512296 0.8802296 ].png
img: 44 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_103_s_1.4_r_124_0.7511_[0.37971848 0.92232424 0.75855225 0.990721   0.7043237 ].png
img: 45 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1040_s_1.39_r_58_0.7303_[0.3728113  0.92224205 0.72107774 0.99007666 0.6454618 ].png
img: 46 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1041_s_1.84_r_44_0.4482_[0.09532571 0.66629857 0.47814345 0.936038   0.06535174].png
img: 47 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1042_s_1.44_r_344_0.5835_[0.346592   0.8843051  0.5192101  0.98833907 0.17924947].png
img: 48 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1043_s_1.14_r_161_0.8296_[0.4035192  0.9260256  0.9162793  0.99100286 0.91101354].png
img: 49 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1044_s_1.45_r_242_0.6738_[0.3532395  0.8812315  0.64624274 0.988012   0.50009197].png
img: 50 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1045_s_1.23_r_79_0.7106_[0.39785916 0.9349564  0.67433965 0.9893773  0.5563149 ].png
img: 51 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1046_s_1.93_r_341_0.4313_[0.07233304 0.66348183 0.4681917  0.94313174 0.00939821].png
img: 52 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1047_s_0.89_r_213_0.8291_[0.40299487 0.8848977  0.9649794  0.9388487  0.9536143 ].png
img: 53 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1048_s_1.68_r_271_0.4452_[1.0786959e-01 6.7731416e-01 4.7230226e-01 9.6855962e-01 6.2793559e-05].png
img: 54 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1049_s_1.42_r_114_0.6977_[0.37347373 0.9184263  0.6641054  0.98922306 0.5432222 ].png
img: 55 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_104_s_0.97_r_163_0.8506_[0.412075   0.9058654  0.97497076 0.9912176  0.9688985 ].png
img: 56 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1050_s_1.29_r_233_0.8099_[0.38928822 0.9237066  0.8788035  0.98888177 0.8688366 ].png
img: 57 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1051_s_1.12_r_198_0.8461_[0.40470275 0.9258988  0.95660305 0.9897296  0.9537558 ].png
img: 58 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1052_s_0.55_r_129_0.3838_[0.3745556  0.41720483 0.26371577 0.35007998 0.51354754].png
img: 59 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1053_s_0.89_r_275_0.8463_[0.40715012 0.91364044 0.9654842  0.9814103  0.96381205].png
img: 60 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1054_s_0.83_r_274_0.8381_[0.41663185 0.8831127  0.96017456 0.975974   0.95474094].png
img: 61 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1055_s_1.04_r_166_0.8473_[0.4108935  0.9110706  0.9627796  0.99222684 0.95953685].png
img: 62 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1056_s_1.33_r_42_0.7684_[0.3864906  0.9236007  0.79183424 0.98604804 0.7540527 ].png
img: 63 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1057_s_1.24_r_174_0.6431_[0.4021682  0.9225149  0.5739592  0.98888963 0.32809588].png
img: 64 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1058_s_0.92_r_319_0.8471_[0.39745563 0.9349595  0.9593682  0.9852627  0.9585686 ].png
img: 65 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1059_s_1.15_r_286_0.8349_[0.40201303 0.9276756  0.9305226  0.98727053 0.927178  ].png
img: 66 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_105_s_0.6_r_54_0.4848_[0.40787596 0.4320308  0.77034914 0.08793832 0.7258632 ].png
img: 67 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1060_s_1.02_r_301_0.838_[0.4006206  0.9200035  0.944798   0.97956854 0.94493145].png
img: 68 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1061_s_1.61_r_258_0.4837_[0.19279918 0.7416951  0.48261166 0.97325015 0.02830253].png
img: 69 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1062_s_1.59_r_115_0.5506_[0.23044871 0.7779669  0.53975827 0.977706   0.22735143].png
img: 70 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1063_s_1.25_r_47_0.8115_[0.39573032 0.9388785  0.8752388  0.98964787 0.85818654].png
img: 71 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1064_s_1.5_r_303_0.6205_[0.29667217 0.83115906 0.5999274  0.98537666 0.3892333 ].png
img: 72 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1065_s_1.62_r_180_0.4585_[1.4414729e-01 6.9677365e-01 4.7421929e-01 9.7729522e-01 5.4166780e-05].png
img: 73 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1066_s_0.51_r_127_0.3195_[0.35398373 0.34589007 0.13630319 0.28842062 0.47278082].png
img: 74 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1067_s_0.61_r_325_0.4739_[0.4218755  0.4458564  0.6730023  0.13677754 0.6918717 ].png
img: 75 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1068_s_1.26_r_115_0.8196_[0.39297923 0.9351597  0.8943688  0.9897646  0.8858383 ].png
img: 76 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1069_s_1.76_r_234_0.483_[0.13770445 0.7059191  0.5018715  0.95953065 0.1101369 ].png
img: 77 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_106_s_1.7_r_297_0.5032_[0.16397525 0.7269766  0.5152263  0.95857024 0.151422  ].png
img: 78 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1070_s_1.23_r_31_0.8441_[0.3862671  0.9402089  0.96029687 0.9891149  0.94481295].png
img: 79 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1071_s_0.72_r_109_0.7134_[0.4349171  0.63766885 0.94873476 0.6326079  0.9130796 ].png
img: 80 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1072_s_1.74_r_114_0.4803_[0.14026427 0.71277463 0.49871394 0.9601374  0.08969682].png
img: 81 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1073_s_0.62_r_235_0.4869_[0.42138004 0.44731653 0.70957935 0.14926201 0.70685816].png
img: 82 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1074_s_1.38_r_164_0.6278_[0.3949119  0.92403495 0.55511475 0.99076533 0.27400613].png
img: 83 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1075_s_0.54_r_201_0.4017_[0.38233474 0.39200976 0.400382   0.29921693 0.5346439 ].png
img: 84 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1076_s_1.94_r_147_0.4302_[0.08409407 0.66632855 0.4649075  0.911259   0.02452409].png
img: 85 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1077_s_1.22_r_296_0.8307_[0.3955987  0.929735   0.9215582  0.98776305 0.91903585].png
img: 86 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1078_s_1.01_r_282_0.8478_[0.40448594 0.91969186 0.9612755  0.98693854 0.9665879 ].png
img: 87 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1079_s_1.73_r_49_0.4872_[0.13969056 0.70901495 0.50518954 0.9576874  0.12419964].png
img: 88 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_107_s_1.87_r_87_0.4255_[5.1055834e-02 6.4089137e-01 4.7026303e-01 9.6507502e-01 3.0484707e-05].png
img: 89 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1080_s_0.96_r_318_0.8384_[0.3977154  0.9353708  0.93343544 0.9875789  0.93781793].png
img: 90 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1081_s_2.0_r_137_0.3824_[5.7393536e-03 5.8825046e-01 4.3797916e-01 8.7978816e-01 9.7558383e-05].png
img: 91 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1082_s_1.85_r_230_0.4505_[0.09634202 0.6754328  0.484551   0.9357199  0.06036465].png
img: 92 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1083_s_0.86_r_250_0.8373_[0.4152519  0.88302314 0.96100575 0.9777225  0.9497427 ].png
img: 93 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1084_s_1.14_r_234_0.8429_[0.39887998 0.93111205 0.94860095 0.9871185  0.9488408 ].png
img: 94 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1085_s_1.72_r_47_0.4903_[0.1333546  0.69302875 0.510218   0.96497494 0.15005025].png
img: 95 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1086_s_1.35_r_160_0.6731_[0.39353493 0.92374337 0.61760676 0.990657   0.43993586].png
img: 96 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1087_s_1.06_r_349_0.8414_[0.40394637 0.9191659  0.94654346 0.98892075 0.9482339 ].png
img: 97 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1088_s_1.12_r_203_0.8443_[0.40231246 0.92882156 0.9524839  0.98918766 0.9487144 ].png
img: 98 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1089_s_0.79_r_312_0.6755_[0.41540146 0.62424594 0.93047345 0.48867774 0.9188686 ].png
img: 99 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_108_s_0.79_r_304_0.7146_[0.42190823 0.66241205 0.94208115 0.61864525 0.9279168 ].png
img: 100 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1090_s_1.78_r_270_0.4305_[0.06137893 0.6467521  0.47076544 0.9733639  0.        ].png
img: 101 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1091_s_0.89_r_237_0.8319_[0.4052251 0.8968598 0.9566155 0.9598347 0.9412143].png
img: 102 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1092_s_1.38_r_136_0.7274_[0.37974253 0.9197006  0.7157387  0.9906216  0.63121396].png
img: 103 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1093_s_1.09_r_274_0.8157_[0.40543786 0.92173094 0.88443875 0.9850212  0.88190436].png
img: 104 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1094_s_1.72_r_274_0.4432_[0.09921145 0.67206055 0.472785   0.9719359  0.        ].png
img: 105 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1095_s_1.12_r_141_0.8471_[0.40039152 0.9338684  0.9601316  0.98957074 0.9515752 ].png
img: 106 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1096_s_1.32_r_142_0.7878_[0.38623863 0.9278172  0.83102334 0.98814857 0.8059216 ].png
img: 107 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1097_s_1.24_r_142_0.8322_[0.39614168 0.9334742  0.92491925 0.99016523 0.9163373 ].png
img: 108 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1098_s_0.79_r_338_0.761_[0.42883542 0.7172788  0.94907856 0.77250063 0.93729967].png
img: 109 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1099_s_1.82_r_323_0.4645_[0.11327077 0.69396067 0.49090803 0.94569856 0.07871923].png
img: 110 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_109_s_0.82_r_156_0.8113_[0.41823977 0.8245525  0.9588747  0.9078584  0.9469215 ].png
img: 111 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_10_s_0.93_r_117_0.8393_[0.4066064  0.90882397 0.9572143  0.9784176  0.9454217 ].png
img: 112 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1100_s_1.09_r_357_0.7705_[0.40338704 0.9208592  0.786763   0.9883632  0.7531075 ].png
img: 113 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1101_s_1.21_r_92_0.6555_[0.3988457  0.928564   0.59056836 0.9856924  0.37379637].png
img: 114 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1102_s_1.13_r_208_0.8478_[0.40142372 0.9305532  0.964367   0.9868383  0.95596033].png
img: 115 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1103_s_1.41_r_128_0.7319_[0.36519247 0.91109455 0.7313676  0.98859894 0.6634496 ].png
img: 116 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1104_s_1.79_r_75_0.4464_[0.10675516 0.6902401  0.47296813 0.95518684 0.0070088 ].png
img: 117 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1105_s_1.44_r_198_0.6299_[0.36227238 0.88825834 0.576348   0.98562104 0.33704644].png
img: 118 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1106_s_1.3_r_30_0.8053_[0.3802604  0.93044645 0.8701598  0.9897112  0.8560534 ].png
img: 119 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1107_s_1.87_r_58_0.4483_[0.10196196 0.6838202  0.47775593 0.93517804 0.04280669].png
img: 120 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1108_s_1.71_r_70_0.4777_[0.15676309 0.7282403  0.48770997 0.96058816 0.05526274].png
img: 121 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1109_s_0.87_r_215_0.821_[0.4012585  0.8972084  0.93435484 0.9505363  0.92153335].png
img: 122 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_110_s_1.07_r_29_0.8492_[0.3929146 0.9447511 0.9643794 0.9880887 0.9557245].png
img: 123 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1110_s_0.83_r_65_0.7806_[0.41793036 0.7746306  0.9473278  0.8375759  0.92560613].png
img: 124 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1111_s_1.25_r_312_0.8143_[0.3951653  0.93310106 0.8782243  0.9897176  0.8753732 ].png
img: 125 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1112_s_0.81_r_322_0.7158_[0.4204718  0.6724953  0.9336126  0.62546116 0.9270637 ].png
img: 126 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1113_s_0.57_r_116_0.4596_[0.39405745 0.4076982  0.6575933  0.15698543 0.6819072 ].png
img: 127 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1114_s_1.59_r_36_0.5749_[0.23032704 0.77839226 0.5701106  0.9802158  0.3153475 ].png
img: 128 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1115_s_0.84_r_204_0.8132_[0.40971392 0.8534967  0.9493637  0.92289346 0.93033975].png
img: 129 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1116_s_1.13_r_163_0.8262_[0.4061452  0.9255553  0.90847206 0.9911821  0.8996961 ].png
img: 130 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1117_s_1.3_r_147_0.7968_[0.3858009  0.92157847 0.848937   0.9899351  0.8377286 ].png
img: 131 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1118_s_0.96_r_90_0.8483_[0.40767652 0.9129256  0.97180796 0.9863285  0.9625888 ].png
img: 132 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1119_s_1.9_r_95_0.4229_[0.04740995 0.6396825  0.46855783 0.9588888  0.        ].png
img: 133 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_111_s_1.1_r_240_0.8439_[0.40203178 0.9266818  0.9531337  0.98654276 0.95112526].png
img: 134 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1120_s_1.34_r_165_0.6514_[0.39740524 0.92157674 0.5877656  0.99186003 0.35815305].png
img: 135 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1121_s_1.82_r_48_0.4556_[0.10355903 0.6789148  0.4813851  0.94487584 0.06919459].png
img: 136 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1122_s_1.81_r_67_0.4533_[0.11731776 0.7015634  0.47531578 0.9433748  0.02905401].png
img: 137 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1123_s_1.16_r_183_0.7036_[0.40422556 0.92240685 0.6630341  0.98616064 0.54233295].png
img: 138 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1124_s_1.5_r_20_0.5748_[0.29691833 0.8312679  0.5371672  0.9839972  0.22476552].png
img: 139 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1125_s_1.48_r_4_0.5154_[0.2812508  0.815867   0.47559556 0.9852141  0.01925014].png
img: 140 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1126_s_1.92_r_146_0.4333_[0.0862077  0.6653286  0.46613464 0.91645056 0.03249969].png
img: 141 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1127_s_1.37_r_179_0.5656_[0.38947544 0.90862626 0.4887253  0.98672795 0.05451551].png
img: 142 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1128_s_0.86_r_170_0.8472_[0.41648343 0.8928087  0.97188795 0.9902006  0.9648069 ].png
img: 143 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1129_s_1.92_r_111_0.4271_[0.07850733 0.65715253 0.46455055 0.9190882  0.01618712].png
img: 144 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_112_s_1.83_r_147_0.4571_[0.11215803 0.6876115  0.48765475 0.9475607  0.05060325].png
img: 145 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1130_s_1.83_r_89_0.4266_[5.5075049e-02 6.4289212e-01 4.7015896e-01 9.6489054e-01 1.0625412e-04].png
img: 146 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1131_s_0.61_r_83_0.5782_[0.43956423 0.4524368  0.9124336  0.2515787  0.8350796 ].png
img: 147 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1132_s_1.25_r_100_0.7035_[0.4020661  0.9230285  0.66403383 0.9875665  0.5408874 ].png
img: 148 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1133_s_1.55_r_346_0.5166_[0.24623294 0.79095304 0.49090967 0.9800344  0.0751103 ].png
img: 149 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1134_s_1.67_r_59_0.5129_[0.18566754 0.7510518  0.51343447 0.96631974 0.14820021].png
img: 150 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1135_s_0.79_r_96_0.8336_[0.42009407 0.8596136  0.96630096 0.9715932  0.9502523 ].png
img: 151 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1136_s_1.62_r_120_0.5471_[0.21595067 0.765632   0.5449575  0.9792807  0.22984697].png
img: 152 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1137_s_0.97_r_14_0.8474_[0.40484703 0.9136888  0.96988654 0.9894807  0.95900977].png
img: 153 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1138_s_1.08_r_80_0.8377_[0.4040208  0.921686   0.9418867  0.98884434 0.9322587 ].png
img: 154 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1139_s_0.62_r_267_0.6093_[0.43154585 0.49768946 0.92719066 0.32668144 0.86347646].png
img: 155 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_113_s_0.8_r_173_0.8414_[0.4210932  0.8741065  0.96695685 0.98769486 0.9573128 ].png
img: 156 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1140_s_1.03_r_169_0.8496_[0.40943122 0.91075224 0.9722143  0.989479   0.96610725].png
img: 157 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1141_s_1.61_r_53_0.5545_[0.21350503 0.7627642  0.5538505  0.97511643 0.26720682].png
img: 158 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1142_s_1.9_r_196_0.4298_[0.07067963 0.65478003 0.47355908 0.94494194 0.00489699].png
img: 159 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1143_s_1.03_r_273_0.8384_[0.40691257 0.9152514  0.9418431  0.98431975 0.94384915].png
img: 160 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1144_s_0.83_r_228_0.7885_[0.41319847 0.79346824 0.9562096  0.8383047  0.94119394].png
img: 161 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1145_s_1.42_r_150_0.7093_[0.37137437 0.9006841  0.69163114 0.9905066  0.59246844].png
img: 162 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1146_s_0.51_r_45_0.3303_[0.362      0.34143057 0.23375584 0.25423494 0.46006054].png
img: 163 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1147_s_1.86_r_353_0.427_[6.2718689e-02 6.5165710e-01 4.6603063e-01 9.5417309e-01 6.0527097e-04].png
img: 164 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1148_s_1.23_r_131_0.8274_[0.38884968 0.9374032  0.91589856 0.99004894 0.90501624].png
img: 165 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1149_s_1.81_r_53_0.4648_[0.11396336 0.6938171  0.48965332 0.9407131  0.08607645].png
img: 166 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_114_s_1.13_r_150_0.8472_[0.40070787 0.9240529  0.96145713 0.9902576  0.95941925].png
img: 167 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1150_s_1.83_r_149_0.4572_[0.12084151 0.6965913  0.47854856 0.9396123  0.05045721].png
img: 168 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1151_s_1.44_r_295_0.6934_[0.36706394 0.90246135 0.6648412  0.9881815  0.54467183].png
img: 169 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1152_s_1.47_r_249_0.5861_[0.3358186  0.85670614 0.5350384  0.98513573 0.21765506].png
img: 170 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1153_s_1.78_r_340_0.4564_[0.12159529 0.7069466  0.47917292 0.95126647 0.0228752 ].png
img: 171 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1154_s_1.44_r_267_0.5318_[0.32589468 0.852676   0.47711697 0.98442996 0.01894167].png
img: 172 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1155_s_1.77_r_48_0.4721_[0.12313082 0.6973067  0.497548   0.95113933 0.09121438].png
img: 173 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1156_s_1.99_r_47_0.4051_[0.06247754 0.6227503  0.4401549  0.8603597  0.03984328].png
img: 174 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1157_s_1.03_r_26_0.8413_[0.39925015 0.921686   0.95637476 0.97981364 0.9493679 ].png
img: 175 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1158_s_0.99_r_59_0.8327_[0.39854962 0.9139317  0.94061685 0.9817607  0.9284859 ].png
img: 176 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1159_s_0.99_r_306_0.8143_[0.39743993 0.93254614 0.8744202  0.981569   0.8856398 ].png
img: 177 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_115_s_1.47_r_289_0.6179_[0.34053603 0.86741453 0.57118595 0.9839622  0.32664573].png
img: 178 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1160_s_0.87_r_190_0.8434_[0.4110338 0.899112  0.9668685 0.9813613 0.9587474].png
img: 179 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1161_s_0.91_r_135_0.8469_[0.40319178 0.92111534 0.968069   0.979509   0.9625293 ].png
img: 180 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1162_s_1.05_r_52_0.8455_[0.39612174 0.9355131  0.9596763  0.9866152  0.94945306].png
img: 181 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1163_s_1.22_r_44_0.821_[0.39376894 0.93831253 0.8970168  0.98977053 0.8861021 ].png
img: 182 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1164_s_1.88_r_95_0.4232_[0.05123927 0.6428274  0.4674383  0.9546095  0.        ].png
img: 183 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1165_s_1.36_r_176_0.58_[0.39368197 0.9155707  0.50135154 0.9880437  0.10136792].png
img: 184 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1166_s_1.29_r_90_0.5931_[0.39833555 0.9251438  0.5125214  0.98648447 0.14296673].png
img: 185 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1167_s_1.89_r_99_0.4242_[5.5563159e-02 6.4545143e-01 4.6686855e-01 9.5287883e-01 8.9366389e-05].png
img: 186 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1168_s_1.39_r_162_0.6397_[0.3862115  0.9152986  0.5756853  0.98837435 0.33292457].png
img: 187 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1169_s_1.18_r_296_0.8439_[0.39847323 0.9327126  0.9505872  0.9879733  0.9497685 ].png
img: 188 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_116_s_1.27_r_184_0.6352_[0.401728   0.921191   0.56498706 0.98751014 0.30051222].png
img: 189 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1170_s_0.92_r_313_0.8392_[0.39748418 0.9348969  0.9367978  0.9830395  0.94370663].png
img: 190 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1171_s_0.73_r_198_0.7034_[0.43635723 0.624027   0.9537564  0.5879189  0.91518354].png
img: 191 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1172_s_0.83_r_172_0.8445_[0.42025524 0.8806338  0.9690665  0.9890608  0.9637024 ].png
img: 192 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1173_s_1.27_r_185_0.6352_[0.40198806 0.9233872  0.5625458  0.98694634 0.3011158 ].png
img: 193 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1174_s_1.27_r_252_0.7059_[0.4010369  0.9254367  0.66539246 0.98705155 0.55062807].png
img: 194 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1175_s_0.77_r_195_0.7877_[0.4323862  0.76079965 0.9584956  0.85721993 0.92944765].png
img: 195 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1176_s_1.08_r_70_0.8391_[0.40292054 0.9222218  0.94689786 0.9893375  0.9343633 ].png
img: 196 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1177_s_1.75_r_297_0.48_[0.13720742 0.7082246  0.5002249  0.9595624  0.09457991].png
img: 197 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1178_s_1.75_r_11_0.4467_[0.10859231 0.6895406  0.4714465  0.95980006 0.00427311].png
img: 198 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1179_s_1.66_r_251_0.484_[0.18456286 0.7365839  0.48518798 0.96597075 0.0478138 ].png
img: 199 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_117_s_1.0_r_95_0.8594_[0.40739626 0.9276444  0.9855663  0.9934439  0.98282194].png
img: 200 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1180_s_0.68_r_194_0.6599_[0.44591606 0.5536145  0.95601964 0.46802458 0.8760596 ].png
img: 201 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1181_s_1.45_r_275_0.532_[0.31197125 0.8364466  0.4843928  0.985007   0.04206168].png
img: 202 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1182_s_1.82_r_79_0.4367_[8.3302408e-02 6.7075270e-01 4.6946070e-01 9.5989877e-01 1.1813983e-04].png
img: 203 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1183_s_1.86_r_47_0.4414_[0.08582091 0.65471166 0.47004297 0.93102485 0.06544795].png
img: 204 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1184_s_1.16_r_300_0.8484_[0.39475995 0.93358016 0.96365476 0.98682576 0.96339625].png
img: 205 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1185_s_1.79_r_240_0.4661_[0.12947407 0.7017692  0.49008808 0.9444223  0.06472399].png
img: 206 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1186_s_0.93_r_87_0.8462_[0.4103565  0.90163124 0.9730237  0.9849085  0.9613022 ].png
img: 207 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1187_s_0.95_r_185_0.8503_[0.4104933  0.90992534 0.9749684  0.98753667 0.9686513 ].png
img: 208 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1188_s_1.33_r_33_0.7926_[0.3843298  0.9276209  0.84203595 0.9898198  0.8192857 ].png
img: 209 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1189_s_1.81_r_114_0.4581_[0.11340977 0.6917718  0.48350325 0.9443929  0.05745421].png
img: 210 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_118_s_1.67_r_119_0.5182_[0.17673412 0.7437601  0.52594733 0.95936877 0.18543239].png
img: 211 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1190_s_1.68_r_184_0.4508_[1.2103283e-01 6.8237877e-01 4.7522765e-01 9.7514081e-01 3.7687969e-05].png
img: 212 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1191_s_0.99_r_35_0.8158_[0.3945001  0.932896   0.8845686  0.98414695 0.883081  ].png
img: 213 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1192_s_1.29_r_29_0.8163_[0.38545853 0.9288867  0.8958054  0.98928076 0.8822786 ].png
img: 214 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1193_s_1.88_r_137_0.4348_[0.08326024 0.6458414  0.46502662 0.9296376  0.05040025].png
img: 215 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1194_s_1.21_r_32_0.8415_[0.38499302 0.9418291  0.95155483 0.9871695  0.94198555].png
img: 216 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1195_s_0.73_r_209_0.6692_[0.42547277 0.5904958  0.9558907  0.44202754 0.9319405 ].png
img: 217 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1196_s_0.7_r_82_0.7136_[0.4474136  0.6238013  0.94912267 0.6325064  0.91498333].png
img: 218 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1197_s_1.45_r_255_0.5809_[0.34652814 0.87729377 0.5204552  0.9873672  0.17280881].png
img: 219 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1198_s_1.25_r_121_0.8326_[0.3904787  0.9296596  0.9303558  0.9915957  0.92096645].png
img: 220 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1199_s_1.39_r_154_0.7135_[0.3841937  0.91806734 0.6859865  0.9893768  0.5896303 ].png
img: 221 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_119_s_0.7_r_115_0.6102_[0.43291828 0.5233432  0.9387124  0.26571816 0.89029896].png
img: 222 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_11_s_1.41_r_74_0.6028_[0.37862116 0.91894066 0.5295228  0.9870903  0.1998506 ].png
img: 223 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1200_s_0.99_r_324_0.8147_[0.3982138  0.91252124 0.8869772  0.96724224 0.9084587 ].png
img: 224 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1201_s_1.08_r_57_0.8477_[0.39941075 0.9288376  0.97107476 0.98746526 0.9519448 ].png
img: 225 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1202_s_1.21_r_359_0.6504_[0.39807484 0.9339026  0.57979506 0.9901872  0.35015774].png
img: 226 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1203_s_1.79_r_335_0.4602_[0.12352344 0.704129   0.48332277 0.9540359  0.03622932].png
img: 227 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1204_s_0.59_r_107_0.4802_[0.4084908  0.4419518  0.6136802  0.27814332 0.6587535 ].png
img: 228 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1205_s_1.26_r_345_0.7054_[0.3943025  0.9396203  0.6611886  0.9894062  0.54267955].png
img: 229 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1206_s_1.54_r_351_0.4989_[0.23877563 0.77874327 0.47650322 0.98249674 0.01788976].png
img: 230 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1207_s_1.81_r_252_0.447_[0.10815423 0.6912274  0.47516605 0.94705695 0.0136016 ].png
img: 231 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1208_s_1.05_r_81_0.8446_[0.40360153 0.9238506  0.95892537 0.9886909  0.94796   ].png
img: 232 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1209_s_0.75_r_104_0.7619_[0.43794367 0.70507526 0.961407   0.77600735 0.92915076].png
img: 233 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_120_s_0.79_r_69_0.7842_[0.42217088 0.7647752  0.9536556  0.84906524 0.931337  ].png
img: 234 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1210_s_1.63_r_232_0.5338_[0.20330216 0.75721407 0.53558475 0.96164715 0.21106626].png
img: 235 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1211_s_1.91_r_344_0.427_[6.3857943e-02 6.6010374e-01 4.6613681e-01 9.4435370e-01 6.3370122e-04].png
img: 236 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1212_s_1.41_r_272_0.5511_[0.36336154 0.8882005  0.48159322 0.985721   0.03640042].png
img: 237 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1213_s_0.81_r_275_0.8388_[0.41145673 0.89564943 0.9567107  0.9782456  0.9518924 ].png
img: 238 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1214_s_1.99_r_73_0.4142_[0.05717389 0.64618915 0.45399043 0.91265833 0.00102238].png
img: 239 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1215_s_1.67_r_101_0.4672_[0.15658137 0.72101665 0.47658196 0.9697984  0.01224614].png
img: 240 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1216_s_1.85_r_286_0.4384_[0.0852043  0.6704241  0.4729489  0.95374984 0.00955692].png
img: 241 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1217_s_1.24_r_120_0.8313_[0.39004865 0.9327442  0.92956626 0.9886161  0.9152785 ].png
img: 242 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1218_s_1.72_r_94_0.4441_[0.09937607 0.67340636 0.4736855  0.97404355 0.        ].png
img: 243 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1219_s_1.58_r_346_0.4998_[0.2139381  0.7614521  0.48797855 0.9753198  0.06024697].png
img: 244 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_121_s_1.1_r_134_0.8527_[0.39894238 0.9427338  0.96988195 0.98803896 0.9638676 ].png
img: 245 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1220_s_1.14_r_198_0.8405_[0.4042304  0.92700833 0.94133717 0.9890928  0.9408435 ].png
img: 246 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1221_s_0.98_r_125_0.84_[0.40254593 0.91859365 0.95176953 0.9810973  0.9461333 ].png
img: 247 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1222_s_1.0_r_177_0.861_[0.4097843  0.9255245  0.98639274 0.996188   0.98698515].png
img: 248 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1223_s_1.06_r_133_0.851_[0.4023961  0.93041784 0.97073776 0.9866652  0.964652  ].png
img: 249 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1224_s_1.62_r_207_0.5373_[0.20500046 0.7488418  0.53856844 0.9745551  0.21976541].png
img: 250 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1225_s_0.95_r_102_0.8517_[0.40557784 0.91823846 0.9815917  0.98658556 0.9662653 ].png
img: 251 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1226_s_1.56_r_280_0.4957_[0.23008908 0.767048   0.47915706 0.97774386 0.02427717].png
img: 252 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1227_s_1.42_r_195_0.6252_[0.3730543  0.8993873  0.56268626 0.9885166  0.3023985 ].png
img: 253 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1228_s_1.69_r_177_0.448_[0.11289454 0.68179125 0.47398877 0.97114867 0.        ].png
img: 254 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1229_s_1.71_r_311_0.4963_[0.14119613 0.70413345 0.51176363 0.9682923  0.15593742].png
img: 255 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_122_s_1.68_r_63_0.4984_[0.17775011 0.7389713  0.5038985  0.963872   0.10774149].png
img: 256 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1230_s_0.76_r_141_0.6737_[0.41946217 0.6048661  0.953818   0.4623513  0.9280679 ].png
img: 257 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1231_s_0.73_r_207_0.6482_[0.42673168 0.573957   0.9381458  0.38937017 0.9130354 ].png
img: 258 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1232_s_0.69_r_101_0.6932_[0.436651   0.6052677  0.96083885 0.5587284  0.9047292 ].png
img: 259 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1233_s_1.01_r_127_0.8348_[0.3971243  0.9313494  0.9339846  0.97817945 0.93337286].png
img: 260 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1234_s_1.29_r_157_0.7611_[0.39566106 0.9214626  0.772154   0.99021876 0.72623295].png
img: 261 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1235_s_0.77_r_240_0.7112_[0.4259175 0.652186  0.9455774 0.6175945 0.9148627].png
img: 262 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1236_s_0.58_r_336_0.4735_[0.4138535  0.42201498 0.6716832  0.19651702 0.66321325].png
img: 263 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1237_s_1.71_r_53_0.5_[0.1537522  0.725924   0.5134827  0.9606315  0.14615385].png
img: 264 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1238_s_1.03_r_144_0.8441_[0.40074098 0.9280276  0.958739   0.9853178  0.9477721 ].png
img: 265 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1239_s_1.54_r_157_0.5546_[0.27804744 0.80406904 0.5243794  0.9849072  0.1817381 ].png
img: 266 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_123_s_0.88_r_271_0.844_[0.41134113 0.90146315 0.9635908  0.9828878  0.96075284].png
img: 267 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1240_s_1.5_r_325_0.6086_[0.29411945 0.8320943  0.5826552  0.9851179  0.34914416].png
img: 268 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1241_s_0.95_r_126_0.8458_[0.3993954  0.9241057  0.9669849  0.9797724  0.95886755].png
img: 269 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1242_s_0.89_r_48_0.8287_[0.3952499  0.9309491  0.92312473 0.98056275 0.9138298 ].png
img: 270 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1243_s_1.22_r_312_0.8343_[0.39597237 0.93388027 0.9291886  0.98844117 0.92425096].png
img: 271 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1244_s_0.52_r_151_0.3409_[0.39525163 0.34785137 0.35348192 0.11347988 0.4942597 ].png
img: 272 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1245_s_0.96_r_201_0.8458_[0.4072989  0.9120771  0.9660989  0.98329514 0.959982  ].png
img: 273 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1246_s_1.08_r_224_0.8482_[0.40184382 0.92770463 0.96520585 0.9868207  0.9592026 ].png
img: 274 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1247_s_1.23_r_120_0.8343_[0.38737804 0.9307645  0.93742794 0.9890001  0.9270809 ].png
img: 275 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1248_s_0.64_r_258_0.6169_[0.43855944 0.50327057 0.9255368  0.3680625  0.8489394 ].png
img: 276 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1249_s_1.6_r_84_0.4765_[1.8733379e-01 7.4050081e-01 4.7360435e-01 9.8069167e-01 5.8176578e-04].png
img: 277 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_124_s_0.66_r_193_0.6554_[0.4381518  0.55445784 0.95032245 0.4491376  0.88506424].png
img: 278 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1250_s_1.84_r_50_0.4515_[0.09734841 0.6756069  0.48022562 0.9366879  0.06779253].png
img: 279 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1251_s_1.99_r_283_0.4123_[0.04689388 0.62690514 0.4594678  0.92161286 0.0065265 ].png
img: 280 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1252_s_1.31_r_82_0.6239_[0.3960541  0.93004286 0.54833573 0.9877484  0.25722525].png
img: 281 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1253_s_0.77_r_51_0.6374_[0.42940992 0.5544728  0.94374007 0.34411854 0.91512233].png
img: 282 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1254_s_1.65_r_255_0.4782_[0.17426974 0.7283067  0.48282748 0.9715314  0.03400341].png
img: 283 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1255_s_1.1_r_281_0.8341_[0.40180588 0.9306699  0.92361695 0.9836966  0.93051106].png
img: 284 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1256_s_1.6_r_186_0.4749_[0.18893123 0.73172337 0.4742929  0.97642595 0.00320264].png
img: 285 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1257_s_0.73_r_161_0.7276_[0.4365754  0.6594118  0.94933033 0.67431253 0.9183597 ].png
img: 286 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1258_s_1.46_r_277_0.538_[0.30867216 0.8341856  0.4915236  0.9829443  0.07246497].png
img: 287 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1259_s_0.73_r_226_0.6107_[0.4229268  0.5356529  0.9362476  0.25733477 0.9014318 ].png
img: 288 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_125_s_1.9_r_59_0.4418_[0.09743551 0.681033   0.46694    0.92477876 0.03882769].png
img: 289 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1260_s_1.67_r_213_0.5199_[0.17470208 0.7354823  0.5308709  0.96196365 0.19667186].png
img: 290 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1261_s_1.6_r_324_0.5588_[0.21958987 0.77140963 0.5537864  0.9764899  0.27262804].png
img: 291 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1262_s_0.94_r_28_0.8406_[0.3966288  0.92724115 0.9547116  0.9806239  0.94374496].png
img: 292 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1263_s_1.5_r_179_0.4929_[2.3813617e-01 7.6779646e-01 4.7409454e-01 9.8446840e-01 2.5259302e-04].png
img: 293 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1264_s_1.78_r_71_0.456_[0.11900478 0.7008734  0.4775849  0.9564613  0.02605053].png
img: 294 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1265_s_0.6_r_251_0.4854_[0.4216608  0.43892026 0.69398963 0.19025545 0.68227977].png
img: 295 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1266_s_1.35_r_298_0.7718_[0.38891885 0.92537385 0.793213   0.98842454 0.7630314 ].png
img: 296 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1267_s_1.36_r_285_0.6641_[0.38980156 0.91752    0.6065197  0.9870609  0.41969988].png
img: 297 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1268_s_1.98_r_340_0.421_[0.06469427 0.6563526  0.4584422  0.9152086  0.0101011 ].png
img: 298 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1269_s_1.17_r_93_0.7003_[0.40170303 0.9309976  0.6545786  0.9849421  0.5291763 ].png
img: 299 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_126_s_0.69_r_119_0.5906_[0.42472345 0.5044812  0.93704295 0.19481447 0.89185905].png
img: 300 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1270_s_0.7_r_358_0.7204_[0.43831423 0.6400902  0.95261616 0.6497834  0.9210544 ].png
img: 301 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1271_s_1.85_r_176_0.426_[0.05527533 0.64386547 0.46975192 0.9610337  0.        ].png
img: 302 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1272_s_1.0_r_155_0.7277_[0.40206033 0.7421248  0.8584118  0.7715467  0.86448437].png
img: 303 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1273_s_1.4_r_103_0.6305_[0.38613808 0.91403514 0.56409425 0.9873895  0.30063674].png
img: 304 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1274_s_1.9_r_145_0.4402_[0.093574   0.6680718  0.46975845 0.9241528  0.0452242 ].png
img: 305 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1275_s_0.99_r_30_0.8153_[0.3954231  0.9223715  0.89196485 0.97481406 0.89178604].png
img: 306 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1276_s_1.7_r_300_0.5034_[0.16366553 0.72800666 0.5155555  0.95880455 0.15117304].png
img: 307 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1277_s_1.72_r_17_0.4667_[0.13855933 0.713179   0.48270375 0.9592085  0.03960479].png
img: 308 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1278_s_1.88_r_70_0.4388_[0.0890152  0.6790175  0.47040996 0.94450414 0.01095404].png
img: 309 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1279_s_0.72_r_131_0.5958_[0.43270993 0.52828234 0.8900022  0.2811234  0.8468857 ].png
img: 310 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_127_s_1.41_r_78_0.5891_[0.37799385 0.9186489  0.51291823 0.98711616 0.14889637].png
img: 311 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1280_s_1.52_r_144_0.618_[0.29322514 0.82821214 0.5984585  0.9812003  0.38879117].png
img: 312 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1281_s_0.93_r_55_0.8293_[0.40518326 0.8866594  0.9512547  0.96620226 0.9371079 ].png
img: 313 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1282_s_1.5_r_212_0.6234_[0.2954337  0.82694757 0.60616326 0.9849507  0.403627  ].png
img: 314 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1283_s_1.76_r_57_0.4853_[0.13970883 0.71647084 0.5040815  0.95511484 0.11094865].png
img: 315 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1284_s_1.04_r_246_0.843_[0.4072054  0.9089404  0.9579367  0.98595446 0.95498145].png
img: 316 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1285_s_0.51_r_195_0.3643_[0.3568094  0.34792814 0.33346552 0.29194883 0.49142167].png
img: 317 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1286_s_0.8_r_101_0.8342_[0.4150768  0.87406766 0.9686019  0.9759087  0.937457  ].png
img: 318 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1287_s_0.99_r_345_0.844_[0.40694168 0.90564746 0.95992804 0.9881601  0.95926017].png
img: 319 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1288_s_1.9_r_255_0.4297_[7.3285341e-02 6.6106921e-01 4.6906695e-01 9.4466627e-01 4.1319468e-04].png
img: 320 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1289_s_0.95_r_272_0.8484_[0.40704396 0.9123187  0.97130054 0.9839635  0.96728504].png
img: 321 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_128_s_0.94_r_234_0.8415_[0.40319923 0.9211739  0.9513105  0.98423684 0.9478281 ].png
img: 322 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1290_s_1.05_r_153_0.8484_[0.40338096 0.9264842  0.96367365 0.9893989  0.9590396 ].png
img: 323 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1291_s_0.78_r_41_0.6555_[0.4187465  0.5929265  0.92770857 0.43829086 0.8996673 ].png
img: 324 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1292_s_1.67_r_2_0.4501_[0.1164386  0.6900078  0.46978086 0.9740601  0.        ].png
img: 325 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1293_s_1.78_r_67_0.4607_[0.12810853 0.7081399  0.48006332 0.9561261  0.0309797 ].png
img: 326 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1294_s_1.06_r_220_0.8419_[0.40148875 0.92592543 0.95025706 0.98665994 0.9453429 ].png
img: 327 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1295_s_1.17_r_82_0.758_[0.4006476  0.9313435  0.75901616 0.98843944 0.71041626].png
img: 328 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1296_s_0.95_r_124_0.8432_[0.40103295 0.91983825 0.9631499  0.97999483 0.9521553 ].png
img: 329 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1297_s_1.2_r_0_0.6324_[0.39814836 0.9303681  0.55584425 0.9879003  0.28977787].png
img: 330 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1298_s_0.91_r_342_0.846_[0.4057112  0.91015655 0.9606303  0.9889025  0.964696  ].png
img: 331 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1299_s_0.56_r_190_0.4419_[0.38926467 0.38023207 0.5975524  0.20359795 0.6386802 ].png
img: 332 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_129_s_1.44_r_203_0.6663_[0.36358622 0.8905925  0.6253875  0.98807544 0.46403942].png
img: 333 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_12_s_1.92_r_195_0.4236_[0.06416479 0.6442924  0.4668706  0.940702   0.00216531].png
img: 334 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1300_s_1.38_r_112_0.7117_[0.38800153 0.92934805 0.67856103 0.9887201  0.5739524 ].png
img: 335 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1301_s_0.92_r_294_0.8426_[0.40102544 0.9252318  0.9557716  0.9791902  0.9516396 ].png
img: 336 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1302_s_0.76_r_75_0.7766_[0.43186536 0.7361869  0.9540747  0.8387596  0.9222801 ].png
img: 337 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1303_s_1.34_r_189_0.6207_[0.39764962 0.92078376 0.5446733  0.9874908  0.2527034 ].png
img: 338 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1304_s_1.0_r_280_0.8567_[0.40681994 0.92243457 0.9845664  0.9907148  0.9790322 ].png
img: 339 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1305_s_0.57_r_108_0.4352_[0.3922908  0.41939005 0.50784814 0.25605306 0.6005549 ].png
img: 340 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1306_s_1.77_r_312_0.4747_[0.11894072 0.6896888  0.5007263  0.9510558  0.11331147].png
img: 341 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1307_s_1.43_r_127_0.7214_[0.3622653  0.9012886  0.71770555 0.99096483 0.6346124 ].png
img: 342 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1308_s_1.07_r_109_0.85_[0.40047    0.93354154 0.9702567  0.9861632  0.9594079 ].png
img: 343 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1309_s_1.28_r_208_0.8194_[0.3934822  0.9272042  0.89574426 0.9899546  0.8908163 ].png
img: 344 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_130_s_1.49_r_158_0.5777_[0.3224563  0.84651566 0.5306753  0.9894221  0.1996014 ].png
img: 345 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1310_s_0.69_r_31_0.6057_[0.4195645  0.5243142  0.9367843  0.26425883 0.8833996 ].png
img: 346 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1311_s_1.69_r_215_0.5093_[0.15922593 0.7239446  0.52506053 0.9629493  0.17556731].png
img: 347 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1312_s_0.92_r_13_0.8489_[0.39734507 0.9328977  0.9668528  0.9875889  0.95980066].png
img: 348 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1313_s_0.59_r_311_0.4556_[0.4043443  0.42995134 0.57689446 0.24371423 0.62300426].png
img: 349 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1314_s_0.66_r_23_0.5993_[0.41981465 0.51282    0.9229156  0.2727535  0.86834854].png
img: 350 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1315_s_0.89_r_146_0.8237_[0.40765306 0.87465346 0.9544214  0.9350541  0.94657505].png
img: 351 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1316_s_0.52_r_296_0.4061_[0.3599984  0.39462677 0.37385046 0.36675444 0.53505564].png
img: 352 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1317_s_1.7_r_45_0.4887_[0.1442888  0.7090276  0.5026786  0.95538396 0.13200891].png
img: 353 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1318_s_0.63_r_20_0.5544_[0.42010254 0.502085   0.7771364  0.33965674 0.7329728 ].png
img: 354 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1319_s_0.73_r_2_0.7719_[0.4289191  0.73472756 0.9489398  0.8133973  0.93355715].png
img: 355 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_131_s_0.6_r_153_0.4854_[0.433403   0.41976282 0.7881874  0.02403774 0.7615853 ].png
img: 356 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1320_s_1.58_r_227_0.5612_[0.22349721 0.76       0.55657053 0.9803151  0.28561494].png
img: 357 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1321_s_1.56_r_292_0.563_[0.2549756  0.79219985 0.5437889  0.9771578  0.24708435].png
img: 358 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1322_s_1.45_r_287_0.6184_[0.35421467 0.8824359  0.5635607  0.98345244 0.30831835].png
img: 359 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1323_s_1.56_r_50_0.5781_[0.24115755 0.7863692  0.571732   0.9798677  0.3112244 ].png
img: 360 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1324_s_1.53_r_345_0.5278_[0.26761723 0.8086987  0.49447668 0.9803329  0.08786472].png
img: 361 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1325_s_1.8_r_98_0.4379_[8.2745813e-02 6.6714454e-01 4.7240359e-01 9.6718770e-01 1.0964672e-04].png
img: 362 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1326_s_1.5_r_126_0.634_[0.29231274 0.82702523 0.6224217  0.9874514  0.44078007].png
img: 363 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1327_s_0.96_r_110_0.8485_[0.4015302  0.9235189  0.97302854 0.98276895 0.9615052 ].png
img: 364 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1328_s_0.97_r_289_0.8455_[0.4039589  0.92162716 0.963976   0.9822514  0.9557503 ].png
img: 365 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1329_s_0.58_r_255_0.4695_[0.4078686  0.4119802  0.6159696  0.28888535 0.6226084 ].png
img: 366 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_132_s_1.03_r_248_0.8449_[0.4056124  0.9139225  0.96287835 0.98637223 0.9558478 ].png
img: 367 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1330_s_1.12_r_231_0.8461_[0.4001852  0.9294018  0.95725274 0.9879522  0.955784  ].png
img: 368 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1331_s_0.88_r_82_0.8442_[0.4106538  0.8976023  0.972568   0.98521906 0.95518196].png
img: 369 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1332_s_1.24_r_52_0.8291_[0.3915607 0.93126   0.922597  0.9895615 0.9106789].png
img: 370 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1333_s_1.32_r_103_0.6839_[0.39359078 0.9310893  0.63253736 0.9881377  0.4741456 ].png
img: 371 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1334_s_0.54_r_136_0.3511_[0.37658864 0.37759137 0.20199265 0.32919484 0.46993518].png
img: 372 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1335_s_0.97_r_16_0.8475_[0.40349075 0.91506106 0.9697092  0.9886791  0.96037304].png
img: 373 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1336_s_1.62_r_310_0.5519_[0.19993426 0.75188875 0.55280524 0.9756177  0.27901927].png
img: 374 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1337_s_1.51_r_208_0.6342_[0.30316955 0.83158976 0.61638623 0.9864532  0.4332005 ].png
img: 375 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1338_s_0.78_r_313_0.7108_[0.4147657  0.66885024 0.9383596  0.60745645 0.92475116].png
img: 376 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1339_s_1.71_r_90_0.4418_[0.08942886 0.6684581  0.47414336 0.9771376  0.        ].png
img: 377 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_133_s_1.0_r_66_0.7412_[0.4029275  0.7667272  0.8538971  0.80419004 0.87846   ].png
img: 378 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1340_s_1.93_r_218_0.4293_[0.08121481 0.6527685  0.46747458 0.8964105  0.04865853].png
img: 379 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1341_s_1.08_r_25_0.8449_[0.39934242 0.925996   0.96298224 0.98688734 0.9495    ].png
img: 380 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1342_s_0.79_r_19_0.7947_[0.4158876  0.7991633  0.94911546 0.8840347  0.9250886 ].png
img: 381 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1343_s_1.12_r_226_0.8419_[0.39951843 0.9304169  0.9481788  0.9873593  0.9440523 ].png
img: 382 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1344_s_0.65_r_342_0.6118_[0.4429873  0.5127397  0.89455026 0.3912566  0.81744844].png
img: 383 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1345_s_1.99_r_191_0.4136_[0.04584373 0.6281125  0.4612803  0.92270017 0.00990658].png
img: 384 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1346_s_1.5_r_325_0.6086_[0.29411945 0.8320943  0.5826552  0.9851179  0.34914416].png
img: 385 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1347_s_1.09_r_15_0.8437_[0.40100327 0.92642856 0.95563495 0.9894941  0.9458479 ].png
img: 386 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1348_s_1.65_r_180_0.4523_[0.12507106 0.68550885 0.4755142  0.97539216 0.        ].png
img: 387 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1349_s_1.66_r_255_0.4746_[0.17014813 0.7291808  0.48067647 0.9673113  0.0256027 ].png
img: 388 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_134_s_0.77_r_244_0.7508_[0.4251688  0.71141165 0.9507132  0.7379049  0.92867273].png
img: 389 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1350_s_1.43_r_109_0.6512_[0.37334868 0.9053506  0.599249   0.98721623 0.39107895].png
img: 390 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1351_s_1.8_r_105_0.4459_[0.10010097 0.68440276 0.47537908 0.9600441  0.00955637].png
img: 391 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1352_s_1.4_r_316_0.7125_[0.3767468  0.9138122  0.68959624 0.98812455 0.5942675 ].png
img: 392 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1353_s_1.19_r_119_0.8443_[0.3913386  0.9352377  0.9572033  0.98915815 0.9485186 ].png
img: 393 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1354_s_1.78_r_203_0.4626_[0.12476599 0.7001313  0.48675284 0.9481912  0.05330586].png
img: 394 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1355_s_0.77_r_170_0.8121_[0.44189504 0.7870108  0.9598832  0.92946196 0.9424126 ].png
img: 395 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1356_s_1.71_r_304_0.5056_[0.16196321 0.7279751  0.5151373  0.95775694 0.16519092].png
img: 396 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1357_s_1.33_r_124_0.7845_[0.3833182  0.92339325 0.8268928  0.98997635 0.7991039 ].png
img: 397 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1358_s_1.68_r_194_0.4668_[0.1531064  0.70972425 0.48159406 0.96825933 0.02125014].png
img: 398 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1359_s_0.59_r_151_0.4723_[0.431024   0.42190582 0.694687   0.13071392 0.68320525].png
img: 399 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_135_s_0.51_r_48_0.3363_[0.35518137 0.35397807 0.17552207 0.3417477  0.4551671 ].png
img: 400 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1360_s_0.8_r_81_0.8358_[0.41990072 0.8614505  0.9625331  0.98560005 0.94930655].png
img: 401 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1361_s_1.21_r_22_0.8286_[0.3941215  0.9418009  0.91126746 0.9871196  0.908767  ].png
img: 402 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1362_s_1.06_r_44_0.8493_[0.39686373 0.9366267  0.9657127  0.9875993  0.95950866].png
img: 403 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1363_s_0.95_r_114_0.8471_[0.40248656 0.92429143 0.9681462  0.9843168  0.95612025].png
img: 404 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1364_s_1.56_r_303_0.601_[0.25567192 0.79495645 0.5940147  0.97944784 0.38067687].png
img: 405 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1365_s_1.46_r_169_0.5548_[0.3318925  0.85689926 0.5000819  0.98796415 0.09703764].png
img: 406 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1366_s_0.56_r_292_0.4225_[0.3842216  0.4199399  0.45005834 0.27409092 0.5840998 ].png
img: 407 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1367_s_1.02_r_173_0.8413_[0.40993747 0.91226447 0.9488459  0.9885248  0.9469646 ].png
img: 408 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1368_s_1.41_r_285_0.6386_[0.37809378 0.9086876  0.578677   0.9881114  0.33956918].png
img: 409 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1369_s_1.87_r_268_0.4219_[0.04878176 0.6382116  0.46647933 0.95602745 0.        ].png
img: 410 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_136_s_0.52_r_177_0.4017_[0.38558877 0.37608993 0.40451542 0.3306579  0.5117558 ].png
img: 411 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1370_s_0.79_r_17_0.8027_[0.4226404  0.79773843 0.9540397  0.9122174  0.9268306 ].png
img: 412 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1371_s_0.96_r_337_0.8493_[0.40297508 0.91846555 0.9723812  0.9893851  0.9630856 ].png
img: 413 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1372_s_1.78_r_279_0.4404_[0.08948263 0.6695069  0.47311816 0.9696472  0.        ].png
img: 414 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1373_s_1.35_r_188_0.6125_[0.39665118 0.92099416 0.5363021  0.98713464 0.22150904].png
img: 415 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1374_s_1.51_r_240_0.619_[0.30332938 0.8308733  0.5939925  0.9867211  0.38030353].png
img: 416 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1375_s_1.61_r_271_0.4627_[1.5548140e-01 7.0874429e-01 4.7360349e-01 9.7546923e-01 2.7395759e-05].png
img: 417 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1376_s_1.69_r_322_0.5054_[0.16333203 0.73064774 0.5132897  0.96170974 0.15783663].png
img: 418 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1377_s_1.09_r_209_0.8467_[0.4015636  0.9286535  0.9621744  0.98596925 0.955331  ].png
img: 419 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1378_s_1.29_r_131_0.7995_[0.39413294 0.9347916  0.84947556 0.9878888  0.83123904].png
img: 420 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1379_s_0.98_r_318_0.8409_[0.39890462 0.9327719  0.9426587  0.9855118  0.94466937].png
img: 421 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_137_s_1.4_r_54_0.74_[0.37951767 0.91674143 0.73965096 0.98953766 0.6744228 ].png
img: 422 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1380_s_0.54_r_134_0.3366_[0.37673363 0.37348604 0.13722953 0.33948338 0.45623776].png
img: 423 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1381_s_1.53_r_214_0.6251_[0.27966172 0.81086737 0.6188846  0.9842961  0.43156782].png
img: 424 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1382_s_0.86_r_76_0.8415_[0.414655   0.8850846  0.96649814 0.9876009  0.95356745].png
img: 425 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1383_s_1.62_r_340_0.505_[0.21275726 0.7659925  0.49309584 0.9682587  0.0849217 ].png
img: 426 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1384_s_1.45_r_336_0.6398_[0.35353327 0.88758034 0.59053713 0.9904136  0.37699604].png
img: 427 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1385_s_1.09_r_193_0.8412_[0.40629163 0.9218143  0.945666   0.9893744  0.9427114 ].png
img: 428 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1386_s_0.8_r_35_0.7012_[0.40508834 0.6746296  0.92356044 0.60536474 0.89741373].png
img: 429 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1387_s_0.66_r_300_0.5744_[0.41601443 0.49756292 0.90835154 0.18837732 0.86159366].png
img: 430 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1388_s_0.78_r_152_0.7219_[0.42860305 0.65852255 0.95769924 0.61928785 0.9455554 ].png
img: 431 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1389_s_0.56_r_342_0.4529_[0.39590815 0.41757044 0.53021115 0.31939164 0.6014117 ].png
img: 432 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_138_s_0.63_r_136_0.5071_[0.42764208 0.4441661  0.825283   0.09199511 0.74624604].png
img: 433 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1390_s_1.4_r_41_0.7326_[0.37553623 0.9137777  0.7275827  0.9889137  0.6570062 ].png
img: 434 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1391_s_1.59_r_66_0.5345_[0.2370693  0.7778689  0.5175462  0.98588955 0.1540796 ].png
img: 435 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1392_s_1.87_r_228_0.4431_[0.09116612 0.6632943  0.47596598 0.936682   0.04850833].png
img: 436 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1393_s_1.94_r_257_0.4211_[5.6753289e-02 6.4145273e-01 4.6530652e-01 9.4153434e-01 4.5223717e-04].png
img: 437 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1394_s_1.39_r_253_0.6301_[0.38864934 0.9205777  0.55822986 0.9853503  0.29764128].png
img: 438 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1395_s_0.71_r_106_0.7173_[0.43328875 0.6470104  0.9512286  0.6483407  0.9067103 ].png
img: 439 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1396_s_1.78_r_74_0.4505_[0.11234201 0.69401604 0.47468445 0.9580494  0.01353742].png
img: 440 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1397_s_1.27_r_4_0.6281_[0.3978314  0.9242957  0.55233425 0.9871792  0.27868026].png
img: 441 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1398_s_1.09_r_87_0.7676_[0.40546376 0.92025447 0.78366774 0.9869283  0.7418531 ].png
img: 442 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1399_s_1.41_r_346_0.5996_[0.3686103  0.9120816  0.5268614  0.9874748  0.20309074].png
img: 443 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_139_s_0.97_r_155_0.8494_[0.40952593 0.9105216  0.96972394 0.9903804  0.9667282 ].png
img: 444 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_13_s_1.78_r_65_0.4628_[0.1280793  0.70794183 0.48237813 0.95756227 0.03803009].png
img: 445 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1400_s_1.56_r_96_0.4927_[0.2209234  0.75897205 0.47994068 0.9810572  0.02275584].png
img: 446 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1401_s_1.14_r_226_0.845_[0.40010068 0.9333967  0.9550027  0.98708534 0.9495323 ].png
img: 447 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1402_s_1.92_r_234_0.4324_[0.0894568  0.66431135 0.4626532  0.91242415 0.03293977].png
img: 448 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1403_s_0.59_r_345_0.4993_[0.4157974  0.45307624 0.62606525 0.3553196  0.64621043].png
img: 449 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1404_s_1.69_r_231_0.5019_[0.16359504 0.7253218  0.51294273 0.9610948  0.1463904 ].png
img: 450 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1405_s_1.85_r_203_0.4475_[0.10092926 0.6842668  0.4803786  0.9371577  0.03480389].png
img: 451 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1406_s_1.71_r_233_0.5001_[0.15259977 0.7203944  0.5180618  0.9558501  0.15356363].png
img: 452 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1407_s_0.82_r_197_0.8306_[0.41484246 0.8688588  0.9619645  0.9606831  0.946842  ].png
img: 453 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1408_s_0.73_r_49_0.619_[0.42127874 0.53836006 0.94833946 0.2755539  0.911607  ].png
img: 454 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1409_s_1.96_r_27_0.4218_[0.07339688 0.65222824 0.46158612 0.8990098  0.02272013].png
img: 455 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_140_s_1.95_r_212_0.425_[0.07866535 0.6455663  0.4639767  0.8988658  0.03808769].png
img: 456 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1410_s_1.46_r_66_0.6243_[0.34353432 0.8847325  0.5729887  0.98869205 0.33158618].png
img: 457 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1411_s_0.59_r_57_0.459_[0.41445842 0.4090747  0.7025793  0.07056099 0.6980865 ].png
img: 458 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1412_s_0.57_r_188_0.5004_[0.39617866 0.43845725 0.6533109  0.35542598 0.65862924].png
img: 459 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1413_s_1.38_r_350_0.5968_[0.38542286 0.92412406 0.5177087  0.98816395 0.16869083].png
img: 460 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1414_s_1.04_r_73_0.845_[0.40460202 0.9158986  0.96356696 0.98771715 0.9531034 ].png
img: 461 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1415_s_1.06_r_358_0.8174_[0.4051421  0.9195652  0.88560736 0.98992383 0.88659084].png
img: 462 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1416_s_0.84_r_267_0.8429_[0.41251698 0.8975934  0.96368325 0.9812764  0.95959693].png
img: 463 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1417_s_0.78_r_140_0.6783_[0.42573348 0.6113042  0.94071764 0.4945684  0.91918755].png
img: 464 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1418_s_1.36_r_171_0.6042_[0.39424098 0.9208229  0.5265054  0.98856086 0.19073887].png
img: 465 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1419_s_1.95_r_205_0.425_[0.07670359 0.64551884 0.47144634 0.90703785 0.02412373].png
img: 466 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_141_s_1.81_r_51_0.4648_[0.1143494  0.6932678  0.49353656 0.94497913 0.07791421].png
img: 467 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1420_s_0.67_r_314_0.5601_[0.41809133 0.49030104 0.9006211  0.14861819 0.8428096 ].png
img: 468 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1421_s_1.35_r_228_0.7601_[0.38274688 0.91810036 0.77698785 0.98778844 0.7351093 ].png
img: 469 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1422_s_0.94_r_60_0.8413_[0.40021163 0.91531384 0.96012676 0.978932   0.9518096 ].png
img: 470 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1423_s_1.94_r_215_0.428_[0.08052257 0.64819413 0.46363845 0.9008194  0.04662534].png
img: 471 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1424_s_1.95_r_98_0.4129_[4.3700490e-02 6.3312584e-01 4.5750868e-01 9.3004948e-01 5.5799937e-05].png
img: 472 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1425_s_1.98_r_354_0.4097_[3.7987839e-02 6.2860769e-01 4.5449552e-01 9.2733592e-01 9.0632248e-06].png
img: 473 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1426_s_0.74_r_108_0.7219_[0.43449223 0.65343046 0.95502496 0.6590253  0.90731096].png
img: 474 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1427_s_0.88_r_299_0.8333_[0.40447408 0.9049042  0.9491316  0.9674998  0.940648  ].png
img: 475 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1428_s_0.99_r_221_0.8323_[0.40067676 0.92319566 0.9327596  0.9732694  0.93154305].png
img: 476 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1429_s_1.02_r_7_0.8418_[0.40246233 0.919429   0.94970775 0.98865914 0.948521  ].png
img: 477 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_142_s_1.87_r_329_0.4508_[0.10565674 0.6905197  0.4751937  0.9400751  0.042342  ].png
img: 478 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1430_s_1.27_r_134_0.804_[0.39434576 0.93179876 0.8595318  0.99034595 0.8437766 ].png
img: 479 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1431_s_1.56_r_239_0.5885_[0.27219746 0.80283326 0.57086635 0.981805   0.314741  ].png
img: 480 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1432_s_1.33_r_97_0.6177_[0.39701727 0.91991353 0.54211235 0.9865061  0.24293289].png
img: 481 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1433_s_1.83_r_128_0.4578_[0.10871086 0.6811363  0.4888545  0.9357231  0.07454852].png
img: 482 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1434_s_1.56_r_261_0.4905_[0.22756073 0.76367843 0.4745885  0.98039585 0.00632071].png
img: 483 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1435_s_1.03_r_196_0.8493_[0.40824315 0.91394526 0.9716998  0.98634267 0.9662031 ].png
img: 484 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1436_s_1.12_r_151_0.8503_[0.4026858  0.9277037  0.96920985 0.98988247 0.9619121 ].png
img: 485 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1437_s_1.95_r_277_0.4137_[4.1389294e-02 6.2999427e-01 4.5875478e-01 9.3844688e-01 6.5324712e-05].png
img: 486 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1438_s_1.95_r_341_0.4257_[0.066771   0.6610425  0.4613956  0.93684864 0.00241604].png
img: 487 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1439_s_1.7_r_109_0.4777_[0.15287663 0.72388136 0.49177665 0.9596075  0.06024082].png
img: 488 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_143_s_0.75_r_99_0.7951_[0.43565217 0.7644877  0.9613352  0.87971884 0.93423027].png
img: 489 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1440_s_1.25_r_329_0.8224_[0.39120793 0.9266084  0.9054097  0.99065465 0.89797926].png
img: 490 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1441_s_0.72_r_249_0.702_[0.43803284 0.6256893  0.9398003  0.60027313 0.9062321 ].png
img: 491 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1442_s_1.64_r_130_0.5402_[0.18253262 0.74198276 0.5511423  0.9755688  0.24978246].png
img: 492 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1443_s_1.52_r_236_0.6176_[0.29020444 0.8207278  0.5998104  0.9840351  0.39310104].png
img: 493 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1444_s_0.67_r_84_0.6507_[0.44624707 0.5390239  0.95092696 0.42344928 0.8938814 ].png
img: 494 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1445_s_1.69_r_133_0.4985_[0.1546619  0.71226686 0.5122153  0.96578276 0.14733523].png
img: 495 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1446_s_1.74_r_212_0.4909_[0.14633799 0.7147747  0.50998497 0.95266384 0.13089588].png
img: 496 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1447_s_0.76_r_326_0.6859_[0.41903406 0.6202374  0.9483426  0.50230527 0.9396456 ].png
img: 497 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1448_s_1.96_r_313_0.4177_[0.06666923 0.6430216  0.45318347 0.8972242  0.02858305].png
img: 498 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1449_s_1.66_r_123_0.5318_[0.17948538 0.7437665  0.5415145  0.9668623  0.22726281].png
img: 499 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_144_s_0.98_r_8_0.8487_[0.40136293 0.9192524  0.973032   0.98819965 0.9616136 ].png
img: 500 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1450_s_1.23_r_251_0.7795_[0.39899322 0.9202792  0.8057223  0.9857203  0.7866481 ].png
img: 501 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1451_s_0.65_r_33_0.5574_[0.43174946 0.46242598 0.9154702  0.12524478 0.852195  ].png
img: 502 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1452_s_1.32_r_239_0.7869_[0.3892343  0.92273015 0.82559896 0.9833716  0.8137561 ].png
img: 503 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1453_s_1.13_r_168_0.8009_[0.40646055 0.9248452  0.8495911  0.9909524  0.8325663 ].png
img: 504 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1454_s_1.06_r_264_0.8316_[0.40622246 0.9188843  0.9226246  0.9866156  0.9234589 ].png
img: 505 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1455_s_1.83_r_225_0.4495_[0.09433628 0.6561667  0.47784856 0.93558896 0.08358054].png
img: 506 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1456_s_1.66_r_22_0.5055_[0.18673049 0.7482755  0.5041723  0.9701816  0.11829105].png
img: 507 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1457_s_0.77_r_130_0.657_[0.42239758 0.5837426  0.95645493 0.39852667 0.92365   ].png
img: 508 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1458_s_0.64_r_117_0.5685_[0.4347719  0.47497562 0.92063785 0.16318394 0.84900415].png
img: 509 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1459_s_1.02_r_354_0.8334_[0.40432122 0.91825545 0.9232292  0.9904284  0.9308751 ].png
img: 510 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_145_s_0.86_r_8_0.8414_[0.41036004 0.88923323 0.96877575 0.9834914  0.95500606].png
img: 511 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1460_s_1.7_r_310_0.505_[0.14912595 0.71605545 0.5189902  0.962324   0.1786966 ].png
img: 512 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1461_s_0.59_r_99_0.5098_[0.408594   0.42971396 0.73542315 0.26158193 0.713735  ].png
img: 513 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1462_s_0.81_r_126_0.7222_[0.41458446 0.67978287 0.95766586 0.6335678  0.92524225].png
img: 514 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1463_s_0.76_r_50_0.6681_[0.41456842 0.605318   0.9436297  0.45428625 0.9228545 ].png
img: 515 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1464_s_1.49_r_359_0.5012_[2.5822717e-01 7.9140341e-01 4.7125387e-01 9.8479432e-01 3.0455063e-04].png
img: 516 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1465_s_0.9_r_202_0.8393_[0.4079798  0.90702945 0.9561852  0.9812154  0.94386405].png
img: 517 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1466_s_1.24_r_358_0.6346_[0.3991894  0.9278425  0.55976325 0.9854708  0.30066866].png
img: 518 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1467_s_0.97_r_16_0.8475_[0.40349075 0.91506106 0.9697092  0.9886791  0.96037304].png
img: 519 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1468_s_0.94_r_231_0.8413_[0.40451133 0.91685385 0.95263654 0.9826902  0.9498062 ].png
img: 520 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1469_s_1.2_r_203_0.8347_[0.40066153 0.9288035  0.9291289  0.9893546  0.9254417 ].png
img: 521 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_146_s_1.24_r_93_0.652_[0.40190598 0.9276146  0.5837317  0.98498654 0.3618609 ].png
img: 522 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1470_s_0.71_r_120_0.6108_[0.42592546 0.53375924 0.9363445  0.26615226 0.8920266 ].png
img: 523 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1471_s_1.88_r_346_0.4325_[0.07299214 0.66703665 0.4683703  0.95313346 0.00112458].png
img: 524 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1472_s_1.02_r_62_0.839_[0.40071794 0.9190455  0.95000714 0.9849734  0.9402203 ].png
img: 525 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1473_s_1.29_r_125_0.8167_[0.39059597 0.9372676  0.8907054  0.9897637  0.8750079 ].png
img: 526 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1474_s_0.87_r_44_0.8131_[0.39861086 0.8689156  0.94864744 0.91349906 0.9358418 ].png
img: 527 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1475_s_0.94_r_296_0.8375_[0.3994257  0.9237585  0.94079626 0.9767842  0.9467651 ].png
img: 528 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1476_s_0.74_r_50_0.6085_[0.42888975 0.52904934 0.92662835 0.28231314 0.8757793 ].png
img: 529 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1477_s_0.84_r_161_0.8376_[0.42175284 0.868257   0.9645895  0.98019224 0.9530234 ].png
img: 530 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1478_s_1.12_r_342_0.8368_[0.4027221  0.9235934  0.9346624  0.98964846 0.9332201 ].png
img: 531 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1479_s_1.85_r_299_0.4557_[0.10437912 0.69041604 0.48419696 0.9337988  0.06586827].png
img: 532 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_147_s_1.32_r_170_0.6313_[0.39876744 0.92979795 0.5563091  0.98863786 0.2830728 ].png
img: 533 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1480_s_0.9_r_286_0.842_[0.40723163 0.90782744 0.9609408  0.9792578  0.95494384].png
img: 534 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1481_s_0.6_r_288_0.485_[0.3939423  0.48083344 0.5795616  0.34618407 0.6243229 ].png
img: 535 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1482_s_0.62_r_307_0.4974_[0.41423368 0.46865672 0.70366716 0.2005562  0.70006   ].png
img: 536 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1483_s_1.36_r_69_0.6818_[0.38845086 0.91820014 0.63460743 0.9895779  0.47792676].png
img: 537 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1484_s_1.34_r_239_0.7674_[0.38967127 0.9195728  0.7872228  0.98857534 0.7520233 ].png
img: 538 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1485_s_1.94_r_137_0.4136_[0.06593449 0.6278894  0.44894275 0.8875667  0.03784406].png
img: 539 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1486_s_0.97_r_39_0.8376_[0.3981382  0.92609245 0.9443505  0.98563737 0.93387985].png
img: 540 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1487_s_1.93_r_264_0.4173_[4.4299155e-02 6.2868112e-01 4.6680588e-01 9.4676667e-01 9.5271671e-06].png
img: 541 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1488_s_0.72_r_241_0.6527_[0.43509877 0.56525505 0.94527763 0.41259196 0.90534717].png
img: 542 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1489_s_1.92_r_74_0.4282_[0.06417927 0.6542704  0.46848133 0.94933    0.00460533].png
img: 543 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_148_s_1.11_r_346_0.8172_[0.40287837 0.9238347  0.8859882  0.98987    0.8831949 ].png
img: 544 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1490_s_0.79_r_273_0.8327_[0.42159167 0.8638655  0.9558797  0.97399837 0.9482589 ].png
img: 545 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1491_s_0.66_r_97_0.625_[0.4363208  0.5210668  0.9479085  0.35291204 0.86689496].png
img: 546 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1492_s_1.86_r_7_0.4281_[5.8851510e-02 6.4954025e-01 4.6898955e-01 9.6324652e-01 4.1075775e-05].png
img: 547 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1493_s_1.7_r_341_0.475_[0.15483443 0.72223383 0.48356533 0.9659238  0.04840055].png
img: 548 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1494_s_1.34_r_65_0.7353_[0.38746208 0.92722493 0.72199774 0.9883137  0.6513469 ].png
img: 549 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1495_s_0.61_r_133_0.4765_[0.42906585 0.441448   0.6728812  0.16994599 0.6692743 ].png
img: 550 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1496_s_0.91_r_219_0.8296_[0.4013091  0.9057507  0.94513255 0.95941365 0.9363466 ].png
img: 551 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1497_s_1.71_r_168_0.4565_[0.13340056 0.6998537  0.47643164 0.9711439  0.00185392].png
img: 552 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1498_s_0.72_r_109_0.7134_[0.4349171  0.63766885 0.94873476 0.6326079  0.9130796 ].png
img: 553 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1499_s_1.91_r_277_0.4197_[0.0460724  0.6358531  0.46503222 0.95178187 0.        ].png
img: 554 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_149_s_1.61_r_289_0.5138_[0.20921117 0.7566381  0.5074041  0.9667895  0.1290684 ].png
img: 555 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_14_s_0.5_r_261_0.3276_[0.40028653 0.34854928 0.3100814  0.14407563 0.4347861 ].png
img: 556 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1500_s_0.84_r_91_0.843_[0.41435516 0.8879152  0.9726966  0.98040307 0.95946604].png
img: 557 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1501_s_0.53_r_225_0.3468_[0.36704934 0.38045183 0.1682291  0.32570055 0.49264556].png
img: 558 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1502_s_0.5_r_37_0.2972_[0.3984508  0.3262977  0.23040618 0.01548054 0.515321  ].png
img: 559 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1503_s_1.81_r_215_0.4693_[0.11588787 0.69321984 0.4970455  0.9460485  0.09453631].png
img: 560 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1504_s_1.93_r_161_0.431_[0.07365481 0.6574726  0.47033215 0.94407123 0.00956879].png
img: 561 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1505_s_1.13_r_110_0.8421_[0.39992094 0.93584603 0.9479634  0.9880639  0.93854135].png
img: 562 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1506_s_0.68_r_176_0.678_[0.45537597 0.57141066 0.95429975 0.496997   0.91197956].png
img: 563 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1507_s_0.85_r_94_0.8429_[0.4115483 0.8948984 0.9727382 0.9807165 0.9545281].png
img: 564 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1508_s_1.89_r_155_0.438_[0.09537584 0.68189925 0.46758935 0.9256349  0.0196505 ].png
img: 565 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1509_s_1.63_r_27_0.5401_[0.20244522 0.7557218  0.5400492  0.97437    0.2278466 ].png
img: 566 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_150_s_1.47_r_333_0.6448_[0.33678842 0.8667127  0.61040884 0.988877   0.42119813].png
img: 567 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1510_s_1.27_r_250_0.7348_[0.3994368  0.92321706 0.7169877  0.9863609  0.6478482 ].png
img: 568 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1511_s_1.7_r_176_0.4476_[1.126630e-01 6.811294e-01 4.723420e-01 9.715138e-01 3.070348e-04].png
img: 569 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1512_s_0.67_r_256_0.643_[0.44321054 0.54391426 0.9269546  0.44513205 0.8555432 ].png
img: 570 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1513_s_0.57_r_177_0.5399_[0.41427717 0.4350108  0.78458077 0.31344104 0.7519699 ].png
img: 571 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1514_s_1.16_r_49_0.8382_[0.3940855  0.9437229  0.93834    0.98854995 0.9260776 ].png
img: 572 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1515_s_1.87_r_72_0.4383_[0.08846916 0.6803908  0.47167292 0.9456741  0.00527112].png
img: 573 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1516_s_1.57_r_310_0.5865_[0.23373228 0.78164065 0.5855738  0.9755599  0.35611713].png
img: 574 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1517_s_1.51_r_176_0.5045_[0.2537506  0.78007865 0.48001078 0.98345506 0.02511561].png
img: 575 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1518_s_1.02_r_320_0.8465_[0.39940715 0.93102485 0.9572985  0.98667914 0.95796734].png
img: 576 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1519_s_1.46_r_220_0.6846_[0.34091803 0.87520593 0.6706524  0.9876548  0.54865175].png
img: 577 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_151_s_1.49_r_341_0.5667_[0.31254968 0.845661   0.51776296 0.9862231  0.17119822].png
img: 578 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1520_s_0.73_r_66_0.6792_[0.4223427  0.6073075  0.95174414 0.49365556 0.92105097].png
img: 579 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1521_s_1.21_r_231_0.8291_[0.39681533 0.93077165 0.91779214 0.9867435  0.91355187].png
img: 580 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1522_s_0.5_r_86_0.3574_[0.404441   0.35480282 0.40835017 0.09585901 0.5236472 ].png
img: 581 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1523_s_1.27_r_225_0.7939_[0.3962676  0.9329295  0.8337495  0.98783666 0.818511  ].png
img: 582 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1524_s_0.98_r_70_0.8452_[0.40336683 0.9142656  0.9664141  0.98757106 0.9544439 ].png
img: 583 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1525_s_1.01_r_282_0.8478_[0.40448594 0.91969186 0.9612755  0.98693854 0.9665879 ].png
img: 584 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1526_s_1.1_r_125_0.8499_[0.39554322 0.9444616  0.9687724  0.98791426 0.95280707].png
img: 585 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1527_s_0.65_r_260_0.6506_[0.44607076 0.536133   0.9288632  0.48417032 0.8578355 ].png
img: 586 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1528_s_1.76_r_343_0.4544_[0.12393311 0.7046193  0.472665   0.9593983  0.01130196].png
img: 587 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1529_s_1.35_r_200_0.724_[0.3927485  0.91961104 0.7018059  0.98858774 0.61702496].png
img: 588 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_152_s_0.72_r_216_0.6077_[0.43284908 0.5230825  0.9322394  0.27397448 0.8765743 ].png
img: 589 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1530_s_1.76_r_233_0.4797_[0.13391571 0.70191133 0.501321   0.94795763 0.11338898].png
img: 590 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1531_s_0.54_r_166_0.3841_[0.3987564  0.36460355 0.3741067  0.25231752 0.530917  ].png
img: 591 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1532_s_1.12_r_41_0.848_[0.39365613 0.9439288  0.96217394 0.9873623  0.95272505].png
img: 592 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1533_s_1.47_r_127_0.6844_[0.33511844 0.8686609  0.6738184  0.98894995 0.5553015 ].png
img: 593 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1534_s_1.78_r_44_0.4633_[0.10808087 0.67763823 0.49059048 0.9439484  0.09603242].png
img: 594 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1535_s_0.61_r_291_0.5097_[0.42169073 0.46082318 0.71434295 0.23267469 0.71910435].png
img: 595 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1536_s_0.55_r_125_0.3603_[0.39058706 0.38427997 0.26643068 0.22518677 0.5347891 ].png
img: 596 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1537_s_1.46_r_229_0.6674_[0.33504716 0.8654698  0.6470227  0.9871591  0.5021802 ].png
img: 597 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1538_s_0.85_r_88_0.8445_[0.4108326  0.899677   0.96727973 0.9853345  0.9591476 ].png
img: 598 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1539_s_1.18_r_336_0.8277_[0.39940965 0.92195743 0.9167095  0.99030215 0.9099009 ].png
img: 599 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_153_s_1.62_r_6_0.4702_[1.7110626e-01 7.2843337e-01 4.7283730e-01 9.7819096e-01 3.5259017e-04].png
img: 600 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1540_s_1.58_r_15_0.5126_[0.23023966 0.7716039  0.49631283 0.980046   0.08473035].png
img: 601 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1541_s_1.89_r_199_0.4342_[0.08148374 0.66551787 0.47239977 0.9429612  0.00853577].png
img: 602 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1542_s_1.85_r_274_0.4269_[0.05611493 0.6448406  0.47016507 0.9631484  0.        ].png
img: 603 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1543_s_0.61_r_61_0.5407_[0.42464423 0.44798005 0.88118213 0.15139845 0.7983992 ].png
img: 604 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1544_s_1.24_r_105_0.764_[0.40133578 0.93205094 0.77140963 0.9884021  0.72666943].png
img: 605 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1545_s_0.62_r_140_0.4972_[0.41967896 0.4367269  0.76102835 0.12763281 0.7408082 ].png
img: 606 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1546_s_1.19_r_280_0.7524_[0.40221962 0.9283088  0.7465199  0.98436135 0.7005549 ].png
img: 607 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1547_s_1.23_r_18_0.8069_[0.39649588 0.9366753  0.8613173  0.98843324 0.8516508 ].png
img: 608 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1548_s_0.99_r_253_0.8459_[0.40957478 0.9061717  0.9671765  0.9840458  0.96242774].png
img: 609 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1549_s_0.78_r_253_0.8003_[0.42960626 0.78529024 0.95168483 0.8986897  0.9364435 ].png
img: 610 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_154_s_1.46_r_243_0.6559_[0.34736124 0.8738146  0.6240184  0.98640543 0.44765374].png
img: 611 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1550_s_1.2_r_132_0.8413_[0.3966112  0.9403908  0.9428983  0.99031717 0.93612826].png
img: 612 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1551_s_0.76_r_66_0.7311_[0.41820765 0.6806416  0.9604834  0.6600656  0.93619394].png
img: 613 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1552_s_1.23_r_154_0.8242_[0.39187214 0.92410624 0.9127262  0.9909091  0.9013798 ].png
img: 614 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1553_s_1.6_r_193_0.4906_[0.20401524 0.74677646 0.4847678  0.9738413  0.04339341].png
img: 615 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1554_s_1.96_r_194_0.4208_[0.05513558 0.6397255  0.4678496  0.9400746  0.00110906].png
img: 616 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1555_s_0.85_r_305_0.8148_[0.40010214 0.8692736  0.95094734 0.9155341  0.9381443 ].png
img: 617 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1556_s_0.84_r_184_0.8451_[0.41688514 0.8916712  0.97177505 0.9855062  0.9598378 ].png
img: 618 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1557_s_1.14_r_327_0.8478_[0.39645502 0.9383161  0.95864445 0.9889701  0.9566443 ].png
img: 619 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1558_s_0.75_r_245_0.7052_[0.4331663  0.63262916 0.9482435  0.59512806 0.91694665].png
img: 620 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1559_s_0.73_r_194_0.7355_[0.43234584 0.6801041  0.95265555 0.7092386  0.9030556 ].png
img: 621 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_155_s_0.95_r_265_0.8482_[0.40908617 0.909331   0.96851647 0.98595136 0.96795046].png
img: 622 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1560_s_0.94_r_167_0.8499_[0.41134912 0.90881157 0.97323924 0.99108976 0.96495557].png
img: 623 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1561_s_1.68_r_342_0.4781_[0.17025922 0.7346799  0.48144382 0.96588004 0.03799754].png
img: 624 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1562_s_0.91_r_182_0.8488_[0.41266817 0.90348417 0.9706017  0.9867367  0.9704483 ].png
img: 625 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1563_s_0.87_r_120_0.8207_[0.41043288 0.86215913 0.95659125 0.9351802  0.9393126 ].png
img: 626 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1564_s_2.0_r_115_0.3911_[1.1195636e-02 6.0557252e-01 4.4246644e-01 8.9639807e-01 1.1546318e-04].png
img: 627 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1565_s_1.8_r_0_0.4293_[0.05760511 0.65175897 0.46975437 0.9671718  0.        ].png
img: 628 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1566_s_1.46_r_338_0.6181_[0.3431451  0.876951   0.5657175  0.9898532  0.31499463].png
img: 629 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1567_s_1.51_r_244_0.6018_[0.29909876 0.8238582  0.5745342  0.98495215 0.3267734 ].png
img: 630 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1568_s_1.32_r_186_0.6213_[0.39815077 0.9218876  0.5462126  0.98708576 0.2529206 ].png
img: 631 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1569_s_1.24_r_32_0.8288_[0.38449234 0.9310595  0.9258938  0.98897827 0.91333425].png
img: 632 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_156_s_1.06_r_20_0.8432_[0.3993842 0.9277935 0.9541134 0.987215  0.9474837].png
img: 633 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1570_s_0.95_r_12_0.8513_[0.402563   0.921234   0.97437197 0.99026823 0.9681212 ].png
img: 634 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1571_s_0.91_r_199_0.8457_[0.4067875  0.912908   0.96681446 0.984085   0.95801973].png
img: 635 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1572_s_1.98_r_10_0.4155_[4.4878956e-02 6.3610214e-01 4.6246520e-01 9.3397260e-01 3.6351739e-05].png
img: 636 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1573_s_1.84_r_168_0.4344_[8.0226369e-02 6.6220522e-01 4.7084150e-01 9.5846808e-01 6.2845655e-05].png
img: 637 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1574_s_1.97_r_310_0.4198_[0.06838473 0.640873   0.45773393 0.9040772  0.0281472 ].png
img: 638 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1575_s_0.77_r_25_0.7069_[0.42423865 0.6422079  0.9545513  0.58402145 0.9295679 ].png
img: 639 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1576_s_1.64_r_255_0.4825_[0.18663433 0.74017096 0.4841199  0.9696326  0.03190043].png
img: 640 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1577_s_0.51_r_356_0.3937_[0.363679   0.37257218 0.41059425 0.2921387  0.52950835].png
img: 641 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1578_s_0.85_r_24_0.831_[0.4037186  0.89202726 0.95048887 0.9713686  0.9374736 ].png
img: 642 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1579_s_1.74_r_207_0.4884_[0.1472597  0.70983046 0.5061154  0.96177524 0.11705576].png
img: 643 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_157_s_1.98_r_219_0.4221_[0.06971657 0.642748   0.4611433  0.8951964  0.04163947].png
img: 644 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1580_s_0.98_r_28_0.8357_[0.39947665 0.9125215  0.94806015 0.9749008  0.94333655].png
img: 645 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1581_s_1.04_r_322_0.838_[0.40165195 0.9244074  0.93718064 0.98708767 0.9395211 ].png
img: 646 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1582_s_0.68_r_149_0.5965_[0.44007766 0.50046104 0.9441921  0.2112029  0.88660365].png
img: 647 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1583_s_0.81_r_51_0.7309_[0.41494817 0.6909601  0.95270544 0.66455245 0.9310878 ].png
img: 648 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1584_s_1.75_r_275_0.4393_[0.09000377 0.66900355 0.47075137 0.9668214  0.        ].png
img: 649 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1585_s_1.9_r_225_0.4245_[0.0787857  0.6400267  0.45971292 0.9017768  0.04225145].png
img: 650 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1586_s_1.96_r_276_0.4152_[0.04055708 0.6289797  0.46211684 0.944453   0.        ].png
img: 651 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1587_s_1.84_r_129_0.457_[0.10171892 0.67714226 0.49041897 0.94136727 0.07429523].png
img: 652 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1588_s_0.8_r_161_0.8023_[0.42265236 0.79815465 0.95890087 0.8821627  0.9494544 ].png
img: 653 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1589_s_1.14_r_190_0.8219_[0.40636647 0.9247747  0.896957   0.98797816 0.89359343].png
img: 654 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_158_s_1.02_r_117_0.8411_[0.40127298 0.92447674 0.9503533  0.9822014  0.94720995].png
img: 655 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1590_s_0.89_r_279_0.8437_[0.40554523 0.9112856  0.9653665  0.97806275 0.95848054].png
img: 656 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1591_s_1.54_r_121_0.6194_[0.27032685 0.80510706 0.61690515 0.98647004 0.41824567].png
img: 657 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1592_s_1.61_r_258_0.4837_[0.19279918 0.7416951  0.48261166 0.97325015 0.02830253].png
img: 658 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1593_s_1.36_r_127_0.7764_[0.3803048  0.91897315 0.811153   0.9900626  0.7816848 ].png
img: 659 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1594_s_1.09_r_62_0.8372_[0.3980965  0.92552185 0.9424817  0.9882199  0.93158   ].png
img: 660 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1595_s_0.91_r_226_0.8426_[0.40229532 0.91970265 0.9593925  0.9772722  0.9545341 ].png
img: 661 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1596_s_1.73_r_311_0.49_[0.13506752 0.7026164  0.5105685  0.9629948  0.13879842].png
img: 662 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1597_s_0.69_r_222_0.584_[0.425309   0.50919235 0.9314436  0.20280817 0.8511396 ].png
img: 663 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1598_s_0.66_r_33_0.5538_[0.42029968 0.49203292 0.86019623 0.18838784 0.8078376 ].png
img: 664 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1599_s_0.7_r_286_0.6814_[0.43139094 0.59980315 0.94142294 0.54008883 0.8942117 ].png
img: 665 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_159_s_1.02_r_217_0.8278_[0.40124282 0.91610354 0.92217314 0.97648984 0.92274415].png
img: 666 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_15_s_1.28_r_153_0.812_[0.39209422 0.9226312  0.88093007 0.99113744 0.873053  ].png
img: 667 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1600_s_0.81_r_354_0.8379_[0.41819257 0.8683321  0.9611914  0.9829573  0.95882756].png
img: 668 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1601_s_1.14_r_193_0.8235_[0.40555683 0.9251808  0.90059143 0.9884195  0.89758515].png
img: 669 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1602_s_0.61_r_153_0.501_[0.44765443 0.42207164 0.81823695 0.04964607 0.7674331 ].png
img: 670 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1603_s_1.55_r_292_0.5747_[0.27648813 0.8115942  0.545964   0.979858   0.2595066 ].png
img: 671 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1604_s_0.92_r_140_0.8437_[0.4023015  0.9262428  0.95465523 0.9881125  0.94724154].png
img: 672 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1605_s_1.65_r_196_0.4846_[0.17742987 0.7279936  0.4908387  0.96591467 0.06069455].png
img: 673 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1606_s_1.02_r_205_0.8373_[0.4038997  0.92235106 0.93729264 0.9870566  0.9360128 ].png
img: 674 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1607_s_0.98_r_149_0.8469_[0.4040859 0.9176036 0.9685574 0.9835959 0.9605055].png
img: 675 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1608_s_1.34_r_56_0.7641_[0.38423404 0.9282905  0.7796854  0.987942   0.74041986].png
img: 676 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1609_s_0.61_r_148_0.5064_[0.43063003 0.42441398 0.81038964 0.11395573 0.75253683].png
img: 677 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_160_s_1.42_r_116_0.715_[0.37103552 0.9115586  0.69631106 0.98953277 0.6066574 ].png
img: 678 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1610_s_0.87_r_244_0.8251_[0.4127359  0.86271805 0.9589946  0.94376975 0.94713336].png
img: 679 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1611_s_1.4_r_293_0.7103_[0.38265353 0.9157526  0.68333286 0.98658496 0.5833558 ].png
img: 680 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1612_s_0.86_r_332_0.8109_[0.41355655 0.83513165 0.94792145 0.91604006 0.942037  ].png
img: 681 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1613_s_1.28_r_122_0.8244_[0.38824034 0.9419384  0.90741575 0.98921704 0.8951876 ].png
img: 682 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1614_s_1.25_r_117_0.8282_[0.39501724 0.9285234  0.91797113 0.98942965 0.9099616 ].png
img: 683 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1615_s_1.34_r_183_0.5821_[0.3973259  0.9178417  0.50291574 0.98678994 0.10540466].png
img: 684 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1616_s_0.62_r_275_0.5815_[0.42425507 0.47557938 0.9216014  0.24345295 0.8426607 ].png
img: 685 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1617_s_1.09_r_327_0.8484_[0.3987216  0.92915034 0.96579915 0.9888206  0.95948195].png
img: 686 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1618_s_1.61_r_25_0.5478_[0.21964838 0.77239585 0.5404173  0.9725884  0.23396195].png
img: 687 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1619_s_1.45_r_68_0.6202_[0.35932642 0.89560086 0.56176263 0.99027514 0.29416904].png
img: 688 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_161_s_1.43_r_128_0.7168_[0.36377007 0.9032429  0.7082386  0.99004465 0.61848474].png
img: 689 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1620_s_1.25_r_12_0.7256_[0.40034184 0.93078345 0.6968172  0.9894857  0.61065346].png
img: 690 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1621_s_0.54_r_183_0.4741_[0.39522356 0.39569446 0.6563215  0.25475216 0.6687409 ].png
img: 691 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1622_s_1.96_r_352_0.4152_[4.2525340e-02 6.3713729e-01 4.6097422e-01 9.3540561e-01 9.2429127e-06].png
img: 692 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1623_s_1.17_r_142_0.8474_[0.39723197 0.9376619  0.9599859  0.98930275 0.9527583 ].png
img: 693 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1624_s_1.44_r_153_0.6821_[0.36347282 0.89436376 0.6509767  0.99169827 0.50993854].png
img: 694 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1625_s_0.68_r_183_0.6878_[0.45128593 0.5866524  0.95421153 0.52898663 0.9180504 ].png
img: 695 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1626_s_1.61_r_336_0.5223_[0.21861295 0.7639835  0.5104733  0.97844    0.13987197].png
img: 696 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1627_s_1.19_r_6_0.7283_[0.39873376 0.93490547 0.6993333  0.9904206  0.6181205 ].png
img: 697 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1628_s_1.97_r_40_0.4204_[0.06818008 0.64212173 0.45847803 0.9050759  0.02820774].png
img: 698 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1629_s_1.52_r_175_0.5009_[0.24899107 0.779568   0.47735414 0.9840956  0.01448051].png
img: 699 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_162_s_0.52_r_318_0.3523_[0.36502582 0.36265633 0.16976714 0.3900686  0.47374126].png
img: 700 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1630_s_1.2_r_5_0.7132_[0.39839432 0.935715   0.6749917  0.9887629  0.5683748 ].png
img: 701 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1631_s_0.74_r_283_0.7429_[0.4330347  0.6887235  0.94599664 0.7273405  0.91950464].png
img: 702 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1632_s_1.78_r_131_0.4733_[0.11927264 0.6889426  0.49583098 0.9560799  0.10643254].png
img: 703 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1633_s_1.44_r_268_0.5266_[0.31731793 0.8439464  0.4756319  0.98438895 0.01192639].png
img: 704 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1634_s_0.93_r_322_0.8414_[0.4025153  0.91787475 0.9541705  0.98431253 0.94824743].png
img: 705 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1635_s_1.84_r_80_0.4322_[7.3401667e-02 6.5968198e-01 4.7006574e-01 9.5733631e-01 5.1286345e-04].png
img: 706 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1636_s_1.99_r_24_0.4194_[0.0601887  0.6345073  0.46519318 0.8819904  0.05530412].png
img: 707 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1637_s_0.73_r_112_0.6977_[0.42973977 0.6300319  0.9407797  0.57577693 0.912321  ].png
img: 708 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1638_s_1.85_r_219_0.4514_[0.09657227 0.6743419  0.48531064 0.93816465 0.06242098].png
img: 709 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1639_s_1.35_r_82_0.5932_[0.3895664  0.9294102  0.5138487  0.98675746 0.14657512].png
img: 710 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_163_s_1.36_r_124_0.7748_[0.38250598 0.9237984  0.80444354 0.99021465 0.77288413].png
img: 711 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1640_s_0.83_r_188_0.8388_[0.41756165 0.8767381  0.9692308  0.9725141  0.9577585 ].png
img: 712 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1641_s_0.59_r_20_0.4892_[0.40749255 0.44929832 0.64055693 0.27327758 0.6754202 ].png
img: 713 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1642_s_1.59_r_218_0.5735_[0.22666727 0.7690505  0.5744511  0.9796148  0.3174865 ].png
img: 714 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1643_s_0.52_r_247_0.3706_[0.37501565 0.36066377 0.38710472 0.23007916 0.50027305].png
img: 715 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1644_s_1.87_r_102_0.4303_[7.0372909e-02 6.5898645e-01 4.6818247e-01 9.5385516e-01 2.1314171e-04].png
img: 716 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1645_s_0.66_r_2_0.6314_[0.43426493 0.53279436 0.94965595 0.330602   0.90969014].png
img: 717 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1646_s_1.42_r_356_0.5504_[0.3503946  0.8879877  0.48280206 0.9874843  0.04325181].png
img: 718 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1647_s_0.96_r_249_0.8457_[0.40810314 0.90900344 0.9668291  0.9853681  0.9593124 ].png
img: 719 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1648_s_1.69_r_28_0.5097_[0.1702916  0.7397002  0.5184821  0.9623501  0.15753314].png
img: 720 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1649_s_0.96_r_80_0.8484_[0.40464604 0.9157109  0.97232944 0.99019474 0.9590588 ].png
img: 721 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_164_s_1.67_r_216_0.5206_[0.17246656 0.733127   0.5326527  0.9625477  0.2022284 ].png
img: 722 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1650_s_0.62_r_141_0.486_[0.4333595  0.4270393  0.7668439  0.07002984 0.7327182 ].png
img: 723 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1651_s_0.73_r_293_0.7055_[0.42459878 0.6474404  0.93980557 0.6078751  0.90770936].png
img: 724 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1652_s_1.98_r_289_0.4166_[0.06171644 0.6471911  0.4540904  0.9125665  0.00751006].png
img: 725 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1653_s_1.96_r_81_0.4163_[4.3750539e-02 6.3199073e-01 4.6355963e-01 9.4202244e-01 9.2302864e-05].png
img: 726 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1654_s_1.16_r_221_0.834_[0.3901556  0.9214342  0.93792015 0.986183   0.93419546].png
img: 727 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1655_s_1.52_r_51_0.6212_[0.28549108 0.81944335 0.60736454 0.9880252  0.40546817].png
img: 728 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1656_s_1.52_r_34_0.6397_[0.29657182 0.8350336  0.62682855 0.98749584 0.4527651 ].png
img: 729 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1657_s_0.58_r_100_0.5133_[0.41023895 0.43724084 0.73331124 0.27433866 0.71157193].png
img: 730 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1658_s_1.74_r_19_0.4688_[0.13647722 0.7100029  0.4853269  0.96168333 0.05041967].png
img: 731 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1659_s_1.15_r_166_0.8107_[0.40583602 0.9277254  0.8693199  0.9894669  0.86114496].png
img: 732 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_165_s_1.92_r_160_0.4336_[0.08019749 0.66508126 0.4717769  0.9378675  0.01288194].png
img: 733 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1660_s_0.98_r_33_0.8379_[0.39948097 0.915483   0.94964933 0.9832787  0.9417053 ].png
img: 734 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1661_s_1.54_r_47_0.5972_[0.25871706 0.7942033  0.58631814 0.98665667 0.3599017 ].png
img: 735 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1662_s_1.83_r_39_0.462_[0.10467757 0.68702596 0.49405757 0.9414212  0.0828932 ].png
img: 736 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1663_s_1.9_r_204_0.4367_[0.08571789 0.6656738  0.4690076  0.9324962  0.03045545].png
img: 737 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1664_s_1.2_r_21_0.8329_[0.39537486 0.9390134  0.9239991  0.98905045 0.9168321 ].png
img: 738 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1665_s_0.74_r_7_0.773_[0.43403307 0.72609454 0.9558375  0.81242853 0.9365148 ].png
img: 739 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1666_s_1.69_r_83_0.4554_[0.1284158  0.69715303 0.473666   0.9764589  0.00108099].png
img: 740 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1667_s_0.86_r_99_0.8418_[0.41203675 0.892821   0.9724968  0.98021024 0.9516204 ].png
img: 741 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1668_s_1.17_r_10_0.797_[0.3977301  0.9376464  0.83742505 0.99017835 0.8218754 ].png
img: 742 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1669_s_1.73_r_323_0.4936_[0.14388677 0.716183   0.5074893  0.96330404 0.13694622].png
img: 743 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_166_s_1.55_r_238_0.5947_[0.2672431  0.7984529  0.5796322  0.98191667 0.3463069 ].png
img: 744 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1670_s_1.01_r_92_0.839_[0.40390217 0.9228383  0.9450131  0.9847497  0.9386037 ].png
img: 745 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1671_s_0.84_r_217_0.8024_[0.40541208 0.836937   0.9537087  0.8839317  0.93194884].png
img: 746 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1672_s_0.52_r_315_0.3208_[0.37955713 0.38599312 0.07913946 0.32262102 0.4368989 ].png
img: 747 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1673_s_0.95_r_326_0.8398_[0.40290064 0.90864533 0.9568206  0.9748326  0.9556504 ].png
img: 748 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1674_s_1.41_r_327_0.7176_[0.3714683  0.9170832  0.6980166  0.9880879  0.61352783].png
img: 749 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1675_s_1.97_r_94_0.4112_[0.03379551 0.6219936  0.46161398 0.9385829  0.        ].png
img: 750 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1676_s_0.61_r_31_0.5319_[0.40674666 0.47868595 0.7439359  0.28966016 0.7406462 ].png
img: 751 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1677_s_0.97_r_2_0.8465_[0.40770277 0.91123784 0.96320885 0.990629   0.959828  ].png
img: 752 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1678_s_1.18_r_331_0.8397_[0.39547375 0.9213359  0.9469147  0.9896843  0.9449413 ].png
img: 753 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1679_s_1.88_r_310_0.4395_[0.08701813 0.66278285 0.4731605  0.9200276  0.0546648 ].png
img: 754 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_167_s_0.67_r_147_0.5631_[0.4350561  0.48123845 0.9124161  0.11868455 0.86801004].png
img: 755 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1680_s_1.7_r_296_0.4962_[0.16690545 0.7324708  0.50652045 0.9547848  0.12007357].png
img: 756 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1681_s_1.39_r_61_0.7344_[0.37562445 0.92289454 0.727831   0.9906055  0.65498704].png
img: 757 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1682_s_1.31_r_43_0.775_[0.39046052 0.9380166  0.7988065  0.98890233 0.7585918 ].png
img: 758 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1683_s_0.83_r_322_0.7464_[0.4155012  0.72679293 0.9352139  0.72832936 0.9262653 ].png
img: 759 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1684_s_0.7_r_52_0.5963_[0.42504716 0.51471853 0.93059623 0.24457456 0.8664954 ].png
img: 760 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1685_s_0.87_r_241_0.8216_[0.40882334 0.87615025 0.9451369  0.9450603  0.9329835 ].png
img: 761 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1686_s_2.0_r_180_0.3986_[0.00869266 0.6003602  0.45484257 0.9289611  0.        ].png
img: 762 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1687_s_0.88_r_313_0.8224_[0.4028682  0.88285077 0.9440071  0.9369727  0.9450772 ].png
img: 763 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1688_s_0.66_r_228_0.5481_[0.42748442 0.47917226 0.87744117 0.13982409 0.8167855 ].png
img: 764 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1689_s_1.42_r_237_0.6973_[0.36830348 0.90013325 0.6719104  0.9877073  0.5582197 ].png
img: 765 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_168_s_0.87_r_269_0.8427_[0.41210002 0.89958596 0.958733   0.9822922  0.9609314 ].png
img: 766 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1690_s_1.34_r_207_0.7846_[0.3913359  0.9217265  0.81949615 0.9891671  0.8012193 ].png
img: 767 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1691_s_1.22_r_317_0.8254_[0.3971497  0.93228674 0.9055657  0.98719704 0.9050091 ].png
img: 768 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1692_s_0.88_r_238_0.8192_[0.4106969  0.8640455  0.94745857 0.93621397 0.9373688 ].png
img: 769 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1693_s_0.53_r_148_0.3609_[0.38392535 0.35704133 0.36138365 0.17369126 0.5284993 ].png
img: 770 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1694_s_1.38_r_123_0.754_[0.38035002 0.9240759  0.7625451  0.99009407 0.7128185 ].png
img: 771 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1695_s_1.48_r_181_0.506_[2.7260560e-01 7.9816693e-01 4.7421545e-01 9.8389441e-01 8.9385838e-04].png
img: 772 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1696_s_0.98_r_210_0.8428_[0.4039084 0.9193007 0.9585564 0.980278  0.9517745].png
img: 773 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1697_s_0.8_r_223_0.756_[0.41531274 0.74638116 0.93620425 0.7632323  0.91861975].png
img: 774 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1698_s_1.05_r_252_0.8406_[0.40787715 0.91225696 0.94632137 0.98721826 0.9491054 ].png
img: 775 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1699_s_0.71_r_7_0.7279_[0.42959157 0.66363615 0.94948286 0.67869425 0.9180285 ].png
img: 776 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_169_s_1.13_r_59_0.8453_[0.3958541 0.9352996 0.9595004 0.9891566 0.9464774].png
img: 777 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_16_s_1.33_r_165_0.6642_[0.39619467 0.92330897 0.60436624 0.990565   0.406628  ].png
img: 778 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1700_s_1.93_r_42_0.4236_[0.07156051 0.64256364 0.46195868 0.90635014 0.03565983].png
img: 779 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1701_s_1.37_r_157_0.6937_[0.3908383  0.92089784 0.65105665 0.98866266 0.5172602 ].png
img: 780 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1702_s_1.45_r_101_0.574_[0.34106603 0.8703789  0.5160051  0.98752457 0.15505989].png
img: 781 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1703_s_0.95_r_110_0.8486_[0.40263182 0.9230433  0.9715066  0.9858243  0.96012706].png
img: 782 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1704_s_1.85_r_99_0.4305_[6.8398535e-02 6.5796512e-01 4.6907717e-01 9.5681101e-01 3.1100975e-05].png
img: 783 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1705_s_1.32_r_40_0.7834_[0.3827603  0.9374857  0.8192426  0.9879302  0.78955966].png
img: 784 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1706_s_1.9_r_31_0.4392_[0.09081681 0.66862    0.4727488  0.9248248  0.03881023].png
img: 785 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1707_s_1.07_r_89_0.8005_[0.40315828 0.9293033  0.8504904  0.9886047  0.83084   ].png
img: 786 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1708_s_1.37_r_28_0.7542_[0.38383693 0.93027806 0.7573678  0.9880066  0.71154314].png
img: 787 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1709_s_0.9_r_202_0.8393_[0.4079798  0.90702945 0.9561852  0.9812154  0.94386405].png
img: 788 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_170_s_1.45_r_351_0.5524_[0.3322017  0.86653745 0.49324578 0.9875361  0.08263961].png
img: 789 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1710_s_0.88_r_298_0.8304_[0.40799782 0.8871921  0.95742685 0.95242894 0.94682443].png
img: 790 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1711_s_0.85_r_104_0.8429_[0.40717548 0.9054706  0.9689168  0.97967356 0.95313317].png
img: 791 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1712_s_0.55_r_46_0.3942_[0.38170418 0.40391067 0.3813688  0.273888   0.5298835 ].png
img: 792 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1713_s_1.08_r_272_0.8018_[0.40487298 0.9223026  0.8509824  0.98277247 0.8482974 ].png
img: 793 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1714_s_1.52_r_61_0.602_[0.28455588 0.8192299  0.5805103  0.98464763 0.34081784].png
img: 794 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1715_s_0.54_r_125_0.3169_[0.37962675 0.35563737 0.14446305 0.23021539 0.47442794].png
img: 795 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1716_s_1.28_r_352_0.6254_[0.3951634  0.932905   0.5470618  0.98889816 0.26321346].png
img: 796 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1717_s_1.18_r_80_0.7412_[0.4024913  0.92377114 0.72838724 0.98630327 0.66526043].png
img: 797 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1718_s_1.02_r_216_0.8338_[0.39927372 0.9272019  0.9293963  0.9838011  0.92951953].png
img: 798 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1719_s_0.64_r_270_0.6176_[0.4346015  0.51798624 0.9282217  0.3299175  0.87750816].png
img: 799 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_171_s_0.64_r_324_0.534_[0.41753957 0.45818588 0.8743997  0.094403   0.8256746 ].png
img: 800 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1720_s_0.66_r_39_0.5403_[0.41851717 0.48618773 0.8361055  0.16199248 0.7985925 ].png
img: 801 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1721_s_0.99_r_132_0.8376_[0.40147465 0.9186493  0.94935054 0.9735085  0.9449253 ].png
img: 802 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1722_s_1.82_r_253_0.4429_[0.09708381 0.6796465  0.47478673 0.9544564  0.00860515].png
img: 803 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1723_s_1.83_r_314_0.4514_[0.09414067 0.6616047  0.48193446 0.93901944 0.08028462].png
img: 804 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1724_s_1.27_r_314_0.8056_[0.39274493 0.9312627  0.86217636 0.9890185  0.85291874].png
img: 805 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1725_s_0.52_r_223_0.3603_[0.37657216 0.38249615 0.20595665 0.3560237  0.4803745 ].png
img: 806 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1726_s_0.83_r_7_0.8349_[0.41343772 0.87467813 0.9598876  0.97862506 0.9476698 ].png
img: 807 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1727_s_1.11_r_152_0.8449_[0.4033574  0.923282   0.9582767  0.98986596 0.94994086].png
img: 808 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1728_s_0.77_r_132_0.672_[0.4256383  0.5983432  0.9531977  0.46664456 0.9163003 ].png
img: 809 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1729_s_1.91_r_62_0.438_[0.08847179 0.67114747 0.46487167 0.9353922  0.03032132].png
img: 810 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_172_s_1.09_r_162_0.8392_[0.40758342 0.92053384 0.9421846  0.9898077  0.93572223].png
img: 811 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1730_s_1.64_r_0_0.4551_[0.1289057  0.6966349  0.47117513 0.97877157 0.        ].png
img: 812 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1731_s_0.98_r_273_0.8457_[0.406777   0.91437775 0.9610211  0.98150706 0.9650084 ].png
img: 813 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1732_s_0.53_r_203_0.3903_[0.36685666 0.38489664 0.3761295  0.28769815 0.5361346 ].png
img: 814 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1733_s_1.28_r_111_0.7775_[0.3933746  0.9365447  0.79824215 0.9880692  0.77102673].png
img: 815 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1734_s_1.02_r_304_0.8342_[0.3976583  0.92388856 0.9304672  0.9825599  0.93661624].png
img: 816 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1735_s_1.64_r_121_0.5436_[0.19642377 0.75685465 0.54765666 0.9724687  0.24476177].png
img: 817 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1736_s_1.33_r_173_0.6117_[0.39918706 0.9232893  0.5336026  0.98803705 0.21438731].png
img: 818 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1737_s_1.59_r_108_0.5218_[0.22205105 0.7695827  0.5108992  0.9720335  0.13429518].png
img: 819 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1738_s_0.69_r_177_0.6893_[0.4477624 0.5955341 0.9482581 0.5564275 0.8987636].png
img: 820 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1739_s_1.1_r_208_0.8489_[0.40077063 0.9305106  0.9670543  0.9860032  0.9601327 ].png
img: 821 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_173_s_0.98_r_56_0.8388_[0.3973672  0.9250341  0.9491906  0.9820672  0.94043505].png
img: 822 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1740_s_0.88_r_331_0.8292_[0.41030076 0.8698136  0.95773816 0.95056766 0.95773333].png
img: 823 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1741_s_0.9_r_203_0.8387_[0.40837303 0.9004267  0.9608608  0.9766047  0.94720876].png
img: 824 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1742_s_1.45_r_316_0.6635_[0.34505638 0.8820421  0.6324129  0.9885171  0.46959516].png
img: 825 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1743_s_1.37_r_356_0.5755_[0.38583288 0.9250117  0.49298579 0.9882412  0.0852659 ].png
img: 826 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1744_s_0.5_r_336_0.3665_[0.40865713 0.3701649  0.40827784 0.13203509 0.5135135 ].png
img: 827 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1745_s_1.02_r_71_0.8377_[0.40498275 0.9126966  0.94669837 0.9871247  0.93706083].png
img: 828 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1746_s_0.99_r_156_0.8457_[0.407163   0.914472   0.9614388  0.98822373 0.9569908 ].png
img: 829 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1747_s_1.8_r_204_0.454_[0.11232492 0.6858128  0.48386496 0.9322646  0.05597023].png
img: 830 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1748_s_1.92_r_123_0.4333_[0.08555993 0.661343   0.47210512 0.90048975 0.04676677].png
img: 831 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1749_s_0.78_r_59_0.7394_[0.41341373 0.7003065  0.9595192  0.68305594 0.9406561 ].png
img: 832 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_174_s_1.96_r_274_0.4104_[3.404752e-02 6.207493e-01 4.603391e-01 9.369473e-01 9.240863e-06].png
img: 833 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1750_s_0.64_r_42_0.5169_[0.42239764 0.4649693  0.80359447 0.1276456  0.7660287 ].png
img: 834 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1751_s_1.7_r_1_0.4453_[0.10142803 0.67856234 0.4718923  0.97450995 0.        ].png
img: 835 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1752_s_0.79_r_90_0.838_[0.42199877 0.8672372  0.96995217 0.98047197 0.9504319 ].png
img: 836 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1753_s_1.84_r_47_0.4421_[0.09386175 0.6572999  0.46252635 0.9279967  0.06877492].png
img: 837 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1754_s_0.99_r_272_0.8478_[0.40641877 0.92161876 0.9642321  0.9852137  0.96152884].png
img: 838 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1755_s_1.28_r_345_0.7171_[0.39605388 0.9316618  0.68390214 0.9889666  0.58516407].png
img: 839 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1756_s_1.06_r_118_0.844_[0.400532   0.9304376  0.95656407 0.984739   0.9475166 ].png
img: 840 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1757_s_0.77_r_243_0.7307_[0.4276516  0.67903185 0.94977313 0.6674219  0.92981756].png
img: 841 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1758_s_1.67_r_170_0.4649_[0.15517783 0.7129405  0.47748604 0.9736041  0.00524258].png
img: 842 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1759_s_0.62_r_30_0.5403_[0.4191275  0.46078765 0.8750246  0.13086857 0.81591576].png
img: 843 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_175_s_1.95_r_119_0.4237_[0.07776896 0.6567915  0.46386278 0.89528674 0.02478396].png
img: 844 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1760_s_1.3_r_48_0.7961_[0.38820422 0.9374017  0.84371793 0.9903388  0.82077295].png
img: 845 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1761_s_1.57_r_307_0.5968_[0.23943007 0.78473496 0.59512126 0.98096395 0.38383374].png
img: 846 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1762_s_1.53_r_65_0.5766_[0.28617394 0.82584697 0.54373366 0.985042   0.2419858 ].png
img: 847 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1763_s_1.71_r_92_0.4435_[0.09657308 0.67266023 0.47217223 0.9759174  0.        ].png
img: 848 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1764_s_1.24_r_176_0.6436_[0.40343451 0.92722195 0.57370514 0.9881725  0.32567075].png
img: 849 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1765_s_0.64_r_64_0.5701_[0.43046683 0.48015484 0.9138374  0.1720661  0.8539591 ].png
img: 850 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1766_s_0.57_r_341_0.4456_[0.39284185 0.40861747 0.57294077 0.2459846  0.60773724].png
img: 851 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1767_s_1.88_r_356_0.4218_[0.04892714 0.6397964  0.46526006 0.95498705 0.        ].png
img: 852 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1768_s_0.93_r_97_0.8463_[0.40885144 0.90348184 0.9763638  0.9845757  0.9581533 ].png
img: 853 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1769_s_1.08_r_277_0.8371_[0.4050105  0.92134464 0.93701905 0.98516583 0.937143  ].png
img: 854 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_176_s_1.62_r_240_0.5386_[0.22475725 0.76882696 0.5309182  0.9700932  0.19835481].png
img: 855 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1770_s_1.76_r_357_0.4392_[0.08382455 0.6707866  0.47145438 0.9700652  0.        ].png
img: 856 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1771_s_1.79_r_7_0.4372_[7.9779632e-02 6.6615242e-01 4.7125566e-01 9.6853316e-01 2.8801523e-04].png
img: 857 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1772_s_0.57_r_48_0.4551_[0.3930972  0.44251338 0.5169482  0.32264307 0.60036653].png
img: 858 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1773_s_0.68_r_128_0.5701_[0.4413778  0.48011324 0.9316694  0.12981775 0.8674943 ].png
img: 859 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1774_s_1.8_r_129_0.4682_[0.11406883 0.69395876 0.49732888 0.94417375 0.09125888].png
img: 860 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1775_s_1.64_r_71_0.4967_[0.19338676 0.75006866 0.49223125 0.97152406 0.07620979].png
img: 861 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1776_s_1.98_r_73_0.4192_[0.05466411 0.6482856  0.46233496 0.9242944  0.006478  ].png
img: 862 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1777_s_0.76_r_263_0.7999_[0.42984182 0.7835966  0.9533442  0.8879824  0.9447893 ].png
img: 863 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1778_s_0.92_r_234_0.8383_[0.40194863 0.92226726 0.943162   0.983325   0.9406658 ].png
img: 864 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1779_s_0.98_r_137_0.848_[0.40225157 0.929384   0.9604715  0.98860824 0.95911306].png
img: 865 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_177_s_1.28_r_81_0.6538_[0.39555502 0.9282199  0.58899355 0.9873573  0.3689621 ].png
img: 866 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1780_s_0.8_r_232_0.7552_[0.41481012 0.7354634  0.95163965 0.7411176  0.93275887].png
img: 867 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1781_s_0.71_r_18_0.684_[0.42603114 0.61045915 0.9402782  0.550255   0.89293295].png
img: 868 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1782_s_1.28_r_157_0.7702_[0.39299756 0.9213891  0.7912449  0.9916085  0.75351053].png
img: 869 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1783_s_1.8_r_91_0.4323_[0.06488636 0.65289915 0.47227612 0.9712246  0.        ].png
img: 870 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1784_s_1.62_r_192_0.4826_[0.19053952 0.73661625 0.4818732  0.97370994 0.03013554].png
img: 871 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1785_s_1.92_r_294_0.4269_[0.07592045 0.6524094  0.4619904  0.9165881  0.02758534].png
img: 872 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1786_s_1.5_r_145_0.6096_[0.2966623  0.8304426  0.5860339  0.98514426 0.34996235].png
img: 873 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1787_s_0.69_r_141_0.5818_[0.43382508 0.50228024 0.9108245  0.20075019 0.86119646].png
img: 874 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1788_s_0.66_r_122_0.5766_[0.41853932 0.49407077 0.9196164  0.18930297 0.86166006].png
img: 875 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1789_s_1.39_r_185_0.5728_[0.38255173 0.90789485 0.498425   0.98754156 0.08776679].png
img: 876 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_178_s_0.75_r_172_0.784_[0.44198117 0.7336991  0.9658389  0.83428735 0.9440997 ].png
img: 877 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1790_s_1.06_r_166_0.8464_[0.40938517 0.91491765 0.96161664 0.99044216 0.9558214 ].png
img: 878 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1791_s_1.36_r_25_0.7481_[0.38487408 0.92006546 0.7512297  0.9895729  0.69490206].png
img: 879 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1792_s_1.87_r_9_0.4304_[6.197794e-02 6.531987e-01 4.697925e-01 9.669027e-01 9.154156e-05].png
img: 880 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1793_s_1.09_r_280_0.8372_[0.4036749  0.9235616  0.93550175 0.98558295 0.9374853 ].png
img: 881 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1794_s_0.51_r_333_0.369_[0.36756042 0.35903007 0.3907764  0.21588959 0.51171243].png
img: 882 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1795_s_1.97_r_141_0.4159_[0.0730909  0.64598125 0.4510229  0.8859631  0.023653  ].png
img: 883 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1796_s_0.84_r_4_0.8429_[0.4115433 0.8909513 0.965195  0.9850618 0.9618037].png
img: 884 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1797_s_0.56_r_291_0.4319_[0.37328392 0.41264272 0.46270558 0.32880914 0.58182335].png
img: 885 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1798_s_1.45_r_179_0.5226_[0.3125722  0.8329023  0.47572884 0.9850457  0.00652678].png
img: 886 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1799_s_0.55_r_187_0.4752_[0.3930063  0.4079303  0.62828183 0.29126155 0.6555864 ].png
img: 887 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_179_s_1.92_r_262_0.4182_[0.0488623  0.63843906 0.46467412 0.93894017 0.        ].png
img: 888 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_17_s_1.23_r_289_0.8036_[0.39963955 0.9339661  0.8516795  0.9865442  0.84615386].png
img: 889 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1800_s_1.23_r_42_0.8232_[0.39070556 0.9450698  0.9020645  0.9864766  0.8918419 ].png
img: 890 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1801_s_1.01_r_145_0.8268_[0.40028745 0.9193563  0.91192925 0.9822096  0.92016804].png
img: 891 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1802_s_0.71_r_254_0.7046_[0.4394073 0.6247464 0.9336155 0.6240174 0.9011791].png
img: 892 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1803_s_1.39_r_193_0.6348_[0.3893915  0.91536665 0.56872183 0.98745227 0.31315774].png
img: 893 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1804_s_2.0_r_282_0.3988_[0.01212237 0.6073096  0.4485395  0.9259842  0.        ].png
img: 894 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1805_s_1.94_r_316_0.4211_[0.06839418 0.6381609  0.4573518  0.89681447 0.04482232].png
img: 895 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1806_s_0.53_r_347_0.3842_[0.37142292 0.37694442 0.3670602  0.31986597 0.48550296].png
img: 896 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1807_s_1.29_r_118_0.816_[0.3941126  0.9340829  0.8866535  0.9906496  0.87467664].png
img: 897 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1808_s_0.52_r_227_0.3729_[0.360467   0.35763264 0.31639364 0.34499112 0.48516843].png
img: 898 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1809_s_1.97_r_331_0.4204_[0.07638338 0.65773946 0.4488745  0.9022679  0.01665677].png
img: 899 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_180_s_1.88_r_355_0.4243_[0.0504554  0.6426735  0.4680494  0.96016455 0.        ].png
img: 900 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1810_s_1.83_r_312_0.4509_[0.09790648 0.66392857 0.47712797 0.93770397 0.07772147].png
img: 901 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1811_s_0.81_r_223_0.7794_[0.40698358 0.7872026  0.9531964  0.8091979  0.9405422 ].png
img: 902 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1812_s_1.86_r_325_0.4532_[0.09850985 0.6800021  0.48475975 0.94455886 0.05804655].png
img: 903 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1813_s_0.9_r_353_0.8454_[0.4092291 0.8979603 0.9678615 0.9890519 0.9626869].png
img: 904 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1814_s_1.04_r_57_0.841_[0.39847136 0.92528284 0.95341873 0.98775107 0.94030136].png
img: 905 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1815_s_1.97_r_236_0.4225_[0.07137658 0.6503975  0.45736742 0.91142905 0.021872  ].png
img: 906 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1816_s_0.78_r_240_0.7237_[0.42633083 0.67048955 0.9451561  0.6455814  0.93094474].png
img: 907 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1817_s_0.54_r_72_0.4002_[0.39680025 0.3861932  0.4223987  0.2488763  0.5469351 ].png
img: 908 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1818_s_1.67_r_49_0.507_[0.16425072 0.73127776 0.51767194 0.96860796 0.15343413].png
img: 909 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1819_s_1.12_r_291_0.8471_[0.40002567 0.93503803 0.95665604 0.9864709  0.95710635].png
img: 910 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_181_s_1.82_r_106_0.4479_[0.09902911 0.68711007 0.4792174  0.95561266 0.01841307].png
img: 911 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1820_s_0.79_r_0_0.8375_[0.42158297 0.8636705  0.9625675  0.98272264 0.9568552 ].png
img: 912 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1821_s_1.36_r_227_0.7425_[0.38826716 0.9191854  0.7383583  0.98769796 0.67901045].png
img: 913 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1822_s_1.57_r_235_0.5755_[0.24608013 0.78628176 0.5666937  0.9748163  0.30385518].png
img: 914 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1823_s_0.78_r_224_0.7407_[0.41712135 0.71716595 0.93959814 0.71643573 0.91320896].png
img: 915 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1824_s_1.08_r_263_0.8285_[0.40573743 0.9186871  0.9156245  0.98670155 0.91559786].png
img: 916 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1825_s_1.64_r_193_0.4767_[0.18023741 0.72982776 0.47917113 0.972077   0.0219892 ].png
img: 917 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1826_s_0.62_r_95_0.5785_[0.43354025 0.4657475  0.9217085  0.20874871 0.8626743 ].png
img: 918 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1827_s_1.3_r_113_0.7894_[0.39202592 0.93609124 0.82694495 0.98802173 0.8040587 ].png
img: 919 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1828_s_1.33_r_126_0.7943_[0.38660744 0.9285665  0.8448556  0.9894244  0.8220595 ].png
img: 920 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1829_s_1.66_r_38_0.5292_[0.17156589 0.73531586 0.5389939  0.97321755 0.22685114].png
img: 921 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_182_s_0.58_r_289_0.4767_[0.4007812  0.4530609  0.55520403 0.35492748 0.6196533 ].png
img: 922 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1830_s_1.73_r_189_0.4477_[1.1089087e-01 6.8135720e-01 4.7522911e-01 9.7060841e-01 2.1385038e-04].png
img: 923 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1831_s_1.13_r_89_0.7233_[0.40383816 0.9268856  0.69698703 0.98603565 0.60285366].png
img: 924 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1832_s_1.84_r_26_0.451_[0.10779905 0.684576   0.481682   0.9296811  0.05126138].png
img: 925 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1833_s_0.7_r_96_0.6991_[0.44289818 0.6057805  0.9617314  0.5791109  0.90604115].png
img: 926 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1834_s_1.27_r_17_0.7483_[0.39600068 0.9327541  0.7389248  0.9883018  0.68530375].png
img: 927 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1835_s_1.12_r_296_0.8463_[0.3998203  0.93273735 0.9590285  0.9856842  0.9540452 ].png
img: 928 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1836_s_1.31_r_34_0.8072_[0.38385597 0.9334331  0.87282526 0.9898429  0.8560558 ].png
img: 929 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1837_s_0.8_r_256_0.8267_[0.4178148  0.8549125  0.95791715 0.9552317  0.9474985 ].png
img: 930 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1838_s_0.83_r_35_0.7736_[0.4091833  0.7868192  0.9316017  0.83274263 0.9075887 ].png
img: 931 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1839_s_1.02_r_36_0.8343_[0.39521208 0.9291058  0.935478   0.98241097 0.9291275 ].png
img: 932 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_183_s_1.66_r_63_0.5032_[0.1847192  0.7476057  0.5042825  0.96867007 0.11064877].png
img: 933 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1840_s_0.62_r_329_0.5459_[0.41577548 0.45757332 0.8785001  0.1478583  0.8296609 ].png
img: 934 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1841_s_0.97_r_228_0.8295_[0.4033377  0.91993725 0.9220202  0.98248917 0.91950697].png
img: 935 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1842_s_1.22_r_126_0.8359_[0.3927926  0.93554395 0.9379614  0.9885781  0.92483157].png
img: 936 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1843_s_1.45_r_242_0.6738_[0.3532395  0.8812315  0.64624274 0.988012   0.50009197].png
img: 937 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1844_s_1.34_r_357_0.5836_[0.39040592 0.92301023 0.501714   0.98758614 0.11508846].png
img: 938 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1845_s_1.45_r_138_0.6855_[0.35569596 0.89528215 0.66140574 0.9904417  0.5248489 ].png
img: 939 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1846_s_0.89_r_268_0.8448_[0.40983704 0.9070018  0.9616453  0.9828987  0.96239614].png
img: 940 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1847_s_1.19_r_312_0.8367_[0.39420462 0.94148123 0.93127775 0.98832697 0.92833585].png
img: 941 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1848_s_1.53_r_76_0.5228_[0.2678706  0.8053763  0.49047053 0.9825475  0.06786249].png
img: 942 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1849_s_1.84_r_76_0.4364_[0.08619253 0.67615455 0.46820423 0.95041835 0.00116374].png
img: 943 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_184_s_0.66_r_178_0.63_[0.44758528 0.51837265 0.9514935  0.34775114 0.88481367].png
img: 944 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1850_s_1.72_r_277_0.4476_[0.11159021 0.68221176 0.47252473 0.97020984 0.0013457 ].png
img: 945 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1851_s_1.88_r_267_0.4218_[0.04794454 0.6366869  0.46765447 0.9566387  0.        ].png
img: 946 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1852_s_1.35_r_257_0.6308_[0.3917996  0.9257665  0.55851424 0.9869868  0.2907191 ].png
img: 947 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1853_s_1.18_r_318_0.8437_[0.39730895 0.93339854 0.94932485 0.98977315 0.94849765].png
img: 948 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1854_s_1.0_r_72_0.8263_[0.40464365 0.8792771  0.95286965 0.9441262  0.9504208 ].png
img: 949 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1855_s_1.94_r_311_0.4239_[0.07289394 0.64129233 0.46344826 0.9058656  0.03605506].png
img: 950 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1856_s_1.5_r_356_0.5013_[0.25151378 0.78862864 0.4736799  0.9851287  0.00731504].png
img: 951 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1857_s_1.57_r_317_0.5713_[0.22625329 0.76792943 0.5646492  0.9832287  0.31439123].png
img: 952 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1858_s_0.51_r_184_0.3931_[0.37533054 0.3648743  0.39847046 0.31497782 0.5120013 ].png
img: 953 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1859_s_1.55_r_24_0.5794_[0.26232213 0.8033586  0.5612494  0.9850872  0.28511545].png
img: 954 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_185_s_1.86_r_150_0.4438_[0.10560553 0.680303   0.4737711  0.9259366  0.03338564].png
img: 955 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1860_s_1.45_r_178_0.5254_[0.3091128  0.83015645 0.48048133 0.9834769  0.02388034].png
img: 956 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1861_s_1.93_r_180_0.4162_[0.03209445 0.62126553 0.46881506 0.9587867  0.        ].png
img: 957 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1862_s_1.3_r_158_0.7413_[0.39448637 0.9209037  0.73235893 0.9899862  0.66869265].png
img: 958 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1863_s_2.0_r_120_0.3896_[9.7173471e-03 6.0626811e-01 4.3995282e-01 8.9220965e-01 4.4379747e-05].png
img: 959 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1864_s_0.99_r_268_0.8417_[0.40547344 0.923022   0.94728696 0.9852522  0.94724214].png
img: 960 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1865_s_1.31_r_358_0.5885_[0.3932385  0.92709225 0.5062165  0.98680043 0.12908368].png
img: 961 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1866_s_0.89_r_205_0.8389_[0.40521678 0.91385543 0.9571223  0.9772248  0.94119406].png
img: 962 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1867_s_0.69_r_329_0.5861_[0.42760435 0.5017489  0.92765653 0.16949406 0.90391093].png
img: 963 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1868_s_1.27_r_214_0.8245_[0.39493597 0.93159837 0.9077172  0.9893824  0.89886546].png
img: 964 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1869_s_1.35_r_93_0.5831_[0.38859034 0.92177975 0.5041113  0.9864845  0.11453307].png
img: 965 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_186_s_1.38_r_112_0.7117_[0.38800153 0.92934805 0.67856103 0.9887201  0.5739524 ].png
img: 966 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1870_s_0.71_r_328_0.6045_[0.42722577 0.51937646 0.93572664 0.23784299 0.90238374].png
img: 967 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1871_s_1.9_r_133_0.4369_[0.08501945 0.65580285 0.47421286 0.92503566 0.04428063].png
img: 968 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1872_s_1.91_r_192_0.4252_[5.9496988e-02 6.4441758e-01 4.6841469e-01 9.5313257e-01 6.1295374e-04].png
img: 969 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1873_s_0.93_r_145_0.8338_[0.4085827  0.8907951  0.955575   0.9674592  0.94665724].png
img: 970 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1874_s_1.82_r_79_0.4367_[8.3302408e-02 6.7075270e-01 4.6946070e-01 9.5989877e-01 1.1813983e-04].png
img: 971 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1875_s_0.74_r_197_0.7232_[0.43581313 0.6554925  0.9536011  0.66663414 0.9043572 ].png
img: 972 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1876_s_1.76_r_187_0.44_[0.09043326 0.6660195  0.47321984 0.97049344 0.        ].png
img: 973 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1877_s_0.86_r_53_0.797_[0.40931824 0.82240474 0.94258523 0.88727754 0.9233234 ].png
img: 974 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1878_s_1.96_r_31_0.4244_[0.07716779 0.6533673  0.46659446 0.8997278  0.02492077].png
img: 975 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1879_s_0.78_r_325_0.7073_[0.41919705 0.65046084 0.94778967 0.5799451  0.9390623 ].png
img: 976 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_187_s_1.98_r_341_0.4238_[0.06241202 0.65727484 0.45999843 0.93065876 0.00887269].png
img: 977 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1880_s_1.77_r_260_0.4413_[0.09808463 0.6784846  0.47046444 0.9583349  0.00104059].png
img: 978 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1881_s_0.79_r_12_0.8216_[0.41659582 0.8484999  0.95356584 0.9638285  0.9252769 ].png
img: 979 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1882_s_1.86_r_172_0.4284_[6.8603858e-02 6.5337378e-01 4.6827585e-01 9.5162654e-01 7.1615650e-05].png
img: 980 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1883_s_1.99_r_358_0.4081_[2.6928833e-02 6.1661541e-01 4.6026015e-01 9.3649846e-01 5.3748030e-05].png
img: 981 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1884_s_0.73_r_191_0.7623_[0.43544766 0.71216    0.961629   0.77174604 0.9306413 ].png
img: 982 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1885_s_1.96_r_117_0.4225_[0.07349741 0.6485898  0.4647308  0.8949362  0.03064008].png
img: 983 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1886_s_0.98_r_170_0.8513_[0.4113754  0.9091364  0.9748807  0.9912549  0.96975344].png
img: 984 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1887_s_1.92_r_347_0.4268_[0.05948891 0.6499018  0.46750286 0.9541445  0.00317662].png
img: 985 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1888_s_0.62_r_199_0.5475_[0.42131883 0.5032314  0.72797525 0.37021255 0.7147089 ].png
img: 986 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1889_s_1.83_r_1_0.4279_[5.2946661e-02 6.4315319e-01 4.7022644e-01 9.7310555e-01 4.2485848e-05].png
img: 987 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_188_s_1.14_r_190_0.8219_[0.40636647 0.9247747  0.896957   0.98797816 0.89359343].png
img: 988 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1890_s_0.69_r_18_0.6661_[0.427037   0.5939721  0.9188201  0.5148893  0.87576264].png
img: 989 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1891_s_1.0_r_123_0.6489_[0.39428958 0.7016207  0.7006331  0.66428465 0.7837227 ].png
img: 990 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1892_s_1.16_r_57_0.8484_[0.39400026 0.9431348  0.9642797  0.98968154 0.95089644].png
img: 991 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1893_s_0.82_r_90_0.8413_[0.4121841  0.89178085 0.96940553 0.97894734 0.9541718 ].png
img: 992 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1894_s_0.83_r_263_0.8399_[0.41461807 0.8888128  0.9602759  0.9839357  0.9520934 ].png
img: 993 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1895_s_0.72_r_132_0.6059_[0.43671286 0.5188794  0.94042397 0.24899668 0.88455606].png
img: 994 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1896_s_1.84_r_205_0.453_[0.10343867 0.6814034  0.48182303 0.9427914  0.05542055].png
img: 995 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1897_s_0.81_r_330_0.7691_[0.41892868 0.74249715 0.95169055 0.78079855 0.951682  ].png
img: 996 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1898_s_0.51_r_229_0.3394_[0.34177727 0.33589536 0.25613078 0.30933133 0.45370704].png
img: 997 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1899_s_1.15_r_147_0.852_[0.4011204  0.92699075 0.97571033 0.9898563  0.9664291 ].png
img: 998 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_189_s_1.44_r_62_0.684_[0.35795525 0.9011092  0.6538146  0.9904607  0.51641905].png
img: 999 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_18_s_1.65_r_81_0.4662_[0.15880528 0.7195755  0.47475627 0.9740482  0.00385939].png
img: 1000 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1900_s_0.52_r_283_0.3663_[0.35176173 0.35990793 0.3332025  0.27849928 0.50790083].png
img: 1001 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1901_s_1.09_r_188_0.834_[0.4086679  0.9193606  0.92734873 0.99022555 0.92448884].png
img: 1002 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1902_s_1.48_r_255_0.5587_[0.31098488 0.8402386  0.5118755  0.98562974 0.1448555 ].png
img: 1003 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1903_s_1.43_r_347_0.5786_[0.34905624 0.8784712  0.5153913  0.9884264  0.16175298].png
img: 1004 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1904_s_1.38_r_141_0.7493_[0.37980756 0.9188496  0.75797343 0.99067795 0.6993926 ].png
img: 1005 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1905_s_1.99_r_42_0.413_[0.06304628 0.6318074  0.45631245 0.8716367  0.04229708].png
img: 1006 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1906_s_1.41_r_147_0.7112_[0.3747543  0.9082139  0.69057256 0.99064213 0.59190845].png
img: 1007 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1907_s_0.63_r_212_0.5089_[0.4234427  0.4358655  0.8160767  0.08480375 0.784301  ].png
img: 1008 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1908_s_0.69_r_339_0.6393_[0.43226504 0.5518401  0.92921615 0.38265288 0.9003498 ].png
img: 1009 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1909_s_1.38_r_152_0.7208_[0.38420743 0.9160394  0.70232666 0.99073726 0.6106498 ].png
img: 1010 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_190_s_1.66_r_286_0.4809_[0.1717538  0.7302707  0.48724204 0.96454597 0.05062606].png
img: 1011 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1910_s_0.8_r_168_0.8419_[0.41887954 0.8789962  0.965605   0.98734635 0.9586586 ].png
img: 1012 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1911_s_1.74_r_283_0.4528_[0.12010023 0.69393945 0.47653037 0.96191126 0.01148818].png
img: 1013 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1912_s_1.07_r_180_0.7745_[0.4089017  0.9164735  0.7945665  0.98859185 0.76409835].png
img: 1014 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1913_s_1.53_r_278_0.5072_[0.24872632 0.780824   0.48408553 0.98309493 0.03912964].png
img: 1015 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1914_s_0.52_r_286_0.3954_[0.35758436 0.39504063 0.3429555  0.3556108  0.52565455].png
img: 1016 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1915_s_0.71_r_23_0.6687_[0.42638263 0.58939165 0.9425866  0.48414895 0.9007515 ].png
img: 1017 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1916_s_1.9_r_203_0.4398_[0.08725985 0.66989934 0.47714588 0.93883127 0.02587556].png
img: 1018 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1917_s_0.59_r_250_0.4835_[0.415969   0.43966562 0.6324538  0.2867988  0.64284706].png
img: 1019 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1918_s_0.74_r_217_0.6289_[0.43073058 0.55011505 0.93673086 0.32943165 0.8974527 ].png
img: 1020 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1919_s_1.42_r_134_0.687_[0.36216635 0.898546   0.655896   0.98970056 0.5288332 ].png
img: 1021 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_191_s_0.89_r_271_0.8437_[0.40907    0.9070783  0.9618109  0.9800009  0.96051306].png
img: 1022 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1920_s_1.43_r_35_0.7193_[0.35942703 0.89901793 0.7137075  0.9893631  0.6349288 ].png
img: 1023 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1921_s_0.83_r_296_0.7917_[0.41055316 0.8078305  0.95019686 0.86175674 0.92827946].png
img: 1024 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1922_s_1.8_r_34_0.4718_[0.12217296 0.6996845  0.49826708 0.93224996 0.1065743 ].png
img: 1025 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1923_s_1.24_r_56_0.8315_[0.39247495 0.9335232  0.9288703  0.98910916 0.9136531 ].png
img: 1026 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1924_s_0.99_r_257_0.8356_[0.4090653 0.9081039 0.941713  0.9849727 0.9342321].png
img: 1027 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1925_s_1.36_r_290_0.7127_[0.39416268 0.92341495 0.6789938  0.9863434  0.5807506 ].png
img: 1028 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1926_s_1.0_r_275_0.8593_[0.40766633 0.92631114 0.98481655 0.9943578  0.9832027 ].png
img: 1029 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1927_s_1.48_r_356_0.5167_[0.28732356 0.82261586 0.4742092  0.9866869  0.01279075].png
img: 1030 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1928_s_0.73_r_178_0.7563_[0.44360188 0.69072676 0.95964766 0.74271274 0.94502884].png
img: 1031 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1929_s_1.02_r_215_0.834_[0.3997487  0.9242509  0.93235797 0.9836513  0.930085  ].png
img: 1032 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_192_s_1.46_r_99_0.5538_[0.33145624 0.86042625 0.49827242 0.9869896  0.09196665].png
img: 1033 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1930_s_1.52_r_325_0.6144_[0.28630447 0.819638   0.59501296 0.9860838  0.38494432].png
img: 1034 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1931_s_1.93_r_20_0.4318_[0.07310623 0.6630212  0.46756324 0.93639207 0.01881884].png
img: 1035 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1932_s_2.0_r_16_0.3917_[0.01296423 0.60318744 0.44640788 0.89597124 0.        ].png
img: 1036 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1933_s_0.56_r_130_0.4033_[0.3925866  0.4030917  0.33290756 0.33348596 0.554466  ].png
img: 1037 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1934_s_0.68_r_73_0.652_[0.44057724 0.55637383 0.91809446 0.48320353 0.8616007 ].png
img: 1038 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1935_s_1.81_r_90_0.4284_[0.05331117 0.643735   0.47115284 0.97362363 0.        ].png
img: 1039 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1936_s_0.6_r_178_0.5773_[0.43163604 0.44674873 0.9254106  0.23062858 0.85186774].png
img: 1040 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1937_s_1.76_r_271_0.4325_[0.07179356 0.6542491  0.46903166 0.9673826  0.        ].png
img: 1041 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1938_s_1.69_r_34_0.5126_[0.1689233  0.73891306 0.5219607  0.95957774 0.17354798].png
img: 1042 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1939_s_0.56_r_183_0.5045_[0.4114082  0.40973923 0.7510413  0.23346259 0.71673346].png
img: 1043 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_193_s_1.74_r_37_0.4893_[0.14373179 0.71677446 0.5026574  0.9527909  0.13038793].png
img: 1044 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1940_s_1.47_r_226_0.6469_[0.32896218 0.85678387 0.61961335 0.9876805  0.4416923 ].png
img: 1045 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1941_s_1.24_r_341_0.759_[0.39891022 0.9309605  0.75871706 0.9889928  0.7172148 ].png
img: 1046 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1942_s_1.94_r_215_0.428_[0.08052257 0.64819413 0.46363845 0.9008194  0.04662534].png
img: 1047 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1943_s_1.95_r_210_0.4328_[0.08104466 0.66505456 0.4681894  0.9234013  0.02607202].png
img: 1048 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1944_s_0.86_r_128_0.8115_[0.40698647 0.8472707  0.96190673 0.90593845 0.9353652 ].png
img: 1049 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1945_s_0.77_r_209_0.7299_[0.4195015  0.69299805 0.9458352  0.68099886 0.9104056 ].png
img: 1050 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1946_s_0.52_r_329_0.3638_[0.37199587 0.38260534 0.26276994 0.31245872 0.48908108].png
img: 1051 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1947_s_1.43_r_239_0.6949_[0.3694204  0.8978402  0.6689739  0.98948544 0.5488486 ].png
img: 1052 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1948_s_0.62_r_214_0.5115_[0.42611384 0.45626664 0.75705546 0.16823688 0.7497871 ].png
img: 1053 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1949_s_0.58_r_233_0.4053_[0.42026272 0.39307627 0.5102785  0.10098483 0.6020134 ].png
img: 1054 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_194_s_1.28_r_18_0.7473_[0.39242166 0.93221194 0.7395841  0.98755336 0.68478703].png
img: 1055 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1950_s_1.47_r_107_0.6032_[0.32970074 0.8596964  0.5570434  0.986084   0.28354704].png
img: 1056 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1951_s_1.1_r_136_0.8476_[0.39982983 0.9376848  0.9603948  0.9890952  0.950901  ].png
img: 1057 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1952_s_1.19_r_66_0.8269_[0.39283553 0.933709   0.9160311  0.98719543 0.9045266 ].png
img: 1058 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1953_s_0.68_r_112_0.6333_[0.43722045 0.53689396 0.9425662  0.3536179  0.89596915].png
img: 1059 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1954_s_0.88_r_112_0.8378_[0.4073408 0.903652  0.9590996 0.9781192 0.9409401].png
img: 1060 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1955_s_0.66_r_226_0.5621_[0.42052346 0.495835   0.8815675  0.20519735 0.80720127].png
img: 1061 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1956_s_0.8_r_10_0.8323_[0.4120412  0.8657026  0.9650142  0.96346843 0.9551003 ].png
img: 1062 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1957_s_1.29_r_264_0.63_[0.39875913 0.9289271  0.5544889  0.98669004 0.2813163 ].png
img: 1063 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1958_s_1.72_r_287_0.4657_[0.13930154 0.709962   0.48267403 0.9567943  0.03970928].png
img: 1064 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1959_s_0.83_r_330_0.7833_[0.41571286 0.78040767 0.9468738  0.8351395  0.9384714 ].png
img: 1065 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_195_s_1.14_r_94_0.7525_[0.401771   0.93467253 0.7453949  0.98726183 0.693369  ].png
img: 1066 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1960_s_1.4_r_11_0.6002_[0.3770074  0.9052553  0.52795315 0.9883598  0.20257072].png
img: 1067 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1961_s_0.89_r_14_0.8449_[0.40037706 0.91793877 0.9642121  0.9836956  0.9583388 ].png
img: 1068 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1962_s_0.67_r_161_0.6463_[0.44193375 0.5564928  0.9189302  0.4599428  0.85433453].png
img: 1069 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1963_s_0.76_r_236_0.6798_[0.4242021  0.60843956 0.9495886  0.48698872 0.92973065].png
img: 1070 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1964_s_0.92_r_269_0.8472_[0.40638033 0.9157444  0.9642873  0.9823422  0.96704876].png
img: 1071 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1965_s_1.98_r_216_0.4172_[0.07367879 0.6463896  0.454276   0.88085014 0.03087035].png
img: 1072 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1966_s_1.66_r_322_0.5278_[0.18238102 0.74371916 0.5329193  0.96802086 0.21214032].png
img: 1073 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1967_s_0.89_r_294_0.8394_[0.40041974 0.9221543  0.95279074 0.97916853 0.94256324].png
img: 1074 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1968_s_0.65_r_266_0.623_[0.45313084 0.5133297  0.92959654 0.3581098  0.8609134 ].png
img: 1075 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1969_s_1.09_r_304_0.8482_[0.39787135 0.93231064 0.96520877 0.9836539  0.9619223 ].png
img: 1076 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_196_s_1.3_r_83_0.6255_[0.396441   0.93263286 0.5481556  0.9862671  0.26398763].png
img: 1077 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1970_s_1.46_r_315_0.6545_[0.33491424 0.8678363  0.6198824  0.98785466 0.46223974].png
img: 1078 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1971_s_1.12_r_302_0.8502_[0.39614302 0.9374885  0.96569544 0.9870646  0.9644217 ].png
img: 1079 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1972_s_0.85_r_80_0.8432_[0.40821138 0.9005637  0.96731    0.98676413 0.9531868 ].png
img: 1080 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1973_s_1.62_r_340_0.505_[0.21275726 0.7659925  0.49309584 0.9682587  0.0849217 ].png
img: 1081 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1974_s_0.63_r_302_0.5172_[0.41304943 0.44900423 0.82663625 0.09660316 0.80086964].png
img: 1082 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1975_s_1.9_r_161_0.4379_[0.08511432 0.6679665  0.47454923 0.9479899  0.01405138].png
img: 1083 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1976_s_0.62_r_354_0.5975_[0.43627566 0.48109567 0.90648466 0.32327825 0.840275  ].png
img: 1084 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1977_s_1.91_r_80_0.4228_[5.7880171e-02 6.4792293e-01 4.6482641e-01 9.4318551e-01 6.8109286e-05].png
img: 1085 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1978_s_1.22_r_223_0.823_[0.39783818 0.9309351  0.9013998  0.9876415  0.89743346].png
img: 1086 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1979_s_1.35_r_62_0.7451_[0.3818781  0.93124753 0.7429637  0.98976064 0.6797426 ].png
img: 1087 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_197_s_1.92_r_144_0.4335_[0.08752414 0.6638552  0.46323052 0.91765344 0.03546413].png
img: 1088 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1980_s_1.53_r_201_0.5658_[0.27810958 0.8049258  0.5378803  0.9820373  0.2260621 ].png
img: 1089 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1981_s_0.99_r_79_0.835_[0.40587842 0.9117836  0.9380745  0.9901814  0.9289282 ].png
img: 1090 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1982_s_1.74_r_333_0.4803_[0.14244027 0.71419114 0.49697956 0.9613875  0.08625823].png
img: 1091 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1983_s_1.09_r_298_0.8472_[0.4006668  0.927619   0.9635768  0.98442125 0.9597583 ].png
img: 1092 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1984_s_1.7_r_222_0.497_[0.1496612  0.7091814  0.51534593 0.964892   0.14578708].png
img: 1093 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1985_s_0.93_r_346_0.8468_[0.4104791  0.89707136 0.9686292  0.9908089  0.9670025 ].png
img: 1094 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1986_s_1.82_r_109_0.449_[0.10020392 0.6879165  0.4778264  0.9519914  0.02721972].png
img: 1095 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1987_s_1.7_r_260_0.4563_[0.13406368 0.7009315  0.47515684 0.9680232  0.00337585].png
img: 1096 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1988_s_0.82_r_99_0.8408_[0.41021183 0.89178526 0.9693549  0.978317   0.9541727 ].png
img: 1097 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1989_s_1.59_r_279_0.4822_[0.2020612  0.7463007  0.47604448 0.9760237  0.01046128].png
img: 1098 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_198_s_2.0_r_302_0.3912_[7.6826764e-03 6.0121155e-01 4.4314972e-01 9.0404099e-01 8.8705956e-06].png
img: 1099 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1990_s_1.13_r_359_0.7257_[0.40072486 0.929644   0.69764507 0.9864814  0.6139281 ].png
img: 1100 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1991_s_0.59_r_300_0.4713_[0.4090769  0.4418352  0.63082904 0.20250511 0.67244196].png
img: 1101 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1992_s_1.2_r_172_0.7162_[0.4037614  0.92482245 0.68200046 0.98709655 0.58344924].png
img: 1102 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1993_s_0.52_r_71_0.3801_[0.3778253  0.3510823  0.38275    0.28356236 0.50503886].png
img: 1103 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1994_s_0.8_r_166_0.8321_[0.42260715 0.85321283 0.96592927 0.9634221  0.9551403 ].png
img: 1104 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1995_s_1.72_r_220_0.4966_[0.14220312 0.7029895  0.5167216  0.9665877  0.15434545].png
img: 1105 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1996_s_1.67_r_60_0.5143_[0.18563756 0.7503732  0.5150976  0.9662131  0.15425558].png
img: 1106 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1997_s_0.92_r_92_0.8515_[0.4064049 0.9173947 0.977411  0.9875975 0.968827 ].png
img: 1107 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1998_s_1.27_r_311_0.8144_[0.39192078 0.93381566 0.88048637 0.9886863  0.87716126].png
img: 1108 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1999_s_1.33_r_13_0.6783_[0.3956295  0.9215209  0.62492734 0.98964125 0.45959756].png
img: 1109 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_199_s_1.51_r_46_0.6132_[0.28318295 0.8254795  0.5940214  0.9860493  0.37747064].png
img: 1110 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_19_s_0.74_r_319_0.6658_[0.42428735 0.58905745 0.9466889  0.44880095 0.9202089 ].png
img: 1111 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_1_s_1.61_r_307_0.5662_[0.2178621  0.76533955 0.56580895 0.97633106 0.30566773].png
img: 1112 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_200_s_1.68_r_93_0.45_[1.1867150e-01 6.8201077e-01 4.7321591e-01 9.7585791e-01 1.2564550e-04].png
img: 1113 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_201_s_1.97_r_112_0.4151_[0.06319313 0.6382971  0.46285248 0.8972575  0.0138139 ].png
img: 1114 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_202_s_0.71_r_201_0.6676_[0.43399253 0.58378434 0.9374296  0.47930938 0.9035879 ].png
img: 1115 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_203_s_0.54_r_3_0.4677_[0.3884754  0.39762008 0.6238392  0.27666748 0.65183574].png
img: 1116 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_204_s_1.62_r_47_0.5361_[0.18736812 0.7371425  0.536332   0.9815645  0.23806573].png
img: 1117 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_205_s_1.42_r_16_0.6373_[0.37286267 0.91122687 0.5763639  0.98688227 0.33916408].png
img: 1118 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_206_s_0.65_r_192_0.6377_[0.43972522 0.52350277 0.9518126  0.41122285 0.8622604 ].png
img: 1119 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_207_s_1.28_r_217_0.8174_[0.3864416  0.92362225 0.8974397  0.9892523  0.8903408 ].png
img: 1120 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_208_s_1.26_r_51_0.8207_[0.38731006 0.937474   0.9016296  0.9894364  0.88740087].png
img: 1121 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_209_s_0.93_r_268_0.8474_[0.41021112 0.9064022  0.96724975 0.9860257  0.96711296].png
img: 1122 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_20_s_1.65_r_205_0.5203_[0.20029056 0.74946696 0.5207337  0.9643044  0.16666232].png
img: 1123 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_210_s_0.87_r_213_0.8078_[0.4032428  0.8654428  0.93146574 0.9167663  0.92222905].png
img: 1124 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_211_s_0.77_r_217_0.6804_[0.41839677 0.63250303 0.92134905 0.5465732  0.88313156].png
img: 1125 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_212_s_1.38_r_22_0.7117_[0.3864112  0.92933995 0.67785066 0.98845446 0.5762084 ].png
img: 1126 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_213_s_0.73_r_139_0.632_[0.4303965  0.54421    0.9548727  0.30439895 0.92636997].png
img: 1127 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_214_s_1.57_r_58_0.5786_[0.25591707 0.8018356  0.56012404 0.98505145 0.29029715].png
img: 1128 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_215_s_1.79_r_53_0.474_[0.12200917 0.69982827 0.49958742 0.94883084 0.09997569].png
img: 1129 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_216_s_1.53_r_166_0.5248_[0.26844168 0.79772377 0.49496877 0.98364866 0.07936028].png
img: 1130 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_217_s_0.9_r_89_0.8455_[0.41228428 0.8979852  0.9703593  0.985605   0.9613668 ].png
img: 1131 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_218_s_1.1_r_305_0.849_[0.39548895 0.94030195 0.95885354 0.9862733  0.9638734 ].png
img: 1132 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_219_s_1.27_r_110_0.7837_[0.3966101 0.9329657 0.811368  0.9882826 0.7895182].png
img: 1133 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_21_s_0.53_r_194_0.4148_[0.3684109  0.38878244 0.40871555 0.36823174 0.5397989 ].png
img: 1134 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_220_s_1.02_r_20_0.8493_[0.40042546 0.9275293  0.97062474 0.9871703  0.9609078 ].png
img: 1135 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_221_s_1.32_r_247_0.7315_[0.3896903  0.91773206 0.71720207 0.9856047  0.64723825].png
img: 1136 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_222_s_1.53_r_146_0.6062_[0.28299272 0.81440055 0.5861761  0.9880141  0.35932714].png
img: 1137 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_223_s_0.95_r_0_0.8492_[0.40445736 0.9162247  0.96926236 0.98945516 0.96665245].png
img: 1138 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_224_s_0.82_r_238_0.7702_[0.4161824  0.7534645  0.9564408  0.7809245  0.94420123].png
img: 1139 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_225_s_1.68_r_290_0.4912_[0.17516153 0.7326084  0.49827206 0.96087265 0.08888637].png
img: 1140 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_226_s_1.66_r_19_0.4891_[0.18267214 0.74658954 0.4898924  0.96414304 0.06224286].png
img: 1141 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_227_s_0.56_r_173_0.4586_[0.4202502  0.39028972 0.64475507 0.19486009 0.64274955].png
img: 1142 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_228_s_1.47_r_245_0.6341_[0.33758128 0.85786766 0.5979787  0.9863783  0.39080027].png
img: 1143 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_229_s_0.69_r_69_0.6403_[0.42940792 0.5542813  0.9402419  0.39341122 0.88407177].png
img: 1144 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_22_s_0.7_r_36_0.5742_[0.42441654 0.49297997 0.9285051  0.15618142 0.8690354 ].png
img: 1145 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_230_s_1.32_r_65_0.7625_[0.38561785 0.93627185 0.7722952  0.9888641  0.72948056].png
img: 1146 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_231_s_0.94_r_310_0.8462_[0.3971099  0.9361136  0.95988464 0.97883654 0.95915014].png
img: 1147 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_232_s_1.74_r_72_0.4652_[0.13937536 0.71200824 0.48183906 0.9635137  0.02929346].png
img: 1148 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_233_s_0.65_r_201_0.5883_[0.4364217  0.49702388 0.88550854 0.28364268 0.83902407].png
img: 1149 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_234_s_1.85_r_220_0.4491_[0.09784303 0.6719895  0.47976518 0.9333577  0.0627671 ].png
img: 1150 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_235_s_1.01_r_301_0.8375_[0.3971866 0.9309946 0.9419611 0.9801949 0.9372221].png
img: 1151 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_236_s_0.7_r_2_0.7091_[0.43354413 0.6318366  0.9477185  0.61945873 0.91303766].png
img: 1152 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_237_s_1.19_r_251_0.7988_[0.40131223 0.91892326 0.8455136  0.98523873 0.8432032 ].png
img: 1153 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_238_s_0.63_r_128_0.484_[0.42727873 0.45993775 0.67257726 0.16833967 0.6917011 ].png
img: 1154 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_239_s_1.61_r_248_0.5063_[0.21932985 0.7597006  0.49606827 0.97310823 0.08330712].png
img: 1155 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_23_s_0.67_r_220_0.5723_[0.4261359  0.5109881  0.87409467 0.2422343  0.8081232 ].png
img: 1156 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_240_s_1.05_r_26_0.8455_[0.39776307 0.9276063  0.96286    0.98588765 0.95339274].png
img: 1157 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_241_s_1.0_r_227_0.6909_[0.39418533 0.71891564 0.79830277 0.696372   0.84683275].png
img: 1158 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_242_s_0.66_r_206_0.5681_[0.4252458  0.48539472 0.90784895 0.17029566 0.8518413 ].png
img: 1159 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_243_s_0.78_r_192_0.8293_[0.42008153 0.85806227 0.961766   0.9621471  0.9446181 ].png
img: 1160 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_244_s_1.28_r_352_0.6254_[0.3951634  0.932905   0.5470618  0.98889816 0.26321346].png
img: 1161 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_245_s_0.67_r_153_0.5953_[0.43797496 0.49626288 0.9462907  0.19787648 0.89819837].png
img: 1162 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_246_s_1.23_r_127_0.8344_[0.3879324  0.9347934  0.93487674 0.9888396  0.9256777 ].png
img: 1163 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_247_s_1.9_r_246_0.4396_[0.09084559 0.6688478  0.47294205 0.9454991  0.02005863].png
img: 1164 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_248_s_1.1_r_9_0.8168_[0.39888328 0.9342257  0.88219786 0.98521733 0.88343805].png
img: 1165 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_249_s_0.77_r_194_0.8014_[0.4350814  0.7799419  0.9592642  0.8990117  0.93351924].png
img: 1166 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_24_s_0.96_r_145_0.8432_[0.40714008 0.91315657 0.95929223 0.9873859  0.94898677].png
img: 1167 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_250_s_1.71_r_53_0.5_[0.1537522  0.725924   0.5134827  0.9606315  0.14615385].png
img: 1168 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_251_s_1.49_r_182_0.5047_[0.26923057 0.79075843 0.47475886 0.98556256 0.00321888].png
img: 1169 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_252_s_1.42_r_135_0.682_[0.36050105 0.8935581  0.65233076 0.98888105 0.514582  ].png
img: 1170 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_253_s_0.69_r_130_0.5559_[0.43043128 0.49114904 0.8819886  0.13974127 0.8362793 ].png
img: 1171 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_254_s_1.03_r_249_0.8435_[0.40548134 0.913632   0.95828307 0.98558164 0.954425  ].png
img: 1172 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_255_s_1.21_r_344_0.7405_[0.39732492 0.92822695 0.7234315  0.98846906 0.66486394].png
img: 1173 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_256_s_1.07_r_261_0.8338_[0.40514475 0.9230052  0.92610776 0.98731726 0.9274665 ].png
img: 1174 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_257_s_0.83_r_303_0.7789_[0.4106946  0.79560083 0.9270336  0.8378734  0.92330325].png
img: 1175 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_258_s_0.84_r_238_0.8031_[0.41415587 0.8165651  0.9592481  0.8789176  0.9467384 ].png
img: 1176 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_259_s_0.71_r_314_0.6146_[0.4163673  0.5497818  0.91861516 0.30705497 0.8814169 ].png
img: 1177 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_25_s_1.51_r_41_0.6287_[0.2868291  0.82676643 0.6131859  0.98843676 0.42839912].png
img: 1178 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_260_s_1.59_r_341_0.5155_[0.2272557  0.7739997  0.4997311  0.9771107  0.09950464].png
img: 1179 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_261_s_0.68_r_220_0.5689_[0.43628755 0.4939839  0.8894337  0.20130618 0.8235827 ].png
img: 1180 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_262_s_0.98_r_301_0.8395_[0.4014861  0.91638684 0.9500534  0.975707   0.95408565].png
img: 1181 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_263_s_1.09_r_57_0.8469_[0.39583895 0.9345981  0.9673591  0.98874664 0.9478817 ].png
img: 1182 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_264_s_0.56_r_190_0.4419_[0.38926467 0.38023207 0.5975524  0.20359795 0.6386802 ].png
img: 1183 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_265_s_0.73_r_180_0.8095_[0.44012555 0.786861   0.96034676 0.91663045 0.9435494 ].png
img: 1184 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_266_s_0.76_r_241_0.6798_[0.42918062 0.6028489  0.949637   0.48941717 0.92804503].png
img: 1185 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_267_s_1.66_r_102_0.4722_[0.16368665 0.7263026  0.48053986 0.96962535 0.02091641].png
img: 1186 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_268_s_0.86_r_245_0.8155_[0.4167219 0.8380965 0.9600062 0.9194061 0.9433025].png
img: 1187 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_269_s_1.62_r_314_0.5264_[0.17774513 0.7277246  0.5303397  0.98074603 0.21539335].png
img: 1188 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_26_s_1.21_r_96_0.7043_[0.39911255 0.9320132  0.6634617  0.98551536 0.5413109 ].png
img: 1189 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_270_s_1.02_r_12_0.8486_[0.40149313 0.9221156  0.9674667  0.98900044 0.9631381 ].png
img: 1190 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_271_s_1.49_r_217_0.666_[0.3135924  0.84344685 0.65878034 0.98521656 0.52881306].png
img: 1191 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_272_s_1.48_r_160_0.5777_[0.32817012 0.85129195 0.5273991  0.98923266 0.1922375 ].png
img: 1192 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_273_s_0.85_r_69_0.8306_[0.40971202 0.876752   0.958431   0.966974   0.9411737 ].png
img: 1193 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_274_s_1.13_r_350_0.7945_[0.4008492  0.92947716 0.83156395 0.9908854  0.8196802 ].png
img: 1194 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_275_s_1.51_r_248_0.5696_[0.2975467  0.82673687 0.53252316 0.9840077  0.20734847].png
img: 1195 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_276_s_1.41_r_44_0.7201_[0.37096003 0.9203697  0.70370066 0.9909398  0.61441296].png
img: 1196 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_277_s_1.41_r_169_0.5837_[0.37710863 0.90742904 0.5101459  0.98860645 0.13506137].png
img: 1197 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_278_s_0.56_r_319_0.4158_[0.3780138  0.41244578 0.42188394 0.32443836 0.5423479 ].png
img: 1198 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_279_s_1.86_r_19_0.439_[0.0906354  0.68264586 0.47103438 0.9404559  0.01024087].png
img: 1199 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_27_s_1.72_r_336_0.4753_[0.15444309 0.722527   0.48543423 0.960404   0.05355473].png
img: 1200 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_280_s_1.83_r_87_0.4287_[6.1063141e-02 6.4758271e-01 4.6890667e-01 9.6598941e-01 4.2496678e-05].png
img: 1201 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_281_s_0.77_r_212_0.7095_[0.42358437 0.6561973  0.9460097  0.61073846 0.9111445 ].png
img: 1202 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_282_s_1.08_r_221_0.8477_[0.40140784 0.9304187  0.96182126 0.9871629  0.9577313 ].png
img: 1203 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_283_s_1.86_r_200_0.439_[0.09326062 0.6694983  0.47533643 0.9389346  0.01791945].png
img: 1204 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_284_s_1.18_r_172_0.7346_[0.406635  0.9255489 0.7126595 0.9883724 0.6399305].png
img: 1205 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_285_s_1.15_r_8_0.7868_[0.40181077 0.92557657 0.81723493 0.9870658  0.80252534].png
img: 1206 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_286_s_1.56_r_163_0.5212_[0.2503917  0.7827401  0.4992541  0.9814248  0.09206677].png
img: 1207 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_287_s_0.74_r_195_0.76_[0.43716684 0.7084054  0.9559875  0.7820721  0.9162231 ].png
img: 1208 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_288_s_1.8_r_3_0.4339_[0.06688605 0.6589605  0.47208095 0.97144973 0.        ].png
img: 1209 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_289_s_0.52_r_359_0.431_[0.3860313  0.3977098  0.47580963 0.33471727 0.56057084].png
img: 1210 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_28_s_0.93_r_206_0.8384_[0.40470523 0.91309196 0.95462734 0.97520185 0.9445667 ].png
img: 1211 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_290_s_0.61_r_89_0.586_[0.4446263  0.46648556 0.9345729  0.21061264 0.8735307 ].png
img: 1212 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_291_s_1.06_r_129_0.8492_[0.40006945 0.9326577  0.96739966 0.98771423 0.95834625].png
img: 1213 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_292_s_0.87_r_277_0.843_[0.40917137 0.903795   0.9623928  0.9799443  0.9594946 ].png
img: 1214 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_293_s_1.27_r_121_0.8243_[0.38720477 0.93366516 0.9097828  0.9897515  0.90113634].png
img: 1215 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_294_s_0.72_r_122_0.6082_[0.43736798 0.52082056 0.9321214  0.26594383 0.8847008 ].png
img: 1216 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_295_s_1.46_r_298_0.6825_[0.35386765 0.8885364  0.6568959  0.98789835 0.5251963 ].png
img: 1217 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_296_s_1.31_r_120_0.8105_[0.3901813  0.9339062  0.8774757  0.99044937 0.8602573 ].png
img: 1218 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_297_s_1.74_r_223_0.4811_[0.13432047 0.70107394 0.5006287  0.95757073 0.11177195].png
img: 1219 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_298_s_0.9_r_276_0.8451_[0.4091114  0.9062893  0.96532905 0.98302305 0.96170574].png
img: 1220 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_299_s_0.76_r_133_0.6641_[0.42224553 0.59446436 0.94720966 0.43961382 0.91712326].png
img: 1221 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_29_s_1.6_r_6_0.4774_[0.18649937 0.7372457  0.4753586  0.98239166 0.00563083].png
img: 1222 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_2_s_0.89_r_270_0.845_[0.41003433 0.9073475  0.9630498  0.982453   0.96214914].png
img: 1223 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_300_s_1.29_r_199_0.7613_[0.39850873 0.9214411  0.76841915 0.987806   0.73015606].png
img: 1224 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_301_s_0.86_r_213_0.8259_[0.41033092 0.8791854  0.94940215 0.9586864  0.93183774].png
img: 1225 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_302_s_1.18_r_174_0.7141_[0.4056381  0.92471504 0.6773654  0.98951006 0.5731646 ].png
img: 1226 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_303_s_0.67_r_324_0.5763_[0.4184608  0.49815872 0.9139668  0.18082409 0.87028205].png
img: 1227 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_304_s_1.4_r_163_0.6271_[0.38847053 0.9135476  0.55676854 0.9898186  0.2868382 ].png
img: 1228 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_305_s_1.75_r_301_0.4829_[0.13717104 0.7116155  0.5008676  0.9544238  0.11049673].png
img: 1229 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_306_s_1.87_r_188_0.4266_[6.1197586e-02 6.4657605e-01 4.6624771e-01 9.5887154e-01 1.4204257e-04].png
img: 1230 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_307_s_1.93_r_287_0.4248_[0.06597965 0.64779747 0.4659769  0.9361131  0.00804192].png
img: 1231 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_308_s_1.37_r_100_0.6194_[0.3902323  0.92364305 0.5445713  0.98880327 0.24990585].png
img: 1232 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_309_s_1.27_r_215_0.8234_[0.39400685 0.93244946 0.90465605 0.9888138  0.8972716 ].png
img: 1233 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_30_s_1.55_r_38_0.6056_[0.25733075 0.80305046 0.59668183 0.9850391  0.38572207].png
img: 1234 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_310_s_1.67_r_3_0.4524_[0.1237089  0.69349223 0.46988213 0.97479653 0.        ].png
img: 1235 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_311_s_1.51_r_340_0.5596_[0.29450136 0.8313714  0.51764166 0.98451376 0.1698572 ].png
img: 1236 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_312_s_0.75_r_332_0.6777_[0.43383205 0.5951427  0.94514453 0.4866349  0.92783445].png
img: 1237 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_313_s_1.14_r_123_0.8481_[0.3957821  0.94341743 0.96297044 0.98765415 0.950613  ].png
img: 1238 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_314_s_0.73_r_199_0.7136_[0.4301307  0.65136683 0.94552445 0.6362816  0.90482926].png
img: 1239 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_315_s_1.35_r_72_0.6575_[0.3899285  0.93518037 0.5912178  0.9897782  0.3815224 ].png
img: 1240 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_316_s_1.26_r_85_0.6423_[0.39670438 0.93127847 0.5726116  0.9847083  0.3263027 ].png
img: 1241 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_317_s_1.18_r_313_0.8335_[0.39675686 0.9338773  0.9244242  0.98811626 0.9244475 ].png
img: 1242 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_318_s_1.99_r_100_0.4125_[0.04318603 0.6276615  0.45854893 0.92773086 0.00512435].png
img: 1243 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_319_s_1.85_r_55_0.4533_[0.10440815 0.68737674 0.4838084  0.9463373  0.04453974].png
img: 1244 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_31_s_0.99_r_284_0.8467_[0.4042354 0.9260595 0.9586643 0.9854617 0.9592295].png
img: 1245 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_320_s_0.73_r_163_0.7218_[0.43888864 0.64430386 0.9571733  0.65433633 0.9143727 ].png
img: 1246 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_321_s_1.41_r_140_0.7225_[0.37310016 0.9136148  0.71132237 0.9902672  0.62408644].png
img: 1247 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_322_s_1.22_r_70_0.7872_[0.39701635 0.92911863 0.8224824  0.98668283 0.80046993].png
img: 1248 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_323_s_1.74_r_349_0.4512_[0.11774176 0.6986277  0.47373953 0.96272296 0.00313248].png
img: 1249 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_324_s_1.89_r_152_0.4422_[0.09535944 0.6743116  0.47657952 0.9380982  0.02647441].png
img: 1250 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_325_s_1.74_r_222_0.4836_[0.1315833  0.69085395 0.5066049  0.96310544 0.1258706 ].png
img: 1251 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_326_s_0.54_r_92_0.4339_[0.40599275 0.38679036 0.5523366  0.20272185 0.62172925].png
img: 1252 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_327_s_1.84_r_168_0.4344_[8.0226369e-02 6.6220522e-01 4.7084150e-01 9.5846808e-01 6.2845655e-05].png
img: 1253 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_328_s_0.75_r_164_0.7585_[0.4439472  0.6941001  0.9597396  0.7704093  0.92442137].png
img: 1254 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_329_s_1.0_r_232_0.6556_[0.39391917 0.6956257  0.72512364 0.6578859  0.8054768 ].png
img: 1255 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_32_s_1.0_r_144_0.6443_[0.39658213 0.68039596 0.7187594  0.63149834 0.79419684].png
img: 1256 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_330_s_1.07_r_346_0.8402_[0.40051472 0.9316389  0.9376066  0.9892433  0.9417505 ].png
img: 1257 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_331_s_1.73_r_159_0.468_[0.14308368 0.70898    0.48691    0.96381825 0.03719606].png
img: 1258 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_332_s_0.8_r_206_0.7642_[0.41264582 0.7567716  0.95346344 0.77141666 0.9267029 ].png
img: 1259 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_333_s_0.76_r_176_0.8349_[0.43258512 0.8433405  0.9638373  0.98022306 0.95428133].png
img: 1260 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_334_s_1.99_r_151_0.4178_[0.07412551 0.6533697  0.4528364  0.89566255 0.01303803].png
img: 1261 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_335_s_0.57_r_339_0.4719_[0.40737167 0.4433234  0.6044332  0.2685557  0.6360477 ].png
img: 1262 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_336_s_0.97_r_191_0.8486_[0.4092369  0.91306233 0.97076    0.9872389  0.9628563 ].png
img: 1263 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_337_s_1.12_r_113_0.8473_[0.39889336 0.9386997  0.958305   0.9883446  0.9520868 ].png
img: 1264 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_338_s_0.84_r_270_0.8417_[0.4131847  0.8956669  0.9633333  0.98015815 0.9559461 ].png
img: 1265 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_339_s_0.91_r_92_0.8483_[0.4070268  0.91354483 0.9725733  0.98703045 0.9614982 ].png
img: 1266 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_33_s_1.97_r_65_0.422_[0.07358795 0.6515629  0.46054286 0.9059078  0.01861234].png
img: 1267 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_340_s_0.66_r_54_0.5435_[0.42200062 0.46236122 0.91280276 0.07590596 0.8442821 ].png
img: 1268 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_341_s_1.72_r_143_0.4952_[0.15229045 0.7140847  0.50861084 0.9614019  0.13951541].png
img: 1269 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_342_s_0.87_r_60_0.8024_[0.4085038 0.8156813 0.9673108 0.8696413 0.9510897].png
img: 1270 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_343_s_1.45_r_34_0.7001_[0.34706613 0.89273083 0.6874793  0.9890719  0.5842041 ].png
img: 1271 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_344_s_1.04_r_191_0.8509_[0.40913838 0.914547   0.973956   0.9896205  0.9674392 ].png
img: 1272 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_345_s_0.51_r_335_0.3376_[0.3816323  0.34920198 0.34000257 0.13882983 0.47857904].png
img: 1273 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_346_s_0.87_r_34_0.8221_[0.40280578 0.8731787  0.9564281  0.9384415  0.9397526 ].png
img: 1274 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_347_s_1.74_r_106_0.4609_[0.1309791  0.7046872  0.48123664 0.9630726  0.0246585 ].png
img: 1275 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_348_s_1.12_r_45_0.8441_[0.3948345  0.942245   0.95357156 0.9889318  0.9408781 ].png
img: 1276 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_349_s_0.63_r_117_0.5356_[0.430642   0.46224624 0.84152484 0.13858967 0.804941  ].png
img: 1277 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_34_s_1.44_r_324_0.6989_[0.36012986 0.90095764 0.67619693 0.98918366 0.5681961 ].png
img: 1278 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_350_s_1.96_r_95_0.4112_[0.03525114 0.62838614 0.4611108  0.9310554  0.        ].png
img: 1279 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_351_s_1.48_r_212_0.666_[0.32430577 0.8541782  0.65226895 0.98591524 0.51324475].png
img: 1280 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_352_s_1.48_r_37_0.6691_[0.32170126 0.86956435 0.65059066 0.98729163 0.5165265 ].png
img: 1281 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_353_s_1.89_r_158_0.4398_[0.08756837 0.66836005 0.47577602 0.9534566  0.01367887].png
img: 1282 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_354_s_1.9_r_182_0.4203_[0.04160893 0.62868667 0.468461   0.962963   0.        ].png
img: 1283 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_355_s_1.82_r_336_0.4568_[0.11438517 0.69435906 0.4797888  0.9578614  0.03766781].png
img: 1284 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_356_s_1.1_r_101_0.8381_[0.401216   0.93384916 0.9392054  0.9888546  0.92739457].png
img: 1285 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_357_s_0.92_r_238_0.8386_[0.40435198 0.915556   0.9468786  0.98238915 0.9436241 ].png
img: 1286 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_358_s_1.22_r_193_0.778_[0.40343156 0.9291693  0.7990997  0.98695344 0.7713175 ].png
img: 1287 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_359_s_1.64_r_132_0.5236_[0.17829199 0.7301236  0.5304408  0.9762616  0.20279232].png
img: 1288 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_35_s_1.93_r_323_0.4319_[0.07812205 0.66004354 0.46611863 0.91290396 0.04234475].png
img: 1289 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_360_s_1.26_r_87_0.6325_[0.39599696 0.93125343 0.5599748  0.9846838  0.2906656 ].png
img: 1290 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_361_s_1.06_r_158_0.8447_[0.40632838 0.92045283 0.95383334 0.9908086  0.95218766].png
img: 1291 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_362_s_1.4_r_315_0.6951_[0.3799527  0.9130425  0.65663135 0.9894771  0.53647506].png
img: 1292 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_363_s_1.46_r_220_0.6846_[0.34091803 0.87520593 0.6706524  0.9876548  0.54865175].png
img: 1293 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_364_s_1.97_r_166_0.418_[5.4088101e-02 6.3945991e-01 4.6134645e-01 9.3502939e-01 1.5544705e-04].png
img: 1294 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_365_s_1.43_r_19_0.6498_[0.37192065 0.90186775 0.5963912  0.98708034 0.39184096].png
img: 1295 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_366_s_1.09_r_121_0.8474_[0.39961484 0.93595713 0.96342665 0.98758274 0.9506212 ].png
img: 1296 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_367_s_1.9_r_94_0.4208_[0.04466651 0.63256276 0.46729997 0.95944107 0.        ].png
img: 1297 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_368_s_1.6_r_10_0.4813_[0.19615372 0.7478278  0.47444427 0.9761245  0.01177644].png
img: 1298 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_369_s_1.15_r_234_0.843_[0.3980581  0.9292538  0.95344186 0.9874147  0.9466037 ].png
img: 1299 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_36_s_1.65_r_162_0.4859_[0.18738864 0.7381075  0.4876758  0.96839315 0.04816436].png
img: 1300 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_370_s_1.19_r_40_0.8396_[0.39120212 0.9453532  0.94139355 0.988592   0.93170154].png
img: 1301 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_371_s_2.0_r_117_0.3911_[7.5270464e-03 5.9732097e-01 4.4762611e-01 9.0301603e-01 9.7703960e-05].png
img: 1302 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_372_s_1.95_r_243_0.4319_[0.08168135 0.6610671  0.47062728 0.9244694  0.0214419 ].png
img: 1303 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_373_s_0.51_r_317_0.3038_[0.3567994  0.3317019  0.25225574 0.13279319 0.44568264].png
img: 1304 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_374_s_1.77_r_167_0.4465_[1.0721251e-01 6.8233889e-01 4.7509015e-01 9.6721691e-01 8.7248167e-04].png
img: 1305 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_375_s_1.04_r_226_0.8437_[0.40301663 0.9240961  0.95368356 0.986888   0.9507499 ].png
img: 1306 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_376_s_1.1_r_170_0.8308_[0.40572155 0.92470247 0.92080665 0.9907621  0.9121028 ].png
img: 1307 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_377_s_0.94_r_20_0.846_[0.39764148 0.9303804  0.9622836  0.9859246  0.9535535 ].png
img: 1308 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_378_s_1.42_r_100_0.5804_[0.3675792  0.9022443  0.50975543 0.9866023  0.13564885].png
img: 1309 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_379_s_0.76_r_120_0.7209_[0.41731825 0.674905   0.9548779  0.62821424 0.92928416].png
img: 1310 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_37_s_1.74_r_79_0.4509_[0.11667845 0.6948339  0.47475347 0.9651082  0.00315554].png
img: 1311 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_380_s_0.81_r_19_0.8094_[0.41409564 0.8265046  0.95373374 0.9215382  0.93103623].png
img: 1312 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_381_s_0.82_r_301_0.804_[0.4048662  0.8377378  0.95143926 0.8837295  0.94242346].png
img: 1313 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_382_s_1.34_r_120_0.7934_[0.38457847 0.9283828  0.84311295 0.9883381  0.8225216 ].png
img: 1314 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_383_s_0.65_r_68_0.5825_[0.43627304 0.49402496 0.88306844 0.28315198 0.81620735].png
img: 1315 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_384_s_0.97_r_43_0.8459_[0.39793053 0.92651576 0.9676614  0.9834281  0.95417297].png
img: 1316 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_385_s_1.71_r_111_0.4799_[0.14801702 0.72076887 0.49547637 0.95947635 0.07588224].png
img: 1317 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_386_s_1.23_r_298_0.8289_[0.3934533  0.93245095 0.91619533 0.98820287 0.9140983 ].png
img: 1318 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_387_s_1.93_r_262_0.4202_[4.6197522e-02 6.3690192e-01 4.6694216e-01 9.5068008e-01 2.8532299e-05].png
img: 1319 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_388_s_1.57_r_215_0.5931_[0.2488996  0.7875192  0.5889087  0.97891784 0.36125317].png
img: 1320 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_389_s_0.67_r_343_0.6325_[0.43236202 0.5490558  0.9080102  0.43359327 0.83950365].png
img: 1321 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_38_s_1.11_r_43_0.8459_[0.39844194 0.9301135  0.9626401  0.9855922  0.95254266].png
img: 1322 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_390_s_1.17_r_16_0.8173_[0.39736116 0.94002944 0.88300484 0.9899078  0.8759676 ].png
img: 1323 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_391_s_1.29_r_254_0.6751_[0.39846668 0.92613983 0.6185952  0.9867711  0.44533446].png
img: 1324 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_392_s_1.84_r_102_0.4345_[7.6870404e-02 6.6599911e-01 4.7077325e-01 9.5886475e-01 1.3628692e-04].png
img: 1325 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_393_s_1.88_r_62_0.4427_[0.09433071 0.6774614  0.4734766  0.9425146  0.025485  ].png
img: 1326 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_394_s_0.58_r_219_0.4808_[0.41402084 0.4445499  0.5676275  0.35213292 0.6259053 ].png
img: 1327 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_395_s_1.86_r_113_0.4431_[0.09552719 0.6759045  0.4800235  0.9290475  0.03515922].png
img: 1328 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_396_s_1.53_r_245_0.5809_[0.28653526 0.8138775  0.552427   0.98092574 0.27076918].png
img: 1329 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_397_s_1.36_r_232_0.7635_[0.38243547 0.9104955  0.7870707  0.9873269  0.750404  ].png
img: 1330 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_398_s_1.88_r_227_0.4366_[0.08520352 0.64998555 0.4669598  0.9285997  0.05219758].png
img: 1331 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_399_s_1.11_r_148_0.8447_[0.40425253 0.92621064 0.9570656  0.99002504 0.94599926].png
img: 1332 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_39_s_1.18_r_326_0.8402_[0.395241   0.9279615  0.94485384 0.9900777  0.9427671 ].png
img: 1333 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_3_s_1.3_r_80_0.6336_[0.39554316 0.933063   0.5577195  0.98707855 0.29440257].png
img: 1334 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_400_s_1.51_r_335_0.5964_[0.2969828  0.83389074 0.56217396 0.98684937 0.30208123].png
img: 1335 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_401_s_1.74_r_255_0.4561_[0.1290563  0.70289767 0.47654346 0.95780677 0.01418248].png
img: 1336 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_402_s_1.72_r_14_0.461_[0.13607778 0.70656496 0.47732747 0.96776474 0.01740998].png
img: 1337 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_403_s_1.34_r_48_0.7645_[0.38434625 0.9325712  0.7808081  0.9889717  0.7358254 ].png
img: 1338 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_404_s_1.34_r_198_0.7066_[0.39683086 0.923819   0.66825044 0.9885617  0.55565566].png
img: 1339 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_405_s_1.79_r_283_0.4418_[0.09623967 0.6757798  0.4709198  0.9616249  0.00444262].png
img: 1340 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_406_s_0.81_r_325_0.7427_[0.4149523  0.7163898  0.93886566 0.71375847 0.9294436 ].png
img: 1341 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_407_s_1.57_r_55_0.5788_[0.24027753 0.7896256  0.5691024  0.9813459  0.31357354].png
img: 1342 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_408_s_1.72_r_247_0.4713_[0.15677889 0.7206383  0.48324192 0.95443755 0.04126109].png
img: 1343 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_409_s_0.68_r_30_0.5812_[0.42704502 0.48943081 0.9369524  0.17509878 0.8772449 ].png
img: 1344 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_40_s_1.1_r_303_0.8484_[0.395683   0.9362919  0.9604632  0.9853781  0.96398187].png
img: 1345 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_410_s_1.77_r_96_0.4407_[0.08964542 0.6724861  0.47284344 0.96842843 0.        ].png
img: 1346 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_411_s_0.69_r_45_0.5729_[0.42607448 0.49220613 0.930527   0.13456325 0.8812706 ].png
img: 1347 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_412_s_0.58_r_111_0.4478_[0.4030553  0.42479518 0.53743637 0.2696942  0.60409695].png
img: 1348 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_413_s_1.21_r_227_0.8301_[0.39462882 0.9286628  0.92141646 0.98817015 0.91754085].png
img: 1349 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_414_s_1.91_r_206_0.4379_[0.08700568 0.66770524 0.4775774  0.9304071  0.02684858].png
img: 1350 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_415_s_1.92_r_103_0.4255_[6.0598429e-02 6.5058297e-01 4.6569666e-01 9.5035058e-01 2.2133901e-04].png
img: 1351 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_416_s_1.38_r_184_0.5728_[0.3875683  0.9106682  0.49527743 0.9852349  0.08513254].png
img: 1352 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_417_s_1.72_r_358_0.4427_[0.09403356 0.6742504  0.4711259  0.973928   0.        ].png
img: 1353 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_418_s_0.88_r_67_0.8374_[0.40807626 0.8900641  0.9626884  0.9777495  0.9481863 ].png
img: 1354 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_419_s_1.46_r_266_0.5269_[0.31078538 0.8349665  0.47967058 0.9849202  0.02424141].png
img: 1355 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_41_s_1.99_r_78_0.4107_[0.04668587 0.6299555  0.45612493 0.91919416 0.0014792 ].png
img: 1356 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_420_s_0.75_r_4_0.813_[0.4346092  0.7989896  0.95521486 0.9328564  0.9433962 ].png
img: 1357 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_421_s_0.88_r_98_0.8436_[0.41086972 0.8983669  0.9718427  0.9826726  0.95402145].png
img: 1358 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_422_s_1.9_r_97_0.4239_[0.05172839 0.6410715  0.46751767 0.9591621  0.        ].png
img: 1359 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_423_s_1.85_r_270_0.4216_[0.04580619 0.6350491  0.46656454 0.9606702  0.        ].png
img: 1360 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_424_s_1.61_r_273_0.463_[1.5844579e-01 7.1203899e-01 4.7232908e-01 9.7228885e-01 6.8504414e-05].png
img: 1361 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_425_s_1.21_r_108_0.8046_[0.39874208 0.9375841  0.8570193  0.98635364 0.84311616].png
img: 1362 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_426_s_1.82_r_41_0.455_[0.09879156 0.6705224  0.47845963 0.9475863  0.07949284].png
img: 1363 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_427_s_0.76_r_66_0.7311_[0.41820765 0.6806416  0.9604834  0.6600656  0.93619394].png
img: 1364 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_428_s_1.26_r_31_0.8295_[0.38137785 0.9376141  0.9256529  0.98945475 0.91355145].png
img: 1365 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_429_s_1.4_r_41_0.7326_[0.37553623 0.9137777  0.7275827  0.9889137  0.6570062 ].png
img: 1366 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_42_s_0.77_r_358_0.8222_[0.4299912 0.8195096 0.958328  0.9534793 0.9495159].png
img: 1367 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_430_s_0.56_r_267_0.501_[0.40253577 0.42346194 0.6958509  0.30212525 0.6812557 ].png
img: 1368 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_431_s_1.72_r_111_0.4784_[0.14806107 0.7204908  0.49375916 0.95634925 0.07343752].png
img: 1369 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_432_s_0.92_r_102_0.8485_[0.4026522  0.9234022  0.9730429  0.9857902  0.95754063].png
img: 1370 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_433_s_1.89_r_265_0.4235_[0.05168904 0.6384948  0.4684292  0.9586969  0.        ].png
img: 1371 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_434_s_1.9_r_283_0.4265_[0.06570289 0.6525259  0.46545514 0.9466442  0.00216472].png
img: 1372 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_435_s_1.68_r_320_0.5061_[0.1625962  0.7230969  0.5134313  0.9690134  0.16222376].png
img: 1373 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_436_s_1.74_r_86_0.4398_[0.09086137 0.67204624 0.47100145 0.96518373 0.        ].png
img: 1374 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_437_s_0.95_r_171_0.8515_[0.41210663 0.9050246  0.977222   0.99013984 0.97281283].png
img: 1375 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_438_s_0.74_r_10_0.7833_[0.43182755 0.74588734 0.9555679  0.84591484 0.9374304 ].png
img: 1376 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_439_s_1.05_r_272_0.8235_[0.4062005  0.9177296  0.90542805 0.9854728  0.90275884].png
img: 1377 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_43_s_1.94_r_283_0.4215_[0.05797413 0.645015   0.46254984 0.9421317  0.        ].png
img: 1378 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_440_s_1.09_r_240_0.8427_[0.4029094  0.92202616 0.9535611  0.9855941  0.9492278 ].png
img: 1379 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_441_s_1.9_r_292_0.4346_[0.08663926 0.6715779  0.4687178  0.9241536  0.02177187].png
img: 1380 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_442_s_1.74_r_144_0.4905_[0.15179706 0.720829   0.50569224 0.9538832  0.12043928].png
img: 1381 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_443_s_1.76_r_120_0.4838_[0.1369791  0.70954    0.50473017 0.9551158  0.11245489].png
img: 1382 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_444_s_1.54_r_206_0.6053_[0.27766076 0.8064119  0.58908266 0.98642236 0.3668415 ].png
img: 1383 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_445_s_1.7_r_250_0.4751_[0.16466935 0.7254927  0.48510277 0.95687896 0.04359991].png
img: 1384 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_446_s_1.2_r_148_0.8369_[0.39579415 0.92400515 0.94219214 0.99029213 0.9320652 ].png
img: 1385 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_447_s_1.85_r_90_0.4244_[0.04656703 0.64063096 0.47040474 0.9642198  0.        ].png
img: 1386 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_448_s_1.96_r_23_0.4244_[0.07090877 0.6493907  0.46841007 0.9117291  0.02180411].png
img: 1387 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_449_s_1.12_r_121_0.8533_[0.39614397 0.946284   0.97514236 0.9896538  0.95929605].png
img: 1388 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_44_s_1.13_r_50_0.8486_[0.39421484 0.943428   0.96489    0.98953545 0.9509369 ].png
img: 1389 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_450_s_1.86_r_61_0.4446_[0.10169854 0.67868125 0.47216454 0.9398849  0.03039934].png
img: 1390 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_451_s_1.57_r_91_0.473_[1.8188147e-01 7.2974592e-01 4.7337696e-01 9.7993881e-01 5.7711732e-05].png
img: 1391 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_452_s_1.46_r_202_0.6426_[0.34188396 0.86975455 0.60382175 0.9874891  0.4098586 ].png
img: 1392 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_453_s_1.29_r_359_0.5899_[0.39332446 0.9260076  0.5086802  0.98565245 0.13601725].png
img: 1393 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_454_s_1.92_r_315_0.4158_[0.07282037 0.6352674  0.4436106  0.8836238  0.04381332].png
img: 1394 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_455_s_1.04_r_119_0.8401_[0.40106544 0.9262198  0.949593   0.9829735  0.94069   ].png
img: 1395 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_456_s_0.71_r_236_0.6007_[0.42714405 0.5185853  0.9268639  0.24359472 0.88753355].png
img: 1396 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_457_s_0.59_r_125_0.4678_[0.41468412 0.42626536 0.629819   0.20316906 0.6652776 ].png
img: 1397 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_458_s_1.71_r_131_0.4967_[0.14417958 0.70579827 0.51418155 0.97410333 0.1450092 ].png
img: 1398 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_459_s_1.31_r_344_0.6716_[0.39409664 0.92526275 0.613164   0.98899776 0.43671316].png
img: 1399 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_45_s_1.14_r_174_0.7687_[0.40456647 0.92028445 0.7828684  0.9880537  0.74772483].png
img: 1400 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_460_s_0.86_r_226_0.8346_[0.40782502 0.891024   0.9581905  0.96765697 0.9483181 ].png
img: 1401 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_461_s_1.01_r_245_0.8319_[0.40303186 0.91045153 0.9392233  0.9784821  0.92841566].png
img: 1402 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_462_s_1.49_r_310_0.6512_[0.31323382 0.8469705  0.6334013  0.9847883  0.4776926 ].png
img: 1403 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_463_s_1.62_r_263_0.4693_[1.7259596e-01 7.2263992e-01 4.7281456e-01 9.7826046e-01 2.4383306e-04].png
img: 1404 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_464_s_0.63_r_347_0.5825_[0.433706   0.49442428 0.83550227 0.36449945 0.7843381 ].png
img: 1405 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_465_s_1.43_r_181_0.5301_[0.32392755 0.84035474 0.48044991 0.9869804  0.01865393].png
img: 1406 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_466_s_1.41_r_240_0.7222_[0.3712774  0.8983958  0.71506727 0.9884319  0.6380481 ].png
img: 1407 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_467_s_1.69_r_259_0.459_[0.14006442 0.70462173 0.47456962 0.97169566 0.00401038].png
img: 1408 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_468_s_0.84_r_112_0.8246_[0.41182384 0.8624301  0.96198535 0.94581616 0.9411708 ].png
img: 1409 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_469_s_0.74_r_49_0.6353_[0.42602572 0.5508077  0.9515672  0.3381557  0.9099552 ].png
img: 1410 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_46_s_1.19_r_252_0.8003_[0.4014636  0.9252039  0.84725827 0.9874681  0.84014744].png
img: 1411 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_470_s_1.63_r_37_0.5497_[0.19961354 0.75895643 0.55380785 0.96969575 0.26662943].png
img: 1412 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_471_s_1.08_r_266_0.812_[0.40710387 0.91582197 0.8779391  0.9825436  0.87681985].png
img: 1413 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_472_s_0.68_r_247_0.6171_[0.4453905  0.52084655 0.92802286 0.3215093  0.8697263 ].png
img: 1414 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_473_s_1.16_r_150_0.8406_[0.39364505 0.9215806  0.9526683  0.98981977 0.94540656].png
img: 1415 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_474_s_1.7_r_229_0.4951_[0.14921115 0.7099792  0.510845   0.9693457  0.13608468].png
img: 1416 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_475_s_1.02_r_33_0.8357_[0.39654547 0.9195559  0.9425304  0.97746426 0.9422703 ].png
img: 1417 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_476_s_0.8_r_231_0.7399_[0.4152275  0.7092974  0.94563866 0.69393235 0.93546337].png
img: 1418 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_477_s_1.65_r_47_0.5166_[0.17261808 0.72303843 0.5226949  0.9751773  0.18943773].png
img: 1419 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_478_s_0.6_r_129_0.4575_[0.4175021  0.47584346 0.54036576 0.2180231  0.6355282 ].png
img: 1420 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_479_s_0.64_r_314_0.5678_[0.41546252 0.5010423  0.8762582  0.2283252  0.81806284].png
img: 1421 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_47_s_1.06_r_127_0.8483_[0.39949155 0.932262   0.9661131  0.9867774  0.9566748 ].png
img: 1422 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_480_s_0.54_r_325_0.387_[0.39551908 0.36376765 0.47129834 0.1386333  0.5657314 ].png
img: 1423 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_481_s_1.7_r_87_0.448_[0.11298911 0.6849429  0.47176024 0.9703196  0.        ].png
img: 1424 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_482_s_1.03_r_12_0.8518_[0.40161717 0.924367   0.9748116  0.9884178  0.97000825].png
img: 1425 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_483_s_0.81_r_142_0.6977_[0.42646867 0.6377917  0.9401744  0.55365604 0.9304143 ].png
img: 1426 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_484_s_0.5_r_349_0.3373_[0.40064195 0.3447908  0.34908536 0.10993009 0.4821743 ].png
img: 1427 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_485_s_0.9_r_244_0.8406_[0.41028178 0.89784384 0.962547   0.98253256 0.94992584].png
img: 1428 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_486_s_0.71_r_294_0.6362_[0.4224372  0.5531883  0.9394486  0.35780463 0.90793425].png
img: 1429 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_487_s_1.81_r_303_0.4641_[0.11409112 0.6973969  0.49193072 0.937133   0.08016379].png
img: 1430 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_488_s_0.67_r_39_0.5484_[0.41895708 0.48568866 0.88127315 0.14380778 0.8120845 ].png
img: 1431 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_489_s_1.65_r_301_0.5307_[0.19023748 0.7420359  0.53592634 0.96951354 0.21568806].png
img: 1432 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_48_s_1.2_r_228_0.8332_[0.39690804 0.93120086 0.9273211  0.9881282  0.92236286].png
img: 1433 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_490_s_1.28_r_298_0.8114_[0.38995883 0.92846096 0.87548935 0.986889   0.8763118 ].png
img: 1434 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_491_s_0.56_r_94_0.489_[0.39950278 0.4149338  0.6737722  0.2766371  0.68021303].png
img: 1435 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_492_s_0.8_r_130_0.7446_[0.41483286 0.7220256  0.9467235  0.71593577 0.9232974 ].png
img: 1436 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_493_s_1.01_r_111_0.8448_[0.40011683 0.93033063 0.9604854  0.9823571  0.9509504 ].png
img: 1437 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_494_s_1.05_r_38_0.8458_[0.39488167 0.9380106  0.95797944 0.9864012  0.9514977 ].png
img: 1438 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_495_s_0.95_r_1_0.8508_[0.40377694 0.9173412  0.97387934 0.987997   0.9708351 ].png
img: 1439 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_496_s_1.46_r_269_0.5179_[0.2982556  0.8240035  0.47408435 0.9843067  0.00895388].png
img: 1440 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_497_s_0.64_r_236_0.5023_[0.42642033 0.44964743 0.79979706 0.07823247 0.75731903].png
img: 1441 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_498_s_0.62_r_86_0.5734_[0.4392396  0.4576394  0.9177854  0.19492632 0.85730565].png
img: 1442 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_499_s_1.31_r_161_0.6959_[0.39607707 0.9198649  0.65329635 0.98995113 0.52045834].png
img: 1443 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_49_s_0.55_r_61_0.4189_[0.39081392 0.39624387 0.5465831  0.17593966 0.58511776].png
img: 1444 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_4_s_0.52_r_178_0.4366_[0.3912283  0.37130424 0.55853754 0.2680719  0.59369266].png
img: 1445 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_500_s_0.96_r_267_0.8454_[0.40911347 0.9105039  0.9592652  0.98557234 0.96239114].png
img: 1446 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_501_s_1.51_r_54_0.6292_[0.30523616 0.84707695 0.6043635  0.9877326  0.40161058].png
img: 1447 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_502_s_0.92_r_262_0.8471_[0.40759286 0.91334885 0.962963   0.985211   0.96632445].png
img: 1448 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_503_s_1.52_r_305_0.6299_[0.2879561  0.8214978  0.61479264 0.98574376 0.439415  ].png
img: 1449 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_504_s_1.82_r_46_0.4546_[0.09973279 0.669677   0.48057473 0.9403661  0.0828859 ].png
img: 1450 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_505_s_1.02_r_302_0.8382_[0.40033895 0.9187363  0.9446175  0.97771376 0.9496391 ].png
img: 1451 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_506_s_0.89_r_93_0.847_[0.4082716  0.9066263  0.974695   0.98168993 0.96360606].png
img: 1452 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_507_s_1.62_r_222_0.5433_[0.198348   0.7438205  0.54743695 0.97891325 0.24784698].png
img: 1453 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_508_s_0.71_r_80_0.7183_[0.43762425 0.64294153 0.9465729  0.6618907  0.9024152 ].png
img: 1454 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_509_s_1.28_r_77_0.6757_[0.39563072 0.9332767  0.61895657 0.9875143  0.44313356].png
img: 1455 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_50_s_0.63_r_10_0.5626_[0.42778847 0.473207   0.8706676  0.2393838  0.8019384 ].png
img: 1456 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_510_s_1.89_r_278_0.4241_[5.5090070e-02 6.4693362e-01 4.6835443e-01 9.5017749e-01 9.9437184e-06].png
img: 1457 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_511_s_0.94_r_153_0.8468_[0.40720373 0.91047007 0.96748316 0.9852656  0.96337545].png
img: 1458 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_512_s_1.63_r_66_0.5117_[0.20414098 0.7593666  0.5059564  0.9721256  0.1169932 ].png
img: 1459 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_513_s_1.11_r_252_0.835_[0.40582988 0.9217845  0.9320001  0.987253   0.92819786].png
img: 1460 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_514_s_1.76_r_145_0.4829_[0.13214085 0.7036271  0.50526726 0.9590437  0.11427526].png
img: 1461 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_515_s_1.62_r_175_0.4662_[0.16187656 0.7121696  0.47522143 0.9779364  0.00373584].png
img: 1462 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_516_s_0.54_r_75_0.4131_[0.39070964 0.37598366 0.42452064 0.34395963 0.5303121 ].png
img: 1463 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_517_s_1.84_r_279_0.431_[6.8527691e-02 6.5197623e-01 4.7050306e-01 9.6411937e-01 1.0469560e-05].png
img: 1464 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_518_s_0.75_r_322_0.6391_[0.43559432 0.56200683 0.9175167  0.37572235 0.9047344 ].png
img: 1465 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_519_s_1.82_r_284_0.4385_[0.08874325 0.6750032  0.47145316 0.95408523 0.00337921].png
img: 1466 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_51_s_1.6_r_284_0.4959_[0.20241944 0.74890685 0.4901634  0.97139716 0.06650141].png
img: 1467 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_520_s_1.09_r_194_0.8427_[0.40578288 0.92195886 0.95166916 0.9884805  0.9454455 ].png
img: 1468 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_521_s_0.58_r_107_0.4586_[0.40501148 0.43560696 0.51857436 0.32942435 0.6041421 ].png
img: 1469 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_522_s_1.82_r_84_0.432_[0.06828966 0.65603024 0.4704212  0.9654267  0.        ].png
img: 1470 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_523_s_1.45_r_54_0.6857_[0.34988132 0.8923992  0.6632573  0.9890026  0.5338157 ].png
img: 1471 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_524_s_0.93_r_161_0.8492_[0.41195783 0.9024852  0.97318614 0.98955154 0.96904397].png
img: 1472 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_525_s_1.8_r_58_0.4669_[0.12487403 0.70316446 0.4881896  0.9519081  0.06653089].png
img: 1473 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_526_s_0.89_r_287_0.8425_[0.403131   0.91937834 0.9583914  0.97864497 0.9527068 ].png
img: 1474 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_527_s_0.99_r_259_0.8358_[0.40751716 0.91113025 0.94137955 0.9840892  0.9350552 ].png
img: 1475 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_528_s_1.33_r_225_0.7437_[0.39445713 0.9260009  0.7365211  0.98608136 0.6754218 ].png
img: 1476 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_529_s_1.4_r_349_0.5836_[0.38090777 0.9164589  0.5057418  0.988285   0.1263654 ].png
img: 1477 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_52_s_1.45_r_54_0.6857_[0.34988132 0.8923992  0.6632573  0.9890026  0.5338157 ].png
img: 1478 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_530_s_1.21_r_159_0.8091_[0.40154076 0.92826825 0.8666697  0.9913351  0.857482  ].png
img: 1479 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_531_s_1.69_r_293_0.4969_[0.1742225  0.73518187 0.5026989  0.9621615  0.11036408].png
img: 1480 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_532_s_1.31_r_340_0.6935_[0.39143902 0.9238462  0.64939666 0.98937744 0.51338696].png
img: 1481 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_533_s_1.49_r_348_0.5378_[0.30331483 0.83700144 0.49127132 0.9883474  0.06884696].png
img: 1482 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_534_s_0.62_r_247_0.5471_[0.4260136  0.4404722  0.909313   0.12899035 0.83048826].png
img: 1483 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_535_s_1.86_r_188_0.4284_[0.06473328 0.64984447 0.4706809  0.9566393  0.        ].png
img: 1484 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_536_s_0.62_r_135_0.489_[0.43020952 0.44367817 0.7293865  0.14137883 0.70039785].png
img: 1485 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_537_s_1.53_r_125_0.6237_[0.27426642 0.81562036 0.6143374  0.98540527 0.42907512].png
img: 1486 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_538_s_1.43_r_131_0.7019_[0.36462843 0.90129614 0.68169904 0.9899508  0.57185495].png
img: 1487 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_539_s_0.88_r_49_0.8131_[0.39926684 0.8631513  0.9561562  0.90523225 0.9415436 ].png
img: 1488 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_53_s_0.54_r_51_0.3558_[0.3817598  0.37296844 0.26646814 0.26998025 0.48775235].png
img: 1489 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_540_s_2.0_r_235_0.3964_[0.01020341 0.6061343  0.44893348 0.91693175 0.        ].png
img: 1490 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_541_s_1.79_r_16_0.4485_[0.10663097 0.6898266  0.474533   0.957497   0.01401771].png
img: 1491 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_542_s_1.21_r_213_0.839_[0.3921102  0.9301972  0.94441515 0.98839223 0.9399049 ].png
img: 1492 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_543_s_2.0_r_225_0.3828_[0.00771959 0.5955142  0.43607572 0.87474334 0.        ].png
img: 1493 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_544_s_1.11_r_293_0.8472_[0.40191603 0.92735916 0.96443176 0.98484915 0.95737725].png
img: 1494 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_545_s_1.15_r_94_0.7599_[0.4030328  0.92382973 0.76527977 0.98895144 0.71844226].png
img: 1495 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_546_s_1.53_r_64_0.5869_[0.28198844 0.8204938  0.55783343 0.9873723  0.2869827 ].png
img: 1496 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_547_s_0.9_r_307_0.8302_[0.40273815 0.9059061  0.9396637  0.96906334 0.93377346].png
img: 1497 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_548_s_1.16_r_33_0.8468_[0.39034382 0.9436816  0.9612494  0.9889103  0.94957745].png
img: 1498 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_549_s_1.51_r_14_0.545_[0.2812875  0.81803703 0.5077744  0.98588383 0.13190421].png
img: 1499 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_54_s_0.95_r_80_0.8485_[0.40582168 0.91161853 0.9770154  0.9890893  0.95916253].png
img: 1500 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_550_s_0.86_r_246_0.8332_[0.41555798 0.877419   0.9557082  0.9754773  0.94191116].png
img: 1501 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_551_s_1.17_r_225_0.8395_[0.39917088 0.9348585  0.9402622  0.98759234 0.93555635].png
img: 1502 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_552_s_0.64_r_353_0.6307_[0.4418195  0.5187219  0.930965   0.3703041  0.89160085].png
img: 1503 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_553_s_1.92_r_337_0.4307_[0.0810775  0.6756554  0.4608535  0.92087644 0.01493974].png
img: 1504 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_554_s_1.42_r_258_0.5869_[0.37438655 0.9074118  0.51534134 0.98646605 0.1509928 ].png
img: 1505 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_555_s_0.71_r_111_0.6641_[0.4312739  0.58340186 0.9357084  0.47204262 0.8979381 ].png
img: 1506 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_556_s_1.33_r_118_0.7893_[0.38915887 0.9294456  0.8302761  0.9903916  0.8073768 ].png
img: 1507 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_557_s_0.61_r_47_0.4498_[0.42953637 0.40586317 0.70793366 0.01499807 0.6905269 ].png
img: 1508 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_558_s_1.17_r_36_0.8472_[0.38858575 0.9464017  0.9620461  0.987774   0.9510472 ].png
img: 1509 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_559_s_1.75_r_233_0.4837_[0.13645622 0.70297515 0.50181884 0.96389776 0.11341076].png
img: 1510 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_55_s_0.83_r_296_0.7917_[0.41055316 0.8078305  0.95019686 0.86175674 0.92827946].png
img: 1511 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_560_s_1.47_r_161_0.5833_[0.33542797 0.8537944  0.5323192  0.9882949  0.20676538].png
img: 1512 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_561_s_1.1_r_4_0.8088_[0.39984602 0.9334629  0.8651163  0.98708975 0.85835433].png
img: 1513 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_562_s_1.47_r_72_0.5757_[0.3308041  0.85978025 0.52190983 0.98782855 0.17793879].png
img: 1514 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_563_s_1.89_r_331_0.4407_[0.09721077 0.68089783 0.4703474  0.93366927 0.02128273].png
img: 1515 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_564_s_0.84_r_78_0.8402_[0.41756654 0.87668467 0.96797    0.9867719  0.9519193 ].png
img: 1516 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_565_s_1.85_r_313_0.4484_[0.09458587 0.6702185  0.47807527 0.93211    0.06682548].png
img: 1517 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_566_s_0.88_r_42_0.8304_[0.39843193 0.91615844 0.9345483  0.9787224  0.9239993 ].png
img: 1518 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_567_s_1.43_r_130_0.7032_[0.3651405 0.903318  0.68438   0.989817  0.5731722].png
img: 1519 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_568_s_0.72_r_321_0.5832_[0.43156523 0.50444245 0.9104675  0.18625697 0.8832328 ].png
img: 1520 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_569_s_1.24_r_267_0.6418_[0.3997855 0.9270579 0.5709254 0.9839137 0.3272313].png
img: 1521 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_56_s_0.58_r_60_0.4526_[0.42305264 0.3949944  0.7069593  0.05217997 0.6857884 ].png
img: 1522 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_570_s_1.92_r_277_0.4203_[4.7162242e-02 6.3644254e-01 4.6627179e-01 9.5158684e-01 2.8890601e-05].png
img: 1523 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_571_s_1.18_r_337_0.8249_[0.39922306 0.9239601  0.9069495  0.9899969  0.9045133 ].png
img: 1524 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_572_s_1.59_r_217_0.5754_[0.22591133 0.76770747 0.5774029  0.97725666 0.3288677 ].png
img: 1525 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_573_s_1.22_r_55_0.8299_[0.39042702 0.9291986  0.9293476  0.9886794  0.9116877 ].png
img: 1526 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_574_s_0.59_r_208_0.4656_[0.42559755 0.43120176 0.65928245 0.12674758 0.6853666 ].png
img: 1527 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_575_s_1.22_r_277_0.6958_[0.4022671  0.92580706 0.6491345  0.9876824  0.51419526].png
img: 1528 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_576_s_0.9_r_312_0.8381_[0.4005449 0.9198622 0.9472893 0.9749298 0.9478635].png
img: 1529 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_577_s_1.96_r_36_0.4205_[0.07699314 0.6503776  0.4565502  0.8891424  0.02962806].png
img: 1530 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_578_s_1.68_r_231_0.5126_[0.16930732 0.7236288  0.5234771  0.96817046 0.1784699 ].png
img: 1531 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_579_s_1.83_r_312_0.4509_[0.09790648 0.66392857 0.47712797 0.93770397 0.07772147].png
img: 1532 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_57_s_1.28_r_302_0.822_[0.38977218 0.9317055  0.9024154  0.9890688  0.89680827].png
img: 1533 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_580_s_1.37_r_40_0.7581_[0.3798917  0.9317742  0.770075   0.98762745 0.7213451 ].png
img: 1534 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_581_s_1.97_r_61_0.4206_[0.07644936 0.6575956  0.44965592 0.9027723  0.0166653 ].png
img: 1535 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_582_s_1.85_r_28_0.4547_[0.10549594 0.6919983  0.48127353 0.9416437  0.05305251].png
img: 1536 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_583_s_1.19_r_125_0.8465_[0.38804033 0.9363348  0.96758157 0.98915017 0.9512471 ].png
img: 1537 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_584_s_1.39_r_80_0.6047_[0.38296816 0.92125165 0.52905977 0.9879597  0.20201631].png
img: 1538 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_585_s_0.94_r_49_0.8477_[0.39563954 0.9383217  0.9634345  0.9886483  0.9524978 ].png
img: 1539 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_586_s_1.13_r_140_0.8507_[0.3989603  0.94017965 0.9672595  0.99009997 0.9572133 ].png
img: 1540 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_587_s_0.57_r_131_0.4208_[0.39980528 0.4238591  0.4172448  0.298265   0.564834  ].png
img: 1541 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_588_s_1.59_r_124_0.5837_[0.24254061 0.7900655  0.57933766 0.9786469  0.32805112].png
img: 1542 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_589_s_1.01_r_217_0.8327_[0.3996586  0.9191892  0.9366056  0.976207   0.93200433].png
img: 1543 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_58_s_1.12_r_110_0.8487_[0.39881343 0.93832266 0.9639249  0.98935354 0.95328456].png
img: 1544 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_590_s_1.16_r_320_0.8484_[0.39494863 0.9428377  0.9572378  0.9893755  0.9577204 ].png
img: 1545 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_591_s_1.1_r_50_0.85_[0.39441898 0.94439757 0.9688904  0.9880236  0.9541876 ].png
img: 1546 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_592_s_1.79_r_136_0.4602_[0.11016209 0.67054313 0.48453775 0.9449606  0.0910358 ].png
img: 1547 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_593_s_0.92_r_140_0.8437_[0.4023015  0.9262428  0.95465523 0.9881125  0.94724154].png
img: 1548 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_594_s_1.42_r_15_0.622_[0.36828178 0.9060128  0.556348   0.9876993  0.2918277 ].png
img: 1549 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_595_s_0.83_r_157_0.8053_[0.42265174 0.80813354 0.9591386  0.8939539  0.9428459 ].png
img: 1550 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_596_s_0.96_r_71_0.848_[0.4026931  0.91746056 0.9692954  0.98898053 0.96142834].png
img: 1551 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_597_s_1.6_r_195_0.5021_[0.21395561 0.75516766 0.49411598 0.97353774 0.07367708].png
img: 1552 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_598_s_1.29_r_98_0.6573_[0.39909628 0.9273734  0.59298956 0.988377   0.37845775].png
img: 1553 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_599_s_1.13_r_283_0.8209_[0.40230426 0.93026686 0.89285517 0.98718303 0.8919304 ].png
img: 1554 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_59_s_0.57_r_328_0.426_[0.39382005 0.40311387 0.5824893  0.13208795 0.61843824].png
img: 1555 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_5_s_1.88_r_264_0.4234_[5.4050643e-02 6.3890940e-01 4.6795848e-01 9.5587027e-01 2.0101917e-05].png
img: 1556 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_600_s_0.9_r_240_0.8392_[0.4084095 0.9062581 0.9568186 0.9816361 0.9426867].png
img: 1557 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_601_s_0.6_r_86_0.5615_[0.42780897 0.4386832  0.9258488  0.18300848 0.8321886 ].png
img: 1558 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_602_s_0.55_r_275_0.4329_[0.38024783 0.40020147 0.5631334  0.21388677 0.60680896].png
img: 1559 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_603_s_1.74_r_263_0.4442_[1.0309457e-01 6.7785281e-01 4.7108951e-01 9.6831936e-01 7.5165014e-04].png
img: 1560 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_604_s_1.53_r_163_0.5314_[0.2771617  0.8073927  0.49822518 0.9812583  0.09279879].png
img: 1561 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_605_s_1.65_r_111_0.5016_[0.19214264 0.74617493 0.502225   0.9694029  0.09803896].png
img: 1562 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_606_s_1.43_r_356_0.5384_[0.33824256 0.8649881  0.47697166 0.98607165 0.02565482].png
img: 1563 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_607_s_0.59_r_58_0.4453_[0.41199127 0.39535558 0.68479407 0.06209453 0.6725049 ].png
img: 1564 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_608_s_1.52_r_23_0.6029_[0.29351616 0.83041155 0.5757835  0.98256725 0.3321524 ].png
img: 1565 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_609_s_0.73_r_144_0.5994_[0.43048266 0.5147493  0.94120157 0.20657293 0.9040853 ].png
img: 1566 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_60_s_1.36_r_196_0.6801_[0.39631096 0.9207627  0.62752503 0.988517   0.4673847 ].png
img: 1567 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_610_s_1.95_r_187_0.4136_[4.1471563e-02 6.2730694e-01 4.5944753e-01 9.3951100e-01 1.0237129e-04].png
img: 1568 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_611_s_1.93_r_125_0.437_[0.08162432 0.6565634  0.4751423  0.92267895 0.04913617].png
img: 1569 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_612_s_1.95_r_21_0.4216_[0.07140496 0.65285397 0.46464947 0.9115836  0.00742775].png
img: 1570 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_613_s_1.15_r_261_0.7908_[0.404285   0.9222905  0.830118   0.9866906  0.81070584].png
img: 1571 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_614_s_1.47_r_119_0.6754_[0.33742636 0.87071174 0.65918607 0.9883791  0.5214252 ].png
img: 1572 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_615_s_0.62_r_110_0.5236_[0.41875595 0.47359088 0.74764997 0.24273926 0.73546207].png
img: 1573 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_616_s_1.83_r_48_0.4561_[0.10275766 0.67725474 0.48416114 0.9473772  0.06905032].png
img: 1574 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_617_s_1.59_r_245_0.5389_[0.24050993 0.77661383 0.52384776 0.9768787  0.17654137].png
img: 1575 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_618_s_0.98_r_80_0.8501_[0.4050977  0.91430134 0.97736984 0.9891199  0.9643765 ].png
img: 1576 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_619_s_1.26_r_34_0.8294_[0.38471776 0.93997097 0.92344046 0.9894765  0.9094984 ].png
img: 1577 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_61_s_1.71_r_34_0.505_[0.16295692 0.7362781  0.5145019  0.95624465 0.15498142].png
img: 1578 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_620_s_0.8_r_313_0.7651_[0.41275007 0.7612229  0.93893313 0.7870309  0.92562026].png
img: 1579 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_621_s_1.44_r_98_0.5675_[0.35009947 0.88188463 0.504797   0.9894815  0.11140837].png
img: 1580 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_622_s_1.98_r_330_0.4202_[0.07604481 0.65833926 0.45373866 0.8974063  0.01559527].png
img: 1581 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_623_s_0.91_r_290_0.8441_[0.4028762  0.9237574  0.95841    0.9805979  0.95470786].png
img: 1582 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_624_s_0.58_r_312_0.4194_[0.40360072 0.4237873  0.43115222 0.2603308  0.5779426 ].png
img: 1583 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_625_s_0.64_r_121_0.5364_[0.43262476 0.43960106 0.91382176 0.06033803 0.83539706].png
img: 1584 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_626_s_1.24_r_189_0.7139_[0.40277037 0.9273561  0.6781886  0.985561   0.57585907].png
img: 1585 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_627_s_1.83_r_273_0.4281_[5.7125553e-02 6.4478511e-01 4.7117394e-01 9.6726811e-01 1.0622928e-05].png
img: 1586 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_628_s_0.58_r_137_0.4205_[0.4110615  0.40714303 0.50065076 0.19747472 0.586266  ].png
img: 1587 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_629_s_1.25_r_83_0.6502_[0.40086192 0.92947716 0.58243525 0.9876008  0.35048652].png
img: 1588 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_62_s_0.67_r_4_0.6396_[0.43262017 0.5475666  0.9458165  0.3854531  0.8863782 ].png
img: 1589 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_630_s_1.13_r_292_0.8455_[0.4013068  0.928881   0.95772445 0.9861017  0.9533935 ].png
img: 1590 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_631_s_1.52_r_263_0.5054_[0.25489372 0.7882448  0.4787664  0.9794258  0.02575569].png
img: 1591 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_632_s_1.43_r_152_0.6954_[0.3685893  0.89424294 0.6715336  0.99143386 0.5513877 ].png
img: 1592 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_633_s_1.4_r_50_0.7277_[0.3782278  0.91858053 0.71782327 0.99088204 0.63298   ].png
img: 1593 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_634_s_1.27_r_63_0.8112_[0.38622585 0.9242978  0.8850599  0.98982847 0.87082297].png
img: 1594 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_635_s_1.28_r_142_0.8097_[0.3890567  0.92858076 0.8773538  0.98980635 0.86357117].png
img: 1595 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_636_s_0.64_r_8_0.6013_[0.42048866 0.5089697  0.92618126 0.2921525  0.8585758 ].png
img: 1596 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_637_s_1.2_r_224_0.8322_[0.3990196 0.930307  0.9246675 0.9876602 0.9192329].png
img: 1597 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_638_s_0.9_r_24_0.8343_[0.40578344 0.89865595 0.9507789  0.9826779  0.93380153].png
img: 1598 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_639_s_1.08_r_315_0.8458_[0.40098107 0.92886627 0.95501095 0.9884732  0.9557055 ].png
img: 1599 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_63_s_0.92_r_183_0.8485_[0.41163942 0.9050181  0.97339475 0.98479193 0.967415  ].png
img: 1600 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_640_s_1.36_r_126_0.7704_[0.38376427 0.9256986  0.7936484  0.9886974  0.760426  ].png
img: 1601 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_641_s_1.68_r_253_0.4728_[0.16219424 0.72304654 0.48273984 0.96279746 0.03301834].png
img: 1602 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_642_s_1.54_r_151_0.5931_[0.27867028 0.8065073  0.5725573  0.9869769  0.32056516].png
img: 1603 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_643_s_0.86_r_336_0.8344_[0.41347986 0.8752534  0.9597488  0.9747523  0.948647  ].png
img: 1604 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_644_s_1.8_r_68_0.4571_[0.11561956 0.69651294 0.48018974 0.96264803 0.03060351].png
img: 1605 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_645_s_1.32_r_296_0.7942_[0.39132407 0.9309911  0.835508   0.9878493  0.82557434].png
img: 1606 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_646_s_0.74_r_37_0.6212_[0.42975262 0.537246   0.93771243 0.29581118 0.9053713 ].png
img: 1607 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_647_s_1.45_r_37_0.6953_[0.34369627 0.8911263  0.6812286  0.9894425  0.5708517 ].png
img: 1608 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_648_s_1.82_r_290_0.4491_[0.10766311 0.68918765 0.47708327 0.94086784 0.03071603].png
img: 1609 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_649_s_1.38_r_108_0.6819_[0.38658738 0.92154086 0.6346569  0.98974353 0.47680846].png
img: 1610 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_64_s_1.46_r_224_0.6602_[0.3260223  0.8531515  0.63871735 0.98783404 0.49505606].png
img: 1611 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_650_s_1.77_r_136_0.4679_[0.1203856  0.6845086  0.49412963 0.949262   0.09100163].png
img: 1612 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_651_s_1.78_r_293_0.4648_[0.12784956 0.70309746 0.48537508 0.9532046  0.05440516].png
img: 1613 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_652_s_1.79_r_48_0.4664_[0.11655243 0.6920917  0.49161887 0.94344324 0.08816893].png
img: 1614 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_653_s_0.63_r_44_0.4814_[0.41430277 0.45271626 0.6847971  0.15812585 0.6972135 ].png
img: 1615 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_654_s_1.04_r_117_0.8432_[0.40370584 0.919991   0.9590018  0.98479617 0.9484049 ].png
img: 1616 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_655_s_0.81_r_315_0.7386_[0.409009   0.72135943 0.9381873  0.69062704 0.9340467 ].png
img: 1617 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_656_s_1.98_r_256_0.4185_[0.05332644 0.6453691  0.46276307 0.9254911  0.00577585].png
img: 1618 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_657_s_1.51_r_181_0.4939_[2.4197337e-01 7.6676410e-01 4.7469518e-01 9.8543400e-01 5.4506096e-04].png
img: 1619 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_658_s_1.86_r_227_0.4425_[0.08755752 0.6534217  0.47187072 0.93406916 0.06569844].png
img: 1620 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_659_s_1.33_r_309_0.7751_[0.3885374  0.9273734  0.7993368  0.98757404 0.7725452 ].png
img: 1621 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_65_s_1.24_r_85_0.6529_[0.39974847 0.92600834 0.58749366 0.9855101  0.36595628].png
img: 1622 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_660_s_0.9_r_116_0.8387_[0.40782705 0.8989383  0.96476036 0.97455    0.94742835].png
img: 1623 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_661_s_0.66_r_322_0.5471_[0.42385197 0.47759765 0.88302773 0.12934078 0.8214335 ].png
img: 1624 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_662_s_1.18_r_345_0.7755_[0.3989148  0.9237353  0.79496175 0.9881374  0.77174896].png
img: 1625 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_663_s_1.42_r_187_0.5669_[0.35772607 0.87968785 0.50238    0.98621523 0.10853027].png
img: 1626 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_664_s_1.54_r_340_0.5434_[0.27794972 0.81159353 0.5094972  0.9835191  0.13466218].png
img: 1627 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_665_s_1.97_r_278_0.4153_[4.3578744e-02 6.3228899e-01 4.6094361e-01 9.3939084e-01 2.0167945e-04].png
img: 1628 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_666_s_0.66_r_17_0.6105_[0.4235117  0.535243   0.8817204  0.38172752 0.83049786].png
img: 1629 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_667_s_1.13_r_39_0.8484_[0.393118  0.9418004 0.9648803 0.9889116 0.9533584].png
img: 1630 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_668_s_1.87_r_7_0.4266_[5.7742920e-02 6.4923435e-01 4.6846858e-01 9.5709145e-01 2.1329975e-04].png
img: 1631 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_669_s_1.28_r_54_0.8145_[0.3853286  0.9363558  0.889153   0.98899853 0.8728441 ].png
img: 1632 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_66_s_1.26_r_167_0.7076_[0.40095982 0.92613    0.66976666 0.9896479  0.5513841 ].png
img: 1633 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_670_s_1.52_r_139_0.6189_[0.2828181  0.8157444  0.60761124 0.98697376 0.40125814].png
img: 1634 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_671_s_1.77_r_35_0.4787_[0.13061997 0.6980374  0.49984333 0.94224    0.12286234].png
img: 1635 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_672_s_1.26_r_168_0.6879_[0.40259394 0.928345   0.63848567 0.9910417  0.4792559 ].png
img: 1636 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_673_s_1.74_r_269_0.4381_[0.08356366 0.6623751  0.4723945  0.9721933  0.        ].png
img: 1637 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_674_s_0.82_r_302_0.7707_[0.40685633 0.7852737  0.9293651  0.8090354  0.9228253 ].png
img: 1638 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_675_s_1.56_r_177_0.4793_[2.0258759e-01 7.3922986e-01 4.7428882e-01 9.7957414e-01 7.4522180e-04].png
img: 1639 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_676_s_1.0_r_174_0.8605_[0.4090182  0.9267947  0.9850314  0.99691683 0.98449016].png
img: 1640 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_677_s_1.7_r_269_0.4424_[0.09707637 0.6692615  0.4710662  0.97474414 0.        ].png
img: 1641 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_678_s_1.02_r_105_0.851_[0.40401626 0.9251343  0.97470975 0.98749894 0.96373194].png
img: 1642 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_679_s_1.55_r_256_0.5129_[0.24445036 0.78161234 0.49087927 0.97897106 0.06875323].png
img: 1643 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_67_s_1.19_r_76_0.7857_[0.39802396 0.93855673 0.81494695 0.989553   0.78739125].png
img: 1644 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_680_s_1.74_r_165_0.4554_[0.12792763 0.6997548  0.477039   0.96171373 0.01056879].png
img: 1645 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_681_s_1.76_r_49_0.4786_[0.12784132 0.7025766  0.49804443 0.9607736  0.10362505].png
img: 1646 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_682_s_0.87_r_150_0.805_[0.41402608 0.8150553  0.9675484  0.86995566 0.9582783 ].png
img: 1647 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_683_s_1.99_r_263_0.408_[3.5883639e-02 6.2114000e-01 4.5772019e-01 9.2498714e-01 3.0544226e-04].png
img: 1648 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_684_s_0.51_r_357_0.377_[0.36475304 0.3689964  0.39468864 0.23422496 0.52255887].png
img: 1649 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_685_s_1.11_r_221_0.845_[0.401124   0.92928    0.95668244 0.98670334 0.9514368 ].png
img: 1650 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_686_s_0.99_r_317_0.8435_[0.39875242 0.9259969  0.95722526 0.97949976 0.9559577 ].png
img: 1651 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_687_s_1.93_r_270_0.4155_[0.03104629 0.62223667 0.4671711  0.95717275 0.        ].png
img: 1652 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_688_s_1.35_r_144_0.7759_[0.38475123 0.9264386  0.80435526 0.98852783 0.77518094].png
img: 1653 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_689_s_1.62_r_89_0.4623_[1.5178451e-01 7.0899940e-01 4.7307995e-01 9.7750926e-01 1.3533449e-04].png
img: 1654 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_68_s_1.84_r_300_0.4578_[0.1068242  0.68821853 0.4852989  0.93894875 0.06951956].png
img: 1655 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_690_s_1.04_r_249_0.848_[0.40789843 0.9125199  0.9675361  0.98688006 0.9651062 ].png
img: 1656 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_691_s_0.78_r_269_0.8358_[0.417398   0.87885237 0.9530047  0.9791376  0.9505742 ].png
img: 1657 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_692_s_0.54_r_119_0.3534_[0.3835006  0.36460686 0.31610116 0.18103342 0.52159107].png
img: 1658 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_693_s_0.69_r_181_0.7234_[0.44820723 0.6381112  0.96107405 0.65118015 0.91832626].png
img: 1659 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_694_s_1.01_r_316_0.8324_[0.3968487  0.93281364 0.921654   0.9814953  0.92908686].png
img: 1660 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_695_s_1.59_r_237_0.5625_[0.2404973  0.77722067 0.5538732  0.97810185 0.26274148].png
img: 1661 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_696_s_1.19_r_205_0.8402_[0.39703372 0.93023384 0.9451467  0.9893826  0.93935597].png
img: 1662 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_697_s_1.55_r_86_0.4877_[0.21965629 0.76067793 0.47428837 0.981242   0.00257001].png
img: 1663 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_698_s_1.37_r_338_0.6896_[0.38646355 0.92245054 0.6454741  0.98997366 0.5035456 ].png
img: 1664 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_699_s_1.01_r_276_0.8409_[0.40545955 0.9197549  0.9436937  0.9869017  0.94891506].png
img: 1665 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_69_s_1.41_r_105_0.6309_[0.37332729 0.9095428  0.5696126  0.98810965 0.31408   ].png
img: 1666 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_6_s_1.85_r_118_0.4523_[0.10527497 0.69079393 0.47790286 0.9374063  0.04994044].png
img: 1667 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_700_s_1.23_r_80_0.6998_[0.39790475 0.9325156  0.6561361  0.9892874  0.5231012 ].png
img: 1668 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_701_s_1.25_r_144_0.8247_[0.39760414 0.93222666 0.90634084 0.99188465 0.89558566].png
img: 1669 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_702_s_0.76_r_237_0.7145_[0.4189786  0.6684354  0.945408   0.62091964 0.918622  ].png
img: 1670 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_703_s_1.26_r_218_0.8235_[0.38533217 0.9229337  0.9135019  0.988919   0.90674376].png
img: 1671 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_704_s_1.89_r_18_0.4355_[0.07671902 0.6696881  0.47293606 0.94983095 0.00854607].png
img: 1672 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_705_s_1.42_r_11_0.6017_[0.3647656  0.9029919  0.5328357  0.98793656 0.21982026].png
img: 1673 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_706_s_1.75_r_73_0.4544_[0.12424986 0.7008424  0.47558996 0.9639205  0.0072416 ].png
img: 1674 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_707_s_1.93_r_331_0.4258_[0.08036485 0.6621605  0.45223635 0.91493183 0.01925548].png
img: 1675 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_708_s_0.51_r_289_0.3644_[0.35263976 0.38443688 0.29424983 0.32488385 0.46557853].png
img: 1676 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_709_s_1.49_r_106_0.5699_[0.30537364 0.83645993 0.5283027  0.9862138  0.1930622 ].png
img: 1677 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_70_s_1.41_r_290_0.6787_[0.38151914 0.91302145 0.6316571  0.9858943  0.48123527].png
img: 1678 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_710_s_1.08_r_72_0.8389_[0.4037163  0.9208301  0.94759494 0.9887435  0.93354404].png
img: 1679 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_711_s_1.86_r_37_0.4533_[0.09761037 0.6833191  0.48112056 0.93874824 0.06556471].png
img: 1680 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_712_s_1.41_r_82_0.574_[0.36142895 0.90142167 0.5040918  0.9866178  0.11663811].png
img: 1681 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_713_s_1.05_r_56_0.8464_[0.3948982  0.9382214  0.96219546 0.98753107 0.9492493 ].png
img: 1682 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_714_s_0.68_r_288_0.6414_[0.43675998 0.5562355  0.91060257 0.43215406 0.87110627].png
img: 1683 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_715_s_0.57_r_73_0.4593_[0.4017932  0.4211626  0.5912941  0.28202012 0.600381  ].png
img: 1684 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_716_s_1.58_r_302_0.5819_[0.24396181 0.78423816 0.57354736 0.9768367  0.3311032 ].png
img: 1685 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_717_s_1.92_r_116_0.4247_[0.08002425 0.6587566  0.4628595  0.8932912  0.02875981].png
img: 1686 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_718_s_1.1_r_32_0.8491_[0.39225346 0.9471531  0.96795976 0.9858174  0.9523891 ].png
img: 1687 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_719_s_0.92_r_132_0.845_[0.40163222 0.9270365  0.9622642  0.98366004 0.9506123 ].png
img: 1688 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_71_s_1.17_r_231_0.8404_[0.39907098 0.93070894 0.9434687  0.98745346 0.94145316].png
img: 1689 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_720_s_0.61_r_266_0.5803_[0.44044617 0.46221438 0.9250455  0.22513364 0.84890294].png
img: 1690 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_721_s_1.62_r_190_0.4779_[0.18346615 0.7304703  0.48035508 0.9746877  0.02075155].png
img: 1691 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_722_s_0.68_r_259_0.6855_[0.44695234 0.5878821  0.93484765 0.5624046  0.89542025].png
img: 1692 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_723_s_1.33_r_219_0.774_[0.38808855 0.9224477  0.8005264  0.98743266 0.77142006].png
img: 1693 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_724_s_1.31_r_152_0.7743_[0.38895273 0.9170315  0.8018103  0.99048394 0.7732271 ].png
img: 1694 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_725_s_0.91_r_113_0.8464_[0.40319172 0.9215913  0.9659979  0.9850088  0.9560746 ].png
img: 1695 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_726_s_1.8_r_0_0.4293_[0.05760511 0.65175897 0.46975437 0.9671718  0.        ].png
img: 1696 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_727_s_1.16_r_18_0.8339_[0.39706257 0.9396043  0.92449284 0.989936   0.91840816].png
img: 1697 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_728_s_1.19_r_174_0.7079_[0.4038023  0.92240685 0.6704194  0.9875842  0.5551028 ].png
img: 1698 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_729_s_1.72_r_38_0.5021_[0.14907852 0.71765417 0.5208624  0.9564664  0.16626567].png
img: 1699 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_72_s_1.22_r_175_0.665_[0.40236095 0.9234354  0.6046335  0.9862316  0.40837014].png
img: 1700 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_730_s_1.71_r_91_0.4434_[0.09546638 0.67266744 0.4732365  0.97555923 0.        ].png
img: 1701 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_731_s_1.12_r_180_0.7273_[0.40724578 0.9245138  0.7011782  0.9879576  0.6155631 ].png
img: 1702 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_732_s_0.9_r_310_0.8374_[0.40247446 0.9072983  0.95697004 0.96684235 0.95362467].png
img: 1703 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_733_s_1.61_r_331_0.5408_[0.2169828  0.7623499  0.5345132  0.97835016 0.21155971].png
img: 1704 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_734_s_1.29_r_222_0.798_[0.39283118 0.93021494 0.84774303 0.9892727  0.82969683].png
img: 1705 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_735_s_1.56_r_19_0.5406_[0.25460815 0.7928416  0.5172691  0.9811147  0.1572823 ].png
img: 1706 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_736_s_1.95_r_131_0.4211_[0.07293374 0.63725597 0.45643148 0.89697975 0.04185834].png
img: 1707 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_737_s_1.64_r_200_0.5007_[0.18953057 0.7407978  0.50279427 0.9644039  0.10592196].png
img: 1708 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_738_s_0.77_r_157_0.7495_[0.43379664 0.69309205 0.9603765  0.7341407  0.92631996].png
img: 1709 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_739_s_1.19_r_265_0.6944_[0.40167606 0.928962   0.645315   0.983782   0.5122    ].png
img: 1710 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_73_s_1.83_r_105_0.4408_[0.08850528 0.6749931  0.4735892  0.9547338  0.01242315].png
img: 1711 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_740_s_1.81_r_91_0.4284_[0.05739025 0.647269   0.46932018 0.96797585 0.        ].png
img: 1712 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_741_s_0.89_r_237_0.8319_[0.4052251 0.8968598 0.9566155 0.9598347 0.9412143].png
img: 1713 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_742_s_1.67_r_311_0.5109_[0.15886755 0.7244481  0.5227479  0.9699995  0.17848715].png
img: 1714 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_743_s_1.36_r_197_0.6854_[0.3956452  0.9189331  0.63629305 0.98925245 0.48710674].png
img: 1715 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_744_s_0.92_r_178_0.8504_[0.4128867 0.9065046 0.9727338 0.9889642 0.9710133].png
img: 1716 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_745_s_1.58_r_303_0.5868_[0.24577333 0.7865804  0.5795224  0.9783718  0.34397504].png
img: 1717 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_746_s_0.63_r_222_0.5143_[0.42367446 0.46772614 0.7744053  0.18052684 0.7252337 ].png
img: 1718 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_747_s_0.88_r_117_0.8345_[0.4065043  0.89571923 0.9633848  0.96221226 0.94467187].png
img: 1719 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_748_s_0.84_r_216_0.8003_[0.40932676 0.8376912  0.93572426 0.9014353  0.91756594].png
img: 1720 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_749_s_0.84_r_6_0.8407_[0.40722278 0.8961973  0.96089983 0.98285484 0.9562019 ].png
img: 1721 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_74_s_0.81_r_214_0.7537_[0.4106183  0.7492841  0.93307453 0.76136243 0.91406447].png
img: 1722 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_750_s_0.91_r_134_0.8459_[0.40274215 0.91874236 0.9704207  0.9768537  0.96065724].png
img: 1723 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_751_s_0.92_r_218_0.8241_[0.4009425  0.91967547 0.91688925 0.9719894  0.9112226 ].png
img: 1724 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_752_s_1.95_r_168_0.4192_[0.05613256 0.639402   0.4635313  0.93573    0.00138681].png
img: 1725 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_753_s_1.04_r_202_0.8463_[0.40585724 0.9192938  0.9626842  0.9881216  0.9556661 ].png
img: 1726 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_754_s_1.0_r_227_0.6909_[0.39418533 0.71891564 0.79830277 0.696372   0.84683275].png
img: 1727 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_755_s_1.6_r_207_0.5571_[0.22202235 0.7602832  0.5555294  0.9764767  0.271322  ].png
img: 1728 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_756_s_1.19_r_290_0.8236_[0.39878634 0.9318861  0.89748317 0.98622626 0.90342426].png
img: 1729 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_757_s_1.24_r_20_0.7949_[0.39751324 0.9330759  0.8350476  0.9889093  0.8199324 ].png
img: 1730 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_758_s_1.74_r_245_0.4717_[0.14917538 0.7164972  0.488057   0.95658296 0.04810227].png
img: 1731 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_759_s_0.7_r_183_0.725_[0.44412443 0.64399457 0.9497615  0.6699586  0.91715616].png
img: 1732 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_75_s_1.92_r_84_0.4191_[0.04901743 0.6396661  0.46438503 0.94218445 0.        ].png
img: 1733 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_760_s_1.28_r_259_0.68_[0.39970624 0.9258059  0.62608606 0.98511046 0.4632424 ].png
img: 1734 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_761_s_0.56_r_100_0.4272_[0.38574332 0.37554356 0.57979774 0.16509028 0.62992126].png
img: 1735 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_762_s_0.88_r_245_0.8341_[0.4104363  0.88840085 0.9578343  0.9679116  0.9461437 ].png
img: 1736 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_763_s_0.86_r_8_0.8414_[0.41036004 0.88923323 0.96877575 0.9834914  0.95500606].png
img: 1737 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_764_s_1.05_r_56_0.8464_[0.3948982  0.9382214  0.96219546 0.98753107 0.9492493 ].png
img: 1738 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_765_s_1.0_r_282_0.8523_[0.40398648 0.9192548  0.982982   0.9807122  0.9747222 ].png
img: 1739 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_766_s_0.97_r_76_0.8497_[0.40829068 0.9073691  0.97930056 0.98901075 0.9647757 ].png
img: 1740 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_767_s_2.0_r_250_0.3996_[0.01281314 0.6134976  0.44918218 0.9223641  0.        ].png
img: 1741 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_768_s_1.36_r_226_0.7417_[0.3902365  0.9210708  0.73583883 0.9892997  0.6719128 ].png
img: 1742 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_769_s_1.06_r_142_0.8506_[0.40208933 0.93016046 0.97075844 0.98784655 0.9620563 ].png
img: 1743 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_76_s_0.61_r_165_0.5708_[0.43899876 0.47379366 0.8302478  0.35206136 0.75869435].png
img: 1744 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_770_s_1.29_r_111_0.7832_[0.39729434 0.9311099  0.81352854 0.98940337 0.78466076].png
img: 1745 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_771_s_1.89_r_265_0.4235_[0.05168904 0.6384948  0.4684292  0.9586969  0.        ].png
img: 1746 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_772_s_1.68_r_152_0.4985_[0.17813788 0.7323717  0.5058381  0.9668881  0.10932706].png
img: 1747 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_773_s_1.21_r_82_0.7131_[0.39858577 0.93249565 0.6769292  0.9858369  0.5716688 ].png
img: 1748 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_774_s_0.72_r_272_0.7625_[0.44267792 0.7070866  0.9519807  0.78819317 0.9224487 ].png
img: 1749 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_775_s_0.61_r_141_0.4494_[0.42414686 0.4066851  0.67903084 0.06368322 0.67328054].png
img: 1750 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_776_s_0.5_r_316_0.2935_[0.39898723 0.339933   0.21006656 0.040094   0.47863638].png
img: 1751 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_777_s_1.86_r_133_0.4452_[0.0943162  0.6653615  0.4770499  0.93466467 0.05452064].png
img: 1752 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_778_s_0.75_r_89_0.8163_[0.44139358 0.7943274  0.96421874 0.9384664  0.9428468 ].png
img: 1753 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_779_s_1.62_r_157_0.5121_[0.21957019 0.7644425  0.50271165 0.9723095  0.10153684].png
img: 1754 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_77_s_1.39_r_226_0.7201_[0.37630588 0.9119529  0.7057878  0.98743576 0.61880726].png
img: 1755 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_780_s_1.97_r_39_0.4254_[0.06991179 0.6407799  0.46540004 0.91003263 0.04087613].png
img: 1756 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_781_s_1.37_r_50_0.7452_[0.38017792 0.9277018  0.7462908  0.9896981  0.6819194 ].png
img: 1757 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_782_s_1.78_r_187_0.4381_[8.389867e-02 6.609754e-01 4.739543e-01 9.714763e-01 5.607330e-05].png
img: 1758 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_783_s_1.73_r_243_0.481_[0.14994507 0.71369636 0.49729887 0.9600182  0.08407358].png
img: 1759 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_784_s_1.91_r_183_0.4168_[0.04158087 0.6284911  0.46588954 0.9482709  0.        ].png
img: 1760 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_785_s_1.61_r_53_0.5545_[0.21350503 0.7627642  0.5538505  0.97511643 0.26720682].png
img: 1761 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_786_s_1.11_r_33_0.8462_[0.39626536 0.9301344  0.9673676  0.9875272  0.94991875].png
img: 1762 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_787_s_0.96_r_298_0.8486_[0.4008837  0.93086594 0.963686   0.9836078  0.9637321 ].png
img: 1763 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_788_s_1.29_r_117_0.8178_[0.3878884  0.92337346 0.9009544  0.99030924 0.8866367 ].png
img: 1764 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_789_s_0.99_r_259_0.8358_[0.40751716 0.91113025 0.94137955 0.9840892  0.9350552 ].png
img: 1765 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_78_s_0.55_r_147_0.3982_[0.38224798 0.3705787  0.4839131  0.17989199 0.5744619 ].png
img: 1766 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_790_s_1.92_r_118_0.4292_[0.08304351 0.6602646  0.47005895 0.90136975 0.03109581].png
img: 1767 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_791_s_0.63_r_104_0.5473_[0.4267661  0.48460954 0.7643312  0.31721112 0.7435109 ].png
img: 1768 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_792_s_0.8_r_205_0.7802_[0.4168955  0.77882206 0.9479721  0.8385583  0.91882896].png
img: 1769 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_793_s_1.1_r_191_0.8375_[0.40584648 0.9238649  0.93311995 0.9866114  0.9382146 ].png
img: 1770 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_794_s_1.32_r_119_0.7986_[0.38257205 0.9348369  0.8508143  0.98992616 0.8350312 ].png
img: 1771 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_795_s_1.38_r_48_0.7426_[0.38145018 0.9307958  0.7390766  0.98789096 0.67357874].png
img: 1772 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_796_s_1.76_r_90_0.434_[7.1273208e-02 6.5866405e-01 4.7163242e-01 9.6835339e-01 1.1469205e-05].png
img: 1773 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_797_s_0.95_r_344_0.8463_[0.40765527 0.9048622  0.9643817  0.9903408  0.9643558 ].png
img: 1774 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_798_s_1.71_r_306_0.5023_[0.15409228 0.7229446  0.5155199  0.9618348  0.15686703].png
img: 1775 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_799_s_0.96_r_55_0.8392_[0.3988006  0.92517906 0.95009905 0.98640776 0.9355549 ].png
img: 1776 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_79_s_1.5_r_190_0.5136_[0.2687214  0.79328156 0.48330075 0.98559546 0.03710467].png
img: 1777 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_7_s_0.55_r_319_0.3723_[0.36464846 0.3902938  0.28678483 0.30299982 0.5166348 ].png
img: 1778 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_800_s_0.94_r_210_0.8342_[0.40419272 0.9116393  0.9425149  0.97264093 0.9400214 ].png
img: 1779 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_801_s_1.76_r_256_0.4483_[0.11411051 0.6948176  0.47445294 0.9532913  0.00483374].png
img: 1780 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_802_s_0.71_r_312_0.6001_[0.4244247  0.52226734 0.93393236 0.22703542 0.89283663].png
img: 1781 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_803_s_1.9_r_174_0.4195_[0.04761558 0.6311299  0.46718132 0.9517718  0.        ].png
img: 1782 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_804_s_1.53_r_290_0.5718_[0.2863347  0.8173954  0.5388563  0.9796873  0.23687705].png
img: 1783 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_805_s_1.34_r_34_0.7899_[0.3783891  0.93372107 0.8350338  0.988255   0.8141876 ].png
img: 1784 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_806_s_0.95_r_66_0.8418_[0.40372694 0.9059136  0.96502674 0.9834724  0.9510952 ].png
img: 1785 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_807_s_1.53_r_206_0.6138_[0.2880514  0.8156349  0.59571105 0.98357606 0.38581002].png
img: 1786 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_808_s_1.77_r_224_0.4657_[0.11473237 0.67464083 0.49224985 0.950893   0.09602787].png
img: 1787 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_809_s_1.54_r_177_0.4897_[0.22792698 0.759443   0.47450095 0.98306787 0.0035809 ].png
img: 1788 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_80_s_1.46_r_316_0.6595_[0.3362082  0.8749604  0.62775517 0.98601913 0.47253004].png
img: 1789 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_810_s_1.74_r_124_0.4907_[0.14471063 0.7170744  0.5101373  0.9520773  0.12959822].png
img: 1790 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_811_s_1.38_r_338_0.6863_[0.3848435  0.92370665 0.6389892  0.9890955  0.49464774].png
img: 1791 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_812_s_1.06_r_78_0.8351_[0.40563944 0.91753113 0.9377817  0.98834395 0.9262104 ].png
img: 1792 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_813_s_1.2_r_292_0.8351_[0.39986727 0.93322533 0.9283688  0.98633134 0.9277775 ].png
img: 1793 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_814_s_1.1_r_16_0.8468_[0.39742887 0.9387037  0.9581711  0.98865944 0.9512727 ].png
img: 1794 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_815_s_1.5_r_140_0.6033_[0.28805876 0.823343   0.58081335 0.98508626 0.3390636 ].png
img: 1795 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_816_s_1.96_r_314_0.4132_[0.05902237 0.6289911  0.45019343 0.89211303 0.03572881].png
img: 1796 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_817_s_1.77_r_151_0.4726_[0.13514759 0.70981705 0.49411556 0.95258045 0.07117691].png
img: 1797 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_818_s_0.8_r_324_0.7269_[0.4153076  0.684894   0.94878465 0.6464969  0.9391867 ].png
img: 1798 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_819_s_1.25_r_284_0.7502_[0.40129375 0.92827374 0.7416946  0.98691034 0.69277096].png
img: 1799 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_81_s_1.79_r_130_0.47_[0.11254399 0.68635625 0.50016016 0.94779176 0.10327392].png
img: 1800 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_820_s_1.86_r_341_0.4418_[0.09484938 0.68389577 0.47216603 0.9523729  0.00567441].png
img: 1801 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_821_s_2.0_r_324_0.3904_[0.00808684 0.604629   0.4374663  0.9016024  0.        ].png
img: 1802 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_822_s_1.93_r_115_0.4297_[0.07928288 0.65285933 0.47020403 0.9129278  0.03306495].png
img: 1803 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_823_s_0.63_r_340_0.5347_[0.42839533 0.4728875  0.76225215 0.27860093 0.7311975 ].png
img: 1804 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_824_s_0.91_r_56_0.8327_[0.40140173 0.8938242  0.96383554 0.95833874 0.9463198 ].png
img: 1805 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_825_s_1.59_r_314_0.5482_[0.20436889 0.7501083  0.54668754 0.98026067 0.2594786 ].png
img: 1806 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_826_s_0.51_r_307_0.3453_[0.3367753  0.3653785  0.22234042 0.338931   0.4632427 ].png
img: 1807 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_827_s_1.57_r_242_0.5704_[0.25459057 0.7924836  0.55418235 0.97503066 0.27591956].png
img: 1808 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_828_s_0.55_r_53_0.395_[0.3849455  0.3861979  0.47846013 0.17346574 0.55198765].png
img: 1809 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_829_s_0.75_r_175_0.8193_[0.44172835 0.79428786 0.9678825  0.934808   0.957669  ].png
img: 1810 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_82_s_1.91_r_104_0.4267_[0.06482343 0.65382975 0.46824282 0.94525427 0.00128546].png
img: 1811 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_830_s_1.57_r_344_0.5117_[0.24046807 0.7864204  0.4881587  0.9795522  0.06374095].png
img: 1812 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_831_s_1.91_r_7_0.4227_[4.9497370e-02 6.4242905e-01 4.6706808e-01 9.5456982e-01 1.1687363e-04].png
img: 1813 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_832_s_0.55_r_107_0.4244_[0.38437325 0.4087076  0.43925452 0.324406   0.56510204].png
img: 1814 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_833_s_0.58_r_207_0.4591_[0.4132038  0.42189947 0.60108143 0.21462478 0.644837  ].png
img: 1815 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_834_s_1.36_r_233_0.7641_[0.38494197 0.91637313 0.78413486 0.9882371  0.74683446].png
img: 1816 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_835_s_1.34_r_316_0.7618_[0.38724962 0.9309929  0.77125317 0.9879402  0.7316365 ].png
img: 1817 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_836_s_1.83_r_112_0.4516_[0.10482818 0.68641376 0.4801479  0.95001763 0.03656738].png
img: 1818 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_837_s_1.81_r_72_0.449_[0.10800113 0.6942185  0.47594264 0.9547962  0.01183028].png
img: 1819 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_838_s_1.6_r_355_0.4726_[0.17449492 0.7332861  0.4725499  0.978544   0.00394961].png
img: 1820 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_839_s_1.52_r_116_0.6202_[0.2871278  0.82220614 0.6027695  0.9846945  0.40400788].png
img: 1821 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_83_s_1.17_r_38_0.848_[0.38901636 0.9462857  0.96422696 0.98880243 0.9518363 ].png
img: 1822 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_840_s_1.72_r_49_0.4919_[0.14714012 0.71249086 0.5054511  0.9654933  0.1288348 ].png
img: 1823 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_841_s_1.77_r_15_0.4519_[0.10837848 0.69336486 0.4785314  0.95682585 0.02242559].png
img: 1824 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_842_s_1.63_r_294_0.5206_[0.20270956 0.75423026 0.5169204  0.9686144  0.16041525].png
img: 1825 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_843_s_0.81_r_26_0.7712_[0.4086809  0.7678336  0.95248854 0.8013906  0.9256836 ].png
img: 1826 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_844_s_1.35_r_129_0.7674_[0.37874004 0.9225565  0.7908979  0.98930943 0.7555431 ].png
img: 1827 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_845_s_1.04_r_173_0.8437_[0.41022128 0.91189915 0.9553814  0.989525   0.95140505].png
img: 1828 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_846_s_1.43_r_246_0.6492_[0.36978742 0.89516294 0.5966624  0.98683584 0.39736402].png
img: 1829 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_847_s_1.97_r_226_0.4103_[0.0659894  0.6211752  0.44644716 0.87824756 0.03943541].png
img: 1830 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_848_s_1.7_r_342_0.4728_[0.15793204 0.72702193 0.48122904 0.9629497  0.03481684].png
img: 1831 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_849_s_1.89_r_113_0.4406_[0.08625396 0.6744689  0.47583187 0.9374988  0.02903636].png
img: 1832 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_84_s_1.5_r_18_0.555_[0.29358283 0.82498515 0.5149211  0.9854852  0.1562662 ].png
img: 1833 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_850_s_1.06_r_323_0.8486_[0.39888367 0.9297876  0.96468675 0.9880276  0.961421  ].png
img: 1834 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_851_s_1.38_r_98_0.5976_[0.38840455 0.9218876  0.5194214  0.98625344 0.17216499].png
img: 1835 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_852_s_0.7_r_230_0.584_[0.42844877 0.5018194  0.9327796  0.19785999 0.85913074].png
img: 1836 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_853_s_0.5_r_248_0.3479_[0.4165842  0.34425086 0.42739275 0.00753483 0.5436622 ].png
img: 1837 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_854_s_1.56_r_132_0.5845_[0.2379002  0.77719116 0.5822859  0.9822801  0.34295356].png
img: 1838 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_855_s_0.79_r_42_0.6695_[0.41325876 0.61749667 0.9332121  0.47485858 0.90877396].png
img: 1839 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_856_s_1.86_r_83_0.4266_[6.3412555e-02 6.4915448e-01 4.6693873e-01 9.5299828e-01 5.7350018e-04].png
img: 1840 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_857_s_0.98_r_277_0.8472_[0.4059532  0.9164477  0.9666403  0.9822761  0.96476287].png
img: 1841 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_858_s_0.72_r_122_0.6082_[0.43736798 0.52082056 0.9321214  0.26594383 0.8847008 ].png
img: 1842 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_859_s_1.91_r_50_0.4275_[0.07875321 0.6563457  0.46123675 0.90417606 0.03706771].png
img: 1843 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_85_s_1.89_r_261_0.4249_[5.7252236e-02 6.4581281e-01 4.6828687e-01 9.5316970e-01 5.9646889e-05].png
img: 1844 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_860_s_0.79_r_311_0.7033_[0.42483532 0.650297   0.93049043 0.5972543  0.9136459 ].png
img: 1845 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_861_s_1.84_r_271_0.4245_[0.04907739 0.637725   0.4676571  0.96789336 0.        ].png
img: 1846 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_862_s_0.72_r_168_0.7306_[0.45052814 0.6419273  0.95718855 0.68254244 0.92097986].png
img: 1847 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_863_s_1.16_r_124_0.8464_[0.3907422  0.941024   0.96195364 0.98968786 0.9487199 ].png
img: 1848 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_864_s_1.79_r_111_0.457_[0.11902703 0.6996748  0.4775768  0.9468452  0.04206969].png
img: 1849 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_865_s_1.78_r_282_0.4443_[0.10131782 0.6801787  0.47218347 0.9607439  0.00714005].png
img: 1850 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_866_s_1.57_r_286_0.5205_[0.24459249 0.78168756 0.49854785 0.97684276 0.10106935].png
img: 1851 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_867_s_1.87_r_15_0.4355_[0.07530878 0.666409   0.4718545  0.9577922  0.00618042].png
img: 1852 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_868_s_1.69_r_352_0.455_[1.2747452e-01 7.0279300e-01 4.7163719e-01 9.7219366e-01 9.4462745e-04].png
img: 1853 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_869_s_1.71_r_220_0.4965_[0.14614803 0.71232355 0.51313007 0.9607599  0.15      ].png
img: 1854 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_86_s_1.43_r_324_0.7096_[0.36497852 0.9022583  0.69218975 0.9892997  0.59931064].png
img: 1855 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_870_s_1.17_r_242_0.837_[0.3973627  0.9244953  0.9391442  0.9877392  0.93612033].png
img: 1856 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_871_s_1.44_r_345_0.5869_[0.34920302 0.8887992  0.5213601  0.9875777  0.18739347].png
img: 1857 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_872_s_1.9_r_247_0.4334_[0.08733466 0.66992676 0.46928617 0.9319351  0.00873758].png
img: 1858 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_873_s_0.75_r_121_0.684_[0.42639044 0.61722314 0.944553   0.52209854 0.90982896].png
img: 1859 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_874_s_1.62_r_194_0.4894_[0.18807922 0.734313   0.48914766 0.9733143  0.06210148].png
img: 1860 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_875_s_1.11_r_339_0.8354_[0.40215102 0.9270187  0.9316121  0.98963803 0.9263837 ].png
img: 1861 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_876_s_1.36_r_151_0.7501_[0.38672355 0.9101658  0.7559686  0.9907123  0.70681494].png
img: 1862 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_877_s_0.63_r_313_0.5138_[0.42255935 0.46222436 0.78227943 0.16012044 0.7417827 ].png
img: 1863 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_878_s_1.43_r_33_0.7242_[0.36626598 0.90630984 0.7191094  0.99067354 0.638762  ].png
img: 1864 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_879_s_1.73_r_356_0.4436_[0.09662993 0.67921335 0.4713588  0.97078377 0.        ].png
img: 1865 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_87_s_0.98_r_123_0.8411_[0.4038362 0.9143005 0.9563334 0.9822024 0.9487858].png
img: 1866 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_880_s_1.21_r_85_0.6796_[0.40008643 0.92986    0.62388676 0.98483706 0.45955512].png
img: 1867 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_881_s_1.95_r_81_0.4157_[4.8791818e-02 6.3765401e-01 4.6191743e-01 9.2975461e-01 1.3966480e-04].png
img: 1868 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_882_s_1.36_r_279_0.6055_[0.39276314 0.9160811  0.528727   0.9860733  0.20395692].png
img: 1869 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_883_s_0.98_r_207_0.8418_[0.4041287  0.91744006 0.9578843  0.9778053  0.95179045].png
img: 1870 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_884_s_1.52_r_138_0.6112_[0.28449428 0.8200033  0.5947652  0.9855776  0.37097836].png
img: 1871 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_885_s_1.77_r_312_0.4747_[0.11894072 0.6896888  0.5007263  0.9510558  0.11331147].png
img: 1872 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_886_s_1.63_r_147_0.5432_[0.21245849 0.768214   0.5443615  0.9622419  0.22878592].png
img: 1873 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_887_s_0.65_r_107_0.5718_[0.42981988 0.48940775 0.85678947 0.2751127  0.8077685 ].png
img: 1874 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_888_s_0.99_r_259_0.8358_[0.40751716 0.91113025 0.94137955 0.9840892  0.9350552 ].png
img: 1875 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_889_s_1.83_r_94_0.4303_[6.2204901e-02 6.4779329e-01 4.7111702e-01 9.7013682e-01 4.2498938e-05].png
img: 1876 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_88_s_0.98_r_49_0.8459_[0.396474  0.9370726 0.9575082 0.9902224 0.9481049].png
img: 1877 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_890_s_1.82_r_168_0.4393_[8.9584656e-02 6.7105871e-01 4.7309399e-01 9.6200877e-01 5.9017306e-04].png
img: 1878 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_891_s_0.59_r_186_0.5593_[0.42072466 0.44504285 0.8733676  0.26439363 0.79301006].png
img: 1879 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_892_s_0.76_r_212_0.687_[0.4145545 0.6344973 0.9429807 0.5216431 0.9213444].png
img: 1880 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_893_s_1.03_r_31_0.8389_[0.3965547  0.93087476 0.94910574 0.9825829  0.93558794].png
img: 1881 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_894_s_0.8_r_285_0.8191_[0.41993192 0.8427133  0.9489112  0.939907   0.94381845].png
img: 1882 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_895_s_1.43_r_355_0.5491_[0.34465352 0.87438977 0.48528185 0.9857217  0.0553041 ].png
img: 1883 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_896_s_1.75_r_191_0.4459_[0.1091199  0.68364996 0.473348   0.9590071  0.00424351].png
img: 1884 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_897_s_0.55_r_255_0.4665_[0.39076546 0.41847137 0.54003304 0.39581257 0.58762884].png
img: 1885 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_898_s_1.79_r_279_0.4359_[8.2792461e-02 6.6399270e-01 4.6984830e-01 9.6272272e-01 1.1081683e-05].png
img: 1886 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_899_s_0.6_r_196_0.5245_[0.41389436 0.4820702  0.6751415  0.36814326 0.6833814 ].png
img: 1887 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_89_s_0.94_r_79_0.8475_[0.40382212 0.9174542  0.9700758  0.98888195 0.9572234 ].png
img: 1888 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_8_s_1.94_r_340_0.4281_[0.07144821 0.66198343 0.4666763  0.93538487 0.00506379].png
img: 1889 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_900_s_1.67_r_11_0.4661_[0.15519994 0.7209926  0.4744435  0.9705177  0.00927906].png
img: 1890 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_901_s_1.11_r_244_0.8427_[0.4015674  0.92180157 0.95604527 0.9857487  0.9481781 ].png
img: 1891 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_902_s_1.17_r_56_0.8475_[0.39067382 0.9408284  0.9670221  0.98885196 0.9499886 ].png
img: 1892 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_903_s_1.03_r_67_0.8475_[0.4005902 0.9233393 0.9717696 0.9868084 0.954999 ].png
img: 1893 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_904_s_1.1_r_205_0.8503_[0.40160403 0.929976   0.9694893  0.98801166 0.9624882 ].png
img: 1894 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_905_s_1.82_r_48_0.4556_[0.10355903 0.6789148  0.4813851  0.94487584 0.06919459].png
img: 1895 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_906_s_0.99_r_338_0.8493_[0.4042959  0.91532403 0.97113776 0.98921317 0.96639735].png
img: 1896 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_907_s_1.51_r_89_0.4958_[0.24141881 0.7773704  0.473217   0.9834586  0.00351932].png
img: 1897 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_908_s_1.59_r_171_0.4828_[0.20376454 0.74642354 0.4763782  0.97774327 0.00954905].png
img: 1898 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_909_s_0.98_r_126_0.8369_[0.4038295  0.9118273  0.9514403  0.97521245 0.9421963 ].png
img: 1899 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_90_s_1.94_r_228_0.4246_[0.07209792 0.64463186 0.46369877 0.9094634  0.0329516 ].png
img: 1900 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_910_s_1.28_r_117_0.8226_[0.3914991  0.9372751  0.9036299  0.98998994 0.8907649 ].png
img: 1901 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_911_s_0.66_r_37_0.553_[0.4206515  0.48627558 0.86934495 0.17589994 0.812742  ].png
img: 1902 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_912_s_1.7_r_331_0.4966_[0.16974886 0.7328482  0.5032328  0.9671946  0.10991934].png
img: 1903 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_913_s_1.17_r_192_0.8038_[0.40483385 0.92582506 0.85526925 0.9848917  0.8479514 ].png
img: 1904 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_914_s_1.3_r_61_0.787_[0.38138047 0.9248344  0.8313743  0.9894244  0.8080119 ].png
img: 1905 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_915_s_0.7_r_288_0.6566_[0.4312127  0.5778852  0.92675924 0.46393353 0.8833453 ].png
img: 1906 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_916_s_1.58_r_72_0.5121_[0.23393011 0.776406   0.49324465 0.9780615  0.07863003].png
img: 1907 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_917_s_1.47_r_289_0.6179_[0.34053603 0.86741453 0.57118595 0.9839622  0.32664573].png
img: 1908 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_918_s_1.85_r_350_0.4317_[7.0589714e-02 6.6483194e-01 4.6688148e-01 9.5628166e-01 1.0375812e-04].png
img: 1909 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_919_s_1.38_r_4_0.5717_[0.38233596 0.9182966  0.49219468 0.98586136 0.07991578].png
img: 1910 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_91_s_1.11_r_34_0.8498_[0.39580512 0.93801504 0.9694626  0.98923904 0.9562949 ].png
img: 1911 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_920_s_1.98_r_131_0.4168_[0.0653222  0.63358766 0.4547175  0.8807772  0.04949912].png
img: 1912 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_921_s_1.95_r_43_0.4204_[0.07053652 0.642285   0.4579284  0.8957966  0.03555385].png
img: 1913 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_922_s_1.49_r_235_0.6526_[0.32151538 0.8507847  0.6352257  0.98372936 0.4716026 ].png
img: 1914 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_923_s_1.18_r_104_0.8157_[0.40302736 0.92746955 0.8858264  0.988193   0.8738917 ].png
img: 1915 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_924_s_1.73_r_199_0.4679_[0.13776919 0.70432377 0.4865856  0.9609015  0.05001128].png
img: 1916 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_925_s_1.55_r_352_0.4967_[0.23039964 0.7778947  0.47640744 0.9809737  0.01769938].png
img: 1917 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_926_s_1.31_r_228_0.7891_[0.39194885 0.92603254 0.83063453 0.98879147 0.807889  ].png
img: 1918 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_927_s_1.53_r_213_0.6289_[0.28360507 0.81445026 0.62154865 0.9844971  0.44035244].png
img: 1919 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_928_s_1.86_r_129_0.4476_[0.09462981 0.67218214 0.48207837 0.9308539  0.0580174 ].png
img: 1920 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_929_s_1.36_r_45_0.7313_[0.3891233  0.92539656 0.71508557 0.990942   0.63580096].png
img: 1921 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_92_s_1.92_r_82_0.4163_[5.1186144e-02 6.3911533e-01 4.6144980e-01 9.2982239e-01 5.7742276e-05].png
img: 1922 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_930_s_1.06_r_63_0.8467_[0.39999384 0.92568016 0.96626115 0.98842317 0.9533199 ].png
img: 1923 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_931_s_1.46_r_242_0.653_[0.34600157 0.8733934  0.6183454  0.9859534  0.44134736].png
img: 1924 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_932_s_1.39_r_42_0.7264_[0.37620094 0.92846227 0.7119888  0.9906088  0.6247154 ].png
img: 1925 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_933_s_0.94_r_240_0.8416_[0.40562898 0.9097357  0.9596912  0.97734004 0.95564234].png
img: 1926 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_934_s_1.85_r_333_0.4473_[0.10457814 0.68978125 0.4754381  0.9407605  0.02592727].png
img: 1927 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_935_s_0.81_r_161_0.8249_[0.4253108  0.838245   0.9610097  0.95238745 0.9474532 ].png
img: 1928 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_936_s_1.24_r_81_0.6867_[0.3998173  0.9296483  0.6370647  0.98922    0.47761193].png
img: 1929 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_937_s_1.49_r_227_0.64_[0.31009382 0.83764976 0.62225115 0.98501337 0.4448302 ].png
img: 1930 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_938_s_1.73_r_244_0.4789_[0.14848986 0.7113244  0.49490103 0.96594924 0.073889  ].png
img: 1931 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_939_s_1.25_r_185_0.6461_[0.40293622 0.92141783 0.5767421  0.98882794 0.34036267].png
img: 1932 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_93_s_1.79_r_296_0.462_[0.12088314 0.69219595 0.48930782 0.9371253  0.07063842].png
img: 1933 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_940_s_1.44_r_344_0.5835_[0.346592   0.8843051  0.5192101  0.98833907 0.17924947].png
img: 1934 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_941_s_0.64_r_9_0.5878_[0.4226935  0.48380157 0.93341976 0.24188828 0.85725147].png
img: 1935 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_942_s_0.56_r_359_0.4852_[0.41202533 0.41829875 0.6970734  0.2148482  0.68390286].png
img: 1936 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_943_s_0.84_r_277_0.8411_[0.40997678 0.89783514 0.9628315  0.97770315 0.95712477].png
img: 1937 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_944_s_1.89_r_11_0.428_[6.3218668e-02 6.5524834e-01 4.6719131e-01 9.5405692e-01 1.3923699e-04].png
img: 1938 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_945_s_0.89_r_127_0.8248_[0.40339896 0.89514756 0.9392823  0.9586878  0.9273571 ].png
img: 1939 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_946_s_0.74_r_317_0.6241_[0.4285455  0.53939456 0.9347298  0.3031655  0.9145841 ].png
img: 1940 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_947_s_1.38_r_274_0.5696_[0.38446808 0.9129475  0.4911036  0.9834682  0.07584573].png
img: 1941 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_948_s_0.72_r_229_0.6121_[0.4304588  0.52941585 0.9362605  0.27407965 0.8900674 ].png
img: 1942 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_949_s_0.86_r_109_0.8407_[0.40831074 0.90160704 0.96481615 0.9841888  0.9446998 ].png
img: 1943 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_94_s_1.53_r_273_0.4901_[0.23053868 0.76473695 0.47226375 0.9802274  0.00291333].png
img: 1944 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_950_s_1.51_r_280_0.5225_[0.2761301  0.80683476 0.48867655 0.98250866 0.0583236 ].png
img: 1945 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_951_s_0.52_r_323_0.3908_[0.372277   0.38625452 0.33912712 0.36031452 0.49589613].png
img: 1946 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_952_s_1.39_r_129_0.7353_[0.3732419  0.92123526 0.7323151  0.9896806  0.6599712 ].png
img: 1947 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_953_s_0.81_r_54_0.7469_[0.41286913 0.71742594 0.9545009  0.71454334 0.93529016].png
img: 1948 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_954_s_0.83_r_231_0.7753_[0.41456065 0.77829176 0.93449396 0.820417   0.9287634 ].png
img: 1949 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_955_s_1.02_r_111_0.8487_[0.4008215  0.9328311  0.96862    0.98663324 0.95465034].png
img: 1950 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_956_s_0.73_r_144_0.5994_[0.43048266 0.5147493  0.94120157 0.20657293 0.9040853 ].png
img: 1951 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_957_s_1.91_r_181_0.4178_[0.03583061 0.62475896 0.46807614 0.96034646 0.        ].png
img: 1952 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_958_s_1.14_r_132_0.8468_[0.39816394 0.9388381  0.95577437 0.98869824 0.9526741 ].png
img: 1953 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_959_s_0.9_r_84_0.8449_[0.41294035 0.8933527  0.9701172  0.9879574  0.96031   ].png
img: 1954 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_95_s_0.5_r_350_0.3286_[0.39864507 0.3318731  0.36808538 0.04771429 0.4967796 ].png
img: 1955 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_960_s_1.39_r_68_0.6652_[0.38081482 0.9242378  0.608742   0.99013805 0.42208692].png
img: 1956 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_961_s_0.77_r_159_0.7721_[0.43206793 0.72902435 0.9603129  0.7898705  0.94899607].png
img: 1957 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_962_s_0.98_r_209_0.8395_[0.40315992 0.9135888  0.9575832  0.972177   0.9508742 ].png
img: 1958 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_963_s_1.74_r_356_0.4398_[0.08908125 0.6728694  0.46963608 0.96726876 0.        ].png
img: 1959 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_964_s_0.93_r_25_0.8381_[0.4032434  0.9037144  0.96008956 0.97958344 0.94374067].png
img: 1960 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_965_s_0.73_r_250_0.7218_[0.4334508 0.6576894 0.9433976 0.6645372 0.9099194].png
img: 1961 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_966_s_0.81_r_126_0.7222_[0.41458446 0.67978287 0.95766586 0.6335678  0.92524225].png
img: 1962 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_967_s_1.63_r_231_0.5361_[0.19665237 0.7455242  0.539123   0.97279614 0.22662316].png
img: 1963 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_968_s_0.76_r_176_0.8349_[0.43258512 0.8433405  0.9638373  0.98022306 0.95428133].png
img: 1964 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_969_s_1.64_r_164_0.4879_[0.18817008 0.73915726 0.4883538  0.9711635  0.05271829].png
img: 1965 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_96_s_1.85_r_222_0.4439_[0.09558169 0.6603898  0.46898332 0.929424   0.06502716].png
img: 1966 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_970_s_1.3_r_194_0.7084_[0.3986535  0.92616874 0.67110115 0.98786736 0.5581594 ].png
img: 1967 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_971_s_1.18_r_195_0.8117_[0.40375638 0.9289883  0.8721914  0.9900777  0.8636946 ].png
img: 1968 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_972_s_0.59_r_120_0.4749_[0.4154715  0.43507496 0.6503369  0.1873393  0.68641365].png
img: 1969 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_973_s_1.81_r_141_0.4653_[0.11386091 0.68959045 0.49592447 0.9480186  0.07894424].png
img: 1970 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_974_s_1.08_r_138_0.8514_[0.4024739  0.93041307 0.9716859  0.9892813  0.963263  ].png
img: 1971 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_975_s_1.85_r_196_0.4376_[0.08550579 0.66904527 0.47427467 0.95008403 0.00905329].png
img: 1972 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_976_s_1.83_r_86_0.428_[6.0253333e-02 6.4833802e-01 4.6728629e-01 9.6384269e-01 5.3057716e-05].png
img: 1973 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_977_s_1.71_r_273_0.4428_[0.10070175 0.6746479  0.4715311  0.96700317 0.        ].png
img: 1974 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_978_s_1.81_r_55_0.4631_[0.1208053  0.69482136 0.4890109  0.94907683 0.06170982].png
img: 1975 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_979_s_1.96_r_98_0.413_[4.3383915e-02 6.3156265e-01 4.6032733e-01 9.2968976e-01 8.3073348e-05].png
img: 1976 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_97_s_1.88_r_344_0.4342_[0.07391214 0.6649715  0.47048253 0.9580521  0.00371617].png
img: 1977 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_980_s_1.18_r_207_0.8436_[0.39846623 0.9291748  0.9536767  0.98845494 0.9482216 ].png
img: 1978 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_981_s_1.61_r_8_0.4756_[0.18166076 0.7314589  0.47549424 0.97931254 0.01030532].png
img: 1979 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_982_s_0.78_r_333_0.7497_[0.42303678 0.70428365 0.9550337  0.7194669  0.94651777].png
img: 1980 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_983_s_1.8_r_277_0.4344_[0.07623482 0.660472   0.47034967 0.9636757  0.00141359].png
img: 1981 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_984_s_0.69_r_34_0.5669_[0.42386544 0.4865049  0.91613775 0.14437918 0.86375624].png
img: 1982 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_985_s_1.79_r_89_0.4312_[0.06642895 0.65317273 0.46943074 0.9669222  0.        ].png
img: 1983 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_986_s_0.54_r_3_0.4677_[0.3884754  0.39762008 0.6238392  0.27666748 0.65183574].png
img: 1984 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_987_s_1.78_r_153_0.4651_[0.12758158 0.7019271  0.4873634  0.95479685 0.053798  ].png
img: 1985 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_988_s_1.66_r_187_0.4573_[0.14169545 0.6996869  0.473362   0.9702497  0.00149811].png
img: 1986 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_989_s_0.75_r_192_0.7872_[0.44279945 0.74489796 0.9616446  0.8615482  0.9253529 ].png
img: 1987 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_98_s_0.51_r_231_0.3446_[0.35462734 0.34078044 0.2697101  0.2994722  0.45833033].png
img: 1988 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_990_s_0.79_r_270_0.8364_[0.41999304 0.87510437 0.9569456  0.97908163 0.9508936 ].png
img: 1989 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_991_s_1.72_r_338_0.4742_[0.14852887 0.71780545 0.48643145 0.9631104  0.05526202].png
img: 1990 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_992_s_1.23_r_240_0.8286_[0.39132252 0.9194435  0.9235985  0.9872602  0.9212615 ].png
img: 1991 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_993_s_1.27_r_40_0.8149_[0.3882127  0.9373918  0.88704026 0.98861045 0.87341636].png
img: 1992 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_994_s_1.07_r_144_0.846_[0.40109217 0.9299883  0.9572714  0.9893566  0.9524893 ].png
img: 1993 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_995_s_1.5_r_229_0.6026_[0.28295174 0.81341404 0.5820436  0.98725957 0.34710017].png
img: 1994 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_996_s_0.52_r_28_0.3582_[0.3532488  0.3703498  0.30414113 0.2938216  0.46957147].png
img: 1995 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_997_s_1.8_r_238_0.4701_[0.12744834 0.7001183  0.49386066 0.9479567  0.08122384].png
img: 1996 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_998_s_1.64_r_289_0.5007_[0.18895236 0.7457705  0.5024982  0.96317124 0.10317723].png
img: 1997 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_999_s_0.82_r_123_0.7695_[0.4087952 0.7626438 0.9587024 0.7806992 0.9365957].png
img: 1998 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_99_s_1.46_r_200_0.6285_[0.34760258 0.87131584 0.584532   0.98856133 0.35066485].png
img: 1999 evaluate_data/Mosaics/E2CNN/vis/0_0.pn_id_9_s_0.71_r_35_0.5876_[0.41723242 0.5113658  0.9389135  0.19206852 0.8783775 ].png
iou list:
[0.7202, 0.4826, 0.7019, 0.5875, 0.844, 0.5858, 0.737, 0.8114, 0.4951, 0.4304, 0.7368, 0.8334, 0.5978, 0.7659, 0.5787, 0.6237, 0.5407, 0.462, 0.411, 0.4499, 0.5579, 0.823, 0.7391, 0.4427, 0.3642, 0.5237, 0.6044, 0.6107, 0.5278, 0.6819, 0.8356, 0.5595, 0.4985, 0.7314, 0.4221, 0.8274, 0.4454, 0.8407, 0.8432, 0.6805, 0.8147, 0.7807, 0.5633, 0.6204, 0.7511, 0.7303, 0.4482, 0.5835, 0.8296, 0.6738, 0.7106, 0.4313, 0.8291, 0.4452, 0.6977, 0.8506, 0.8099, 0.8461, 0.3838, 0.8463, 0.8381, 0.8473, 0.7684, 0.6431, 0.8471, 0.8349, 0.4848, 0.838, 0.4837, 0.5506, 0.8115, 0.6205, 0.4585, 0.3195, 0.4739, 0.8196, 0.483, 0.5032, 0.8441, 0.7134, 0.4803, 0.4869, 0.6278, 0.4017, 0.4302, 0.8307, 0.8478, 0.4872, 0.4255, 0.8384, 0.3824, 0.4505, 0.8373, 0.8429, 0.4903, 0.6731, 0.8414, 0.8443, 0.6755, 0.7146, 0.4305, 0.8319, 0.7274, 0.8157, 0.4432, 0.8471, 0.7878, 0.8322, 0.761, 0.4645, 0.8113, 0.8393, 0.7705, 0.6555, 0.8478, 0.7319, 0.4464, 0.6299, 0.8053, 0.4483, 0.4777, 0.821, 0.8492, 0.7806, 0.8143, 0.7158, 0.4596, 0.5749, 0.8132, 0.8262, 0.7968, 0.8483, 0.4229, 0.8439, 0.6514, 0.4556, 0.4533, 0.7036, 0.5748, 0.5154, 0.4333, 0.5656, 0.8472, 0.4271, 0.4571, 0.4266, 0.5782, 0.7035, 0.5166, 0.5129, 0.8336, 0.5471, 0.8474, 0.8377, 0.6093, 0.8414, 0.8496, 0.5545, 0.4298, 0.8384, 0.7885, 0.7093, 0.3303, 0.427, 0.8274, 0.4648, 0.8472, 0.4572, 0.6934, 0.5861, 0.4564, 0.5318, 0.4721, 0.4051, 0.8413, 0.8327, 0.8143, 0.6179, 0.8434, 0.8469, 0.8455, 0.821, 0.4232, 0.58, 0.5931, 0.4242, 0.6397, 0.8439, 0.6352, 0.8392, 0.7034, 0.8445, 0.6352, 0.7059, 0.7877, 0.8391, 0.48, 0.4467, 0.484, 0.8594, 0.6599, 0.532, 0.4367, 0.4414, 0.8484, 0.4661, 0.8462, 0.8503, 0.7926, 0.4581, 0.5182, 0.4508, 0.8158, 0.8163, 0.4348, 0.8415, 0.6692, 0.7136, 0.5809, 0.8326, 0.7135, 0.6102, 0.6028, 0.8147, 0.8477, 0.6504, 0.4602, 0.4802, 0.7054, 0.4989, 0.447, 0.8446, 0.7619, 0.7842, 0.5338, 0.427, 0.5511, 0.8388, 0.4142, 0.4672, 0.4384, 0.8313, 0.4441, 0.4998, 0.8527, 0.8405, 0.84, 0.861, 0.851, 0.5373, 0.8517, 0.4957, 0.6252, 0.448, 0.4963, 0.4984, 0.6737, 0.6482, 0.6932, 0.8348, 0.7611, 0.7112, 0.4735, 0.5, 0.8441, 0.5546, 0.844, 0.6086, 0.8458, 0.8287, 0.8343, 0.3409, 0.8458, 0.8482, 0.8343, 0.6169, 0.4765, 0.6554, 0.4515, 0.4123, 0.6239, 0.6374, 0.4782, 0.8341, 0.4749, 0.7276, 0.538, 0.6107, 0.4418, 0.5199, 0.5588, 0.8406, 0.4929, 0.456, 0.4854, 0.7718, 0.6641, 0.421, 0.7003, 0.5906, 0.7204, 0.426, 0.7277, 0.6305, 0.4402, 0.8153, 0.5034, 0.4667, 0.4388, 0.5958, 0.5891, 0.618, 0.8293, 0.6234, 0.4853, 0.843, 0.3643, 0.8342, 0.844, 0.4297, 0.8484, 0.8415, 0.8484, 0.6555, 0.4501, 0.4607, 0.8419, 0.758, 0.8432, 0.6324, 0.846, 0.4419, 0.6663, 0.4236, 0.7117, 0.8426, 0.7766, 0.6207, 0.8567, 0.4352, 0.4747, 0.7214, 0.85, 0.8194, 0.5777, 0.6057, 0.5093, 0.8489, 0.4556, 0.5993, 0.8237, 0.4061, 0.4887, 0.5544, 0.7719, 0.4854, 0.5612, 0.563, 0.6184, 0.5781, 0.5278, 0.4379, 0.634, 0.8485, 0.8455, 0.4695, 0.8449, 0.8461, 0.8442, 0.8291, 0.6839, 0.3511, 0.8475, 0.5519, 0.6342, 0.7108, 0.4418, 0.7412, 0.4293, 0.8449, 0.7947, 0.8419, 0.6118, 0.4136, 0.6086, 0.8437, 0.4523, 0.4746, 0.7508, 0.6512, 0.4459, 0.7125, 0.8443, 0.4626, 0.8121, 0.5056, 0.7845, 0.4668, 0.4723, 0.3363, 0.8358, 0.8286, 0.8493, 0.8471, 0.601, 0.5548, 0.4225, 0.8413, 0.6386, 0.4219, 0.4017, 0.8027, 0.8493, 0.4404, 0.6125, 0.619, 0.4627, 0.5054, 0.8467, 0.7995, 0.8409, 0.74, 0.3366, 0.6251, 0.8415, 0.505, 0.6398, 0.8412, 0.7012, 0.5744, 0.7219, 0.4529, 0.5071, 0.7326, 0.5345, 0.4431, 0.4211, 0.6301, 0.7173, 0.4505, 0.6281, 0.7676, 0.5996, 0.8494, 0.4628, 0.4927, 0.845, 0.4324, 0.4993, 0.5019, 0.4475, 0.5001, 0.8306, 0.619, 0.4218, 0.425, 0.6243, 0.459, 0.5004, 0.5968, 0.845, 0.8174, 0.8429, 0.6783, 0.6042, 0.425, 0.4648, 0.5601, 0.7601, 0.8413, 0.428, 0.4129, 0.4097, 0.7219, 0.8333, 0.8323, 0.8418, 0.4508, 0.804, 0.5885, 0.6177, 0.4578, 0.4905, 0.8493, 0.8503, 0.4137, 0.4257, 0.4777, 0.7951, 0.8224, 0.702, 0.5402, 0.6176, 0.6507, 0.4985, 0.4909, 0.6859, 0.4177, 0.5318, 0.8487, 0.7795, 0.5574, 0.7869, 0.8009, 0.8316, 0.4495, 0.5055, 0.657, 0.5685, 0.8334, 0.8414, 0.505, 0.5098, 0.7222, 0.6681, 0.5012, 0.8393, 0.6346, 0.8475, 0.8413, 0.8347, 0.652, 0.6108, 0.4325, 0.839, 0.8167, 0.8131, 0.8375, 0.6085, 0.8376, 0.8368, 0.4557, 0.6313, 0.842, 0.485, 0.4974, 0.6818, 0.7674, 0.4136, 0.8376, 0.4173, 0.6527, 0.4282, 0.8172, 0.8327, 0.625, 0.4281, 0.475, 0.7353, 0.4765, 0.8296, 0.4565, 0.7134, 0.4197, 0.5138, 0.3276, 0.843, 0.3468, 0.2972, 0.4693, 0.431, 0.8421, 0.678, 0.8429, 0.438, 0.5401, 0.6448, 0.7348, 0.4476, 0.643, 0.5399, 0.8382, 0.4383, 0.5865, 0.5045, 0.8465, 0.6846, 0.5667, 0.6792, 0.8291, 0.3574, 0.7939, 0.8452, 0.8478, 0.8499, 0.6506, 0.4544, 0.724, 0.6077, 0.4797, 0.3841, 0.848, 0.6844, 0.4633, 0.5097, 0.3603, 0.6674, 0.8445, 0.8277, 0.4702, 0.5126, 0.4342, 0.4269, 0.5407, 0.764, 0.4972, 0.7524, 0.8069, 0.8459, 0.8003, 0.6559, 0.8413, 0.7311, 0.8242, 0.4906, 0.4208, 0.8148, 0.8451, 0.8478, 0.7052, 0.7355, 0.8482, 0.8499, 0.4781, 0.8488, 0.8207, 0.3911, 0.4293, 0.6181, 0.6018, 0.6213, 0.8288, 0.8432, 0.8513, 0.8457, 0.4155, 0.4344, 0.4198, 0.7069, 0.4825, 0.3937, 0.831, 0.4884, 0.4221, 0.8357, 0.838, 0.5965, 0.7309, 0.4393, 0.4245, 0.4152, 0.457, 0.8023, 0.8219, 0.8411, 0.8437, 0.6194, 0.4837, 0.7764, 0.8372, 0.8426, 0.49, 0.584, 0.5538, 0.6814, 0.8278, 0.812, 0.8379, 0.8235, 0.501, 0.5747, 0.8437, 0.4846, 0.8373, 0.8469, 0.7641, 0.5064, 0.715, 0.8251, 0.7103, 0.8109, 0.8244, 0.8282, 0.5821, 0.5815, 0.8484, 0.5478, 0.6202, 0.7168, 0.7256, 0.4741, 0.4152, 0.8474, 0.6821, 0.6878, 0.5223, 0.7283, 0.4204, 0.5009, 0.3523, 0.7132, 0.7429, 0.4733, 0.5266, 0.8414, 0.4322, 0.4194, 0.6977, 0.4514, 0.5932, 0.7748, 0.8388, 0.4892, 0.5735, 0.3706, 0.4303, 0.6314, 0.5504, 0.8457, 0.5097, 0.8484, 0.5206, 0.486, 0.7055, 0.4166, 0.4163, 0.834, 0.6212, 0.6397, 0.5133, 0.4688, 0.8107, 0.4336, 0.8379, 0.5972, 0.462, 0.4367, 0.8329, 0.773, 0.4554, 0.8418, 0.797, 0.4936, 0.5947, 0.839, 0.8024, 0.3208, 0.8398, 0.7176, 0.4112, 0.5319, 0.8465, 0.8397, 0.4395, 0.5631, 0.4962, 0.7344, 0.775, 0.7464, 0.5963, 0.8216, 0.3986, 0.8224, 0.5481, 0.6973, 0.8427, 0.7846, 0.8254, 0.8192, 0.3609, 0.754, 0.506, 0.8428, 0.756, 0.8406, 0.7279, 0.8453, 0.6642, 0.4236, 0.6937, 0.574, 0.8486, 0.4305, 0.7834, 0.4392, 0.8005, 0.7542, 0.8393, 0.5524, 0.8304, 0.8429, 0.3942, 0.8018, 0.602, 0.3169, 0.6254, 0.7412, 0.8338, 0.6176, 0.534, 0.5403, 0.8376, 0.4429, 0.4514, 0.8056, 0.3603, 0.8349, 0.8449, 0.672, 0.438, 0.8392, 0.4551, 0.8457, 0.3903, 0.7775, 0.8342, 0.5436, 0.6117, 0.5218, 0.6893, 0.8489, 0.8388, 0.8292, 0.8387, 0.6635, 0.5755, 0.3665, 0.8377, 0.8457, 0.454, 0.4333, 0.7394, 0.4104, 0.5169, 0.4453, 0.838, 0.4421, 0.8478, 0.7171, 0.844, 0.7307, 0.4649, 0.5403, 0.4237, 0.7961, 0.5968, 0.5766, 0.4435, 0.6436, 0.5701, 0.4456, 0.4218, 0.8463, 0.8371, 0.5386, 0.4392, 0.4372, 0.4551, 0.5701, 0.4682, 0.4967, 0.4192, 0.7999, 0.8383, 0.848, 0.6538, 0.7552, 0.684, 0.7702, 0.4323, 0.4826, 0.4269, 0.6096, 0.5818, 0.5766, 0.5728, 0.784, 0.8464, 0.7481, 0.4304, 0.8372, 0.369, 0.4159, 0.8429, 0.4319, 0.5226, 0.4752, 0.4182, 0.8036, 0.8232, 0.8268, 0.7046, 0.6348, 0.3988, 0.4211, 0.3842, 0.816, 0.3729, 0.4204, 0.4243, 0.4509, 0.7794, 0.4532, 0.8454, 0.841, 0.4225, 0.7237, 0.4002, 0.507, 0.8471, 0.4479, 0.8375, 0.7425, 0.5755, 0.7407, 0.8285, 0.4767, 0.5785, 0.7894, 0.7943, 0.5292, 0.4767, 0.4477, 0.7233, 0.451, 0.6991, 0.7483, 0.8463, 0.8072, 0.8267, 0.7736, 0.8343, 0.5032, 0.5459, 0.8295, 0.8359, 0.6738, 0.5836, 0.6855, 0.8448, 0.8367, 0.5228, 0.4364, 0.63, 0.4476, 0.4218, 0.6308, 0.8437, 0.8263, 0.4239, 0.5013, 0.5713, 0.3931, 0.5794, 0.4438, 0.5254, 0.4162, 0.7413, 0.3896, 0.8417, 0.5885, 0.8389, 0.5861, 0.8245, 0.5831, 0.7117, 0.6045, 0.4369, 0.4252, 0.8338, 0.4367, 0.7232, 0.44, 0.797, 0.4244, 0.7073, 0.4238, 0.4413, 0.8216, 0.4284, 0.4081, 0.7623, 0.4225, 0.8513, 0.4268, 0.5475, 0.4279, 0.8219, 0.6661, 0.6489, 0.8484, 0.8413, 0.8399, 0.6059, 0.453, 0.7691, 0.3394, 0.852, 0.684, 0.4662, 0.3663, 0.834, 0.5587, 0.5786, 0.7493, 0.413, 0.7112, 0.5089, 0.6393, 0.7208, 0.4809, 0.8419, 0.4528, 0.7745, 0.5072, 0.3954, 0.6687, 0.4398, 0.4835, 0.6289, 0.687, 0.8437, 0.7193, 0.7917, 0.4718, 0.8315, 0.8356, 0.7127, 0.8593, 0.5167, 0.7563, 0.834, 0.5538, 0.6144, 0.4318, 0.3917, 0.4033, 0.652, 0.4284, 0.5773, 0.4325, 0.5126, 0.5045, 0.4893, 0.6469, 0.759, 0.428, 0.4328, 0.8115, 0.7299, 0.3638, 0.6949, 0.5115, 0.4053, 0.7473, 0.6032, 0.8476, 0.8269, 0.6333, 0.8378, 0.5621, 0.8323, 0.63, 0.4657, 0.7833, 0.7525, 0.6002, 0.8449, 0.6463, 0.6798, 0.8472, 0.4172, 0.5278, 0.8394, 0.623, 0.8482, 0.6255, 0.6545, 0.8502, 0.8432, 0.505, 0.5172, 0.4379, 0.5975, 0.4228, 0.823, 0.7451, 0.4335, 0.5658, 0.835, 0.4803, 0.8472, 0.497, 0.8468, 0.449, 0.4563, 0.8408, 0.4822, 0.3912, 0.7257, 0.4713, 0.7162, 0.3801, 0.8321, 0.4966, 0.5143, 0.8515, 0.8144, 0.6783, 0.6132, 0.6658, 0.5662, 0.45, 0.4151, 0.6676, 0.4677, 0.5361, 0.6373, 0.6377, 0.8174, 0.8207, 0.8474, 0.5203, 0.8078, 0.6804, 0.7117, 0.632, 0.5786, 0.474, 0.5248, 0.8455, 0.849, 0.7837, 0.4148, 0.8493, 0.7315, 0.6062, 0.8492, 0.7702, 0.4912, 0.4891, 0.4586, 0.6341, 0.6403, 0.5742, 0.7625, 0.8462, 0.4652, 0.5883, 0.4491, 0.8375, 0.7091, 0.7988, 0.484, 0.5063, 0.5723, 0.8455, 0.6909, 0.5681, 0.8293, 0.6254, 0.5953, 0.8344, 0.4396, 0.8168, 0.8014, 0.8432, 0.5, 0.5047, 0.682, 0.5559, 0.8435, 0.7405, 0.8338, 0.7789, 0.8031, 0.6146, 0.6287, 0.5155, 0.5689, 0.8395, 0.8469, 0.4419, 0.8095, 0.6798, 0.4722, 0.8155, 0.5264, 0.7043, 0.8486, 0.666, 0.5777, 0.8306, 0.7945, 0.5696, 0.7201, 0.5837, 0.4158, 0.439, 0.4753, 0.4287, 0.7095, 0.8477, 0.439, 0.7346, 0.7868, 0.5212, 0.76, 0.4339, 0.431, 0.8384, 0.586, 0.8492, 0.843, 0.8243, 0.6082, 0.6825, 0.8105, 0.4811, 0.8451, 0.6641, 0.4774, 0.845, 0.7613, 0.8259, 0.7141, 0.5763, 0.6271, 0.4829, 0.4266, 0.4248, 0.6194, 0.8234, 0.6056, 0.4524, 0.5596, 0.6777, 0.8481, 0.7136, 0.6575, 0.6423, 0.8335, 0.4125, 0.4533, 0.8467, 0.7218, 0.7225, 0.7872, 0.4512, 0.4422, 0.4836, 0.4339, 0.4344, 0.7585, 0.6556, 0.6443, 0.8402, 0.468, 0.7642, 0.8349, 0.4178, 0.4719, 0.8486, 0.8473, 0.8417, 0.8483, 0.422, 0.5435, 0.4952, 0.8024, 0.7001, 0.8509, 0.3376, 0.8221, 0.4609, 0.8441, 0.5356, 0.6989, 0.4112, 0.666, 0.6691, 0.4398, 0.4203, 0.4568, 0.8381, 0.8386, 0.778, 0.5236, 0.4319, 0.6325, 0.8447, 0.6951, 0.6846, 0.418, 0.6498, 0.8474, 0.4208, 0.4813, 0.843, 0.4859, 0.8396, 0.3911, 0.4319, 0.3038, 0.4465, 0.8437, 0.8308, 0.846, 0.5804, 0.7209, 0.4509, 0.8094, 0.804, 0.7934, 0.5825, 0.8459, 0.4799, 0.8289, 0.4202, 0.5931, 0.6325, 0.8459, 0.8173, 0.6751, 0.4345, 0.4427, 0.4808, 0.4431, 0.5809, 0.7635, 0.4366, 0.8447, 0.8402, 0.6336, 0.5964, 0.4561, 0.461, 0.7645, 0.7066, 0.4418, 0.7427, 0.5788, 0.4713, 0.5812, 0.8484, 0.4407, 0.5729, 0.4478, 0.8301, 0.4379, 0.4255, 0.5728, 0.4427, 0.8374, 0.5269, 0.4107, 0.813, 0.8436, 0.4239, 0.4216, 0.463, 0.8046, 0.455, 0.7311, 0.8295, 0.7326, 0.8222, 0.501, 0.4784, 0.8485, 0.4235, 0.4265, 0.5061, 0.4398, 0.8515, 0.7833, 0.8235, 0.4215, 0.8427, 0.4346, 0.4905, 0.4838, 0.6053, 0.4751, 0.8369, 0.4244, 0.4244, 0.8533, 0.8486, 0.4446, 0.473, 0.6426, 0.5899, 0.4158, 0.8401, 0.6007, 0.4678, 0.4967, 0.6716, 0.7687, 0.8346, 0.8319, 0.6512, 0.4693, 0.5825, 0.5301, 0.7222, 0.459, 0.8246, 0.6353, 0.8003, 0.5497, 0.812, 0.6171, 0.8406, 0.4951, 0.8357, 0.7399, 0.5166, 0.4575, 0.5678, 0.8483, 0.387, 0.448, 0.8518, 0.6977, 0.3373, 0.8406, 0.6362, 0.4641, 0.5484, 0.5307, 0.8332, 0.8114, 0.489, 0.7446, 0.8448, 0.8458, 0.8508, 0.5179, 0.5023, 0.5734, 0.6959, 0.4189, 0.4366, 0.8454, 0.6292, 0.8471, 0.6299, 0.4546, 0.8382, 0.847, 0.5433, 0.7183, 0.6757, 0.5626, 0.4241, 0.8468, 0.5117, 0.835, 0.4829, 0.4662, 0.4131, 0.431, 0.6391, 0.4385, 0.4959, 0.8427, 0.4586, 0.432, 0.6857, 0.8492, 0.4669, 0.8425, 0.8358, 0.7437, 0.5836, 0.6857, 0.8091, 0.4969, 0.6935, 0.5378, 0.5471, 0.4284, 0.489, 0.6237, 0.7019, 0.8131, 0.3558, 0.3964, 0.4485, 0.839, 0.3828, 0.8472, 0.7599, 0.5869, 0.8302, 0.8468, 0.545, 0.8485, 0.8332, 0.8395, 0.6307, 0.4307, 0.5869, 0.6641, 0.7893, 0.4498, 0.8472, 0.4837, 0.7917, 0.5833, 0.8088, 0.5757, 0.4407, 0.8402, 0.4484, 0.8304, 0.7032, 0.5832, 0.6418, 0.4526, 0.4203, 0.8249, 0.5754, 0.8299, 0.4656, 0.6958, 0.8381, 0.4205, 0.5126, 0.4509, 0.822, 0.7581, 0.4206, 0.4547, 0.8465, 0.6047, 0.8477, 0.8507, 0.4208, 0.5837, 0.8327, 0.8487, 0.8484, 0.85, 0.4602, 0.8437, 0.622, 0.8053, 0.848, 0.5021, 0.6573, 0.8209, 0.426, 0.4234, 0.8392, 0.5615, 0.4329, 0.4442, 0.5314, 0.5016, 0.5384, 0.4453, 0.6029, 0.5994, 0.6801, 0.4136, 0.437, 0.4216, 0.7908, 0.6754, 0.5236, 0.4561, 0.5389, 0.8501, 0.8294, 0.505, 0.7651, 0.5675, 0.4202, 0.8441, 0.4194, 0.5364, 0.7139, 0.4281, 0.4205, 0.6502, 0.6396, 0.8455, 0.5054, 0.6954, 0.7277, 0.8112, 0.8097, 0.6013, 0.8322, 0.8343, 0.8458, 0.8485, 0.7704, 0.4728, 0.5931, 0.8344, 0.4571, 0.7942, 0.6212, 0.6953, 0.4491, 0.6819, 0.6602, 0.4679, 0.4648, 0.4664, 0.4814, 0.8432, 0.7386, 0.4185, 0.4939, 0.4425, 0.7751, 0.6529, 0.8387, 0.5471, 0.7755, 0.5669, 0.5434, 0.4153, 0.6105, 0.8484, 0.4266, 0.8145, 0.7076, 0.6189, 0.4787, 0.6879, 0.4381, 0.7707, 0.4793, 0.8605, 0.4424, 0.851, 0.5129, 0.7857, 0.4554, 0.4786, 0.805, 0.408, 0.377, 0.845, 0.8435, 0.4155, 0.7759, 0.4623, 0.4578, 0.848, 0.8358, 0.3534, 0.7234, 0.8324, 0.5625, 0.8402, 0.4877, 0.6896, 0.8409, 0.6309, 0.4523, 0.6998, 0.8247, 0.7145, 0.8235, 0.4355, 0.6017, 0.4544, 0.4258, 0.3644, 0.5699, 0.6787, 0.8389, 0.4533, 0.574, 0.8464, 0.6414, 0.4593, 0.5819, 0.4247, 0.8491, 0.845, 0.8404, 0.5803, 0.4779, 0.6855, 0.774, 0.7743, 0.8464, 0.4293, 0.8339, 0.7079, 0.5021, 0.665, 0.4434, 0.7273, 0.8374, 0.5408, 0.798, 0.5406, 0.4211, 0.5007, 0.7495, 0.6944, 0.4408, 0.4284, 0.8319, 0.5109, 0.6854, 0.8504, 0.5868, 0.5143, 0.8345, 0.8003, 0.8407, 0.7537, 0.8459, 0.8241, 0.4192, 0.8463, 0.6909, 0.5571, 0.8236, 0.7949, 0.4717, 0.725, 0.4191, 0.68, 0.4272, 0.8341, 0.8414, 0.8464, 0.8523, 0.8497, 0.3996, 0.7417, 0.8506, 0.5708, 0.7832, 0.4235, 0.4985, 0.7131, 0.7625, 0.4494, 0.2935, 0.4452, 0.8163, 0.5121, 0.7201, 0.4254, 0.7452, 0.4381, 0.481, 0.4168, 0.5545, 0.8462, 0.8486, 0.8178, 0.8358, 0.3982, 0.4292, 0.5473, 0.7802, 0.8375, 0.7986, 0.7426, 0.434, 0.8463, 0.5023, 0.8392, 0.5136, 0.3723, 0.8342, 0.4483, 0.6001, 0.4195, 0.5718, 0.7899, 0.8418, 0.6138, 0.4657, 0.4897, 0.6595, 0.4907, 0.6863, 0.8351, 0.8351, 0.8468, 0.6033, 0.4132, 0.4726, 0.7269, 0.7502, 0.47, 0.4418, 0.3904, 0.4297, 0.5347, 0.8327, 0.5482, 0.3453, 0.5704, 0.395, 0.8193, 0.4267, 0.5117, 0.4227, 0.4244, 0.4591, 0.7641, 0.7618, 0.4516, 0.449, 0.4726, 0.6202, 0.848, 0.4919, 0.4519, 0.5206, 0.7712, 0.7674, 0.8437, 0.6492, 0.4103, 0.4728, 0.4406, 0.555, 0.8486, 0.5976, 0.584, 0.3479, 0.5845, 0.6695, 0.4266, 0.8472, 0.6082, 0.4275, 0.4249, 0.7033, 0.4245, 0.7306, 0.8464, 0.457, 0.4443, 0.5205, 0.4355, 0.455, 0.4965, 0.7096, 0.837, 0.5869, 0.4334, 0.684, 0.4894, 0.8354, 0.7501, 0.5138, 0.7242, 0.4436, 0.8411, 0.6796, 0.4157, 0.6055, 0.8418, 0.6112, 0.4747, 0.5432, 0.5718, 0.8358, 0.4303, 0.8459, 0.4393, 0.5593, 0.687, 0.8389, 0.8191, 0.5491, 0.4459, 0.4665, 0.4359, 0.5245, 0.8475, 0.4281, 0.4661, 0.8427, 0.8475, 0.8475, 0.8503, 0.4556, 0.8493, 0.4958, 0.4828, 0.8369, 0.4246, 0.8226, 0.553, 0.4966, 0.8038, 0.787, 0.6566, 0.5121, 0.6179, 0.4317, 0.5717, 0.8498, 0.4168, 0.4204, 0.6526, 0.8157, 0.4679, 0.4967, 0.7891, 0.6289, 0.4476, 0.7313, 0.4163, 0.8467, 0.653, 0.7264, 0.8416, 0.4473, 0.8249, 0.6867, 0.64, 0.4789, 0.6461, 0.462, 0.5835, 0.5878, 0.4852, 0.8411, 0.428, 0.8248, 0.6241, 0.5696, 0.6121, 0.8407, 0.4901, 0.5225, 0.3908, 0.7353, 0.7469, 0.7753, 0.8487, 0.5994, 0.4178, 0.8468, 0.8449, 0.3286, 0.6652, 0.7721, 0.8395, 0.4398, 0.8381, 0.7218, 0.7222, 0.5361, 0.8349, 0.4879, 0.4439, 0.7084, 0.8117, 0.4749, 0.4653, 0.8514, 0.4376, 0.428, 0.4428, 0.4631, 0.413, 0.4342, 0.8436, 0.4756, 0.7497, 0.4344, 0.5669, 0.4312, 0.4677, 0.4651, 0.4573, 0.7872, 0.3446, 0.8364, 0.4742, 0.8286, 0.8149, 0.846, 0.6026, 0.3582, 0.4701, 0.5007, 0.7695, 0.6285, 0.5876]
2022-12-27 00:42:16.194719, iou: tensor([0.2318, 0.7452, 0.5672, 0.9365, 0.3377], device='cuda:0'), 0.5637
==============================================================================
Running epilogue script on alpha51.

Submit time  : 2022-12-26T18:04:01
Start time   : 2022-12-26T18:04:01
End time     : 2022-12-27T00:42:19
Elapsed time : 06:38:18 (Timelimit=1-00:00:00)

Job ID: 2349360
Cluster: i5
User/Group: yy3u19/fp
State: COMPLETED (exit code 0)
Nodes: 1
Cores per node: 4
CPU Utilized: 06:39:21
CPU Efficiency: 25.07% of 1-02:33:12 core-walltime
Job Wall-clock time: 06:38:18
Memory Utilized: 16.06 GB
Memory Efficiency: 76.13% of 21.09 GB

