KPU example
=====
20 classes recognition.

SDK v0.5.3 or later.

added UART communication 

char data[4];
int n;
n = sprintf(data, "%d\n", class);
uart_send_data(UART_NUM, &data, 4);
