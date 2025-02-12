# Music Transformer Script: A ported script from Google Music Transformer notebook

This is a ported script from the original Google Music Transformer [notebook](https://colab.research.google.com/notebooks/magenta/piano_transformer/piano_transformer.ipynb).
By porting from notebook to script, automating music generation creative process will be much easier. Note that this repo
is only for music generation from pre-trained model only, not for training purpose.

## Installation:
You need to install [Magenta](https://github.com/tensorflow/magenta) package (support only Python >= 3.5) with correct version:
```bash
pip install magenta==1.3.1
```

If you have any issues regarding installation, you can install via this method:
```bash
cd <path_to_this_repo>; pip install -r requirements.txt
```
**Note**: Some packages in here are redundant since this is my local environment.
 
You also need to install `google cloud sdk` to get `Music Transformer` pre-trained model on cloud bucket. To get Google Cloud
SDK please follow this [installation guide](https://cloud.google.com/sdk/docs/downloads-versioned-archives).

## How to use
Download Music Transformer pre-trained model with Google Cloud SDK:
```
gsutil -q -m cp -r 'gs://magentadata/models/music_transformer/checkpoints/*' <destination folder>
```

### Unconditional Transformer:
You can generate music without any priming effect by simply type:

```bash
python unconditional_sample.py -model_path=path/to/model/checkpoints/unconditional_model_16.ckpt -output_dir=/tmp -decode_length=1024 -num_samples=1
```

or you can add primer by using `primer_path` parameter:
```bash
python unconditional_sample.py -model_path=magenta-music_transformer-folder/checkpoints/unconditional_model_16.ckpt -output_dir=results/ -decode_length=1024 -primer_path=magenta-music_transformer-folder/primers/goldberg17.mid -num_samples=1
```

### Conditional Transformer:
Generating music conditioned on midi file by typing:
```bash
python3 melody_sample.py -model_path=magenta-music_transformer-folder/checkpoints/melody_conditioned_model_16.ckpt -output_dir=results/ -decode_length=1024 -melody_path=data/goldberg17.mid -num_samples=1
```

### Music Generation Automation:
You can also create a whole new music melody by combining [SmallMusicVAE](https://github.com/Elvenson/midiMe) to generate your
own favorite melody and this Music Transformer to make your melody feel more natural and coherence. This repo also includes 
a bash script job to do just that:

```
sh music_generation.sh <path/to/midime_train.py> <path/to/midime_generate.py> <path/to/midime/tmp> <path/to/midime_training_tfrecord> <midime training step> <musicVAE model checkpoint> <number of melody samples to generate> <melody samples output path> <transformer uncoditioned checkpoint> <transformer conditioned checkpoint> <transformer output sample name> <transformer uncoditioned checkpoint> <transformer conditioned checkpoint>  
```

On how to create tfrecord for training `SmallMusicVAE`, you need to convert your melody midi file to tfrecord by 
following the instructions in [Building your Dataset](https://github.com/tensorflow/magenta/blob/master/magenta/scripts/README.md).
