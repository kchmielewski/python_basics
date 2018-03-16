#include <stdio.h>
#include <math.h>
#include <string.h>

void do_the_things_in32(FILE* file);
void do_the_things_in64(FILE* file);
int binary(int exponent);
int binary64(int exponent);
int power_of_2;
int bits, bin;
int positive_number;
int integer_of_number;
int iterations;
float fraction;
float number;
double number64;
double fraction64;

int main(int argcount, char *argv[]) {
FILE* file = fopen (argv[1], "r");
  if(argcount == 3)
  {
    if (strcmp(argv[2], "32") == 0)
    {
      printf("Wybrana konwersja: 32 bitowa\n");
      do_the_things_in32(file);
    }
    else if((strcmp(argv[2], "64") == 0))
    {
      printf("Wybrana konwersja: 64 bitowa\n");
      do_the_things_in64(file);
    }
    else
    {
      printf("Bledny kod wprowadzania, zamykanie programu...\n");
    }
  }
  else
  {
    printf("Musisz podać 2 argumenty, zeby program dzialal- nazwe pliku txt oraz ilosc bitow. zamykanie programu...\n" );
  }
}

void check_if_positive_number(){
  if(number > 0 || number64 > 0)
  {
    printf("0");
    positive_number = 0;
  }
  else
  {
    positive_number = 1;
    printf("1");
  }
}
void check_if_positive_number64(){
  if(number64 > 0)
  {
    printf("0");
    positive_number = 0;
  }
  else
  {
    printf("1");
    positive_number = 1;
  }
}

float divide_by_powers()
{
  return number/powf(2,power_of_2);
}

double divide_by_powers64()
{
  return number64/pow(2,power_of_2);
}

void findexponent()
{
  power_of_2 = -1025;
  if(positive_number == 0)
    while(divide_by_powers()<=1 || divide_by_powers()>=2)
    {
      power_of_2+=1;
    }
  else
    while(divide_by_powers()>=-1 || divide_by_powers()<=-2 || divide_by_powers() == 0)
    {
      power_of_2+=1;
    }
  int exponent = 127+power_of_2;
  binary(exponent);
}

void findexponent64()
{
  power_of_2 = -1024;
  if(positive_number == 0)
    while(divide_by_powers64()<=1 || divide_by_powers64()>=2)
    {
      power_of_2+=1;
    }
  else
    while(divide_by_powers64()>=-1 || divide_by_powers64()<-2)
    {
      power_of_2+=1;
    }

  int exponent = 1023+power_of_2;
  binary64(exponent);
}

int binary(int exponent){
  for (int bits = 7; bits >= 0; bits--)
  {
    bin = exponent >> bits;

    if (bin & 1)
      printf("1");
    else
      printf("0");
  }
  return 0;
}

int binary64(int exponent){
  for (int bits = 10; bits >= 0; bits--)
  {
    bin = exponent >> bits;
    if (bin & 1)
      printf("1");
    else
      printf("0");
  }
  return 0;
}

void findfraction()
{
  integer_of_number = (divide_by_powers());
  float float_of_number = (divide_by_powers());
  fraction = float_of_number - integer_of_number;
  iterations = 1;
  if(fraction>0)
  {
    while(fraction != 1)
    {
      fraction = fraction * 2;
      if(fraction>=1)
      {
        printf("1");
        fraction = fraction-1;
      }
      else
      {
      printf("0");
      }
      iterations+=1;
      if(iterations==24)
      {
        break;
      }
    }
    if(iterations<24)
    {
      printf("1");
      while(iterations != 24)
      {
        printf("0");
        iterations+=1;
      }
    }
  }
  else
  {
  while(fraction != -1)
  {
    fraction = fraction * 2;
    if(fraction<=-1)
    {
      printf("1");
      fraction = fraction + 1;
    }
    else
    {
    printf("0");
    }
    iterations += 1;
    if(iterations == 24)
    {
      break;
    }
  }
  if(iterations < 24)
  {
    printf("1");
    while(iterations != 24)
    {
      printf("0");
      iterations += 1;
    }
  }
}
printf("\n");
}


void findfraction64()
{
  integer_of_number = (divide_by_powers64());
  double double_of_number = (divide_by_powers64());
  fraction64 = double_of_number - integer_of_number;
  iterations = 1;
  if(fraction64>0)
  {
    while(fraction64 != 1)
    {
      fraction64 = fraction64 * 2;
      if(fraction64>=1)
      {
        printf("1");
        fraction64 = fraction64-1;
      }
      else
      {
      printf("0");
      }
      iterations+=1;
      if(iterations==53)
      {
        break;
      }
    }
    if(iterations<53)
    {
      printf("1");
      while(iterations != 53)
      {
        printf("0");
        iterations+=1;
      }
    }
  }
  else
  {
  while(fraction64 != -1)
  {
    fraction64 = fraction64 * 2;
    if(fraction64<=-1)
    {
      printf("1");
      fraction64 = fraction64 + 1;
    }
    else
    {
    printf("0");
    }
    iterations += 1;
    if(iterations == 53)
    {
      break;
    }
  }
  if(iterations < 53)
  {
    printf("1");
    while(iterations != 53)
    {
      printf("0");
      iterations += 1;
    }
  }
}
printf("\n");
}

void do_the_things_in32(FILE* file)
  {
    if(fscanf (file, "%f", &number)== 1)
    {
      printf("%f\n",number);
      check_if_positive_number();
      findexponent();
      findfraction();
    }
    else
    {
      fscanf(file, "%*[^ %\n]");
      printf("\nInvalid type!\n");
    }
    while (!feof(file))
    {
      if(fscanf (file, "%f", &number)== 1)
      {
        printf("%f\n",number);
        check_if_positive_number();
        findexponent();
        findfraction();
      }
      else
      {
        if(!feof(file))
        {
          fscanf(file, "%*[^ %\n]");
          printf("Invalid type!\n");
        }
        else
        {
          printf("End of the file\n");
          break;
        }
      }
    }
  fclose (file);
  }

  void do_the_things_in64(FILE* file)
    {
      if(fscanf (file, "%lf", &number64)== 1)
      {
        printf("%lf\n",number64);
        check_if_positive_number64();
        findexponent64();
        findfraction64();
      }
      else
      {
        fscanf(file, "%*[^ %\n]");
        printf("\nInvalid type!\n");
      }
      while (!feof(file))
      {

        if(fscanf (file, "%lf", &number64)== 1)
        {
          printf("%lf\n",number64);
          check_if_positive_number64();
          findexponent64();
          findfraction64();
        }
        else
        {
          if(!feof(file))
          {
            fscanf(file, "%*[^ %\n]");
            printf("Invalid type!\n");
          }
          else
          {
            printf("End of the file\n");
            break;
          }
        }
      }
    fclose (file);
    }
