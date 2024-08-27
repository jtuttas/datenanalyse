import cv2
from PIL import Image
import re

from transformers import DonutProcessor, VisionEncoderDecoderModel
from datasets import load_dataset
import torch

allowed_cars = ["HAP515"]
# Initialisieren Sie die Kamera
cap = cv2.VideoCapture(0)  # '0' ist für die Standardkamera Ihres Computers.

processor = DonutProcessor.from_pretrained(
    "naver-clova-ix/donut-base-finetuned-cord-v2")
model = VisionEncoderDecoderModel.from_pretrained(
    "naver-clova-ix/donut-base-finetuned-cord-v2")

device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)
# load document image
#dataset = load_dataset("hf-internal-testing/example-documents", split="test")

try:
    # Endlosschleife
    while True:
        # Einzelnes Bild aufnehmen
        ret, frame = cap.read()

        # Überprüfen Sie, ob das Bild korrekt aufgenommen wurde
        if ret:
        # Konvertieren Sie das Bild von BGR zu RGB
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Erstellen Sie ein PIL.Image aus dem RGB-Frame
            pil_image = Image.fromarray(rgb_frame)
            image = pil_image
            # prepare decoder inputs
            task_prompt = "<s_cord-v2>"
            decoder_input_ids = processor.tokenizer(
                task_prompt, add_special_tokens=False, return_tensors="pt").input_ids

            pixel_values = processor(image, return_tensors="pt").pixel_values

            outputs = model.generate(
                pixel_values.to(device),
                decoder_input_ids=decoder_input_ids.to(device),
                max_length=model.decoder.config.max_position_embeddings,
                pad_token_id=processor.tokenizer.pad_token_id,
                eos_token_id=processor.tokenizer.eos_token_id,
                use_cache=True,
                bad_words_ids=[[processor.tokenizer.unk_token_id]],
                return_dict_in_generate=True,
            )

            sequence = processor.batch_decode(outputs.sequences)[0]
            sequence = sequence.replace(processor.tokenizer.eos_token, "").replace(
                processor.tokenizer.pad_token, "")
            # remove first task start token
            sequence = re.sub(r"<.*?>", "", sequence, count=1).strip()
            print(processor.token2json(sequence))
            
            seq = processor.token2json(sequence)
            seq = seq["text_sequence"].replace(".", "").replace(" ", "")
            cut_off_index = seq.find('<')
            if cut_off_index != -1:  # Find gibt -1 zurück, wenn das Zeichen nicht gefunden wird
                seq = seq[:cut_off_index]
            print(seq)

            found = False
            for car in allowed_cars:
                if car == seq:
                    print("Car is allowed")
                    found = True
                    break

            if not found:
                print("Car is not allowed")
            seq=""

except KeyboardInterrupt:
    print("Programm beendet")
finally:
    cap.release()