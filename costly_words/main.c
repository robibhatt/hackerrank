#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

unsigned long long product(unsigned long long number1, unsigned long long number2){
  unsigned long long prime = 1000000007ULL;
  return ((number1 * number2) % prime);
} 

unsigned long long power(unsigned long long base, unsigned long long exponent){
  unsigned long long prime = 1000000007UL;
  unsigned long long a = base % prime;
  unsigned long long b = exponent % (prime - 1);
  if (b == 0)
    return 1UL;
  if (a == 0)
    return 0UL;
  if (a == 1)
    return 1UL;
  if (b == 1)
    return (a % prime);
  if (b == 2)
    return (product(a, a) % prime);
  unsigned long long temp = power(a, b/2);
  if (b % 2 == 0)
    return (product(temp, temp) % prime);
  else
    return (product(product(temp, temp), a) % prime); 

       
}

int main(){
  unsigned long long prime = 1000000007UL;
  unsigned long long d;
  scanf("%lu",&d);
  unsigned long long a[d+1];
  for(unsigned long long i = 0; i < d+1; i++){
    scanf("%lu",&a[i]);
  }
  unsigned long long t;
  scanf("%lu", &t);
  unsigned long long n,m;
  unsigned long long values[d+1];
  unsigned long long last_value;
  unsigned long long next_value;
  for(unsigned long long test = 0; test < t; test++){
    scanf("%lu", &n);
    scanf("%lu", &m);
    for(unsigned long long i = 0; i < d+1; i++){
      last_value = power(m-d+i, n);
      for(unsigned long long j = 0; j < i; j++){
	next_value = product((m - d + i) , (prime + last_value - values[j])) % prime;
	values[j] = last_value;
	last_value = next_value;
      }
      values[i] = last_value;
    }
    unsigned long long answer = 0;
    for(unsigned long long i = 0; i < d+1; i++){
      answer += product(a[i] , values[i]) % prime;
      answer = answer % prime;
    }
    printf("%lu\n", answer);
  }

  return 0;
}





