from TTS.api import TTS
import time
import torch

def load_text(file_path):
    
    with open(file_path, "r") as f:
        text = f.readlines()
        
    return text[0]


def text2wav(language_gender, save_path, file_path="", text=""):
    """To do the TTS

    Args:
        language_gender (str): should be "en_f, en_m, zn_f" one of them
        save_path (str): the save path of .wav file
        file_path (str, optional): the file which contain the text we want to do the TTS. Defaults to "".
        text (str, optional): The string which we want to do the TTS. Defaults to "".
    """
    
    start = time.time()
    
    language, gender = (language_gender).split("_")
    
    # There are two ways to get the input.
    if text=="" and file_path != "":
        text = load_text(file_path)
    
    # model_name = TTS.list_models()[model]
    # model_name = "tts_models/en/ljspeech/vits"
    if language == "en":
        model_name = "tts_models/en/vctk/vits"
        if gender == "f":
            speaker = 76
        if gender == "m":
            speaker = 41
    if language == "zn":
        model_name = "tts_models/zh-CN/baker/tacotron2-DDC-GST"
    
    # Init TTS model
    if torch.cuda.is_available():
        gpu_sig = True
    else:
        gpu_sig = False
    tts = TTS(model_name, gpu=gpu_sig)

    # English : Woman 65/73/75/76, Man 41/77
    if language == "en":
        tts.tts_to_file(text=text, file_path=f"{save_path}/demo.wav", speaker=tts.speakers[speaker])
    if language == "zn":
        # I did not find the male's voice in zn-Ch
        tts.tts_to_file(text=text, file_path=f"{save_path}/demo.wav")
    
    end = time.time()
    # print(f"总花费时间：{end-start} 秒")
    
    