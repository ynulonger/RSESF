Running SLURM prolog script on alpha51.cluster.local
===============================================================================
Job started on Mon Dec 26 15:21:02 GMT 2022
Job ID          : 2349160
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
---------- kernel_size: 3 ---------- classes: 5 ---------- model: E2CNN ---------- rotations: 8 ---------- dataset: Mosaics - test ----------
num of trainable parameters:7033853
Loading model checkpoints/Mosaics/lr_0.002_bn_16_epoch_70_E2CNN_Ksize_3_rotation_8.pth num of rotations of filters: 8
Using device cuda
----------------------------------------------------------------------------------------------------------------------------------------------------------------
Num of images for evaulation: 160
img: 0 evaluate_data/Mosaics/E2CNN/test/0_0_0.9947_[0.997  0.9987 0.9913 0.9987 0.9879].png
img: 1 evaluate_data/Mosaics/E2CNN/test/0_1_0.9941_[0.9941 0.9871 0.9969 0.9985 0.9937].png
img: 2 evaluate_data/Mosaics/E2CNN/test/0_2_0.9946_[0.9947 0.9943 0.9981 0.9981 0.9877].png
img: 3 evaluate_data/Mosaics/E2CNN/test/0_3_0.993_[0.9975 0.9852 0.989  0.9986 0.9947].png
img: 4 evaluate_data/Mosaics/E2CNN/test/0_4_0.9952_[0.9944 0.995  0.9908 0.9974 0.9982].png
img: 5 evaluate_data/Mosaics/E2CNN/test/0_5_0.992_[0.995  0.9957 0.9853 0.9863 0.9979].png
img: 6 evaluate_data/Mosaics/E2CNN/test/0_6_0.9952_[0.9909 0.9945 0.9976 0.9987 0.9943].png
img: 7 evaluate_data/Mosaics/E2CNN/test/0_7_0.994_[0.9939 0.9877 0.9982 0.9928 0.9972].png
img: 8 evaluate_data/Mosaics/E2CNN/test/0_8_0.9915_[0.9988 0.9811 0.9974 0.9857 0.9946].png
img: 9 evaluate_data/Mosaics/E2CNN/test/0_9_0.9928_[0.9986 0.9905 0.983  0.9943 0.9978].png
img: 10 evaluate_data/Mosaics/E2CNN/test/10_0_0.9966_[0.9967 0.9959 0.9988 0.9975 0.9941].png
img: 11 evaluate_data/Mosaics/E2CNN/test/10_1_0.9933_[0.9977 0.9987 0.9893 0.9956 0.9852].png
img: 12 evaluate_data/Mosaics/E2CNN/test/10_2_0.9954_[0.9986 0.993  0.9932 0.9952 0.997 ].png
img: 13 evaluate_data/Mosaics/E2CNN/test/10_3_0.9946_[0.9969 0.9957 0.9878 0.9989 0.9936].png
img: 14 evaluate_data/Mosaics/E2CNN/test/10_4_0.9942_[0.9973 0.9984 0.9869 0.9942 0.994 ].png
img: 15 evaluate_data/Mosaics/E2CNN/test/10_5_0.9956_[0.9983 0.9911 0.995  0.9985 0.9952].png
img: 16 evaluate_data/Mosaics/E2CNN/test/10_6_0.9947_[0.997  0.9957 0.9975 0.9885 0.9949].png
img: 17 evaluate_data/Mosaics/E2CNN/test/10_7_0.9917_[0.9979 0.9924 0.9931 0.9792 0.9959].png
img: 18 evaluate_data/Mosaics/E2CNN/test/10_8_0.9953_[0.9923 0.9951 0.9978 0.9949 0.9962].png
img: 19 evaluate_data/Mosaics/E2CNN/test/10_9_0.984_[0.9967 0.9891 0.9646 0.9711 0.9983].png
img: 20 evaluate_data/Mosaics/E2CNN/test/11_0_0.9932_[0.9977 0.9819 0.9934 0.9972 0.9956].png
img: 21 evaluate_data/Mosaics/E2CNN/test/11_1_0.9946_[0.9984 0.9929 0.996  0.9961 0.9896].png
img: 22 evaluate_data/Mosaics/E2CNN/test/11_2_0.9953_[0.9972 0.9976 0.9965 0.9966 0.9885].png
img: 23 evaluate_data/Mosaics/E2CNN/test/11_3_0.9949_[0.9973 0.9963 0.9973 0.9966 0.987 ].png
img: 24 evaluate_data/Mosaics/E2CNN/test/11_4_0.9937_[0.9978 0.9971 0.9945 0.9983 0.9809].png
img: 25 evaluate_data/Mosaics/E2CNN/test/11_5_0.9952_[0.9971 0.9972 0.9869 0.9977 0.9973].png
img: 26 evaluate_data/Mosaics/E2CNN/test/11_6_0.9946_[0.9987 0.9974 0.9839 0.9977 0.9953].png
img: 27 evaluate_data/Mosaics/E2CNN/test/11_7_0.9944_[0.9969 0.9944 0.9969 0.9954 0.9883].png
img: 28 evaluate_data/Mosaics/E2CNN/test/11_8_0.9923_[0.9962 0.9776 0.9934 0.9982 0.9959].png
img: 29 evaluate_data/Mosaics/E2CNN/test/11_9_0.9937_[0.9977 0.9978 0.9938 0.9825 0.997 ].png
img: 30 evaluate_data/Mosaics/E2CNN/test/12_0_0.9944_[0.9918 0.9912 0.9951 0.9978 0.9959].png
img: 31 evaluate_data/Mosaics/E2CNN/test/12_1_0.9946_[0.9915 0.9961 0.9947 0.9947 0.9962].png
img: 32 evaluate_data/Mosaics/E2CNN/test/12_2_0.9927_[0.9976 0.9967 0.9894 0.9859 0.9941].png
img: 33 evaluate_data/Mosaics/E2CNN/test/12_3_0.9944_[0.9973 0.9918 0.9966 0.9928 0.9933].png
img: 34 evaluate_data/Mosaics/E2CNN/test/12_4_0.9955_[0.9946 0.9935 0.998  0.9958 0.9955].png
img: 35 evaluate_data/Mosaics/E2CNN/test/12_5_0.9956_[0.9959 0.9929 0.9944 0.9981 0.9966].png
img: 36 evaluate_data/Mosaics/E2CNN/test/12_6_0.9951_[0.9983 0.9939 0.9955 0.9937 0.994 ].png
img: 37 evaluate_data/Mosaics/E2CNN/test/12_7_0.9944_[0.9946 0.99   0.9956 0.9946 0.997 ].png
img: 38 evaluate_data/Mosaics/E2CNN/test/12_8_0.9945_[0.991  0.99   0.9957 0.9977 0.9984].png
img: 39 evaluate_data/Mosaics/E2CNN/test/12_9_0.9954_[0.9931 0.9943 0.9971 0.996  0.9963].png
img: 40 evaluate_data/Mosaics/E2CNN/test/13_0_0.9911_[0.9928 0.999  0.9904 0.9962 0.9771].png
img: 41 evaluate_data/Mosaics/E2CNN/test/13_1_0.9832_[0.9827 0.9423 0.9963 0.9972 0.9975].png
img: 42 evaluate_data/Mosaics/E2CNN/test/13_2_0.9904_[0.9883 0.9917 0.9755 0.9975 0.9989].png
img: 43 evaluate_data/Mosaics/E2CNN/test/13_3_0.9915_[0.9946 0.9755 0.996  0.9932 0.9983].png
img: 44 evaluate_data/Mosaics/E2CNN/test/13_4_0.9924_[0.9836 0.9984 0.9967 0.9945 0.989 ].png
img: 45 evaluate_data/Mosaics/E2CNN/test/13_5_0.9945_[0.9937 0.9979 0.999  0.9971 0.9849].png
img: 46 evaluate_data/Mosaics/E2CNN/test/13_6_0.9803_[0.9983 0.9722 0.9389 0.9936 0.9986].png
img: 47 evaluate_data/Mosaics/E2CNN/test/13_7_0.991_[0.98   0.9966 0.9938 0.9861 0.9986].png
img: 48 evaluate_data/Mosaics/E2CNN/test/13_8_0.9873_[0.9978 0.997  0.9938 0.9645 0.9835].png
img: 49 evaluate_data/Mosaics/E2CNN/test/13_9_0.9925_[0.9954 0.9905 0.998  0.9983 0.9802].png
img: 50 evaluate_data/Mosaics/E2CNN/test/14_0_0.9951_[0.996  0.9971 0.9919 0.9956 0.9947].png
img: 51 evaluate_data/Mosaics/E2CNN/test/14_1_0.9966_[0.9972 0.9976 0.9974 0.9951 0.9958].png
img: 52 evaluate_data/Mosaics/E2CNN/test/14_2_0.9971_[0.9977 0.9976 0.9957 0.9987 0.9956].png
img: 53 evaluate_data/Mosaics/E2CNN/test/14_3_0.9968_[0.9965 0.9963 0.9973 0.9974 0.9966].png
img: 54 evaluate_data/Mosaics/E2CNN/test/14_4_0.9966_[0.9963 0.9976 0.9972 0.9963 0.9957].png
img: 55 evaluate_data/Mosaics/E2CNN/test/14_5_0.9946_[0.9962 0.9977 0.9933 0.99   0.996 ].png
img: 56 evaluate_data/Mosaics/E2CNN/test/14_6_0.996_[0.9985 0.9967 0.9954 0.995  0.9945].png
img: 57 evaluate_data/Mosaics/E2CNN/test/14_7_0.9961_[0.996  0.9929 0.9962 0.9976 0.9979].png
img: 58 evaluate_data/Mosaics/E2CNN/test/14_8_0.9967_[0.9978 0.9966 0.9944 0.9977 0.9969].png
img: 59 evaluate_data/Mosaics/E2CNN/test/14_9_0.9965_[0.9951 0.9968 0.9977 0.9956 0.9972].png
img: 60 evaluate_data/Mosaics/E2CNN/test/15_0_0.9964_[0.9942 0.9977 0.9961 0.9971 0.997 ].png
img: 61 evaluate_data/Mosaics/E2CNN/test/15_1_0.9959_[0.9967 0.9974 0.9949 0.9984 0.992 ].png
img: 62 evaluate_data/Mosaics/E2CNN/test/15_2_0.9949_[0.9919 0.9953 0.997  0.9958 0.9944].png
img: 63 evaluate_data/Mosaics/E2CNN/test/15_3_0.9939_[0.9978 0.992  0.9914 0.9917 0.9967].png
img: 64 evaluate_data/Mosaics/E2CNN/test/15_4_0.9948_[0.9975 0.9974 0.9951 0.9901 0.9941].png
img: 65 evaluate_data/Mosaics/E2CNN/test/15_5_0.9966_[0.9979 0.9976 0.9964 0.9942 0.9969].png
img: 66 evaluate_data/Mosaics/E2CNN/test/15_6_0.9971_[0.9984 0.9984 0.9971 0.9943 0.9971].png
img: 67 evaluate_data/Mosaics/E2CNN/test/15_7_0.995_[0.9968 0.9963 0.9932 0.9926 0.9959].png
img: 68 evaluate_data/Mosaics/E2CNN/test/15_8_0.9963_[0.9988 0.9972 0.9967 0.9975 0.9915].png
img: 69 evaluate_data/Mosaics/E2CNN/test/15_9_0.9952_[0.9938 0.997  0.9921 0.9957 0.9974].png
img: 70 evaluate_data/Mosaics/E2CNN/test/1_0_0.9966_[0.9969 0.9962 0.9976 0.9951 0.9973].png
img: 71 evaluate_data/Mosaics/E2CNN/test/1_1_0.9958_[0.9973 0.998  0.9927 0.997  0.9941].png
img: 72 evaluate_data/Mosaics/E2CNN/test/1_2_0.9965_[0.9967 0.997  0.9968 0.9943 0.9979].png
img: 73 evaluate_data/Mosaics/E2CNN/test/1_3_0.9949_[0.9933 0.9926 0.9959 0.9962 0.9968].png
img: 74 evaluate_data/Mosaics/E2CNN/test/1_4_0.9958_[0.9978 0.9921 0.9974 0.9943 0.9975].png
img: 75 evaluate_data/Mosaics/E2CNN/test/1_5_0.9964_[0.9964 0.9978 0.9952 0.9978 0.9946].png
img: 76 evaluate_data/Mosaics/E2CNN/test/1_6_0.994_[0.9963 0.9896 0.993  0.9965 0.9947].png
img: 77 evaluate_data/Mosaics/E2CNN/test/1_7_0.9967_[0.9971 0.9965 0.9974 0.998  0.9946].png
img: 78 evaluate_data/Mosaics/E2CNN/test/1_8_0.9968_[0.9971 0.9961 0.9977 0.9951 0.9978].png
img: 79 evaluate_data/Mosaics/E2CNN/test/1_9_0.9956_[0.9978 0.9957 0.995  0.9943 0.9952].png
img: 80 evaluate_data/Mosaics/E2CNN/test/2_0_0.995_[0.9947 0.9975 0.9958 0.9895 0.9973].png
img: 81 evaluate_data/Mosaics/E2CNN/test/2_1_0.9951_[0.9954 0.9943 0.9974 0.9988 0.9895].png
img: 82 evaluate_data/Mosaics/E2CNN/test/2_2_0.9957_[0.9937 0.9973 0.9977 0.9934 0.9965].png
img: 83 evaluate_data/Mosaics/E2CNN/test/2_3_0.996_[0.997  0.9983 0.9908 0.996  0.9978].png
img: 84 evaluate_data/Mosaics/E2CNN/test/2_4_0.9963_[0.9947 0.9953 0.9978 0.9979 0.9959].png
img: 85 evaluate_data/Mosaics/E2CNN/test/2_5_0.99_[0.9988 0.9909 0.9799 0.9826 0.9977].png
img: 86 evaluate_data/Mosaics/E2CNN/test/2_6_0.9949_[0.9912 0.9945 0.996  0.9972 0.9957].png
img: 87 evaluate_data/Mosaics/E2CNN/test/2_7_0.9947_[0.9913 0.9961 0.9965 0.9961 0.9933].png
img: 88 evaluate_data/Mosaics/E2CNN/test/2_8_0.9953_[0.9892 0.9962 0.9977 0.9976 0.996 ].png
img: 89 evaluate_data/Mosaics/E2CNN/test/2_9_0.9955_[0.9967 0.9986 0.9968 0.9963 0.9889].png
img: 90 evaluate_data/Mosaics/E2CNN/test/3_0_0.995_[0.9931 0.9888 0.9979 0.9994 0.9959].png
img: 91 evaluate_data/Mosaics/E2CNN/test/3_1_0.9921_[0.9991 0.9923 0.9907 0.9869 0.9913].png
img: 92 evaluate_data/Mosaics/E2CNN/test/3_2_0.9959_[0.9961 0.9991 0.9945 0.9942 0.9958].png
img: 93 evaluate_data/Mosaics/E2CNN/test/3_3_0.99_[0.9975 0.9988 0.9716 0.9876 0.9947].png
img: 94 evaluate_data/Mosaics/E2CNN/test/3_4_0.9958_[0.9996 0.9968 0.994  0.9963 0.9921].png
img: 95 evaluate_data/Mosaics/E2CNN/test/3_5_0.9964_[0.9964 0.9959 0.9943 0.9959 0.9993].png
img: 96 evaluate_data/Mosaics/E2CNN/test/3_6_0.9949_[0.9957 0.9925 0.9991 0.9916 0.9953].png
img: 97 evaluate_data/Mosaics/E2CNN/test/3_7_0.996_[0.9961 0.9951 0.9953 0.9993 0.9944].png
img: 98 evaluate_data/Mosaics/E2CNN/test/3_8_0.9955_[0.9968 0.9944 0.9991 0.9952 0.9918].png
img: 99 evaluate_data/Mosaics/E2CNN/test/3_9_0.9963_[0.9967 0.9944 0.996  0.9994 0.9953].png
img: 100 evaluate_data/Mosaics/E2CNN/test/4_0_0.9931_[0.9971 0.9908 0.9902 0.994  0.9934].png
img: 101 evaluate_data/Mosaics/E2CNN/test/4_1_0.9964_[0.9972 0.9984 0.9948 0.997  0.9946].png
img: 102 evaluate_data/Mosaics/E2CNN/test/4_2_0.996_[0.998  0.9962 0.9968 0.9963 0.9925].png
img: 103 evaluate_data/Mosaics/E2CNN/test/4_3_0.9901_[0.9979 0.9854 0.995  0.9778 0.9945].png
img: 104 evaluate_data/Mosaics/E2CNN/test/4_4_0.9957_[0.9955 0.9951 0.9958 0.995  0.9972].png
img: 105 evaluate_data/Mosaics/E2CNN/test/4_5_0.9957_[0.9944 0.9926 0.9976 0.9963 0.9973].png
img: 106 evaluate_data/Mosaics/E2CNN/test/4_6_0.9963_[0.9981 0.9979 0.9951 0.9956 0.9948].png
img: 107 evaluate_data/Mosaics/E2CNN/test/4_7_0.9973_[0.9974 0.9959 0.9979 0.9972 0.9979].png
img: 108 evaluate_data/Mosaics/E2CNN/test/4_8_0.9958_[0.9968 0.9979 0.9939 0.9956 0.9947].png
img: 109 evaluate_data/Mosaics/E2CNN/test/4_9_0.996_[0.9983 0.9961 0.9962 0.9961 0.9935].png
img: 110 evaluate_data/Mosaics/E2CNN/test/5_0_0.992_[0.9986 0.9888 0.9908 0.9975 0.9843].png
img: 111 evaluate_data/Mosaics/E2CNN/test/5_1_0.9918_[0.9918 0.9908 0.983  0.9962 0.9974].png
img: 112 evaluate_data/Mosaics/E2CNN/test/5_2_0.9919_[0.9929 0.9874 0.9932 0.9904 0.9958].png
img: 113 evaluate_data/Mosaics/E2CNN/test/5_3_0.9908_[0.9925 0.9953 0.9957 0.9853 0.9851].png
img: 114 evaluate_data/Mosaics/E2CNN/test/5_4_0.9915_[0.9917 0.9975 0.9937 0.9814 0.993 ].png
img: 115 evaluate_data/Mosaics/E2CNN/test/5_5_0.988_[0.9983 0.9848 0.9759 0.9842 0.997 ].png
img: 116 evaluate_data/Mosaics/E2CNN/test/5_6_0.9921_[0.9977 0.9965 0.9896 0.9931 0.9837].png
img: 117 evaluate_data/Mosaics/E2CNN/test/5_7_0.9919_[0.9968 0.9981 0.9898 0.9898 0.9851].png
img: 118 evaluate_data/Mosaics/E2CNN/test/5_8_0.9927_[0.995  0.9979 0.994  0.9857 0.9909].png
img: 119 evaluate_data/Mosaics/E2CNN/test/5_9_0.9881_[0.9969 0.9834 0.9967 0.9812 0.9824].png
img: 120 evaluate_data/Mosaics/E2CNN/test/6_0_0.9974_[0.9979 0.9979 0.9981 0.9972 0.996 ].png
img: 121 evaluate_data/Mosaics/E2CNN/test/6_1_0.99_[0.9963 0.9774 0.9974 0.9822 0.9968].png
img: 122 evaluate_data/Mosaics/E2CNN/test/6_2_0.9962_[0.9974 0.9966 0.9963 0.9939 0.9969].png
img: 123 evaluate_data/Mosaics/E2CNN/test/6_3_0.9962_[0.9974 0.9964 0.9929 0.9971 0.9969].png
img: 124 evaluate_data/Mosaics/E2CNN/test/6_4_0.9966_[0.9983 0.9967 0.9966 0.9941 0.9972].png
img: 125 evaluate_data/Mosaics/E2CNN/test/6_5_0.9968_[0.9979 0.9951 0.9964 0.9977 0.9969].png
img: 126 evaluate_data/Mosaics/E2CNN/test/6_6_0.9968_[0.998  0.9966 0.9951 0.9979 0.9967].png
img: 127 evaluate_data/Mosaics/E2CNN/test/6_7_0.995_[0.9973 0.9954 0.9951 0.9924 0.9948].png
img: 128 evaluate_data/Mosaics/E2CNN/test/6_8_0.9968_[0.9984 0.9968 0.995  0.9975 0.9964].png
img: 129 evaluate_data/Mosaics/E2CNN/test/6_9_0.9958_[0.9965 0.9937 0.9962 0.9961 0.9968].png
img: 130 evaluate_data/Mosaics/E2CNN/test/7_0_0.9964_[0.9961 0.9972 0.995  0.9971 0.9963].png
img: 131 evaluate_data/Mosaics/E2CNN/test/7_1_0.9942_[0.9965 0.9912 0.9936 0.9931 0.9965].png
img: 132 evaluate_data/Mosaics/E2CNN/test/7_2_0.9952_[0.9978 0.9973 0.991  0.9932 0.9968].png
img: 133 evaluate_data/Mosaics/E2CNN/test/7_3_0.9966_[0.9975 0.996  0.9968 0.9983 0.9941].png
img: 134 evaluate_data/Mosaics/E2CNN/test/7_4_0.9956_[0.9976 0.9956 0.9918 0.9977 0.9953].png
img: 135 evaluate_data/Mosaics/E2CNN/test/7_5_0.9948_[0.995  0.9908 0.9951 0.9963 0.9966].png
img: 136 evaluate_data/Mosaics/E2CNN/test/7_6_0.9959_[0.9958 0.997  0.9954 0.996  0.9955].png
img: 137 evaluate_data/Mosaics/E2CNN/test/7_7_0.9959_[0.9962 0.9975 0.9926 0.9972 0.9959].png
img: 138 evaluate_data/Mosaics/E2CNN/test/7_8_0.9933_[0.9958 0.9938 0.9893 0.9916 0.9959].png
img: 139 evaluate_data/Mosaics/E2CNN/test/7_9_0.995_[0.9944 0.9938 0.9968 0.9956 0.9943].png
img: 140 evaluate_data/Mosaics/E2CNN/test/8_0_0.9958_[0.999  0.9938 0.9934 0.9965 0.9963].png
img: 141 evaluate_data/Mosaics/E2CNN/test/8_1_0.9965_[0.9963 0.9975 0.9985 0.9948 0.9954].png
img: 142 evaluate_data/Mosaics/E2CNN/test/8_2_0.9952_[0.9978 0.9954 0.9914 0.9973 0.9939].png
img: 143 evaluate_data/Mosaics/E2CNN/test/8_3_0.9967_[0.9955 0.998  0.9952 0.9987 0.9962].png
img: 144 evaluate_data/Mosaics/E2CNN/test/8_4_0.9967_[0.995  0.9975 0.9977 0.9985 0.9951].png
img: 145 evaluate_data/Mosaics/E2CNN/test/8_5_0.997_[0.9974 0.9979 0.9981 0.9962 0.9953].png
img: 146 evaluate_data/Mosaics/E2CNN/test/8_6_0.9967_[0.9988 0.9953 0.9958 0.9977 0.9957].png
img: 147 evaluate_data/Mosaics/E2CNN/test/8_7_0.9962_[0.9988 0.9986 0.9951 0.9949 0.9937].png
img: 148 evaluate_data/Mosaics/E2CNN/test/8_8_0.9957_[0.9943 0.9972 0.9927 0.9958 0.9983].png
img: 149 evaluate_data/Mosaics/E2CNN/test/8_9_0.9963_[0.9964 0.9977 0.9951 0.995  0.9971].png
img: 150 evaluate_data/Mosaics/E2CNN/test/9_0_0.9947_[0.9992 0.9964 0.9918 0.9892 0.9967].png
img: 151 evaluate_data/Mosaics/E2CNN/test/9_1_0.9953_[0.997  0.9938 0.9989 0.9976 0.9893].png
img: 152 evaluate_data/Mosaics/E2CNN/test/9_2_0.9948_[0.9907 0.9966 0.9976 0.9941 0.995 ].png
img: 153 evaluate_data/Mosaics/E2CNN/test/9_3_0.9954_[0.9995 0.9925 0.9911 0.9975 0.9966].png
img: 154 evaluate_data/Mosaics/E2CNN/test/9_4_0.9914_[0.9934 0.9927 0.9962 0.9767 0.9981].png
img: 155 evaluate_data/Mosaics/E2CNN/test/9_5_0.9945_[0.9992 0.9921 0.9961 0.9974 0.9876].png
img: 156 evaluate_data/Mosaics/E2CNN/test/9_6_0.9954_[0.9944 0.9989 0.9965 0.9916 0.9957].png
img: 157 evaluate_data/Mosaics/E2CNN/test/9_7_0.9928_[0.9977 0.9971 0.9831 0.9872 0.9991].png
img: 158 evaluate_data/Mosaics/E2CNN/test/9_8_0.9954_[0.9968 0.9953 0.9948 0.9918 0.9984].png
img: 159 evaluate_data/Mosaics/E2CNN/test/9_9_0.9956_[0.9962 0.9962 0.9916 0.9993 0.9946].png
iou list:
[0.9947, 0.9941, 0.9946, 0.993, 0.9952, 0.992, 0.9952, 0.994, 0.9915, 0.9928, 0.9966, 0.9933, 0.9954, 0.9946, 0.9942, 0.9956, 0.9947, 0.9917, 0.9953, 0.984, 0.9932, 0.9946, 0.9953, 0.9949, 0.9937, 0.9952, 0.9946, 0.9944, 0.9923, 0.9937, 0.9944, 0.9946, 0.9927, 0.9944, 0.9955, 0.9956, 0.9951, 0.9944, 0.9945, 0.9954, 0.9911, 0.9832, 0.9904, 0.9915, 0.9924, 0.9945, 0.9803, 0.991, 0.9873, 0.9925, 0.9951, 0.9966, 0.9971, 0.9968, 0.9966, 0.9946, 0.996, 0.9961, 0.9967, 0.9965, 0.9964, 0.9959, 0.9949, 0.9939, 0.9948, 0.9966, 0.9971, 0.995, 0.9963, 0.9952, 0.9966, 0.9958, 0.9965, 0.9949, 0.9958, 0.9964, 0.994, 0.9967, 0.9968, 0.9956, 0.995, 0.9951, 0.9957, 0.996, 0.9963, 0.99, 0.9949, 0.9947, 0.9953, 0.9955, 0.995, 0.9921, 0.9959, 0.99, 0.9958, 0.9964, 0.9949, 0.996, 0.9955, 0.9963, 0.9931, 0.9964, 0.996, 0.9901, 0.9957, 0.9957, 0.9963, 0.9973, 0.9958, 0.996, 0.992, 0.9918, 0.9919, 0.9908, 0.9915, 0.988, 0.9921, 0.9919, 0.9927, 0.9881, 0.9974, 0.99, 0.9962, 0.9962, 0.9966, 0.9968, 0.9968, 0.995, 0.9968, 0.9958, 0.9964, 0.9942, 0.9952, 0.9966, 0.9956, 0.9948, 0.9959, 0.9959, 0.9933, 0.995, 0.9958, 0.9965, 0.9952, 0.9967, 0.9967, 0.997, 0.9967, 0.9962, 0.9957, 0.9963, 0.9947, 0.9953, 0.9948, 0.9954, 0.9914, 0.9945, 0.9954, 0.9928, 0.9954, 0.9956]
2022-12-26 15:34:51.933890, iou: tensor([0.9968, 0.9954, 0.9952, 0.9954, 0.9958], device='cuda:0'), 0.9957
/scratch/yy3u19/anaconda3/lib/python3.9/site-packages/e2cnn/nn/modules/r2_conv/basisexpansion_singleblock.py:80: UserWarning: indexing with dtype torch.uint8 is now deprecated, please use a dtype torch.bool instead. (Triggered internally at  /opt/conda/conda-bld/pytorch_1639180549130/work/aten/src/ATen/native/IndexingUtils.h:30.)
  full_mask[mask] = norms.to(torch.uint8)
---------- kernel_size: 3 ---------- classes: 5 ---------- model: E2CNN ---------- rotations: -1 ---------- dataset: Mosaics - test ----------
num of trainable parameters:13983429
Loading model checkpoints/Mosaics/lr_0.002_bn_16_epoch_70_E2CNN_Ksize_3_rotation_-1.pth num of rotations of filters: -1
Using device cuda
----------------------------------------------------------------------------------------------------------------------------------------------------------------
Num of images for evaulation: 160
img: 0 evaluate_data/Mosaics/E2CNN/test/0_0_0.9958_[0.997631  0.9988795 0.9934494 0.9990305 0.9898067].png
img: 1 evaluate_data/Mosaics/E2CNN/test/0_1_0.9953_[0.9944645  0.9899485  0.9980058  0.99938756 0.9947596 ].png
img: 2 evaluate_data/Mosaics/E2CNN/test/0_2_0.9956_[0.9956854  0.9965926  0.9978061  0.99832445 0.9896139 ].png
img: 3 evaluate_data/Mosaics/E2CNN/test/0_3_0.9947_[0.99800646 0.9879441  0.9939519  0.99857944 0.99478143].png
img: 4 evaluate_data/Mosaics/E2CNN/test/0_4_0.9963_[0.99354863 0.9973553  0.9938774  0.9984905  0.997992  ].png
img: 5 evaluate_data/Mosaics/E2CNN/test/0_5_0.9927_[0.996441   0.99801934 0.985346   0.9864071  0.99734443].png
img: 6 evaluate_data/Mosaics/E2CNN/test/0_6_0.9966_[0.9943747 0.9963115 0.998629  0.9987871 0.994884 ].png
img: 7 evaluate_data/Mosaics/E2CNN/test/0_7_0.9953_[0.9962493  0.98858696 0.99907595 0.9939773  0.9985457 ].png
img: 8 evaluate_data/Mosaics/E2CNN/test/0_8_0.9955_[0.99881035 0.9905314  0.9982688  0.9943222  0.99574035].png
img: 9 evaluate_data/Mosaics/E2CNN/test/0_9_0.9947_[0.99883336 0.9948511  0.9869979  0.99500936 0.9979101 ].png
img: 10 evaluate_data/Mosaics/E2CNN/test/10_0_0.998_[0.9980134  0.99785453 0.9995487  0.9988142  0.99592173].png
img: 11 evaluate_data/Mosaics/E2CNN/test/10_1_0.9934_[0.9981147  0.9994755  0.9886374  0.99742985 0.9833903 ].png
img: 12 evaluate_data/Mosaics/E2CNN/test/10_2_0.995_[0.9990975  0.99274606 0.99213177 0.9941844  0.99706244].png
img: 13 evaluate_data/Mosaics/E2CNN/test/10_3_0.9964_[0.998222   0.9975605  0.992469   0.99868315 0.99522036].png
img: 14 evaluate_data/Mosaics/E2CNN/test/10_4_0.9968_[0.9987225  0.9993414  0.99261844 0.9970883  0.9960348 ].png
img: 15 evaluate_data/Mosaics/E2CNN/test/10_5_0.9958_[0.9983425  0.99419945 0.99437004 0.99796474 0.9941073 ].png
img: 16 evaluate_data/Mosaics/E2CNN/test/10_6_0.9952_[0.99729633 0.9969442  0.9978534  0.9896511  0.9944014 ].png
img: 17 evaluate_data/Mosaics/E2CNN/test/10_7_0.9971_[0.99870735 0.9991706  0.99616784 0.9946536  0.9967112 ].png
img: 18 evaluate_data/Mosaics/E2CNN/test/10_8_0.9967_[0.9952367  0.99756104 0.9982569  0.99573135 0.99693054].png
img: 19 evaluate_data/Mosaics/E2CNN/test/10_9_0.9902_[0.99691415 0.9938022  0.9788586  0.9829469  0.9985856 ].png
img: 20 evaluate_data/Mosaics/E2CNN/test/11_0_0.9952_[0.9977537 0.9872218 0.9958476 0.9985063 0.9965488].png
img: 21 evaluate_data/Mosaics/E2CNN/test/11_1_0.9958_[0.9988452  0.99555975 0.9977324  0.9982301  0.9888436 ].png
img: 22 evaluate_data/Mosaics/E2CNN/test/11_2_0.9971_[0.9987641 0.9985492 0.9976659 0.9979838 0.9924883].png
img: 23 evaluate_data/Mosaics/E2CNN/test/11_3_0.9958_[0.9982544  0.9974406  0.99775416 0.9977239  0.9880335 ].png
img: 24 evaluate_data/Mosaics/E2CNN/test/11_4_0.996_[0.99820924 0.99809766 0.99757224 0.9984491  0.9875725 ].png
img: 25 evaluate_data/Mosaics/E2CNN/test/11_5_0.9968_[0.9979414  0.9985069  0.99081755 0.99870574 0.9980608 ].png
img: 26 evaluate_data/Mosaics/E2CNN/test/11_6_0.9963_[0.9987588  0.998988   0.9882353  0.99889565 0.9963869 ].png
img: 27 evaluate_data/Mosaics/E2CNN/test/11_7_0.9944_[0.99759585 0.9954903  0.9970194  0.99782634 0.9841186 ].png
img: 28 evaluate_data/Mosaics/E2CNN/test/11_8_0.9968_[0.998482   0.99389523 0.9961546  0.9989084  0.99655205].png
img: 29 evaluate_data/Mosaics/E2CNN/test/11_9_0.9954_[0.9984987  0.99850255 0.99494267 0.98801726 0.9968405 ].png
img: 30 evaluate_data/Mosaics/E2CNN/test/12_0_0.9962_[0.9951643  0.99332494 0.9975451  0.9985444  0.9961985 ].png
img: 31 evaluate_data/Mosaics/E2CNN/test/12_1_0.9967_[0.99503744 0.9976877  0.99721634 0.997053   0.9964793 ].png
img: 32 evaluate_data/Mosaics/E2CNN/test/12_2_0.9963_[0.9980074  0.99813867 0.99538976 0.9928963  0.99689925].png
img: 33 evaluate_data/Mosaics/E2CNN/test/12_3_0.9958_[0.9981872  0.99401486 0.99754274 0.99506134 0.99407715].png
img: 34 evaluate_data/Mosaics/E2CNN/test/12_4_0.9966_[0.99584943 0.99419963 0.9980073  0.99726075 0.9977293 ].png
img: 35 evaluate_data/Mosaics/E2CNN/test/12_5_0.9971_[0.9970556  0.99555206 0.99693394 0.9984571  0.99732196].png
img: 36 evaluate_data/Mosaics/E2CNN/test/12_6_0.995_[0.9986316  0.99411964 0.9942696  0.99538445 0.992743  ].png
img: 37 evaluate_data/Mosaics/E2CNN/test/12_7_0.997_[0.99774903 0.9956343  0.99694073 0.99702126 0.9977735 ].png
img: 38 evaluate_data/Mosaics/E2CNN/test/12_8_0.9955_[0.99186504 0.9920278  0.9975868  0.9978252  0.9983261 ].png
img: 39 evaluate_data/Mosaics/E2CNN/test/12_9_0.9973_[0.9963741  0.9967301  0.99847186 0.9972165  0.99782515].png
img: 40 evaluate_data/Mosaics/E2CNN/test/13_0_0.9942_[0.99478495 0.999269   0.99432725 0.9976792  0.98471045].png
img: 41 evaluate_data/Mosaics/E2CNN/test/13_1_0.9944_[0.99200964 0.98533607 0.99895734 0.9983171  0.9973853 ].png
img: 42 evaluate_data/Mosaics/E2CNN/test/13_2_0.9866_[0.9902675  0.99573785 0.95384127 0.9988072  0.9945668 ].png
img: 43 evaluate_data/Mosaics/E2CNN/test/13_3_0.9949_[0.99401456 0.9862211  0.9982801  0.9970471  0.9989183 ].png
img: 44 evaluate_data/Mosaics/E2CNN/test/13_4_0.9946_[0.9860715  0.99867517 0.99782884 0.99574125 0.9944818 ].png
img: 45 evaluate_data/Mosaics/E2CNN/test/13_5_0.9952_[0.9953488  0.9988572  0.9989575  0.99686575 0.98597574].png
img: 46 evaluate_data/Mosaics/E2CNN/test/13_6_0.9787_[0.99844265 0.9829253  0.92777866 0.98510057 0.9990743 ].png
img: 47 evaluate_data/Mosaics/E2CNN/test/13_7_0.9955_[0.99082494 0.9982543  0.997229   0.99258363 0.9985971 ].png
img: 48 evaluate_data/Mosaics/E2CNN/test/13_8_0.994_[0.99868166 0.9990838  0.99740845 0.98377395 0.99101305].png
img: 49 evaluate_data/Mosaics/E2CNN/test/13_9_0.9959_[0.9981738  0.9941007  0.99861604 0.99843067 0.99040675].png
img: 50 evaluate_data/Mosaics/E2CNN/test/14_0_0.998_[0.9980356  0.9986736  0.9974732  0.99878544 0.99723023].png
img: 51 evaluate_data/Mosaics/E2CNN/test/14_1_0.997_[0.9981709  0.9979515  0.99734837 0.99558926 0.99592996].png
img: 52 evaluate_data/Mosaics/E2CNN/test/14_2_0.9976_[0.99788916 0.99799526 0.9970439  0.9990211  0.9960526 ].png
img: 53 evaluate_data/Mosaics/E2CNN/test/14_3_0.9984_[0.99833053 0.9977045  0.99905735 0.9990684  0.99801385].png
img: 54 evaluate_data/Mosaics/E2CNN/test/14_4_0.9962_[0.99464506 0.9962422  0.99749994 0.997196   0.9952703 ].png
img: 55 evaluate_data/Mosaics/E2CNN/test/14_5_0.9974_[0.99831605 0.9985001  0.99710226 0.9957848  0.99751765].png
img: 56 evaluate_data/Mosaics/E2CNN/test/14_6_0.997_[0.998677   0.99695885 0.99679786 0.99673647 0.99598646].png
img: 57 evaluate_data/Mosaics/E2CNN/test/14_7_0.9977_[0.9975719  0.99582124 0.9978083  0.99850273 0.9986224 ].png
img: 58 evaluate_data/Mosaics/E2CNN/test/14_8_0.9977_[0.9979909  0.99739885 0.9965839  0.9989104  0.99737483].png
img: 59 evaluate_data/Mosaics/E2CNN/test/14_9_0.9957_[0.9961398  0.9971632  0.99596876 0.99222773 0.9968191 ].png
img: 60 evaluate_data/Mosaics/E2CNN/test/15_0_0.9976_[0.9960413  0.9988188  0.99757314 0.99779433 0.9979028 ].png
img: 61 evaluate_data/Mosaics/E2CNN/test/15_1_0.9972_[0.9986702  0.9987031  0.99673337 0.9985112  0.9934787 ].png
img: 62 evaluate_data/Mosaics/E2CNN/test/15_2_0.9971_[0.9942069  0.9979079  0.99799806 0.99884635 0.9963717 ].png
img: 63 evaluate_data/Mosaics/E2CNN/test/15_3_0.9972_[0.99822813 0.9969176  0.9972778  0.9959199  0.9977411 ].png
img: 64 evaluate_data/Mosaics/E2CNN/test/15_4_0.996_[0.9980341  0.99765235 0.9967796  0.9933592  0.9939288 ].png
img: 65 evaluate_data/Mosaics/E2CNN/test/15_5_0.9969_[0.998029   0.99912655 0.99630237 0.99336374 0.9976384 ].png
img: 66 evaluate_data/Mosaics/E2CNN/test/15_6_0.9978_[0.9990559  0.9992807  0.99741447 0.9973475  0.9958894 ].png
img: 67 evaluate_data/Mosaics/E2CNN/test/15_7_0.9963_[0.99782276 0.99874127 0.9937809  0.9943829  0.996806  ].png
img: 68 evaluate_data/Mosaics/E2CNN/test/15_8_0.9972_[0.9987927  0.998595   0.99703187 0.99790925 0.993887  ].png
img: 69 evaluate_data/Mosaics/E2CNN/test/15_9_0.9968_[0.99530935 0.99756914 0.996397   0.9983561  0.9965854 ].png
img: 70 evaluate_data/Mosaics/E2CNN/test/1_0_0.9978_[0.99849737 0.9980737  0.9984996  0.9961777  0.9979921 ].png
img: 71 evaluate_data/Mosaics/E2CNN/test/1_1_0.9976_[0.9975385 0.9979657 0.9965283 0.998429  0.9972994].png
img: 72 evaluate_data/Mosaics/E2CNN/test/1_2_0.9977_[0.9979309  0.99788123 0.9981761  0.9962964  0.9982787 ].png
img: 73 evaluate_data/Mosaics/E2CNN/test/1_3_0.997_[0.9967272  0.9971875  0.99680287 0.99703014 0.99730724].png
img: 74 evaluate_data/Mosaics/E2CNN/test/1_4_0.9979_[0.9983216  0.99747884 0.99801743 0.9972998  0.998205  ].png
img: 75 evaluate_data/Mosaics/E2CNN/test/1_5_0.9971_[0.99799967 0.9988081  0.9959802  0.99721164 0.9957223 ].png
img: 76 evaluate_data/Mosaics/E2CNN/test/1_6_0.9975_[0.9973663  0.9969602  0.99712163 0.99823225 0.99802876].png
img: 77 evaluate_data/Mosaics/E2CNN/test/1_7_0.9973_[0.9975816  0.9976868  0.99741805 0.9986338  0.99508387].png
img: 78 evaluate_data/Mosaics/E2CNN/test/1_8_0.9978_[0.9979997 0.9971796 0.9986677 0.9970344 0.9983057].png
img: 79 evaluate_data/Mosaics/E2CNN/test/1_9_0.997_[0.997884   0.9986698  0.996064   0.99725354 0.9950155 ].png
img: 80 evaluate_data/Mosaics/E2CNN/test/2_0_0.9959_[0.99631155 0.9983443  0.9969917  0.98992795 0.99808943].png
img: 81 evaluate_data/Mosaics/E2CNN/test/2_1_0.9964_[0.99721503 0.9966463  0.9974545  0.9989202  0.9919378 ].png
img: 82 evaluate_data/Mosaics/E2CNN/test/2_2_0.9963_[0.99203646 0.9984263  0.9982193  0.99699277 0.99588096].png
img: 83 evaluate_data/Mosaics/E2CNN/test/2_3_0.997_[0.9977395  0.9986235  0.9935784  0.99686307 0.9981041 ].png
img: 84 evaluate_data/Mosaics/E2CNN/test/2_4_0.9975_[0.9963518 0.9977276 0.9980613 0.999046  0.9965092].png
img: 85 evaluate_data/Mosaics/E2CNN/test/2_5_0.9944_[0.999235   0.99328953 0.9899644  0.99154615 0.99804574].png
img: 86 evaluate_data/Mosaics/E2CNN/test/2_6_0.996_[0.9914534  0.99489677 0.9975413  0.99840724 0.9976637 ].png
img: 87 evaluate_data/Mosaics/E2CNN/test/2_7_0.9966_[0.9945793  0.99657875 0.9980296  0.997555   0.9960373 ].png
img: 88 evaluate_data/Mosaics/E2CNN/test/2_8_0.9967_[0.99457306 0.99777097 0.99820167 0.99707806 0.99567944].png
img: 89 evaluate_data/Mosaics/E2CNN/test/2_9_0.9957_[0.99150497 0.99746215 0.9984949  0.9972802  0.993765  ].png
img: 90 evaluate_data/Mosaics/E2CNN/test/3_0_0.9973_[0.99653286 0.99527544 0.9983143  0.9994069  0.99703985].png
img: 91 evaluate_data/Mosaics/E2CNN/test/3_1_0.9958_[0.9995773  0.99639314 0.9943922  0.9962764  0.99259895].png
img: 92 evaluate_data/Mosaics/E2CNN/test/3_2_0.9973_[0.9966759  0.9995032  0.99661374 0.99619085 0.9976405 ].png
img: 93 evaluate_data/Mosaics/E2CNN/test/3_3_0.995_[0.99818736 0.9989846  0.98777664 0.99328446 0.9965918 ].png
img: 94 evaluate_data/Mosaics/E2CNN/test/3_4_0.9967_[0.9996366  0.99725926 0.9954526  0.996634   0.99456495].png
img: 95 evaluate_data/Mosaics/E2CNN/test/3_5_0.9979_[0.99727863 0.9981457  0.9973629  0.99716365 0.9993402 ].png
img: 96 evaluate_data/Mosaics/E2CNN/test/3_6_0.9977_[0.99714273 0.99759775 0.9993995  0.99722964 0.99722046].png
img: 97 evaluate_data/Mosaics/E2CNN/test/3_7_0.9972_[0.99746895 0.99699336 0.99666893 0.9995477  0.9955229 ].png
img: 98 evaluate_data/Mosaics/E2CNN/test/3_8_0.9972_[0.99793756 0.9971343  0.99945134 0.99699277 0.9945682 ].png
img: 99 evaluate_data/Mosaics/E2CNN/test/3_9_0.9967_[0.99700123 0.9940614  0.99628925 0.9994736  0.996508  ].png
img: 100 evaluate_data/Mosaics/E2CNN/test/4_0_0.9961_[0.9978832  0.99655247 0.9933773  0.9978536  0.9947593 ].png
img: 101 evaluate_data/Mosaics/E2CNN/test/4_1_0.9971_[0.9980705  0.998695   0.99563366 0.9980073  0.99490833].png
img: 102 evaluate_data/Mosaics/E2CNN/test/4_2_0.9973_[0.9989919  0.99773395 0.99780107 0.99776036 0.994297  ].png
img: 103 evaluate_data/Mosaics/E2CNN/test/4_3_0.9954_[0.99606204 0.99427766 0.9970317  0.9952153  0.994371  ].png
img: 104 evaluate_data/Mosaics/E2CNN/test/4_4_0.9976_[0.99827373 0.9977891  0.9970402  0.996906   0.99786556].png
img: 105 evaluate_data/Mosaics/E2CNN/test/4_5_0.9975_[0.99773926 0.9965717  0.9984428  0.99706566 0.99751234].png
img: 106 evaluate_data/Mosaics/E2CNN/test/4_6_0.9976_[0.9986451  0.99890566 0.99678683 0.9977961  0.99601674].png
img: 107 evaluate_data/Mosaics/E2CNN/test/4_7_0.9981_[0.9978208  0.99635065 0.9989769  0.99862754 0.99861115].png
img: 108 evaluate_data/Mosaics/E2CNN/test/4_8_0.9963_[0.9977496  0.99839056 0.993826   0.9967668  0.994846  ].png
img: 109 evaluate_data/Mosaics/E2CNN/test/4_9_0.9975_[0.998779   0.9970178  0.9976417  0.99824363 0.9955867 ].png
img: 110 evaluate_data/Mosaics/E2CNN/test/5_0_0.9936_[0.99915755 0.99212563 0.99289894 0.9983389  0.98540896].png
img: 111 evaluate_data/Mosaics/E2CNN/test/5_1_0.9942_[0.9939155  0.9904486  0.9903723  0.997245   0.99879175].png
img: 112 evaluate_data/Mosaics/E2CNN/test/5_2_0.9874_[0.97690415 0.97373426 0.9966124  0.99219525 0.99761087].png
img: 113 evaluate_data/Mosaics/E2CNN/test/5_3_0.9929_[0.99417543 0.99652785 0.99649656 0.9908988  0.98626286].png
img: 114 evaluate_data/Mosaics/E2CNN/test/5_4_0.9937_[0.9941528  0.99653757 0.9942838  0.9900412  0.99323636].png
img: 115 evaluate_data/Mosaics/E2CNN/test/5_5_0.9953_[0.99874103 0.994644   0.9957045  0.9895446  0.9979409 ].png
img: 116 evaluate_data/Mosaics/E2CNN/test/5_6_0.9926_[0.9983582  0.9977915  0.9887732  0.99456626 0.98345107].png
img: 117 evaluate_data/Mosaics/E2CNN/test/5_7_0.9916_[0.99830586 0.99867284 0.98764914 0.99331063 0.9799068 ].png
img: 118 evaluate_data/Mosaics/E2CNN/test/5_8_0.994_[0.9955374  0.99843484 0.99581987 0.98452884 0.99592555].png
img: 119 evaluate_data/Mosaics/E2CNN/test/5_9_0.9939_[0.9977722  0.9919008  0.99755937 0.99493074 0.9873702 ].png
img: 120 evaluate_data/Mosaics/E2CNN/test/6_0_0.9971_[0.9979588 0.9973956 0.9977112 0.9970104 0.9951966].png
img: 121 evaluate_data/Mosaics/E2CNN/test/6_1_0.9971_[0.99710155 0.9964633  0.9978959  0.998798   0.99539447].png
img: 122 evaluate_data/Mosaics/E2CNN/test/6_2_0.996_[0.9982015  0.994774   0.99693525 0.99289095 0.9971792 ].png
img: 123 evaluate_data/Mosaics/E2CNN/test/6_3_0.9974_[0.9975095  0.9987326  0.99498355 0.9985287  0.9972654 ].png
img: 124 evaluate_data/Mosaics/E2CNN/test/6_4_0.9977_[0.9987449  0.9979071  0.9968823  0.99711424 0.9977711 ].png
img: 125 evaluate_data/Mosaics/E2CNN/test/6_5_0.9983_[0.99891675 0.9971411  0.9987111  0.99880064 0.9977605 ].png
img: 126 evaluate_data/Mosaics/E2CNN/test/6_6_0.9979_[0.998745   0.99768424 0.9966637  0.9984801  0.99777895].png
img: 127 evaluate_data/Mosaics/E2CNN/test/6_7_0.9978_[0.99837863 0.9982193  0.9975226  0.99765563 0.9971676 ].png
img: 128 evaluate_data/Mosaics/E2CNN/test/6_8_0.9979_[0.99899155 0.9981082  0.9959127  0.99880636 0.99768376].png
img: 129 evaluate_data/Mosaics/E2CNN/test/6_9_0.9971_[0.99776137 0.99702007 0.9964443  0.99770236 0.9966498 ].png
img: 130 evaluate_data/Mosaics/E2CNN/test/7_0_0.9973_[0.997197  0.9985471 0.9959859 0.9975737 0.9971847].png
img: 131 evaluate_data/Mosaics/E2CNN/test/7_1_0.9961_[0.9968286  0.99488014 0.9952413  0.9964467  0.9969893 ].png
img: 132 evaluate_data/Mosaics/E2CNN/test/7_2_0.9965_[0.99794763 0.9975513  0.9939715  0.99642205 0.9967323 ].png
img: 133 evaluate_data/Mosaics/E2CNN/test/7_3_0.9972_[0.99842715 0.9977475  0.99668103 0.9980219  0.99505085].png
img: 134 evaluate_data/Mosaics/E2CNN/test/7_4_0.9965_[0.9964696  0.99564785 0.9951833  0.99905294 0.9961988 ].png
img: 135 evaluate_data/Mosaics/E2CNN/test/7_5_0.9966_[0.9971781  0.99662083 0.9945544  0.9970972  0.9974674 ].png
img: 136 evaluate_data/Mosaics/E2CNN/test/7_6_0.997_[0.99656725 0.9976208  0.9969886  0.99695486 0.99694866].png
img: 137 evaluate_data/Mosaics/E2CNN/test/7_7_0.997_[0.9964433  0.9982313  0.9955092  0.9978273  0.99713266].png
img: 138 evaluate_data/Mosaics/E2CNN/test/7_8_0.9944_[0.99727845 0.99641085 0.98947304 0.990948   0.9976409 ].png
img: 139 evaluate_data/Mosaics/E2CNN/test/7_9_0.997_[0.99640304 0.9971334  0.9981474  0.99771166 0.99571407].png
img: 140 evaluate_data/Mosaics/E2CNN/test/8_0_0.9972_[0.9992252  0.9968543  0.99512637 0.99768716 0.9969904 ].png
img: 141 evaluate_data/Mosaics/E2CNN/test/8_1_0.9979_[0.99791783 0.99844676 0.9988457  0.9968536  0.99725527].png
img: 142 evaluate_data/Mosaics/E2CNN/test/8_2_0.9963_[0.99777126 0.99688727 0.9921746  0.9990407  0.995746  ].png
img: 143 evaluate_data/Mosaics/E2CNN/test/8_3_0.9977_[0.9966501  0.99887776 0.99671614 0.99861443 0.99774957].png
img: 144 evaluate_data/Mosaics/E2CNN/test/8_4_0.9978_[0.99649495 0.9985856  0.9984927  0.99930435 0.9960534 ].png
img: 145 evaluate_data/Mosaics/E2CNN/test/8_5_0.9976_[0.9984185  0.99864084 0.9982641  0.9968326  0.99574906].png
img: 146 evaluate_data/Mosaics/E2CNN/test/8_6_0.9975_[0.9990253  0.99614155 0.9973394  0.99860907 0.99652696].png
img: 147 evaluate_data/Mosaics/E2CNN/test/8_7_0.9976_[0.9992079  0.9988934  0.99673414 0.99678457 0.996259  ].png
img: 148 evaluate_data/Mosaics/E2CNN/test/8_8_0.998_[0.99696684 0.9979786  0.9976836  0.99858356 0.99859273].png
img: 149 evaluate_data/Mosaics/E2CNN/test/8_9_0.9977_[0.9982065  0.9986406  0.9973526  0.99606097 0.99838555].png
img: 150 evaluate_data/Mosaics/E2CNN/test/9_0_0.9958_[0.99901414 0.9972779  0.993454   0.9926084  0.99684095].png
img: 151 evaluate_data/Mosaics/E2CNN/test/9_1_0.998_[0.99828154 0.99754834 0.9992283  0.99888283 0.9959206 ].png
img: 152 evaluate_data/Mosaics/E2CNN/test/9_2_0.9958_[0.9919673  0.9970704  0.9980511  0.9958678  0.99611104].png
img: 153 evaluate_data/Mosaics/E2CNN/test/9_3_0.9965_[0.99957126 0.99419165 0.9936638  0.99804854 0.99686146].png
img: 154 evaluate_data/Mosaics/E2CNN/test/9_4_0.9964_[0.9955064  0.99758935 0.99610317 0.99461937 0.99804974].png
img: 155 evaluate_data/Mosaics/E2CNN/test/9_5_0.9965_[0.9995284 0.9953134 0.9973074 0.9980773 0.9923295].png
img: 156 evaluate_data/Mosaics/E2CNN/test/9_6_0.9975_[0.99797505 0.9990676  0.9984363  0.9948154  0.99710363].png
img: 157 evaluate_data/Mosaics/E2CNN/test/9_7_0.9969_[0.998689   0.99778754 0.9929382  0.9955898  0.99932474].png
img: 158 evaluate_data/Mosaics/E2CNN/test/9_8_0.9971_[0.9982729  0.9974228  0.9953684  0.99570966 0.99884295].png
img: 159 evaluate_data/Mosaics/E2CNN/test/9_9_0.9967_[0.9980493  0.9979156  0.99273807 0.9997213  0.99504924].png
iou list:
[0.9958, 0.9953, 0.9956, 0.9947, 0.9963, 0.9927, 0.9966, 0.9953, 0.9955, 0.9947, 0.998, 0.9934, 0.995, 0.9964, 0.9968, 0.9958, 0.9952, 0.9971, 0.9967, 0.9902, 0.9952, 0.9958, 0.9971, 0.9958, 0.996, 0.9968, 0.9963, 0.9944, 0.9968, 0.9954, 0.9962, 0.9967, 0.9963, 0.9958, 0.9966, 0.9971, 0.995, 0.997, 0.9955, 0.9973, 0.9942, 0.9944, 0.9866, 0.9949, 0.9946, 0.9952, 0.9787, 0.9955, 0.994, 0.9959, 0.998, 0.997, 0.9976, 0.9984, 0.9962, 0.9974, 0.997, 0.9977, 0.9977, 0.9957, 0.9976, 0.9972, 0.9971, 0.9972, 0.996, 0.9969, 0.9978, 0.9963, 0.9972, 0.9968, 0.9978, 0.9976, 0.9977, 0.997, 0.9979, 0.9971, 0.9975, 0.9973, 0.9978, 0.997, 0.9959, 0.9964, 0.9963, 0.997, 0.9975, 0.9944, 0.996, 0.9966, 0.9967, 0.9957, 0.9973, 0.9958, 0.9973, 0.995, 0.9967, 0.9979, 0.9977, 0.9972, 0.9972, 0.9967, 0.9961, 0.9971, 0.9973, 0.9954, 0.9976, 0.9975, 0.9976, 0.9981, 0.9963, 0.9975, 0.9936, 0.9942, 0.9874, 0.9929, 0.9937, 0.9953, 0.9926, 0.9916, 0.994, 0.9939, 0.9971, 0.9971, 0.996, 0.9974, 0.9977, 0.9983, 0.9979, 0.9978, 0.9979, 0.9971, 0.9973, 0.9961, 0.9965, 0.9972, 0.9965, 0.9966, 0.997, 0.997, 0.9944, 0.997, 0.9972, 0.9979, 0.9963, 0.9977, 0.9978, 0.9976, 0.9975, 0.9976, 0.998, 0.9977, 0.9958, 0.998, 0.9958, 0.9965, 0.9964, 0.9965, 0.9975, 0.9969, 0.9971, 0.9967]
2022-12-26 15:49:38.793076, iou: tensor([0.9977, 0.9973, 0.9966, 0.9972, 0.9966], device='cuda:0'), 0.9971
==============================================================================
Running epilogue script on alpha51.

Submit time  : 2022-12-26T15:21:01
Start time   : 2022-12-26T15:21:02
End time     : 2022-12-26T15:49:43
Elapsed time : 00:28:41 (Timelimit=08:00:00)

Job ID: 2349160
Cluster: i5
User/Group: yy3u19/fp
State: COMPLETED (exit code 0)
Nodes: 1
Cores per node: 4
CPU Utilized: 00:29:01
CPU Efficiency: 25.29% of 01:54:44 core-walltime
Job Wall-clock time: 00:28:41
Memory Utilized: 15.86 GB
Memory Efficiency: 75.19% of 21.09 GB

