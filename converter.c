#include <stdio.h>
int number, bits, bin;
int binary32bit();
int binary16bit();
void read_numbers_from_file_and_convert(const char* file_name);
void run_converting_functions();
void check_if_not_number();

int main()
{
  read_numbers_from_file_and_convert("liczby_tekstowe.txt");
}

void read_numbers_from_file_and_convert(const char* file_name)
{

    FILE* file = fopen (file_name, "r");

    if(fscanf (file, "%d", &number)== 1)
    {
      run_converting_functions();
    }
    else
    {
      fscanf(file, "%*[^ %\n]");
      printf("\nInvalid type!\n");
    }
      while (true)
        {
          if(fscanf (file, "%d", &number)== 1)
          {
            run_converting_functions();
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

void run_converting_functions(){
  printf ("%d\n", number);
  binary32bit();
  binary16bit();
}

int binary32bit(){
  for (bits = 31; bits >= 0; bits--)
  {
    bin = number >> bits;

    if (bin & 1)
      printf("1");
    else
      printf("0");
  }

  printf(" 32bit\n");

  return 0;
}
int binary16bit(){
  for (bits = 16; bits >= 0; bits--)
  {
    bin = number >> bits;
  if (number > 32767)
  {
    printf("This number is too large for");
    break;
  }
    if (bin & 1)
      printf("1");
    else
      printf("0");
  }

  printf(" 16bit\n");

  return 0;
}
