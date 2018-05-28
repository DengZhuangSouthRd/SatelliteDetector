#!/usr/bin/env bash
python eval.py \
    --logtostderr \
    --checkpoint_dir=/Volumes/projects/DataSets/CSUVideo/300x300/models/ssd_incep_v3 \
    --pipeline_config_path=/Users/liuguiyang/github.com/tfmodels/object_detection/samples/ssd_inception_v2_csu.pbtxt \
    --eval_dir=/Volumes/projects/DataSets/CSUVideo/300x300/eval
