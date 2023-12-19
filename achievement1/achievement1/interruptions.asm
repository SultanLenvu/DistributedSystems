/*
 * interruptions.asm
 *
 *  Created: 17.12.2023 14:44:52
 *   Author: Sultan
 */ 

 timer1_interrupt:
	ldi temp, low(TIMER1_STR)  ; Загрузка адреса строки TIMER1_STR
    rjmp usart_send_string  ; Отправка строки через USART
    reti

timer2_interrupt:
    ldi temp, low(TIMER2_STR)  ; Загрузка адреса строки TIMER2_STR
    rjmp usart_send_string  ; Отправка строки через USART
    reti