def plot_params(axis):
    axs = axis
    axs.grid(b=True, axis='both', which='major', linestyle='--', linewidth=1.5)
    axs.minorticks_on()
    axs.grid(b=True, which='minor', axis='both', linestyle=':', linewidth=1.0)
    axs.tick_params(axis='both', labelsize=16, length=6, which='major',
                    width=1.5)
    axs.tick_params(axis='both', length=3, which='minor', width=1.0)
    axs.set_axisbelow(True)
