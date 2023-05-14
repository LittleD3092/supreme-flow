import matplotlib.pyplot as plt
from scipy import stats

linear_module_X = [length * 0.02 for length in range(7)]
linear_module_T_No1 = [50.4, 48.0, 44.8, 38.2, 29.0, 26.8, 24.8]
linear_module_T_No2 = [76.3, 71.2, 65.4, 52.3, 36.0, 31.7, 27.7]
linear_module_T_No3 = [46.0, 44.3, 42.0, 34.4, 26.3, 24.8, 23.6]
linear_module_T_No4 = [68.0, 63.9, 59.5, 44.7, 29.6, 27.1, 24.9]
linear_module_slope_No1, linear_module_intercept_No1, _, _, stderr = stats.linregress(linear_module_X, linear_module_T_No1)
linear_module_slope_No2, linear_module_intercept_No2, _, _, stderr = stats.linregress(linear_module_X, linear_module_T_No2)
linear_module_slope_No3, linear_module_intercept_No3, _, _, stderr = stats.linregress(linear_module_X, linear_module_T_No3)
linear_module_slope_No4, linear_module_intercept_No4, _, _, stderr = stats.linregress(linear_module_X, linear_module_T_No4)

linear_module_No1_Q = 15.072
linear_module_No2_Q = 29.7
linear_module_No3_Q = 14.88
linear_module_No4_Q = 29.565

linear_module_length = 6 * 0.02 # m
linear_module_area = 0.015 ** 2 * 3.14159 # m^2

radial_module_X = [length * 0.01 for length in range(7)]
radial_module_T_No1 = [28.5, 27.2, 26.0, 24.9, 24.2, 23.5, 22.9]
radial_module_T_No2 = [33.9, 31.2, 29.2, 27.1, 25.8, 24.6, 23.7]
radial_module_slope_No1, radial_module_intercept_No1, _, _, stderr = stats.linregress(radial_module_X, radial_module_T_No1)
radial_module_slope_No2, radial_module_intercept_No2, _, _, stderr = stats.linregress(radial_module_X, radial_module_T_No2)

radial_module_No1_Q = 14.378
radial_module_No2_Q = 30.457

radial_module_thickness = 0.005 # m
radial_module_area = (
    2 * 3.14159 * (
        0.01 * 7 + 0.01 * 1
    )/2 * radial_module_thickness
)

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 4))
# draw linear module
axes[0].plot(linear_module_X, linear_module_T_No1, '.', label='Brass 15W')
axes[0].plot(linear_module_X, linear_module_T_No2, '^', label='Brass 30W')
axes[0].plot(linear_module_X, linear_module_T_No3, 'o', label='Stainless Steel 15W')
axes[0].plot(linear_module_X, linear_module_T_No4, 'v', label='Stainless Steel 30W')

print("linear:")
print("黃銅15W 斜率: ", linear_module_slope_No1)
print("黃銅30W 斜率: ", linear_module_slope_No2)
print("不鏽鋼15W 斜率: ", linear_module_slope_No3)
print("不鏽鋼30W 斜率: ", linear_module_slope_No4)
print("---")
print(
    "黃銅15W K: ", 
    linear_module_No1_Q / (
        -linear_module_slope_No1 * linear_module_area
    )
)
print(
    "黃銅30W K: ",
    linear_module_No2_Q / (
        -linear_module_slope_No2 * linear_module_area
    )
)
print(
    "不鏽鋼15W K: ",
    linear_module_No3_Q / (
        -linear_module_slope_No3 * linear_module_area
    )
)
print(
    "不鏽鋼30W K: ",
    linear_module_No4_Q / (
        -linear_module_slope_No4 * linear_module_area
    )
)

axes[0].set_xlabel('Position (mm)')
axes[0].set_ylabel('Temperature (℃)')
axes[0].set_title('Linear Module')

# draw radial module
axes[1].plot(radial_module_X, radial_module_T_No1, '.', label='Brass 15W')
axes[1].plot(radial_module_X, radial_module_T_No2, 'o', label='Brass 30W')

print("---")
print("radial:")
print("黃銅15W 斜率: ", radial_module_slope_No1)
print("黃銅30W 斜率: ", radial_module_slope_No2)
print("---")
print(
    "黃銅15W K: ",
    radial_module_No1_Q / (
        -radial_module_slope_No1 * radial_module_area
    )
)
print(
    "黃銅30W K: ",
    radial_module_No2_Q / (
        -radial_module_slope_No2 * radial_module_area
    )
)

axes[1].set_xlabel('Position (mm)')
axes[1].set_ylabel('Temperature (℃)')
axes[1].set_title('Radial Module')

axes[0].legend()
axes[1].legend()
plt.show()