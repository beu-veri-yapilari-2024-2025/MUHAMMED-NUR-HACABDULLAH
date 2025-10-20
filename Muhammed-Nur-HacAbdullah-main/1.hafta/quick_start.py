"""
HIZLI BAŞLANGIÇ - Algoritmaların Basit Kullanımı

Bu dosya, her bir algoritmanın nasıl kullanılacağını gösteren basit örnekler içerir.
"""

from binary_search import binary_search
from array_sum import array_sum_iterative, array_sum_recursive
from linear_search import linear_search_iterative, linear_search_all_occurrences
from matrix_multiplication import matrix_multiply, print_matrix

def demo_binary_search():
    """İkili Arama Demosu"""
    print("\n" + "="*60)
    print("🔍 İKİLİ ARAMA (BINARY SEARCH) DEMO")
    print("="*60)
    
    # Sıralı bir dizi oluştur
    numbers = [2, 5, 8, 12, 16, 23, 38, 45, 56, 67, 78]
    target = 23
    
    print(f"\nSıralı Dizi: {numbers}")
    print(f"Aranan Sayı: {target}")
    
    result = binary_search(numbers, target)
    
    if result != -1:
        print(f"✅ Bulundu! Index: {result}")
        print(f"Doğrulama: numbers[{result}] = {numbers[result]}")
    else:
        print(f"❌ Bulunamadı!")


def demo_array_sum():
    """Dizi Toplama Demosu"""
    print("\n" + "="*60)
    print("➕ DİZİ TOPLAMA (ARRAY SUM) DEMO")
    print("="*60)
    
    numbers = [10, 20, 30, 40, 50]
    
    print(f"\nDizi: {numbers}")
    
    iter_sum = array_sum_iterative(numbers)
    rec_sum = array_sum_recursive(numbers)
    
    print(f"Iterative Toplam: {iter_sum}")
    print(f"Recursive Toplam: {rec_sum}")
    print(f"Python sum(): {sum(numbers)}")


def demo_linear_search():
    """Lineer Arama Demosu"""
    print("\n" + "="*60)
    print("🔎 LİNEER ARAMA (LINEAR SEARCH) DEMO")
    print("="*60)
    
    # Sırasız bir dizi
    fruits = ["elma", "armut", "kiraz", "muz", "üzüm", "kiraz", "çilek"]
    target = "kiraz"
    
    print(f"\nMeyve Listesi: {fruits}")
    print(f"Aranan: '{target}'")
    
    first_index = linear_search_iterative(fruits, target)
    all_indices = linear_search_all_occurrences(fruits, target)
    
    print(f"İlk Bulunma: Index {first_index}")
    print(f"Tüm Konumlar: {all_indices}")


def demo_matrix_multiplication():
    """Matris Çarpımı Demosu"""
    print("\n" + "="*60)
    print("✖️  MATRİS ÇARPIMI (MATRIX MULTIPLICATION) DEMO")
    print("="*60)
    
    # İki matris tanımla
    A = [[1, 2, 3],
         [4, 5, 6]]
    
    B = [[7, 8],
         [9, 10],
         [11, 12]]
    
    print(f"\nMatris A (2×3):")
    print_matrix(A, "A")
    
    print(f"\nMatris B (3×2):")
    print_matrix(B, "B")
    
    # Çarp
    C = matrix_multiply(A, B)
    
    print(f"\nSonuç C = A × B (2×2):")
    print_matrix(C, "C")


def main():
    """Ana fonksiyon - Tüm demoları çalıştır"""
    print("\n" + "="*60)
    print("🚀 VERİ YAPILARI VE ALGORİTMALAR - HIZLI BAŞLANGIÇ")
    print("="*60)
    
    # Tüm demoları çalıştır
    demo_binary_search()
    demo_array_sum()
    demo_linear_search()
    demo_matrix_multiplication()
    
    # Özet
    print("\n" + "="*60)
    print("📚 DAHA FAZLA BİLGİ")
    print("="*60)
    print("\nHer algoritmanın detaylı testleri için:")
    print("  • python3 binary_search.py")
    print("  • python3 array_sum.py")
    print("  • python3 linear_search.py")
    print("  • python3 matrix_multiplication.py")
    print("\nTüm testleri çalıştırmak için:")
    print("  • python3 run_all_tests.py")
    print("\nDetaylı dokümantasyon için:")
    print("  • README.md dosyasını okuyun")
    print("="*60)


if __name__ == "__main__":
    main()

