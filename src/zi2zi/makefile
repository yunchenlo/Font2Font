# Variables
SRCFONT = BIAUKAI
TARFONT = STZMF
BATCH = 32

# prepare dataset
prepare:
	ls # temporary
# train the UNET
train: prepare
	python train.py --experiment_dir=$(SRCFONT)_$(TARFONT)_6000/ \
					--experiment_id=0 \
					--batch_size=$(BATCH) \
					--lr=0.001 \
					--epoch=100 \
					--sample_steps=50 \
					--schedule=20 \
					--L1_penalty=100 \
					--Lconst_penalty=15 \
					--gpu 0

# eval the unet with our data
eval: prepare
	python infer.py --model_dir=$(SRCFONT)_$(TARFONT)_6000/checkpoint/experiment_0_batch_32/ \
                --batch_size=1 \
                --source_obj=demo_sample/$(SRCFONT)_$(TARFONT)/obj/val.obj \
                --embedding_ids=0 \
                --save_dir=test_save \
                --gpu 0
# run all
all: prepare train eval


.PHONY: all eval train prepare