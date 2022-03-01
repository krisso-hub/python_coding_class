''' A demo of Employee Production worker using
    Employee class and Production Worker subclass
    Author: Ndubuisi    Date: 02/28/22022
'''

import Employee_ProductionWorker
def main():
    # create a production worker object
    active_worker = Employee_ProductionWorker.ProductionWorker('John', 'id010', 2, 15.50)
    # display active worker datat after initialization
    print('______Employee____1')
    print('Name      ', active_worker.get_name())
    print('number    ', active_worker.get_number())
    print('shift     ', active_worker.get_shift())
    print('rate      ', active_worker.get_hrRate())
    # test mutator method
    active_worker.set_name('Mark')
    active_worker.set_number('id011')
    active_worker.set_shift(1)
    active_worker.set_hrRate(14.40)
    # display active working after employing addtional worker
    print('______Employee____2')
    print('Name      ', active_worker.get_name())
    print('number    ', active_worker.get_number())
    print('shift     ', active_worker.get_shift())
    print('rate      ', active_worker.get_hrRate())

main()