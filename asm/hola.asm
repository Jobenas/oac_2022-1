; Este es un comentario
section .data
; ****************************************
; Variables
; ****************************************
texto db "Hola Intel de 64 bits",10
fin equ $-texto

section .text
    global _start
_start:
    ; Imprimimos en el terminal el contenido de texto
    mov rax, 1
    mov rdi, 1
    mov rsi, texto  ; este es el puntero del inicio de la cadena
    mov rdx, fin    ; esta es la longitud de la cadena
    syscall
end:
    ; Salimos del programa e indicamos al sistema operativo que libere recursos
    mov rax, 60
    mov rdi, 0
    syscall
