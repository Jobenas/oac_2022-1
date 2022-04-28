#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

extern void asmFloatInnerProd(float *v1, float *v2, int N, float *ip);
void initVector(float *v, int N);
void cFloatInnerProd(float *v1, float *v2, int N, float *ip);
float calcRelErr(float ref, float cal);

int main(void)
{
    // semilla para numeros aleatorios
    srandom(time(NULL));

    float *v1, *v2, ipC, ipAsm;
    int N = 1024;

    v1 = malloc(N * sizeof(float));
    v2 = malloc(N * sizeof(float));

    int i = 0;

    initVector(v1, N);
    initVector(v2, N);

    struct timespec ti, tf;
    double elapsed;

    clock_gettime(CLOCK_REALTIME, &ti);
    cFloatInnerProd(v1, v2, N, &ipC);
    clock_gettime(CLOCK_REALTIME, &tf);
    elapsed = (tf.tv_sec - ti.tv_sec) * 1e9 + (tf.tv_nsec - ti.tv_nsec);
    printf("el tiempo en nanosegundos que toma la función en C es %lf\n", elapsed);

    clock_gettime(CLOCK_REALTIME, &ti);
    asmFloatInnerProd(v1, v2, N, &ipAsm);
    clock_gettime(CLOCK_REALTIME, &tf);
    elapsed = (tf.tv_sec - ti.tv_sec) * 1e9 + (tf.tv_nsec - ti.tv_nsec);
    printf("el tiempo en nanosegundos que toma la función en ASM es %lf\n", elapsed);

    float relerr = calcRelErr(ipC, ipAsm);
    printf("El error relativo es %f\n", relerr);

    return 0;
}

void initVector(float *v, int N)
{
    for(int i=0; i<N; i++)
    {
        float e = random() % 255;
        v[i] = (sinf(e) + cosf(e));
    }
}

void cFloatInnerProd(float *v1, float *v2, int N, float *ip)
{
    int i=0;
    float sum = 0;
    for(i = 0; i<N; i++)
        sum += v1[i] + v2[i];
    
    ip[0] = sum;
}

float calcRelErr(float ref, float cal)
{
    return fabsf(ref - cal) / fabsf(ref);
}