## ChatBot part-ii Text to Speech

Bin Liang
2023-2-24

### Describe

In this part, we neeed a input which should be a text file or just a string. Then the user should request the language and the gender of the speaker. After that, run the script, we can get a `.wav` file which can be the input in part-iii.

### Required Packages 

we just need some very normal package:

1. torch, torchaudio
2. TTS
   
### Files structure
```bash
├── generate_speech.py  
├── README.md  
├── requirements.txt  
├── run_TTS.sh  
├── setup.sh  
├── text_input  
│   ├── README.md  
│   ├── text.txt  
│   └── 中文.txt  
├── TTS_checkpoints  
├── TTS_utils.py  
└── wav_output  
    ├── demo.wav  
    └── README.md  
```

The directorys:
1. text_input: if you want to use the text file to be the input in `generate_speech.py`, pleaser put the text file here.
2. TTS_checkpoints: Saving the `.pth` file here, but from now on we do not need it.
3. wav_output: the `.wav` file which we get wiul in this directory.

The scripts:
1. generate_speech.py: The inference script, do the TTS.
2. setup.sh: to do all the preparation.
3. run_TTS.sh: a using demo.
4. TTS_utils.py: I re-write the generate_speech.py to be a python function, which you can just use in other scripts.

### Using method

1. preparation:
```bash
conda activate [your python virtual enviroment]
cd [your path to]/chatbot_human/part_2_TTS
pip -r requirement.txt
``` 

or 

```bash 
bash setup.sh
```


If everything ok, you can check: `tts --list_models`

2. Using the generate_speech.py

There is a cli demo: run the `run_TTS.sh` bash script can get a demo.

there are four args in this script:

1. `--file_path`: The path input text.
2. `--text`: The text (str) which you want to use.

You can only use one of 1 and 2

3. `save_path` : the save path of the `.wav` file.
4. `language_gender`: you can onle use: `en_f` female English speaker; `en_m` male English speaker; `zn_f` female Chinese speaker.

These parameters have the same meaning in `TTS_utils.py`'s function `text2wav(language_gender, save_path, file_path, text)`


