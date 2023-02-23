# ffmpeg -ss 10 -i video_daliu.mp4 -t 1 -c copy video_daliu_1s.mp4



# tts --text "A facial composite is a graphical representation of one or more eyewitnesses' memories of a face, as recorded by a composite artist." --out_path sentence2audio.wav

# file_root="./data/中文"
# for i in 0
#     do
#     python inference_face.py --checkpoint_path wav2lip_gan.pth --face american_male.png --audio "$file_root/tts_m27_$i.wav" \
#     --outfile "american_male.mp4"
#     done


python inference_face.py \
    --checkpoint_path "checkpoints/wav2lip_gan.pth" \
    --face "data/face_imgs/asian_female_256x256.png" \
    --audio "data/中文/tts_m27_0.wav" \
    --outfile "results/asian_female.mp4"