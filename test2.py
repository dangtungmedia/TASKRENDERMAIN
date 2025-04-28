import requests

# 1. URL server của bạn (thay thế đúng URL, nếu local thì http://127.0.0.1:8000 chẳng hạn)
url = 'http://your-server.com/announcement/saveNewText'

# 2. Các giá trị lấy từ phía front-end (giả sử bạn đã có hoặc bạn đọc từ đâu đó)
startText = "Start of translation"
mainText = "Main translated text"
endText = "End of translation"
repeatText = "Repeat part of translation"
selectedLanguage = "English"  # Giả sử người dùng chọn English
speedRangeValue = 5  # Speed được chọn
option1Checked = True
option2Checked = False
option3Checked = True
option4Checked = False
musicSelectValue = "background.mp3"
radio1Checked = True
musicPartSelectValue = "background_part.mp3"

# 3. Mapping cho Voice name giống trên web
voiceMap = {
    'Korean': 'nminseo',
    'English': '9BWtsMINqrJLrRacOk9x',
    'Japanese': 'nnaomi',
    'Chinese': 'zh-CN-XiaoxiaoNeural',
    'French': 'fr-FR-Studio-A',
    'German': 'de-DE-KatjaNeural',
    'Russian': 'ru-RU-DariyaNeural',
    'Arabic': 'ar-AE-FatimaNeural',
    'Spanish': 'es-US-PalomaNeural'
}
selectedVoice = voiceMap.get(selectedLanguage, '9BWtsMINqrJLrRacOk9x')

# 4. Đóng gói payload
payload = {
    'group': 'apt',
    'title': 'AI 번역 멘트',
    'text': mainText,
    'start_ment': startText,
    'ending_ment': endText,
    'middle_ment': repeatText,
    'language': selectedLanguage,
    'voice_name': selectedVoice,
    'settingsAsMent': True,
    'ment_speed': speedRangeValue,
    'auto_repeat_checked': option1Checked,
    'auto_repeat_ment': repeatText,
    'effect_sound_checked': option2Checked,
    'chime_sound_checked': option4Checked,
    'background_sound_checked': option3Checked,
    'background_sound_filename': musicSelectValue,
    'background_play_type': 'all' if radio1Checked else 'part',
    'background_sound_part_filename': musicPartSelectValue
}

# 5. Gửi POST request
response = requests.post(url, json=payload)

print("Status code:", response.status_code)
print("Response text:", response.text)  # In nội dung trả về

if response.status_code == 200:
    try:
        data = response.json()
        if data['result'] == 'success':
            print("저장 완료: 번역된 멘트가 성공적으로 저장되었습니다")
        elif data['result'] == 'duplicate':
            print("저장 실패: 동일한 제목의 멘트가 있습니다")
        else:
            print("저장 실패: 알 수 없는 오류 발생")
    except Exception as e:
        print("JSON decode error:", str(e))
else:
    print(f"서버 오류: {response.status_code}")
