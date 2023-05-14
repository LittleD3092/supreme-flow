import math
import numpy as np
import matplotlib.pyplot as plt

PART_REYNOLDS_NUMBER = False
PART_NUSSELT_NUMBER = False
PART_DRAW = True

if PART_REYNOLDS_NUMBER:
    def part_reynolds_number():
        # inputs
        u_bar = [2.30, 1.97, 2.20]
        d_bar = [0.0158 for i in range(3)]
        nu_bar = [15.34e-6 for i in range(3)]
        sigma_U = [0.01 for i in range(3)]
        sigma_d = [0 for i in range(3)]

        # calculations
        re_bar = list()
        sigma_Ud = list()
        sigma_Ud_v = list()
        for i in range(3):
            re_bar.append(u_bar[i] * d_bar[i] / nu_bar[i])
            sigma_Ud.append(math.sqrt(
                sigma_U[i] ** 2 * d_bar[i] ** 2 +
                sigma_d[i] ** 2 * u_bar[i] ** 2
            ))
            sigma_Ud_v.append(sigma_Ud[i] / nu_bar[i])

        # outputs
        print("re_bar: ", re_bar)
        print("sigma_Ud_v: ", sigma_Ud_v)

    part_reynolds_number()

if PART_NUSSELT_NUMBER:
    def part_nusselt_number():
        # inputs
        Re_bar = [2369, 2029, 2266]
        sigma_Re = [10 for i in range(3)]

        # calculations
        Nu_bar = list()
        sigma_0_174_Re_0_618 = list()
        for i in range(3):
            Nu_bar.append(0.174 * Re_bar[i] ** 0.618)
            sigma_0_174_Re_0_618.append(
                0.618 * sigma_Re[i] / Re_bar[i]
            )

        # outputs
        print("Nu_bar: ", Nu_bar)
        print("sigma_0_174_Re_0_618: ", sigma_0_174_Re_0_618)
    
    part_nusselt_number()

if PART_DRAW:
    single_pipe_re = [2369, 2029, 2266]
    single_pipe_h_experiment = [48.7, 48.6, 48.6]
    single_pipe_h_theory = [34.456, 31.310, 33.523]

    multiple_pipe_pos1_re = [4440, 4390, 5000]
    multiple_pipe_pos1_h_experiment = [58, 58, 58]
    multiple_pipe_pos1_h_theory = [78.13239, 77.57252, 84.25368]

    multiple_pipe_pos3_re = [4580, 4660, 4660]
    multiple_pipe_pos3_h_experiment = [77, 82, 78]
    multiple_pipe_pos3_h_theory = [79.68792, 80.56900, 80.56900]

    multiple_pipe_pos6_re = [4130, 4560, 4320]
    multiple_pipe_pos6_h_experiment = [88, 88, 87]
    multiple_pipe_pos6_h_theory = [74.62274, 79.46678, 76.78477]

    # draw subplot for each pipe
    fig, axs = plt.subplots(2, 2)
    fig.suptitle('h vs Reynolds Number')

    axs[0, 0].plot(single_pipe_re, single_pipe_h_experiment, 'o', label='Experiment')
    coefficients = np.polyfit(single_pipe_re, single_pipe_h_experiment, 1)
    regression_x = np.array([min(single_pipe_re), max(single_pipe_re)])
    regression_y = np.polyval(coefficients, regression_x)
    axs[0, 0].plot(regression_x, regression_y, '-', label='Experiment Regression')

    axs[0, 0].plot(single_pipe_re, single_pipe_h_theory, '.', label='Theory')
    coefficients = np.polyfit(single_pipe_re, single_pipe_h_theory, 1)
    regression_x = np.array([min(single_pipe_re), max(single_pipe_re)])
    regression_y = np.polyval(coefficients, regression_x)
    axs[0, 0].plot(regression_x, regression_y, '--', label='Theory Regression')

    axs[0, 0].set_title('Single Pipe')
    axs[0, 0].set_xlabel('Reynolds No.')
    axs[0, 0].set_ylabel('h (W/m^2K)')
    axs[0, 0].legend()

    axs[0, 1].plot(multiple_pipe_pos1_re, multiple_pipe_pos1_h_experiment, 'o', label='Experiment')
    coefficients = np.polyfit(multiple_pipe_pos1_re, multiple_pipe_pos1_h_experiment, 1)
    regression_x = np.array([min(multiple_pipe_pos1_re), max(multiple_pipe_pos1_re)])
    regression_y = np.polyval(coefficients, regression_x)
    axs[0, 1].plot(regression_x, regression_y, '-', label='Experiment Regression')

    axs[0, 1].plot(multiple_pipe_pos1_re, multiple_pipe_pos1_h_theory, '.', label='Theory')
    coefficients = np.polyfit(multiple_pipe_pos1_re, multiple_pipe_pos1_h_theory, 1)
    regression_x = np.array([min(multiple_pipe_pos1_re), max(multiple_pipe_pos1_re)])
    regression_y = np.polyval(coefficients, regression_x)
    axs[0, 1].plot(regression_x, regression_y, '--', label='Theory Regression')

    axs[0, 1].set_title('Multiple Pipe (1st row)')
    axs[0, 1].set_xlabel('Reynolds No.')
    axs[0, 1].set_ylabel('h (W/m^2K)')
    axs[0, 1].legend()

    axs[1, 0].plot(multiple_pipe_pos3_re, multiple_pipe_pos3_h_experiment, 'o', label='Experiment')
    coefficients = np.polyfit(multiple_pipe_pos3_re, multiple_pipe_pos3_h_experiment, 1)
    regression_x = np.array([min(multiple_pipe_pos3_re), max(multiple_pipe_pos3_re)])
    regression_y = np.polyval(coefficients, regression_x)
    axs[1, 0].plot(regression_x, regression_y, '-', label='Experiment Regression')

    axs[1, 0].plot(multiple_pipe_pos3_re, multiple_pipe_pos3_h_theory, '.', label='Theory')
    coefficients = np.polyfit(multiple_pipe_pos3_re, multiple_pipe_pos3_h_theory, 1)
    regression_x = np.array([min(multiple_pipe_pos3_re), max(multiple_pipe_pos3_re)])
    regression_y = np.polyval(coefficients, regression_x)
    axs[1, 0].plot(regression_x, regression_y, '--', label='Theory Regression')

    axs[1, 0].set_title('Multiple Pipe (3rd row)')
    axs[1, 0].set_xlabel('Reynolds No.')
    axs[1, 0].set_ylabel('h (W/m^2K)')
    axs[1, 0].legend()

    axs[1, 1].plot(multiple_pipe_pos6_re, multiple_pipe_pos6_h_experiment, 'o', label='Experiment')
    coefficients = np.polyfit(multiple_pipe_pos6_re, multiple_pipe_pos6_h_experiment, 1)
    regression_x = np.array([min(multiple_pipe_pos6_re), max(multiple_pipe_pos6_re)])
    regression_y = np.polyval(coefficients, regression_x)
    axs[1, 1].plot(regression_x, regression_y, '-', label='Experiment Regression')

    axs[1, 1].plot(multiple_pipe_pos6_re, multiple_pipe_pos6_h_theory, '.', label='Theory')
    coefficients = np.polyfit(multiple_pipe_pos6_re, multiple_pipe_pos6_h_theory, 1)
    regression_x = np.array([min(multiple_pipe_pos6_re), max(multiple_pipe_pos6_re)])
    regression_y = np.polyval(coefficients, regression_x)
    axs[1, 1].plot(regression_x, regression_y, '--', label='Theory Regression')
    
    axs[1, 1].set_title('Multiple Pipe (6th row)')
    axs[1, 1].set_xlabel('Reynolds No.')
    axs[1, 1].set_ylabel('h (W/m^2K)')
    axs[1, 1].legend()

    plt.show()
