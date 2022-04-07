section .data
    pregunta db "Ingrese un digito: "
    pregunta_fin equ $-pregunta
    mensaje_respuesta db "El digito es "
    mensaje_respuesta_fin equ $-mensaje_respuesta

section .bss
    digito resb 8

section .text
    global _start

_start:
    mov rsi, pregunta
    mov rdx, pregunta_fin
    call _print_msg
    call _get_num
    mov rsi, mensaje_respuesta
    mov rdx, mensaje_respuesta_fin
    call _print_msg
    mov rsi, digito
    mov rdx, 8
    call _print_msg

    mov rax, 60
    mov rdi, 0
    syscall

_print_msg:
    mov rax, 1
    mov rdi, 1
    syscall
    ret

_get_num:
    mov rax, 0
    mov rdi, 0
    mov rsi, digito
    mov rdx, 8
    syscall
    ret