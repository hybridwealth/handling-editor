# Improved function to modify handling parameters for more realistic driving and braking
def modify_handling_line_safe(line):
    parts = line.split()
    if len(parts) < 20 or not parts[1].replace('.', '', 1).isdigit():
        return line  # Not a valid handling line or not enough parts

    try:
        # Extract relevant parameters and convert them to floats
        mass = float(parts[1])
        drag_mult = float(parts[2])
        traction_mult = float(parts[7])
        suspension_force = float(parts[11])
        brake_deceleration = float(parts[16])
        brake_bias = float(parts[17])

        # Modify parameters for realism
        mass *= 1.1  # Slightly increase mass
        drag_mult *= 1.1  # Adjust drag multiplier
        traction_mult *= 1.2  # Increase traction
        suspension_force *= 1.2  # Stiffen suspension
        brake_deceleration *= 0.8  # Reduce brake deceleration
        brake_bias = 0.5  # Set brake bias to even distribution

        # Update the parts with new values
        parts[1] = f"{mass:.1f}"
        parts[2] = f"{drag_mult:.1f}"
        parts[7] = f"{traction_mult:.2f}"
        parts[11] = f"{suspension_force:.1f}"
        parts[16] = f"{brake_deceleration:.2f}"
        parts[17] = f"{brake_bias:.2f}"

        return " ".join(parts) + "\n"
    except (ValueError, IndexError):
        # In case of any conversion error, return the original line
        return line

# Apply modifications to each handling line safely
modified_handling_data = []
for line in handling_data:
    if line.strip().startswith(';') or not line.strip():
        # Keep comments and empty lines unchanged
        modified_handling_data.append(line)
    else:
        modified_handling_data.append(modify_handling_line_safe(line))

# Save the modified data to a new handling.cfg file
modified_file_path = '/mnt/data/modified_handling.cfg'
with open(modified_file_path, 'w') as modified_file:
    modified_file.writelines(modified_handling_data)

modified_file_path
