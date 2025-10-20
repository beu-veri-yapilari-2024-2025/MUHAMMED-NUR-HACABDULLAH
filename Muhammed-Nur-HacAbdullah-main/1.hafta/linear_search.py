"""
DİZİDE ELEMAN ARAMA (LINEAR SEARCH)

Algoritma Açıklaması:
Lineer arama, bir dizide belirli bir elemanı bulmak için diziyi baştan sona 
tek tek kontrol eden basit bir arama algoritmasıdır.

Zaman Karmaşıklığı:
- En İyi Durum: O(1) - Aranan eleman dizinin başındadır
- Ortalama Durum: O(n/2) ≈ O(n) - Aranan eleman dizinin ortalarındadır
- En Kötü Durum: O(n) - Aranan eleman dizinin sonundadır veya dizide yoktur

Alan Karmaşıklığı: 
- Iterative: O(1) - Sabit alan kullanımı
- Recursive: O(n) - Stack kullanımı
"""

def linear_search_iterative(arr, target):
    """
    İterative (döngü kullanarak) lineer arama
    
    Args:
        arr: Dizi (sıralı olmak zorunda değil)
        target: Aranan değer
    
    Returns:
        int: Elemanın index'i (bulunamazsa -1)
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def linear_search_recursive(arr, target, index=0):
    """
    Recursive (özyinelemeli) lineer arama
    
    Args:
        arr: Dizi (sıralı olmak zorunda değil)
        target: Aranan değer
        index: Mevcut index (varsayılan 0)
    
    Returns:
        int: Elemanın index'i (bulunamazsa -1)
    """
    # Base case: Dizinin sonuna ulaşıldı, eleman bulunamadı
    if index >= len(arr):
        return -1
    
    # Base case: Eleman bulundu
    if arr[index] == target:
        return index
    
    # Recursive case: Sonraki elemana geç
    return linear_search_recursive(arr, target, index + 1)


def linear_search_all_occurrences(arr, target):
    """
    Bir elemanın dizideki tüm konumlarını bulur
    
    Args:
        arr: Dizi
        target: Aranan değer
    
    Returns:
        list: Elemanın bulunduğu tüm index'ler
    """
    indices = []
    for i in range(len(arr)):
        if arr[i] == target:
            indices.append(i)
    return indices


def linear_search_with_count(arr, target):
    """
    Elemana kaç adımda ulaşıldığını da döndürür
    
    Args:
        arr: Dizi
        target: Aranan değer
    
    Returns:
        tuple: (index, adım sayısı)
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return (i, i + 1)
    return (-1, len(arr))


# Test Senaryoları
if __name__ == "__main__":
    print("=" * 60)
    print("LİNEER ARAMA TEST SENARYOLARI")
    print("=" * 60)
    
    # Test 1: Normal durum
    test_array_1 = [64, 34, 25, 12, 22, 11, 90]
    target_1 = 22
    result_iter_1 = linear_search_iterative(test_array_1, target_1)
    result_rec_1 = linear_search_recursive(test_array_1, target_1)
    print(f"\nTest 1: Normal Durum")
    print(f"Dizi: {test_array_1}")
    print(f"Aranan: {target_1}")
    print(f"Iterative Sonuç: Index {result_iter_1}")
    print(f"Recursive Sonuç: Index {result_rec_1}")
    
    # Test 2: Eleman dizide yok
    target_2 = 100
    result_iter_2 = linear_search_iterative(test_array_1, target_2)
    result_rec_2 = linear_search_recursive(test_array_1, target_2)
    print(f"\nTest 2: Eleman Dizide Yok")
    print(f"Dizi: {test_array_1}")
    print(f"Aranan: {target_2}")
    print(f"Iterative Sonuç: {'Bulunamadı' if result_iter_2 == -1 else f'Index {result_iter_2}'}")
    print(f"Recursive Sonuç: {'Bulunamadı' if result_rec_2 == -1 else f'Index {result_rec_2}'}")
    
    # Test 3: En iyi durum (ilk eleman)
    target_3 = 64
    result_3, steps_3 = linear_search_with_count(test_array_1, target_3)
    print(f"\nTest 3: En İyi Durum (İlk Eleman)")
    print(f"Dizi: {test_array_1}")
    print(f"Aranan: {target_3}")
    print(f"Sonuç: Index {result_3}, {steps_3} adımda bulundu")
    
    # Test 4: En kötü durum (son eleman)
    target_4 = 90
    result_4, steps_4 = linear_search_with_count(test_array_1, target_4)
    print(f"\nTest 4: En Kötü Durum (Son Eleman)")
    print(f"Dizi: {test_array_1}")
    print(f"Aranan: {target_4}")
    print(f"Sonuç: Index {result_4}, {steps_4} adımda bulundu")
    
    # Test 5: Tekrar eden elemanlar
    test_array_5 = [3, 7, 2, 7, 9, 7, 1]
    target_5 = 7
    all_indices = linear_search_all_occurrences(test_array_5, target_5)
    print(f"\nTest 5: Tekrar Eden Elemanlar")
    print(f"Dizi: {test_array_5}")
    print(f"Aranan: {target_5}")
    print(f"İlk Bulunma: Index {linear_search_iterative(test_array_5, target_5)}")
    print(f"Tüm Konumlar: {all_indices}")
    
    # Test 6: String dizisi
    test_array_6 = ["elma", "armut", "kiraz", "üzüm", "çilek"]
    target_6 = "kiraz"
    result_6 = linear_search_iterative(test_array_6, target_6)
    print(f"\nTest 6: String Dizisi")
    print(f"Dizi: {test_array_6}")
    print(f"Aranan: '{target_6}'")
    print(f"Sonuç: Index {result_6}")
    
    print("\n" + "=" * 60)

