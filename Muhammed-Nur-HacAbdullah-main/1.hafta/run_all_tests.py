"""
TÜM TESTLERI ÇALIŞTIR

Bu script tüm algoritma dosyalarını çalıştırarak test sonuçlarını gösterir.
"""

import subprocess
import sys

def run_test(filename, description):
    """
    Bir test dosyasını çalıştırır ve sonucu gösterir
    
    Args:
        filename: Çalıştırılacak Python dosyası
        description: Test açıklaması
    """
    print("\n" + "="*80)
    print(f"🧪 {description}")
    print("="*80)
    
    try:
        result = subprocess.run(
            [sys.executable, filename],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        if result.returncode == 0:
            print(result.stdout)
            print(f"✅ {description} - BAŞARILI")
        else:
            print(result.stdout)
            print(result.stderr)
            print(f"❌ {description} - HATA")
            return False
            
    except subprocess.TimeoutExpired:
        print(f"⏱️ {description} - ZAMAN AŞIMI")
        return False
    except Exception as e:
        print(f"❌ {description} - BEKLENMEYEN HATA: {e}")
        return False
    
    return True

def main():
    """Ana test fonksiyonu"""
    print("\n" + "="*80)
    print("🚀 VERİ YAPILARI VE ALGORİTMALAR - TÜM TESTLER")
    print("="*80)
    
    tests = [
        ("binary_search.py", "İkili Arama (Binary Search)"),
        ("array_sum.py", "Dizilerde Toplama (Array Summation)"),
        ("linear_search.py", "Dizide Eleman Arama (Linear Search)"),
        ("matrix_multiplication.py", "Matris Çarpımı (Matrix Multiplication)")
    ]
    
    results = []
    
    for filename, description in tests:
        success = run_test(filename, description)
        results.append((description, success))
    
    # Özet
    print("\n" + "="*80)
    print("📊 TEST SONUÇLARI ÖZETİ")
    print("="*80)
    
    total = len(results)
    passed = sum(1 for _, success in results if success)
    failed = total - passed
    
    for description, success in results:
        status = "✅ BAŞARILI" if success else "❌ BAŞARISIZ"
        print(f"{status:15} - {description}")
    
    print("-"*80)
    print(f"Toplam: {total} test")
    print(f"✅ Başarılı: {passed}")
    print(f"❌ Başarısız: {failed}")
    print(f"📈 Başarı Oranı: {(passed/total)*100:.1f}%")
    print("="*80)
    
    if failed == 0:
        print("\n🎉 Tüm testler başarıyla tamamlandı!")
    else:
        print(f"\n⚠️ {failed} test başarısız oldu.")
    
    return failed == 0

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)

