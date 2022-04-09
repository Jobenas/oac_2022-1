section .data
    num db 6
    nl db 10

section .text
    global _start

_start:

    ; mov r8, num     ; muevo a r8 direccion de memoria
    mov r9, [num]   ; muevo contenido de direccion de memoria a r9
    add r9, 48      ; codigo de '0' en ascii
    mov [num], r9

    mov rax, 1
    mov rdi, 1
    mov rsi, num
    mov rdx, 1
    syscall

    mov rax, 1
    mov rdi, 1
    mov rsi, nl
    mov rdx, 1
    syscall

    mov rax, 60
    mov rdi, 0
    syscall
