# prepare dataset
prepare:
	ls # temporary
# train the UNET
train: prepare
	python train.py --experiment_dir=BIAUKAI_STZMF_6000/ \
					--experiment_id=0 \
					--batch_size=32 \
					--lr=0.001 \
					--epoch=100 \
					--sample_steps=50 \
					--schedule=20 \
					--L1_penalty=100 \
					--Lconst_penalty=15 \
					--gpu 0

# eval the unet with our data
eval: train prepare
	python infer.py --model_dir=BIAUKAI_STZMF_6000/checkpoint/experiment_0_batch_32/ \
                --batch_size=1 \
                --source_obj=demo_sample/BIAUKAI_STZMF/obj/val.obj \
                --embedding_ids=0 \
                --save_dir=test_save \
                --gpu 0
# run all
all: prepare train eval


.PHONY: all eval train prepare