Running SLURM prolog script on alpha54.cluster.local
===============================================================================
Job started on Wed Dec 21 22:17:45 GMT 2022
Job ID          : 2340867
Job name        : run_test
WorkDir         : /mainfs/scratch/yy3u19/myN-JetNet
Command         : /mainfs/scratch/yy3u19/myN-JetNet/run_test
Partition       : ecsall
Num hosts       : 1
Num cores       : 2
Num of tasks    : 1
Hosts allocated : alpha54
Job Output Follows ...
===============================================================================
-------------------- model name: RST-NJet n_rotations: 8 n_scales: 4 -------------------- dataset: GlaS
num of trainable parameters:1224158
Loading model checkpoints/GlaS_select_angle/True/0.004_16_70_N-Jet_order=2_scale=4_rotation=1.pth num of rotations of filters: 8
Using device cuda
----------------------------------------------------------------------------------------------------------------------------------------------------------------
Num of images for evaulation: 320
Traceback (most recent call last):
  File "/mainfs/scratch/yy3u19/myN-JetNet/evaluate_RST.py", line 212, in <module>
    mIoU, feats = predict_img(args.name, net, device, classes, args.data, n_channels)
  File "/mainfs/scratch/yy3u19/myN-JetNet/evaluate_RST.py", line 89, in predict_img
    Final_y_hat = F.softmax(F_out,dim=1)
  File "/scratch/yy3u19/anaconda3/lib/python3.9/site-packages/torch/nn/functional.py", line 1680, in softmax
    ret = input.softmax(dim)
AttributeError: 'list' object has no attribute 'softmax'
==============================================================================
Running epilogue script on alpha54.

Submit time  : 2022-12-21T22:17:44
Start time   : 2022-12-21T22:17:45
End time     : 2022-12-21T22:18:02
Elapsed time : 00:00:17 (Timelimit=1-00:00:00)

Job ID: 2340867
Cluster: i5
User/Group: yy3u19/fp
State: FAILED (exit code 1)
Nodes: 1
Cores per node: 2
CPU Utilized: 00:00:16
CPU Efficiency: 47.06% of 00:00:34 core-walltime
Job Wall-clock time: 00:00:17
Memory Utilized: 1.38 MB
Memory Efficiency: 0.01% of 10.55 GB

