section .data
    hello db "Hello World",10
    hello_end equ $-hello

section .text
    global _start

_start:
    mov rax, 1
    mov rdi, 1
    mov rsi, hello
    mov rdx, hello_end
    syscall

    mov rax, 60
    mov rdi, 0
    syscall