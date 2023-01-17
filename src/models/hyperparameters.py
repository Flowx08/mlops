class hyperparameters:
    # Managing params
    save_model_path = "./models/model.pth"
    deploy_model_path = "./models/model_82_8.pth"

    # Model hyperparameters
    model_output_size = 10
    model_filter_k = 10
    image_size = 224
    efficientnet_num = 0
    num_classes = 6

    # Training params
    learningrate = 1e-4
    epochs = 2
    batch_size = 32
    num_workers = 8
