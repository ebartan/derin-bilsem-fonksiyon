def calculate_letter_value(letter):
    """
    Verilen Türkçe harfin alfabedeki sırasını bulup 2x-30 formülüyle hesaplar
    ve sonuca göre renkli çıktı verir
    """
    # Türkçe alfabe listesi
    turkish_alphabet = ['a', 'b', 'c', 'ç', 'd', 'e', 'f', 'g', 'ğ', 'h', 'ı', 'i', 
                       'j', 'k', 'l', 'm', 'n', 'o', 'ö', 'p', 'r', 's', 'ş', 't', 
                       'u', 'ü', 'v', 'y', 'z']
    
    # ANSI renk kodları
    BLUE = '\033[94m'
    RED = '\033[91m'
    RESET = '\033[0m'
    
    try:
        # Harfi küçük harfe çevir
        letter = letter.lower()
        
        # Harfin alfabedeki konumunu bul (1'den başlayarak)
        position = turkish_alphabet.index(letter) + 1
        
        # 2x-30 formülünü uygula
        result = 2 * position - 30
        
        # Sonucun mutlak değerini al
        abs_result = abs(result)
        
        # Sonuç negatifse mavi, pozitifse kırmızı renkte göster
        if result < 0:
            print(f"'{letter}' harfi için sonuç: {BLUE}{abs_result}{RESET}")
        else:
            print(f"'{letter}' harfi için sonuç: {RED}{abs_result}{RESET}")
            
        return abs_result
            
    except ValueError:
        print(f"Hata: '{letter}' Türkçe alfabede bulunamadı!")
        return None

# Test için örnek kullanım
#test_letters = ['e', 's', 'd', 'ş', 'k']
#for letter in test_letters:
    calculate_letter_value(letter)
print("Bir hafr girişi yapın")