import numpy as np
import matplotlib.pyplot as plt

def analyze_pmos():
    # 1. TRANSFER CHARACTERISTICS
    data_trans = np.loadtxt('pmos_transfer_data.txt')
    
    # We take the absolute values of voltage and current for easier plotting
    vgs = np.abs(data_trans[:, 0])
    id_trans = np.abs(data_trans[:, 1])

    # Calculate Transconductance (gm)
    gm = np.gradient(id_trans, vgs)
    max_gm_idx = np.argmax(gm)
    max_gm = gm[max_gm_idx]
    vgs_max_gm = vgs[max_gm_idx]
    id_max_gm = id_trans[max_gm_idx]

    # Extrapolate |Vt|
    abs_vt = vgs_max_gm - (id_max_gm / max_gm)

    # Calculate Subthreshold Swing (SS)
    log_id = np.log10(id_trans + 1e-15)
    log_slope = np.gradient(log_id, vgs)
    max_log_slope = np.max(log_slope)
    ss = (1 / max_log_slope) * 1000 # Convert to mV/dec

    print(f"\n--- PMOS Extracted Parameters ---")
    print(f"Absolute Threshold Voltage (|Vt|) : {abs_vt:.3f} V")
    print(f"Subthreshold Swing (SS)           : {ss:.2f} mV/dec")
    print(f"---------------------------------\n")

    # 2. OUTPUT CHARACTERISTICS
    data_out = np.loadtxt('pmos_output_data.txt')
    vds = np.abs(data_out[:, 0])
    id_out = np.abs(data_out[:, 1])

    num_vds_points = 181
    num_vgs_steps = 5
    vgs_labels = ['-0.6V', '-0.9V', '-1.2V', '-1.5V', '-1.8V']
    
    vds_reshaped = vds.reshape(num_vgs_steps, num_vds_points)
    id_reshaped = id_out.reshape(num_vgs_steps, num_vds_points)

    # 3. PLOTTING
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))

    # Plot 1: Transfer (Linear)
    axes[0].plot(vgs, id_trans, color='blue', linewidth=2)
    vgs_tangent = np.linspace(abs_vt, 1.8, 50)
    id_tangent = max_gm * (vgs_tangent - abs_vt)
    axes[0].plot(vgs_tangent, id_tangent, 'r--', label=f'Extrapolated $|V_t|$ = {abs_vt:.2f}V')
    axes[0].set_title('PMOS Transfer Characteristic')
    axes[0].set_xlabel('$|V_{gs}|$ (V)')
    axes[0].set_ylabel('$|I_d|$ (A)')
    axes[0].legend()
    axes[0].grid(True, linestyle='--', alpha=0.7)

    # Plot 2: Transfer (Log)
    axes[1].semilogy(vgs, id_trans, color='red', linewidth=2)
    axes[1].set_title(f'Subthreshold (SS = {ss:.1f} mV/dec)')
    axes[1].set_xlabel('$|V_{gs}|$ (V)')
    axes[1].set_ylabel('$|I_d|$ (A) [Log]')
    axes[1].grid(True, linestyle='--', alpha=0.7)

    # Plot 3: Output Characteristics
    for i in range(num_vgs_steps):
        axes[2].plot(vds_reshaped[i], id_reshaped[i], linewidth=2, label=f'$V_{{gs}}$ = {vgs_labels[i]}')
    
    axes[2].set_title('PMOS Output Characteristics')
    axes[2].set_xlabel('$|V_{ds}|$ (V)')
    axes[2].set_ylabel('$|I_d|$ (A)')
    axes[2].legend()
    axes[2].grid(True, linestyle='--', alpha=0.7)

    plt.tight_layout()
    plt.savefig('pmos_full_characterization.png', dpi=300)
    print("Plots saved as 'pmos_full_characterization.png'")

if __name__ == "__main__":
    analyze_pmos()