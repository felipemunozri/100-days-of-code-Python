# set callback for window close
window.protocol("WM_DELETE_WINDOW", save_files)


# window close callback function

def save_files():
    # Prompt user for confirmation
    if messagebox.askokcancel(title="Goodbye", message="Update dictionary based on this session?"):

    # File saving logic goes here.
    # Dict updating is in a separate function

    window.destroy()
