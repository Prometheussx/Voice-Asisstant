# SESLİ ASİSTAN ALEXY
#Kütüphane
import speech_recognition as sr
from datetime import datetime
import webbrowser
import time
from gtts import gTTS
from playsound import playsound
import random
import os
"""-----------------------------------------------------------------"""

print("|------------------------------------------------------|")                                    
print("|       _  _  _  _  _  _  _  _  _  _  _  _  _          |")   
print("|      / \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \         |")
print("|                 _      ________   ____     __        |")                  
print("|           /\   | |    |  ____\ \ / /\ \   / /        |")
print("|          /  \  | |    | |__   \ V /  \ \_/ /         |")
print("|         / /\ \ | |    |  __|   > <    \   /          |")
print("|        / ____ \| |____| |____ / . \    | |           |")
print("|       /_/    \_\______|______/_/ \_\   |_|           |")     
print("|                                                      |")                    
print("|      \_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/         |")
print("|                                                      |")  
print("|                          *Creative By : Erdem Taha*  |")
print("|------------------------------------------------------|")
print("      *---------- SİSTEME HOŞGELDİNİZ ------------*     ")
time.sleep(0.4)
print("Alexy Açılıyor...")
time.sleep(0.5)
print("Alexy Sisteme Bağlandı.")


#Kısaltmaya Atama
r = sr.Recognizer()
#Dinleme -Algılama Fonksiyonu
def record(ask = False):
    #sr.Microphone Kaynak Olarak Al
    with sr.Microphone() as source:
         #içerde Soru Varsa İşlem Yap
        if ask:
            speak(ask)
        #Ses Dinle Kaynak Olarak Ata
        audio = r.listen(source)
        voice = ""
        #Sesi Googlda Tanımlat 
        try:
            voice = r.recognize_google(audio , language="tr-TR")
        #Algılama Eroru
        except sr.UnknownValueError:
            speak("Tekrar Edin Lütfen")
            
        #Sistem Eroru
        except sr.RequestError:
            speak("Sistem Çalışmıyor")            
        
        return voice
#Tanımlamalar
def response(voice):
    if "hey" in voice:
        speak("Buyrun Efendim")
        döngü()
    if "nasılsın" in voice:
        speak("İyiyim Siz Nasılsınız")
    if "saat kaç" in voice:
        speak(datetime.now().strftime('%H:%M'))
    #Arama Sistemi
    if "arama yap" in voice:
        #Soruy record gönder search ata
        search = record("Ne Aramamı İstiyorsunuz Efendim")
        print(search + " Hakkında Bilgiler Aranıyor")
        #Url Oluştur
        url = 'https://google.com/search?q='+search
        #google aç url arat
        webbrowser.get().open(url)
        speak("Google'da " + search + " İçin Buldukarım Efendim")
    return response
    
    


#asistanın sesi
def speak(string):
    #gTTS Alıcağı Değer Ve Dilini Belirledik Ve tts Değişkenine Atadık
    tts = gTTS(string,lang='tr')
    #Dosyaların çakışmaması için random değer ataması
    rand = random.randint(1,10000)
    #Dosyanın Adı,Formatı Ve Randomdan Alınan Değerin String İle İsme Eklenmesi
    file = 'audio-'+str(rand)+'.mp3'
    #Dosyayı gTTS ile Kaydettik
    tts.save(file)
    #Dosyayı Oynatmak için
    playsound(file)
    #Kaydedilen Dosyanın Silinmesini Sağlıyor (Fazla Yer Kaplamaması için)
    os.remove(file)


speak("Sisteme Hoşgeldiniz Efendim")
#time ile sonsuz döngüye aldık
time.sleep(1)
def döngü():
    while 1:
        speak("Size Nasıl Yardımcı Olabilirim ")
        time.sleep(2)
        print("İstekleriniz Dinleniyor...")
        #record fonksiyonunu kullanmak için atama yaptık
        voice = record()
        print("İstek Algılandı ==>" + voice)
        #respone voicden bilgi alıyo ve işliyoruz
        response(voice)
        if "kapat" in voice:
            speak("Sistem Kapanıyor Efendim")
            print("Sistem 3 Saniye İçerisinde Kapatılacaktır")
            time.sleep(3)
            break
döngü()
 
