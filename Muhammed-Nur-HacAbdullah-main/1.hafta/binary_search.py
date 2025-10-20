"""
İKİLİ ARAMA (BINARY SEARCH) - RECURSIVE IMPLEMENTATION

Algoritma Açıklaması:
İkili arama, sıralı bir dizide belirli bir elemanı bulmak için kullanılan etkili bir arama algoritmasıdır.
Diziyi sürekli ikiye bölerek arama yapılır.

Zaman Karmaşıklığı:
- En İyi Durum: O(1) - Aranan eleman tam ortadadır
- Ortalama Durum: O(log n) - Aranan eleman dizinin herhangi bir yerindedir
- En Kötü Durum: O(log n) - Aranan eleman dizinin sonundadır veya dizide yoktur

Alan Karmaşıklığı: O(log n) - Recursive çağrılardan dolayı stack kullanımı
"""

def binary_search_recursive(arr, target, left, right):
    """
    Recursive ikili arama fonksiyonu
    
    Args:
        arr: Sıralı dizi
        target: Aranan değer
        left: Arama aralığının sol sınırı
        right: Arama aralığının sağ sınırı
    
    Returns:
        int: Elemanın index'i (bulunamazsa -1)
    """
    # Base case: Eleman bulunamadı
    if left > right:
        return -1
    
    # Ortanca elemanı bul
    mid = left + (right - left) // 2
    
    # Base case: Eleman bulundu
    if arr[mid] == target:
        return mid
    
    # Recursive case: Sol yarıda ara
    if arr[mid] > target:
        return binary_search_recursive(arr, target, left, mid - 1)
    
    # Recursive case: Sağ yarıda ara
    else:
        return binary_search_recursive(arr, target, mid + 1, right)


def binary_search(arr, target):
    """
    İkili arama için kolaylık fonksiyonu
    
    Args:
        arr: Sıralı dizi
        target: Aranan değer
    
    Returns:
        int: Elemanın index'i (bulunamazsa -1)
    """
    return binary_search_recursive(arr, target, 0, len(arr) - 1)


# Test Senaryoları
if __name__ == "__main__":
    print("=" * 60)
    print("İKİLİ ARAMA (BINARY SEARCH) TEST SENARYOLARI")
    print("=" * 60)
    
    # Test 1: Normal durum
    test_array_1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    target_1 = 7
    result_1 = binary_search(test_array_1, target_1)
    print(f"\nTest 1: Normal Durum")
    print(f"Dizi: {test_array_1}")
    print(f"Aranan: {target_1}")
    print(f"Sonuç: Index {result_1}" if result_1 != -1 else "Sonuç: Bulunamadı")
    
    # Test 2: Eleman dizide yok
    target_2 = 8
    result_2 = binary_search(test_array_1, target_2)
    print(f"\nTest 2: Eleman Dizide Yok")
    print(f"Dizi: {test_array_1}")
    print(f"Aranan: {target_2}")
    print(f"Sonuç: Index {result_2}" if result_2 != -1 else "Sonuç: Bulunamadı")
    
    # Test 3: En iyi durum (ortadaki eleman)
    test_array_3 = [10, 20, 30, 40, 50, 60, 70]
    target_3 = 40  # Ortadaki eleman
    result_3 = binary_search(test_array_3, target_3)
    print(f"\nTest 3: En İyi Durum (Ortadaki Eleman)")
    print(f"Dizi: {test_array_3}")
    print(f"Aranan: {target_3}")
    print(f"Sonuç: Index {result_3}")
    
    # Test 4: En kötü durum (son eleman)
    target_4 = 70
    result_4 = binary_search(test_array_3, target_4)
    print(f"\nTest 4: En Kötü Durum (Son Eleman)")
    print(f"Dizi: {test_array_3}")
    print(f"Aranan: {target_4}")
    print(f"Sonuç: Index {result_4}")
    
    # Test 5: Büyük dizi
    test_array_5 = list(range(0, 1000, 2))  # 0, 2, 4, ..., 998
    target_5 = 500
    result_5 = binary_search(test_array_5, target_5)
    print(f"\nTest 5: Büyük Dizi (500 eleman)")
    print(f"Dizi: [0, 2, 4, ..., 998]")
    print(f"Aranan: {target_5}")
    print(f"Sonuç: Index {result_5}")
    
    print("\n" + "=" * 60)

