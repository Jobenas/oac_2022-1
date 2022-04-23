section .data
    operando1 db "Ingrese primer operando: "
    operando1_len equ $-operando1
    operando2 db "Ingrese segundo operando: "
    operando2_len equ $-operando2
    operacion db "Seleccione operación (1 -> suma, 2 -> resta, 3 -> mult): "
    operacion_len equ $-operacion 

    msje_suma db "Seleccionó la operación de suma",10
    msje_suma_len equ $-msje_suma
    msje_resta db "Seleccionó la operación de resta",10
    msje_resta_len equ $-msje_resta
    msje_mult db "Seleccionó la operación de multiplicación",10
    msje_mult_len equ $-msje_mult
    msje_incorrecto db "No seleccionó ninguna opción válida",10
    msje_incorrecto_len equ $-msje_incorrecto

    msje_resultado db "El resultado de la operación es: "
    msje_resultado_len equ $-msje_resultado

    nl db 10

section .bss
    op1 resb 5
    op2 resb 5
    op resb 5
    resultado resb 5

section .text
    global _start

_start:
    ; solicitamos el primer operando
    mov rax, 1
    mov rdi, 1
    mov rsi, operando1
    mov rdx, operando1_len
    syscall

    ; guardamos el primer operando
    mov rax, 0
    mov rdi, 0
    mov rsi, op1
    mov rdx, 5
    syscall

    ; solicitamos el segundo operando
    mov rax, 1
    mov rdi, 1
    mov rsi, operando2
    mov rdx, operando2_len
    syscall

    ; guardamos el segundo operando
    mov rax, 0
    mov rdi, 0
    mov rsi, op2
    mov rdx, 5
    syscall

    ; solicitamos la operacion
    mov rax, 1
    mov rdi, 1
    mov rsi, operacion
    mov rdx, operacion_len
    syscall

    ; guardamos la operacion
    mov rax, 0
    mov rdi, 0
    mov rsi, op
    mov rdx, 5
    syscall

    ; validando las opciones
    mov r9b, byte [op]
    cmp r9b, 49
    je suma
    cmp r9b, 50
    je resta
    cmp r9b, 51
    je multiplica
    jmp opcion_incorrecta


suma:
    ; imprimimos mensaje de seleccion
    mov rax, 1
    mov rdi, 1
    mov rsi, msje_suma
    mov rdx, msje_suma_len
    syscall
    
    mov r8, [op1]
    sub r8, 48
    mov r9, [op2]
    sub r9, 48
    add r9, r8
    add r9, 48
    mov [resultado], r9

    mov rax, 1
    mov rdi, 1
    mov rsi, msje_resultado
    mov rdx, msje_resultado_len
    syscall 

    mov rax, 1
    mov rdi, 1
    mov rsi, resultado
    mov rdx, 1
    syscall

    mov rax, 1
    mov rdi, 1
    mov rsi, nl
    mov rdx, 1
    syscall

    jmp _fin

resta:
    ; imprimimos mensaje de seleccion
    mov rax, 1
    mov rdi, 1
    mov rsi, msje_resta
    mov rdx, msje_resta_len
    syscall
    
    mov r8, [op1]
    sub r8, 48
    mov r9, [op2]
    sub r9, 48
    sub r8, r9
    add r8, 48
    mov [resultado], r8

    mov rax, 1
    mov rdi, 1
    mov rsi, msje_resultado
    mov rdx, msje_resultado_len
    syscall 

    mov rax, 1
    mov rdi, 1
    mov rsi, resultado
    mov rdx, 1
    syscall

    mov rax, 1
    mov rdi, 1
    mov rsi, nl
    mov rdx, 1
    syscall

    jmp _fin

multiplica:
    ; imprimimos mensaje de seleccion
    mov rax, 1
    mov rdi, 1
    mov rsi, msje_mult
    mov rdx, msje_mult_len
    syscall
    
    mov r8, [op1]
    sub r8, 48
    
    mov r9, [op2]
    sub r9, 48

    mov rax, r8
    mul r9
    mov r9, rax
    
    add r9, 48
    mov [resultado], r9

    mov rax, 1
    mov rdi, 1
    mov rsi, msje_resultado
    mov rdx, msje_resultado_len
    syscall 

    mov rax, 1
    mov rdi, 1
    mov rsi, resultado
    mov rdx, 1
    syscall

    mov rax, 1
    mov rdi, 1
    mov rsi, nl
    mov rdx, 1
    syscall

    jmp _fin

opcion_incorrecta:
    ; imprimimos mensaje de seleccion
    mov rax, 1
    mov rdi, 1
    mov rsi, msje_incorrecto
    mov rdx, msje_incorrecto_len
    syscall

    ; jmp _fin

_fin:
    mov rax, 60
    mov rdi, 0
    syscall
    