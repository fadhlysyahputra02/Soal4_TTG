import itertools
def cari_kombinasi(numbers, target):
    ops = ['+', '-', '*', '/']
    results = []

    for comb in itertools.product(ops, repeat=len(numbers) - 1):
        expr = ""
        for i in range(len(numbers)):
            expr += str(numbers[i])
            if i < len(comb):
                expr += comb[i]

        try:
            result = eval(expr)

            if abs(result - target) < 1e-9:
                results.append(expr)
        except ZeroDivisionError:
            continue

    return results


if __name__ == "__main__":
    print("=== 🔢 Pencari Ekspresi Sesuai Target ===")
    print("Masukkan angka dipisahkan spasi (contoh: 1 2 3 4):")
    user_input = input("Angka: ").strip()
    numbers = [int(x) for x in user_input.split()]

    target = float(input("Masukkan target: "))

    solutions = cari_kombinasi(numbers, target)

    print("\n📊 Hasil:")
    if solutions:
        for s in solutions:
            print("✅", s, "=", target)
    else:
        print("Tidak ditemukan kombinasi yang cocok.")
