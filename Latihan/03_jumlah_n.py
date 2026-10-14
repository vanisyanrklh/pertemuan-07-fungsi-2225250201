def jumlah_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# Test case
def test_case():
    for n in [1, 5, 10, 100]:
        hasil_loop = jumlah_n(n)
        hasil_rumus = n * (n + 1) // 2
        status = "BENAR" if hasil_loop == hasil_rumus else "SALAH"
        print(f"n = {n}, loop = {hasil_loop}, rumus = {hasil_rumus}, status = {status}")

# Jalankan test case
test_case()
