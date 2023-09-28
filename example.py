from debugger import debugger, canyoubaidu

@canyoubaidu
@debugger
def faulty_function():
    return 1 / 0

faulty_function()