# Streamlitライブラリをインポート
import streamlit as st

# ページ設定（タブに表示されるタイトル、表示幅）
st.set_page_config(page_title="時間計測", layout="wide")

# タイトルを設定
st.title('時間計測')

import time
import math

def factorize(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 1:
        factors.append(n)
    return factors

# 素因数分解対象の数
number_to_factorize = 1234567890

# 素因数分解の計測開始
start_time = time.time()

factors = factorize(number_to_factorize)

# 素因数分解の計測終了
end_time = time.time()

elapsed_time = end_time - start_time

print(f"素因数分解結果: {factors}")
print(f"素因数分解にかかる時間: {elapsed_time} 秒")