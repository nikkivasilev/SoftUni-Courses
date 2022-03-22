electrons = int(input())
current_shell = 1
shells = []
while True:
    if electrons > 0:
        shell_electrons = 2 * (current_shell ** 2)
        if electrons >= shell_electrons:
            shells.append(shell_electrons)
        else:
            shells.append(electrons)
        electrons -= shell_electrons
    else:
        break
    current_shell += 1

print(shells)
