python train.py \
  --cameras_glob ./glob/train/pro2test/*.txt \
  --image_dir /data/matryodshka/replica/pro2/ \
  --experiment_name pro2 \
  --shuffle_seq_length 7 \
  --input_type PRO2 \
  --pro2_calibration_file calibration.json \
  --max_steps 140000 \
  --operation train \
  --which_loss elpips
