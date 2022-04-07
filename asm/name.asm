section .data
    pregunta db "Cual es tu nombre? "
    pregunta_fin equ $-pregunta
    saludo db "Hola, "
    saludo_fin equ $-saludo    

section .bss
    nombre resb 16

section .text
    global _start

_start:
    ; Imprimimos pregunta
    mov rax, 1
    mov rdi, 1
    mov rsi, pregunta
    mov rdx, pregunta_fin
    syscall

    ; Esperamos ingreso de nombre
    mov rax, 0
    mov rdi, 0
    mov rsi, nombre
    mov rdx, 16
    syscall

    mov rax, 1
    mov rdi, 1
    mov rsi, saludo
    mov rdx, saludo_fin
    syscall

    mov rax, 1
    mov rdi, 1
    mov rsi, nombre
    mov rdx, 16
    syscall

end:
    mov rax, 60
    mov rdi, 0
    syscall