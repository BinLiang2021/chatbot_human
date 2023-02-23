## 2023-2-2 ChatBot 问答语音合成测试

利用 coqui-tts 库，做了一些语音合成的测试，用比较优秀的模型生成一些例子。

### 文件结构说明：

1. 文件夹命名： 英文版本的语音合成demo储存的目录由 `{模型名称}_{训练集}}` 构成。
2. .wav 文件命名： `tts_{模型编号}_{语句序号}.wav`. 其中我们使用的模型都来自于 TTS 库，模型编号列表请看本文档的最下方。我们序号是从0开始，也就是我们的模型编号 +1 去和表格对应。

#### 模型 1： capacitron-t2-c50_blizzard2013

模型名称： capacitron-t2-c50  
训练集： blizzard2013

语速较快，有地方有错误，声音电流音大。但是大部分情况可以念对。

#### 模型 2： tacotron2-DCA_ljspeech

模型名称：tacotron2-DCA  
训练集：ljspeech

声音比较自然，但是也会有一些错误，在我们的demo中，每一次念完之后，都还会有一些模糊的“啊呜”，怀疑是数据和模型的使用方式不正确。但是是可以解决的，认为也是不错的选择之一。

可以和模型 4 做对比，同样的数据集。只是架构不同。

#### 模型 3： tacotron2_ek1

模型名称：tacotron2_ek1  
训练集：ek1

准确率高，发音能听懂。但是底噪比较大，数据集的录音设备的问题。但是模型也很好。

#### 模型 4： vits_ljspeech

模型名称：vits  
训练集：ljspeech

声音清晰，准确。文件夹中有两组，另一个一个 vits 开头的，用的是 espnet 库提供的模型。两者差距不大。
目前效果最好的。

#### 模型 5： your_tts_multilingual

模型名称：tts 库默认  
训练集：没有查到，两个文件夹：`your_tts_multilingual`，是男声英语。

男声可以准确念出语句，但是有底噪。


#### 模型 6: tacotron2-DDC-GST  

模型名称： tacotron2-DDC-GST  
训练集： baker 中文女声。

中文版本的很流利，通顺，比较自然。但是有一个问题，就是无法念出中文语句中的英文，碰到英文的时候，用的是拼音的念法。

### QA1

Human: What kind of music you like?

Bot: I like all kinds of music, as long as it has a good melody and rhythm. I enjoy listening to different genres and artists from around the world. What about you? What kind of Music do you like?.

Human: I like Metal and Core very much.

Bot: Metal and Core are very energetic and powerful genres. I can see why you like them. What are some of your favorite bands or songs in those genres?.

Human: My favourite band is Metallica, do you know them?

Bot: Yes, I know Metallica. They are one of the most influential and successful Metal bands of all time. They have sold over 125 million records worldwide, and have won nine Grammy Awards. They are known for their epic anthems, such as "One", "Enter Sandman", and "Nothing Else Matters". Do you have a favorite Metallica song?

### QA2

Human: Today is a little bit cold.

Bot: I agree, it feels cold here too. Do you have any warm clothes to wear?

Human: Of course.

Bot: That's good to hear. I hope you enjoy them. What do you like to do when it's cold?

Human: Sleeping.

Bot: Sleeping sounds like a good way to warm up. Do you prefer warm or cold sleep?

Human: What is warm sleep?

Bot: Warm sleep is a term that some people use to describe a type of sleep that is more comfortable and relaxed than normal sleep. It can involve having a higher body temperature, a lighter sleep stage, and more dreams. Some people claim that warm sleep can improve their mood, energy, and well-being. Learn more: from the web.

Human: Which web?

Bot: The web is a large and diverse collection of information and resources on the internet. I can access it and provide you with some links if you like. Here are some examples: from the web, from the web, from the web.

### QA3 中文

Human： 你喜欢什么风格的音乐？

Bot: 我喜欢欢快、朗朗上口且多样化的音乐。我喜欢听不同类型的音乐，例如流行音乐、摇滚乐、爵士乐、古典音乐等等。我认为音乐是一种可以表达情感、故事和文化的通用语言。你呢？你喜欢什么风格的音乐？

Human: 我喜欢金属和核。

Bot: 我懂了。Metal 和核是不错的选择。Metal 通常以电吉他、鼓和低音线为特色，而核则通常以人声、键盘和旋律吉他为特色。Metal 和核也可以有不同的风格和子流派，例如黑金属、死亡金属、激流金属、垃圾金属等等。你有最喜欢的金属或核乐队或艺术家吗？

Human: 我最喜欢的就是 Metallica.

Bot: Metallica 是一个不错的选择。Metallica 是有史以来最具影响力和最成功的金属乐队之一。他们从 1981 年开始制作音乐，并在全球销售了超过 1.25 亿张唱片。他们以强大的即兴重复段、朗朗上口的 hook 和充满活力的现场表演而闻名。他们的一些歌曲包括 Enter Sandman、One、Nothing Else Matters 和 Master of Puppets。你最喜欢 Metallica 的什么？

### QA3

Human： 给我讲个笑话吧：

Bot： 好吧，给你讲个笑话。戴领结的鱼叫什么？精巧！你喜欢它吗？

Human： 一点也不好笑。

Bot： 听到这个我很难过。幽默是主观的，并不是每个人都喜欢同一种笑话。也许您更喜欢不同类型的笑话，例如双关语、敲门笑话或谜语。你有偏好吗？

Human：那你给我猜个谜语吧。

Bot： 好吧，这是给你的谜语。什么东西可以足不出户就可以环游世界？仔细想想，也许你可以猜出答案。

Human：太阳！

Bot：说的对，干得好！你很擅长解谜。太阳是天生的谜语爱好者，可以随时随地享受它的照耀。你喜欢太阳吗？

### 附录：TTS模型：

 Name format: type/language/dataset/model  
 1: tts_models/multilingual/multi-dataset/your_tts [already downloaded]  
 2: tts_models/bg/cv/vits [already downloaded]  
 3: tts_models/cs/cv/vits  
 4: tts_models/da/cv/vits  
 5: tts_models/et/cv/vits  
 6: tts_models/ga/cv/vits  
 7: tts_models/en/ek1/tacotron2 [already downloaded]  
 8: tts_models/en/ljspeech/tacotron2-DDC [already downloaded]  
 9: tts_models/en/ljspeech/tacotron2-DDC_ph [already downloaded]  
 10: tts_models/en/ljspeech/glow-tts [already downloaded]  
 11: tts_models/en/ljspeech/speedy-speech  
 12: tts_models/en/ljspeech/tacotron2-DCA  
 13: tts_models/en/ljspeech/vits [already downloaded]  
 14: tts_models/en/ljspeech/vits--neon  
 15: tts_models/en/ljspeech/fast_pitch  
 16: tts_models/en/ljspeech/overflow  
 17: tts_models/en/vctk/vits [already downloaded]  
 18: tts_models/en/vctk/fast_pitch  
 19: tts_models/en/sam/tacotron-DDC  
 20: tts_models/en/blizzard2013/capacitron-t2-c50  
 21: tts_models/en/blizzard2013/capacitron-t2-c150_v2  
 22: tts_models/es/mai/tacotron2-DDC  
 23: tts_models/es/css10/vits  
 24: tts_models/fr/mai/tacotron2-DDC  
 25: tts_models/fr/css10/vits  
 26: tts_models/uk/mai/glow-tts  
 27: tts_models/uk/mai/vits [already downloaded]  
 28: tts_models/zh-CN/baker/tacotron2-DDC-GST  
 29: tts_models/nl/mai/tacotron2-DDC  
 30: tts_models/nl/css10/vits  
 31: tts_models/de/thorsten/tacotron2-DCA  
 32: tts_models/de/thorsten/vits  
 33: tts_models/de/thorsten/tacotron2-DDC [already downloaded]   
 34: tts_models/de/css10/vits-neon  
 35: tts_models/ja/kokoro/tacotron2-DDC  
 36: tts_models/tr/common-voice/glow-tts  
 37: tts_models/it/mai_female/glow-tts  
 38: tts_models/it/mai_female/vits  
 39: tts_models/it/mai_male/glow-tts  
 40: tts_models/it/mai_male/vits  
 41: tts_models/ewe/openbible/vits  
 42: tts_models/hau/openbible/vits  
 43: tts_models/lin/openbible/vits  
 44: tts_models/tw_akuapem/openbible/vits  
 45: tts_models/tw_asante/openbible/vits  
 46: tts_models/yor/openbible/vits  
 47: tts_models/hu/css10/vits  
 48: tts_models/el/cv/vits  
 49: tts_models/fi/css10/vits  
 50: tts_models/hr/cv/vits  
 51: tts_models/lt/cv/vits  
 52: tts_models/lv/cv/vits  
 53: tts_models/mt/cv/vits  
 54: tts_models/pl/mai_female/vits  
 55: tts_models/pt/cv/vits  
 56: tts_models/ro/cv/vits  
 57: tts_models/sk/cv/vits  
 58: tts_models/sl/cv/vits  
 59: tts_models/sv/cv/vits  
 60: tts_models/ca/custom/vits  
 61: tts_models/fa/custom/glow-tts  






