"""
MATRİS ÇARPIMI (MATRIX MULTIPLICATION)

Algoritma Açıklaması:
İki matrisin çarpımını hesaplayan algoritma. A(m×n) ve B(n×p) matrisleri 
çarpıldığında sonuç C(m×p) matrisi elde edilir.

Kural: A matrisinin sütun sayısı, B matrisinin satır sayısına eşit olmalıdır.

Zaman Karmaşıklığı:
- En İyi Durum: O(m × n × p) - Tüm elemanlar işlenmeli
- Ortalama Durum: O(m × n × p) - Tüm elemanlar işlenmeli
- En Kötü Durum: O(m × n × p) - Tüm elemanlar işlenmeli

Not: Klasik algoritma için O(n³) karmaşıklığı, Strassen algoritması O(n^2.807)

Alan Karmaşıklığı: O(m × p) - Sonuç matrisi için
"""

def matrix_multiply(A, B):
    """
    İki matrisi çarpar (klasik algoritma)
    
    Args:
        A: İlk matris (m × n)
        B: İkinci matris (n × p)
    
    Returns:
        list: Sonuç matrisi (m × p)
    
    Raises:
        ValueError: Matrisler çarpılamıyorsa
    """
    # Matris boyutlarını al
    if not A or not B:
        raise ValueError("Matrisler boş olamaz")
    
    m = len(A)          # A'nın satır sayısı
    n = len(A[0])       # A'nın sütun sayısı
    n2 = len(B)         # B'nin satır sayısı
    p = len(B[0])       # B'nin sütun sayısı
    
    # Çarpma kontrolü
    if n != n2:
        raise ValueError(f"Matrisler çarpılamaz: A({m}×{n}) × B({n2}×{p})")
    
    # Sonuç matrisini oluştur (m × p boyutunda, sıfırlarla doldur)
    C = [[0 for _ in range(p)] for _ in range(m)]
    
    # Matris çarpımı
    for i in range(m):
        for j in range(p):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    
    return C


def matrix_multiply_optimized(A, B):
    """
    Optimize edilmiş matris çarpımı (daha az bellek erişimi)
    
    Args:
        A: İlk matris (m × n)
        B: İkinci matris (n × p)
    
    Returns:
        list: Sonuç matrisi (m × p)
    """
    m = len(A)
    n = len(A[0])
    p = len(B[0])
    
    if n != len(B):
        raise ValueError("Matrisler çarpılamaz")
    
    # Sonuç matrisi
    C = [[0 for _ in range(p)] for _ in range(m)]
    
    # B matrisini transpose et (cache performansı için)
    B_T = [[B[j][i] for j in range(len(B))] for i in range(len(B[0]))]
    
    # Çarpım işlemi
    for i in range(m):
        for j in range(p):
            for k in range(n):
                C[i][j] += A[i][k] * B_T[j][k]
    
    return C


def print_matrix(matrix, name="Matris"):
    """
    Matrisi düzgün formatta yazdırır
    
    Args:
        matrix: Yazdırılacak matris
        name: Matris ismi
    """
    print(f"\n{name}:")
    for row in matrix:
        print("  [" + ", ".join(f"{val:6.2f}" if isinstance(val, float) else f"{val:6}" for val in row) + "]")


def get_matrix_dimensions(matrix):
    """
    Matris boyutlarını döndürür
    
    Args:
        matrix: Matris
    
    Returns:
        tuple: (satır sayısı, sütun sayısı)
    """
    return (len(matrix), len(matrix[0]) if matrix else 0)


def create_identity_matrix(n):
    """
    n×n birim matris oluşturur
    
    Args:
        n: Matris boyutu
    
    Returns:
        list: Birim matris
    """
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


# Test Senaryoları
if __name__ == "__main__":
    print("=" * 60)
    print("MATRİS ÇARPIMI TEST SENARYOLARI")
    print("=" * 60)
    
    # Test 1: Basit 2×2 matrisleri
    A1 = [[1, 2],
          [3, 4]]
    
    B1 = [[5, 6],
          [7, 8]]
    
    print("\nTest 1: 2×2 Matrisler")
    print_matrix(A1, "Matris A")
    print_matrix(B1, "Matris B")
    C1 = matrix_multiply(A1, B1)
    print_matrix(C1, "Sonuç (A × B)")
    
    # Test 2: Farklı boyutlu matrisler (3×2 ve 2×3)
    A2 = [[1, 2],
          [3, 4],
          [5, 6]]
    
    B2 = [[7, 8, 9],
          [10, 11, 12]]
    
    print("\n\nTest 2: Farklı Boyutlu Matrisler (3×2 ve 2×3)")
    dims_A2 = get_matrix_dimensions(A2)
    dims_B2 = get_matrix_dimensions(B2)
    print(f"A boyutu: {dims_A2[0]}×{dims_A2[1]}")
    print(f"B boyutu: {dims_B2[0]}×{dims_B2[1]}")
    print_matrix(A2, "Matris A")
    print_matrix(B2, "Matris B")
    C2 = matrix_multiply(A2, B2)
    dims_C2 = get_matrix_dimensions(C2)
    print(f"Sonuç boyutu: {dims_C2[0]}×{dims_C2[1]}")
    print_matrix(C2, "Sonuç (A × B)")
    
    # Test 3: Birim matris ile çarpım
    A3 = [[2, 3],
          [4, 5]]
    I3 = create_identity_matrix(2)
    
    print("\n\nTest 3: Birim Matris ile Çarpım")
    print_matrix(A3, "Matris A")
    print_matrix(I3, "Birim Matris I")
    C3 = matrix_multiply(A3, I3)
    print_matrix(C3, "Sonuç (A × I) = A")
    
    # Test 4: Ondalıklı sayılar
    A4 = [[1.5, 2.5],
          [3.5, 4.5]]
    
    B4 = [[0.5, 1.5],
          [2.5, 3.5]]
    
    print("\n\nTest 4: Ondalıklı Sayılar")
    print_matrix(A4, "Matris A")
    print_matrix(B4, "Matris B")
    C4 = matrix_multiply(A4, B4)
    print_matrix(C4, "Sonuç (A × B)")
    
    # Test 5: Tek satır ve tek sütun (vektör çarpımı)
    A5 = [[1, 2, 3]]  # 1×3 matris
    B5 = [[4],
          [5],
          [6]]        # 3×1 matris
    
    print("\n\nTest 5: Vektör Çarpımı (1×3 ve 3×1)")
    print_matrix(A5, "Matris A (Satır Vektörü)")
    print_matrix(B5, "Matris B (Sütun Vektörü)")
    C5 = matrix_multiply(A5, B5)
    print_matrix(C5, "Sonuç (A × B) = Skaler")
    print(f"Sonuç: {C5[0][0]}")
    
    # Test 6: Hata durumu - Çarpılamayan matrisler
    A6 = [[1, 2, 3],
          [4, 5, 6]]  # 2×3
    
    B6 = [[7, 8],
          [9, 10]]    # 2×2
    
    print("\n\nTest 6: Hata Durumu - Çarpılamayan Matrisler")
    dims_A6 = get_matrix_dimensions(A6)
    dims_B6 = get_matrix_dimensions(B6)
    print(f"A boyutu: {dims_A6[0]}×{dims_A6[1]}")
    print(f"B boyutu: {dims_B6[0]}×{dims_B6[1]}")
    try:
        C6 = matrix_multiply(A6, B6)
    except ValueError as e:
        print(f"Hata: {e}")
    
    # Test 7: Performans testi (büyük matrisler)
    import time
    
    print("\n\nTest 7: Performans Testi")
    size = 50
    A7 = [[i + j for j in range(size)] for i in range(size)]
    B7 = [[i - j for j in range(size)] for i in range(size)]
    
    print(f"İki {size}×{size} matris çarpılıyor...")
    start_time = time.time()
    C7 = matrix_multiply(A7, B7)
    end_time = time.time()
    print(f"Klasik Algoritma: {end_time - start_time:.4f} saniye")
    
    start_time = time.time()
    C7_opt = matrix_multiply_optimized(A7, B7)
    end_time = time.time()
    print(f"Optimize Edilmiş: {end_time - start_time:.4f} saniye")
    
    print("\n" + "=" * 60)

