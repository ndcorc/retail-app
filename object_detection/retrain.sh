printf "Creating train and test sets from object storage\n"
printf "________________________________________________\n\n"
python train_test_split.py

printf "\n\nGenerating tfrecord files from train and test sets\n"
printf "________________________________________________\n\n"
python generate_tfrecord.py

printf "\n\nTraining and evaluating new model on train and test tfrecords\n"
printf "________________________________________________\n\n"
python train.py --logtostderr --train_dir=models/model/train --pipeline_config_path=models/model/ssd_mobilenet_v1_coco.config &
python eval.py --logtostderr --checkpoint_dir=models/model/train/ --eval_dir=models/model/eval/ --pipeline_config_path=models/model/ssd_mobilenet_v1_coco.config &

