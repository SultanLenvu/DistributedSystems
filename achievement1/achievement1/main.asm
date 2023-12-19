;
; achievement1.asm
;
; Created: 17.12.2023 14:30:30
; Author : Sultan Lenvu
;

.include "program_memory.asm" ; Подключение файла с разметкой памяти программ
.include "interruptions.asm" ; Подключение файла с обработчиками прерываний 

.def temp = r16       ; Временный регистр

; Константы
.equ TIMER1_INTERVAL = 7812  ; Интервал для TIMER1 (1 секунда)
.equ TIMER2_INTERVAL = 15625  ; Интервал для TIMER2 (2 секунды)
TIMER1_STR: .db "ping", 13, 10, 0  ; Строка для вывода при срабатывании TIMER1
TIMER2_STR: .db "pong", 13, 10, 0  ; Строка для вывода при срабатывании TIMER2

main:
ldi temp, high(RAMEND)  ; Инициализация указателя стека
    out SPH, temp
    ldi temp, low(RAMEND)
    out SPL, temp

    ; Настройка USART
    ldi temp, (1 << URSEL) | (1 << UCSZ1) | (1 << UCSZ0)  ; 8 бит данных, 1 стоп-бит, без контроля четности
    out UCSRC, temp
    ldi temp, (1 << RXEN) | (1 << TXEN)  ; Включение приемника и передатчика USART
    out UCSRB, temp
    ldi temp, 16  ; Установка скорости передачи USART на 9600 бод
    out UBRRH, temp
    ldi temp, 0
    out UBRRL, temp

    ; Настройка TIMER1
    ldi temp, (1 << TOIE1) | (1 << CS12) | (1 << CS10)  ; Включение прерывания по переполнению, предделитель 1024
    out TCCR1B, temp
    ldi temp, high(TIMER1_INTERVAL)  ; Загрузка значения для интервала TIMER1
    out OCR1AH, temp  ; Настройка регистра сравнения A
    ldi temp, low(TIMER1_INTERVAL)
    out OCR1AL, temp

    ; Настройка TIMER2
    ldi temp, (1 << TOIE2) | (1 << CS22) | (1 << CS21) | (1 << CS20)  ; Включение прерывания по переполнению, предделитель 1024
    out TCCR2, temp
    ldi temp, high(TIMER2_INTERVAL)  ; Загрузка значения для интервала TIMER2
    out OCR2, temp  ; Настройка регистра сравнения

    sei  ; Разрешение глобальных прерываний

main_loop:
    rjmp main_loop  ; Бесконечный цикл

; Подпрограмма для отправки строки через USART
usart_send_string:
    push r16  ; Сохранение регистра
    push r17  ; Сохранение регистра

    loop:
        lpm r16, Z+  ; Загрузка символа из памяти программы
        cp r16, r1   ; Сравнение с нулем (конец строки)
        brne send_char         pop r17  ; Восстановление регистра
        pop r16  ; Восстановление регистра
        ret

    send_char:
        out UDR, r16  ; Отправка символа через USART
        sbic UCSRA, UDRE  ; Проверка готовности передатчика
        rjmp send_char  ; Ожидание готовности

        rjmp loop  ; Переход к следующему символу


