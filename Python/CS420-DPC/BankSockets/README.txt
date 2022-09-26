Sockets Homework:

Use the attached files to update the previous bank_threading.py example into a sockets program.

The Bank class will now be its own process, and each Branch object will exist in its own process.

The Bank and Branch processes will communicate through sockets (TCP). As mentioned in class, we'll use TCP for this assigmnet since banking data needs the guarantee of delivery ( what UDP cannot provide). 

Start at least 2 Branch processes. I would prefer you add a command line argument that can adjust how many Branch processes get started, but I wont require that for this homework.

All Branch processes should communicate with the Bank process to confirm a transaction. 

For example. a Branch will send a message similar to --> {'branch_id':1, 'action':'withdraw', 'amount':100} 

The Bank will receive this message, determine if the bank has the money to make this transaction, and then respond to the client in a similar fashion with saying whether the transaction was confirmed or denied.

Have a Branch send a request ( randomoly choose deposit or withdraw) every 1-3 seconds

Run the Bank process for 30 seconds and let the Branch processes know when it's time to close

Hint: Use Python dictionaries (JSON) messages for communication.