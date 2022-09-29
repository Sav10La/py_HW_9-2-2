import user_interface as ui
import logger as lg
import control as cl


lg.logging.info('Start')
cl.init_data_base('base_phone.csv')
ui.ls_menu()