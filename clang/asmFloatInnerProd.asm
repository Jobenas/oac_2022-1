global asmFloatInnerProd
section .text

asmFloatInnerProd:
    ; inicializacion de registros que se van a usar en calculos
    xorpd xmm0, xmm0    
    xorpd xmm1, xmm1
    xorpd xmm2, xmm2    ; sum
    cmp rdx, 0
    je done

next:
    movss xmm0, [rdi]       ; v1[i]
    movss xmm1, [rsi]       ; v2[i]
    mulss xmm0, xmm1
    addss xmm2, xmm0
    ; Desplazar indice una posicion adicional
    add rdi, 4
    add rsi, 4
    ; evaluamos si debe terminar el bucle
    sub rdx, 1
    jnz next

done:
    movss [rcx], xmm2
    ret