#!/usr/bin/env bash
python export_inference_graph.py \
    --input_type image_tensor \
    --pipeline_config_path=/Users/liuguiyang/github.com/tfmodels/object_detection/samples/ssd_inception_v2_csu.pbtxt \
    --trained_checkpoint_prefix=/Volumes/projects/DataSets/CSUVideo/300x300/models/ssd_incep_v3/model.ckpt-20000 \
    --output_directory=/Volumes/projects/DataSets/CSUVideo/300x300/models/ssd_incep_v3/exported_graphs
