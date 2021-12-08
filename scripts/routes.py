import os

work_directory = os.getcwd()

if os.path.basename(work_directory) == 'scripts':
    work_directory = os.path.normpath(os.getcwd() + os.sep + os.pardir)


# пути для узлов
start_storage = f'{work_directory}\\factory\start_storage\\'
end_storage = f'{work_directory}\\factory\end_storage\\'
cocoa_oven = f'{work_directory}\\factory\cocoa_oven\\'
fat_oven = f'{work_directory}\\factory\\fat_oven\\'
candies = f'{work_directory}\\factory\\candies\\'
chocolate_mass = f'{work_directory}\\factory\\chocolate_mass\\'
dough = f'{work_directory}\\factory\\dough\\'
filling = f'{work_directory}\\factory\\filling\\'
candies_fridge = f'{work_directory}\\factory\\fridge\candies_fridge\\'
chocolate_fridge = f'{work_directory}\\factory\\fridge\chocolate_fridge\\'
waffles_fridge = f'{work_directory}\\factory\\fridge\waffles_fridge\\'
candies_package = f'{work_directory}\\factory\package\candies_package\\'
chocolate_package = f'{work_directory}\\factory\package\chocolate_package\\'
waffels_package = f'{work_directory}\\factory\package\waffels_package\\'
whipping_chocolate = f'{work_directory}\\factory\\whipping_chocolate\\'
chocolate_bar = f'{work_directory}\\factory\\chocolate_bar\\'
chocolate_forming = f'{work_directory}\\factory\\chocolate_forming\\'
furnace = f'{work_directory}\\factory\\furnace\\'
slicing = f'{work_directory}\\factory\\slicing\\'
filling_preparation = f'{work_directory}\\factory\\filling_preparation\\'


def test():
    print("working directory is ", work_directory)
    print("start_storage directory is ", start_storage)

