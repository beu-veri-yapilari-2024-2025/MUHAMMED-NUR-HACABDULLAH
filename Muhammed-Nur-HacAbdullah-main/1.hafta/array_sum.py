"""
DİZİLERDE TOPLAMA (ARRAY SUMMATION)

Algoritma Açıklaması:
Bir dizideki tüm elemanların toplamını bulan algoritmalar.
Hem iterative hem de recursive implementasyonlar sunulmuştur.

Zaman Karmaşıklığı:
- En İyi Durum: O(n) - Tüm elemanları kontrol etmek gerekir
- Ortalama Durum: O(n) - Tüm elemanları kontrol etmek gerekir
- En Kötü Durum: O(n) - Tüm elemanları kontrol etmek gerekir

Alan Karmaşıklığı: 
- Iterative: O(1) - Sabit alan kullanımı
- Recursive: O(n) - Stack kullanımı
"""

def array_sum_iterative(arr):
    """
    İterative (döngü kullanarak) toplama
    
    Args:
        arr: Sayı dizisi
    
    Returns:
        int/float: Dizinin toplamı
    """
    total = 0
    for num in arr:
        total += num
    return total


def array_sum_recursive(arr, index=0):
    """
    Recursive (özyinelemeli) toplama
    
    Args:
        arr: Sayı dizisi
        index: Mevcut index (varsayılan 0)
    
    Returns:
        int/float: Dizinin toplamı
    """
    # Base case: Dizinin sonuna ulaşıldı
    if index >= len(arr):
        return 0
    
    # Recursive case: Mevcut eleman + kalan elemanların toplamı
    return arr[index] + array_sum_recursive(arr, index + 1)


def array_sum_recursive_v2(arr):
    """
    Recursive toplama - alternatif versiyon (liste slicing ile)
    
    Args:
        arr: Sayı dizisi
    
    Returns:
        int/float: Dizinin toplamı
    """
    # Base case: Boş dizi
    if len(arr) == 0:
        return 0
    
    # Base case: Tek elemanlı dizi
    if len(arr) == 1:
        return arr[0]
    
    # Recursive case: İlk eleman + geri kalan elemanların toplamı
    return arr[0] + array_sum_recursive_v2(arr[1:])


# Test Senaryoları
if __name__ == "__main__":
    print("=" * 60)
    print("DİZİLERDE TOPLAMA TEST SENARYOLARI")
    print("=" * 60)
    
    # Test 1: Pozitif sayılar
    test_array_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"\nTest 1: Pozitif Sayılar")
    print(f"Dizi: {test_array_1}")
    print(f"Iterative Toplam: {array_sum_iterative(test_array_1)}")
    print(f"Recursive Toplam (v1): {array_sum_recursive(test_array_1)}")
    print(f"Recursive Toplam (v2): {array_sum_recursive_v2(test_array_1)}")
    
    # Test 2: Negatif sayılar
    test_array_2 = [-5, -3, -1, 0, 1, 3, 5]
    print(f"\nTest 2: Negatif ve Pozitif Sayılar")
    print(f"Dizi: {test_array_2}")
    print(f"Iterative Toplam: {array_sum_iterative(test_array_2)}")
    print(f"Recursive Toplam (v1): {array_sum_recursive(test_array_2)}")
    print(f"Recursive Toplam (v2): {array_sum_recursive_v2(test_array_2)}")
    
    # Test 3: Ondalıklı sayılar
    test_array_3 = [1.5, 2.3, 3.7, 4.2, 5.8]
    print(f"\nTest 3: Ondalıklı Sayılar")
    print(f"Dizi: {test_array_3}")
    print(f"Iterative Toplam: {array_sum_iterative(test_array_3):.2f}")
    print(f"Recursive Toplam (v1): {array_sum_recursive(test_array_3):.2f}")
    print(f"Recursive Toplam (v2): {array_sum_recursive_v2(test_array_3):.2f}")
    
    # Test 4: Tek elemanlı dizi
    test_array_4 = [42]
    print(f"\nTest 4: Tek Elemanlı Dizi")
    print(f"Dizi: {test_array_4}")
    print(f"Iterative Toplam: {array_sum_iterative(test_array_4)}")
    print(f"Recursive Toplam (v1): {array_sum_recursive(test_array_4)}")
    print(f"Recursive Toplam (v2): {array_sum_recursive_v2(test_array_4)}")
    
    # Test 5: Boş dizi
    test_array_5 = []
    print(f"\nTest 5: Boş Dizi")
    print(f"Dizi: {test_array_5}")
    print(f"Iterative Toplam: {array_sum_iterative(test_array_5)}")
    print(f"Recursive Toplam (v1): {array_sum_recursive(test_array_5)}")
    print(f"Recursive Toplam (v2): {array_sum_recursive_v2(test_array_5)}")
    
    # Test 6: Büyük dizi
    test_array_6 = list(range(1, 101))  # 1'den 100'e kadar
    print(f"\nTest 6: Büyük Dizi (1-100)")
    print(f"Dizi: [1, 2, 3, ..., 100]")
    print(f"Iterative Toplam: {array_sum_iterative(test_array_6)}")
    print(f"Recursive Toplam (v1): {array_sum_recursive(test_array_6)}")
    # Not: v2 çok büyük dizilerde stack overflow'a neden olabilir
    
    print("\n" + "=" * 60)

