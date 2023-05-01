# 實驗2.1: 熱傳實驗I 熱傳導

## 1. 實驗目的

驗證在一維且穩態(one dimensional, steady state)下的傅立葉熱傳導定律(Fourier's law of heat conduction)。

## 2. 實驗設備

1. Heat Conduction Unit: 如圖二所示，分成兩種型號，線型模式與徑向模式。
    1. 線型模式：一邊有一個加熱器產生熱，熱會通過外圍有絕熱材質的金屬棒，金屬棒上面有7個溫度計，每個相隔10mm，可以測量溫度。另一邊有冷卻裝置維持溫度。
    2. 徑向模式：加熱器在中間，外圍有金屬盤導熱，有7個溫度計，每個相隔20mm。最外圈有冷卻裝置。
2. 線型模式的測試棒3隻，材質如下：
    1. $\phi 30\text{mm}$ 黃銅
    2. $\phi 13\text{mm}$ 黃銅
    3. $\phi 30\text{mm}$ 不鏽鋼
3. 溫度顯示器：用來插在 heat conduction unit 上面測量溫度。
4. 冷卻水系統：放在 heat conduction unit 的一邊作為冷卻裝置製造溫度差。

![Figure-2](imgs/Figure-2.jpeg)

## 3. 實驗原理

1. 熱的傳導方式有三種：
    1. 熱傳導(thermal conduction)
    2. 熱對流(thermal convection)
    3. 熱輻射(thermal radiation)
2. Fourier's law 說明了熱傳導率與溫度梯度成正比。

$$q\propto \frac{\Delta T}{\Delta X}$$

- $q$: 熱傳導率
- $\displaystyle \frac{\Delta T}{\Delta X}$: 溫度梯度

3. 一維的 Fourier's law 可以寫成以下公式：

$$q = -KA \frac{dT}{dX}$$

- $A$: 截面積
- $K$: 熱傳導係數

![Figure-3](imgs/Figure-3.jpeg)

根據以上公式，可以得出圓柱棒的熱傳導係數 $K$ 為

$$K = \frac{qL}{(T_1 - T_2)A}$$

![Figure-4](imgs/Figure-4.jpeg)

4. 若金屬棒由不同材料組成，利用熱阻(thermal resistance)的概念可以得出熱傳導率為

$$q = \frac{T_1 - T_4}
           {\frac{\Delta x_A}{k_A A} + 
	    \frac{\Delta x_B}{k_B A} + 
	    \frac{\Delta x_C}{k_C A}}
    = \frac{T_1 - T_4}{R_A + R_B + R_C}$$

- $R_A, R_B. R_C$: 分別為 $A, B, C$ 材料的熱阻：

$$
\begin{array}{}
    R_A = \frac{\Delta x_A}{k_A A} \\
    R_B = \frac{\Delta x_B}{k_B A} \\
    R_C = \frac{\Delta x_C}{k_C A}
\end{array}
$$

![Figure-5](imgs/Figure-5.jpeg)

5. 在徑向系統下，Fourier's law 可以寫成以下公式：

$$q = -KA \frac{dT}{dr} = -2\pi Kr L \frac{dT}{dr}$$

6. 考慮在內圈 $r = r_i$ 與外圈 $$r = r_o 的溫度為 $T = T_i$ 與 $T = T_o$ ，則第五點的公式可以寫成：

$$q = 2\pi KL\frac{T_i - T_o}{\ln(r_o / r_i)}$$

![Figure-6](imgs/Figure-6.jpeg)

## 4. 實驗步驟

### 1. 線型模式(linear module)
ㄛ
1. 開啟冷卻水馬達，並確認水流有在循環。
2. 於黃銅的測試棒兩端塗上矽質黏土或散熱膏，以避免接觸面有空隙形成新的熱阻抗(contact resistance)。
3. 接好測試棒及線型模式的加熱電源線，並開啟電源。
4. 調整加熱功率至 30W，等待一段時間達到穩態後，量取各測量點溫度。
    - 注意任一點溫度不能超過 $100\degree \text C$，以免過熱。
5. 變更加熱功率為 50W 和 70W，並重複上述步驟。
6. 更換不同材質的測試棒（不銹鋼、鋁），並重複上物步驟，求得其熱傳遞係數 $K$。

### 2. 徑向模式(radial module)

1. 拔出線型模式的加熱電源線更換為徑向模式的，並重複上述步驟，求得熱傳遞係數 $K$。

### 注意事項

1. 任一點溫度不能超過 $100\degree C$，以避免過熱。
2. 實驗過後的測試棒溫度非常高，注意避免燙傷。
3. 常用材料的熱傳導係數：

| 材質               | 熱傳導係數 $\text W \cdot \text{m}^{-1}\text{K}^{-1}$ |
| ------------------ | ---------- |
| Brass (type CZ121) | 123        |
| Copper             | 353 to 386 |
| Stainless Steel    | 16         |
| Aluminium          | 205 to 237 |

# 實驗2-2: 熱傳實驗II 熱對流交錯流熱交換器

## 1. 實驗目的

觀察管簇(tube bundle)的排列方式，對交錯流熱交換器(Cross-flow Heat Exchanger)熱傳效率之影響，並利用此方法應用在實際熱交換器的設計。

## 2. 實驗設備

1. 交錯流熱交換器：上方有進氣口，下方側邊有出氣口。風會在管道內流動。見下圖。包含以下部分：
    1. 空氣管道(Air Duct): 垂直的管道，由玻璃與強化塑膠製成。截面積為 $65\times 150 \text{mm}$，長約 $1.2\text{ m}$，上方為喇叭狀之進氣口，而正前方中央有一個高 $200\text{ mm}$ 的開口，將配合不同面板使用。
    2. 風扇
    3. 風扇氣門：在風扇出口處控制出口面積，以改變管道空氣流速。

![pic2](imgs/exp-2-2_picture2.jpg)

2. 控制器(Instrument Console)
3. 加熱棒(Heater Element): 利用電力加熱的銅棒
    1. 直徑：$15.8\text{ mm}$
    2. 長度：$50\text{ mm}$
    3. 加熱表面積：$2.482\text{ m}^2$
    4. 電阻$R$：$70\Omega$
4. 標準面板(Standard Tube Plates)：
    1. 單管面板(Single Tube Plate)：一個高 $200\text{ mm}$ 的壓克力板，中間有一個孔可以插入加熱棒。
    2. 多管面板(Multi-Tube Plate)：和單管面板的尺寸相似，但有27根塑膠管在上面。可以拔掉替換為加熱棒。
5. 溫度計：電子溫度計，用來測量加熱棒表面溫度與管道內空氣的溫度。
6. 伏特計：類比伏特計，用來量測通過加熱棒的電壓。

## 3. 實驗原理

1. 熱量的基本傳遞方式有三種：
    1. 熱傳導(thermal conduction)
    2. 熱對流(thermal convection)
    3. 熱輻射(thermal radiation)
2. 工業上常利用流體來傳送熱能，利用熱交換器交換兩種或多種不同溫度流體間的熱量。
3. 熱交換器有許多形式，其中常見的一種是交錯流熱交換器(Cross-flow Heat Exchanger)。此交換器有一個流體在管簇內流動，另一流體在管簇外流動，以達到熱交換效果，如下圖：

![pic3](imgs/exp-2-2_picture3.png)

4. 交錯流熱交換器的筒體，其熱傳導係數(Heat Transfer Coefficient)由三個因素決定：
    1. 流體流經管內的表面熱傳係數。
    2. 管壁的熱傳導係數與厚度。
    3. 流體流經管外的表面熱傳係數。
5. 上面的三個因素中：
    1. 第一、二項可以藉由增加流速和減少管壁厚度，或使用高熱傳導係數的管材增加熱傳效果。
    2. 第三項可以藉由提升外部流體的流速（增加雷諾數）來提升表面熱傳係數。
    3. 變更管簇的排列方式也可以提升熱傳效率，減少熱交換器體積。變更管簇排列可以產生紊流，增加表面熱傳係數。本實驗測量這部分的影響。
6. 流體分為兩種流：
    1. 層流：流速慢且流線不會交錯混淆，主要靠熱傳導(conduction)來傳遞熱量。
    2. 紊流：流速快且流線相互混雜，可以快速傳遞熱量。雷諾數越高，熱傳效果越好。
7. 我們定義以下三個常數：

$$
\begin{array}{l}
    \text{Reynolds number: } & \text{Re}=\frac{\rho Ud}{\mu} \\
    \text{Prandtl number: } & \text{Pr}=\frac{C_p\mu}{k} \\
    \text{Nusselt number: } & \text{Nu}=\frac{hd}{k}
\end{array}
$$

- $k$: thermal conductivity
- $h$: surface heat transfer coefficient

8. 因為熱對流系統複雜，所以會用動力相似(dynamic similarity)的原理來分析，可以得出 Nusselt number 是雷諾數($\text{Re}$)與 Prandtl number 的函數：

$$\text{Nu} = f(\text{Re}, \text{Pr})$$

9. 無因次分析可以得到：

$$\text{Nu} = C \text{Re}^m \text{Pr}^n$$

- $C, m, n$: 常數

10. 經由實驗可以得到單管管子在交錯流熱交換器的 Nusselt number 為

$$\implies \text{Nu} = 0.714 \text{Re}^{0.618}$$

11. 當雷諾數介於 $4000 \sim 40000$ 時，將上式代入 Nusselt number 的定義可以得到：

$$h = \frac{k}{d}0.714 \text{Re}^{0.618}$$

12. 在多管管簇的交錯流熱交換器中，管道的截面積會縮小，導致流經管簇周邊的流體流速增加。流速可以用下面的公式修正：

$$U' = U \frac{A_d}{A_t}$$

- $A_d$: 無管簇的管道截面積
- $A_t$: 有管簇時的管道截面積

13. 經由實驗我們可以得到多管管簇在交錯流熱交換器的 Nusselt number 為：

$$
\text{Nu} = 0.273 \text{Re}^{0.635} \text{Pr}^{0.34} \text{Fn} \qquad \text{當 Re 介於 300~200000}
$$

- $\text{Fn}$: a function of the number of tube rows crossed by the transverse stream.

| Number of Rows Crossed | 2   | 3    | 4   | 5    | 6    | 8    | 10  |
| ---------------------- | --- | ---- | --- | ---- | ---- | ---- | --- |
| $\text{Fn}$            | 0.8 | 0.84 | 0.9 | 0.93 | 0.96 | 0.98 | 1   |

## 4. 相關計算

1. 加熱棒的熱傳率：

$$\dot Q = \frac{V^2}{R}$$

- $V$: 加熱棒的電壓
- $R$: 加熱棒的電阻，$70\Omega$

2. 熱通量：

$$\phi = \frac{\dot Q}{A}$$

- $A$: 加熱棒的表面積，$2.482 \times 10^{-3} \text{m}^2$

3. 加熱棒表面與空氣間之溫差：

$$T_s - T_a = \Delta T$$

- $T_a$: 管道內空氣溫度

4. 平均表面熱傳係數(Mean Surface Heat Transfer Coefficient) $h$:

$$
\begin{array}{l}
\displaystyle \phi = \frac{\dot Q}{A} = h(T_s - T_a) \\
\displaystyle h = \frac{\phi}{(T_s - T_a)}
\end{array}
$$

5. 管道空氣速度：
    1. 單管：直接利用風速計測得風速$U$。
    2. 多管：當管道內有管簇時，空氣流速會因為截面積的縮減而加快。因此空氣速度修正為：

$$
\begin{array}{l}
    U' = U \times \frac{A_d}{A_t} \\
    \qquad A_d: \text{無管簇時的管道截面積} 
           = 0.065\text{m} \times 0.15\text{m} 
	   = 9.75 \times 10^{-3} \text{m}^2 \\
    \qquad A_t: \text{無管簇時的管道截面積}
           = 4.16 \times 10^{-3} \text{m}^2 \\
    U' = 2.343 U
\end{array}
$$

6. 雷諾數：

$$\text{Re} = \frac{U\cdot d}{v}$$

7. Nusselt number：

$$
\begin{array}{l}
    \text{單管：} & \displaystyle 
                    \text{Nu} = \frac{h \cdot d}{k}
		    = 0.174 \text{Re}^{0.618}
    \text{多管：} & \text{Nu} 
                    = 0.273 \text{Re}^{0.635} \text{Pr}^{0.34} \text{Fn}
\end{array}
$$

- $\text{Fn}$: for 6 rows, 0.96

8. 平均表面熱傳係數（理論值）

$$
\begin{array}{l}
    \text{單管：} & h = \frac{k}{d}0.174 \text{Re}^{0.618} 
                      = 0.283 \text{Re}^{0.618} \\
    \text{多管：} & h = \frac{k}{d} 0.273 \text{Re}^{0.635} 
                        \text{Pr}^{0.34}
\end{array}
$$

9. 參考數據：

- 加熱棒的直徑：$d = 15.8\text{mm}$
