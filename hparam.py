class hparams:

    train_or_test = 'train'
    output_dir = 'logs'
    aug = False
    latest_checkpoint_file = 'checkpoint_latest.pt'
    total_epochs = 5000000
    epochs_per_checkpoint = 10
    batch_size = 25
    ckpt = True
    init_lr = 0.0002
    scheduer_step_size = 20
    scheduer_gamma = 0.8
    debug = False
    mode = '2d' # '2d or '3d'
    in_class = 1
    out_class = 2

    crop_or_pad_size = 224,224,1 # if 3D: 256,256,256



    fold_arch = '*.png'

    source_train_0_dir = '/data/zkn/data/Medical_image_dataset/Classification/Montgomery County X-ray Set/train/0'
    source_train_1_dir = '/data/zkn/data/Medical_image_dataset/Classification/Montgomery County X-ray Set/train/1'
    source_test_0_dir = '/data/zkn/data/Medical_image_dataset/Classification/Shenzhen Hospital X-ray Set/test/0'
    source_test_1_dir = '/data/zkn/data/Medical_image_dataset/Classification/Shenzhen Hospital X-ray Set/test/1'
