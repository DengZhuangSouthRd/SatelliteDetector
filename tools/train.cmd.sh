#!/usr/bin/env bash
python train.py \
    --logtostderr \
    --train_dir=/Volumes/projects/DataSets/CSUVideo/300x300/models/ssd_incep_v3 \
    --pipeline_config_path=/Users/liuguiyang/github.com/tfmodels/object_detection/samples/ssd_inception_v2_csu.pbtxt
