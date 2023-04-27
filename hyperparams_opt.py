# 🐝 Define sweep config for CNN, E2CNN, H-Nets
sweep_configuration = {
    'method': 'random',
    'name': 'CNN-sweep',
    'metric': {'goal': 'maximize', 'name': 'val_miou'},
    'parameters': 
    {
        'batch_size': {'max': 24, 'min': 2},
        'epochs': {'max': 70, 'min': 20},
        'lr': {'max': 0.1, 'min': 0.0001},
        'weight_decay': {'max': 1e-2, 'min': 1e-7}
     }
}